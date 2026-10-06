"""Export source-backed pin transcriptions with resumable single-read or double-read policy.

Source hashes and schema are always checked. Clean single reads export only when policy.json
selects single-read-with-checks. Existing disagreements and invalid files stay in the review
queue; they never become single-entry results. Neither mode approves electrical correctness.
"""
import argparse, hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIB = ROOT / 'library'
TRANSCRIPTIONS = ROOT / 'catalog' / 'pin-transcriptions'
CONNECTOR_ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.-]{0,40}$')
DESIGNATOR = re.compile(r'^[A-Z]{1,3}\d{1,3}$')

def fail(errors, path, message): errors.append(f'{path.relative_to(ROOT)}: {message}')
def norm(label): return re.sub(r'\s+', '', label).upper()

def load(path, records, errors, digests):
    data = json.loads(path.read_text(encoding='utf-8'))
    record = records.get(data.get('recordId'))
    if not record: fail(errors, path, 'unknown recordId'); return None
    if path.stem != data['recordId']: fail(errors, path, 'file name must match recordId')
    if data.get('status') not in ('transcribed', 'no-connector-map'): fail(errors, path, 'invalid status')
    assets = {a['file']: a['hash'] for a in record.get('assets', [])}
    images = {}
    for image in data.get('images', []):
        if assets.get(image.get('file')) != image.get('sha256'): fail(errors, path, f"image {image.get('file')} is not a hashed asset of this record"); continue
        if not re.fullmatch(r'media/[a-f0-9]{64}\.[a-z0-9]{2,5}', image['file']): fail(errors, path, 'invalid source image path'); continue
        if image['file'] not in digests:
            with (LIB / image['file']).open('rb') as stream: digests[image['file']] = hashlib.file_digest(stream, 'sha256').hexdigest()
        if digests[image['file']] != image['sha256']: fail(errors, path, f"hash mismatch for {image['file']}")
        images[image['file']] = image['sha256']
    if not images: fail(errors, path, 'no valid source images')
    ids = set()
    for c in data.get('connectors', []):
        where = f"connector {c.get('id')}"
        if not isinstance(c.get('id'), str) or not CONNECTOR_ID.match(c['id']) or c['id'] in ids: fail(errors, path, f'{where}: invalid or duplicate id')
        ids.add(c.get('id'))
        if c.get('image') not in images: fail(errors, path, f'{where}: image must be one of the cited images')
        if c.get('rows') not in (1, 2, 3): fail(errors, path, f'{where}: rows must be 1, 2 or 3')  # 3: servo/Gravity S-V-G rows
        pins = c.get('pins') or []
        if [p.get('position') for p in pins] != list(range(1, len(pins) + 1)): fail(errors, path, f'{where}: positions must run 1..n')
        for p in pins:
            if not isinstance(p.get('label'), str) or not p['label'].strip() or len(p['label']) > 60 or not isinstance(p.get('functions', []), list) or not all(isinstance(f, str) and len(f) <= 120 for f in p.get('functions', [])): fail(errors, path, f"{where}: invalid pin {p.get('position')}")
    if data['status'] == 'no-connector-map' and data.get('connectors'): fail(errors, path, 'no-connector-map files cannot list connectors')
    return data

OCR_BLOCKING = ('odd pin count', 'has no connectors', 'needs an explanation')
OCR_SETTLES = {'order', 'mapping', 'grouping', 'reading'}
IDENTITY = re.compile(r'different (board|product)|another (board|product)|titled|shows (a|an|the) .*(board|module|base)|not the record', re.I)
def caveats(check, categories, connectors):
    notes = ['Pin 1 end inferred by the reader'] if 'order' in categories else []
    unconfirmed = [label for c in connectors for label in check.get('connectors', {}).get(c['id'], {}).get('unconfirmed', [])]
    if unconfirmed: notes.append('Not machine-confirmed: ' + ', '.join(unconfirmed[:8]) + ('…' if len(unconfirmed) > 8 else ''))
    return notes

