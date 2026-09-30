#!/usr/bin/env python3
import os
from render import card

OUT = "/mnt/user-data/outputs/waypoint-october"
os.makedirs(OUT, exist_ok=True)
REEL = (1080, 1920)

def single(name, blocks, variant="ink"):
    card(f"{OUT}/{name}.png", blocks, variant=variant)

def carousel(name, slides):
    tot = len(slides)
    for i, (variant, blocks) in enumerate(slides, 1):
        card(f"{OUT}/{name}_s{i}.png", blocks, variant=variant, slide=(i, tot))

def reel(name, frame1, endcard, v1="ink", v2="ink"):
    card(f"{OUT}/{name}_frame1.png", frame1, variant=v1, size=REEL, scale=1.3)
    card(f"{OUT}/{name}_endcard.png", endcard, variant=v2, size=REEL, scale=1.3)

# 01 — Thu Oct 1 — humour
single("02_sep24_humour_winter-checklist", [
    ("kicker", "Winter Preparedness Checklist"),
    ("rule", None),
    ("check", [(True, "Blades changed"),
               (True, "Salt ordered"),
               (True, "Trucks greased"),
               (True, "Two new subs hired"),
               (False, "Anyone knows which driveways they're doing")]),
])

# 02 — Sat Oct 3 — comparison carousel
carousel("03_sep26_comparison_offtheshelf", [
    ("ink",     [("kicker", "Comparison"), ("hook", "Off-the-shelf, or built for your shop."), ("rule", None)]),
    ("paper",   [("kv", [("Price — theirs", "Per user, per month, forever. It goes up when you hire."),
                         ("Price — mine", "$1,200 to build. $60 a month. Flat.")])]),
    ("ink",     [("kv", [("Support — theirs", "A ticket queue and a help centre article."),
                         ("Support — mine", "The person who built it. 902-670-9297.")])]),
    ("paper",   [("kv", [("Changes — theirs", "File a feature request and wait. Or hire a developer to bolt something on the side."),
                         ("Changes — mine", "I change it.")])]),
    ("ink",     [("kicker", "The rest of your stack"),
                 ("body", "It plugs into what you already run, because it's built after I look at what you already run.")]),
    ("ink", [("big", "Your name on it. Not theirs. Hosted in Canada.")]),
])

# 03 — Sun Oct 4 — business plan
single("01_sep23_readymade", [
    ("hook", "I stopped selling readymade."),
    ("rule", None),
    ("body", "I build software — CRMs, booking, invoicing, job logging. What I don't do anymore is hand you a product and ask you to fit your shop around it."),
])

# 04 — Tue Oct 6 — feature reel
reel("05_sep29_feature_signing",
     [("hook", "Signed at 6:40 in the morning, on a phone, in a truck.")],
     [("big", "The signed PDF is emailed to you and to them the moment they tap sign.")])

# 05 — Thu Oct 8 — humour
single("06_oct01_humour_dispatcher", [
    ("kicker", "Dispatcher's Last Words"),
    ("rule", None),
    ("hook", "\u201cDarrell knows the route.\u201d"),
], variant="ink")

# 06 — Sat Oct 10 — comparison carousel
carousel("07_oct03_comparison_jobber", [
    ("ink",     [("hook", "Jobber is good software."), ("rule", None)]),
    ("paper",   [("body", "It's built for tens of thousands of contractors. Which means it's built for none of them exactly.")]),
    ("ink",     [("body", "So you learn their words for your job. Their fields. Their idea of a visit.")]),
    ("paper",   [("body", "You end up with a column you don't use, and a thing you do that has nowhere to go.")]),
    ("ink", [("big", "I go the other way. One shop, one process, built around how you already work.")]),
])

# 07 — Sun Oct 11 — non-trades
single("08_oct04_clinic", [
    ("kicker", "Not a contractor post"),
    ("hook", "The front desk is a person and a paper daybook."),
    ("rule", None),
    ("body", "Clinic runs fine until she's off. Then nobody knows who's booked, who owes for last month, or whether the Tuesday cancellation got filled."),
], variant="paper")

# 08 — Tue Oct 13 — feature reel
reel("09_oct06_feature_missedcall",
     [("hook", "The call you didn't catch.")],
     [("big", "Every missed call gets a text back in seconds. Automatically.")])

