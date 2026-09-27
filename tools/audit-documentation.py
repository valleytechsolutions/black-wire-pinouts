"""Inventory exact-model documentation without promoting chip data to board data.

Known publisher domains identify recorded manufacturer links, not live-page checks.
Only reviewed, explicitly typed resources count as board datasheets.
"""
import collections,csv,json,re,datetime
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
DOMAINS={
 'Inland':['microcenter.com','microcenter.zendesk.com'],'Texas Instruments':['ti.com'],'Microchip':['microchip.com'],'Silicon Labs':['silabs.com'],
 'Adafruit':['adafruit.com'],'SparkFun':['sparkfun.com'],'FriendlyELEC':['friendlyelec.com','friendlyarm.com'],
 'NVIDIA':['nvidia.com'],'Raspberry Pi':['raspberrypi.com','raspberrypi.org'],'Arduino':['arduino.cc'],
 'Seeed Studio':['seeedstudio.com'],'M5Stack':['m5stack.com'],'Waveshare':['waveshare.com'],'LILYGO':['lilygo.cc'],
 'Espressif':['espressif.com'],'Banana Pi':['banana-pi.org','banana-pi.com'],'Orange Pi':['orangepi.org'],
 'Heltec':['heltec.org'],'RAKwireless':['rakwireless.com'],'Pimoroni':['pimoroni.com'],'Elecrow':['elecrow.com'],
 'Unexpected Maker':['unexpectedmaker.com'],'Luckfox':['luckfox.com'],'Wemos':['wemos.cc'],'LOLIN':['wemos.cc'],
 'PJRC':['pjrc.com'],'Radxa':['radxa.com'],'LattePanda':['lattepanda.com'],'Milk-V':['milkv.io'],
 'BeagleBoard.org':['beagleboard.org'],'STMicroelectronics':['st.com'],'Sipeed':['sipeed.com'],
 'Olimex':['olimex.com'],'DFRobot':['dfrobot.com'],'Antmicro':['antmicro.com'],'Cytron Technologies':['cytron.io'],
 'NodeMCU':['nodemcu.com'],'WIZnet':['wiznet.io'],'Flipper Devices':['flipper.net','flipperzero.one'],
 'TinyCircuits':['tinycircuits.com'],'Spotpear':['spotpear.com'],'HardKernel':['hardkernel.com','odroid.com'],
 'BrisbaneSilicon':['brisbanesilicon.com.au'],'Terasic':['terasic.com.tw','terasic.com'],'Nologo':['nologo.tech'],
}
OWNERS={'Adafruit':['adafruit'],'SparkFun':['sparkfun'],'Espressif':['espressif'],'LILYGO':['xinyuan-lilygo'],'WeAct Studio':['weactstudio'],'M5Stack':['m5stack'],'Seeed Studio':['seeed-studio'],'RAKwireless':['rakwireless'],'Sipeed':['sipeed'],'Antmicro':['antmicro'],'Waveshare':['waveshareteam']}
def valid(url):
 try:
  p=urlsplit(url)
  return p.scheme in ['https','http'] and bool(p.hostname) and not p.username and not p.password
 except (ValueError,TypeError):return False
def original(brand,url):
 if not valid(url):return False
 p=urlsplit(url);host=p.hostname.lower()
 return any(host==d or host.endswith('.'+d) for d in DOMAINS.get(brand,[])) or (host=='github.com' and p.path.strip('/').split('/')[0].lower() in OWNERS.get(brand,[]))
