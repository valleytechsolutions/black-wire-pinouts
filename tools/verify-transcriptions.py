"""Machine check of pin transcriptions against their source images (Python 3 + macOS Vision OCR).

No AI reading. For each transcribed connector this script asks two deterministic questions of the
cited image: are the transcribed labels actually printed there, and do they line up in the same
physical sequence as the transcribed positions? It cannot tell which end is pin 1, read graphics,
or establish board identity; those remain caveats or review items.

Writes catalog/pin-transcriptions/ocr-checks.json, consumed by tools/build-board-connectors.py.
OCR output is cached per image SHA-256 in .cache/ocr/ (rerun-safe and incremental).

  python3 tools/verify-transcriptions.py            # check every saved reading
  python3 tools/verify-transcriptions.py --record ID
"""
import argparse, concurrent.futures, json, os, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LIB = ROOT / 'library'
TRANSCRIPTIONS = ROOT / 'catalog' / 'pin-transcriptions'
CACHE = ROOT / '.cache'
SWIFT = ROOT / 'tools' / 'ocr' / 'vision-ocr.swift'
BINARY = CACHE / 'vision-ocr'
MIN_LINE_CONFIDENCE = 0.3
WORKERS = max(1, min(4, (os.cpu_count() or 2) // 2))

# --- OCR -----------------------------------------------------------------------------------
def ocr_binary():
    if not BINARY.exists() or BINARY.stat().st_mtime < SWIFT.stat().st_mtime:
        CACHE.mkdir(exist_ok=True)
        subprocess.run(['swiftc', '-O', str(SWIFT), '-o', str(BINARY)], check=True)
    return BINARY

def ocr(images):
    """images: {file: sha256} → {file: ocr result}; cached by hash."""
    out, todo = {}, []
    (CACHE / 'ocr').mkdir(parents=True, exist_ok=True)
    for file, sha in images.items():
        cached = CACHE / 'ocr' / f'{sha}.json'
        if cached.exists(): out[file] = json.loads(cached.read_text())
        else: todo.append((file, sha))
    binary = ocr_binary()
    def run(chunk):
        result = subprocess.run([str(binary), *(str(LIB / f) for f, _ in chunk)], capture_output=True, text=True, check=True)
        for (file, sha), line in zip(chunk, result.stdout.splitlines()):
            data = json.loads(line)
            (CACHE / 'ocr' / f'{sha}.json').write_text(json.dumps(data))  # cached per chunk, so an interrupted run resumes
            out[file] = data
        return len(chunk)
    chunks = [todo[i:i + 10] for i in range(0, len(todo), 10)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        done = 0
        for count in pool.map(run, chunks):
            done += count
            if done % 100 < count: print(f'OCR {done}/{len(todo)} images', file=sys.stderr, flush=True)
    return out

# --- Matching ------------------------------------------------------------------------------
SEPARATORS = re.compile(r'[\s_./\-:;,()\[\]{}|>]+')
def fold(text):
    """Comparison form: uppercase, O→0 and I/L→1 (OCR and fonts confuse them), separators removed."""
    return SEPARATORS.sub('', text.upper()).translate(str.maketrans({'O': '0', 'I': '1', 'L': '1'}))

def folded_line(text):
    """Folded characters of an OCR line, each with its index in the original text and whether a separator preceded it."""
    chars, gap = [], True
    for i, ch in enumerate(text.upper()):
        if SEPARATORS.fullmatch(ch): gap = True; continue
        chars.append((fold(ch) or ch, i, gap)); gap = False
    return chars

def kind(ch): return 'd' if ch.isdigit() else 'a' if ch.isalpha() else 'o'

def find(label, lines):
    """Centres of every occurrence of a label in the OCR lines, respecting token boundaries."""
    target = fold(label)
    if len(target) < 1: return []
    hits = []
    for line in lines:
        chars = folded_line(line['text'])
        s = ''.join(c for c, _, _ in chars)
        start = s.find(target)
        while start != -1:
            end = start + len(target)
            # A match must start at a separator or a letter/digit change, and end the same way, so GPIO1 never matches GPIO10.
            left = start == 0 or chars[start][2] or kind(s[start - 1]) != kind(s[start])
            right = end == len(s) or chars[end][2] or kind(s[end - 1]) != kind(s[end])
            if left and right and (len(target) > 1 or (start == 0 and end == len(s))):
                x, y, w, h = line['box']; n = max(1, len(line['text']))
                mid = (chars[start][1] + chars[end - 1][1] + 1) / 2
                hits.append((x + w * mid / n, y + h / 2, h))
            start = s.find(target, start + 1)
    return hits

def spearman(values):
    n = len(values)
    if n < 2: return 0.0
    ranks = {v: r for r, v in enumerate(sorted(range(n), key=lambda i: values[i]))}
    d = sum((i - ranks[i]) ** 2 for i in range(n))
    return 1 - 6 * d / (n * (n * n - 1))

def band(pins_hits, size):
    """The line of text (constant perpendicular coordinate) that holds the most of these pins' labels."""
    best = None
    for axis in (0, 1):  # 0: labels spread along x (horizontal row), 1: along y (vertical column)
        perp = 1 - axis
        for centre in (h for hits in pins_hits for h in hits):
            tol = max(centre[2] * 1.2, size[perp] * 0.012)
            chosen = []
            for i, hits in enumerate(pins_hits):
                near = [h for h in hits if abs(h[perp] - centre[perp]) <= tol]
                if near: chosen.append((i, min(near, key=lambda h: abs(h[perp] - centre[perp]))[axis]))
            if len(chosen) < 2: continue
            values = [c for _, c in chosen]
            strict = all(b > a for a, b in zip(values, values[1:])) or all(b < a for a, b in zip(values, values[1:]))
            score = (len(chosen), strict, abs(spearman(values)))
            if not best or score > best['score']:
                best = {'score': score, 'axis': axis, 'perp': centre[perp], 'tol': tol, 'chosen': chosen, 'strict': strict, 'rho': round(spearman(values), 3)}
    return best

def pitch(b, group):
    """Least-squares slot position (start + step × index in the row) from the labels on the connector's line."""
    points = b['chosen']
    if len(points) < 2: return None
    n = len(points); mx = sum(x for x, _ in points) / n; my = sum(y for _, y in points) / n
    var = sum((x - mx) ** 2 for x, _ in points)
    if not var: return None
    step = sum((x - mx) * (y - my) for x, y in points) / var
    return (my - step * mx, step) if abs(step) > 0 else None

def in_slot(hits, b, slot, index, size):
    start, step = slot; axis, perp = b['axis'], 1 - b['axis']
    expected = start + step * index
    return any(abs(h[axis] - expected) <= abs(step) * 0.45 and abs(h[perp] - b['perp']) <= size[perp] * 0.3 for h in hits)

def in_band(hits, b):
    perp = 1 - b['axis']
    return any(abs(h[perp] - b['perp']) <= b['tol'] for h in hits)

POWER = re.compile(r'^\+?(GND|AGND|DGND|PGND|VSS|VCC|VDD|VIN|VBUS|VBAT|BAT|VSYS|3V3|3\.3V|5V|5V0|12V|V\+|V-|NC)$', re.I)

def check_connector(connector, lines, size):
    # Not-connected pads are not wiring points and are often labelled away from the header.
    pins = [p for p in connector['pins'] if p['label'] not in ('?', 'Unlabeled') and fold(p['label']) not in ('NC', 'N/C', 'DNC')]
    if not pins: return {'pins': 0, 'verdict': 'unverified'}
    # The label itself or the silkscreen spelling rule 5 places first in functions: either may be the text beside the pin.
    hits = [find(p['label'], lines) + (find(p['functions'][0], lines) if p.get('functions') else []) for p in pins]
    rows = connector.get('rows', 1)
    # Repeated labels (GND, 3V3…) cannot say where in the row they sit: they count for coverage, not order.
    folded = [fold(p['label']) for p in pins]
    unique = [h if folded.count(folded[i]) == 1 else [] for i, h in enumerate(hits)]
    # Only power and ground names legitimately repeat in one connector; a repeated signal name is a misreading.
    repeated = sorted({p['label'] for p, f in zip(pins, folded) if folded.count(f) > 1 and not POWER.match(p['label'])})
    # Alternating 2-row numbering puts odd and even positions on separate rows: check each row on its own.
    idx = [list(range(r, len(pins), rows)) for r in range(rows)]
    found = anchors = 0; rhos = []; ok = True; misplaced, missing = [], []
    for group in idx:
        # Indices stay row-relative (empty entries kept) so the pitch fit maps each label to its true slot.
        b = band([unique[i] for i in group], size) or band([hits[i] for i in group], size)
        if not b: ok = ok and len(group) < 2; rhos.append(None); continue
        # A label counts when it sits in this pin's slot along the connector: on the connector's line of text, or
        # offset sideways (power pins often get their own column) at the position the pin pitch predicts.
        # Found only elsewhere means misplaced (a misread or shuffle); not found at all means the OCR missed it.
        slot = pitch(b, group)
        for n, i in enumerate(group):
            if hits[i] and (in_band(hits[i], b) or (slot and in_slot(hits[i], b, slot, n, size))): found += 1
            elif hits[i]: misplaced.append(pins[i]['label'])
            else: missing.append(pins[i]['label'])
        n_unique = sum(1 for i in group if unique[i])
        anchors += len(b['chosen']) if n_unique >= 2 else 0
        rhos.append(b['rho'])
        if n_unique >= 2 and not b['strict']: ok = False
    coverage = found / len(pins)
    # Confirmed: labels sit on the connector's own line of text in strict transcribed order, none appear only
    # elsewhere, and OCR missed at most one pin or 10% (those are listed so the app can name them).
    if not misplaced and not repeated and len(missing) <= max(1, len(pins) // 10) and ok and anchors >= min(sum(1 for h in unique if h), 2): verdict = 'confirmed'
    elif coverage >= 0.5: verdict = 'partial'
    else: verdict = 'unverified'
    return {'pins': len(pins), 'found': found, 'coverage': round(coverage, 3), 'anchors': anchors, 'rho': rhos, 'verdict': verdict, **({'unconfirmed': missing} if missing else {}), **({'misplaced': misplaced} if misplaced else {}), **({'repeated': repeated} if repeated else {})}

# --- Uncertainty triage --------------------------------------------------------------------
CATEGORIES = [
    ('identity', r'identit|variant|titled|different (board|product)|not the |only (labeled|labelled)|cannot confirm|could not confirm|shared image|same image|record (name|is)|shows (a|an|the) .*(board|module|base)|no (product|board) name|render'),
    ('order', r'order|nearest|closest|usb|outer|inner row|reverse|start(s|ed)? (at|from)|pin 1|direction|left to right|top to bottom'),
    ('mapping', r'infer|mapping|map(ped)? |leader|line(s)? |align|assign|callout|table|which (label|pin|pad|hole)'),
    ('grouping', r'group|separate|single pad|test pad|skipp|not transcribed|included|excluded|left out|omitted|treated as'),
    ('reading', r'faint|legib|small|blur|resolution|o/0|look-alike|typo|misprint|printed as'),
]
def classify(note):
    text = note if isinstance(note, str) else json.dumps(note)
    found = [name for name, pattern in CATEGORIES if re.search(pattern, text, re.I)]
    return found or ['other']

# --- Main ----------------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--record'); args = parser.parse_args()
    readings = {}
    for key in ('a', 'b'):
        for path in sorted((TRANSCRIPTIONS / 'passes' / key).glob('*.json')):
            if args.record and path.stem != args.record: continue
            try: data = json.loads(path.read_text())
            except ValueError: continue
            if data.get('status') == 'transcribed': readings.setdefault(path.stem, {})[key] = data
    images = {i['file']: i['sha256'] for r in readings.values() for d in r.values() for i in d.get('images', [])}
    results = ocr(images)
    out_path = TRANSCRIPTIONS / 'ocr-checks.json'
    checks = json.loads(out_path.read_text()) if args.record and out_path.exists() else {}
    checks = checks.get('records', checks) if isinstance(checks, dict) else {}
    for rid, passes in readings.items():
        entry = {}
        for key, data in passes.items():
            connectors = {}
            for c in data.get('connectors', []):
                page = results.get(c.get('image'), {})
                lines = [l for l in page.get('lines', []) if l.get('confidence', 1) >= MIN_LINE_CONFIDENCE]
                connectors[c['id']] = check_connector(c, lines, (page.get('width', 1), page.get('height', 1))) if lines else {'verdict': 'no-text'}
            verdicts = [v['verdict'] for v in connectors.values()]
            entry[key] = {
                'verdict': 'confirmed' if verdicts and all(v == 'confirmed' for v in verdicts) else 'partial' if any(v in ('confirmed', 'partial') for v in verdicts) else 'unverified',
                'connectors': connectors,
                'uncertainty': sorted({c for note in data.get('uncertain', []) for c in classify(note)}),
            }
        checks[rid] = entry
    summary = {}
    for entry in checks.values():
        for reading in entry.values(): summary[reading['verdict']] = summary.get(reading['verdict'], 0) + 1
    scope = 'Machine OCR check (Apple Vision): transcribed labels found in the cited image and lined up in the transcribed sequence. Not a reading of graphics, pin-1 direction, board identity or electrical function.'
    out_path.write_text(json.dumps({'scope': scope, 'records': dict(sorted(checks.items()))}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print(json.dumps({'records': len(checks), 'readings': summary, 'images': len(images)}, indent=2))
    return 0

if __name__ == '__main__': sys.exit(main())
