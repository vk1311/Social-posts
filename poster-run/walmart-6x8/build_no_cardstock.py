"""Walmart 6x8 prints that replace ALL the cardstock (30 Oct 2026). One-sided, 4 cards per print unless noted.
  k-spots/  37 prints: Keegix key cards per drop-off spot (4 cards, that spot's code C##, same links as the cardstock cards)
  k-mail/    8 prints: Keegix mail cards M01-M30 + 2 spares (one per letter, numbered)
  s-postcard/ 2 prints: Staffkin reference-check postcard, 2 per print (6 x 4 in each); stick an address label + stamp on the back
Run: python3 build_no_cardstock.py"""
import os, re, openpyxl, html
from build import card, sheet, render, HERE, GF, FONTS, SK_LOGO, pretty_qr, STAFFKIN_RINGS
REPO = os.path.dirname(os.path.dirname(HERE))
ws = openpyxl.load_workbook(os.path.join(REPO, "poster-run/keegix/2-lists/keegix-dropoff-spots-valley.xlsx"), data_only=True)["Drop-off spots"]
spots = [dict(n=r[0], town=r[1], name=r[2], code=r[9].upper()) for r in ws.iter_rows(min_row=5, values_only=True)
         if isinstance(r[0], int) and "card" in (r[7] or "").lower()]
assert len(spots) == 37, len(spots)

def kcard(code, head, sub):
    return card("kg", head, sub, f"https://keegix.com/demo?src={code.lower()}", f"keegix.com · {code}", "Pro free until<br>end of 2027.")

def slug(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:40]
for d in ("k-spots", "k-mail", "s-postcard"): os.makedirs(os.path.join(HERE, d), exist_ok=True)

jobs = []
for i, s in enumerate(spots, 1):
    c = kcard(s["code"], "One guest page per <i>property.</i>", "Opened from a QR sign by the door: check-in, parking, house rules and local picks.")
    jobs.append((f"k-spots/{i:02d}-{s['code']}-{slug(s['name'])}", sheet(c * 4)))
codes = [f"M{n:02d}" for n in range(1, 31)] + ["M01", "M02"]  # 2 spares
for p in range(8):
    cs = "".join(kcard(c, "Scan for a sample guest <i>page.</i>", "This is what your guests would see. One page per property, from a QR sign by the door.") for c in codes[p*4:p*4+4])
    jobs.append((f"k-mail/mail-cards-{p+1}-of-8-{codes[p*4]}-to-{codes[p*4+3]}", sheet(cs)))

REFS = "https://staffkin.com/app/?utm_source=ref-postcard#/signup?intent=refs"
qr = pretty_qr(REFS, dot="#2E2A6B", ring="#2E2A6B", eye="#7B8CF5", logo=STAFFKIN_RINGS, px=150)
steps = "".join(f'<div style="display:flex;gap:10px;align-items:baseline"><b style="flex:none;width:20px;height:20px;border-radius:50%;background:#DDE1FF;color:#2E2A6B;font-size:12px;display:grid;place-items:center">{i}</b><span>{t}</span></div>'
                for i, t in enumerate(["The candidate agrees to the check.", "Each referee gets the same short questions by email.", "You get one PDF report back."], 1))
pc = f'''<div style="width:576px;height:384px;box-sizing:border-box;padding:30px 34px;background:#fff;color:#2E2A6B;font-family:Outfit,sans-serif;display:flex;gap:26px;align-items:center">
<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:12px">
<div style="height:26px;width:108px">{SK_LOGO.replace("<svg ", "<svg style='width:108px;height:26px' ", 1)}</div>
<div style="font-weight:600;font-size:30px;line-height:1.05;letter-spacing:-.01em">Checking references on a new hire?</div>
<div style="display:flex;flex-direction:column;gap:7px;font-size:13.5px;line-height:1.3">{steps}</div>
<div style="font-size:20px;font-weight:600;margin-top:4px">$9 CAD a check <span style="font-size:13px;font-weight:400">· No subscription.</span></div></div>
<div style="flex:none;text-align:center"><div style="background:#fff;padding:6px;border:2px solid #2E2A6B;border-radius:8px">{qr}</div>
<div style="font-size:12.5px;margin-top:8px;letter-spacing:.04em">staffkin.com</div></div></div>'''
ph = f'''<html><head><meta charset="utf-8"><style>{FONTS}*{{margin:0}}body{{width:576px;height:768px}}</style></head><body>{pc}{pc}
<div style="position:absolute;top:383px;left:0;right:0;border-top:1.5px dashed #9aa7b0"></div></body></html>'''
jobs += [("s-postcard/staffkin-postcard-1-of-2", ph), ("s-postcard/staffkin-postcard-2-of-2", ph)]
render(jobs, HERE)
print(len(jobs), "prints")
