"""Validate editable maker intake, then generate application and Markdown indexes."""
import collections,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def main():
    data=json.loads((ROOT/'catalog/maker-parts.json').read_text(encoding='utf-8'))
    c=json.loads((ROOT/'library/catalog.json').read_text(encoding='utf-8'))
    ids=set();boardids={b['id'] for b in c['boards']}
    for p in data['parts']:
        assert p['id'] not in ids and re.fullmatch('[a-z0-9-]+',p['id']),p['id'];ids.add(p['id'])
        assert p['name'] and p['category'] and p['brand']
        assert not p['completePhysicalPinout'],'This intake compiler cannot approve physical pinouts'
        assert set(p['boardIds'])<=boardids
        for s in p['sources']:assert s['url'].startswith('https://')
        if p['documentationStatus']=='Manufacturer documentation recorded':
            assert p['sources'] and all(re.fullmatch('[a-f0-9]{64}',s.get('sha256','')) for s in p['sources'])
        if p['pinLabels']:assert p['sources'] and p['identityKind']!='generic-family'
    c['makerParts']=data['parts'];c['makerScope']={k:v for k,v in data.items() if k!='parts'}
    c['stats'].update(makerRecords=len(ids),makerDocumented=sum(p['documentationStatus']=='Manufacturer documentation recorded' for p in data['parts']),makerGenericFamilies=sum(p['identityKind']=='generic-family' for p in data['parts']))
    (ROOT/'library/catalog.json').write_text(json.dumps(c,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    (ROOT/'library/maker-parts.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    lines=['# Displays, sensors and maker modules','',data['scope'],'',data['countMeaning'],'',f"**{len(ids)} intake records**. {c['stats']['makerDocumented']} manufacturer documentation records. No new complete physical pinout approvals in this intake.",'','[Search the interactive guide](https://valleytech-black-wire-guide.pages.dev/?tab=makers) · [Expansion roadmap](docs/MAKER_ROADMAP.md) · [Coverage backlog](catalog/maker-research-backlog.json)','','Search by product/controller code first; filter by interface, function, technology or recorded display size. A blank field means unknown, not universal compatibility. Pin-label lists do not give physical connector order.','']
    groups=collections.defaultdict(list)
    for p in data['parts']:groups[p['category']].append(p)
    for cat,parts in sorted(groups.items()):
        lines += ['## '+cat,'','| Product or family | Manufacturer | Record status | Source |','|---|---|---|---|']
        for p in parts:
            source='[Documentation]('+p['sources'][0]['url']+')' if p['sources'] else 'Identification needed'
            lines.append('| '+p['name'].replace('|','/')+' | '+p['brand']+' | '+p['identityKind']+' / '+p['documentationStatus']+' | '+source+' |')
        lines.append('')
    (ROOT/'MAKERS.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({k:v for k,v in c['stats'].items() if k.startswith('maker')}))
if __name__=='__main__':main()
