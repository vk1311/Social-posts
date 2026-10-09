#!/usr/bin/env python3
"""Original audio for the concept-suite reels: a composed music bed plus UI sound effects
timed to each reel's on-screen events (taps, typing, screen changes, hand-off toast, logo sting).
Everything is synthesised here, so it's original and cleared for business use.

  python3 audio.py                 -> audio/<name>.wav for every reel + out_audio/<name>.mp4
  python3 audio.py s03_quotes      -> just that reel
"""
import sys, os, re, glob, importlib, subprocess
import numpy as np
from scipy.signal import butter, sosfilt

SR = 44100
DUR = 21.5
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
rng = np.random.default_rng(7)


def t_axis(d):
    return np.arange(int(d * SR)) / SR


def lp(x, fc, order=2):
    return sosfilt(butter(order, fc, 'low', fs=SR, output='sos'), x)


def hp(x, fc, order=2):
    return sosfilt(butter(order, fc, 'high', fs=SR, output='sos'), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], 'band', fs=SR, output='sos'), x)


def env(n, a, d, s_lvl, r, hold=None):
    """ADSR in seconds -> array of length n."""
    a_n, d_n, r_n = int(a * SR), int(d * SR), int(r * SR)
    e = np.full(n, s_lvl, dtype=float)
    a_n = min(a_n, n); e[:a_n] = np.linspace(0, 1, a_n, endpoint=False)
    d_end = min(n, a_n + d_n); e[a_n:d_end] = np.linspace(1, s_lvl, d_end - a_n, endpoint=False)
    if r_n and n > r_n:
        e[-r_n:] *= np.linspace(1, 0, r_n)
    return e


def midi(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def place(buf, sig, t0, gain=1.0):
    i = int(t0 * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[:j - i] * gain


# ------------------------------------------------------------------ instruments
def pad_note(f, d):
    t = t_axis(d)
    x = sum(np.sin(2 * np.pi * f * (1 + det) * t + ph) for det, ph in [(-0.004, 0), (0.0, 1.1), (0.0045, 2.3)])
    x += 0.35 * sum(np.sin(2 * np.pi * 2 * f * (1 + det) * t) for det in (-0.003, 0.003))
    x = lp(x, 1800)
    return x * env(len(t), 0.6, 0.4, 0.8, 0.8) * 0.12


def pluck(f, d=0.6):
    t = t_axis(d)
    x = np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * 2 * f * t) + 0.15 * np.sin(2 * np.pi * 3 * f * t)
    return lp(x, 3200) * np.exp(-t * 7) * 0.16


def bass(f, d):
    t = t_axis(d)
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2 * f * t)
    return lp(x, 400) * env(len(t), 0.01, 0.15, 0.7, 0.12) * 0.32


def kick():
    t = t_axis(0.35)
    f = 50 + 70 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 9) * 0.55


def snap():
    t = t_axis(0.18)
    n = bp(rng.standard_normal(len(t)), 1500, 6000)
    return n * np.exp(-t * 28) * 0.12


def hat():
    t = t_axis(0.06)
    return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t * 70) * 0.05


# ------------------------------------------------------------------ sound effects
def sfx_tap():
    t = t_axis(0.07)
    x = np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 90) + 0.6 * bp(rng.standard_normal(len(t)), 2000, 7000) * np.exp(-t * 140)
    return x * 0.22


def sfx_key():
    t = t_axis(0.045)
    x = bp(rng.standard_normal(len(t)), 1800, 5200) * np.exp(-t * 160)
    return x * rng.uniform(0.07, 0.11)


def sfx_whoosh(d=0.45):
    t = t_axis(d)
    n = rng.standard_normal(len(t))
    # sweep a band-pass upward by crossfading two filtered layers
    lo, hi = bp(n, 300, 1400), bp(n, 1400, 6000)
    w = np.linspace(0, 1, len(t))
    shape = np.sin(np.pi * w) ** 2
    return (lo * (1 - w) + hi * w) * shape * 0.08


