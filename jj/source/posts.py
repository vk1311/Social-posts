import os, shutil
from playwright.sync_api import sync_playwright

W = '/tmp/claude-0/-home-claude/c55a830d-2bf7-5686-8eae-0c9939c60360/scratchpad/work'
V = W + '/v2'
PH = W + '/photos/'
OUT = W + '/out2/JJ-Pumps-Social-Posts/Images'
os.makedirs(OUT, exist_ok=True)

DEEP = '#0C2631'; ROYAL = '#1E4485'; SKY = '#B7D2FF'; SOFTB = '#86A8DB'; INK = '#0C2631'; SUB = '#3E5570'
WHITE = '#FFFFFF'; PALE = '#F2F6FD'; LINE = '#D5E2F6'
S = (1080, 1350)

CSS = """*{box-sizing:border-box} body{margin:0;font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased}
.a{position:absolute} h1,h2,p{margin:0}"""


def page(inner, bg='linear-gradient(180deg,#FFFFFF 0%,#F3F7FC 100%)', size=S):
    w, h = size
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
            f"<div style='position:relative;width:{w}px;height:{h}px;overflow:hidden;background:{bg}'>{inner}</div></body></html>")


def fade(name, pos='center', op=.34, start=30, end=85, extra=''):
    """Faded photo that melts into the white page toward the top."""
    m = f"linear-gradient(to top, #000 {start}%, rgba(0,0,0,0) {end}%)"
    return (f"<img class='a' src='file://{PH}{name}.jpg' style='left:0;top:0;width:100%;height:100%;object-fit:cover;object-position:{pos};"
            f"opacity:{op};filter:saturate(.8);-webkit-mask-image:{m};mask-image:{m};{extra}'>")


def pump(k, left=None, right=None, bottom=150, h=900, center=False):
    pos = 'left:50%;transform:translateX(-50%);' if center else (f'left:{left}px;' if left is not None else f'right:{right}px;')
    return (f"<img class='a' src='file://{V}/p-{k}.png' style='{pos}bottom:{bottom}px;height:{h}px;"
            f"filter:drop-shadow(0 18px 22px rgba(12,38,49,.28)) drop-shadow(0 2px 4px rgba(12,38,49,.25))'>")


def floor(cx, bottom, w):
    return (f"<div class='a' style='left:{cx - w // 2}px;bottom:{bottom - 18}px;width:{w}px;height:40px;border-radius:50%;"
            f"background:radial-gradient(ellipse at center, rgba(12,38,49,.35) 0%, rgba(12,38,49,0) 70%)'></div>")


def chip(t, dark=False):
    c, b = (SKY, 'rgba(183,210,255,.5)') if dark else (ROYAL, ROYAL)
    return f"<div style='align-self:flex-start;padding:9px 22px;border-radius:999px;border:2px solid {b};color:{c};font-size:22px;font-weight:600;letter-spacing:3px'>{t}</div>"


def logo(size=98):
    return f"<img src='file://{W}/jj-mark.png' style='height:{size}px;width:auto;flex-shrink:0'>"


def foot(h=130):
    return (f"<div class='a' style='left:0;right:0;bottom:0;height:{h}px;padding:0 56px;background:{DEEP};color:{WHITE};display:flex;align-items:center;justify-content:space-between'>"
            f"<div style='display:flex;align-items:center;gap:20px'>{logo()}<div style='display:flex;flex-direction:column'>"
            f"<span style='font-size:28px;font-weight:700;line-height:1.2;color:{SKY}'>Jay Jalaram Pumps &amp; Spares</span><span style='font-size:20px;color:#C6D6F2'>JJ Pumps · Bakrol, Ahmedabad</span></div></div>"
            f"<div style='display:flex;flex-direction:column;align-items:flex-end'><span style='font-size:30px;font-weight:700;color:{WHITE}'>+91 92271 06108</span>"
            f"<span style='font-size:20px;color:#C6D6F2'>@jayjalarampumps</span></div></div>")


