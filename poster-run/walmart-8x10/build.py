"""Walmart free 8x10 glossy (Black Friday deal, ends 26 Nov 2026). One Keegix poster, 2400x3000 (300 dpi).
Run: python3 build.py"""
import os, sys, base64
HERE = os.path.dirname(os.path.abspath(__file__)); PR = os.path.dirname(HERE); REPO = os.path.dirname(PR)
sys.path.insert(0, os.path.join(PR, "source"))
from prettyqr import pretty_qr, KEEGIX_KEY
from playwright.sync_api import sync_playwright
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
F = os.path.join(PR, "walmart-6x8", "fonts")
FONTS = f"@font-face{{font-family:Archivo;font-weight:400 800;font-stretch:62% 125%;src:url(data:font/woff2;base64,{b64(F+'/Archivo-normal.woff2')})}}" + \
    f"@font-face{{font-family:Newsreader;font-weight:400 600;src:url(data:font/woff2;base64,{b64(F+'/Newsreader-normal.woff2')})}}" + \
    f"@font-face{{font-family:Newsreader;font-style:italic;font-weight:400 600;src:url(data:font/woff2;base64,{b64(F+'/Newsreader-italic.woff2')})}}"
LOGO = "data:image/png;base64," + b64(os.path.join(REPO, "keegix", "brand", "logo-lockup-navy.png"))
PHOTO = "data:image/jpeg;base64," + b64(os.path.join(REPO, "keegix", "photos", "cottage-porch-yellow-door.jpg"))
URL = "https://keegix.com/founding?src=photo-8x10"
qr = pretty_qr(URL, dot="#15304A", ring="#15304A", eye="#15304A", logo=KEEGIX_KEY, px=168)
html = f'''<html><head><meta charset="utf-8"><style>{FONTS}*{{margin:0;box-sizing:border-box}}
body{{width:768px;height:960px;background:#fff;color:#15304A;font-family:Archivo,sans-serif;overflow:hidden}}</style></head><body>
<div style="height:372px;background:url({PHOTO}) 72% 55%/cover"></div>
<div style="padding:30px 56px 0">
 <img src="{LOGO}" style="width:150px;display:block">
 <div style="font-family:Newsreader,serif;font-weight:500;font-size:58px;line-height:1.02;letter-spacing:-.02em;margin-top:14px">Check-in night.<br>Your phone stays <i>quiet.</i></div>
 <div style="width:80px;height:7px;background:#F4C430;margin-top:20px"></div>
 <div style="font-size:19px;line-height:1.4;margin-top:16px;color:#4E5C66;max-width:620px">Check-in steps, parking, house rules and local picks on one guest page. Guests scan the sign by the door.</div>
</div>
<div style="margin:30px 56px 0;display:flex;align-items:center;gap:26px">
 <div style="flex:none;background:#fff;padding:9px;border:3px solid #15304A;border-radius:10px">{qr}</div>
 <div><div style="font-size:26px;font-weight:700;line-height:1.2">Pro free until<br>end of 2027.</div>
 <div style="font-size:19px;letter-spacing:.05em;margin-top:12px">keegix.com/founding</div></div>
</div></body></html>'''
f = os.path.join(HERE, "_t.html"); open(f, "w").write(html)
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 768, "height": 960}, device_scale_factor=3.125)
    pg.goto("file://" + f); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
    pg.screenshot(path=os.path.join(HERE, "keegix-quiet-phone-8x10.jpg"), type="jpeg", quality=95); b.close()
os.remove(f); print("done")
