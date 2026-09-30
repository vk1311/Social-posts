#!/usr/bin/env python3
"""Waypoint social card renderer — October set.

Brand locked: ink #12252F, slate #2F4A56, off-white #F7F7F4,
mist #7E96A2, magenta #C2185B. Manrope headings / DM Sans body.
Full layered mark at every size (two-size rule revoked).
"""
from PIL import Image, ImageDraw, ImageFont
import os

INK     = (0x12, 0x25, 0x2F)
SLATE   = (0x2F, 0x4A, 0x56)
PAPER   = (0xF7, 0xF7, 0xF4)
MIST    = (0x7E, 0x96, 0xA2)
MAGENTA = (0xC2, 0x18, 0x5B)

MANROPE = "/home/claude/fonts/Manrope.ttf"
DMSANS  = "/home/claude/fonts/DMSans.ttf"

_cache = {}
def font(path, size, weight):
    key = (path, size, weight)
    if key not in _cache:
        f = ImageFont.truetype(path, size)
        f.set_variation_by_name(weight)
        _cache[key] = f
    return _cache[key]

def head(size, weight="ExtraBold"): return font(MANROPE, size, weight)
def body(size, weight="Regular"):   return font(DMSANS, size, weight)

# ---------------------------------------------------------------- mark
SURVEY = [(55.10,107.56,43.43,24.59),(30.73,34.51,108.42,65.90),
          (106.17,49.93,40.15,101.52),(64.00,9.44,64.00,114.84)]
SLIVERS = [[(70.20,62.14),(70.20,65.86),(118.56,64.00)],
           [(57.80,62.14),(57.80,65.86),(9.44,64.00)]]
BEARINGS = [(46.40,74.15,59.70,51.10),(81.60,74.15,68.30,51.10)]
TRI   = [(64.00,37.96),(86.55,77.02),(41.45,77.02)]
VERTS = TRI
CENTRE = (64.00,64.00)

def draw_mark(img, x, y, size, scheme="on_dark", box=(22, 18, 84, 84),
              weights=(1.9, 3.2, 6.2, 4.4, 5.6)):
    """Full layered mark, supersampled 4x, pasted with its top-left at x,y.

    box crops the 128-unit space (tight crop keeps the triangle dominant at
    small sizes); weights thicken strokes instead of dropping elements.
    """
    S = 4
    n = size * S
    m = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(m)
    bx, by, bw_, bh_ = box
    k = n / float(bw_)
    def P(px, py): return ((px - bx) * k, (py - by) * k)
    if scheme == "on_magenta":
        survey, tri, dot = (0xE2, 0x7C, 0xA3), PAPER, INK
    elif scheme == "on_dark":
        survey, tri, dot = SLATE, PAPER, MAGENTA
    else:
        survey, tri, dot = MIST, INK, MAGENTA
    ws, wb, wt, dr, cr = weights
    sw = max(1, int(ws * k)); bw = max(1, int(wb * k)); tw = max(2, int(wt * k))
    for x1, y1, x2, y2 in SURVEY:
        d.line([P(x1, y1), P(x2, y2)], fill=survey, width=sw)
    for poly in SLIVERS:
        d.polygon([P(px, py) for px, py in poly], fill=survey)
    for x1, y1, x2, y2 in BEARINGS:
        d.line([P(x1, y1), P(x2, y2)], fill=dot, width=bw)
    d.line([P(px, py) for px, py in TRI] + [P(*TRI[0])],
           fill=tri, width=tw, joint="curve")
    r = dr * k
    for cx, cy in VERTS:
        ux, uy = P(cx, cy)
        d.ellipse([ux-r, uy-r, ux+r, uy+r], fill=dot)
    rc = cr * k
    ux, uy = P(*CENTRE)
    d.ellipse([ux-rc, uy-rc, ux+rc, uy+rc], fill=dot)
    m = m.resize((size, size), Image.LANCZOS)
    img.paste(m, (int(x), int(y)), m)