def dark_foot_text(text):
    return (f"<div class='a' style='left:0;right:0;bottom:0;height:110px;padding:0 56px;background:rgba(8,10,12,.78);color:{WHITE};display:flex;align-items:center;justify-content:space-between'>"
            f"<div style='display:flex;align-items:center;gap:18px'>{logo(78)}<span style='font-size:26px;font-weight:500'>{text}</span></div>"
            f"<span style='font-size:24px;color:{SKY};font-weight:700'>+91 92271 06108</span></div>")


def counter(n, t, dark=False):
    c = 'rgba(183,210,255,.6)' if dark else LINE
    tc = SKY if dark else ROYAL
    return f"<div class='a' style='right:72px;top:72px;padding:8px 22px;border-radius:999px;border:2px solid {c};color:{tc};font-size:24px;font-weight:500'>{n} / {t}</div>"


def swipe(css, t='Swipe →'):
    return f"<div class='a' style='{css};padding:16px 34px;border-radius:999px;background:{ROYAL};color:{WHITE};font-size:32px;font-weight:600'>{t}</div>"


def col(css, inner, gap=26):
    return f"<div class='a' style='{css};display:flex;flex-direction:column;gap:{gap}px'>{inner}</div>"


def h(t, size, color=INK, extra=''):
    return f"<h1 style='font-size:{size}px;line-height:1.06;font-weight:700;letter-spacing:-.5px;color:{color};{extra}'>{t}</h1>"


def ptxt(t, size, color=SUB, weight=400, extra=''):
    return f"<p style='font-size:{size}px;line-height:1.42;font-weight:{weight};color:{color};{extra}'>{t}</p>"


def rule(c=ROYAL):
    return f"<div style='width:88px;height:4px;border-radius:2px;background:{c}'></div>"


def card(inner, pad='40px 44px'):
    return f"<div style='padding:{pad};border-radius:24px;background:{WHITE};border:1.5px solid {LINE};box-shadow:0 10px 30px rgba(12,38,49,.06);display:flex;flex-direction:column;gap:12px'>{inner}</div>"


def info_bg(name, pos='center'):
    return fade(name, pos, op=.22, start=0, end=45)


def cta(bg_name, title, sub, n=None, t=None, extra_line='', site=True, pump_k=None):
    i = f"<img class='a' src='file://{PH}{bg_name}.jpg' style='left:0;top:0;width:100%;height:100%;object-fit:cover;opacity:.16;filter:grayscale(.3)'>"
    if n:
        i += counter(n, t, True)
    wa = (f"<svg width='96' height='96' viewBox='0 0 24 24' fill='none' stroke='{SKY}' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'>"
          "<path d='M20.5 11.5a8.5 8.5 0 0 1-12.6 7.4L3.5 20.5l1.6-4.3A8.5 8.5 0 1 1 20.5 11.5z'/><path d='M9 8.5c0 3.3 3.2 6.5 6.5 6.5l1-1.6-2.2-1-1 1c-1.2-.5-2.2-1.5-2.7-2.7l1-1-1-2.2z'/></svg>")
    w = 600 if pump_k else 936
    body = wa + h(title, 84, WHITE) + ptxt(sub, 38, '#C6D6F2') + \
        f"<div style='align-self:flex-start;padding:20px 40px;border-radius:999px;background:{SKY};color:{DEEP};font-size:50px;font-weight:700'>+91 92271 06108</div>" + \
        (ptxt(extra_line, 28, '#C6D6F2') if extra_line else '')
    i += col(f'left:72px;top:190px;width:{w}px', body, 34)
    if pump_k:
        i += pump(pump_k, right=110, bottom=190, h=960)
    i += (f"<div class='a' style='left:72px;bottom:60px;display:flex;align-items:center;gap:20px;color:{WHITE}'>{logo(96)}"
          f"<div style='display:flex;flex-direction:column'><span style='font-size:28px;font-weight:700;color:{SKY}'>Jay Jalaram Pumps &amp; Spares</span>"
          f"<span style='font-size:22px;color:#C6D6F2'>{'www.jayjalarampumps.in' if site else 'Bakrol, Ahmedabad · Mon–Sat 9 AM – 7 PM'}</span></div></div>")
    return page(i, f'linear-gradient(165deg,{ROYAL} 0%,{DEEP} 70%)')


