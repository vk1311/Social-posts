import os, glob, html
from playwright.sync_api import sync_playwright

W = '/tmp/claude-0/-home-claude/c55a830d-2bf7-5686-8eae-0c9939c60360/scratchpad/work'
PK = W + '/out2/JJ-Pumps-Social-Posts'
IMG = PK + '/Images'
RL = PK + '/Reels'
TH = W + '/out2/thumbs'
os.makedirs(TH, exist_ok=True)
CONTACT = 'Call / WhatsApp: +91 92271 06108\nwww.jayjalarampumps.in'
BASE = '#JJPumps #JayJalaramPumps #SubmersiblePump #BorewellPump #Kisan #IndianFarmer #Agriculture #Irrigation #Gujarat #Ahmedabad'
MUSIC = 'Add a trending instrumental from the Instagram / Facebook music library before posting.'

P = [
 ('01', 'Tue 29 Sep', 'Single photo', 'Meet JJ Pumps',
  'Namaste! We are Jay Jalaram Pumps & Spares (JJ Pumps) from Bakrol, Ahmedabad.\n\nWe make V6 submersible pump sets, motors, pump-only assemblies and spares, and we take job work.\n\nFollow us for pump tips, farm water guides and new models.',
  '#MadeInIndia #FarmLife #WaterForFarms'),
 ('02', 'Thu 1 Oct', 'Carousel (5 slides)', 'Which pump fits your borewell?',
  'The wrong pump wastes power and water.\n\nSend us 3 things on WhatsApp: borewell size, water depth and field size. We will suggest the right JJ pump for you.',
  '#PumpGuide #FarmTips #Borewell'),
 ('03', 'Sat 3 Oct', 'Reel (15 sec)', 'Built piece by piece',
  'Motor. Strainer. Stages. Discharge head.\n\nEvery JJ pump is built piece by piece and checked at every joint in our Ahmedabad workshop.',
  '#BehindTheScenes #MakeInIndia #MadeInGujarat'),
 ('04', 'Tue 6 Oct', 'Single photo', 'Why copper rotor matters',
  'Look for the orange "Copper Rotor" label on our pumps.\n\nCopper carries electricity better than aluminium, so the motor heats up less while it works.',
  '#CopperRotor #PumpMotor'),
 ('05', 'Thu 8 Oct', 'Carousel (5 slides)', '5 signs your pump needs a check-up',
  'Catch small problems early and save yourself a costly motor rewind.\n\nSeen any of these signs? Message us.',
  '#PumpRepair #PumpService #FarmTips'),
 ('06', 'Sun 11 Oct', 'Single photo · Festival', 'Happy Navratri',
  'Wishing you and your family a joyful Navratri. Jay Mataji!',
  '#Navratri #Navratri2026 #Garba #JayMataji'),
 ('07', 'Tue 13 Oct', 'Reel (18 sec)', "What's inside your pump?",
  'Ever wondered what happens deep inside your borewell?\n\nThe copper rotor spins. The impellers lift the water, stage by stage. More stages means more height.',
  '#HowItWorks #PumpBasics #Engineering'),
 ('08', 'Fri 16 Oct', 'Single photo', 'World Food Day',
  'Before food reaches our plate, a farmer works for months, and water makes it possible.\n\nThank you to every kisan.',
  '#WorldFoodDay #ThankYouFarmers #JaiKisan'),
 ('09', 'Sat 17 Oct', 'Carousel (5 slides)', 'Rabi season pump checklist',
  'Wheat, chana and mustard sowing starts soon.\n\nSpend 30 minutes checking your pump now and avoid a breakdown in the middle of the season.',
  '#RabiSeason #Wheat #FarmPrep'),
 ('10', 'Tue 20 Oct', 'Single photo · Festival', 'Happy Dussehra',
  'May this Vijayadashami bring strength and success to your family and your farm.',
  '#Dussehra #Vijayadashami #Dussehra2026'),
 ('11', 'Thu 22 Oct', 'Reel (15 sec)', 'Looking for dealers',
  'Run a hardware, pipe or agri shop? Add JJ pumps to your counter.\n\nV6 pump sets, copper-rotor motors, openwell pumps, spares and job work, with reliable supply from Ahmedabad.\n\nWhatsApp "DEALER" to +91 92271 06108.',
  '#DealershipOpportunity #PumpDealer #BusinessOpportunity'),
 ('12', 'Sat 24 Oct', 'Carousel (5 slides)', "How to read your pump's label",
  'Every pump has a steel label with its numbers. Now you know what they mean.\n\nSave this post!',
  '#PumpGuide #KnowYourPump'),
 ('13', 'Tue 27 Oct', 'Single photo', 'Our motors',
  'We make two V6 motor types: Full SS and Carbon Bearing.\n\nAsk us which one suits your borewell water.',
  '#SubmersibleMotor #V6Motor'),
 ('14', 'Thu 29 Oct', 'Reel (19 sec)', '3 mistakes that damage your pump',
  'Running it dry. Low voltage with no protection. The wrong size for your borewell.\n\nAvoid these three and your pump lasts longer. Share with a farmer friend.',
  '#PumpCare #FarmTips'),
 ('15', 'Sat 31 Oct', 'Carousel (5 slides)', 'Our pump set range',
  'One workshop, a full range of V6 pump sets, plus openwell pumps.\n\nTell us your borewell details and we will match the model.',
  '#PumpRange #V6Pump #OpenwellPump'),
 ('16', 'Tue 3 Nov', 'Reel (16 sec)', 'Repair and job work',
  "We don't just sell pumps. Bring your old one: we open it up, replace the worn parts and test it before it goes back.\n\nRepair · Spares · Job work.",
  '#PumpRepair #JobWork #Spares'),
 ('17', 'Fri 6 Nov', 'Single photo · Festival', 'Happy Dhanteras',
  'On Dhanteras we bring home new metal for good fortune. May your home and your fields prosper this year.',
  '#Dhanteras #Dhanteras2026 #ShubhDhanteras'),
 ('18', 'Sun 8 Nov', 'Single photo · Festival', 'Happy Diwali',
  'From the JJ Pumps family to yours: a bright, safe and happy Diwali.',
  '#HappyDiwali #Diwali2026 #Deepavali'),
 ('19', 'Tue 10 Nov', 'Single photo · Festival', 'New Year and Bhai Dooj',
  'Wishing you a prosperous new year full of good crops and good health. Saal Mubarak!',
  '#SaalMubarak #NutanVarshAbhinandan #BhaiDooj #GujaratiNewYear'),
 ('20', 'Thu 12 Nov', 'Carousel (4 slides)', 'How to order from JJ Pumps',
  'Ordering is simple. Save this post so our number is always with you.',
  '#OrderNow #PumpShop'),
]


