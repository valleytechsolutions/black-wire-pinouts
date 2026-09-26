"""Validate editable maker intake, then generate application and Markdown indexes."""
import collections,json,re,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    data=json.loads((ROOT/'catalog/maker-parts.json').read_text(encoding='utf-8'))
    c=json.loads((ROOT/'library/catalog.json').read_text(encoding='utf-8'))
    ids=set();boardids={b['id'] for b in c['boards']};boards={b['id']:b for b in c['boards']};media={};ledger=[]
    for p in data['parts']:
        assert p['id'] not in ids and re.fullmatch('[a-z0-9-]+',p['id']),p['id'];ids.add(p['id'])
        assert p['name'] and p['category'] and p['brand']
        assert not p['completePhysicalPinout'],'This intake compiler cannot approve physical pinouts'
        assert set(p['boardIds'])<=boardids
        for s in p['sources']:assert s['url'].startswith('https://')
        if p['documentationStatus']=='Manufacturer documentation recorded':
            assert p['sources'] and all(re.fullmatch('[a-f0-9]{64}',s.get('sha256','')) for s in p['sources'])
        if p['pinLabels']:assert p['sources'] and p['identityKind']!='generic-family'
        for a in p.get('assets',[]):
            path=ROOT/'library'/a['file']
            assert path.resolve().is_relative_to((ROOT/'library').resolve())
            assert hashlib.sha256(path.read_bytes()).hexdigest()==a['hash'],a['file']
            assert a['rights'] and a['review'] and a['sources']
            for field in ['thumb','display']:
                if a.get(field):assert (ROOT/'library'/a[field]).is_file()
            media[a['file']]=a
            ledger.append(dict(partId=p['id'],part=p['name'],brand=p['brand'],**a))
        linked=[a for id in p['boardIds'] for a in boards[id]['assets']]
        combined={a['file']:a for a in [*p.get('assets',[]),*linked]}
        p['imageCount']=sum(bool(a.get('thumb')) or a['extension'] in ['jpg','png','webp','svg','gif','jpeg'] for a in combined.values())
        p['referenceCount']=len(combined)
    (ROOT/'catalog/maker-attributions.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    c['makerParts']=data['parts'];c['makerScope']={k:v for k,v in data.items() if k!='parts'}
    c['stats'].update(makerRecords=len(ids),makerDocumented=sum(p['documentationStatus']=='Manufacturer documentation recorded' for p in data['parts']),makerGenericFamilies=sum(p['identityKind']=='generic-family' for p in data['parts']))
    c['stats'].update(makerWithImages=sum(bool(p['imageCount']) for p in data['parts']),makerNewMedia=len(media),makerPhysicalReferences=sum(a['type']=='pinout image' for a in media.values()))
    (ROOT/'library/catalog.json').write_text(json.dumps(c,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    (ROOT/'library/maker-parts.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    lines=['# Displays, sensors and maker modules','',data['scope'],'',data['countMeaning'],'',f"**{len(ids)} intake records**. {c['stats']['makerDocumented']} manufacturer documentation records. No new complete physical pinout approvals in this intake.",'','[Search the interactive guide](https://valleytech-black-wire-guide.pages.dev/?tab=makers) · [Expansion roadmap](docs/MAKER_ROADMAP.md) · [Coverage backlog](catalog/maker-research-backlog.json)','','Search by product/controller code first; filter by interface, function, technology or recorded display size. A blank field means unknown, not universal compatibility. Pin-label lists do not give physical connector order.','']
    groups=collections.defaultdict(list)
    for p in data['parts']:groups[p['category']].append(p)
    visual_index=['# Maker visual references','','Images are source references, with their own credits and review status. Photos do not count as pinouts.','']
    for cat,parts in sorted(groups.items()):
        slug=re.sub('[^a-z0-9]+','-',cat.lower()).strip('-');gallery=ROOT/'docs/maker-visuals'/f'{slug}.md';gallery.parent.mkdir(parents=True,exist_ok=True)
        visual_index.append(f'- [{cat}](docs/maker-visuals/{slug}.md)')
        gl=['# '+cat+' / visual references','','[All categories](../../MAKER_VISUALS.md) · [Image attribution ledger](../../catalog/maker-attributions.json)','','Source references remain unchanged. Check exact PCB/revision, source notes and rights before reuse. Photos and partial connector diagrams are not complete-device approvals.','']
        for p in sorted(parts,key=lambda p:p['name'].lower()):
            assets={a['file']:a for a in [*p.get('assets',[]),*(a for id in p['boardIds'] for a in boards[id]['assets'])]}
            a=next((a for a in assets.values() if a['type']=='pinout image' and a.get('thumb')),None) or next((a for a in assets.values() if a.get('thumb')),None)
            gl += ['## '+p['name'],'',f"{p['brand']} · {p['documentationStatus']}",'',f"[Open full gallery](https://valleytech-black-wire-guide.pages.dev/?tab=makers&part={p['id']})",'']
            if a:gl += [f"[![{p['name']} / {a['type']}](../../library/{a['thumb']})](../../library/{a['file']})",'',f"**{a['type']}** · {a['review']}",'',a['rights'],'']
            else:gl += ['Matching image still needed.','']
        gallery.write_text('\n'.join(gl),encoding='utf-8')
        lines += ['## '+cat,'','| Product or family | Manufacturer | Record status | Source |','|---|---|---|---|']
        for p in parts:
            source='[Documentation]('+p['sources'][0]['url']+')' if p['sources'] else 'Identification needed'
            lines.append('| '+p['name'].replace('|','/')+' | '+p['brand']+' | '+p['identityKind']+' / '+p['documentationStatus']+' | '+source+' |')
        lines.append('')
    (ROOT/'MAKERS.md').write_text('\n'.join(lines),encoding='utf-8')
    (ROOT/'MAKER_VISUALS.md').write_text('\n'.join(visual_index)+'\n',encoding='utf-8')
    gaps=[dict(id=p['id'],name=p['name'],brand=p['brand'],reason='Exact-variant image not yet collected or reviewed',sources=[s['url'] for s in p['sources']]) for p in data['parts'] if not p['imageCount']]
    (ROOT/'catalog/maker-image-gaps.json').write_text(json.dumps(dict(records=gaps),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in c['stats'].items() if k.startswith('maker')}))
if __name__=='__main__':main()
