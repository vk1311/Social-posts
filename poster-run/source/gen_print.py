import qrcode, json, os, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.join(ROOT, "project")
os.makedirs(PROJ, exist_ok=True)

INK = "#12252F"; INK8 = "#1B333F"; SLATE = "#2F4A56"; MIST = "#7E96A2"
PAPER = "#FBF9F4"; CLOUD = "#F2ECE0"; MAG = "#C2185B"; MAGD = "#9E1149"; MUTED = "#5A6B75"
COORD = "45.0774° N &#160; 64.4956° W"

def qr_svg(url, px, label):
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m); d = []
    for y, r in enumerate(m):
        x = 0
        while x < n:
            if r[x]:
                s = x
                while x < n and r[x]: x += 1
                d.append(f"M{s} {y}h{x-s}v1h-{x-s}z")
            else:
                x += 1
    return (f'<svg viewBox="-2 -2 {n+4} {n+4}" width="{px}" height="{px}" role="img" '
            f'aria-label="{label}" shape-rendering="crispEdges" style="display: block; flex: none">'
            f'<rect x="-2" y="-2" width="{n+4}" height="{n+4}" fill="#FFFFFF"></rect>'
            f'<path fill="{INK}" d="{"".join(d)}"></path></svg>')

def qr_pretty(url, px, label, logo=True):
    """Rounded-dot QR with magenta eyes and the Waypoint mark in the middle.
    High error correction (H) so the centre logo doesn't stop it scanning."""
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_H)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    def in_eye(x, y):
        return (x < 7 and y < 7) or (x >= n - 7 and y < 7) or (x < 7 and y >= n - 7)
    lg = int(n * 0.22) | 1          # odd number of modules, ~22% of the width
    l0 = (n - lg) // 2
    def in_logo(x, y):
        return logo and l0 - 1 <= x <= l0 + lg and l0 - 1 <= y <= l0 + lg
    dots = []
    for y in range(n):
        for x in range(n):
            if m[y][x] and not in_eye(x, y) and not in_logo(x, y):
                dots.append(f'<rect x="{x+0.04:.2f}" y="{y+0.04:.2f}" width="0.92" height="0.92" rx="0.28"></rect>')
    eyes = []
    for ex, ey in ((0, 0), (n - 7, 0), (0, n - 7)):
        eyes.append(f'<rect x="{ex+0.5}" y="{ey+0.5}" width="6" height="6" rx="0.9" fill="none" stroke="{INK}" stroke-width="1"></rect>')
        eyes.append(f'<rect x="{ex+2}" y="{ey+2}" width="3" height="3" rx="0.5" fill="{MAG}"></rect>')
    centre = ""
    if logo:
        c = n / 2
        centre = (f'<rect x="{l0-0.6:.2f}" y="{l0-0.6:.2f}" width="{lg+1.2:.2f}" height="{lg+1.2:.2f}" rx="1.4" fill="#FFFFFF"></rect>'
                  f'<svg x="{l0:.2f}" y="{l0:.2f}" width="{lg}" height="{lg}" viewBox="0 0 128 128">'
                  + mark(128).split(">", 1)[1].rsplit("</svg>", 1)[0] + '</svg>')
    return (f'<svg viewBox="-2 -2 {n+4} {n+4}" width="{px}" height="{px}" role="img" '
            f'aria-label="{label}" style="display: block; flex: none">'
            f'<rect x="-2" y="-2" width="{n+4}" height="{n+4}" fill="#FFFFFF"></rect>'
            f'<g fill="{INK}">{"".join(dots)}</g>{"".join(eyes)}{centre}</svg>')