def full_caption(c, tags):
    return f"{c}\n\n{CONTACT}\n\n{BASE} {tags}"


def files_for(n):
    return sorted(os.path.basename(f) for f in glob.glob(f'{RL}/{n}_*.mp4')) + sorted(os.path.basename(f) for f in glob.glob(f'{IMG}/{n}_*.jpg'))


# Captions.txt
lines = ['JJ PUMPS — SOCIAL MEDIA CAPTIONS (29 Sep – 12 Nov 2026)',
         'Post each one on Instagram and Facebook on the date shown, 7–9 PM India time.',
         'Copy everything between the dashed lines.', '']
for n, d, t, title, c, tags in P:
    fl = files_for(n)
    lines += ['=' * 50, f'POST {n} · {d} · {t}', title, 'Files: ' + ', '.join(fl), '-' * 50, full_caption(c, tags), '-' * 50]
    if 'Reel' in t:
        lines += ['Reel: upload the .mp4 from the Reels folder. Pick the reel-cover image as the cover.', MUSIC]
    lines.append('')
open(PK + '/Captions.txt', 'w').write('\n'.join(lines))

# thumbs
from PIL import Image
for f in glob.glob(IMG + '/*.jpg'):
    im = Image.open(f)
    im.thumbnail((240, 430))
    im.save(TH + '/' + os.path.basename(f), quality=80)