TORAN = ("<svg class='a' style='left:0;top:0' width='1080' height='120' viewBox='0 0 1080 120'><path d='M-20 20 Q270 130 560 20 Q850 130 1100 20' fill='none' stroke='#8A5215' stroke-width='3'/>"
         "<g fill='#E08A2E'>" + ''.join(f"<circle cx='{x}' cy='{y}' r='15'/>" for x, y in [(70, 44), (170, 70), (270, 79), (370, 70), (470, 44), (650, 44), (750, 70), (850, 79), (950, 70), (1040, 44)]) +
         "</g><g fill='#F2C14E'>" + ''.join(f"<circle cx='{x}' cy='{y}' r='10'/>" for x, y in [(120, 60), (220, 76), (320, 76), (420, 60), (700, 60), (800, 76), (900, 76), (995, 60)]) + "</g></svg>")


def diya_scene(flip=False):
    t = 'transform:scaleX(-1);' if flip else ''
    return (f"<img class='a' src='file://{PH}diya.jpg' style='left:-60px;top:500px;width:1200px;height:800px;object-fit:cover;{t}'>"
            f"<div class='a' style='left:0;top:490px;width:100%;height:260px;background:linear-gradient(180deg,#110907 0%,rgba(17,9,7,0) 100%)'></div>")


posts = []


def add(fn, html):
    posts.append((fn, html))


# 01 Meet JJ
i = fade('sprinkler', '30% center', .36)
i += col('left:72px;top:96px;width:500px', chip('V6 SUBMERSIBLE PUMPS') + h(f'Water for <span style="color:{ROYAL}">every field.</span>', 86) + rule() + ptxt('Pump sets, motors and spares, made in our Ahmedabad workshop.', 32), 26)
i += floor(820, 150, 480) + pump('tall', left=600, bottom=150, h=1000) + pump('short', left=792, bottom=150, h=410) + pump('sealed', left=922, bottom=150, h=575)
i += foot()
add('01_Tue-29-Sep_single.jpg', page(i))

# 02 Which pump
i = fade('ricechannel', 'center', .3)
i += col('left:72px;top:96px;width:936px', chip('PUMP GUIDE') + h(f'Which pump fits <span style="color:{ROYAL}">your borewell?</span>', 96), 26)
i += floor(540, 150, 620) + pump('old-mixflow', left=250, bottom=150, h=760) + pump('old-ktype', left=420, bottom=150, h=760) + pump('blue', left=640, bottom=150, h=760)
i += swipe('right:72px;bottom:190px') + foot()
add('02_Thu-01-Oct_carousel_1of5.jpg', page(i))
for n, (fam, head, sub, k, r) in enumerate([('MIXFLOW', 'More water.', 'For borewells where the water is not very deep.', 'old-mixflow', 170),
                                           ('K-TYPE', 'Deeper water.', 'Lifts water from deeper borewells with steady pressure.', 'old-ktype', 150)], start=2):
    i = info_bg('ricechannel') + counter(n, 5)
    i += col('left:72px;top:230px;width:560px', f"<div style='font-size:26px;font-weight:600;letter-spacing:4px;color:{ROYAL}'>{fam}</div>" + h(head, 86) + rule() + ptxt(sub, 38), 28)
    i += floor(1080 - r - 110, 150, 320) + pump(k, right=r, bottom=150, h=1060) + foot()
    add(f'02_Thu-01-Oct_carousel_{n}of5.jpg', page(i))
rows = ''.join(card(f"<div style='display:flex;align-items:center;gap:30px'><div style='width:84px;height:84px;flex-shrink:0;border-radius:50%;background:{PALE};border:2px solid {LINE};color:{ROYAL};display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:700'>{n}</div>"
                    f"<div style='display:flex;flex-direction:column'><span style='font-size:42px;font-weight:700;color:{INK}'>{a}</span><span style='font-size:28px;color:{SUB}'>{b}</span></div></div>", '28px 34px')
               for n, a, b in [(1, 'Borewell size', 'in inches'), (2, 'Water depth', 'in feet'), (3, 'Fields to water', 'in bigha or acre')])
