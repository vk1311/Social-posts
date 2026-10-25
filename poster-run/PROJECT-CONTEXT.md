# Physical marketing: poster run context

> **25 Oct 2026: print from [`print-pack/`](print-pack/00-PRINT-LIST.md).** Every piece was re-approved one by one ([`APPROVALS.md`](APPROVALS.md)). The weekend paper pack is retired (not used, shredded).

Start here when picking up the poster run in any chat or project. Last updated 25 Oct 2026.

## What it is

Flyers, posters and cards dropped at businesses and boards around the Annapolis Valley, for four brands on one shared route:

| Brand | Audience | QR goes to |
|---|---|---|
| Waypoint | Business owners with paperwork pain (trades, rentals, offices) | waypointns.ca |
| Waypoint Apps | Makers, market sellers, side hustles | app.waypointns.ca |
| Staffkin | Small employers who hire (restaurants, shops, bookkeepers) | staffkin.com |
| Keegix | Short-term rental hosts (B&Bs, cottages, inns) | keegix.com |

Every design and every Keegix spot has its own QR tag, so scans show which piece and which place brought someone in. The tags are listed in `README.md`.

## Where everything lives (`poster-run/`)

| What | File |
|---|---|
| Brand print files | `waypoint-flyers-print.pdf`, `staffkin-flyers-print.pdf`, `keegix/1-print-final/` |
| Each brand's own stop list | `waypoint-flyer-run.xlsx`, `staffkin-flyer-stops.xlsx`, `keegix/2-lists/keegix-dropoff-spots-valley.xlsx` |
| **All 4 brands merged into one route** | `run-kit/poster-run-master-route.xlsx` (131 places in 7 outings, Mail from home tab) |
| **One print list for everything** | `run-kit/poster-run-print-list.xlsx` (what to print, pack by route, Keegix page-to-spot) |
| Route maps (routes 1–4) | `run-kit/route-maps/` |
| Weekend paper pack (posters and flyers only, routes 2–4, 31 pages) | `run-kit/weekend-paper-pack-routes-2-4.pdf` |
| Route app (Uber-style, one stop at a time) | https://poster-run-driver.netlify.app — source in `run-kit/driver-app/` |
| Editable design sources | `source/`, `source/staffkin/`, `keegix/4-source/` |

## The routes

All routes start and end in Waterville (starting in Kentville just skips the first and last stretch). Stop numbers are the same on the maps, the master route sheet and the app.

| Outing | When | Stops |
|---|---|---|
| 1 · Weekday daytime | Mon–Fri about 9–4 (offices, accountants, trades) | 25 |
| 2 · Wolfville & Grand Pré | Saturday, at the farmers' market by 8:30 | 25 |
| 3 · Kentville & Coldbrook | Weekend; restaurants 2–4 pm | 21 |
| 4 · New Minas | Any evening or weekend | 22 |
| 5 · West (Annapolis Royal → Canning) | A Saturday | 21 |
| 5b · Hantsport & Windsor | Add-on, low priority | 3 |
| 6 · Seasonal / odd hours | Kentville market (Wed), craft fairs | 4 |
| Mail from home | 30 Keegix letters + 4 Staffkin postcards | 34 |

Maps exist for routes 1–4 only. The app covers routes 1–4.

**Route app:** "Hands-free in the car" buttons load up to 10 stops into Google Maps, which shows on Android Auto. Each stop card shows what to leave per brand and what to say; tap Left it / Said no / Closed, then Next stop. On Netlify, progress saves on each phone separately. The Claude-hosted copy saves to Vatsal's account.

## Printing

- Printed at work (employer's printer, colour), on Vatsal's own paper and Pen+Gear 65 lb white cardstock. Home printer is a Brother DCP-L2550DW (black and white only).
- Full run after the paper-saving changes (22 Oct): **154 sheets of cardstock + 93 of copy paper**. Routes 1–4 alone need about 113 cardstock sheets, so one 100-sheet pack is not enough.
- Print at 100% / "Actual size". Two-sided cards: print the fronts, put the stack back, print the backs, flip on the long edge. Cut on the front's dashed lines (backs have no cut lines). Keegix key cards are tag-shaped: straight cuts, then scissors.
- Cutter: the one in the shared mailroom at work.

## Decisions so far

- One route for all four brands, so each place is visited once.
- Waypoint flyer B "Still doing it by hand?" at trades counters, A at the coworking space. Apps poster B at farm and farmers' markets, A (tear-off) everywhere else.
- Counter cards (Waypoint C and Staffkin A) changed to quarter-letter, 4 per sheet, two-sided, to save cardstock. Staffkin board poster on paper.
- Keegix: yellow key cards (option A) + Airbnb house-rules flyer (option 4) until Nov 20, then the tear-off flyer (option 3) for the same 21 spots. Unused options are in `keegix/old-versions/v3-unused-options/`.
- Care homes, home-care agencies and national chains are left off the Staffkin list on purpose.
- First outing: weekend of 24–25 Oct with the paper-only pack (posters and flyers, no cards).

## Open items

- Print the cardstock run (counter cards, take-one cards, pocket cards, Keegix key cards). Needs a second cardstock pack for everything.
- Route 1 needs weekday daytime (a half day off or lunch hours).
- No maps or app routes yet for the west run, Hantsport/Windsor and the seasonal stops.
- Van Meekeren Farms (237 Thorpe Rd, Kentville) has no map location; Google Maps finds it by address.
- Optional: connect the Netlify app to Supabase so both phones share progress.
- Switch Keegix flyers to option 3 after Nov 20.
- Re-post in the first week of each month (boards get cleared every 2–4 weeks).
- Record scans per QR tag (Keegix tracker: Google Sheet "Keegix print tracker (mail + public spots)").
