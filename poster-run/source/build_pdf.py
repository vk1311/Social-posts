"""Render the Waypoint designs in project/ to ../waypoint-flyers-print.pdf and ../png/.

Run after gen_print.py:  python3 build_pdf.py
Needs: pip install playwright pypdf  and  playwright install chromium
Pass a folder to write somewhere else first:  python3 build_pdf.py /tmp/check
"""
import os, sys, tempfile
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(HERE)

# (source file in project/, image name in png/), in PDF page order
PAGES = [
    ("Main", "1-waypoint-A-fit"),
    ("Waypoint-by-hand", "2-waypoint-B-by-hand"),
    ("Waypoint-counter-cards-front", "3a-waypoint-C-counter-cards-front-4up"),
    ("Waypoint-counter-cards-back", "3b-waypoint-C-counter-cards-back-4up"),
    ("Apps-whole-business", "4-apps-A-whole-business"),
    ("Apps-market-sellers", "5-apps-B-market-sellers"),
    ("Apps-take-one-cards", "6-apps-C-take-one-cards-4up"),
]


def load(page, url):
    page.goto(url)
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(500)


def main():
    os.makedirs(os.path.join(OUT, "png"), exist_ok=True)
    writer = PdfWriter()
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        browser = p.chromium.launch()
        pdf_page = browser.new_page()
        png_page = browser.new_page(viewport={"width": 816, "height": 1056}, device_scale_factor=2)
        for src, png in PAGES:
            url = "file://" + os.path.join(HERE, "project", src + ".dc.html")
            load(pdf_page, url)
            one = os.path.join(tmp, src + ".pdf")
            pdf_page.pdf(path=one, width="8.5in", height="11in", print_background=True,
                         margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
            reader = PdfReader(one)
            assert len(reader.pages) == 1, f"{src} spilled onto {len(reader.pages)} pages"
            writer.add_page(reader.pages[0])
            load(png_page, url)
            png_page.screenshot(path=os.path.join(OUT, "png", png + ".png"),
                                clip={"x": 0, "y": 0, "width": 816, "height": 1056})
        browser.close()
        with open(os.path.join(OUT, "waypoint-flyers-print.pdf"), "wb") as f:
            writer.write(f)
    print("wrote", os.path.join(OUT, "waypoint-flyers-print.pdf"), "and", len(PAGES), "images")


if __name__ == "__main__":
    main()