i = info_bg('ricechannel') + counter(4, 5) + col('left:72px;top:190px;width:936px', h('Tell us 3 things.', 86) + f"<div style='display:flex;flex-direction:column;gap:22px'>{rows}</div>", 40) + foot()
add('02_Thu-01-Oct_carousel_4of5.jpg', page(i))
add('02_Thu-01-Oct_carousel_5of5.jpg', cta('ricechannel', 'Send them on WhatsApp.', 'We will suggest the right model for your borewell.', 5, 5))

# 04 Copper rotor
i = fade('canal', 'center 70%', .28)
i += col('left:72px;top:110px;width:560px', chip('INSIDE EVERY MOTOR') + h(f'Copper rotor <span style="color:{ROYAL}">inside.</span>', 96) + rule() + ptxt('Copper carries electricity better than aluminium, so the motor runs cooler.', 32), 26)
i += (f"<div class='a' style='left:72px;top:960px;width:600px;display:flex;align-items:center;gap:18px'>"
      f"<span style='font-size:30px;font-weight:600;color:{ROYAL}'>Look for this label</span><div style='flex-grow:1;height:2px;background:{ROYAL}'></div></div>")
i += floor(830, 150, 300) + pump('sealed', left=720, bottom=150, h=1040)
i += f"<div class='a' style='left:672px;top:900px;width:300px;height:140px;border-radius:50%;border:4px solid {ROYAL}'></div>"
i += foot()
add('04_Tue-06-Oct_single.jpg', page(i))

# 05 5 signs
i = fade('hose', 'center', .3)
i += col('left:72px;top:90px;width:560px', f"<div style='font-size:240px;line-height:.9;font-weight:700;color:{ROYAL}'>5</div>" + h('signs your pump needs a check-up', 84), 14)
i += floor(870, 150, 300) + pump('old-trio', right=60, bottom=150, h=760)
i += swipe('left:72px;bottom:190px') + foot()
add('05_Thu-08-Oct_carousel_1of5.jpg', page(i))
signs = [[('1', 'Less water than before', 'Same pump, same borewell, but a weaker flow.'), ('2', 'Fuse or starter trips often', 'The motor may be pulling too much current.')],
         [('3', 'Motor hums but no water', 'Switch it off at once to protect the motor.'), ('4', 'Sand or mud in the water', 'Sand wears out the pump parts quickly.')]]
for n, pair in enumerate(signs, start=2):
    cards = ''.join(card(f"<div style='font-size:96px;line-height:1;font-weight:700;color:{ROYAL}'>{a}</div><div style='font-size:54px;line-height:1.12;font-weight:700;color:{INK}'>{b}</div>" + ptxt(c, 30)) for a, b, c in pair)
    i = info_bg('hose') + counter(n, 5) + col('left:72px;top:180px;width:936px', cards, 32) + foot()
    add(f'05_Thu-08-Oct_carousel_{n}of5.jpg', page(i))
i = info_bg('hose') + counter(4, 5) + col('left:72px;top:260px;width:936px', card(
    f"<div style='font-size:160px;line-height:1;font-weight:700;color:{ROYAL}'>5</div><div style='font-size:72px;line-height:1.1;font-weight:700;color:{INK}'>Electricity bill suddenly higher</div>" + ptxt('A tired motor uses more power for the same water.', 34), '60px 56px')) + foot()
add('05_Thu-08-Oct_carousel_4of5.jpg', page(i))
add('05_Thu-08-Oct_carousel_5of5.jpg', cta('hose', 'Spares and repair at our workshop.', 'Seen any of these signs? WhatsApp us.', 5, 5, site=False, pump_k='tall'))

# 06 Navratri
i = diya_scene(flip=True)
i += col('left:90px;top:110px;width:900px;align-items:center;text-align:center', f"<div style='font-size:28px;font-weight:500;letter-spacing:8px;color:{SKY}'>JAY MATAJI</div>"
         + h('Happy Navratri', 120, WHITE) + rule(SKY) + ptxt('Nine nights of devotion. May Maa Durga bless every home and every field.', 36, '#E8DFD3'), 26)
i += dark_foot_text('Warm wishes from the JJ Pumps family')
add('06_Sun-11-Oct_festival-Navratri.jpg', page(i, '#110907'))