e = html.escape
AZ = '#0C2631'; AMB = '#1E4485'
cards = ''
for n, d, t, title, c, tags in P:
    imgs = sorted(glob.glob(f'{IMG}/{n}_*.jpg'))
    thumbs = ''.join(f"<img src='file://{TH}/{os.path.basename(f)}'>" for f in imgs)
    rn = ''
    if 'Reel' in t:
        rn = f"<div class='sc'><b>Reel video:</b> {e(', '.join(files_for(n)[:1]))} (Reels folder). Use the image shown as the reel cover. {e(MUSIC)}</div>"
    cards += (f"<section><div class='hd'><span class='n'>{n}</span><div><div class='d'>{e(d)} · {e(t)}</div><div class='t'>{e(title)}</div></div></div>"
              f"<div class='th'>{thumbs}</div><div class='cap'>{e(full_caption(c, tags))}</div>{rn}"
              f"<div class='fn'>{e(', '.join(files_for(n)))}</div></section>")
rows = ''.join(f"<tr><td>{n}</td><td>{e(d)}</td><td>{e(t)}</td><td>{e(title)}</td></tr>" for n, d, t, title, *_ in P)
doc = f"""<!doctype html><html><head><meta charset='utf-8'><style>
body {{ font-family: Poppins, sans-serif; color: #1d2a35; font-size: 10.5pt; }}
h1 {{ color: {AZ}; font-size: 24pt; margin: 0 0 4px }}
.sub {{ color: #4a5b6a; margin-bottom: 14px }}
ol.st {{ margin: 0 0 14px; padding-left: 18px }} ol.st li {{ margin: 3px 0 }}
table {{ width: 100%; border-collapse: collapse; font-size: 10pt }}
th {{ background: {AZ}; color: #fff; text-align: left; padding: 6px 8px }}
td {{ padding: 5px 8px; border-bottom: 1px solid #dde3e8 }}
.note {{ background: #EAF2FF; border-left: 4px solid {AMB}; padding: 8px 12px; margin: 12px 0; }}
section {{ page-break-inside: avoid; border: 1px solid #dde3e8; border-radius: 10px; padding: 12px 14px; margin: 0 0 12px }}
.hd {{ display: flex; gap: 12px; align-items: center; margin-bottom: 8px }}
.n {{ background: {AZ}; color: #fff; font-weight: 700; border-radius: 8px; padding: 6px 10px; font-size: 13pt }}
.d {{ color: {AMB}; font-weight: 700; font-size: 9.5pt }} .t {{ font-weight: 700; font-size: 13pt; color: {AZ} }}
.th {{ display: flex; gap: 6px; margin-bottom: 8px }} .th img {{ height: 118px; border-radius: 4px; border: 1px solid #ccd }}
.cap {{ white-space: pre-wrap; background: #F2F6FD; padding: 8px 10px; border-radius: 6px }}
.sc {{ margin-top: 8px }}
.fn {{ color: #7a8a98; font-size: 8pt; margin-top: 6px }}
.br {{ page-break-after: always }}
</style></head><body>
<h1>JJ Pumps — Social Media Pack</h1>
<div class='sub'>20 posts · 29 Sep – 12 Nov 2026 · Instagram &amp; Facebook · 3 posts a week · 5 finished reels</div>
<b>How to post, step by step</b>
<ol class='st'>
<li>Find the post number and date below. Its files start with the same number.</li>
<li><b>Photo or carousel:</b> open the <b>Images</b> folder and upload the image(s). For a carousel, upload all slides together, in order (1of5, 2of5…).</li>
<li><b>Reel:</b> open the <b>Reels</b> folder and upload the .mp4. When asked for a cover, pick the matching reel-cover image from the Images folder.</li>
<li>Reels have no sound. Add a trending instrumental from the app's music library.</li>
<li>Copy that post's caption from <b>Captions.txt</b> (easier to copy than this PDF).</li>
<li>Post to Instagram and Facebook together using Meta Business Suite, <b>7–9 PM India time</b>.</li>
</ol>
<div class='note'>Brand labels on the pump nameplates are hidden. Festival dates can shift by a day by region: check your local panchang for Gujarati New Year (planned for Tue 10 Nov). Background photos are free Pexels photos, fine for ads with no credit needed.</div>
<table><tr><th>#</th><th>Date</th><th>Type</th><th>Topic</th></tr>{rows}</table>
<div class='br'></div>
{cards}
</body></html>"""
open(W + '/guide2.html', 'w').write(doc)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto('file://' + W + '/guide2.html')
    pg.wait_for_timeout(500)
    pg.pdf(path=PK + '/Posting-Guide.pdf', format='A4', print_background=True, margin={'top': '14mm', 'bottom': '14mm', 'left': '14mm', 'right': '14mm'})
    b.close()
print('ok')
