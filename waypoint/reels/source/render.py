#!/usr/bin/env python3
"""Build HTML for each reel, then either grab stills (--stills) or render full MP4s."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from shell import page
from reels import ALL
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/user-data/outputs/waypoint-reel-videos"
FPS, DUR = 30, 21.5


def build():
    paths = []
    for r in ALL:
        p = os.path.join(HERE, f"{r['name']}.html")
        open(p, "w").write(page(r))
        paths.append((r, p))
    return paths


def open_page(b, path):
    pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    pg.goto("file://" + path)
    pg.wait_for_function("window.READY===true", timeout=20000)
    return pg, errs


def stills(which, times):
    os.makedirs(os.path.join(HERE, "stills"), exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for r, path in build():
            if which and r["name"][:2] not in which:
                continue
            pg, errs = open_page(b, path)
            for t in times:
                pg.evaluate(f"render({t})")
                pg.screenshot(path=os.path.join(HERE, "stills", f"{r['name'][:2]}_{t:05.2f}.png"))
            if errs:
                print(r["name"], "ERRORS:", errs[:5])
            pg.close()
        b.close()


def video(which):
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for r, path in build():
            if which and r["name"][:2] not in which:
                continue
            pg, errs = open_page(b, path)
            out = os.path.join(OUT, f"{r['name']}.mp4")
            ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                                   "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                                   "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", out],
                                  stdin=subprocess.PIPE)
            n = int(FPS * DUR)
            for i in range(n):
                pg.evaluate(f"render({i / FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=94))
            ff.stdin.close(); ff.wait()
            pg.evaluate("render(1.6)")
            pg.screenshot(path=os.path.join(OUT, f"{r['name']}_cover.jpg"), type="jpeg", quality=92)
            print("done", out, "errors:" if errs else "", errs[:3] if errs else "")
            pg.close()
        b.close()


if __name__ == "__main__":
    mode = sys.argv[1]
    which = [w for w in sys.argv[2:] if w.startswith("R")]
    if mode == "--stills":
        ts = [float(x) for x in sys.argv[2:] if not x.startswith("R")]
        stills(which, ts)
    else:
        video(which)
