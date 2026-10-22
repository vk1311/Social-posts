# Poster run (Oct 2026)

Flyers, counter cards and the stop list for putting Waypoint and Waypoint Apps up around the Annapolis Valley. Printed in colour on the office printer, on Pen+Gear 65 lb white cardstock and regular copy paper.

## What's here

| File | What it is |
|---|---|
| `waypoint-flyer-run.xlsx` | 61 stops. Tabs: Waypoint (28), Waypoint Apps (41), All stops in driving order (for the route), Print list (sheet counts by paper type) |
| `waypoint-flyers-print.pdf` | 7 Letter pages, ready to print at actual size (100%). Page list below |
| `png/1`–`png/6` | The same pages as images (`3a` = counter card fronts, `3b` = backs) |
| `source/` | Editable sources: the designs (`project/*.dc.html`), `gen_print.py` (designs), `build_pdf.py` (PDF and images), `build_xlsx.py` (stop list) |

## What to print, and on what

| PDF page | Design | Paper | Sides | Per sheet |
|---|---|---|---|---|
| 1 | Waypoint A: "I make the software fit your business." Light | Copy paper | One | 1 |
| 2 | Waypoint B: "Still doing it by hand?" Dark | Copy paper | One | 1 |
| 3 + 4 | Waypoint C: counter cards, 4.25 × 5.5 in. Page 3 = fronts, page 4 = backs | Cardstock | **Two, flip on long edge** | 4 |
| 5 | Apps A: "Digitize your whole business." Light, with tear-offs | Copy paper (so the tabs tear) | One | 1 |
| 6 | Apps B: "Selling at markets or online?" Dark | Copy paper | One | 1 |
| 7 | Apps C: take-one cards | Cardstock | One | 4 |

At the default amounts (Print list tab): **81 sheets of cardstock** (39 counter cards + 42 Apps cards) and **33 sheets of copy paper** (12 Waypoint flyers including 2 spares, 21 Apps posters).

Counter card front: headline, QR code, "Call or text Vatsal 902-670-9297", in the lining style on a white background. Back: "Built around the way your shop already runs.", the four bullets, the price and waypointns.ca, in dark text on white only, so it prints fine in black and white too. Everything sits at least 0.375 in inside each card, clear of the printer's unprintable edge and the cut lines.

## How to print two-sided (counter cards)

1. Load the cardstock. If the printer has a paper type setting, pick Cardstock or Heavy.
2. Open `waypoint-flyers-print.pdf` and choose Print.
3. Pages: `3-4`. Size: **Actual size** (100%), not "Fit". Colour: on.
4. Two-sided: **Print on both sides, flip on long edge** (sometimes called "long-edge binding").
5. Print **1 copy first**. Hold it up to a window: each back should sit inside the dashed lines on the front. Then print the rest (39 copies at the default amounts).
6. Cut on the dashed lines: one cut down the middle, one across, 4 cards per sheet.

If the printer won't print both sides on cardstock (some only take heavy paper one side at a time from the side tray):

1. Print page 3 only, 1 copy.
2. Put that sheet back in the same tray, turned over side to side, with the same edge going in first.
3. Print page 4 only.
4. If the back comes out upside down, turn the sheet the other way next time. Once the test sheet is right, print all the fronts, then feed the stack back the same way for the backs.

## QR codes

Each design has its own tag, so you can see which one brings people in. All 12 codes in the PDF were scanned (also in black and white) and each opens its link.

| Design | Link |
|---|---|
| Waypoint A | `waypointns.ca/?src=flyer-fit` |
| Waypoint B | `waypointns.ca/?src=flyer-byhand` |
| Waypoint C | `waypointns.ca/?src=card` |
| Apps A | `app.waypointns.ca/?src=poster-whole` |
| Apps B | `app.waypointns.ca/?src=poster-market` |
| Apps C | `app.waypointns.ca/?src=card` |

## Posting

- The two dark designs (pages 2 and 6) use a lot of ink and get a white border, because the printer can't print to the edge.
- Ask before posting anywhere. Boards get cleared every 2–4 weeks, so re-post on the 1st of each month.

## Changing a design

In `source/`: edit the text in `gen_print.py` and run `python3 gen_print.py` (rewrites `project/`), then `python3 build_pdf.py` (rewrites the PDF and `png/`). `python3 build_xlsx.py` rebuilds the stop list. The old one-sided, 2-per-sheet counter card is in the git history (before 22 Oct 2026).

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

This run uses card option A (yellow key cards) and flyer option 4 (Airbnb house rules, timely until Nov 20). After Nov 20, flyer option 3 (tear-off) replaces it for the same spots.

| Folder | What it is |
|---|---|
| `keegix/1-print-final/` | What to print: `10-CARD-option-A-keycards-37-spots.pdf`, `23-FLYER-option-4-airbnb-rules-21-spots.pdf`, the 30 window-envelope letters with numbered mail key cards, the key card backs, and flyer 3 (tear-off) for after Nov 20. `00-READ-ME-printing.txt` has the full page-to-spot lists |
| `keegix/2-lists/` | `keegix-dropoff-spots-valley.xlsx`: 41 drop-off spots west to east (cafés, hardware, furniture, markets, libraries, visitor centre, realtors), with hours, map links, who gets cards and a flyer, and the PDF page for each spot. `mail-30.csv` and `mail-backup-20.csv` for the letters |
| `keegix/3-qr-codes/` | All 8 keegix.com QR sign styles |
| `keegix/4-source/` | Scripts, fonts and data to rebuild any piece |
| `keegix/old-versions/` | Earlier drafts, plus card option B and flyer options 1 and 2 in `v3-unused-options/`. Don't print |

**Who gets what** (from "What to leave" in the spreadsheet):

- Key cards: 37 spots, spots 1–10, 12–15, 17–18, 20–33, 35–41. Pages 1–37 of the key card PDF are those spots in that order.
- Flyer: 21 spots, spots 1, 2, 4, 6, 7, 8, 11, 13, 14, 16, 19, 24, 25, 28, 29, 30, 31, 34, 39, 40, 41. Pages 1–21 of the flyer 4 PDF are those spots in that order.
- Flyer only, no key cards: 11 Berwick and District Library, 16 Kentville Library, 19 Maytag Coin Laundry, 34 Wolfville Memorial Library.

**Sheets** (colour, office printer, 100% / Actual size):

| Stock | What | Sheets |
|---|---|---|
| Cardstock (Pen+Gear 65 lb white) | Spot key cards (9 per sheet) | 37 |
| | Mail key cards (30 cards) | 4 |
| | Key card backs (`03-keycards-BACK.pdf`, 41 copies on the reverse) | 0 extra |
| | **Total cardstock** | **41** |
| Copy paper | Flyer 4 | 21 |
| | Mail letters | 30 |
| | **Total copy paper** | **51** |
| Later | Flyer 3 tear-off after Nov 20 (print only the 21 flyer spots' pages; page = spot number) | 21 copy paper |

QR codes: every piece has its own code. Letters `keegix.com/demo?src=m01`–`m30`, cards left at a spot `src=c01`–`c41`, flyers at a spot `src=l01`–`l41` (flyer 4 opens `keegix.com/airbnb-house-rules?src=l##`). Each page prints its page number, spot number, spot name and code small at the bottom. Scans and sign-ups go in the Google Sheet "Keegix print tracker (mail + public spots)".

The Keegix stops can be merged into the "All stops in driving order" tab of `waypoint-flyer-run.xlsx` for one route.