# 08 World Food Day
i = fade('seedling', 'center 55%', .4, 25, 80)
i += col('left:90px;top:110px;width:900px;align-items:center;text-align:center', chip('16 OCTOBER · WORLD FOOD DAY') + h(f'Every meal begins <span style="color:{ROYAL}">with water.</span>', 92) + rule(), 26)
i += f"<div class='a' style='left:50%;transform:translateX(-50%);top:1050px;padding:22px 52px;border-radius:999px;background:{DEEP};color:{WHITE};font-size:44px;font-weight:600;white-space:nowrap'>Thank you, farmers.</div>"
i += foot()
add('08_Fri-16-Oct_single.jpg', page(i).replace("align-self:flex-start;padding:9px", "align-self:center;padding:9px"))

# 09 Rabi
i = fade('wheat', 'center 60%', .38, 20, 75)
i += col('left:72px;top:96px;width:936px', chip('WHEAT · CHANA · MUSTARD') + h(f'Rabi season is here.<br><span style="color:{ROYAL}">Is your pump ready?</span>', 88), 26)
i += floor(760, 150, 560) + pump('tall', left=560, bottom=150, h=760) + pump('short', left=700, bottom=150, h=312) + pump('sealed', left=790, bottom=150, h=437)
i += swipe('left:72px;bottom:190px', 'Swipe for the checklist →') + foot()
add('09_Sat-17-Oct_carousel_1of5.jpg', page(i))
tick = f"<svg width='120' height='120' viewBox='0 0 24 24' fill='none' stroke='{ROYAL}' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'><rect x='3' y='3' width='18' height='18' rx='4'/><path d='M7.5 12.5l3 3 6-7'/></svg>"
for n, (a, b) in enumerate([('Check cable joints and insulation.', 'A cracked joint lets water in and can burn the motor.'),
                            ('Check starter and voltage before running.', 'Low voltage is one of the biggest reasons motors fail.'),
                            ('Test water flow before sowing starts.', 'Find a weak flow now, not in the middle of the season.')], start=2):
    i = info_bg('wheat') + counter(n, 5) + col('left:72px;top:230px;width:936px', tick + f"<div style='font-size:26px;font-weight:600;letter-spacing:4px;color:{ROYAL}'>CHECK {n-1}</div>" + h(a, 86) + ptxt(b, 36), 30) + foot()
    add(f'09_Sat-17-Oct_carousel_{n}of5.jpg', page(i))
add('09_Sat-17-Oct_carousel_5of5.jpg', cta('wheat', 'Keep our number handy.', 'Spares are ready at our workshop for the season.', 5, 5, 'Save this post · Share with a farmer friend'))

# 10 Dussehra
i = fade('wheat', 'center 30%', .45, 10, 80) + TORAN
i += col('left:90px;top:220px;width:900px;align-items:center;text-align:center', f"<div style='font-size:28px;font-weight:600;letter-spacing:8px;color:{ROYAL}'>VIJAYADASHAMI</div>"
         + h('Happy Dussehra', 124) + ptxt('Victory of good over evil.', 44, ROYAL, 600), 26)
i += f"<div class='a' style='left:50%;transform:translateX(-50%);top:960px;width:780px;padding:24px 40px;border-radius:24px;background:{WHITE};border:1.5px solid {LINE};color:{INK};font-size:34px;line-height:1.35;font-weight:500;text-align:center'>Strength and success to your family and your farm.</div>"
i += foot()
add('10_Tue-20-Oct_festival-Dussehra.jpg', page(i))

# 12 Label
i = fade('terraces', 'center 70%', .3)
i += col('left:72px;top:110px;width:560px', chip('KNOW YOUR PUMP') + h(f"Read your pump's label <span style='color:{ROYAL}'>in 1 minute.</span>", 88) + rule() + ptxt('HP · Head · Discharge · Stages', 32), 26)
i += floor(830, 150, 300) + pump('old-ssjacket', right=110, bottom=150, h=1040) + swipe('left:72px;bottom:190px') + foot()
add('12_Sat-24-Oct_carousel_1of5.jpg', page(i))
ico = {'HP': "<path d='M13 2L4 14h7l-1 8 9-12h-7z'/>", 'Head': "<path d='M12 21V3'/><path d='M6 9l6-6 6 6'/><path d='M4 21h16'/>",
       'Discharge': "<path d='M12 2.5C8 8 5.5 11.5 5.5 15a6.5 6.5 0 0 0 13 0c0-3.5-2.5-7-6.5-12.5z'/>",
       'Stages': "<rect x='6' y='3' width='12' height='4' rx='1'/><rect x='6' y='10' width='12' height='4' rx='1'/><rect x='6' y='17' width='12' height='4' rx='1'/>"}
