"""Build original Black Wire SVG connection guides and their public indexes.

Standard library only. Does not alter manufacturer media or approve electrical tests.
Source prose: catalog/wiring-guides.json. Evidence: catalog/wiring-sources.json.
"""
from pathlib import Path
import copy,hashlib,html,json,textwrap
ROOT=Path(__file__).resolve().parents[1];LIB=ROOT/'library'
E=lambda value:html.escape(str(value),quote=True)
INK='#17222e';MUTED='#4d5d6a';RED='#b82736';TEAL='#007c83';GOLD='#946500'

class Drawing:
 def __init__(self):self.parts=[]
 def rect(self,x,y,w,h,fill='#ffffff',stroke='#d2dae1',r=12):self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}"/>')
 def text(self,x,y,value,size=22,color=INK,weight=400,anchor='start'):
  self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{E(value)}</text>')
 def wrap(self,x,y,value,width=88,size=20,color=MUTED):
  lines=textwrap.wrap(value,width=width,break_long_words=False,break_on_hyphens=False)
  for i,line in enumerate(lines):self.text(x,y+i*(size+8),line,size,color)
  return y+len(lines)*(size+8)
 def line(self,x1,y1,x2,y2,color=TEAL,width=4,dash=False):self.parts.append(f'<path d="M {x1} {y1} L {x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="9 7"' if dash else '')+'/>')
 def dot(self,x,y,color=TEAL):self.parts.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{color}"/>')
 def arrow(self,x1,y,x2,direction='right',color=TEAL):
  self.line(x1,y,x2,y,color)
  for x,sign in ([(x2,1)] if direction=='right' else [(x1,-1)] if direction=='left' else [(x1,-1),(x2,1)] if direction=='both' else []):
   self.parts.append(f'<path d="M {x} {y} L {x-12*sign} {y-7} L {x-12*sign} {y+7} Z" fill="{color}"/>')
 def box(self,x,y,w,h,title,sub=''):
  self.rect(x,y,w,h,'#f1f5f7');self.text(x+w/2,y+40,title,24,INK,700,'middle')
  if sub:self.text(x+w/2,y+72,sub,18,MUTED,400,'middle')

