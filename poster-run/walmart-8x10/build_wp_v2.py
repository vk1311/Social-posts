"""Waypoint 8x10 redo (Nov 26, 2026): minimal, apology-carousel style. 2400x3000 @300dpi."""
import os, sys, base64
HERE=os.path.dirname(os.path.abspath(__file__)); PR=os.path.dirname(HERE)
sys.path.insert(0, os.path.join(PR,"source"))
from prettyqr import pretty_qr
from playwright.sync_api import sync_playwright
INTER="/home/claude/fonts/Inter.ttf"
FONT=f"@font-face{{font-family:I;font-weight:100 900;src:url(data:font/ttf;base64,{base64.b64encode(open(INTER,'rb').read()).decode()})}}"
INK,OFF,MAG="#0E0E10","#F7F5F0","#D81B72"
def page(bg,fg,head,qr_dot,pill_bg,pill_fg,mark_col):
    qr=pretty_qr("https://waypointns.ca/?src=photo-8x10",dot=qr_dot,ring=qr_dot,eye=MAG if bg!=MAG else INK,logo=None,px=150)
    return f'''<html><head><meta charset="utf-8"><style>{FONT}*{{margin:0;box-sizing:border-box}}
body{{width:768px;height:960px;background:{bg};color:{fg};font-family:I,sans-serif;overflow:hidden;position:relative;text-align:center}}</style></head><body>
<div style="position:absolute;left:0;right:0;top:250px;font-weight:900;font-size:92px;line-height:.98;letter-spacing:-.025em;text-transform:uppercase">{head}</div>
<div style="position:absolute;left:0;right:0;top:640px;display:flex;flex-direction:column;align-items:center;gap:18px">
 <div style="background:{OFF};padding:12px;border-radius:14px">{qr}</div>
 <div style="background:{pill_bg};color:{pill_fg};font-weight:800;font-size:24px;padding:12px 30px;border-radius:40px">waypointns.ca</div>
</div>
<div style="position:absolute;left:0;right:0;bottom:36px;font-weight:600;font-size:16px;letter-spacing:.22em;color:{mark_col}">WAYPOINT</div>
</body></html>'''
A=page(INK,OFF,f'Get your<br>evenings<br><span style="color:{MAG}">back.</span>',INK,OFF,INK,"#8A8A90")
B=page(MAG,OFF,'Close the<br>laptop<br>at five.',INK,OFF,INK,"#F5B8D2")
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":768,"height":960},device_scale_factor=3.125)
    for n,h in (("waypoint-evenings-back-8x10-v2A",A),("waypoint-laptop-at-five-8x10-v2B",B)):
        f=os.path.join(HERE,"_t.html"); open(f,"w").write(h); pg.goto("file://"+f); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(400)
        pg.screenshot(path=os.path.join(HERE,n+".jpg"),type="jpeg",quality=95); os.remove(f)
    b.close()
print("done")