for n, (term, size, a, b) in enumerate([('HP', 200, 'How much power the motor has.', 'More HP does more work, and uses more electricity.'),
                                       ('Head', 200, 'How high it can lift water.', 'Written in metres or feet. Deeper water needs more head.'),
                                       ('Discharge', 150, 'How much water it gives.', 'Written in litres per minute (LPM).'),
                                       ('Stages', 150, 'The lifting units inside.', 'More stages lift water higher. Save this post!')], start=2):
    svg = f"<svg width='112' height='112' viewBox='0 0 24 24' fill='none' stroke='{ROYAL}' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'>{ico[term]}</svg>"
    wdt = 600 if term == 'Stages' else 936
    i = info_bg('terraces') + counter(n, 5) + col(f'left:72px;top:210px;width:{wdt}px', svg + f"<div style='font-size:{size}px;line-height:.95;font-weight:700;color:{INK};letter-spacing:-2px'>{term}</div>" + h(a, 62, ROYAL) + ptxt(b, 34), 30)
    if term == 'Stages':
        i += floor(890, 150, 260) + pump('old-mixflow', right=150, bottom=150, h=1040)
    i += foot()
    add(f'12_Sat-24-Oct_carousel_{n}of5.jpg', page(i))

# 13 Motors
i = fade('sprinkler', '65% center', .3)
i += col('left:72px;top:96px;width:560px', chip('V6 SUBMERSIBLE MOTORS') + h(f'Two motors. <span style="color:{ROYAL}">One job: water.</span>', 78), 26)
mc = ''.join(card(f"<svg width='64' height='64' viewBox='0 0 24 24' fill='none' stroke='{ROYAL}' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'>{p}</svg>"
                  f"<span style='font-size:42px;line-height:1.1;font-weight:700;color:{INK}'>{a}</span><span style='font-size:28px;color:{SUB}'>{b}</span>", '32px 34px')
             for p, a, b in [("<rect x='7' y='2' width='10' height='20' rx='2'/><path d='M7 7h10'/><path d='M7 17h10'/>", 'Full SS motor', 'Stainless steel body'),
                             ("<circle cx='12' cy='12' r='9'/><circle cx='12' cy='12' r='3.5'/>", 'Carbon Bearing motor', 'Carbon bearing inside')])
i += col('left:72px;top:500px;width:540px', mc, 24)
i += f"<div class='a' style='left:72px;top:1075px;width:540px;font-size:28px;color:{SUB}'>Ask us which one suits your borewell water.</div>"
i += floor(830, 150, 300) + pump('sealed', left=720, bottom=150, h=1040) + foot()
add('13_Tue-27-Oct_single.jpg', page(i))

# 15 Range
i = fade('terraces', 'center 60%', .3)
i += col('left:72px;top:96px;width:936px', chip('ONE WORKSHOP · FULL RANGE') + h(f'The JJ <span style="color:{ROYAL}">pump set range</span>', 100), 24)
lx = 110
for k, hh in [('old-mixflow', 700), ('old-ktype', 700), ('tall', 700), ('blue', 700), ('old-ssjacket', 700)]:
    i += pump(k, left=lx, bottom=150, h=hh)
    lx += 175
