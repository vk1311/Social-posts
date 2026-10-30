"""8 Walmart 6x8 photo prints (30 Oct 2026 free-print deal). Each print = 4 identical 3x4 in cards, cut in a cross.
Two headlines per brand, each with its own QR tag, so scans show which one works.
Run: python3 build.py  -> 8 JPGs (1800x2400, 300 dpi) in this folder."""
import os, sys, base64
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(os.path.dirname(HERE), "source"); sys.path.insert(0, SRC)
from prettyqr import pretty_qr, STAFFKIN_RINGS, KEEGIX_KEY
from playwright.sync_api import sync_playwright
REPO = os.path.dirname(os.path.dirname(HERE))
def b64(p): return base64.b64encode(open(p, "rb").read()).decode()
F = os.path.join(HERE, "fonts")
FONTS = "".join(f"@font-face{{font-family:Outfit;font-weight:{w};src:url(data:font/woff2;base64,{b64(f'{F}/outfit-latin-{w}-normal.woff2')})}}" for w in (400, 500, 600)) + \
    f"@font-face{{font-family:Archivo;font-weight:400 800;font-stretch:62% 125%;src:url(data:font/woff2;base64,{b64(F+'/Archivo-normal.woff2')})}}" + \
    f"@font-face{{font-family:Newsreader;font-weight:400 600;src:url(data:font/woff2;base64,{b64(F+'/Newsreader-normal.woff2')})}}" + \
    f"@font-face{{font-family:Newsreader;font-style:italic;font-weight:400 600;src:url(data:font/woff2;base64,{b64(F+'/Newsreader-italic.woff2')})}}"
GF = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@700;800&family=DM+Sans:wght@400;500;700&display=swap">'
sys.path.insert(0, SRC)
import importlib.util
spec = importlib.util.spec_from_file_location("gp", os.path.join(SRC, "gen_print.py"))
src = open(os.path.join(SRC, "gen_print.py")).read().split("\nW, H = 816, 1056")[0]
g = {"__file__": os.path.join(SRC, "gen_print.py")}; exec(src, g)
WMARK = g["mark"](40)
SK_LOGO = open(os.path.join(SRC, "staffkin", "assets", "staffkin-logo.svg")).read()
KG_LOGO = "data:image/png;base64," + b64(os.path.join(REPO, "keegix", "brand", "logo-lockup-navy.png"))

def card(brand, head, sub, url, foot, contact):
    if brand == "wp":
        qr = pretty_qr(url, logo=None, px=126); bg, ink, acc = "#FBF9F4", "#12252F", "#C2185B"
        logo = f'<div style="display:flex;align-items:center;gap:7px">{WMARK}<b style="font-family:Manrope;font-size:15px">Waypoint</b></div>'
        hf = "font-family:Manrope,sans-serif;font-weight:800;letter-spacing:-.02em"; bf = "font-family:'DM Sans',sans-serif"
    elif brand == "ap":
        qr = pretty_qr(url, logo=None, px=126); bg, ink, acc = "#FBF9F4", "#12252F", "#C2185B"
        logo = f'<div style="display:flex;align-items:center;gap:7px">{WMARK}<b style="font-family:Manrope;font-size:15px">Waypoint Apps</b></div>'
        hf = "font-family:Manrope,sans-serif;font-weight:800;letter-spacing:-.02em"; bf = "font-family:'DM Sans',sans-serif"
    elif brand == "sk":
        qr = pretty_qr(url, dot="#2E2A6B", ring="#2E2A6B", eye="#7B8CF5", logo=STAFFKIN_RINGS, px=126); bg, ink, acc = "#FFFFFF", "#2E2A6B", "#7B8CF5"
        logo = f'<div style="height:24px;width:100px">{SK_LOGO.replace("<svg ", "<svg style=\'width:100px;height:24px\' ", 1)}</div>'
        hf = "font-family:Outfit,sans-serif;font-weight:600;letter-spacing:-.01em"; bf = "font-family:Outfit,sans-serif"
    else:
        qr = pretty_qr(url, dot="#15304A", ring="#15304A", eye="#15304A", logo=KEEGIX_KEY, px=126); bg, ink, acc = "#FFFFFF", "#15304A", "#F4C430"
        logo = f'<img src="{KG_LOGO}" style="width:92px;display:block">'
        hf = "font-family:Newsreader,serif;font-weight:500;letter-spacing:-.02em"; bf = "font-family:Archivo,sans-serif"
    return f'''<div style="position:relative;width:288px;height:384px;box-sizing:border-box;padding:24px 24px 22px;background:{bg};color:{ink};{bf};display:flex;flex-direction:column;overflow:hidden">
{logo}
<div style="{hf};font-size:27px;line-height:1.04;margin-top:14px;text-wrap:balance">{head}</div>
<div style="width:46px;height:5px;background:{acc};margin-top:10px"></div>
<div style="font-size:12.5px;line-height:1.35;margin-top:9px;opacity:.9">{sub}</div>
<div style="margin-top:auto;display:flex;gap:12px;align-items:center">
<div style="flex:none;background:#fff;padding:5px;border:2px solid {ink};border-radius:6px">{qr}</div>
<div style="font-size:12.5px;line-height:1.35;white-space:nowrap"><b>{contact}</b></div></div>
<div style="font-size:12px;letter-spacing:.06em;margin-top:9px">{foot}</div></div>'''