def sfx_chime():
    out = np.zeros(int(0.9 * SR))
    for i, m in enumerate((84, 88)):  # C6, E6
        t = t_axis(0.9 - i * 0.09)
        f = midi(m)
        x = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2.01 * f * t)) * np.exp(-t * 5)
        place(out, x * 0.14, i * 0.09)
    return out


def sfx_sting():
    """Soft resolving bell chord for the logo."""
    out = np.zeros(int(2.6 * SR))
    for i, m in enumerate((72, 76, 79, 84)):
        t = t_axis(2.6 - i * 0.06)
        f = midi(m)
        x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 2.76 * f * t) * np.exp(-t * 3)
        place(out, x * np.exp(-t * 1.6) * 0.09, i * 0.06)
    return out


# ------------------------------------------------------------------ reverb (cheap feedback delays)
def reverb(x, mix=0.22):
    out = x.copy()
    for d, g in [(0.029, 0.42), (0.037, 0.38), (0.041, 0.35), (0.053, 0.3)]:
        n = int(d * SR); y = np.zeros_like(x)
        for k in range(1, 8):
            if n * k >= len(x): break
            y[n * k:] += x[:-n * k] * (g ** k)
        out += lp(y, 5000) * mix / 2
    return out


# ------------------------------------------------------------------ music bed
PROGS = [  # (root-key chords as midi triads/7ths), tempo
    ([[48, 55, 59, 64], [45, 52, 55, 60], [41, 48, 52, 57], [43, 50, 55, 59]], 96),   # Cmaj7 Am7 Fmaj7 G
    ([[50, 57, 60, 65], [46, 53, 57, 62], [43, 50, 55, 58], [45, 52, 57, 61]], 92),   # Dm7 Bbmaj7 Gm7 A
    ([[45, 52, 55, 60], [41, 48, 52, 57], [48, 55, 59, 64], [43, 50, 55, 59]], 98),   # Am7 Fmaj7 Cmaj7 G
    ([[43, 50, 54, 59], [40, 47, 50, 55], [36, 43, 47, 52], [38, 45, 50, 54]], 94),   # Gmaj7 Em7 Cmaj7 D
]


def music(seed):
    prog, bpm = PROGS[seed % len(PROGS)]
    beat = 60 / bpm
    bar = beat * 4
    n = int(DUR * SR)
    padL, padR = np.zeros(n), np.zeros(n)
    plk, bs, drums = np.zeros(n), np.zeros(n), np.zeros(n)
    nbars = int(np.ceil(DUR / bar)) + 1
    for b in range(nbars):
        ch = prog[b % 4]
        t0 = b * bar
        for k, m in enumerate(ch[1:]):
            note = pad_note(midi(m + 12), bar + 0.6)
            place(padL if k % 2 else padR, note, t0)
            place(padR if k % 2 else padL, note, t0, 0.6)
        # bass on beats 1 and 3 (+ pickup)
        place(bs, bass(midi(ch[0] - 12), beat * 1.8), t0)
        place(bs, bass(midi(ch[0] - 12), beat * 1.6), t0 + beat * 2)
        # arpeggio in 8ths from 3.0 s on
        arp = [ch[1], ch[2], ch[3], ch[2] + 12, ch[3], ch[2], ch[1] + 12, ch[3]]
        for i, m in enumerate(arp):
            tt = t0 + i * beat / 2
            if 3.0 <= tt < 15.9:
                place(plk, pluck(midi(m + 12)), tt, 0.9 if i % 2 == 0 else 0.6)
        # drums from 3.0 s to 15.8 s
        for i in range(4):
            tt = t0 + i * beat
            if 3.0 <= tt < 15.8:
                if i in (0, 2): place(drums, kick(), tt)
                if i in (1, 3): place(drums, snap(), tt)
            for h in (0, 0.5):
                th = tt + h * beat
                if 3.0 <= th < 15.8: place(drums, hat(), th, 1.0 if h else 0.6)
    t = np.arange(n) / SR
    # arrangement: soft intro, lift at 3.0, drop drums for end card, gentle fade under sting
    pad_gain = np.interp(t, [0, 2.8, 3.2, 15.8, 18.6, 19.2, 21.5], [0.65, 0.85, 1.0, 1.0, 0.9, 0.45, 0.0])
    body_gain = np.interp(t, [0, 2.9, 3.1, 15.6, 16.2, 21.5], [0, 0, 1, 1, 0, 0])
    padL *= pad_gain; padR *= pad_gain
    mono = (plk + bs * 0.9 + drums) * body_gain
    L = reverb(padL + mono * 0.95 + plk * 0.08)
    R = reverb(padR + mono * 0.95 - plk * 0.08)
    return np.stack([L, R], 1), beat