i = i.replace("<img class='a' src='file://" + V, floor(540, 150, 900) + "<img class='a' src='file://" + V, 1)
i += swipe('left:72px;top:390px') + foot()
add('15_Sat-31-Oct_carousel_1of5.jpg', page(i))
fams = [('FAMILY 1', 'Mixflow', ['262 Mixflow', '262 Heavy Mixflow', 'NENO Mixflow', 'NENO Heavy Mixflow'], 'old-mixflow', 150),
        ('FAMILY 2', 'K-Type', ['K-Type', 'Heavy Series K-Type', 'K-Type AR'], 'old-ktype', 130),
        ('FAMILY 3', '273 &amp; 50 Feet', ['273 Light', '273 Heavy', 'SS 50 Feet', '50 Feet DRS', '50 Feet CI / SS Jacket'], 'old-ssjacket', 110)]
for n, (lab, name, models, k, r) in enumerate(fams, start=2):
    items = ''.join(f"<div style='padding:20px 28px;border-radius:18px;background:{WHITE};border:1.5px solid {LINE};font-size:34px;font-weight:600;color:{INK}'>{m}</div>" for m in models)
    i = info_bg('terraces') + counter(n, 5) + col('left:72px;top:170px;width:590px', f"<div style='font-size:26px;font-weight:600;letter-spacing:4px;color:{ROYAL}'>{lab}</div>" + h(name, 90) + items, 16)
    i += floor(1080 - r - 120, 150, 300) + pump(k, right=r, bottom=150, h=1040) + foot()
    add(f'15_Sat-31-Oct_carousel_{n}of5.jpg', page(i))
grid = ''.join(f"<div style='padding:22px 26px;border-radius:18px;background:rgba(255,255,255,.08);border:1.5px solid rgba(183,210,255,.35);font-size:34px;font-weight:600;color:{WHITE}'>{m}</div>"
               for m in ['Openwell pumps', 'Neno Type AR', '262 Type AR', 'Motors', 'Pump only', 'Spares &amp; job work'])
i = f"<img class='a' src='file://{PH}terraces.jpg' style='left:0;top:0;width:100%;height:100%;object-fit:cover;opacity:.14;filter:grayscale(.3)'>" + counter(5, 5, True)
i += col('left:72px;top:160px;width:936px', h('Also from JJ', 92, WHITE) + f"<div style='display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px'>{grid}</div>", 30)
i += f"<img class='a' src='file://{V}/p-openwell.png' style='left:50%;transform:translateX(-50%);top:680px;width:620px;filter:drop-shadow(0 18px 24px rgba(0,0,0,.45))'>"
i += col('left:72px;top:1080px;width:936px', ptxt('Send your borewell details. We will match the model.', 32, '#C6D6F2') +
         f"<div style='align-self:flex-start;padding:16px 36px;border-radius:999px;background:{SKY};color:{DEEP};font-size:42px;font-weight:700'>+91 92271 06108</div>", 18)
add('15_Sat-31-Oct_carousel_5of5.jpg', page(i, f'linear-gradient(165deg,{ROYAL} 0%,{DEEP} 70%)'))

# 17 Dhanteras
i = diya_scene()
i += col('left:72px;top:110px;width:600px', f"<div style='font-size:28px;font-weight:500;letter-spacing:8px;color:{SKY}'>SHUBH DHANTERAS</div>"
         + h('Happy Dhanteras', 100, WHITE) + rule(SKY) + ptxt('Bring home new strength for your farm.', 38, '#E8DFD3', 500), 26)
i += pump('sealed', right=120, bottom=150, h=620)
i += dark_foot_text('JJ Pumps · Bakrol, Ahmedabad')
add('17_Fri-06-Nov_festival-Dhanteras.jpg', page(i, '#110907'))

# 18 Diwali
i = diya_scene()
i += col('left:90px;top:100px;width:900px;align-items:center;text-align:center', f"<div style='font-size:28px;font-weight:500;letter-spacing:8px;color:{SKY}'>SHUBH DEEPAVALI</div>"
         + h('Happy Diwali', 136, WHITE) + rule(SKY) + ptxt('Light in every home.<br>Water in every field.', 42, '#E8DFD3', 500), 26)
i += dark_foot_text('From the JJ Pumps family to yours')
add('18_Sun-08-Nov_festival-Diwali.jpg', page(i, '#110907'))