def mark(px, dark=False):
    tri = PAPER if dark else INK
    survey = MIST if dark else SLATE
    return f'''<svg viewBox="0 0 128 128" width="{px}" height="{px}" role="img" aria-label="Waypoint logo" style="display: block; flex: none">
<line x1="55.10" y1="107.56" x2="43.43" y2="24.59" stroke="{survey}" stroke-width="2"></line>
<line x1="30.73" y1="34.51" x2="108.42" y2="65.90" stroke="{survey}" stroke-width="2"></line>
<line x1="106.17" y1="49.93" x2="40.15" y2="101.52" stroke="{survey}" stroke-width="2"></line>
<line x1="64.00" y1="9.44" x2="64.00" y2="114.84" stroke="{survey}" stroke-width="2"></line>
<polygon points="70.20,62.14 70.20,65.86 118.56,64.00" fill="{survey}"></polygon>
<polygon points="57.80,62.14 57.80,65.86 9.44,64.00" fill="{survey}"></polygon>
<line x1="46.40" y1="74.15" x2="59.70" y2="51.10" stroke="{MAG}" stroke-width="3" stroke-linecap="round"></line>
<line x1="81.60" y1="74.15" x2="68.30" y2="51.10" stroke="{MAG}" stroke-width="3" stroke-linecap="round"></line>
<polygon points="64.00,37.96 86.55,77.02 41.45,77.02" fill="none" stroke="{tri}" stroke-width="5" stroke-linejoin="round"></polygon>
<circle cx="64.00" cy="37.96" r="4.6" fill="{MAG}"></circle>
<circle cx="86.55" cy="77.02" r="4.6" fill="{MAG}"></circle>
<circle cx="41.45" cy="77.02" r="4.6" fill="{MAG}"></circle>
<circle cx="64.00" cy="64.00" r="6" fill="{MAG}"></circle>
</svg>'''

