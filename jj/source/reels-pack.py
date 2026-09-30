import os, shutil, html, subprocess
from playwright.sync_api import sync_playwright

W = '/tmp/claude-0/-home-claude/c55a830d-2bf7-5686-8eae-0c9939c60360/scratchpad/work'
SRC = W + '/out2/JJ-Pumps-Social-Posts'
PK = W + '/out3/JJ-Reels-For-Edits'
if os.path.exists(PK):
    shutil.rmtree(PK)
os.makedirs(PK + '/Videos'); os.makedirs(PK + '/Covers')

TIME = '7:30 PM India time (11:00 AM Halifax)'

R = [
 dict(n='03', date='Sat 3 Oct 2026', title='Built piece by piece', dur=15,
      file='03_Sat-03-Oct_reel_built-piece-by-piece',
      mood='Confident build-up. Clean percussion with a slow rise that lands on a hit when the pump is complete.',
      search=['cinematic build up', 'corporate percussion', 'industrial rhythm', 'epic tabla'],
      beats=[('0.0', 'Title appears'), ('1.0', 'Motor rises into frame'), ('3.5', 'Strainer locks on (blue flash)'),
             ('5.0', 'Stages lock on (blue flash)'), ('6.5', 'Discharge head locks on: BIGGEST HIT here'),
             ('7.2', 'Light shine runs down the steel'), ('10.0', 'Pump slides left'), ('11.0', 'End card with phone number')],
      sfx='A soft metal "clunk" at 3.5, 5.0 and 6.5 sec (search "metal click" or "mechanical lock" in Edits sound effects).',
      vo=[('0–2', 'Every JJ pump starts here.'), ('2–7', 'Copper-rotor motor. Stainless strainer. Pump stages. Discharge head.'),
          ('7–10', 'Built piece by piece, checked at every joint.'), ('11–15', 'Jay Jalaram Pumps, Ahmedabad. Call or WhatsApp us today.')]),
 dict(n='07', date='Tue 13 Oct 2026', title="What's inside your pump?", dur=18,
      file='07_Tue-13-Oct_reel_inside-the-pump',
      mood='Calm, curious, a little techy. Soft electronic pulse or ambient piano with a light beat.',
      search=['technology ambient', 'science documentary', 'minimal electronic', 'curious explainer'],
      beats=[('0.0', 'Title: What’s inside your pump?'), ('2.4', 'Photo wipes into the cut-open view'),
             ('3.5', 'Copper rotor starts spinning'), ('4.4', 'Camera pushes into the motor'), ('6.2', 'Water starts flowing up'),
             ('8.4', 'Camera glides up to the impellers'), ('11.8', 'Stage counter 1-2-3-4-5'), ('15.0', 'End card')],
      sfx='A low electric hum rising from 3.5 sec, and a soft water "whoosh" from 6.2 sec.',
      vo=[('0–3', 'Ever wondered what happens deep inside your borewell?'), ('3–8', 'The copper rotor spins, nearly three thousand turns a minute.'),
          ('8–12', 'The impellers push the water up, stage by stage.'), ('12–15', 'More stages, more height.'),
          ('15–18', 'JJ Pumps. Engineered inside and out.')]),
 dict(n='11', date='Thu 22 Oct 2026', title='Looking for dealers', dur=15,
      file='11_Thu-22-Oct_reel_dealers-wanted',
      mood='Upbeat and business-like. Positive, driving beat that feels like growth and opportunity.',
      search=['upbeat corporate', 'business motivation', 'positive energy', 'indian fusion upbeat'],
      beats=[('0.0', 'Title: Looking for dealers'), ('1.2', 'Pumps slide in one by one (every half second until 3.5)'),
             ('4.6', 'Shine across the lineup'), ('6.0', 'Openwell pump appears'), ('6.4', 'Product tags pop in'),
             ('10.4', 'Big DEALER end card: BIGGEST HIT here')],
      sfx='A soft "swoosh" as each pump slides in (1.2 to 3.5 sec).',
      vo=[('0–3', 'Do you run a hardware, pipe or agri shop?'), ('3–7', 'Add JJ pumps, motors and spares to your counter.'),
          ('7–10', 'Reliable supply straight from our Ahmedabad workshop.'), ('10–15', 'WhatsApp "DEALER" to nine two two seven one, zero six one zero eight.')]),
 dict(n='14', date='Thu 29 Oct 2026', title='3 mistakes that damage your pump', dur=19,
      file='14_Thu-29-Oct_reel_3-mistakes',
      mood='Serious but helpful. Suspenseful pulse for the mistakes, then a warm, relieved lift at the end card.',
      search=['suspense tension', 'documentary serious', 'ticking clock', 'hopeful resolve'],
      beats=[('0.0', 'Title: 3 mistakes'), ('2.0', 'Mistake 1: water level drops'), ('4.7', 'Red warning pulse'),
             ('6.6', 'Mistake 2: voltage needle falls'), ('11.0', 'Mistake 3: wrong-size pump shakes'),
             ('13.2', 'Right-size pump fits'), ('15.4', 'End card: switch music to a brighter feel here')],
      sfx='A short warning beep at 4.7 sec, a "power down" sound at 8.6 sec, and a soft "ding" at 13.2 sec.',
      vo=[('0–2', 'Three mistakes that damage your pump.'), ('2–6', 'One: running it dry. The motor overheats.'),
          ('6–11', 'Two: low voltage with no protection. Fit a proper starter.'), ('11–15', 'Three: the wrong size for your borewell.'),
          ('15–19', 'Not sure what fits? Ask JJ Pumps before you buy.')]),
 dict(n='16', date='Tue 3 Nov 2026', title='Repair and job work', dur=16,
      file='16_Tue-03-Nov_reel_repair-and-job-work',
      mood='Hands-on and reassuring. Steady workshop groove, mid tempo.',
      search=['workshop groove', 'hip hop instrumental chill', 'DIY repair', 'steady corporate'],
      beats=[('0.0', 'Title: Pump not working?'), ('1.4', 'Pump opens up'), ('3.8', 'Worn part slides out'),
             ('5.2', 'New part slides in'), ('8.2', 'Pump closes back up'), ('9.8', 'Tested tick mark'), ('12.2', 'End card')],
      sfx='A "whoosh" at 3.8 and 5.2 sec, and a click when the pump closes at 9.4 sec.',
      vo=[('0–2', 'Pump not working?'), ('2–6', 'We open it up and replace the worn parts.'),
          ('6–10', 'Every repaired pump is tested before it goes back.'), ('10–16', 'Repair, spares and job work at JJ Pumps, Bakrol, Ahmedabad.')]),
]