def draw(g):
 d=Drawing();spec=g['diagram'];d.rect(0,0,1200,1100,'#fff','#fff',0)
 d.rect(0,0,1200,14,RED,RED,0);d.text(50,59,'BLACK WIRE / WIRING & PROTOCOLS',18,RED,700)
 d.text(50,110,spec['title'],33,INK,700);y=d.wrap(50,148,spec['subtitle'],99,20)+35
 kind=spec['kind']
 if kind=='wires':
  rows=g['connections'];d.box(50,y,345,60,spec['left']);d.box(805,y,345,60,spec['right']);y+=92
  for left,right,note,direction in rows:
   color=RED if 'supply' in left.lower() or '5 V' in left else MUTED if left=='GND' else TEAL
   d.rect(50,y-25,345,57,'#f7f9fb');d.text(70,y+10,left,23,INK,600)
   d.rect(805,y-25,345,57,'#f7f9fb');d.text(825,y+10,right,23,INK,600)
   d.text(600,y-11,note,18,MUTED,400,'middle');d.arrow(410,y+12,790,'none' if left=='GND' else direction,color);y+=75
 elif kind=='ethernet':
  colors={'green':'#26915b','orange':'#e07323','blue':'#2b6cbd','brown':'#875639'}
  d.text(68,y,'CONTACT',18,MUTED,700);d.text(240,y,'T568A',24,INK,700);d.text(750,y,'T568B',24,INK,700);y+=25
  for pin,a,b in g['rows']:
   d.rect(50,y,1100,56,'#f5f8fa');d.text(95,y+37,pin,25,INK,700)
   for x,value in [(210,a),(720,b)]:
    color=next(c for k,c in colors.items() if k in value.lower());d.line(x,y+28,x+105,y+28,color,15)
    if value.lower().startswith('white'):d.line(x,y+28,x+105,y+28,'#fff',6,True)
    d.text(x+130,y+37,value,23)
   y+=65
  y+=10;d.text(50,y,'TWISTED PAIRS: 1-2  /  3-6  /  4-5  /  7-8',23,TEAL,700);y+=32
 elif kind=='bus':
  can=spec['bus']=='can';top=y+155;bottom=top+105
  d.line(120,top,1080,top);d.line(120,bottom,1080,bottom,GOLD)
  for x,label in [(180,'Node A'),(495,'Node B'),(810,'Node C')]:
   d.box(x,y,210,100,label,'CAN transceiver' if can else 'RS-485 transceiver')
   d.line(x+65,y+100,x+65,top);d.dot(x+65,top)
   d.line(x+135,y+100,x+135,bottom,GOLD);d.dot(x+135,bottom,GOLD)
  for x in [120,1080]:
   d.line(x,top,x,top+30,MUTED);d.rect(x-12,top+30,24,45,'#fff',MUTED,0);d.line(x,top+75,x,bottom,MUTED)
   d.text(x,bottom+42,'120 ohm' if can else 'Match Z0',19,INK,600,'middle')
  d.text(420,top-16,'CANH' if can else 'Line A *',24,TEAL,700,'middle')
  d.text(600,bottom+36,'CANL' if can else 'Line B *',24,GOLD,700,'middle')
  y=bottom+105
  d.wrap(50,y,'MCU CAN TX/RX connects through each transceiver. No GPIO connects directly to CANH/CANL.' if can else '* Same part and polarity at every node in this example. Mixed A/B naming must be resolved from truth tables.',91,22);y+=100
  d.wrap(50,y,'Signal reference / isolation and power are not drawn. Design them for the actual ground offsets and transceiver limits.',92,21);y+=85
  d.text(50,y,'Dot = electrical connection. Crossing lines without a dot are not connected.',19,MUTED);y+=38
 elif kind=='i2c':
  d.line(100,y+35,1100,y+35,RED);d.text(600,y+17,'Compatible logic rail',23,RED,700,'middle')
  for x,target in [(450,y+240),(730,y+335)]:
   d.line(x,y+35,x,y+90,RED);d.rect(x-12,y+90,24,52,'#fff',MUTED,0);d.line(x,y+142,x,target);d.dot(x,target)
   d.text(x+28,y+120,'Rp',22,MUTED,600)
  d.box(60,y+170,250,280,'Host MCU');d.box(890,y+170,250,280,'I2C target')
  for yy,label in [(y+240,'SDA'),(y+335,'SCL'),(y+415,'GND')]:
   d.arrow(310,yy,890,'none' if label=='GND' else 'both',MUTED if label=='GND' else TEAL)
   d.text(340,yy-15,label,24,INK,700)
  y+=505;d.wrap(50,y,'Additional targets share SDA/SCL and a compatible reference. Check addresses, total pull-ups and bus capacitance.',94,22);y+=90
 elif kind=='rs232':
  for x,title,sub in [(50,'MCU','Logic-level UART'),(440,'Transceiver','Electrical conversion'),(830,'Remote port','RS-232 interface')]:d.box(x,y+40,320,140,title,sub)
  d.arrow(370,y+110,440,'both');d.arrow(760,y+110,830,'both',RED)
  y+=230
  for a,b,n in [('MCU TX','Transceiver logic input','To remote RX'),('MCU RX','Transceiver logic output','From remote TX'),('Signal reference','According to system design','Isolation may be required')]:
   d.text(70,y,a,23,INK,600);d.text(340,y,b,22);d.text(890,y,n,19,MUTED);y+=68
  y+=30
 elif kind=='rfid':
  for x,title,sub in [(50,'Host MCU','Library / application'),(440,'NFC module','Antenna + controller'),(830,'Test tag / reader','Matching RF protocol')]:d.box(x,y+40,320,140,title,sub)
  d.arrow(370,y+100,440,'both');d.line(760,y+100,830,y+100,TEAL,4,True)
  d.text(405,y+220,'Wired host interface',21,INK,600,'middle');d.text(795,y+260,'13.56 MHz NFC link',21,INK,600,'middle')
  y+=315
  for title,sub in [('READ','Receive supported tag data'),('WRITE','Update supported, writable tag memory'),('EMULATE','Run a supported card application')]:
   d.rect(50,y,1100,66,'#f2f6f7');d.text(70,y+42,title,22,TEAL,700);d.text(280,y+42,sub,24);y+=80
 elif kind=='modes':
  for i,row in enumerate(g['rows']):
   x=50+i*380;d.box(x,y,340,260,row[0]);d.text(x+30,y+110,'Switch 1: '+row[1],25,TEAL,700);d.text(x+30,y+160,'Switch 2: '+row[2],25,TEAL,700)
   d.text(x+30,y+215,'Select one host mode',19,MUTED)
  y+=315;d.wrap(50,y,'Use the corresponding UART, I2C or SPI guide plus the original V3 header drawing. Antenna/card mode is a separate setting.',94,22);y+=90
 else:raise ValueError(kind)
 y+=20;d.line(50,y,1150,y,'#d2dae1',2);y+=34
 y=d.wrap(50,y,g['scope'],105,18)
 y=d.wrap(50,y+8,'Original Black Wire connection diagram. Documentation reviewed; not independently bench-tested.',110,17)
 d.text(50,y+22,'Kal / Valleytech Solutions  |  CC BY 4.0  |  '+g['id']+'  |  2026-09-27',16,RED,600)
 d.text(50,y+49,'Sources: valleytech-black-wire-guide.pages.dev/wiki/wiring/'+g['id']+'/',15,MUTED)
 height=y+78
 d.parts[0]=f'<rect width="1200" height="{height}" fill="#fff"/>'
 metadata=E(json.dumps({'creator':'Kal / Valleytech Solutions','license':'https://creativecommons.org/licenses/by/4.0/','sources':g['sources'],'review':g['review']}))
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc"><title id="title">{E(g["name"])}</title><desc id="desc">{E(g["scope"])}</desc><metadata>{metadata}</metadata><g font-family="Arial, Helvetica, sans-serif">'+''.join(d.parts)+'</g></svg>\n'

