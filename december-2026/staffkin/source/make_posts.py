import base64, json, pathlib, html

REPO = pathlib.Path('REPO_ROOT')
FONTS = REPO / 'staffkin/hub/07-editable-sources/fonts'
OUT = pathlib.Path('./html')
OUT.mkdir(parents=True, exist_ok=True)

def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
font_css = ''.join(
    f"@font-face{{font-family:Outfit;font-weight:{w};src:url(data:font/woff2;base64,{b64(FONTS/f'outfit-latin-{w}-normal.woff2')}) format('woff2');}}"
    for w in (400, 500, 600, 700))
LOGO_DARK = 'data:image/svg+xml;base64,' + b64(REPO/'staffkin/brand/staffkin-logo.svg')
LOGO_WHITE = 'data:image/svg+xml;base64,' + b64(REPO/'staffkin/brand/staffkin-logo-white.svg')

BASE = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px}
body{font-family:Outfit;position:relative;overflow:hidden}
.light{background:#F5F6FC;color:#23213F}
.dark{background:#2E2A6B;color:#fff}
.rings{position:absolute;right:-60px;bottom:-200px;width:700px;height:480px}
.rings i{position:absolute;width:520px;height:520px;border-radius:50%;border:80px solid}
.rings i:nth-child(1){left:0;top:0}
.rings i:nth-child(2){left:265px;top:0}
.light .rings i:nth-child(1){border-color:#E6E6F0}
.light .rings i:nth-child(2){border-color:#EAEEFB}
.dark .rings i:nth-child(1){border-color:rgba(255,255,255,.12)}
.dark .rings i:nth-child(2){border-color:rgba(123,140,245,.18)}
.wrap{position:absolute;left:90px;right:90px;top:0;bottom:0}
.kicker{font-weight:600;font-size:26px;letter-spacing:4px;text-transform:uppercase;color:#7B8CF5}
.dark .kicker{color:#AEB8FF}
h1{font-weight:700;font-size:82px;line-height:1.04;letter-spacing:-1.5px;color:#2E2A6B}
.dark h1{color:#fff}
h1 .acc{color:#7B8CF5}
.dark h1 .acc{color:#AEB8FF}
h2{font-weight:700;font-size:70px;line-height:1.06;letter-spacing:-1px;color:#2E2A6B}
h2 .acc{color:#7B8CF5}
.sub{font-size:38px;line-height:1.3;color:#5F5C85}
.dark .sub{color:#D8DCFF}
.card{background:#fff;border:2px solid #E1E3F2;border-radius:28px;padding:30px 36px;margin-bottom:22px}
.card.mist{background:#EEF0FD}
.card .lab{font-weight:600;font-size:24px;letter-spacing:3px;text-transform:uppercase;color:#7B8CF5;margin-bottom:8px}
.card .lab.stop{color:#A8261B}.card .lab.good{color:#1D6F4C}
.card .txt{font-weight:600;font-size:40px;line-height:1.2;color:#2E2A6B}
.card .txt.q{font-weight:500;font-style:normal}
.list{list-style:none}
.list li{font-size:40px;line-height:1.25;padding:10px 0 10px 56px;position:relative;color:#23213F}
.list li:before{content:'';position:absolute;left:6px;top:24px;width:22px;height:12px;border-left:5px solid #1D6F4C;border-bottom:5px solid #1D6F4C;transform:rotate(-45deg)}
.big{font-weight:700;font-size:150px;line-height:1;color:#7B8CF5}
.foot{position:absolute;left:90px;right:90px;bottom:62px;display:flex;justify-content:space-between;align-items:center}
.foot img{height:48px}
.foot span{font-weight:500;font-size:30px;color:#5F5C85}
.dark .foot span{color:#AEB8FF}
.note{position:absolute;left:90px;bottom:132px;font-size:24px;color:#5F5C85}
.dark .note{color:#C9CEFF}
.swipe{position:absolute;left:90px;bottom:180px;font-weight:500;font-size:32px;color:#AEB8FF}
"""

def page(theme, inner, right='staffkin.com', note=None, swipe=False):
    logo = LOGO_WHITE if theme == 'dark' else LOGO_DARK
    extra = ''
    if note: extra += f'<div class="note">{note}</div>'
    if swipe: extra += '<div class="swipe">Swipe &rarr;</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{font_css}{BASE}</style></head>
<body class="{theme}"><div class="rings"><i></i><i></i></div>
<div class="wrap">{inner}</div>{extra}
<div class="foot"><img src="{logo}"><span>{right}</span></div></body></html>"""

def at(top, h): return f'<div style="position:absolute;left:0;right:0;top:{top}px">{h}</div>'
def cards(items, cls=''):
    return ''.join(f'<div class="card {cls}"><div class="lab {l[2] if len(l)>2 else ""}">{l[0]}</div><div class="txt">{l[1]}</div></div>' for l in items)
def ul(items): return '<ul class="list">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'

posts = []  # (file_stem, theme, html)
def add(stem, theme, inner, **kw): posts.append((stem, page(theme, inner, **kw)))

# Schedule: Mon/Wed/Fri from Mon Nov 30
# 18 Mon-30-Nov  #1 First three hires (single)
add('18_Mon-30-Nov_single', 'light',
    at(190, '<div class="kicker">Unpopular opinion</div>') +
    at(250, '<h1>Your first three hires don\'t need an ATS. <span class="acc">They need six good questions.</span></h1>') +
    at(700, ul(['The same six questions', 'In the same order', 'For every candidate'])) +
    at(980, '<div class="sub">Hollis drafts them. You run the interviews.</div>'))

# 19 Wed-02-Dec  #4 Vague job ads (carousel 4)
add('19_Wed-02-Dec_carousel_1of4', 'dark',
    at(130, '<h1>A vague job ad gets you <span class="acc">more applicants and worse hires.</span></h1>'), right='1 / 4', swipe=True)
add('19_Wed-02-Dec_carousel_2of4', 'light',
    at(250, '<h2>The vague ad</h2>') +
    at(400, '<div class="card"><div class="lab">Example</div><div class="txt" style="font-weight:500">&ldquo;Team player wanted. Fast-paced environment. Competitive pay.&rdquo;</div></div>' +
        '<div class="card mist"><div class="lab stop">The problem</div><div class="txt">Fits everyone. Tells nobody anything.</div></div>'), right='2 / 4')
add('19_Wed-02-Dec_carousel_3of4', 'light',
    at(200, '<h2>The clear ad</h2>') +
    at(340, cards([('Hours', 'Tuesday to Saturday, 10 to 6'), ('Pay', '$18.50 an hour CAD'), ('Day one', 'Open the shop, run the till'), ('First month', 'Learn ordering and closing')])) +
    at(1110, '<div style="font-size:24px;color:#5F5C85">Example job. Made-up details.</div>'), right='3 / 4')
add('19_Wed-02-Dec_carousel_4of4', 'dark',
    at(300, '<h1>Some people will pass. <span class="acc">That\'s the point.</span></h1>') +
    at(720, '<div class="sub">Hollis, your AI HR deskmate, drafts the first version of your ad. You make the calls.</div>'), right='staffkin.com')

# 20 Fri-04-Dec  #9 Night cleaner (single, story)
add('20_Fri-04-Dec_single', 'dark',
    at(190, '<div class="kicker">A short story</div>') +
    at(260, '<h1>She waters the office fern every night. <span class="acc">Nobody asked her to.</span></h1>') +
    at(760, '<div class="sub">Some of the best work happens where no one is looking. Noticing people is part of hiring well.</div>'))

# 21 Mon-07-Dec  #7 Two truths and a lie: paperwork (carousel 5)
def ttal(stem, topic, claims, lie_no, why):
    add(f'{stem}_1of5', 'dark', at(130, f'<h1>Two truths and a lie: <span class="acc">{topic}</span></h1>') +
        at(560, '<div class="sub">Two are true. One is not. Guess before you swipe.</div>'), right='1 / 5', swipe=True)
    for i, c in enumerate(claims, 1):
        add(f'{stem}_{i+1}of5', 'light', at(220, f'<div class="big">{i}</div>') +
            at(420, f'<h2 style="font-weight:600;font-size:60px">{c}</h2>') +
            at(980, '<div class="kicker">Truth or lie?</div>'), right=f'{i+1} / 5')
    add(f'{stem}_5of5', 'light',
        at(200, f'<h2>The lie is <span class="acc">number {lie_no}.</span></h2>') +
        at(380, f'<div class="card mist"><div class="lab stop">Why</div><div class="txt" style="font-weight:500;font-size:38px">{why}</div></div>') +
        at(760, '<div class="sub">Hollis can draft the paperwork. You still make the calls.</div>'),
        right='5 / 5', note='Not legal advice.')

ttal('21_Mon-07-Dec_carousel', 'hiring paperwork',
     ['New hires fill out a federal and a provincial TD1.',
      'When pay stops, you issue a Record of Employment, and the deadline is short.',
      'During probation, you can end employment for any reason, with no rules at all.'],
     3, "Probation doesn't switch off employment standards or human rights law. Details vary by province.")

# 22 Wed-09-Dec  #3 Reference checks save time (single)
add('22_Wed-09-Dec_single', 'light',
    at(190, '<div class="kicker">Unpopular opinion</div>') +
    at(250, '<h1>Skipping reference checks <span class="acc">costs more time than it saves.</span></h1>') +
    at(690, cards([('A reference call', 'One short conversation', 'good'), ('A bad hire', 'Weeks of fixing, re-training and re-posting the job', 'stop')])) +
    at(1080, '<div class="sub" style="font-size:32px">Hollis drafts the questions. You make the call.</div>'))

# 23 Fri-11-Dec  #12 Day-one checklist (carousel 5)
add('23_Fri-11-Dec_carousel_1of5', 'dark',
    at(130, '<h1>Before day one, <span class="acc">have these four things ready.</span></h1>'), right='1 / 5', swipe=True)
for i, (lab, title, desc) in enumerate([
        ('Paperwork', 'Ready to sign', 'Offer letter, tax forms and direct deposit form.'),
        ('Logins', 'Set up and tested', 'Email and the tools they need, with a temporary password.'),
        ('A buddy', 'One named person', 'A teammate who knows they\'re coming and has time for questions.'),
        ('A schedule', 'Day one on paper', 'Where to be, who to meet, and when lunch is.')], 2):
    add(f'23_Fri-11-Dec_carousel_{i}of5', 'light',
        at(260, f'<div class="kicker">{i-1} &middot; {lab}</div>') +
        at(330, f'<h2>{title}</h2>') +
        at(460, f'<div class="sub">{desc}</div>') +
        (at(900, '<div class="sub" style="font-size:32px">Hollis drafts the welcome letter and checklist. You bring the welcome.</div>') if i == 5 else ''),
        right=f'{i} / 5')

# 24 Mon-14-Dec  #5 AI drafts, people decide (single)
add('24_Mon-14-Dec_single', 'light',
    at(170, '<div class="kicker">Meet Hollis, your AI HR deskmate</div>') +
    at(230, '<h1>AI writes the paperwork. <span class="acc">People make the hire.</span></h1>') +
    at(600, '<div style="display:flex;gap:22px">'
        '<div class="card" style="flex:1"><div class="lab">Hollis drafts</div><div class="txt" style="font-size:34px">Job posts<br>Interview questions<br>Offer letters</div></div>'
        '<div class="card mist" style="flex:1"><div class="lab good">You decide</div><div class="txt" style="font-size:34px">Who moves forward<br>Who you hire</div></div></div>') +
    at(930, '<div class="sub" style="font-size:32px">Hollis never scores or ranks anyone.</div>'))

# 25 Wed-16-Dec  #8 Two truths and a lie: interview questions (carousel 5)
ttal('25_Wed-16-Dec_carousel', 'interview questions',
     ['&ldquo;Are you legally able to work in Canada?&rdquo; is fine to ask.',
      '&ldquo;This role includes weekends. Can you work those shifts?&rdquo; is fine to ask.',
      '&ldquo;Do you plan to have kids soon?&rdquo; is fine if you keep it friendly.'],
     3, "Family status is protected under human rights law, and a friendly tone doesn't change that. Stick to what the job needs.")

# 26 Fri-18-Dec  #10 Lunch in the car (single, story)
add('26_Fri-18-Dec_single', 'dark',
    at(190, '<div class="kicker">A short story</div>') +
    at(260, '<h1>Dale ate lunch in his car for three months. <span class="acc">Nobody told him about the break room.</span></h1>') +
    at(860, '<div class="sub">Onboarding someone properly means showing them where lunch happens.</div>'))

# 27 Mon-21-Dec  #11 Reference-check tip (carousel 5)
add('27_Mon-21-Dec_carousel_1of5', 'dark',
    at(130, '<h1>3 reference-check questions <span class="acc">that get honest answers.</span></h1>') +
    at(560, '<div class="sub">Plus one to never ask.</div>'), right='1 / 5', swipe=True)
for i, q in enumerate(['What was their biggest strength on the job?',
                       'What kind of support helped them do their best work?',
                       'Would you work with them again? Why or why not?'], 2):
    add(f'27_Mon-21-Dec_carousel_{i}of5', 'light',
        at(260, f'<div class="kicker">Question {i-1}</div>') +
        at(330, f'<h2>&ldquo;{q}&rdquo;</h2>') +
        (at(900, '<div class="sub" style="font-size:32px">Then pause. A little silence gets people talking.</div>') if i == 4 else ''),
        right=f'{i} / 5')
add('27_Mon-21-Dec_carousel_5of5', 'light',
    at(220, '<h2>One to <span class="acc">never</span> ask</h2>') +
    at(380, '<div class="card mist"><div class="lab stop">Leave it out</div><div class="txt">Anything about health, age, family plans or other personal matters.</div></div>') +
    at(760, '<div class="sub">Hollis drafts your questions before the call. You decide who to hire.</div>'), right='5 / 5')

# 28 Wed-23-Dec  #2 Culture fit (single)
add('28_Wed-23-Dec_single', 'dark',
    at(190, '<div class="kicker">Unpopular opinion</div>') +
    at(260, '<h1>&ldquo;Culture fit&rdquo; usually means <span class="acc">&ldquo;reminds me of us.&rdquo;</span></h1>') +
    at(720, '<div class="sub">Hire for the job: the skills, the tasks, the first 90 days. Then build the culture.</div>'))

# 29 Mon-28-Dec  #6 The first week (single)
add('29_Mon-28-Dec_single', 'light',
    at(170, '<div class="kicker">Unpopular opinion</div>') +
    at(230, '<h1>The first week matters more than <span class="acc">the interview.</span></h1>') +
    at(560, '<div class="card mist"><div class="lab">Day one, example</div>'
        '<div class="txt" style="font-weight:500;font-size:38px;line-height:1.7">'
        '<b style="color:#7B8CF5;font-weight:600">9:00</b>&nbsp; Welcome and coffee<br>'
        '<b style="color:#7B8CF5;font-weight:600">10:00</b>&nbsp; Tour and logins<br>'
        '<b style="color:#7B8CF5;font-weight:600">12:00</b>&nbsp; Lunch together<br>'
        '<b style="color:#7B8CF5;font-weight:600">2:00</b>&nbsp; First real task</div></div>') +
    at(1000, '<div class="sub" style="font-size:32px">One person to ask. Lunch together.</div>'))

for stem, h in posts:
    (OUT / f'{stem}.html').write_text(h)
json.dump([s for s, _ in posts], open(OUT / 'list.json', 'w'))
print(len(posts), 'pages')