def lining(w, h, dark=False, step=48, x0=0, y0=0):
    """Chart grid + two bearing lines, like the Waypoint posts."""
    g = "rgba(126,150,162,0.16)" if dark else "#E7E2D7"
    b = "rgba(126,150,162,0.34)" if dark else "#D6D0C3"
    lines = []
    x = step
    while x < w:
        lines.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{h}" stroke="{g}" stroke-width="1"></line>'); x += step
    y = step
    while y < h:
        lines.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="{g}" stroke-width="1"></line>'); y += step
    lines.append(f'<line x1="-40" y1="{int(h*0.30)}" x2="{w+40}" y2="{int(h*0.62)}" stroke="{b}" stroke-width="1.5"></line>')
    lines.append(f'<line x1="{int(w*0.18)}" y1="-40" x2="{int(w*0.74)}" y2="{h+40}" stroke="{b}" stroke-width="1.5"></line>')
    return (f'<svg aria-hidden="true" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'style="position: absolute; left: {x0}px; top: {y0}px; display: block">{"".join(lines)}</svg>')

def page(title, w, h, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800&amp;family=DM+Sans:wght@400;500;700&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:{MAG}}}a:hover{{color:{INK}}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''

def coords(color, size=13, top=52, left=56):
    return (f'<div style="position: absolute; left: {left}px; top: {top}px; font-size: {size}px; '
            f'letter-spacing: 0.16em; color: {color}">{COORD}</div>')

def footer(dark, url, bottom=44, side=56, mk=60, fs=19, name=True):
    col = PAPER if dark else INK
    nm = (f'<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: {int(fs*1.15)}px; color: {col}">Waypoint</div>' if name else '')
    return (f'<div style="position: absolute; left: {side}px; right: {side}px; bottom: {bottom}px; display: flex; '
            f'align-items: center; justify-content: space-between">'
            f'<div style="display: flex; align-items: center; gap: 12px">{mark(mk, dark)}{nm}</div>'
            f'<div style="font-size: {fs}px; letter-spacing: 0.12em; color: {col}">{url}</div></div>')

def bar(w=120, h=8, color=MAG, mt=22):
    return f'<div style="width: {w}px; height: {h}px; background: {color}; margin-top: {mt}px"></div>'

def bullet(text, fs=19, dark=False, sq=12, sqc=MAG):
    col = PAPER if dark else INK
    return (f'<div style="display: flex; gap: 12px; align-items: flex-start">'
            f'<div style="flex: none; width: {sq}px; height: {sq}px; background: {sqc}; margin-top: {int(fs*0.42)}px"></div>'
            f'<div style="font-size: {fs}px; line-height: 1.35; color: {col}">{text}</div></div>')

W, H = 816, 1056
files = {}

# ---------- Waypoint A: "fit" (light) ----------
q = qr_svg("https://waypointns.ca/?src=flyer-fit", 168, "QR code to waypointns.ca")
body = f'''<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {PAPER}; color: {INK}; font-family: 'DM Sans', sans-serif">
{lining(W, H)}
{coords(MUTED)}
<div style="position: absolute; left: 56px; right: 56px; top: 136px; display: flex; flex-direction: column">
<div style="font-size: 15px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: {MAGD}">Custom software · Atlantic Canada</div>
<h1 style="margin: 18px 0 0 0; font-family: Manrope, sans-serif; font-weight: 800; font-size: 72px; line-height: 1.0; letter-spacing: -0.03em; max-width: 680px; text-wrap: balance">I make the software fit your business.</h1>
{bar()}
<p style="margin: 26px 0 0 0; font-size: 21px; line-height: 1.45; color: {SLATE}; max-width: 660px">Most software hands you a ready-made system and new words to learn. I build the tool around the way your shop already runs.</p>
<div style="margin-top: 30px; display: grid; grid-template-columns: 1fr 1fr; gap: 14px 28px; max-width: 690px">
{bullet("Quotes signed on a phone")}
{bullet("Invoices and receipts as PDFs")}
{bullet("Booking and request forms")}
{bullet("Job and customer records")}
</div>
</div>
<div style="position: absolute; left: 56px; right: 56px; top: 640px; background: {INK}; color: {PAPER}; padding: 28px 32px; display: flex; align-items: center; gap: 32px">
<div style="flex: 1; display: flex; flex-direction: column; gap: 10px">
<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: 34px; line-height: 1.05">From $1,200 CAD to build</div>
<div style="font-size: 18px; line-height: 1.4; color: {CLOUD}">then $60 CAD a month.<br>Half up front. No contract.</div>
<div style="height: 3px; background: {MAG}; width: 72px; margin: 6px 0"></div>
<div style="font-size: 18px; line-height: 1.45">Call or text Vatsal · <b>902-670-9297</b><br>vatsal@waypointns.ca</div>
</div>
<div style="flex: none; display: flex; flex-direction: column; align-items: center; gap: 10px">
<div style="background: #FFFFFF; padding: 12px; box-shadow: 7px 7px 0 {MAG}">{q}</div>
<div style="font-size: 14px; font-weight: 700; letter-spacing: 0.06em">Scan to see how it works</div>
</div>
</div>
{footer(False, "waypointns.ca")}
</div>'''
files["Main.dc.html"] = page("Waypoint flyer: fit", W, H, body)

# ---------- Waypoint B: "by hand" (dark) ----------
q = qr_svg("https://waypointns.ca/?src=flyer-byhand", 160, "QR code to waypointns.ca")
items = ["Quotes written on the dash of the truck", "Invoices typed up in Word at night",
         "Bookings lost in a text thread", "Job notes on a clipboard"]
checks = "".join(
    f'<div style="display: flex; gap: 16px; align-items: center; padding: 11px 0; border-bottom: 1px solid rgba(126,150,162,0.35)">'
    f'<div style="flex: none; width: 22px; height: 22px; border: 2px solid {MIST}; box-sizing: border-box"></div>'
    f'<div style="font-size: 22px; line-height: 1.3; color: {PAPER}">{t}</div></div>' for t in items)
body = f'''<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {INK}; color: {PAPER}; font-family: 'DM Sans', sans-serif">
{lining(W, H, dark=True)}
{coords(MIST)}
<div style="position: absolute; left: 56px; right: 56px; top: 132px; display: flex; flex-direction: column">
<div style="font-size: 15px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: {MIST}">Custom software · Kentville, NS</div>
<h1 style="margin: 18px 0 0 0; font-family: Manrope, sans-serif; font-weight: 800; font-size: 80px; line-height: 0.98; letter-spacing: -0.03em">Still doing it<br>by hand?</h1>
{bar(140, 8)}
<div style="margin-top: 26px; border-top: 1px solid rgba(126,150,162,0.35); max-width: 600px">{checks}</div>
<p style="margin: 28px 0 0 0; font-family: Manrope, sans-serif; font-weight: 700; font-size: 27px; line-height: 1.25; max-width: 640px">I build one tool that does all of it, around how you already work.</p>
</div>
<div style="position: absolute; left: 62px; right: 70px; top: 726px; background: {CLOUD}; color: {INK}; padding: 22px 26px; box-shadow: 9px 9px 0 {MAG}; transform: rotate(-1.2deg); display: flex; gap: 26px; align-items: center">
{q}
<div style="display: flex; flex-direction: column; gap: 8px">
<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: 26px; line-height: 1.1">From $1,200 CAD to build, then $60 CAD a month.</div>
<div style="font-size: 17px; line-height: 1.4; color: {SLATE}">Half up front. No contract. You deal with me start to finish.</div>
<div style="font-size: 18px; line-height: 1.4">Call or text Vatsal · <b>902-670-9297</b></div>
</div>
</div>
{footer(True, "waypointns.ca", mk=56)}
</div>'''
files["Waypoint-by-hand.dc.html"] = page("Waypoint flyer: by hand", W, H, body)

# ---------- Waypoint C: counter cards, quarter-letter, 4 per sheet, two-sided ----------
# Each card is 4.25 x 5.5 in (408 x 528 px). Print the front and back pages on both sides,
# flip on the long edge: the card in column c, row r on the front backs onto column 1-c, row r.
CW, CH = 408, 528
CPAD = 36  # 0.375 in clear on every card edge: the office printer can't print to the sheet edge
SLOTS = [(0, 0), (1, 0), (0, 1), (1, 1)]

def wcard_front(left, top):
    q = qr_svg("https://waypointns.ca/?src=card", 132, "QR code to waypointns.ca")
    return f"""<div style="position: absolute; left: {left}px; top: {top}px; width: {CW}px; height: {CH}px; overflow: hidden; background: #FFFFFF">
{lining(CW, CH, step=34)}
{coords(MUTED, 11, CPAD, CPAD)}
<div style="position: absolute; left: {CPAD}px; right: {CPAD}px; top: 72px; display: flex; flex-direction: column">
<h2 style="margin: 0; font-family: Manrope, sans-serif; font-weight: 800; font-size: 38px; line-height: 1.02; letter-spacing: -0.02em; color: {INK}; text-wrap: balance">I make the software fit your business.</h2>
{bar(72, 6, mt=16)}
</div>
<div style="position: absolute; left: {CPAD}px; right: {CPAD}px; top: 268px; display: flex; gap: 18px; align-items: center">
<div style="flex: none; background: #FFFFFF; padding: 8px; border: 2px solid {INK}; box-shadow: 5px 5px 0 {MAG}">{q}</div>
<div style="font-size: 15px; line-height: 1.45; color: {INK}">Call or text Vatsal<br><b style="font-size: 17px">902-670-9297</b></div>
</div>
{footer(False, "waypointns.ca", bottom=CPAD, side=CPAD, mk=38, fs=13)}
</div>"""

def wcard_back(left, top):
    # Dark text on white only, so it also prints fine in black and white.
    pts = "".join(bullet(t, 17, sq=10, sqc=INK) for t in
                  ["Quotes signed on a phone", "Invoices as PDFs", "Booking forms", "Job records"])
    return f"""<div style="position: absolute; left: {left}px; top: {top}px; width: {CW}px; height: {CH}px; overflow: hidden; background: #FFFFFF">
<div style="position: absolute; left: {CPAD}px; right: {CPAD}px; top: 76px; display: flex; flex-direction: column">
<p style="margin: 0; font-size: 17px; line-height: 1.4; color: {INK}; text-wrap: balance">Built around the way your shop already runs.</p>
<div style="margin-top: 22px; display: flex; flex-direction: column; gap: 12px">{pts}</div>
<div style="height: 2px; background: {INK}; margin-top: 26px"></div>
<div style="margin-top: 22px; font-family: Manrope, sans-serif; font-weight: 800; font-size: 22px; line-height: 1.2; color: {INK}">From $1,200 CAD,<br>then $60 CAD a month.</div>
<div style="margin-top: 8px; font-size: 16px; line-height: 1.4; color: {INK}">Half up front. No contract.</div>
</div>
<div style="position: absolute; right: {CPAD}px; bottom: {CPAD}px; font-size: 14px; letter-spacing: 0.12em; color: {INK}">waypointns.ca</div>
</div>"""

fronts = "".join(wcard_front(c * CW, r * CH) for c, r in SLOTS)
body = f"""<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; background: #FFFFFF; color: {INK}; font-family: 'DM Sans', sans-serif">
{fronts}
<div style="position: absolute; left: 0; right: 0; top: {CH - 1}px; border-top: 2px dashed {MIST}"></div>
<div style="position: absolute; top: 0; bottom: 0; left: {CW - 1}px; border-left: 2px dashed {MIST}"></div>
</div>"""
files["Waypoint-counter-cards-front.dc.html"] = page("Waypoint counter cards, front (4 per sheet)", W, H, body)

backs = "".join(wcard_back((1 - c) * CW, r * CH) for c, r in SLOTS)
body = f"""<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; background: #FFFFFF; color: {INK}; font-family: 'DM Sans', sans-serif">
{backs}
</div>"""
files["Waypoint-counter-cards-back.dc.html"] = page("Waypoint counter cards, back (4 per sheet)", W, H, body)

# ---------- Apps A: whole business (light, tear-offs) ----------
q = qr_pretty("https://app.waypointns.ca/?src=poster-whole", 210, "QR code to app.waypointns.ca")
NTABS = 9
# Tabs run to the paper edge (no extra cut), but the words stop 0.5 in above it,
# clear of the printer's unprintable margin (25 Oct fix: "app" was cut off).
tabs = "".join(
    f'<div style="height: 212px; box-sizing: border-box; padding: 14px 0 48px 0; {"border-right: 2px dashed " + MIST + ";" if i < NTABS - 1 else ""} display: flex; align-items: center; justify-content: center">'
    f'<div style="writing-mode: vertical-rl; transform: rotate(180deg); font-size: 12.5px; line-height: 1.3; text-align: center; color: {INK}">'
    f'<b>app.waypointns.ca</b><br>Start free<br><b>Vatsal 902-670-9297</b></div></div>'
    for i in range(NTABS))
body = f'''<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {PAPER}; color: {INK}; font-family: 'DM Sans', sans-serif">
{lining(W, H)}
{coords(MUTED)}
<div style="position: absolute; left: 56px; right: 56px; top: 118px; display: flex; flex-direction: column">
<div style="font-size: 15px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: {MAGD}">Waypoint Apps · Made in Kentville</div>
<h1 style="margin: 16px 0 0 0; font-family: Manrope, sans-serif; font-weight: 800; font-size: 82px; line-height: 0.98; letter-spacing: -0.03em; max-width: 700px">Digitize your <span style="color: {MAG}">whole</span> business.</h1>
{bar()}
<p style="margin: 24px 0 0 0; font-size: 21px; line-height: 1.42; color: {SLATE}; max-width: 650px">Invoices, quotes, stock, customers, staff, scheduling and safety. 140+ simple apps on your phone and computer, one login.</p>
</div>
<div style="position: absolute; left: 56px; right: 56px; top: 462px; display: flex; gap: 40px; align-items: center">
<div style="flex: none; display: flex; flex-direction: column; align-items: center; gap: 12px">
<div style="background: #FFFFFF; border: 3px solid {INK}; box-shadow: 9px 9px 0 {MAG}; padding: 14px">{q}</div>
<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: 20px">Scan to start free</div>
</div>
<div style="flex: 1; display: flex; flex-direction: column; gap: 16px">
{bullet("<b>Start free.</b> No card needed.")}
{bullet("<b>Pro apps $20 CAD a month each.</b> Only pay for the ones you use.")}
{bullet("<b>Your data stays in Canada.</b>")}
{bullet("<b>Want it set up for you?</b> Call or text Vatsal at 902-670-9297.")}
</div>
</div>
{footer(False, "app.waypointns.ca", bottom=236, mk=48, fs=18)}
<div style="position: absolute; left: 40px; right: 40px; bottom: 0; display: grid; grid-template-columns: repeat({NTABS}, minmax(0, 1fr)); border-top: 2px dashed {MIST}; background: {PAPER}">{tabs}</div>
</div>'''
files["Apps-whole-business.dc.html"] = page("Waypoint Apps poster: whole business", W, H, body)

# ---------- Apps B: market sellers (dark) ----------
q = qr_svg("https://app.waypointns.ca/?src=poster-market", 150, "QR code to app.waypointns.ca")
tiles = [("Invoices &amp; receipts", "PDFs you can text or email right from your phone."),
         ("Stock that keeps count", "Goes down when you send or get paid on an invoice."),
         ("Price list with photos", "One PDF to share with customers. Free."),
         ("Customers &amp; orders", "Who ordered what, and when, in one place.")]
tile_html = "".join(
    f'<div style="background: {INK8}; border: 2px solid rgba(126,150,162,0.45); padding: 18px 20px; display: flex; flex-direction: column; gap: 8px">'
    f'<div style="width: 26px; height: 4px; background: {MAG}"></div>'
    f'<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: 23px; line-height: 1.15; color: {PAPER}">{a}</div>'
    f'<div style="font-size: 16px; line-height: 1.4; color: {CLOUD}">{b}</div></div>' for a, b in tiles)
body = f'''<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; box-sizing: border-box; background: {INK}; color: {PAPER}; font-family: 'DM Sans', sans-serif">
{lining(W, H, dark=True)}
{coords(MIST)}
<div style="position: absolute; left: 56px; right: 56px; top: 124px; display: flex; flex-direction: column">
<div style="font-size: 15px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: {MIST}">Waypoint Apps · For makers and sellers</div>
<h1 style="margin: 16px 0 0 0; font-family: Manrope, sans-serif; font-weight: 800; font-size: 80px; line-height: 0.98; letter-spacing: -0.03em; max-width: 680px">Selling at markets or online?</h1>
{bar(130, 8)}
<p style="margin: 24px 0 0 0; font-size: 21px; line-height: 1.42; color: {CLOUD}; max-width: 640px">Run the paperwork side from your phone. Free to start.</p>
<div style="margin-top: 28px; display: grid; grid-template-columns: 1fr 1fr; gap: 16px">{tile_html}</div>
</div>
<div style="position: absolute; left: 62px; right: 70px; top: 726px; background: {CLOUD}; color: {INK}; padding: 20px 24px; box-shadow: 9px 9px 0 {MAG}; transform: rotate(-1.2deg); display: flex; gap: 24px; align-items: center">
{q}
<div style="display: flex; flex-direction: column; gap: 8px">
<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: 26px; line-height: 1.1">Scan to start free. No card needed.</div>
<div style="font-size: 17px; line-height: 1.4; color: {SLATE}">Pro apps are $20 CAD a month each. Made in Kentville, and your data stays in Canada.</div>
</div>
</div>
{footer(True, "app.waypointns.ca", mk=56)}
</div>'''
files["Apps-market-sellers.dc.html"] = page("Waypoint Apps poster: market sellers", W, H, body)

# ---------- Apps C: take-one cards 4-up (quarter letter portrait) ----------
def acard(left, top):
    q = qr_svg("https://app.waypointns.ca/?src=card", 118, "QR code to app.waypointns.ca")
    cw, ch = 408, 528
    return f'''<div style="position: absolute; left: {left}px; top: {top}px; width: {cw}px; height: {ch}px; overflow: hidden">
{lining(cw, ch, step=34)}
{coords(MUTED, 10, 40, 40)}
<div style="position: absolute; left: 40px; right: 40px; top: 74px; display: flex; flex-direction: column">
<h2 style="margin: 0; font-family: Manrope, sans-serif; font-weight: 800; font-size: 38px; line-height: 1.0; letter-spacing: -0.02em; color: {INK}">Digitize your <span style="color: {MAG}">whole</span> business.</h2>
{bar(70, 6, mt=14)}
<p style="margin: 14px 0 0 0; font-size: 15px; line-height: 1.42; color: {SLATE}">Invoices, quotes, stock, customers and staff. 140+ simple apps, one login.</p>
</div>
<div style="position: absolute; left: 40px; right: 40px; top: 290px; display: flex; gap: 16px; align-items: center">
<div style="background: #FFFFFF; padding: 8px; border: 2px solid {INK}; box-shadow: 5px 5px 0 {MAG}">{q}</div>
<div style="display: flex; flex-direction: column; gap: 6px">
<div style="font-family: Manrope, sans-serif; font-weight: 800; font-size: 18px; line-height: 1.15; color: {INK}">Start free.</div>
<div style="font-size: 13px; line-height: 1.4; color: {INK}">Pro $20 CAD a month<br>per app.</div>
<div style="font-size: 13px; line-height: 1.4; color: {SLATE}">Made in Kentville.<br>Data stays in Canada.</div>
</div>
</div>
{footer(False, "app.waypointns.ca", bottom=36, side=40, mk=38, fs=13, name=False)}
</div>'''
body = f'''<div style="width: {W}px; height: {H}px; position: relative; overflow: hidden; background: {PAPER}; color: {INK}; font-family: 'DM Sans', sans-serif">
{acard(0, 0)}{acard(408, 0)}{acard(0, 528)}{acard(408, 528)}
<div style="position: absolute; left: 0; right: 0; top: 527px; border-top: 2px dashed {MIST}"></div>
<div style="position: absolute; top: 0; bottom: 0; left: 407px; border-left: 2px dashed {MIST}"></div>
</div>'''
files["Apps-take-one-cards.dc.html"] = page("Waypoint Apps take-one cards (4 per sheet)", W, H, body)

for name, src in files.items():
    open(os.path.join(PROJ, name), "w").write(src)

# canvas index
now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
row1 = ["Main.dc.html", "Waypoint-by-hand.dc.html", "Waypoint-counter-cards-front.dc.html", "Waypoint-counter-cards-back.dc.html"]
row2 = ["Apps-whole-business.dc.html", "Apps-market-sellers.dc.html", "Apps-take-one-cards.dc.html"]
titles = {"Main.dc.html": "Waypoint A · Fit (Letter)", "Waypoint-by-hand.dc.html": "Waypoint B · By hand (Letter)",
          "Waypoint-counter-cards-front.dc.html": "Waypoint C · Counter cards, front (4 per sheet)",
          "Waypoint-counter-cards-back.dc.html": "Waypoint C · Counter cards, back (flip on long edge)",
          "Apps-whole-business.dc.html": "Apps A · Whole business, tear-offs (Letter)",
          "Apps-market-sellers.dc.html": "Apps B · Market sellers (Letter)",
          "Apps-take-one-cards.dc.html": "Apps C · Take-one cards, 4 per sheet"}
boards = {}
for i, f in enumerate(row1): boards[f] = {"x": i * 896, "y": 300, "w": W, "h": H, "title": titles[f]}
for i, f in enumerate(row2): boards[f] = {"x": i * 896, "y": 1700, "w": W, "h": H, "title": titles[f]}
canvas = {"v": 3, "createdOnFiles": {"v": 1, "at": now}, "title": "Waypoint print run: flyers and cards",
          "launch": {"view": "canvas"}, "pages": [], "boards": boards, "order": row1 + row2,
          "notes": {"t1": {"x": 0, "y": 20, "text": "Waypoint: business owners", "kind": "title1", "maxW": 3504},
                    "t2": {"x": 0, "y": 1420, "text": "Waypoint Apps: makers, sellers, side hustles", "kind": "title1", "maxW": 2608}},
          "designSystems": []}
json.dump(canvas, open(os.path.join(PROJ, "canvas.json"), "w"))
print("wrote", list(files))
