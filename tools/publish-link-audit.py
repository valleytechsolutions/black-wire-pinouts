"""Apply a private link-check cache without publishing redirects, titles or errors.

Run after build-maker-index.py and before rebuild-indexes.py. A reachable URL is
not a checked pin assignment or evidence that a datasheet covers the exact PCB.
"""
import argparse,collections,json
from pathlib import Path
from urllib.parse import urldefrag
ROOT=Path(__file__).resolve().parents[1]
def write(path,value):path.write_text(json.dumps(value,ensure_ascii=False,separators=(',',':'))+'\n','utf-8')
def main():
 p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);args=p.parse_args()
 cache={r['url']:r for r in (json.loads(line) for line in args.cache.read_text('utf-8').splitlines() if line.strip())}
 c=json.loads((ROOT/'library/catalog.json').read_text('utf-8'));used={};records=[]
 def annotate(record):
  d=record.get('documentation',{});links=([d['website']] if d.get('website') else [])+d.get('resources',[])+record.get('specifications',[])
  for link in links:
   url=urldefrag(link['url'])[0];r=cache.get(url)
   if not r:continue
   result={k:r[k] for k in ['status','checked','http'] if k in r};link['availability']=result;used[url]=dict(url=url,**result)
  return len(links)
 for kind,rs in [('board',c['boards']),('maker',c.get('makerParts',[]))]:
  for r in rs:records.append(dict(id=r['id'],kind=kind,links=annotate(r)))
 statuses=dict(collections.Counter(r['status'] for r in used.values()))
 summary=dict(endpoints=len(used),listings=len(records),listingsWithLinks=sum(r['links']>0 for r in records),statuses=statuses,note='Bounded public GET requests. HTTP availability does not verify document identity, all pages, revisions or electrical correctness. Deferred endpoints were not requested after repeated host errors. Access restrictions are not proof of a broken link.')
 c['documentationLinkAudit']=summary;write(ROOT/'library/catalog.json',c)
 # Preserve annotations in the maker input as well as generated library output.
 for path in [ROOT/'catalog/maker-parts.json',ROOT/'library/maker-parts.json']:
  m=json.loads(path.read_text('utf-8'))
  for r in m['parts']:annotate(r)
  write(path,m)
 write(ROOT/'catalog/document-link-audit.json',dict(summary=summary,endpoints=sorted(used.values(),key=lambda r:r['url'])))
 lines=['# Documentation endpoint audit','',summary['note'],'',f"{summary['endpoints']} distinct endpoints are associated with {summary['listingsWithLinks']} of {summary['listings']} listings. Missing original-site documentation remains an explicit gap.",'','| Result | Endpoints |','|---|---:|',*[f'| {k} | {v} |' for k,v in sorted(statuses.items())],'','Dates and per-endpoint results are in [the audit data](../catalog/document-link-audit.json). The app shows each recorded availability result beside its document link. Saved documents remain available offline even when the publisher endpoint is unavailable.','','These results are a point-in-time observation, not a promise that a remote page will remain available. Unknown model scope, missing datasheets, source conflicts and independent wiring validation require further review.','']
 (ROOT/'docs/LINK-AUDIT.md').write_text('\n'.join(lines),'utf-8');print(json.dumps(summary))
if __name__=='__main__':main()
