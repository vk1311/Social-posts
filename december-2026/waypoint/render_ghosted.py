from playwright.sync_api import sync_playwright
INK="#0E0E10"; OFF="#F7F5F0"; MAG="#D81B72"; GREY="#2A2A2E"
base=f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:'Inter Display','Inter',sans-serif;overflow:hidden}}
.s{{width:1080px;height:1350px;position:relative;display:flex;flex-direction:column;justify-content:center;padding:0 90px}}
.dark{{background:{INK};color:#fff}}
.brand{{position:absolute;bottom:64px;left:0;right:0;text-align:center;font-weight:600;font-size:26px;letter-spacing:.18em;text-transform:uppercase;opacity:.55}}
.head{{position:absolute;top:90px;left:90px;right:90px;display:flex;align-items:center;gap:22px;padding-bottom:34px;border-bottom:2px solid #2c2c30}}
.av{{width:84px;height:84px;border-radius:50%;background:#3a3a40;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:36px}}
.nm{{font-weight:700;font-size:38px}} .sub{{font-size:26px;opacity:.5;margin-top:4px}}
.b{{max-width:760px;padding:30px 40px;border-radius:44px;font-size:42px;font-weight:600;line-height:1.25;margin:14px 0}}
.in{{background:{GREY};align-self:flex-start;border-bottom-left-radius:12px}}
.out{{background:{MAG};align-self:flex-end;border-bottom-right-radius:12px}}
.meta{{font-size:26px;opacity:.5;margin:2px 8px 18px}}
.l{{align-self:flex-start}} .r{{align-self:flex-end}}
.stamp{{align-self:center;font-size:28px;font-weight:600;opacity:.45;letter-spacing:.08em;text-transform:uppercase;margin:40px 0 26px}}
.h{{font-weight:900;text-transform:uppercase;letter-spacing:-.015em;line-height:1.02;text-align:center}}
.mag{{color:{MAG}}}"""
HEAD='<div class="head"><div class="av">S</div><div><div class="nm">Sam · Tree Service</div><div class="sub">New enquiry</div></div></div>'
B='<div class="brand">Waypoint</div>'
slides=[
f'''<div class="s dark">{HEAD}
<div class="b in">Hi! Do you do online booking tools? 🌲</div><div class="meta l">Oct 14 · 9:12 a.m.</div>{B}</div>''',
f'''<div class="s dark">{HEAD}
<div class="b in">Hi! Do you do online booking tools? 🌲</div><div class="meta l">Oct 14 · 9:12 a.m.</div>
<div class="stamp">3 weeks later</div>
<div class="b out">So sorry, just seeing this! Yes we do 🙌</div><div class="meta r">Read</div>{B}</div>''',
f'''<div class="s dark">{HEAD}
<div class="stamp" style="margin-top:0">3 weeks later</div>
<div class="b out">So sorry, just seeing this! Yes we do 🙌</div><div class="meta r">Read</div>
<div class="b in">All good! We went with someone else 🙂</div>{B}</div>''',
f'''<div class="s dark" style="align-items:center"><div style="font-weight:600;font-size:34px;letter-spacing:.16em;text-transform:uppercase;opacity:.6;margin-bottom:40px">Fun fact</div>
<div class="h" style="font-size:100px">I build<br><span class="mag" style="white-space:nowrap">auto-replies</span><br>for a living.</div>
<div style="font-size:130px;margin-top:60px">🫠</div>{B}</div>''',
f'''<div class="s" style="background:{MAG};color:{OFF};align-items:center;text-align:center">
<div style="font-weight:600;font-size:34px;letter-spacing:.16em;text-transform:uppercase;opacity:.85">Lesson learned</div>
<div class="h" style="font-size:104px;margin-top:30px">Fix your own stuff first.</div>
<div style="font-weight:700;font-size:48px;margin-top:50px;line-height:1.3">Now every enquiry hears back in seconds.<br>Even at 9 p.m. Even on a ladder.</div>
<div style="margin-top:64px;background:{OFF};color:{INK};border-radius:999px;padding:26px 56px;font-weight:800;font-size:46px">app.waypointns.ca</div>{B}</div>''',
]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1080,"height":1350})
    for i,s in enumerate(slides,1):
        pg.set_content(f"<html><head><style>{base}</style></head><body>{s}</body></html>"); pg.wait_for_timeout(250)
        pg.screenshot(path=f"waypoint-ghosted-{i}.png")
    b.close()
from PIL import Image
ims=[Image.open(f'waypoint-ghosted-{i}.png') for i in range(1,6)]
c=Image.new('RGB',(370*5,450),'#888')
for k,im in enumerate(ims): c.paste(im.resize((360,450)),(k*370,0))
c.save('ghosted-preview.png')
