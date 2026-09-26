"""Refresh public indexes from library/catalog.json (Python 3, standard library only).

Preserves stable board paths and asset IDs. Does not download, license, or
electrically verify references. Use --boards FILE for a JSON array of board IDs
whose pages need refreshing; otherwise refresh new pages and device pages.
"""
import argparse, collections, csv, datetime, hashlib, json, pathlib, re

ROOT=pathlib.Path(__file__).resolve().parents[1]
LIB=ROOT/'library'
def write_json(path,value,compact=False):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=None if compact else 2,separators=(',',':') if compact else None)+'\n',encoding='utf-8')
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-') or 'unspecified'
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--boards',type=pathlib.Path);args=parser.parse_args()
    c=json.loads((LIB/'catalog.json').read_text(encoding='utf-8'))
    paths=json.loads((ROOT/'catalog/board-paths.json').read_text(encoding='utf-8'))
    refresh=set(json.loads(args.boards.read_text(encoding='utf-8'))) if args.boards else {b['id'] for b in c['boards'] if b.get('device')}
    boards=[b for b in c['boards'] if b['assets']];assets=[a for b in boards for a in b['assets']]
    assert len({b['id'] for b in c['boards']})==len(c['boards']),'Duplicate board IDs'
    assert len({a['id'] for a in assets})==len(assets),'Duplicate asset IDs'
    media={a['file']:a['bytes'] for a in assets}
    for a in assets:
        if a.get('vector'):media[a['vector']]=(LIB/a['vector']).stat().st_size
    c['stats'].update(boardsWithFiles=len(boards),trackedBoards=len(c['boards']),referenceEntries=len(assets),physicalPinouts=sum(a['type']=='pinout image' for a in assets),brands=len({b['brand'] for b in boards}),uniqueMedia=len(media),libraryBytes=sum(media.values()),devicesWithFiles=sum(bool(b.get('device')) for b in boards),devicePinouts=sum(a['type']=='pinout image' for b in boards if b.get('device') for a in b['assets']))
    c['generatedAt']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    for b in boards:
        if b['id'] not in paths:
            paths[b['id']]=f"boards/{slug(b['brand'])}/{slug(b['processor'] or b['family'])}/{slug(b['name'])}--{hashlib.sha256(b['id'].encode()).hexdigest()[:8]}/README.md"
            refresh.add(b['id'])
        if b['id'] not in refresh:continue
        page=ROOT/paths[b['id']];page.parent.mkdir(parents=True,exist_ok=True)
        prefix='../'*(len(pathlib.PurePosixPath(paths[b['id']]).parts)-1)
        lines=[f"# {b['name']}",'',f"**{b['brand']}** · {b['processor'] or b['family']}",'',f"Revision: {b.get('revision') or 'Not identified'}",'',f"Coverage: {b['coverage']}",'',f"[Browse all manufacturers]({prefix}BROWSE.md) · [Devices & IoT]({prefix}DEVICES.md) · [Open in the browser guide](https://valleytech-black-wire-guide.pages.dev/?board={b['id']})",'']
        if b.get('device'):
            lines.extend([f"Device category: **{b['device']['category']}**",''])
            if b['device'].get('note'):lines.extend([b['device']['note'],''])
        if b.get('architecture'):lines.extend([f"Architecture: **{b['architecture']}**",''])
        if b.get('specifications'):
            lines.extend(['## Specifications and hardware documentation',''])
            lines.extend([f"- [{s.get('label','Hardware documentation')}]({s['url']})" for s in b['specifications']])
            lines.append('')
        for a in b['assets']:
            lines.extend([f"## {a['label']}",'',f"**{a['type']}** · {a['review']} · {a['extension'].upper()}",''])
            if a.get('thumb'):lines.extend([f"[![{b['name']} reference preview]({prefix}library/{a['thumb']})]({prefix}library/{a['file']})",''])
            lines.extend([f"[Open original reference]({prefix}library/{a['file']})",''])
            if a.get('vector'):lines.extend([f"[Original vector companion]({prefix}library/{a['vector']})",''])
            lines.extend([f"**Credit and rights:** {a['rights']}. Source/manufacturer: {b['brand']}.",''])
            urls=list(dict.fromkeys([a.get('url'),*a.get('sources',[])]));urls=[u for u in urls if u and u.startswith(('https://','http://'))]
            lines.extend([' · '.join(f'[Source {i+1}]({u})' for i,u in enumerate(urls)),'',a.get('notes',''),'',f"Image revision: {a.get('revision') or 'Not identified'}",'',f"SHA-256: `{a['hash']}`",''])
        lines.extend(['Pin assignments have not been independently electrically verified. Check board revision before wiring.',''])
        page.write_text('\n'.join(lines),encoding='utf-8')
    write_json(ROOT/'catalog/board-paths.json',paths)
    attribution=[]
    for b in boards:
        for a in b['assets']:
            attribution.append(dict(asset_id=a['id'],board=b['name'],manufacturer=b['brand'],processor=b['processor'],reference_type=a['type'],review=a['review'],file=a['file'],sha256=a['hash'],source_urls=' | '.join(dict.fromkeys([u for u in [a.get('url'),*a.get('sources',[])] if u])),rights_status=a['rights'],original_collection_paths=' | '.join(a.get('originals',[]))))
    write_json(ROOT/'catalog/attributions.json',attribution)
    with (ROOT/'catalog/attributions.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(attribution[0]));writer.writeheader();writer.writerows(attribution)
    browse=['# Browse the reference collection','','[Devices & IoT](DEVICES.md) · [First Edition policy](EDITION.md) · [Search the website](https://valleytechsolutions.tech/pages/bwm-technical-reference-guide)','','Board diagrams, GPIO references and additional source documents are labeled separately.','']
    grouped=collections.defaultdict(list)
    for b in boards:grouped[b['brand']].append(b)
    for brand in sorted(grouped):
        browse.extend(['## '+brand,'','| Board / device | Processor / family | References | Pinout images |','|---|---|---:|---:|'])
        for b in sorted(grouped[brand],key=lambda b:b['name'].lower()):browse.append(f"| [{b['name']}]({paths[b['id']]}) | {b['processor'] or b['family']} | {len(b['assets'])} | {b['pinouts']} |")
        browse.append('')
    (ROOT/'BROWSE.md').write_text('\n'.join(browse),encoding='utf-8')
    devices=[b for b in boards if b.get('device')]
    lines=['# Devices & IoT','','[Search devices in the browser guide](https://valleytech-black-wire-guide.pages.dev/?tab=devices) · [All boards](BROWSE.md) · [First Edition](EDITION.md)','',f"**{len(devices)} device records with references.** Includes handhelds, radio nodes, wearables, cameras, displays and controllers. Counts include unreviewed source records and supporting references; not every record has a full physical pinout.",'','Original manufacturer images remain unchanged. Revision and partial-map notes live on each device page.','']
    for category in sorted({b['device']['category'] for b in devices}):
        lines.extend(['## '+category,'','| Manufacturer | Device | Processor | Pinout images | References |','|---|---|---|---:|---:|'])
        for b in sorted((b for b in devices if b['device']['category']==category),key=lambda b:(b['brand'],b['name'])):
            phase=' · pre-release documentation' if b['device']['phase']=='in-development' else ''
            lines.append(f"| {b['brand']} | [{b['name']}]({paths[b['id']]}){phase} | {b['processor'] or 'Not recorded'} | {b['pinouts']} | {len(b['assets'])} |")
        lines.append('')
    lines.extend(['## Documentation watch','','These are identified gaps, not saved pinout sheets or promised release dates.',''])
    for b in c.get('deviceWatchlist',[]):lines.extend([f"### {b['brand']} {b['name']}",'',f"**{b['status']}** · Checked {b['checked']}",'',b['note'],'',f"[Official source]({b['source']})",''])
    (ROOT/'DEVICES.md').write_text('\n'.join(lines),encoding='utf-8')
    write_json(LIB/'catalog.json',c,True)
    manifest=sorted(p.relative_to(LIB).as_posix() for p in LIB.rglob('*') if p.is_file() and p.name!='manifest.json')
    write_json(LIB/'manifest.json',manifest,True)
    print(json.dumps(c['stats'],indent=2))
if __name__=='__main__':main()