for r in R:
    shutil.copy(f"{SRC}/Reels/{r['file']}.mp4", f"{PK}/Videos/{r['file']}.mp4")
    cov = r['file'].replace('_reel_', '_reel-cover_') + '.jpg'
    shutil.copy(f"{SRC}/Images/{cov}", f"{PK}/Covers/{cov}")

# Voiceover-Scripts.txt
L = ['JJ PUMPS — REEL VOICE-OVER SCRIPTS (English)',
     'Read at a calm, clear pace. Times are seconds into the video.', '']
for r in R:
    L += ['=' * 46, f"REEL {r['n']} · {r['title']} · {r['dur']} sec", f"Post: {r['date']}, {TIME}", '-' * 46]
    L += [f"[{t} sec]  {line}" for t, line in r['vo']]
    L.append('')
open(PK + '/Voiceover-Scripts.txt', 'w').write('\n'.join(L))

# PDF guide
e = html.escape
AZ = '#0C2631'; RB = '#1E4485'
rows = ''.join(f"<tr><td>{r['n']}</td><td>{e(r['date'])}</td><td>{e(r['title'])}</td><td>{r['dur']} sec</td></tr>" for r in R)
cards = ''
for r in R:
    fr = ''.join(f"<img src='file://{W}/frames/{r['n']}_{i}.jpg'>" for i in range(4))
    beats = ''.join(f"<tr><td class='t'>{b[0]} s</td><td>{e(b[1])}</td></tr>" for b in r['beats'])
    vo = ''.join(f"<tr><td class='t'>{t} s</td><td>{e(line)}</td></tr>" for t, line in r['vo'])
    srch = ' · '.join(f"<span class='tag'>{e(s)}</span>" for s in r['search'])
    cards += f"""<section>
<div class='hd'><span class='n'>{r['n']}</span><div><div class='d'>{e(r['date'])} · {TIME} · {r['dur']} sec</div><div class='ti'>{e(r['title'])}</div></div></div>
<div class='fr'>{fr}</div>
<div class='g'>
<div><h3>Music</h3><p>{e(r['mood'])}</p><p class='s'>Search in Edits: {srch}</p><h3>Sound effects (optional)</h3><p>{e(r['sfx'])}</p></div>
<div><h3>Where the beats land</h3><table class='b'>{beats}</table></div>
</div>
<h3>Voice-over script</h3><table class='b vo'>{vo}</table>
<p class='fn'>Files: Videos/{e(r['file'])}.mp4 · Covers/{e(r['file'].replace('_reel_', '_reel-cover_'))}.jpg</p>
</section>"""