# ------------------------------------------------------------------ events from the reel module
def events(modname):
    s = open(os.path.join(HERE, modname + ".py")).read()
    taps = sorted({round(float(m), 2) for m in re.findall(r"[\[,]\s*\[(\d+(?:\.\d+)?),\s*'[\w-]+'", s)})
    views = [float(a) for a in re.findall(r"view\('[^']+',t,([\d.]+),", s)]
    typing = [(float(a), float(b)) for a, b in re.findall(r"typeInto\([^;]*?,t,([\d.]+),([\d.]+)\)", s)]
    ho = [float(a) for a in re.findall(r"handoff\(t,([\d.]+),", s)]
    return taps, views, typing, ho


def build(modname, seed):
    bed, beat = music(seed)
    n = len(bed)
    fx = np.zeros(n)
    taps, views, typing, ho = events(modname)
    for t0 in taps:
        place(fx, sfx_tap(), t0)
    for i, v in enumerate(views):
        place(fx, sfx_whoosh(0.5 if i == 0 else 0.4), max(0, v - 0.15), 1.1 if i == 0 else 0.8)
    for a, b in typing:
        k = a
        while k < b:
            place(fx, sfx_key(), k); k += rng.uniform(0.055, 0.1)
    for h in ho:
        place(fx, sfx_chime(), h + 0.05)
    place(fx, sfx_whoosh(0.5), 15.55, 0.8)      # phone leaves
    place(fx, sfx_sting(), 18.95)                 # logo
    # hook words: tiny soft whoosh as the hook text arrives
    place(fx, sfx_whoosh(0.6), 0.3, 0.55)
    fxs = np.stack([fx, fx], 1)
    # duck the bed slightly under effects
    envfx = lp(np.abs(fx), 8) * 6
    duck = 1 - np.clip(envfx, 0, 0.25)
    mix = bed * duck[:, None] * 0.9 + fxs
    mix = reverb(mix[:, 0], 0.08)[:, None] * [1, 0] + reverb(mix[:, 1], 0.08)[:, None] * [0, 1]
    # fades and peak normalise
    t = np.arange(n) / SR
    mix *= np.interp(t, [0, 0.05, DUR - 0.6, DUR], [0, 1, 1, 0])[:, None]
    mix /= max(1e-9, np.abs(mix).max()) / 0.89
    return mix


def write_wav(path, x):
    from scipy.io import wavfile
    wavfile.write(path, SR, (np.clip(x, -1, 1) * 32767).astype(np.int16))


def main(mods):
    os.makedirs(os.path.join(HERE, "audio"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "out_audio"), exist_ok=True)
    for i, m in enumerate(mods):
        reel = importlib.import_module(m).ALL[0]
        name = reel["name"]
        seed = int(name[1:3])
        wav = os.path.join(HERE, "audio", name + ".wav")
        write_wav(wav, build(m, seed))
        vid = os.path.join(HERE, "out", name + ".mp4")
        out = os.path.join(HERE, "out_audio", name + ".mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-i", wav,
                        "-af", "loudnorm=I=-16:TP=-1.5:LRA=9",  # social-friendly loudness
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                        "-map", "0:v:0", "-map", "1:a:0", "-shortest", "-movflags", "+faststart", out], check=True)
        print("done", out)


if __name__ == "__main__":
    mods = sys.argv[1:] or sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE, "s[01][0-9]_*.py")))
    main(mods)
