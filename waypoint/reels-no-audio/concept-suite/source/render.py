#!/usr/bin/env python3
"""Render Waypoint concept-suite reels.

  python3 render.py --stills s01_crm 2 4.5 7 10 13 15 17 20.5   -> stills/<name>_<t>.png
  python3 render.py --video s01_crm [s02_booking ...]           -> out/<name>.mp4 + cover
Each module exposes ALL = [reel_dict, ...].
"""
import sys, os, subprocess, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from shell import page
from playwright.sync_api import sync_playwright

OUT = os.path.join(HERE, "out")
FPS, DUR = 30, 21.5


def reels(mods):
    for m in mods:
        mod = importlib.import_module(m)
        for r in mod.ALL:
            p = os.path.join(HERE, "html", f"{r['name']}.html")
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w").write(page(r))
            yield r, p


def open_page(b, path):
    pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.goto("file://" + path)
    pg.wait_for_function("window.READY===true", timeout=20000)
    return pg, errs


def stills(mods, times, scale=0.5):
    d = os.path.join(HERE, "stills"); os.makedirs(d, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for r, path in reels(mods):
            pg, errs = open_page(b, path)
            for t in times:
                pg.evaluate(f"render({t})")
                f = os.path.join(d, f"{r['name']}_{t:05.2f}.png")
                pg.screenshot(path=f)
                if scale != 1:
                    from PIL import Image
                    im = Image.open(f); im.resize((int(1080*scale), int(1920*scale))).save(f)
            print(r["name"], "stills ok", "ERRORS: " + "; ".join(errs[:5]) if errs else "")
            pg.close()
        b.close()


def video(mods):
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for r, path in reels(mods):
            pg, errs = open_page(b, path)
            out = os.path.join(OUT, f"{r['name']}.mp4")
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                                   "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                                   "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", out],
                                  stdin=subprocess.PIPE)
            for i in range(int(FPS * DUR)):
                pg.evaluate(f"render({i / FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=93))
            ff.stdin.close(); ff.wait()
            pg.evaluate("render(1.6)")
            pg.screenshot(path=os.path.join(OUT, f"{r['name']}_cover.jpg"), type="jpeg", quality=92)
            print("done", out, ("ERRORS: " + "; ".join(errs[:3])) if errs else "")
            pg.close()
        b.close()


if __name__ == "__main__":
    mode, args = sys.argv[1], sys.argv[2:]
    mods = [a for a in args if not a.replace(".", "").isdigit()]
    if mode == "--stills":
        stills(mods, [float(a) for a in args if a.replace(".", "").isdigit()])
    else:
        video(mods)