# 09 — Thu Oct 15 — humour
single("10_oct08_humour_audit", [
    ("kicker", "Business Process Audit"),
    ("rule", None),
    ("kv", [("Current process", "The deposit is a screenshot of an e-transfer in a group chat."),
            ("Risk level", "Extremely high.")]),
])

# 10 — Sat Oct 17 — comparison carousel
carousel("11_oct10_comparison_integrations", [
    ("ink",     [("hook", "\u201cWe integrate with everything\u201d usually means \u201cyou'll need a developer.\u201d"), ("rule", None)]),
    ("paper",   [("body", "Off-the-shelf connects their fields to another company's fields. Your job names, your invoice numbers, your way of quoting sit in the middle of that \u2014 unaccounted for.")]),
    ("ink",     [("body", "So you hire someone to write the glue, or you retype it, or you drop the field.")]),
    ("ink", [("big", "I build the CRM. There's no glue \u2014 the fields are yours because I made them yours.")]),
    ("paper",   [("body", "And where a real outside system has to be in it \u2014 accounting, payments, email \u2014 I wire that in and it stays wired. That's a build, not a checkbox on a pricing page.")]),
    ("ink",     [("big", "Your process in the middle. Everything else arranged around it.")]),
])

# 11 — Sun Oct 18 — phone line
single("04_sep27_phone", [
    ("kicker", "New number"),
    ("hook", "902-670-9297"),
    ("rule", None),
    ("body", "Spells WAYP, which was the whole reason. Waypoint has a real line now. Text it \u2014 that's faster, and I'll answer either way. Kentville, NS."),
])

# 12 — Tue Oct 20 — feature reel
reel("13_oct13_feature_receipt",
     [("hook", "Mark it paid.")],
     [("big", "Marking it paid sends the receipt. You don't write a second email.")])

# 13 — Thu Oct 22 — humour
single("14_oct15_humour_translation", [
    ("kicker", "Customer Translation Guide"),
    ("rule", None),
    ("kv", [("What they said", "\u201cCan you just do the one side?\u201d"),
            ("What it means", "The whole lot. Twice. Before 6am.")]),
], variant="paper")

# 14 — Sat Oct 24 — comparison carousel
carousel("15_oct17_comparison_quickbooks", [
    ("ink",     [("hook", "QuickBooks is a filing cabinet that can add."), ("rule", None)]),
    ("paper",   [("body", "It's excellent at telling you what already happened.")]),
    ("ink",     [("body", "It has nothing to say at 9pm on a Sunday when there are six estimates to write.")]),
    ("ink", [("big", "The front of the job is the part nobody built for you. That's the part I build.")]),
])

# 15 — Sun Oct 25 — podcast
single("12_oct11_podcast", [
    ("kicker", "Podcast"),
    ("hook", "For the drive."),
    ("rule", None),
    ("body", "Started a podcast for owners who'd rather listen than read. Episode one: getting found and getting paid, without the hype. On YouTube \u2014 link in bio."),
])

# 16 — Tue Oct 27 — feature reel
reel("17_oct20_feature_requestform",
     [("hook", "From your website to the route. Without retyping.")],
     [("big", "A request becomes a stop on the route, address already on it.")])

# 17 — Thu Oct 29 — humour
single("18_oct22_humour_whiteboard", [
    ("kicker", "Manual Process Hall of Fame"),
    ("rule", None),
    ("hook", "The whiteboard gets photographed every morning."),
    ("body", "In case someone wipes it."),
])

# 18 — Sat Oct 31 — feature carousel
carousel("16_oct18_feature_howabuildworks", [
    ("ink",     [("hook", "What a build actually looks like."), ("rule", None)]),
    ("paper",   [("kicker", "Step one"), ("body", "One call. I watch how you do it now, and write it down.")]),
    ("ink", [("big", "$1,200 to build. $60 a month after. Half up front, no contract length.")]),
    ("ink",     [("kicker", "Step two"), ("body", "Two weeks, usually. You see it working before you pay the rest.")]),
    ("paper",   [("big", "Then it's yours, and I keep it running.")]),
])

print("rendered:", len(os.listdir(OUT)), "files")
