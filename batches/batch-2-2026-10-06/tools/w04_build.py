"""Rebuild W04 with real logos + listing screenshots.

Usage:
  python3 w04_build.py <path-to-waypoint_renderer> <logos_dir> <shots_dir> <out_dir>

logos_dir/<slug>.png and shots_dir/<slug>.png, slugs: google, clutch, bing, apple, yelp, yellowpages.
Any missing file keeps its placeholder. Output: <out_dir>/W04/W04_Sat-24-Oct_carousel_<n>of8.png
"""
import sys, os
RENDERER, LOGO_DIR_ARG, SHOT_DIR_ARG, OUT = sys.argv[1:5]
sys.path.insert(0, RENDERER)
from render import card, INK, PAPER, SLATE, MIST, MAGENTA, body, head
from PIL import Image, ImageDraw
import datetime


def path(pid, iso, typ, n=None, tot=None):
    folder = os.path.join(OUT, pid); os.makedirs(folder, exist_ok=True)
    d = datetime.date.fromisoformat(iso).strftime("%a-%d-%b")
    return os.path.join(folder, f"{pid}_{d}_{typ}" + (f"_{n}of{tot}" if n else "") + ".png")

# ---------------------------------------------------------------- W04 listings (placeholders for logo + screenshot)
PLATFORMS = [
    ("google", "Google Business Profile", "Directions, hours and reviews on Google Search and Maps."),
    ("clutch", "Clutch", "A directory of B2B service providers."),
    ("bing", "Bing Places", "The listing behind Bing search and Bing Maps."),
    ("apple", "Apple Business Connect", "How the business shows up in Apple Maps."),
    ("yelp", "Yelp", "Local business listings and reviews."),
    ("yellowpages", "Yellow Pages", "The Canadian business directory."),
]
LOGO_DIR = LOGO_DIR_ARG
SHOT_DIR = SHOT_DIR_ARG


def w04_slide(out, n, tot, slug, name, line, variant):
    # text block sits in the top third; the frame below holds the logo + screenshot
    card(out, [("kicker", f"Listed on {name}"), ("big", line), ("gap", 560)], variant=variant, slide=(n, tot))
    im = Image.open(out).convert("RGB")
    d = ImageDraw.Draw(im)
    fg = PAPER if variant == "ink" else INK
    sub = MIST if variant == "ink" else SLATE
    x0, y0, x1, y1 = 90, 640, 990, 1150
    # logo tile
    lt = (x0, y0 - 130, x0 + 110, y0 - 20)
    logo = os.path.join(LOGO_DIR, f"{slug}.png")
    shot = os.path.join(SHOT_DIR, f"{slug}.png")
    if os.path.exists(logo):
        L = Image.open(logo).convert("RGBA"); L.thumbnail((110, 110))
        im.paste(L, (lt[0], lt[1] + (110 - L.height) // 2), L)
    else:
        d.rounded_rectangle(lt, 18, outline=sub, width=3)
        d.text((lt[0] + 16, lt[1] + 40), "LOGO", font=body(26, "Medium"), fill=sub)
    if os.path.exists(shot):
        S = Image.open(shot).convert("RGB")
        w, h = x1 - x0, y1 - y0
        r = max(w / S.width, h / S.height)
        S = S.resize((int(S.width * r), int(S.height * r)))
        S = S.crop((0, 0, w, h))
        mask = Image.new("L", (w, h), 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, w, h), 22, fill=255)
        im.paste(S, (x0, y0), mask)
        d.rounded_rectangle((x0, y0, x1, y1), 22, outline=MAGENTA, width=4)
    else:
        d.rounded_rectangle((x0, y0, x1, y1), 22, outline=MAGENTA, width=4)
        d.text((x0 + 40, y0 + 220), f"Screenshot: Waypoint on {name}", font=body(34, "Medium"), fill=fg)
        d.text((x0 + 40, y0 + 270), "(to be captured)", font=body(30), fill=sub)
    im.save(out)


def build_w04():
    iso = "2026-10-24"
    tot = len(PLATFORMS) + 2
    card(path("W04", iso, "carousel", 1, tot), [
        ("kicker", "Directory"), ("hook", "Where Waypoint is listed."), ("rule", None),
        ("body", "Six places to find the business, its hours and its number. One slide each.")], variant="ink", slide=(1, tot))
    for i, (slug, name, line) in enumerate(PLATFORMS, 2):
        w04_slide(path("W04", iso, "carousel", i, tot), i, tot, slug, name, line, "paper" if i % 2 == 0 else "ink")
    card(path("W04", iso, "carousel", tot, tot), [
        ("kicker", "Or call"), ("big", "902-670-9297"), ("rule", None),
        ("body", "waypointns.ca · hello@waypointns.ca · Kentville, Nova Scotia")], variant="ink", slide=(tot, tot))



build_w04()
print("W04 rebuilt in", OUT)
