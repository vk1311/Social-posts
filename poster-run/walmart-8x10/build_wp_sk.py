"""Walmart free 8x10 glossy: Waypoint + Staffkin posters, 2400x3000 (300 dpi). Run: python3 build_wp_sk.py"""
import os, sys, base64
HERE = os.path.dirname(os.path.abspath(__file__)); PR = os.path.dirname(HERE); REPO = os.path.dirname(PR)
sys.path.insert(0, os.path.join(PR, "source"))
from prettyqr import pretty_qr, STAFFKIN_RINGS
from playwright.sync_api import sync_playwright
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
F = os.path.join(PR, "walmart-6x8", "fonts")
OUTFIT = "".join(f"@font-face{{font-family:Outfit;font-weight:{w};src:url(data:font/woff2;base64,{b64(f'{F}/outfit-latin-{w}-normal.woff2')})}}" for w in (400, 500, 600))
INK, OFF, MAG = "#0E0E10", "#F7F5F0", "#D81B72"
WMARK = open(os.path.join(REPO, "waypoint", "brand", "waypoint-mark-reversed.svg")).read()
SK_LOGO = "data:image/png;base64," + b64(os.path.join(REPO, "staffkin", "brand", "staffkin-logo-1600.png"))

wp_qr = pretty_qr("https://waypointns.ca/?src=photo-8x10", dot=INK, ring=INK, eye=MAG, logo=None, px=168)
WP = f'''<html><head><meta charset="utf-8"><style>*{{margin:0;box-sizing:border-box}}
body{{width:768px;height:960px;background:{INK};color:#fff;font-family:'Inter Display','Inter',sans-serif;overflow:hidden;position:relative}}</style></head><body>
<div style="padding:64px 60px 0">
 <div style="display:flex;align-items:center;gap:12px"><div style="width:38px;height:38px">{WMARK.replace("<svg ", "<svg style='width:38px;height:38px' ", 1)}</div>
 <div style="font-weight:700;font-size:22px;letter-spacing:.18em;text-transform:uppercase">Waypoint</div></div>
 <div style="font-weight:900;text-transform:uppercase;font-size:104px;line-height:.95;letter-spacing:-.02em;margin-top:64px">Get your<br>evenings<br><span style="color:{MAG}">back.</span></div>
 <div style="font-weight:600;font-size:24px;line-height:1.38;margin-top:36px;max-width:600px;opacity:.88">A website plus the booking, quoting and invoicing tools behind it. Built around how you already work.</div>
</div>
<div style="position:absolute;left:60px;right:60px;bottom:58px;display:flex;align-items:center;gap:28px">
 <div style="flex:none;background:{OFF};padding:12px;border-radius:12px">{wp_qr}</div>
 <div><div style="font-weight:800;font-size:27px;line-height:1.25;text-transform:uppercase">Call or text Vatsal<br><span style="color:{MAG}">902-670-9297</span></div>
 <div style="font-weight:600;font-size:20px;letter-spacing:.06em;margin-top:14px;opacity:.75">waypointns.ca · Atlantic Canada</div></div>
</div></body></html>'''

sk_qr = pretty_qr("https://staffkin.com/?utm_source=photo-8x10", dot="#2E2A6B", ring="#2E2A6B", eye="#7B8CF5", logo=STAFFKIN_RINGS, px=168)
SK = f'''<html><head><meta charset="utf-8"><style>{OUTFIT}*{{margin:0;box-sizing:border-box}}
body{{width:768px;height:960px;background:#fff;color:#2E2A6B;font-family:Outfit,sans-serif;overflow:hidden;position:relative}}</style></head><body>
<div style="padding:64px 60px 0">
 <img src="{SK_LOGO}" style="width:190px;display:block">
 <div style="font-weight:600;font-size:80px;line-height:1.02;letter-spacing:-.015em;margin-top:60px">Hiring sorted.<br>Evenings <span style="color:#7B8CF5">yours</span> again.</div>
 <div style="width:80px;height:7px;background:#7B8CF5;margin-top:28px;border-radius:4px"></div>
 <div style="font-size:24px;line-height:1.42;margin-top:26px;max-width:620px"><b style="font-weight:600">Meet Hollis, your HR deskmate.</b> Job ads, interview questions and reference checks in one place. Data stored in Canada.</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:300px;background:#2E2A6B;color:#fff;display:flex;align-items:center;gap:30px;padding:0 60px">
 <div style="flex:none;background:#fff;padding:12px;border-radius:12px">{sk_qr}</div>
 <div><div style="font-weight:600;font-size:34px;line-height:1.2">Your first job<br>is free.</div>
 <div style="font-weight:500;font-size:21px;letter-spacing:.05em;margin-top:14px;color:#C9CEFB">staffkin.com</div></div>
</div></body></html>'''

with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 768, "height": 960}, device_scale_factor=3.125)
    for name, h in (("staffkin-hiring-sorted-8x10", SK),):
        f = os.path.join(HERE, "_t.html"); open(f, "w").write(h)
        pg.goto("file://" + f); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=os.path.join(HERE, name + ".jpg"), type="jpeg", quality=95); os.remove(f)
    b.close()
print("done")