def single_pass_issues(data, record):
    """Structural checks are not a second reading or electrical verification."""
    issues = []
    expected = {a['file'] for a in record.get('assets', []) if a.get('type') == 'pinout image'}
    cited = {i['file'] for i in data.get('images', [])}
    if expected - cited: issues.append('Some pinout images have not been read')
    if data.get('unreadable'): issues.append('Unreadable or unlabeled positions need review')
    if data.get('uncertain'): issues.append('Reader flagged uncertainty')
    if re.search(r'\b(ambiguous|uncertain|unclear|illegible|guess(?:ed)?|assum(?:e|ed))\b', data.get('notes', ''), re.I): issues.append('Notes flag an interpretation requiring review')
    if data['status'] == 'no-connector-map':
        if not data.get('notes', '').strip(): issues.append('No-connector-map needs an explanation')
        return issues
    if not data.get('connectors'): issues.append('Transcribed record has no connectors')
    for c in data.get('connectors', []):
        if not c.get('orderNote', '').strip(): issues.append(f"{c['id']}: physical ordering is not explained")
        if not c.get('pins') or any(p['label'] == '?' for p in c['pins']): issues.append(f"{c['id']}: missing pin labels")
        if c['rows'] == 2 and len(c['pins']) % 2: issues.append(f"{c['id']}: odd pin count in a two-row connector")
    return issues

# Passes may copy the GPIO name or the silkscreen for the same pin (GPIO25 / IO25 / 25, GND / G).
ALIASES = {'G': 'GND', 'GROUND': 'GND', '5V0': '5V', '+5V': '5V', 'VBUS5V': '5V', '3.3V': '3V3', '+3V3': '3V3', '+3.3V': '3V3', '3V3V': '3V3'}
def canon(name):
    n = re.sub(r'^(GPIO|IO)(?=\d)', '', norm(name))
    return ALIASES.get(n, n)
def names(pin): return {canon(pin['label']), *(canon(f) for f in pin.get('functions', []))}
def pins_agree(pa, pb):
    # A pad both passes left unlabeled agrees; a single '?' (or one pass reading a name) does not.
    if pa['label'] == pb['label'] == '?': return True
    if '?' in (pa['label'], pb['label']): return False
    return canon(pa['label']) == canon(pb['label']) or canon(pa['label']) in names(pb) or canon(pb['label']) in names(pa)
def connectors_agree(ca, cb): return ca['rows'] == cb['rows'] and len(ca['pins']) == len(cb['pins']) and all(pins_agree(x, y) for x, y in zip(ca['pins'], cb['pins']))
FUNCTIONAL = re.compile(r'^(GPIO|IO)\d+$|^(GND|3V3|5V|VIN|VBUS|VBAT|EN|RST)$', re.I)

# Rules v3 label fixes applied in code: O/0 by context (IO12, MOSI, MTDO, LDO2, OUT, BOOT; CH0, U0TXD).
O_WORDS = [(r'^I0(?=\d)', 'IO'), (r'M0SI', 'MOSI'), (r'MIS0', 'MISO'), (r'MTD0', 'MTDO'), (r'^LD0(?=\d|$)', 'LDO'), (r'^0UT', 'OUT'), (r'B00T', 'BOOT'), (r'(?<=CH)O(?=\d|$)', '0'), (r'^UO(?=TX|RX|RTS|CTS)', 'U0')]
def fix_prefix(name):
    for pattern, replacement in O_WORDS: name = re.sub(pattern, replacement, name)
    return name
# Rules v3: +/− polarity marks alone are not pin names; such connectors are not wiring headers.
def polarity_only(connector): return all(p['label'].strip() in ('+', '-', '−') for p in connector['pins'])

