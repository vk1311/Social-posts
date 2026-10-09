#!/usr/bin/env python3
"""Voiceover versions of the concept-suite reels (Kokoro TTS, same engine as Snortlo).

  python3 vo.py af_bella am_michael          -> out_vo/<voice>/<name>.mp4 for every reel
  python3 vo.py am_michael s01_crm           -> one reel
Lines come from vo_script.py; each is fitted inside its caption window (speed raised up to 1.3x if needed).
Music is ducked under the voice; UI sounds stay, a little lower.
"""
import sys, os, glob, importlib, subprocess
import numpy as np
import soundfile as sf
from scipy.signal import resample_poly
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import audio as A
from vo_script import STING
from vo_tight import VO

KDIR = "/home/claude/kokoro"
_K = None


def kokoro():
    global _K
    if _K is None:
        from kokoro_onnx import Kokoro
        _K = Kokoro(os.path.join(KDIR, "model.onnx"), os.path.join(KDIR, "voices-v1.0.bin"))
    return _K


def trim(x, thr=0.01):
    idx = np.where(np.abs(x) > thr)[0]
    if not len(idx): return x
    a, b = max(0, idx[0] - 240), min(len(x), idx[-1] + 2400)
    return x[a:b]


def say(text, voice, window):
    """Synthesize text so it fits within `window` seconds. Returns (audio at 44.1k, speed, fits)."""
    speed = 1.08
    for _ in range(4):
        a, sr = kokoro().create(text, voice=voice, speed=speed, lang="en-us")
        a = trim(a.astype(np.float64))
        dur = len(a) / sr
        if dur <= window or speed >= 1.15:
            break
        speed = min(1.15, speed * dur / window * 1.03)
    a = resample_poly(a, 147, 80)  # 24000 -> 44100
    return a, speed, dur <= window


def lines_for(reel):
    v = VO[reel["name"]]
    out = [(0.3, 3.05, v["hook"])]
    for (c0, c1, _), txt in zip(reel["caps"], v["caps"]):
        out.append((c0 + 0.05, c1 - 0.05, txt))
    out.append((16.05, 18.8, v["end"]))
    out.append((19.05, 21.3, STING))
    return out


def build(modname, reel, voice):
    n = int(A.DUR * A.SR)
    vo = np.zeros(n)
    report = []
    for a, b, txt in lines_for(reel):
        x, sp, fits = say(txt, voice, b - a)
        A.place(vo, x * 0.95, a)
        report.append((a, b, round(sp, 2), round(len(x) / A.SR, 2), fits, txt))
    # music + effects (same composition as the music-only versions)
    bed, _ = A.music(int(reel["name"][1:3]))
    fx = np.zeros(n)
    taps, views, typing, ho = A.events(modname)
    for t0 in taps: A.place(fx, A.sfx_tap(), t0, 0.8)
    for i, v in enumerate(views): A.place(fx, A.sfx_whoosh(0.5 if i == 0 else 0.4), max(0, v - 0.15), 0.9 if i == 0 else 0.6)
    for s0, s1 in typing:
        k = s0
        while k < s1:
            A.place(fx, A.sfx_key(), k, 0.8); k += A.rng.uniform(0.055, 0.1)
    for h in ho: A.place(fx, A.sfx_chime(), h + 0.05, 0.8)
    A.place(fx, A.sfx_whoosh(0.5), 15.55, 0.6)
    A.place(fx, A.sfx_sting(), 18.95, 0.9)
    # duck music to ~30% while the voice speaks (smoothed)
    active = A.lp((np.abs(vo) > 0.004).astype(float), 3)
    duck = 1 - 0.7 * np.clip(active * 3, 0, 1)
    bedm = bed * duck[:, None] * 0.85
    mix = bedm + np.stack([fx, fx], 1) * 0.85 + np.stack([vo, vo], 1) * 1.15
    t = np.arange(n) / A.SR
    mix *= np.interp(t, [0, 0.05, A.DUR - 0.5, A.DUR], [0, 1, 1, 0])[:, None]
    mix /= max(1e-9, np.abs(mix).max()) / 0.89
    return mix, report


def main(voices, mods):
    for voice in voices:
        od = os.path.join(HERE, "out_vo", voice); os.makedirs(od, exist_ok=True)
        ad = os.path.join(HERE, "audio_vo", voice); os.makedirs(ad, exist_ok=True)
        for m in mods:
            reel = importlib.import_module(m).ALL[0]
            mix, report = build(m, reel, voice)
            wav = os.path.join(ad, reel["name"] + ".wav")
            A.write_wav(wav, mix)
            out = os.path.join(od, reel["name"] + ".mp4")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(HERE, "out", reel["name"] + ".mp4"), "-i", wav,
                            "-af", "loudnorm=I=-16:TP=-1.5:LRA=9", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                            "-map", "0:v:0", "-map", "1:a:0", "-shortest", "-movflags", "+faststart", out], check=True)
            bad = [r for r in report if not r[4]]
            print(voice, reel["name"], "max speed", max(r[2] for r in report), "| OVERRUN:" if bad else "| all lines fit", bad if bad else "")


if __name__ == "__main__":
    args = sys.argv[1:]
    voices = [a for a in args if a[:3] in ("af_", "am_", "bf_", "bm_")] or ["af_bella", "am_michael"]
    mods = [a for a in args if a not in voices] or sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE, "s[01][0-9]_*.py")))
    main(voices, mods)