doc = f"""<!doctype html><html><head><meta charset='utf-8'><style>
body {{ font-family: Poppins, sans-serif; color: #1d2a35; font-size: 10pt; }}
h1 {{ color: {AZ}; font-size: 22pt; margin: 0 0 4px }} h3 {{ color: {RB}; font-size: 10.5pt; margin: 10px 0 4px }}
.sub {{ color: #4a5b6a; margin-bottom: 12px }}
ol {{ margin: 0 0 10px; padding-left: 18px }} ol li {{ margin: 3px 0 }}
table {{ width: 100%; border-collapse: collapse }}
.sch th {{ background: {AZ}; color: #fff; text-align: left; padding: 6px 8px }} .sch td {{ padding: 5px 8px; border-bottom: 1px solid #dde3e8 }}
.note {{ background: #EAF2FF; border-left: 4px solid {RB}; padding: 8px 12px; margin: 10px 0 }}
section {{ page-break-inside: avoid; page-break-before: always; }}
.hd {{ display: flex; gap: 12px; align-items: center; margin-bottom: 8px }}
.n {{ background: {AZ}; color: #fff; font-weight: 700; border-radius: 8px; padding: 6px 10px; font-size: 13pt }}
.d {{ color: {RB}; font-weight: 600; font-size: 9pt }} .ti {{ font-weight: 700; font-size: 14pt; color: {AZ} }}
.fr {{ display: flex; gap: 8px; margin: 6px 0 4px }} .fr img {{ height: 150px; border-radius: 6px; border: 1px solid #ccd }}
.g {{ display: grid; grid-template-columns: 1fr 1fr; gap: 18px }}
.b td {{ padding: 3px 6px; border-bottom: 1px solid #eef1f4; vertical-align: top }} .b .t {{ width: 58px; color: {RB}; font-weight: 600; white-space: nowrap }}
.vo td {{ font-size: 10.5pt }} .tag {{ background: #F2F6FD; border: 1px solid #D5E2F6; border-radius: 10px; padding: 1px 7px; font-size: 8.5pt }}
.s {{ margin-top: 4px }} .fn {{ color: #7a8a98; font-size: 8pt; margin-top: 8px }}
</style></head><body>
<h1>JJ Pumps — Reels Audio Guide</h1>
<div class='sub'>5 reels · for editing in Edits · posting on Instagram &amp; Facebook</div>
<table class='sch'><tr><th>#</th><th>Post on</th><th>Reel</th><th>Length</th></tr>{rows}</table>
<p>All reels go out at <b>{TIME}</b>.</p>
<h3>How to add audio in Edits, step by step</h3>
<ol>
<li>Open <b>Edits</b> and tap <b>+</b> to start a new project. Pick the reel's .mp4 from the Videos folder.</li>
<li><b>Music:</b> tap <b>Audio</b>, search one of the suggested terms, pick a track and drag it so its biggest hit lines up with the "biggest hit" time in the beat list.</li>
<li><b>Voice-over:</b> tap <b>Voiceover</b> (the microphone), press record and read the script. Speak each line at the time shown.</li>
<li>If you use both, lower the music to about 20–30% so the voice is clear.</li>
<li>Tap <b>Captions</b> to auto-add subtitles for the voice-over. Many people watch on mute.</li>
<li>Export in 1080p. When posting, choose the matching image from the Covers folder as the cover.</li>
</ol>
<div class='note'><b>Music rights:</b> a business account can only use tracks from the in-app library marked safe for business, so pick music inside Edits or Instagram rather than a downloaded Bollywood song. Posts with unlicensed music can be muted or blocked.</div>
{cards}
</body></html>"""
open(W + '/reels-guide.html', 'w').write(doc)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto('file://' + W + '/reels-guide.html'); pg.wait_for_timeout(500)
    pg.pdf(path=PK + '/Reels-Audio-Guide.pdf', format='A4', print_background=True, margin={'top': '14mm', 'bottom': '14mm', 'left': '14mm', 'right': '14mm'})
    b.close()
print('ok')
