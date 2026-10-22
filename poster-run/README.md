# Poster run (Oct 2026)

Flyers, counter cards and the stop list for putting Waypoint and Waypoint Apps up around the Annapolis Valley.

## What's here

| File | What it is |
|---|---|
| `waypoint-flyer-run.xlsx` | 61 stops. Tabs: Waypoint (28), Waypoint Apps (41), All stops in driving order (for the route), Print list |
| `waypoint-flyers-print.pdf` | All six designs, one per Letter page, ready to print |
| `png/` | The same six designs as images |
| `source/` | Editable sources: the six designs (`project/*.dc.html`) and the scripts that make them |

## The six designs

| | Waypoint (business owners) | Waypoint Apps (sellers, side hustles) |
|---|---|---|
| A | "I make the software fit your business." Light | "Digitize your whole business." Light, with tear-offs |
| B | "Still doing it by hand?" Dark | "Selling at markets or online?" Dark |
| C | Counter cards, 2 per sheet (cut in half) | Take-one cards, 4 per sheet (cut on the dashed lines) |

## QR codes

Each design has its own tag, so you can see which one brings people in:

| Design | Link |
|---|---|
| Waypoint A | `waypointns.ca/?src=flyer-fit` |
| Waypoint B | `waypointns.ca/?src=flyer-byhand` |
| Waypoint C | `waypointns.ca/?src=card` |
| Apps A | `app.waypointns.ca/?src=poster-whole` |
| Apps B | `app.waypointns.ca/?src=poster-market` |
| Apps C | `app.waypointns.ca/?src=card` |

## Printing

- Cardstock for the counter and take-one cards. Plain paper for Apps A, so the tear-offs tear.
- The two dark designs use a lot of ink and get a white edge on a home printer.
- Ask before posting anywhere. Boards get cleared every 2–4 weeks, so re-post on the 1st of each month.

## Changing a design

Edit the text in `source/gen_print.py`, then run `python3 gen_print.py` in `source/`. It rewrites the six files in `source/project/`. `build_xlsx.py` rebuilds the stop list the same way.

Look: the "lining" style from the Waypoint posts (chart grid, two bearing lines, coordinates at the top, magenta bar under the headline, full mark bottom-left, URL bottom-right). Manrope + DM Sans, chart palette. Prices carry CAD. Addresses and hours are from Google Maps, Oct 2026.
