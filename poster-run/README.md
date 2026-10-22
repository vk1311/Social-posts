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

---

# Staffkin (added 21 Oct 2026, card A made smaller 22 Oct)

Flyers, cards and a stop list for Staffkin around Kentville, New Minas, Coldbrook, Wolfville and Grand Pré.

## Files

| File | What it is |
|---|---|
| `staffkin-flyer-stops.xlsx` | 59 stops plus 20 businesses hiring right now (Job Bank and Indeed, 21 Oct). Same columns as the Waypoint route tab, so the rows paste straight under it. 20 stops share an address with the Waypoint list (marked "Also on Waypoint list"), so one visit covers both. Tabs: Staffkin stops, Hiring now, Print count, How to use |
| `staffkin-flyers-print.pdf` | 6 Letter pages, print at actual size (100%). Pages 1–5 on 65 lb cardstock, page 6 on plain copy paper (see Printing below) |
| `png/7a`, `png/7b`, `png/8`–`png/11` | The same pages as images |
| `source/staffkin/` | Editable sources (`project/*.dc.html`), logo, QR codes, Outfit font, and `render.py` |

## The four options

| | What | Per sheet | Where it goes |
|---|---|---|---|
| A | Counter card, quarter-letter (4.25 × 5.5 in), two-sided. Front: logo, "Hiring this month?", QR, "Your first job is free. No card needed." Back (dark text on white, fine in black and white): what it does, "Data stored in Canada.", staffkin.com, contact@staffkin.com | 4 (page 1 = front, page 2 = back) | Restaurants, cafés, bookkeepers, wineries, shops with a hiring sign |
| B | Reference-check postcard: "$9 CAD a check" (page 3 = front, page 4 = address side) | 4 | Mail to businesses that are hiring; print page 4 on the back, flip on the long edge |
| C | Board poster: "Hire people, not paperwork." Plain copy paper | 1 | Chamber office, libraries, print shops |
| D | Pocket card: "Hiring? Your first job is free." | 10 | Trades counters, salons, garages, shops |

## QR codes

| Option | Link |
|---|---|
| A | `staffkin.com/?utm_source=counter-card` |
| B | `staffkin.com/app/?utm_source=ref-postcard#/signup?intent=refs` (opens the $9 reference-check signup) |
| C | `staffkin.com/?utm_source=board-poster` |
| D | `staffkin.com/?utm_source=pocket-card` |

Every code was scanned card by card from the print PDF (22 Oct) and opens the right link.

## Printing (office colour printer, Pen+Gear 65 lb white cardstock + copy paper)

| Stock | PDF pages | Sheets (from the Print count tab) |
|---|---|---|
| 65 lb cardstock | 1–2 card A (two-sided), 3–4 postcard B (two-sided), 5 pocket cards D | A 21 + B 3 + D 8 = **32** |
| Plain copy paper | 6 board poster C | **9** |

- Print at actual size (100%), not "fit to page".
- Two-sided A and B: print the front page, put the printed stack back in the tray, then print the back page, flipping on the long edge. Or use the printer's two-sided setting with "flip on long edge" if it takes cardstock. Run one test sheet first and hold it to the light.
- Checked 22 Oct: with the back flipped on the long edge, every back sits inside its front's card with at least 0.46 in (A) and 0.41 in (B) to spare, so a small printer shift won't push text onto the wrong card.
- Cut on the dashed lines on the front.

## Design rules followed

- Real brand files only: the two-ring logo from `staffkin/brand/`, Indigo/Periwinkle/Paper/Ink, Outfit.
- Readability first: white stock, dark text, rings in the corner at low opacity on C, no photos (so nothing AI-made and no heavy ink). Card A has nothing running to the edge, so a slightly off cut doesn't show.
- No stats, testimonials or time-saved claims. Facts only: 70 job description templates, 357 interview questions, $9 CAD reference checks, data stored in Canada, AI only drafts questions.
- Contact is contact@staffkin.com. No day-job mention anywhere.
- No street address on the postcard: return line is "Staffkin · Kentville, Nova Scotia".

## Left off the stop list on purpose

- Care homes and home-care agencies (same sector as the day job).
- National chains: head office decides.

## Keegix (`keegix/`)

Mail letters, key cards and flyers for Keegix hosts (B&Bs, inns, cottages) around the Valley and Cape Breton. Start with `keegix/00-START-HERE.txt`.

| Folder | What it is |
|---|---|
| `keegix/1-print-final/` | The print set: 30 window-envelope letters with numbered key cards, card options A (yellow key cards) and B (business cards), flyer options 1 poster, 2 table tent, 3 tear-off, 4 Airbnb house rules. One page per spot (page number = spot number). `00-OPTIONS-overview.png` shows them all |
| `keegix/2-lists/` | `keegix-dropoff-spots-valley.xlsx`: 41 drop-off spots west to east (cafés, hardware, furniture, markets, libraries, visitor centre, realtors), with hours and map links. `mail-30.csv` and `mail-backup-20.csv` for the letters |
| `keegix/3-qr-codes/` | All 8 keegix.com QR sign styles |
| `keegix/4-source/` | Scripts, fonts and data to rebuild any piece |
| `keegix/old-versions/` | Earlier drafts. Don't print |

QR codes: every piece has its own code. Letters `keegix.com/demo?src=m01`–`m30`, cards left at a spot `src=c01`–`c41`, flyers at a spot `src=l01`–`l41` (flyer 4 opens `keegix.com/airbnb-house-rules?src=l##`). Scans and sign-ups go in the Google Sheet "Keegix print tracker (mail + public spots)".

The Keegix stops can be merged into the "All stops in driving order" tab of `waypoint-flyer-run.xlsx` for one route.
