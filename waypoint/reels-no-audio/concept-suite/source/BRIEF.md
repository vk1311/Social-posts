# Brief: Waypoint concept-suite reels (one per app)

## What this is
A series of vertical 9:16 (1080×1920, 30 fps, 21.5 s) UI/UX demo videos for Waypoint's social channels
(Reels, Shorts, TikTok). They show a CONCEPT integrated business suite (like Zoho/Odoo) that Waypoint
would custom-build for a client. The software does NOT exist; the framing is "here's what a system
built around your process looks like". Every frame carries the "Concept demo · made-up data" badge
(already in the shell — don't remove it).

The invented client is **Harlow & Pine Property Services**, a Kentville, NS snow/landscaping/property
company. Its system has 12 apps (see `APPS` in suite.py). The series' main idea: they're one system —
**every reel ends with a hand-off to another app** (use `toast()` + `handoff()`).

## Files (in /home/claude/suite-reels — read these first)
- `s01_crm.py` — THE REFERENCE REEL. Copy its structure exactly. Study it closely.
- `suite.py` — shared CSS classes, `appview()`, `dock()`, `toast()`, `icon()`, JS helpers
  (`handoff`, `grow`, `countUp`, `money`, `scrollTo`).
- `shell.py` — stage, hook, captions, phone, callouts, end card, sting, and the JS helpers
  `P, W, L, S, E, view, typeInto, taps, finger, callout`. Read its CSS + JS so you know what exists.
- `render.py` — `python3 render.py --stills <module> <t1> <t2> ...` writes half-size PNGs to stills/.
- `sheet.py` — `python3 sheet.py S0N` makes stills/S0N_sheet.png (contact sheet) — Read it to check.

DO NOT run `render.py --video` (the machine has 2 CPUs; the lead renders all videos serially later).
DO NOT edit shell.py, suite.py, render.py, sheet.py or other agents' modules. If you need extra CSS,
put it in your reel's `css=` string, prefixed with your own class prefix (e.g. `.bk-` for booking)
so nothing collides. Element ids must also use your prefix.

## Fixed timeline (set by the shell — fit your story inside it)
- 0–3.2 s: hook (kicker + hook text) — handled by the shell.
- 3.0–16 s: phone on screen. Your `renderReel(t)` drives everything inside it.
- Captions: exactly 4, covering ~3.35→15.5 s, each 2.5–3.5 s long, as (start, end, text).
- ~13–15.5 s: the cross-app hand-off toast (+ optional callout listing which apps use the data).
- 15.8–18.9 s: end card (your `end` text). 18.9–21.5 s: logo sting (default tag is fine).
- Use 2–3 views (screens) with `view(id,t,a,b)` cross-fades like s01. Show real interaction:
  `taps()` on the elements being pressed, `typeInto()` for typing, scrolls, things appearing.
  Leave ~0.4 s between a tap and the screen it triggers. Keep motion readable — one thing at a time.
- Phone screen geometry: body area is 604 px wide; visible body height ≈ 1080 px (top 154 to 224
  from the bottom). Keep key content in the upper ~900 px of the body.

## Writing rules (Waypoint brand bible + house rules — these are hard rules)
- Made-up data only: invented names, 902-555-01xx phone numbers, invented addresses in Kentville /
  Wolfville / New Minas / Berwick. Never a real person, client or live URL.
- Mechanisms, never outcomes: "the crew's hours come straight from the job app" is fine;
  "save 5 hours a week", "+40% bookings", "get paid faster" are NOT.
- No hype words: revolutionary, seamless, unlock, game-changer, 10x, effortless, magic.
- Canadian English (colour, labour, centre). Prices: HST 14%; write CAD in captions when a price appears there.
- AI only drafts or suggests; a person reviews and decides. Payroll/purchasing never execute without an approval step.
- Don't name competitors.
- Hook: ≤ 11 words, concrete, about the job not the software ("Who's off next week? Answered before the crew asks.").
- Kicker format: "<App label> · <what it is>" e.g. "Schedule · Booking".
- End text: one sentence, ≤ 20 words, ending on the idea that Waypoint builds it around how the business already works
  (vary the wording across reels — don't copy s01's).
- Captions: short, plain, present tense, ≤ 12 words each.

## Shared cast (keep continuity across reels)
- Owner/office: **Erin Harlow** (owner), **Sam Pine** (office).
- Crew: **Owen Cleveland** (crew lead), **Maya Ross**, **Jordan Lantz**, **Theo Burgess** (new hire, started Oct 2026).
- Customers: **Dana Keddy** (14 Belcher St, Kentville, 902-555-0142, gate code 4471, dog in back yard),
  Marcel Boudreau, Priya Sandhu, Tom Gallant, Rosa Fitzgerald, Jack Whynot, Lena Comeau.
- Quote Q-1042 (Dana, winter snow service, $720.00 + HST $100.80 = $820.80). Invoice numbers INV-22xx.
- Supplier (stock): "Valley Turf & Supply" (invented). Dates: October–November 2026.

## Done means
1. `/home/claude/suite-reels/<your module>.py` exists with `ALL = [YOUR_REEL]` and a `name` like `S02_schedule-booking`.
2. You rendered stills at at least 12 timestamps across 3–16 s plus 1.5, 17.4, 20.6, made the contact sheet,
   LOOKED at it, and fixed: overlapping/cut-off text, empty screens, elements off-screen or behind the dock,
   taps landing in the wrong place, anything unreadable, JS errors (render.py prints them).
3. Your final message: the module name, hook, the 4 captions, the end text, and 2–3 line post caption idea —
   nothing else. Do not deliver files to the user.
