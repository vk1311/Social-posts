# tools/w04_build.py — finish W04 with real logos and screenshots

1. Save each platform's **official** logo (from its brand or press page) as a PNG with a transparent background: `logos/google.png`, `logos/clutch.png`, `logos/bing.png`, `logos/apple.png`, `logos/yelp.png`, `logos/yellowpages.png`.
2. Screenshot Waypoint's own listing on each platform, ideally the top of the listing showing the name, category and number. Save as `shots/<same slug>.png`. Any size works; the image is scaled to fill a 900×510 frame and cropped from the top-left.
3. Run:
   `python3 tools/w04_build.py /path/to/waypoint_renderer logos shots out`
4. The new slides are in `out/W04/`, with the same file names as in this zip. Any slide whose logo or screenshot is missing keeps its placeholder.

Needs Pillow and the Waypoint renderer folder (`render.py` + `fonts/`).
