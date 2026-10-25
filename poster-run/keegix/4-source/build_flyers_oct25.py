"""Keegix flyers for the 25 Oct 2026 print pack (21 flyer spots only, page = flyer spot in route order).
  23-FLYER-option-4-airbnb-rules-21-spots.pdf : pretty QR, bigger layout that fills the page (was a third empty)
  22-FLYER-option-3-tearoff-21-spots.pdf      : 9 tear-off tabs, words kept 0.5 in off the bottom edge
Usage: python3 build_flyers_oct25.py <keegix-dropoff-spots-valley.xlsx> <out_dir> <path to poster-run/source>
Needs the source zip unpacked next to this file (fonts/, styles/, logo-lockup-navy.png)."""
import os, sys, json, html
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
XLSX, OUTDIR, SRCDIR = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, SRCDIR); sys.path.insert(0, ROOT)
from prettyqr import pretty_qr, KEEGIX_KEY

src = open(os.path.join(HERE, "build_v3.py"), encoding="utf-8").read().split("\nS = spots")[0]
src = src.replace('/tmp/kt', ROOT).replace('os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "/opt/pw-browsers"', '')
exec(src)
import restyle; restyle.SRC = os.path.join(ROOT, "styles")
os.makedirs(OUTDIR, exist_ok=True)

ws = load_workbook(XLSX)["Drop-off spots"]
flyers = []
for r in ws.iter_rows(min_row=5, values_only=True):
    if isinstance(r[0], int) and any(w in (r[7] or "").lower() for w in ("flyer", "tent", "board")):
        flyers.append(dict(n=r[0], town=r[1], name=r[2], flyer=r[10].lower()))
assert len(flyers) == 21, len(flyers)

def kqr(url):
    return pretty_qr(url, dot="#15304A", ring="#15304A", eye="#F4C430", logo=KEEGIX_KEY, label="QR code to keegix.com")

SPOT_CSS = ".spot{position:absolute;left:.8in;right:.8in;bottom:.3in;font-size:7.5pt;color:#5d6b76;text-align:center}"

# ---- flyer 4: Airbnb house rules, filled out ----
NEWS2_CSS = NEWS_CSS + """
.news .k{top:1.0in}
.news .h{top:1.28in;font-size:54pt;line-height:.98}
.news .t{top:4.25in;width:3.75in;font-size:13.5pt;line-height:1.5}
.news .t p{margin-bottom:.18in}
.news .qb{left:4.85in;top:4.25in;width:2.85in;padding:.28in}
.news .qb .qq{width:2.29in;height:2.29in;padding:.1in}
.news .qb .ql{font-size:12pt}
.news .qb .qu{font-size:9pt}
.news .offer{position:absolute;left:.8in;right:.8in;top:8.05in;background:#FFF6D9;border-left:.08in solid #F4C430;padding:.2in .28in;font-size:13pt;line-height:1.4;color:#15304A}
.news .offer b{font-weight:800}
.news .src{bottom:1.3in}
.news .f{bottom:.62in}
"""
def news2(code):
    url = f"https://keegix.com/airbnb-house-rules?src={code}"
    return f"""<div class="page news"><div class="band kick">Heads up for Airbnb hosts</div>
  <div class="kick k">Starts November 20, 2026</div>
  <div class="serif h">Airbnb's new house rules: <em>is your checkout list still allowed?</em></div>
  <div class="t"><p>Airbnb's new policy says guests shouldn't be asked to do a cleaner's job at checkout: washing dishes, stripping beds, starting laundry or taking garbage off-site.</p>
  <p><b>Check your list free, no sign-up.</b> Paste it in and see what gets flagged, with an allowed version for each chore.</p></div>
  <div class="qb"><div class="qq">{kqr(url)}</div><div class="ql">Scan to check your checkout list</div><div class="qu">keegix.com/airbnb-house-rules</div></div>
  <div class="offer">Keegix also gives each property one guest page and a QR sign by the door. <b>{OFFER}</b> No card.</div>
  <div class="src">Based on Airbnb's house rules announcement to hosts (October 2026). Check Airbnb's help centre for the full policy.</div>
  <div class="f"><img src="file://{ROOT}/logo-lockup-navy.png"><span>Made in Kentville, Nova Scotia · {code.upper()}</span></div>"""

# ---- flyer 3: tear-off, 9 tabs, words clear of the bottom edge ----
TEAR2_CSS = TEAR_CSS + """
.tear .tag{top:5.0in}
.tear .s{top:5.8in}
.tabs{top:8.3in;left:.4in;right:.4in;background:transparent}
.tab{display:flex;justify-content:center;align-items:flex-end;padding-bottom:.55in}
.tab .v{position:static;transform:rotate(180deg);writing-mode:vertical-rl;text-align:center;white-space:nowrap}
.tab .v b{font-size:10pt}
.tab .v span{font-size:7pt}
"""
def tear2(code):
    tabs = "".join('<div class="tab"><div class="v"><b>keegix.com/founding</b><span>Pro free to end of 2027</span></div></div>' for _ in range(9))
    return f"""<div class="page tear"><div class="lg"><img src="file://{ROOT}/logo-lockup-navy.png"></div>
  <div class="kick k">Airbnb, cottage &amp; rental hosts</div>
  <div class="serif h">Rent out a cottage, room or cabin?</div><div class="serif sub"><em>Founding hosts get Pro free until the end of 2027.</em></div>
  <div class="t">{WHAT} No card, no call.</div>
  <div class="tag">{tag_svg(code)}</div>
  <div class="s"><div class="kick sk">Scan, or tear one off</div><div class="su">keegix.com/founding</div><div class="sc">{code.upper()}</div></div>
  <div class="tabs">{tabs}</div>"""

def label(i, s):
    return f'<div class="spot">Page {i} of 21 · Spot {s["n"]}: {esc(s["name"])} ({esc(s["town"])}) · flyer code {s["flyer"].upper()}</div></div>'

jobs = {
    "23-FLYER-option-4-airbnb-rules-21-spots.pdf": doc(NEWS2_CSS + SPOT_CSS, "".join(news2(s["flyer"]) + label(i, s) for i, s in enumerate(flyers, 1))),
    "22-FLYER-option-3-tearoff-21-spots.pdf": doc(TEAR2_CSS + SPOT_CSS.replace("left:.8in;right:.8in;bottom:.3in", "left:3.15in;right:.8in;top:8.05in;text-align:left"), "".join(tear2(s["flyer"]) + label(i, s) for i, s in enumerate(flyers, 1))),
}
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for name, h in jobs.items():
        f = os.path.join(OUTDIR, "_f.html"); open(f, "w", encoding="utf-8").write(h)
        pg.goto(f"file://{f}"); pg.wait_for_timeout(800)
        pg.pdf(path=os.path.join(OUTDIR, name), prefer_css_page_size=True, print_background=True)
        os.remove(f)
    b.close()
print("21 flyer pages each:", list(jobs))
