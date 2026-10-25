"""Pretty QR codes for the poster run: rounded dots, rounded corner eyes in a brand colour,
and a small logo in the middle. Uses high error correction (H) so the logo doesn't stop it scanning.
Every code made with this is scan-tested before printing (see check_qr.py).

    from prettyqr import pretty_qr
    svg = pretty_qr(url, dot="#2E2A6B", ring="#2E2A6B", eye="#7B8CF5", logo=STAFFKIN_RINGS)
"""
import qrcode

# Logos for the middle of the code, drawn in a 0 0 100 100 box.
STAFFKIN_RINGS = ('<circle cx="38" cy="50" r="22" fill="none" stroke="#2E2A6B" stroke-width="9"/>'
                  '<circle cx="62" cy="50" r="22" fill="none" stroke="#7B8CF5" stroke-width="9"/>')
KEEGIX_KEY = ('<g transform="translate(4 2) scale(1.45)">'  # the Keegix mark from keegix/brand/keegix-mark.svg (64x64)
              '<path d="M20 4h24a8 8 0 0 1 8 8v30L32 60 12 42V12a8 8 0 0 1 8-8z" fill="#15304A"/>'
              '<circle cx="32" cy="17" r="6" fill="#F4C430"/>'
              '<rect x="22" y="31" width="20" height="4" rx="2" fill="#fff"/>'
              '<rect x="25" y="39" width="14" height="4" rx="2" fill="#fff"/></g>')


def pretty_qr(url, dot="#12252F", ring="#12252F", eye="#C2185B", logo=None, px=None, label="QR code"):
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_H)
    q.add_data(url)
    q.make(fit=True)
    m = q.get_matrix()
    n = len(m)

    def in_eye(x, y):
        return (x < 7 and y < 7) or (x >= n - 7 and y < 7) or (x < 7 and y >= n - 7)

    lg = int(n * 0.22) | 1  # logo hole: odd number of modules, about 22% of the width
    l0 = (n - lg) // 2

    def in_logo(x, y):
        return logo is not None and l0 - 1 <= x <= l0 + lg and l0 - 1 <= y <= l0 + lg

    dots = "".join(
        f'<rect x="{x + 0.04:.2f}" y="{y + 0.04:.2f}" width="0.92" height="0.92" rx="0.28"/>'
        for y in range(n) for x in range(n)
        if m[y][x] and not in_eye(x, y) and not in_logo(x, y))
    eyes = "".join(
        f'<rect x="{ex + 0.5}" y="{ey + 0.5}" width="6" height="6" rx="0.9" fill="none" stroke="{ring}" stroke-width="1"/>'
        f'<rect x="{ex + 2}" y="{ey + 2}" width="3" height="3" rx="0.5" fill="{eye}"/>'
        for ex, ey in ((0, 0), (n - 7, 0), (0, n - 7)))
    centre = ""
    if logo is not None:
        centre = (f'<rect x="{l0 - 0.6:.2f}" y="{l0 - 0.6:.2f}" width="{lg + 1.2:.2f}" height="{lg + 1.2:.2f}" rx="1.4" fill="#FFFFFF"/>'
                  f'<svg x="{l0}" y="{l0}" width="{lg}" height="{lg}" viewBox="0 0 100 100">{logo}</svg>')
    size = f'width="{px}" height="{px}" ' if px else 'width="100%" height="100%" '
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-2 -2 {n + 4} {n + 4}" {size}role="img" aria-label="{label}">'
            f'<rect x="-2" y="-2" width="{n + 4}" height="{n + 4}" fill="#FFFFFF"/>'
            f'<g fill="{dot}">{dots}</g>{eyes}{centre}</svg>')
