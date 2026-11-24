from playwright.sync_api import sync_playwright
INK="#0E0E10"; OFF="#F7F5F0"; MAG="#D81B72"
base=f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:'Inter Display','Inter',sans-serif;overflow:hidden}}
.s{{width:1080px;height:1350px;position:relative;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:0 110px}}
.dark{{background:{INK};color:#fff}}
.brand{{position:absolute;bottom:64px;left:0;right:0;font-weight:600;font-size:26px;letter-spacing:.18em;text-transform:uppercase;opacity:.55}}
.h{{font-weight:900;text-transform:uppercase;letter-spacing:-.01em;line-height:1.02}}
.p{{font-weight:800;text-transform:uppercase;line-height:1.18;font-size:58px;letter-spacing:-.005em}}
.mag{{color:{MAG}}}
"""
slides=[
f"""<div class="s dark"><div class="h" style="font-size:118px">We owe you<br>an apology.</div><div class="brand">Waypoint</div></div>""",
f"""<div class="s dark"><div class="p">For making small businesses think good software costs <span class="mag">thousands.</span></div><div class="brand">Waypoint</div></div>""",
f"""<div class="s dark"><div class="p" style="font-size:54px">The truth?<br><br>Most of you just need invoices, quotes, bookings and reviews <span class="mag">sorted.</span></div>
<svg style="margin-top:90px" width="170" height="90" viewBox="0 0 170 90"><path d="M0 32h100V0l70 45-70 45V58H0z" fill="#fff"/></svg><div class="brand">Waypoint</div></div>""",
f"""<div class="s" style="background:{OFF};color:{INK}">
<div style="font-weight:600;font-size:34px;letter-spacing:.16em;text-transform:uppercase;opacity:.6">So we built</div>
<div class="h mag" style="font-size:330px;line-height:.9;letter-spacing:-.04em;margin:18px 0 6px">200</div>
<div class="h" style="font-size:76px">ready-made tools</div>
<div style="display:flex;flex-wrap:wrap;justify-content:center;gap:16px;margin:56px 0 60px;max-width:860px">
{''.join(f'<span style="border:3px solid {INK};border-radius:999px;padding:14px 30px;font-weight:700;font-size:32px">{t}</span>' for t in ['Invoices','Quotes','Bookings','Form replies','Google reviews','+195 more'])}
</div>
<div style="font-weight:800;font-size:52px;line-height:1.2">Most are <span class="mag">free.</span><br>The rest are <span class="mag">$20 CAD.</span></div>
<div class="brand" style="color:{INK}">Waypoint</div></div>""",
f"""<div class="s" style="background:{MAG};color:{OFF}">
<div class="h" style="font-size:150px;letter-spacing:-.03em">Sorry,<br>not sorry.</div>
<div style="font-weight:700;font-size:54px;margin-top:50px">Get your evenings back.</div>
<div style="margin-top:70px;background:{OFF};color:{INK};border-radius:999px;padding:26px 56px;font-weight:800;font-size:46px">app.waypointns.ca</div>
<div style="margin-top:48px;font-weight:600;font-size:30px;opacity:.85">Need something custom? That's still our thing.</div>
<div class="brand">Waypoint</div></div>""",
]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1080,"height":1350})
    for i,s in enumerate(slides,1):
        pg.set_content(f"<html><head><style>{base}</style></head><body>{s}</body></html>")
        pg.wait_for_timeout(200)
        pg.screenshot(path=f"waypoint-apology-{i}.png")
    b.close()
print("done")