def export_connector(a, b=None):
    pins = []
    for i, pin in enumerate(a['pins']):
        label, functions = pin['label'], pin.get('functions', [])
        if b:
            other = b['pins'][i]
            # Prefer the functional name (GPIO25 over 25, GND over G); keep the other spelling as a printed alias.
            if not FUNCTIONAL.match(label) and FUNCTIONAL.match(other['label']) or canon(label) == canon(other['label']) and len(other['label']) > len(label): label, alias = other['label'], pin['label']
            else: alias = other['label']
            both = {canon(f) for f in other.get('functions', [])}
            functions = [f for f in functions if canon(f) in both]  # functions only both passes read
            if canon(alias) != canon(label) or alias != label and not FUNCTIONAL.match(alias): functions = [alias, *functions]
            seen = {canon(label)}; functions = [f for f in functions if not (canon(f) in seen or seen.add(canon(f)))]
        pins.append({'position': pin['position'], 'label': 'Unlabeled' if label == '?' else fix_prefix(label), 'functions': [fix_prefix(f) for f in functions if f != '?']})
    cid = a['id'] if not b or a['id'] == b['id'] or DESIGNATOR.match(a['id']) else b['id'] if DESIGNATOR.match(b['id']) else a['id']
    return {'id': cid, 'name': a.get('name') or cid, 'rows': a['rows'], 'image': a['image'], 'pins': pins}

def compare(a, b):
    agreed, conflicts, used = [], [], set()
    for ca in a['connectors']:
        options = [i for i, cb in enumerate(b['connectors']) if i not in used and ca['image'] == cb['image'] and connectors_agree(ca, cb)]
        match = next((i for i in options if b['connectors'][i]['image'] == ca['image']), options[0] if options else None)
        if match is not None: used.add(match); agreed.append(export_connector(ca, b['connectors'][match])); continue
        similar = next((cb for i, cb in enumerate(b['connectors']) if i not in used and cb['image'] == ca['image'] and (cb['id'] == ca['id'] or len(cb['pins']) == len(ca['pins']))), None)
        seq = [p['label'] for p in ca['pins']]
        reason = 'unreadable labels' if '?' in seq and similar and len(similar['pins']) == len(seq) else 'reversed order' if similar and connectors_agree({**ca, 'pins': ca['pins'][::-1]}, similar) else 'different labels or pin count' if similar else 'only in pass a'
        conflicts.append({'connector': ca['id'], 'image': ca['image'], 'reason': reason, 'a': ca, 'b': similar})
    for i, cb in enumerate(b['connectors']):
        if i not in used and not any(c['b'] is cb for c in conflicts): conflicts.append({'connector': cb['id'], 'image': cb['image'], 'reason': 'only in pass b', 'a': None, 'b': cb})
    return agreed, conflicts

# Connectors from every image combine into one view. A connector repeating one already taken from
# an earlier image (same position in another view, or another revision) stays an alternative and is
# never merged, so each physical connector appears once.
def views(connectors, order):
    stem = lambda c: re.sub(r'[-_ ]*(img|image|view|rev|v)?[-_ ]*\d+$', '', c['id'].lower())
    primary, alternatives = [], {}
    for c in sorted(connectors, key=lambda c: order.index(c['image'])):
        repeat = c['image'] != (primary[0]['image'] if primary else c['image']) and any(connectors_agree(c, p) or stem(c) == stem(p) for p in primary)
        if repeat: alternatives.setdefault(c['image'], []).append(c)
        else: primary.append(c)
    # Image suffixes are transcription bookkeeping; drop them where the plain id stays unique.
    for c in primary:
        plain = re.sub(r'-img\d+$', '', c['id'])
        if plain != c['id'] and not any(o['id'] == plain for o in primary): c['id'] = plain
    return primary, [{'image': image, 'connectors': group} for image, group in alternatives.items()]