# 19 New Year
i = fade('terraces', 'center 70%', .45, 10, 80) + TORAN
i += col('left:90px;top:210px;width:900px;align-items:center;text-align:center',
         f"<div style='font-size:28px;font-weight:600;letter-spacing:6px;color:{ROYAL}'>SAAL MUBARAK</div>" + h('Nutan Varsh Abhinandan', 100) + ptxt('Happy New Year and Happy Bhai Dooj', 38, ROYAL, 500), 22)
i += f"<div class='a' style='left:50%;transform:translateX(-50%);top:1010px;width:760px;padding:22px 40px;border-radius:999px;background:{DEEP};color:{WHITE};font-size:32px;line-height:1.35;font-weight:500;text-align:center'>Good crops and good health this year.</div>"
i += foot()
add('19_Tue-10-Nov_festival-New-Year-Bhai-Dooj.jpg', page(i))

# 20 How to order
i = fade('seedling', 'center 60%', .34, 20, 75)
i += col('left:72px;top:96px;width:500px', chip('4 SIMPLE STEPS') + h(f'How to order <span style="color:{ROYAL}">from JJ Pumps</span>', 96), 24)
i += floor(840, 150, 440) + pump('blue', left=660, bottom=150, h=900) + pump('tall', left=790, bottom=150, h=900)
i += swipe('left:72px;bottom:190px') + foot()
add('20_Thu-12-Nov_carousel_1of4.jpg', page(i))
for n, pair in enumerate([[('STEP 1', 'WhatsApp your borewell details', 'Borewell size, water depth and field size.'), ('STEP 2', 'We suggest the right model', 'Matched to your borewell, not guessed.')],
                          [('STEP 3', 'Confirm and we dispatch', 'Or pick it up from our Bakrol workshop.'), ('STEP 4', 'Call us anytime for service', 'Spares and repair from the people who made it.')]], start=2):
    cards = ''.join(card(f"<div style='font-size:26px;font-weight:600;letter-spacing:4px;color:{ROYAL}'>{a}</div><div style='font-size:54px;line-height:1.12;font-weight:700;color:{INK}'>{b}</div>" + ptxt(c, 30)) for a, b, c in pair)
    i = info_bg('seedling') + counter(n, 4) + col('left:72px;top:190px;width:936px', cards, 32) + foot()
    add(f'20_Thu-12-Nov_carousel_{n}of4.jpg', page(i))
blk = lambda lab, val, size=32, w=400: f"<div style='display:flex;flex-direction:column;gap:6px'><span style='font-size:22px;font-weight:600;letter-spacing:4px;color:{SKY}'>{lab}</span><span style='font-size:{size}px;line-height:1.4;font-weight:{w};color:{WHITE}'>{val}</span></div>"
i = counter(4, 4, True)
i += col('left:72px;top:150px;width:936px', f"<div style='display:flex;align-items:center;gap:24px'>{logo(150)}<div style='display:flex;flex-direction:column'><span style='font-size:44px;font-weight:700;color:{SKY};line-height:1.15'>Jay Jalaram Pumps &amp; Spares</span><span style='font-size:26px;color:#C6D6F2'>JJ Pumps · Swajal</span></div></div>"
         + blk('CALL / WHATSAPP', '+91 92271 06108', 56, 700) + ptxt('Alternative: +91 92272 06108', 28, '#C6D6F2')
         + blk('WORKSHOP', '33 / N.K. Industrial Estate, Road No. 3, Bakrol–Gatrad Road, Bakrol, Ahmedabad – 382430')
         + blk('HOURS', 'Mon–Sat, 9 AM – 7 PM · Sunday closed') + blk('ONLINE', 'www.jayjalarampumps.in · @jayjalarampumps'), 30)
add('20_Thu-12-Nov_carousel_4of4.jpg', page(i, f'linear-gradient(165deg,{ROYAL} 0%,{DEEP} 70%)'))

os.makedirs(W + '/html2', exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1080, 'height': 1350})
    for fn, html in posts:
        hp = W + '/html2/' + fn.replace('.jpg', '.html')
        open(hp, 'w').write(html)
        pg.goto('file://' + hp)
        pg.wait_for_timeout(120)
        pg.screenshot(path=OUT + '/' + fn, type='jpeg', quality=92)
    b.close()
print(len(posts), 'posts')