def main():
 path=ROOT/'library/catalog.json';c=json.loads(path.read_text('utf-8'));boards={b['id']:b for b in c['boards']};rows=[]
 for kind,records in [('board',c['boards']),('maker',c['makerParts'])]:
  for r in records:
   assets=list({a['file']:a for a in [*r.get('assets',[]),*(a for bid in r.get('boardIds',[]) for a in boards[bid]['assets'])]}.values())
   d=r.setdefault('documentation',{'resources':[]})
   if not d.get('website'):
    sources=[s if isinstance(s,str) else s.get('url') for s in r.get('sources',[])]
    sources += [s.get('url') for s in r.get('specifications',[])]
    sources += [s for a in assets for s in [*a.get('sources',[]),a.get('url')]]
    candidates=[u for u in sources if original(r['brand'],u) and not re.search(r'\.(png|jpg|jpeg|svg|webp|gif|pdf|zip)(?:$|[?#])',u,re.I)]
    if candidates:d['website']={'url':candidates[0],'label':'Manufacturer source (recorded link)','scope':'recorded-source','checked':None}
   resources=[x for x in d.get('resources',[]) if valid(x.get('url'))]
   datasheets=[x for x in resources if x.get('kind')=='datasheet' and x.get('scope')=='board']
   guides=[x for x in resources if x.get('kind')=='hardware-guide' and x.get('scope')=='board']
   visual=sum(a.get('type')!='chip-package reference' and (bool(a.get('thumb')) or a.get('extension') in ['png','jpg','jpeg','webp','svg','gif']) for a in assets)
   missing=[]
   if not datasheets:missing.append('Board datasheet not yet recorded')
   if not d.get('website'):missing.append('Original manufacturer website not yet identified')
   if not visual:missing.append('Board/device visual reference still needed')
   r['documentationCoverage']={'boardDatasheets':len(datasheets),'hardwareGuides':len(guides),'schematics':sum(x.get('kind')=='schematic' for x in resources),'componentDatasheets':sum(x.get('kind')=='datasheet' and x.get('scope')=='component' for x in resources),'visualCount':visual,'websiteStatus':'checked-model-page' if d.get('website',{}).get('checked') and d['website'].get('scope')=='model' else 'recorded-not-rechecked' if d.get('website') else 'missing','missing':missing}
   rows.append(dict(id=r['id'],name=r['name'],brand=r['brand'],kind=kind,**r['documentationCoverage'],website=d.get('website',{}).get('url','')))
 summary={kind:{'listings':len(rs),'withBoardDatasheet':sum(r['boardDatasheets']>0 for r in rs),'withHardwareGuide':sum(r['hardwareGuides']>0 for r in rs),'withVisual':sum(r['visualCount']>0 for r in rs),'withRecordedWebsite':sum(bool(r['website']) for r in rs),'checkedModelWebsite':sum(r['websiteStatus']=='checked-model-page' for r in rs)} for kind in ['board','maker'] for rs in [[r for r in rows if r['kind']==kind]]}
 c['documentationAudit']={'checked':datetime.date.today().isoformat(),'summary':summary,'note':'An inventory audit. Separate endpoint-availability results, when present, do not validate model scope or pin assignments. Typed board datasheets, component datasheets and hardware guides are distinct. Unknown or unclassified documents remain gaps.'}
 def write(p,o):p.write_text(json.dumps(o,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
 write(path,c)
 maker_path=ROOT/'library/maker-parts.json';m=json.loads(maker_path.read_text('utf-8'));m['parts']=c['makerParts'];write(maker_path,m)
 write(ROOT/'catalog/documentation-coverage.json',dict(**c['documentationAudit'],records=rows))
 with (ROOT/'catalog/documentation-coverage.csv').open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows([{**r,'missing':'; '.join(r['missing'])} for r in rows])
 lines=['# Documentation coverage','','Every catalog listing has an explicit datasheet, original-website and visual status. These are listing counts; linked records can describe the same hardware. Only typed board-level datasheets count. A product photo, schematic or chip datasheet is not a complete board pinout.','','| Listings | Board datasheet | Hardware manual | Visual reference | Recorded manufacturer link | Checked model page |','|---|---:|---:|---:|---:|---:|']
 for k,s in summary.items():lines.append(f"| {k}: {s['listings']} | {s['withBoardDatasheet']} | {s['withHardwareGuide']} | {s['withVisual']} | {s['withRecordedWebsite']} | {s['checkedModelWebsite']} |")
 lines+=['','A missing datasheet status means the exact board datasheet has not been classified and recorded here; it does not prove the manufacturer never published one. New hardware manuals and schematics are linked separately. Links marked recorded have not all been revisited. Saved source documents are available offline; external links require internet access.','','[Per-listing CSV](catalog/documentation-coverage.csv) · [Machine-readable evidence](catalog/documentation-coverage.json) · [Pinout coverage](PINOUT_COVERAGE.md)','']
 (ROOT/'DOCUMENTATION.md').write_text('\n'.join(lines),encoding='utf-8');print(json.dumps(summary))
if __name__=='__main__':main()