def main():
    global ROOT, LIB, TRANSCRIPTIONS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=pathlib.Path, default=ROOT)
    parser.add_argument('--strict-double-entry', action='store_true', help='Ignore the single-read policy for this build')
    parser.add_argument('--dry-run', action='store_true', help='Validate and report without writing any catalog files')
    args = parser.parse_args()
    ROOT = args.root.resolve(); LIB = ROOT / 'library'; TRANSCRIPTIONS = ROOT / 'catalog' / 'pin-transcriptions'
    policy_path = TRANSCRIPTIONS / 'policy.json'
    policy = json.loads(policy_path.read_text()) if policy_path.exists() else {}
    single = policy.get('mode') == 'single-read-with-checks' and not args.strict_double_entry
    catalog = json.loads((LIB / 'catalog.json').read_text(encoding='utf-8'))
    records = {r['id']: r for r in [*catalog['boards'], *catalog.get('makerParts', [])]}
    errors, digests, passes, invalid = [], {}, {'a': {}, 'b': {}, 'reviewed': {}}, {}
    for key, folder in (('a', TRANSCRIPTIONS / 'passes' / 'a'), ('b', TRANSCRIPTIONS / 'passes' / 'b'), ('reviewed', TRANSCRIPTIONS / 'reviewed')):
        for path in sorted(folder.glob('*.json')):
            start = len(errors)
            try:
                data = load(path, records, errors, digests)
                if data and key != 'reviewed' and data.get('pass') != key: fail(errors, path, 'pass field does not match directory')
            except (ValueError, KeyError, TypeError, AttributeError, OSError) as error:
                fail(errors, path, f'Cannot validate transcription: {error}')
                data = None
            if len(errors) > start:
                invalid.setdefault(path.stem, []).extend(errors[start:])
            elif data: passes[key][data['recordId']] = data
    ocr_path = TRANSCRIPTIONS / 'ocr-checks.json'
    ocr = json.loads(ocr_path.read_text())['records'] if ocr_path.exists() else {}
    identity = []
    exported, queue, summary = {}, [{'recordId': rid, 'reason': 'Invalid transcription; repair the saved file before export', 'errors': problems, 'conflicts': []} for rid, problems in sorted(invalid.items())], {'double-entry': 0, 'ocr-arbitrated': 0, 'ocr-checked': 0, 'single-entry': 0, 'partial': 0, 'reviewed': 0, 'identity': 0, 'no-connector-map': 0, 'conflict': 0, 'awaiting-second-pass': 0, 'needs-review': 0, 'invalid': len(invalid)}
    for rid in sorted(set(passes['a']) | set(passes['b']) | set(passes['reviewed'])):
        if rid in invalid: continue
        reviewed, a, b = passes['reviewed'].get(rid), passes['a'].get(rid), passes['b'].get(rid)
        if reviewed:
            if reviewed['status'] == 'transcribed': exported[rid] = dict(review='reviewed', source=reviewed, connectors=[export_connector(c) for c in reviewed['connectors']])
            summary['reviewed'] += 1; continue
        if not (a and b):
            if not single: summary['awaiting-second-pass'] += 1; continue
            source, key = (a, 'a') if a else (b, 'b')
            issues = single_pass_issues(source, records[rid])
            if source['status'] == 'no-connector-map':
                if IDENTITY.search(source.get('notes', '')): identity.append({'recordId': rid, 'notes': [source.get('notes', '')]})
                if issues: queue.append({'recordId': rid, 'reason': '; '.join(issues), 'conflicts': [], 'pass': key}); summary['needs-review'] += 1
                else: summary['no-connector-map'] += 1
                continue
            check = ocr.get(rid, {}).get(key) or {}
            categories, confirmed = set(check.get('uncertainty', [])), check.get('verdict') == 'confirmed'
            connectors = [c for c in source['connectors'] if not polarity_only(c)]
            # Board identity cannot be settled by any reading of the same image: those wait for a corrected image.
            if 'identity' in categories:
                identity.append({'recordId': rid, 'notes': source.get('uncertain', [])})
                queue.append({'recordId': rid, 'reason': 'Board identity: the image may show another product or variant', 'conflicts': [], 'pass': key}); summary['identity'] += 1; continue
            blocking = [i for i in issues if any(term in i for term in OCR_BLOCKING)]
            # The OCR check settles reading, mapping, grouping and sequence doubts; pin-1 direction stays a caveat.
            if issues and not (confirmed and not blocking and categories <= OCR_SETTLES):
                queue.append({'recordId': rid, 'reason': '; '.join(issues), 'conflicts': [], 'pass': key, **({'ocr': check.get('verdict')} if check else {})}); summary['needs-review'] += 1; continue
            review = 'ocr-checked' if confirmed else 'single-entry'
            exported[rid] = dict(review=review, source=source, connectors=[export_connector(c) for c in connectors], caveats=caveats(check, categories, connectors))
            summary[review] += 1; continue
        if a['status'] == b['status'] == 'no-connector-map': summary['no-connector-map'] += 1; continue
        if a['status'] != b['status']:
            queue.append({'recordId': rid, 'reason': f"pass a: {a['status']}, pass b: {b['status']}", 'conflicts': []}); summary['conflict'] += 1; continue
        agreed, conflicts = compare(a, b)
        # Where the two readings differ, the one the OCR check confirms against the image wins.
        arbitrated, remaining = [], []
        for conflict in conflicts:
            verdict = {k: (ocr.get(rid, {}).get(k) or {}).get('connectors', {}).get((conflict[k] or {}).get('id'), {}).get('verdict') for k in ('a', 'b')}
            winner = 'a' if verdict['a'] == 'confirmed' != verdict['b'] else 'b' if verdict['b'] == 'confirmed' != verdict['a'] else None
            if winner and conflict[winner] and not polarity_only(conflict[winner]): arbitrated.append(export_connector(conflict[winner]))
            else: remaining.append(conflict)
        agreed, conflicts = agreed + arbitrated, remaining
        if conflicts: queue.append({'recordId': rid, 'reason': f'{len(conflicts)} connector(s) disagree', 'conflicts': conflicts})
        if agreed:
            review = 'partial' if conflicts else 'ocr-arbitrated' if arbitrated else 'double-entry'
            exported[rid] = dict(review=review, source=a, connectors=[c for c in agreed if not polarity_only(c)], pending=len(conflicts))
            summary[review] = summary.get(review, 0) + 1
        else: summary['conflict'] += 1
    for record in records.values(): record.pop('pinConnectors', None)
    dataset = []
    for rid, e in exported.items():
        order = [i['file'] for i in e['source']['images']]
        primary, alternatives = views(e['connectors'], order)
        images = [f for f in order if any(c['image'] == f for c in primary)]
        hashes = {i['file']: i['sha256'] for i in e['source']['images']}
        value = {'method': 'image-transcription', 'review': e['review'], 'transcribed': e['source']['date'], 'images': [{'file': f, 'sha256': hashes[f]} for f in images], 'connectors': primary,
                 **({'alternatives': [{'image': {'file': v['image'], 'sha256': hashes[v['image']]}, 'connectors': v['connectors']} for v in alternatives]} if alternatives else {}), **({'pendingConnectors': e['pending']} if e.get('pending') else {}), **({'caveats': e['caveats']} if e.get('caveats') else {})}
        records[rid]['pinConnectors'] = value
        dataset.append({'recordId': rid, **value})
    catalog['stats']['pinConnectorRecords'] = len(dataset)
    scope = 'Connector lists transcribed from cited pinout images. single-entry means one image reading with source-hash and structural checks; double-entry means two agreeing readings. Neither is electrical verification; match the exact board revision.'
    report = {**summary, 'identityIssues': len(identity), 'exportedRecords': len(dataset), 'exportedConnectors': sum(len(d['connectors']) for d in dataset), 'alternativeViews': sum(len(d.get('alternatives', [])) for d in dataset), 'exportedPins': sum(len(c['pins']) for d in dataset for c in d['connectors']), 'reviewQueue': len(queue)}
    if args.dry_run: print(json.dumps(report, indent=2)); return 0
    (ROOT / 'catalog' / 'board-connectors.json').write_text(json.dumps({'scope': scope, 'records': dataset}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (ROOT / 'catalog' / 'pin-review-queue.json').write_text(json.dumps({'scope': 'Transcriptions that need a human decision. Write the corrected file to catalog/pin-transcriptions/reviewed/.', 'records': queue}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (ROOT / 'catalog' / 'image-identity-issues.json').write_text(json.dumps({'scope': 'Records whose pinout image may show another product or variant. Replace or re-attribute the image; no reading of it can fix this.', 'records': identity}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (LIB / 'catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    # Maker records are mirrored in library/maker-parts.json; run this after tools/build-maker-index.py.
    makers = json.loads((LIB / 'maker-parts.json').read_text(encoding='utf-8')); makers['parts'] = catalog.get('makerParts', [])
    (LIB / 'maker-parts.json').write_text(json.dumps(makers, ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
    return 0

if __name__ == '__main__': sys.exit(main())
