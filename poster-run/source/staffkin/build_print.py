"""Rebuild the Staffkin print PDF and images (25 Oct 2026: pretty QR on counter card, board poster, pocket cards).
Run:  python3 build_print.py   (needs qrcode, playwright, pypdf)
Writes assets/qr-*.svg, runs render.py, then prints ../../staffkin-flyers-print.pdf and ../../png/7a..11.
The reference postcard keeps its original QR (assets/qr-refs.png), as approved."""
import os, sys, subprocess, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from prettyqr import pretty_qr, STAFFKIN_RINGS
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader

OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(HERE))
for name, src in [("counter", "counter-card"), ("poster", "board-poster"), ("pocket", "pocket-card")]:
    svg = pretty_qr(f"https://staffkin.com/?utm_source={src}", dot="#2E2A6B", ring="#2E2A6B", eye="#7B8CF5",
                    logo=STAFFKIN_RINGS, label="QR code to staffkin.com")
    open(os.path.join(HERE, "assets", f"qr-{name}.svg"), "w").write(svg)
subprocess.run([sys.executable, os.path.join(HERE, "render.py")], check=True)

PAGES = [("Counter-front", "7a-staffkin-A-counter-card-front-4up"), ("Counter-back", "7b-staffkin-A-counter-card-back-4up"),
         ("Postcard-front", "8-staffkin-B-ref-postcard-front-4up"), ("Postcard-back", "9-staffkin-B-ref-postcard-back-4up"),
         ("Pocket-cards", "11-staffkin-D-pocket-cards-10up"), ("Board-poster", "10-staffkin-C-board-poster")]
os.makedirs(os.path.join(OUT, "png"), exist_ok=True)
w = PdfWriter()
with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    shot = b.new_page(viewport={"width": 816, "height": 1056}, device_scale_factor=1.5625)
    for src, png in PAGES:
        url = "file://" + os.path.join(HERE, "assets", src + ".html")
        for page in (pg, shot):
            page.goto(url); page.wait_for_load_state("networkidle"); page.evaluate("document.fonts.ready"); page.wait_for_timeout(400)
        f = os.path.join(tmp, src + ".pdf")
        pg.pdf(path=f, width="8.5in", height="11in", print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        r = PdfReader(f); assert len(r.pages) == 1, src
        w.add_page(r.pages[0])
        shot.screenshot(path=os.path.join(OUT, "png", png + ".png"), clip={"x": 0, "y": 0, "width": 816, "height": 1056})
    b.close()
with open(os.path.join(OUT, "staffkin-flyers-print.pdf"), "wb") as fh:
    w.write(fh)
print("wrote", os.path.join(OUT, "staffkin-flyers-print.pdf"))