def main():
 authored=json.loads((ROOT/'catalog/wiring-guides.json').read_text('utf-8'));sources=json.loads((ROOT/'catalog/wiring-sources.json').read_text('utf-8'))
 catalog=json.loads((LIB/'catalog.json').read_text('utf-8'));known={p['id'] for p in catalog['makerParts']};ids={g['id'] for g in authored['guides']}
 assert len(ids)==len(authored['guides'])
 guides=[];attributions=[]
 for original in authored['guides']:
  g=copy.deepcopy(original);assert all(p in known for p in g['relatedParts']),g['id'];assert set(g['relatedGuides'])<=ids
  g['brand']='Black Wire';g['kind']='wiring-guide';g['revision']=authored['revision'];g['review']='Source documents inspected; independent electrical and bench review pending'
  g['rights']='Original writing and diagram by Kal / Valleytech Solutions, CC BY 4.0. Manufacturer artwork and documentation retain their own rights.'
  g['sources']=[sources[k] for k in g.pop('sourceKeys')]
  raw=draw(g).encode();file='wiring/'+g['id']+'.svg';p=LIB/file;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
  g['image']={'file':file,'hash':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'alt':g['name']+' — '+g['scope'],'type':'original connection diagram'}
  guides.append(g);attributions.append(dict(guide=g['id'],file=file,sha256=g['image']['hash'],creator='Kal / Valleytech Solutions',license='CC-BY-4.0',sources=[s['url'] for s in g['sources']],review=g['review']))
 data=dict(schemaVersion=1,revision=authored['revision'],guides=guides)
 (LIB/'wiring-guides.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n','utf-8')
 (ROOT/'catalog/wiring-attributions.json').write_text(json.dumps(attributions,ensure_ascii=False,indent=2)+'\n','utf-8')
 catalog['wiringGuides']=guides;catalog['stats']['wiringGuides']=len(guides);catalog['stats']['wiringDiagrams']=len(guides)
 (LIB/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,separators=(',',':'))+'\n','utf-8')
 lines=['# Wiring & protocols','','Original Black Wire connection diagrams and concise guides. These are distinct from physical board pinouts.','', '[Open the wiring desk](https://valleytech-black-wire-guide.pages.dev/?tab=wiring)','','Documentation reviewed; not independently bench-tested. Identify exact hardware, connector orientation and logic levels before wiring.','']
 for g in guides:
  route='https://valleytech-black-wire-guide.pages.dev/wiki/wiring/'+g['id']+'/'
  lines.extend([f'## [{g["name"]}]({route})','',g['summary'],'',f'[![{g["name"]}](library/{g["image"]["file"]})](library/{g["image"]["file"]})','',g['scope'],'','Sources: '+' · '.join(f'[{s["title"]}]({s["url"]})' for s in g['sources']),''])
 lines.extend(['Original diagrams and editorial text: Kal / Valleytech Solutions, [CC BY 4.0](LICENSE). Manufacturer sources keep their own rights.',''])
 (ROOT/'WIRING.md').write_text('\n'.join(lines),'utf-8')
 paths=sorted(p.relative_to(LIB).as_posix() for p in LIB.rglob('*') if p.is_file() and p.name!='manifest.json')
 (LIB/'manifest.json').write_text(json.dumps(paths,separators=(',',':'))+'\n','utf-8')
 print(f'Built {len(guides)} original guides and SVG diagrams; board counts unchanged.')
if __name__=='__main__':main()
