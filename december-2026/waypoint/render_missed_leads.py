from playwright.sync_api import sync_playwright
INK="#0E0E10"; OFF="#F7F5F0"; MAG="#D81B72"
base=f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:'Inter Display','Inter',sans-serif;overflow:hidden}}
.s{{width:1080px;height:1350px;position:relative;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 100px}}
.dark{{background:{INK};color:#fff}}
.brand{{position:absolute;bottom:64px;left:0;right:0;font-weight:600;font-size:26px;letter-spacing:.18em;text-transform:uppercase;opacity:.55}}
.h{{font-weight:900;text-transform:uppercase;letter-spacing:-.015em;line-height:1.04}}
.p{{font-weight:800;text-transform:uppercase;line-height:1.18;font-size:62px}}
.mag{{color:{MAG}}}"""
B='<div class="brand">Waypoint</div>'
slides=[
f'<div class="s dark"><div class="h" style="font-size:100px">I missed <span class="mag">2 leads</span> because I didn\'t reply on time.</div>{B}</div>',
f'<div class="s dark"><div class="h" style="font-size:120px">Yes, <span class="mag">me.</span></div><div class="p" style="font-size:50px;margin-top:50px;opacity:.9">Not a sales pitch.<br>I actually missed them.</div>{B}</div>',
f'<div class="s" style="background:{OFF};color:{INK}"><div class="h mag" style="font-size:300px;line-height:.9;letter-spacing:-.04em">2</div><div class="h" style="font-size:76px;margin-top:20px">potential clients.</div><div class="p" style="font-size:52px;margin-top:50px">A huge opportunity cost.</div><div class="brand" style="color:{INK}">Waypoint</div></div>',
f'<div class="s dark"><div class="p" style="font-size:60px">All because I wasn\'t checking messages while I was busy with <span class="mag">client work.</span></div>{B}</div>',
f'<div class="s dark"><div style="font-weight:600;font-size:34px;letter-spacing:.16em;text-transform:uppercase;opacity:.6;margin-bottom:44px">That\'s when I decided</div><div class="p" style="font-size:60px"><span class="mag">To actually build the flows.</span></div>{B}</div>',
f'<div class="s" style="background:{MAG};color:{OFF}"><div style="font-weight:600;font-size:34px;letter-spacing:.16em;text-transform:uppercase;opacity:.85">Lesson learned</div><div class="h" style="font-size:112px;margin-top:26px">Do your own stuff first.</div><div style="margin-top:80px;display:flex;align-items:center;gap:34px;background:{OFF};color:{INK};border-radius:40px;padding:34px 50px 34px 34px;text-align:left"><div style="width:150px;height:150px"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="150" height="150" role="img" aria-label="Waypoint">   <line x1="55.10" y1="107.56" x2="43.43" y2="24.59" stroke="#2F4A56" stroke-width="0.78"/>   <line x1="30.73" y1="34.51" x2="108.42" y2="65.90" stroke="#2F4A56" stroke-width="0.78"/>   <line x1="106.17" y1="49.93" x2="40.15" y2="101.52" stroke="#2F4A56" stroke-width="0.78"/>   <line x1="64.00" y1="9.44" x2="64.00" y2="114.84" stroke="#2F4A56" stroke-width="0.78"/>   <polygon points="70.20,62.14 70.20,65.86 118.56,64.00" fill="#2F4A56"/>   <polygon points="57.80,62.14 57.80,65.86 9.44,64.00" fill="#2F4A56"/>   <line x1="46.40" y1="74.15" x2="59.70" y2="51.10" stroke="#C2185B" stroke-width="1.36" stroke-linecap="round"/>   <line x1="81.60" y1="74.15" x2="68.30" y2="51.10" stroke="#C2185B" stroke-width="1.36" stroke-linecap="round"/>   <polygon points="64.00,37.96 86.55,77.02 41.45,77.02" fill="none" stroke="#12252F" stroke-width="2.85" stroke-linejoin="round"/>   <circle cx="64.00" cy="37.96" r="3.10" fill="#C2185B"/>   <circle cx="86.55" cy="77.02" r="3.10" fill="#C2185B"/>   <circle cx="41.45" cy="77.02" r="3.10" fill="#C2185B"/>   <circle cx="64.00" cy="64.00" r="4.34" fill="#C2185B"/> </svg> </div><div><div style="font-weight:900;font-size:50px;letter-spacing:-.01em">WAYPOINT</div><div style="font-weight:700;font-size:40px;margin-top:8px">waypointns.ca</div><div style="font-weight:700;font-size:40px;margin-top:4px;color:{MAG}">902-670-9297</div></div></div></div>',
]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1080,"height":1350})
    for i,s in enumerate(slides,1):
        pg.set_content(f"<html><head><style>{base}</style></head><body>{s}</body></html>"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"waypoint-missed-leads-{i}.png")
    b.close()
from PIL import Image
c=Image.new('RGB',(370*6,450),'#888')
for k in range(6): c.paste(Image.open(f'waypoint-missed-leads-{k+1}.png').resize((360,450)),(k*370,0))
c.save('missed-preview.png')
