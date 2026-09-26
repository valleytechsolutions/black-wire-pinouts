"""Validate all catalog references and original hashes without modifying files."""
import hashlib,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1];LIB=ROOT/'library'
def main():
 c=json.loads((LIB/'catalog.json').read_text('utf-8'));manifest=json.loads((LIB/'manifest.json').read_text('utf-8'));errors=[]
 records=[*c['boards'],*c.get('makerParts',[])];ids=[r['id'] for r in records]
 if len(ids)!=len(set(ids)):errors.append('Duplicate listing IDs')
 known={b['id'] for b in c['boards']};hashes={};paths=set(manifest)
 for p in manifest:
  rel=pathlib.PurePosixPath(p)
  if rel.is_absolute() or '..' in rel.parts or '\\' in p or ':' in p:errors.append('Unsafe path: '+p);continue
  if not (LIB/p).is_file():errors.append('Missing manifest file: '+p)
 for r in records:
  for bid in r.get('boardIds',[]):
   if bid not in known:errors.append('Unknown linked board: '+bid)
  for a in r.get('assets',[]):
   for field in ['file','thumb','display','vector','modelOriginal']:
    if a.get(field) and a[field] not in paths:errors.append('Unlisted '+field+': '+a[field])
   for field,hashfield in [('file','hash'),('modelOriginal','modelOriginalHash')]:
    if a.get(field) and a.get(hashfield):
     p=a[field]
     if p in hashes and hashes[p]!=a[hashfield]:errors.append('Contradictory source hash: '+p)
     hashes[p]=a[hashfield]
   if not a.get('rights') or not a.get('review'):errors.append('Missing rights/review: '+a['id'])
 for p,h in hashes.items():
  if (LIB/p).is_file() and hashlib.file_digest((LIB/p).open('rb'),'sha256').hexdigest()!=h:errors.append('Hash mismatch: '+p)
 assets=[a for b in c['boards'] for a in b['assets']]
 expected={'trackedBoards':len(c['boards']),'boardsWithFiles':sum(bool(b['assets']) for b in c['boards']),'referenceEntries':len(assets),'physicalPinouts':sum(a['type']=='pinout image' for a in assets),'makerRecords':len(c.get('makerParts',[]))}
 for k,n in expected.items():
  if c['stats'][k]!=n:errors.append('Incorrect statistic: '+k)
 report={'snapshot':c['editionInfo']['snapshot'],'listings':len(records),'manifestPaths':len(manifest),'hashedFiles':len(hashes),'errors':errors}
 print(json.dumps(report,indent=2));return bool(errors)
if __name__=='__main__':sys.exit(main())
