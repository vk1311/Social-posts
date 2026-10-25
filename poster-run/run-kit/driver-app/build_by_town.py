"""Rebuild the Poster Run Driver app grouped by TOWN, then TYPE of place (25 Oct 2026).
All 131 in-person places from poster-run-master-route.xlsx (every outing, incl. West, Hantsport/Windsor, seasonal).
Inside a town + type, stops follow the shortest path we can work out from known map points
(nearest next stop), otherwise the master route's driving order. Same address = one stop.

Usage: python3 build_by_town.py <app.html in> <app.html out>
"""
import json, math, re, sys, os, html
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(os.path.dirname(HERE), "poster-run-master-route.xlsx")

TYPES = [  # (key, label) in the order they show
    ("cafes", "Cafés & bakeries"),
    ("food", "Restaurants & pubs"),
    ("trades", "Trades & hardware"),
    ("offices", "Offices"),
    ("print", "Print & shipping"),
    ("boards", "Community boards"),
    ("markets", "Markets & farms"),
    ("shops", "Shops & services"),
]
TYPE_OF = {}  # master route # -> type key
for k, nums in {
    "offices": [1, 2, 5, 9, 11, 12, 13, 14, 15, 19, 20, 21, 25, 43, 54],
    "trades": [3, 4, 7, 16, 17, 22, 26, 27, 28, 31, 67, 71, 76, 78, 81, 98, 99, 100, 103, 104, 111, 114, 117, 122],
    "print": [10, 23, 24, 89, 91],
    "boards": [6, 8, 36, 39, 40, 62, 63, 70, 72, 108, 115, 118, 120, 126],
    "cafes": [35, 42, 45, 48, 59, 66, 68, 74, 106, 107, 109, 112, 116, 119, 121, 123, 124, 127, 130],
    "food": [32, 33, 38, 41, 47, 50, 52, 60, 64, 65, 69, 77, 79, 80, 84, 86, 95, 97, 102, 125, 128],
    "markets": [18, 29, 30, 37, 56, 57, 58, 110, 129, 131],
    "shops": [34, 44, 46, 49, 51, 53, 55, 61, 73, 75, 82, 83, 85, 87, 88, 90, 92, 93, 94, 96, 101, 105, 113],
}.items():
    for n in nums:
        assert n not in TYPE_OF, n
        TYPE_OF[n] = k
TOWNS = ["Kentville", "New Minas", "Wolfville", "Coldbrook", "Greenwich", "Grand Pré", "Hortonville",
         "Annapolis Royal", "Middleton", "Kingston", "Aylesford", "Berwick", "Cambridge", "Woodville",
         "Centreville", "Canning", "Hantsport", "Falmouth", "Windsor", "Valley-wide"]

src_html = open(sys.argv[1], encoding="utf-8").read()
old = json.loads(re.search(r'<script id="routes" type="application/json">(.*?)</script>', src_html, re.S).group(1))
LL = {}
for r in old:
    for s in r["stops"]:
        for p in s["places"]:
            if s.get("ll"):
                LL[p["name"].lower()] = s["ll"]

ws = openpyxl.load_workbook(MASTER, data_only=True)["Master route"]
rows = [r for r in ws.iter_rows(min_row=5, values_only=True) if isinstance(r[0], int)]
assert len(rows) == 131 and set(TYPE_OF) == set(range(1, 132)), (len(rows), set(range(1, 132)) - set(TYPE_OF))

def norm(name):  # names differ slightly between files ("T.A.N. Coffee Wolfville" vs "T.A.N. Coffee - Wolfville")
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()
LLN = {norm(k): v for k, v in LL.items()}

places = []
for r in rows:
    n, outing, town, name, addr, hours, prio = r[0], r[1], r[2], r[3], r[4], r[5], r[6]
    leave = {k: v for k, v in zip("WASK", r[8:12]) if v}
    places.append(dict(n=n, town=town, type=TYPE_OF[n], name=name, addr=addr or town + ", NS",
                       hours=hours, prio=int(prio) if prio else 2, leave=leave, say=r[12], note=r[13],
                       ll=LLN.get(norm(name))))
assert set(p["town"] for p in places) <= set(TOWNS), set(p["town"] for p in places) - set(TOWNS)

def km(a, b):
    dy = (a[0] - b[0]) * 111.0
    dx = (a[1] - b[1]) * 111.0 * math.cos(math.radians(a[0]))
    return math.hypot(dx, dy)

HOME = (45.0517, -64.6539)  # Waterville, where every run starts

def order_stops(ps):
    stops = []  # same address -> one stop
    for p in ps:
        key = re.sub(r"\W+", "", (p["addr"] or "").lower().split(",")[0])
        hit = next((s for s in stops if s["key"] == key and key), None)
        if hit:
            hit["places"].append(p)
        else:
            stops.append({"key": key, "places": [p], "ll": p["ll"]})
    # stops with a map point: nearest next stop, starting from the one closest to Waterville.
    # stops without one keep the master route order and go last.
    known = [s for s in stops if s["ll"]]; unknown = [s for s in stops if not s["ll"]]
    order, here = [], HOME
    while known:
        nxt = min(known, key=lambda s: km(here, s["ll"]))
        known.remove(nxt); order.append(nxt); here = nxt["ll"]
    return order + unknown

def pack(town, key, label, stops):
    out = []
    for i, s in enumerate(stops, 1):
        out.append({"id": f"{town}-{key}-{i}", "n": i, "ll": s["ll"], "town": town,
                    "places": [{k: p[k] for k in ("name", "addr", "hours", "prio", "leave", "say", "note")} for p in s["places"]],
                    "move": {"mode": "drive", "m": None, "min": None}, "walk": None})
    return {"id": re.sub(r"\W+", "-", (town + "-" + key).lower()), "town": town, "type": key,
            "title": town + (" · " + label if key != "all" else ""), "typeLabel": label, "stops": out}

groups = []
for town in TOWNS:
    tps = [p for p in places if p["town"] == town]
    tg = []
    for tkey, tlabel in TYPES:
        ps = [p for p in tps if p["type"] == tkey]
        if ps:
            tg.append(pack(town, tkey, tlabel, order_stops(ps)))
    if len(tg) > 1:  # "All" first: every place in town in one drive
        groups.append(pack(town, "all", "All", order_stops(tps)))
    groups.extend(tg)

total = sum(len(s["places"]) for g in groups if g["type"] != "all" for s in g["stops"])
assert total == 131, total
data = json.dumps(groups, ensure_ascii=False).replace("</", "<\\/")
out_html = re.sub(r'(<script id="routes" type="application/json">)(.*?)(</script>)',
                  lambda m: m.group(1) + data + m.group(3), src_html, count=1, flags=re.S)
open(sys.argv[2], "w", encoding="utf-8").write(out_html)
print(len(groups), "town/type groups,", sum(len(g["stops"]) for g in groups), "stops,", total, "places")
