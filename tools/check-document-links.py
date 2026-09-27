"""Check recorded documentation endpoints; HTTP success is not model validation.

Uses bounded streaming GETs, no authentication, per-host throttling, and a
resumable JSONL cache supplied outside the repository by the caller.
"""
import argparse,concurrent.futures,datetime,ipaddress,json,re,threading,time
from pathlib import Path
from urllib.parse import urlsplit,urldefrag
import requests
ROOT=Path(__file__).resolve().parents[1]
locks={};failures={};lock=threading.Lock()
def public_url(url):
 try:
  p=urlsplit(url)
  if p.scheme not in ['http','https'] or not p.hostname or p.username or p.password:return False
  if p.hostname.lower() in ['localhost','localhost.localdomain'] or p.hostname.endswith(('.local','.internal')):return False
  try:return ipaddress.ip_address(p.hostname).is_global
  except ValueError:return True
 except (TypeError,ValueError):return False
def check(url):
 host=urlsplit(url).hostname
 with lock:gate=locks.setdefault(host,threading.Semaphore(2))
 with gate:
  result={'url':url,'checked':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  with lock:
   if failures.get(host,0)>=6:return dict(result,status='deferred-host-errors',error='Host repeatedly failed; endpoint not checked. Retry this host separately.')
  try:
   with requests.get(url,timeout=(4,8),stream=True,headers={'User-Agent':'BlackWire-Reference-Link-Check/1.0 (+https://github.com/valleytechsolutions/black-wire-pinouts)'}) as r:
    result.update(http=r.status_code,finalUrl=urldefrag(r.url)[0],contentType=r.headers.get('Content-Type','').split(';')[0])
    if r.status_code in [401,403,429]:result['status']='access-limited'
    elif r.status_code in [404,410]:result['status']='not-found'
    elif not r.ok:result['status']='server-error'
    else:
     data=bytearray()
     for chunk in r.iter_content(16384):
      data.extend(chunk)
      if len(data)>=131072:break
     ispdf=data.lstrip().startswith(b'%PDF-')
     expectedPdf=urlsplit(url).path.lower().endswith('.pdf')
     html=data[:131072].decode('utf-8','replace');title=re.search(r'<title[^>]*>(.*?)</title>',html,re.I|re.S)
     result['title']=re.sub(r'\s+',' ',title[1]).strip()[:160] if title else ''
     if expectedPdf and not ispdf:result['status']='unexpected-content'
     elif re.search(r'^(404|page not found|not found|just a moment|access denied|robot check)',result['title'],re.I):result['status']='content-needs-review'
     else:result['status']='reachable'
     result['pdfSignature']=ispdf
     result['sampleBytes']=len(data)
  except requests.RequestException as e:result.update(status='connection-error',error=type(e).__name__)
  with lock:failures[host]=failures.get(host,0)+1 if result['status'] in ['connection-error','server-error'] else 0
  time.sleep(.15)
  return result
def main():
 p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);p.add_argument('--workers',type=int,default=12);a=p.parse_args()
 c=json.loads((ROOT/'library/catalog.json').read_text('utf-8'));urls=set()
 for r in c['boards']+c.get('makerParts',[]):
  d=r.get('documentation',{});sources=([d['website']] if d.get('website') else [])+d.get('resources',[])+r.get('specifications',[])
  for s in sources:
   if public_url(s.get('url')):urls.add(urldefrag(s['url'])[0])
 a.cache.parent.mkdir(parents=True,exist_ok=True)
 done={json.loads(line)['url'] for line in a.cache.read_text('utf-8').splitlines() if line.strip()} if a.cache.exists() else set()
 pending=sorted(urls-done);print(f'{len(urls)} unique endpoints; {len(pending)} pending.',flush=True)
 with a.cache.open('a',encoding='utf-8') as f,concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
  futures=[pool.submit(check,url) for url in pending]
  for i,future in enumerate(concurrent.futures.as_completed(futures),1):
   r=future.result()
   f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
   if i%100==0:print(f'Checked {i}/{len(pending)} endpoints.',flush=True)
 print('Endpoint pass complete. Availability does not validate model, revision or all pin assignments.',flush=True)
if __name__=='__main__':main()