# ---------------------------------------------------------------- backdrop
def backdrop(img, variant, scale=1.0):
    """Chart-paper backdrop: faint graticule, survey diagonals, and one large
    30%-alpha square in the contrasting colour so the card reads slightly filled."""
    W, H = img.size
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    if variant == "ink":
        grid, sq, tick = MIST + (26,), MIST + (77,), MAGENTA + (150,)
    else:
        grid, sq, tick = SLATE + (26,), SLATE + (48,), MAGENTA + (150,)

    step = int(90 * scale)
    lw = max(1, int(1 * scale))
    for x in range(step, W, step):
        d.line([x, 0, x, H], fill=grid, width=lw)
    for y in range(step, H, step):
        d.line([0, y, W, y], fill=grid, width=lw)

    # survey diagonals across the whole field
    d.line([-40, int(H * 0.30), W + 40, int(H * 0.62)], fill=grid, width=max(1, int(2*scale)))
    d.line([int(W * 0.18), -40, int(W * 0.74), H + 40], fill=grid, width=max(1, int(2*scale)))

    img.paste(Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB"), (0, 0))

# ---------------------------------------------------------------- text
def tracked(d, xy, text, f, fill, track):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + track
    return x

def tracked_w(d, text, f, track):
    return sum(d.textlength(c, font=f) for c in text) + track * max(0, len(text) - 1)

def wrap(d, text, f, width):
    out, line = [], ""
    for word in text.split():
        t = (line + " " + word).strip()
        if d.textlength(t, font=f) <= width or not line:
            line = t
        else:
            out.append(line); line = word
    if line: out.append(line)
    return out

# ---------------------------------------------------------------- card
def card(path, blocks, variant="ink", size=(1080, 1350), footer=True,
         slide=None, scale=1.0):
    W, H = size
    if variant == "ink":
        bg, fg, sub, accent, scheme = INK, PAPER, MIST, MAGENTA, "on_dark"
    elif variant == "paper":
        bg, fg, sub, accent, scheme = PAPER, INK, SLATE, MAGENTA, "on_light"
    else:
        raise ValueError("magenta backgrounds are retired: use ink or paper")

    img = Image.new("RGB", (W, H), bg)
    backdrop(img, variant, scale)
    d = ImageDraw.Draw(img)
    M = int(90 * scale)
    CW = W - 2 * M

    F = {
        "kicker": body(int(26*scale), "Medium"),
        "hook":   head(int(76*scale)),
        "big":    head(int(58*scale), "Bold"),
        "body":   body(int(37*scale)),
        "bodym":  body(int(37*scale), "Medium"),
        "kvval":  head(int(52*scale), "Bold"),
        "num":    head(int(34*scale), "Bold"),
        "foot":   body(int(24*scale), "Medium"),
    }
    LH = {"hook": 1.10, "big": 1.18, "body": 1.52}

    # ---- measure
    def measure(blocks):
        h = 0
        for kind, val in blocks:
            if kind == "kicker":
                h += int(F["kicker"].size * 1.2) + int(30 * scale)
            elif kind in ("hook", "big"):
                lines = wrap(d, val, F[kind], CW)
                h += int(len(lines) * F[kind].size * LH[kind]) + int(26 * scale)
            elif kind == "body":
                lines = wrap(d, val, F["body"], CW)
                h += int(len(lines) * F["body"].size * LH["body"]) + int(26 * scale)
            elif kind == "rule":
                h += int(52 * scale)
            elif kind == "gap":
                h += int(val * scale)
            elif kind == "check":
                h += len(val) * int(F["body"].size * 1.95) + int(20 * scale)
            elif kind == "kv":
                for lab, v in val:
                    h += int(F["kicker"].size * 1.5) + \
                         len(wrap(d, v, F["kvval"], CW)) * int(F["kvval"].size * 1.24) + \
                         int(48 * scale)
        return h

    total = measure(blocks)
    y = max(int(150 * scale), (H - total) // 2 - int(40 * scale))

    # ---- draw
    for kind, val in blocks:
        if kind == "kicker":
            tracked(d, (M, y), val.upper(), F["kicker"], accent if variant != "magenta" else sub,
                    F["kicker"].size * 0.22)
            y += int(F["kicker"].size * 1.2) + int(30 * scale)
        elif kind in ("hook", "big"):
            f = F[kind]
            for ln in wrap(d, val, f, CW):
                d.text((M, y), ln, font=f, fill=fg)
                y += int(f.size * LH[kind])
            y += int(26 * scale)
        elif kind == "body":
            f = F["body"]
            for ln in wrap(d, val, f, CW):
                d.text((M, y), ln, font=f, fill=sub)
                y += int(f.size * LH["body"])
            y += int(26 * scale)
        elif kind == "rule":
            th = int(12 * scale)
            d.rectangle([M, y, M + int(190 * scale), y + th], fill=accent)
            y += int(52 * scale)
        elif kind == "gap":
            y += int(val * scale)
        elif kind == "check":
            f = F["bodym"]; bs = int(f.size * 1.08)
            for ticked, txt in val:
                by = y + int(f.size * 0.24)
                d.rectangle([M, by, M + bs, by + bs], outline=sub, width=max(2, int(3*scale)))
                if ticked:
                    d.line([M + bs*0.24, by + bs*0.50, M + bs*0.44, by + bs*0.72],
                           fill=accent, width=max(4, int(7*scale)))
                    d.line([M + bs*0.44, by + bs*0.72, M + bs*0.78, by + bs*0.26],
                           fill=accent, width=max(4, int(7*scale)))
                d.text((M + bs + int(34*scale), y), txt, font=f,
                       fill=fg if ticked else sub)
                y += int(f.size * 1.95)
            y += int(20 * scale)
        elif kind == "kv":
            for lab, v in val:
                tracked(d, (M, y), lab.upper(), F["kicker"], accent,
                        F["kicker"].size * 0.22)
                y += int(F["kicker"].size * 1.5)
                for ln in wrap(d, v, F["kvval"], CW):
                    d.text((M, y), ln, font=F["kvval"], fill=fg)
                    y += int(F["kvval"].size * 1.24)
                y += int(48 * scale)

    # ---- furniture
    coord = "45.0774\u00b0 N  64.4956\u00b0 W"
    tracked(d, (M, int(86 * scale)), coord, F["foot"], sub, F["foot"].size * 0.16)

    if slide:
        n, tot = slide
        txt = f"{n}/{tot}"
        w = d.textlength(txt, font=F["num"])
        d.text((W - M - w, int(86 * scale)), txt, font=F["num"], fill=sub)
    if footer:
        ms = int(92 * scale)
        fy = H - M - ms
        if H >= 1600:            # Reel: clear Instagram's bottom UI zone
            fy = H - int(430 * scale) - ms
        draw_mark(img, M, fy, ms, scheme)
        ft = "waypointns.ca"
        tw = tracked_w(d, ft, F["foot"], F["foot"].size * 0.12)
        tracked(d, (W - M - tw, fy + ms * 0.35), ft, F["foot"],
                fg, F["foot"].size * 0.12)
    img.save(path, "PNG")
    return path
