import numpy as np
from PIL import Image, ImageFilter
from rembg import remove, new_session

W = '/tmp/claude-0/-home-claude/c55a830d-2bf7-5686-8eae-0c9939c60360/scratchpad/work'
V = W + '/v2'


def hide(img, rects):
    a = np.asarray(img).astype(float).copy()
    for (x0, x1, y0, y1, c0, c1) in rects:
        prof = np.median(a[c0:c1, x0:x1, :3], axis=0)  # per-column steel profile
        h = y1 - y0
        noise = np.random.default_rng(1).normal(0, 1.2, (h, x1 - x0, 1))
        fill = np.repeat(prof[None], h, axis=0) + noise
        # feather top/bottom edges
        m = np.ones((h, 1, 1))
        f = 4
        for i in range(f):
            m[i] = m[h - 1 - i] = (i + 1) / (f + 1)
        a[y0:y1, x0:x1, :3] = a[y0:y1, x0:x1, :3] * (1 - m) + fill * m
    return Image.fromarray(np.clip(a, 0, 255).astype('uint8'), 'RGBA')


def save(img, name, box=None):
    if box:
        img = img.crop(box)
    img = img.crop(img.getbbox())
    img.save(f'{V}/p-{name}.png')
    print(name, img.size)


# studio: hide plates, then split
st = hide(Image.open(V + '/cut-studio.png').convert('RGBA'),
          [(86, 203, 964, 1097, 1098, 1113), (521, 635, 977, 1109, 1110, 1128)])
save(st, 'tall', (38, 20, 300, 1450))
sm = st.crop((282, 830, 452, 1450)).copy()
# drop the stray cable from the tall pump at the small pump's top-left
arr = np.asarray(sm).copy()
arr[:80, :30, 3] = 0
save(Image.fromarray(arr, 'RGBA'), 'short')
save(st, 'sealed', (495, 620, 680, 1445))

# older cutouts
olds = {
    'ktype': [(100, 216, 973, 1062, 1180, 1195)],
    'ssjacket': [(48, 169, 823, 922, 970, 1040)],
    'mixflow': [(137, 236, 973, 1057, 1095, 1150)],
    'trio': [(24, 118, 903, 982, 1095, 1130), (449, 553, 913, 1002, 1025, 1055)],
}
for k, r in olds.items():
    save(hide(Image.open(f'{W}/{k}.png').convert('RGBA'), r), 'old-' + k)

for k in ['blue', 'openwell']:
    save(Image.open(f'{V}/cut-{k}.png').convert('RGBA'), k)

# workshop row: left group only
s = new_session('isnet-general-use')
row = Image.open(V + '/row.png').convert('RGB').crop((160, 20, 640, 690))
save(remove(row, session=s, post_process_mask=True), 'rowleft')
