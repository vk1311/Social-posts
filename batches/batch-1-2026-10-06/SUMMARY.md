# Posts batch: 6 Oct 2026

56 manifest rows and 139 PNGs, made from `01_POSTS_TO_MAKE.csv`. Nothing is published or scheduled.

## How the IDs work
Some briefs cover several dates: S01, S02, S03, S04, S08 and K07. Each date gets its own row, named with a suffix (for example `S01-1` to `S01-5`). That way every row has one date and can be scheduled on its own. Report posts R1 to R6 and S09 have no date yet, so their files use `TBD` where the date would go.

## Count by brand
| Brand | Rows | READY | NEEDS-INPUT | HOLD |
|---|---|---|---|---|
| Waypoint | 18 (W01–W12, R1–R6) | 7 | 4 | 7 |
| Keegix | 11 (K01–K06, K07-1…4, K08) | 6 | 0 | 5 |
| Staffkin | 23 (S01-1…5, S02-1…2, S03-1…5, S04-1…4, S05–S07, S08-1…3, S09) | 21 | 1 | 1 |
| JJ Pumps | 4 (J01–J04) | 4 | 0 | 0 |

## Needs Vatsal's input
- **W03, W05, W09, W12 (Waypoint news).** Each is made from a real headline that I checked. The catch is the 14-day rule: by the posting date, most of these headlines will be more than 14 days old.
  - W03 uses the BDC study from Oct 6. It will be 15 days old on Oct 21.
  - W05 uses CFIB's Sept 24 release.
  - W09 uses Retail Insider's Sept 14 story on late payments. That one was already outside the window today, so treat it as a placeholder.
  - W12 uses CBC's Oct 6 story. It names two Valley makers, so decide whether a Waypoint tie-in on their story feels right.
  - Each card can be swapped for a newer headline in a few minutes. The alternatives are in each row's notes. BDC's State of Entrepreneurship report, due the week of Oct 12, is the obvious swap for W03 or W05.
- **S02-2 (Oct 26).** Uses HR Reporter's article from Oct 2, which will be 24 days old on posting day. Three candidate headlines for Nov 2, 9 and 16 are in its notes. I did not make S02-3 to S02-5, as the brief asked.
- **W08.** Three Customer Translation Guide options are rendered. Pick one.
- **S01-3 (references).** NS Labour Standards doesn't cover references, so this set uses a federal Privacy Commissioner finding from 2007. Confirm you're happy with that, or swap the topic.
- **K03.** G2 is the only listing I could confirm is live. A Capterra search found no Keegix listing, and AlternativeTo blocked my check, so both were dropped. If they're live when you check, add them back.
- **R3 changed.** I couldn't verify "41.4% of micro-firms" because StatCan blocks automated reading. The post uses the verified figure instead: 40.0% of all businesses say AI isn't relevant (StatCan Q2 2026, via ATB).
- **R4 changed.** "Nova Scotia the one bright spot" overstates CFIB. The copy now says what CFIB actually says: NS was the only province with modest business dynamism in 2015–19, and that momentum has gone quiet since 2024.
- **W11.** The before/after workflow steps are my placeholders. Confirm they match what the moving company really did, and get the client's OK. *(Not in this public repo: W11 stays out until the client agrees.)*

## Placeholders to fill in
`[TINYLAUNCH LINK]` (S04, S06), `[UNEED LINK]` (K07-4), `[REPORT LINK]` (R1–R6). R1–R5 also end with "Full report: link in bio."

## Decisions made along the way
- **Nov 11 is empty.** The last S01 set moved to Nov 12. W12 was already on Nov 12.
- **Keegix photos not used.** The `keegix/photos/` library looks AI-generated and I couldn't confirm it isn't. To be safe, the Keegix posts use type and the HTML guest-page mock-up only.
- **JJ photos.** `jj/product-photos/` turned out to be handwritten price-list pages, so none were used (prices aren't allowed anyway). I used real workshop photos from `jj/photos/raw` and blurred the other-brand nameplates on them ("UNITED" and others), as the bible requires. There are no real factory-process shots, so J03 is a "workshop floor" post.
- **Topic overlaps to watch.**
  - J03 (Oct 29) lands two days before the queued JJ "One workshop, a full range…" post (Oct 31). I kept J03 off "the range" to limit the overlap.
  - J02 overlaps the Nov 25 dealer draft.
  - R2's "735 hours" repeats the Staffkin post queued for Oct 14.
- **Staffkin's "one post a day" rule.** S01-1, S03-1, S02-1 and S06 share days with queued Staffkin posts, but on different channels (stories or LinkedIn). Check this fits the one-a-day rule.
- **Sticker placement** for every poll, quiz and link sticker is in the row's `notes`.
- **Freshness.** Every number has its source URL in `sources`. Minimum wage ($17.00 since Oct 1, 2026) and the NS short-term rental rules were checked today on novascotia.ca. Re-check both the week they post.
