"""Account for every catalog listing without equating photos with pinouts."""
import collections,csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def coverage(record,assets):
    physical=[a for a in assets if a['type']=='pinout image']
    functions=record.get('pinReferences',[]) or [a for a in assets if a['type']=='pin function reference']
    return {
        'status':'pinout-source' if physical else 'functions-only' if functions else 'reference-only' if assets else 'missing',
        'physicalCount':len(physical),'functionTableCount':len(functions),'functionSheetCount':sum(a['type']=='pin function reference' for a in assets),
        'purposeRows':sum(len(t['pins']) for t in record.get('pinReferences',[])),
        'completeDeviceApproved':False,
        'scope':'Source pinout available; check its connector scope and revision. All-pin completeness has not been independently approved.' if physical else 'Pin functions documented; use the matching source image to locate the connector. Physical order is not established by a function table.' if functions else 'A physical pinout and per-pin purpose reference are still needed. Photos and other supporting documents do not establish pin order.',
        'missing':['Independent all-connector completeness review','Revision match and electrical limits'] if physical else ['Physical connector map','Independent all-connector completeness review','Revision match and electrical limits'],
    }

def main():
    path=ROOT/'library/catalog.json';c=json.loads(path.read_text(encoding='utf-8'));boards={b['id']:b for b in c['boards']};rows=[]
    for kind,records in [('board',c['boards']),('maker',c['makerParts'])]:
        for p in records:
            assets=list({a['file']:a for a in [*p.get('assets',[]),*(a for bid in p.get('boardIds',[]) for a in boards[bid]['assets'])]}.values())
            p['pinoutCoverage']=coverage(p,assets)
            rows.append(dict(id=p['id'],name=p['name'],brand=p['brand'],kind=kind,**p['pinoutCoverage']))
    summary={kind:dict(collections.Counter(r['status'] for r in rows if r['kind']==kind)) for kind in ['board','maker']}
    c['pinoutAudit']={'checked':'2026-09-26','listingCount':len(rows),'countsAreListingsNotUniqueHardware':True,'completeDeviceApprovals':0,'summary':summary}
    path.write_text(json.dumps(c,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    (ROOT/'catalog/pinout-coverage.json').write_text(json.dumps(dict(**c['pinoutAudit'],records=rows),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (ROOT/'catalog/pinout-coverage.csv').open('w',newline='',encoding='utf-8') as f:
        fields=['id','name','brand','kind','status','physicalCount','functionSheetCount','functionTableCount','purposeRows','completeDeviceApproved','missing']
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
        for r in rows:w.writerow({**r,'missing':'; '.join(r['missing'])})
    (ROOT/'PINOUT_COVERAGE.md').write_text('# Pinout coverage audit\n\nEvery board and maker listing is accounted for. Linked maker/board records can describe the same hardware; listing totals are not unique-product counts. A source pinout is not independent approval of every connector. Product photos never count as pinouts.\n\n| Listing type | Source pinout | Functions only | Supporting references only | No reference |\n|---|---:|---:|---:|---:|\n'+''.join(f"| {kind} | {s.get('pinout-source',0)} | {s.get('functions-only',0)} | {s.get('reference-only',0)} | {s.get('missing',0)} |\n" for kind,s in summary.items())+'\n[Full CSV](catalog/pinout-coverage.csv) · [Evidence and remaining work](catalog/pinout-coverage.json)\n\nNo new complete-device approval is inferred from these counts. The app displays the same coverage status beside each record.\n',encoding='utf-8')
    print(json.dumps(c['pinoutAudit']))
if __name__=='__main__':main()