P = [
 ("1-waypoint-by-hand", "wp", "Still doing it by hand?", "Quotes, invoices and bookings in one tool, built around how you already work.", "https://waypointns.ca/?src=photo-byhand", "waypointns.ca", "Call or text<br>Vatsal<br>902-670-9297"),
 ("2-waypoint-fit", "wp", "I make the software fit your business.", "From nothing to built. You deal with me start to finish.", "https://waypointns.ca/?src=photo-fit", "waypointns.ca", "Call or text<br>Vatsal<br>902-670-9297"),
 ("3-apps-whole-business", "ap", "Digitize your <span style='color:#C2185B'>whole</span> business.", "Invoices, quotes, stock, customers and staff. Simple apps, one login.", "https://app.waypointns.ca/?src=photo-whole", "app.waypointns.ca", "Start free.<br>No card needed."),
 ("4-apps-markets", "ap", "Selling at markets or online?", "Invoices, stock that keeps count and a price list with photos, from your phone.", "https://app.waypointns.ca/?src=photo-market", "app.waypointns.ca", "Start free.<br>No card needed."),
 ("5-staffkin-hiring", "sk", "Hiring this month?", "Job ad, interview questions and reference checks in one place. Data stored in Canada.", "https://staffkin.com/?utm_source=photo-hiring", "staffkin.com", "Your first job<br>is free."),
 ("6-staffkin-paperwork", "sk", "Hire people, not paperwork.", "A simple hiring kit for businesses with 1 to 50 people and no HR department.", "https://staffkin.com/?utm_source=photo-paperwork", "staffkin.com", "Your first job<br>is free."),
 ("7-keegix-cottage", "kg", "Rent out a cottage, room or <i>cabin?</i>", "One guest page per property, opened from a QR sign by the door.", "https://keegix.com/founding?src=photo-cottage", "keegix.com/founding", "Pro free until<br>end of 2027."),
 ("8-keegix-guests", "kg", "Hosting guests in the <i>Valley?</i>", "Check-in steps, parking, house rules and local picks on one page. Change it once, every guest sees it.", "https://keegix.com/founding?src=photo-guests", "keegix.com/founding", "Pro free until<br>end of 2027."),
]
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 576, "height": 768}, device_scale_factor=3.125)
    for name, *args in P:
        c = card(*args)
        h = f'''<html><head><meta charset="utf-8">{GF}<style>{FONTS}*{{margin:0}}body{{width:576px;height:768px}}</style></head><body>
<div style="display:grid;grid-template-columns:288px 288px;width:576px;height:768px">{c*4}</div>
<div style="position:absolute;left:287px;top:0;bottom:0;border-left:1.5px dashed #9aa7b0"></div>
<div style="position:absolute;top:383px;left:0;right:0;border-top:1.5px dashed #9aa7b0"></div></body></html>'''
        f = os.path.join(HERE, "_t.html"); open(f, "w").write(h)
        pg.goto("file://" + f); pg.wait_for_load_state("networkidle"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
        pg.screenshot(path=os.path.join(HERE, name + ".jpg"), type="jpeg", quality=95, clip={"x": 0, "y": 0, "width": 576, "height": 768})
        os.remove(f)
    b.close()
print("done")
