# Batch 2: revisions, 6 Oct 2026

22 manifest rows (new or changed posts only), 4 silent reels, the report (`report/`) and the website files (`site/`). Accepted batch-1 posts aren't re-sent. Nothing is published.

> **In this public repo:** `report/` and `site/` are left out. The report is the email-gated download on waypointns.ca/report (and section 9 is still a placeholder), and the site files belong in the website repo. The sections below describe them for reference.

## Counts
| Brand | Rows | READY | NEEDS-INPUT | HOLD |
|---|---|---|---|---|
| Waypoint | 12 (W04, W06, W08, W12, R1–R6, WR1, WR2) | 4 | 2 | 6 |
| Staffkin | 6 (S01-3, S02-2, S08-1…3, SR1) | 5 | 1 | 0 |
| Keegix | 3 (K06, K09, KR1) | 3 | 0 | 0 |
| JJ Pumps | 1 (J04) | 1 | 0 | 0 |

## What changed
- **Dropped:** W05 and W09 (rejected). K03 is parked and not included.
- **W03:** not swapped. BDC's 2026 State of Entrepreneurship report isn't out yet (last year's came out Oct 20), so W03 stays as accepted and isn't in this manifest.
- **W04:** remade. The opener is now "Where Waypoint is listed.", followed by one slide per platform (Google Business Profile, Clutch, Bing Places, Apple Business Connect, Yelp, Yellow Pages) and an end slide, all in the lining design. **NEEDS-INPUT:** I couldn't capture live screenshots or download the official logos from here, so each platform slide has a marked logo tile and screenshot frame. `tools/w04_build.py` drops the files in and re-renders all 8 slides in one command. Listing URLs are in the notes.
- **W06:** now says "Certified QuickBooks Online ProAdvisor", shows the badge, and makes no sync claim. The headline became "Set up the way your bookkeeper expects."
- **W08:** option 2 only.
- **R1:** the 76%/9% opener is removed and the post now opens on the process line. The 39% line uses your wording.
- **R2, R4, R5:** tone softened, numbers unchanged.
- **R3:** adds the custom AI tools slide and ends on "Custom software, with or without AI."
- **R6:** same 39% fix as R1. It also mentions the AI tools.
- **S01-3:** replaced with **pay deductions** in Nova Scotia, checked on novascotia.ca. Ends "Not legal advice." Same slot.
- **S08-1…3:** now read "An example split from our template". S08-1 slide 6 is now "Hiring someone under 16?", which covers both the 14–15 rule and the under-14 rule.
- **K06:** "$100,000 CAD". **J04:** kites removed.
- **New:** K09 (6-slide carousel plus a LinkedIn caption for property managers and cleaners, real features and prices only).
- **New reels:** WR1, WR2, KR1 and SR1. All are silent 1080×1920 H.264 MP4s, 12–14 s each, with a cover PNG. Text fades and rises in. SR1 uses real app screens.

## The report (`report/`)
- `report-final.md` uses the same structure and the same sourced numbers, in neutral, opportunity-led wording. It includes the 40.0% StatCan figure, CFIB's exact Nova Scotia wording and the 39% wording. The Waypoint pitch is one short closing section (custom software and custom AI tools; no websites). Sources are end notes.
- `waypoint-atlantic-report-oct-2026.pdf` is 10 Letter pages: ink cover with the Waypoint mark, Manrope and DM Sans, page numbers, and a Sources page. I viewed every page.
- `CHANGES.md` lists 35 before → after changes to claim wording, plus notes.
- **Needs you:**
  - **Section 9 is a placeholder.** The full report text hadn't been pasted into this conversation, and the pack removed section 9. Paste it in and I'll fold it in with the same tone pass. The intro's "two in three Atlantic organizations have no website on their Google listing" comes from that section and wasn't checked.
  - Sections 10–11 were already condensed in the pack.
  - **39% wording:** CFIB's release says "39% say the business is too reliant on them for day-to-day operations". "To be sellable" is the report's interpretation. Your call.

## Website (`site/`)
Full files plus diffs in `patches/`, with CRLF line endings to match the repo:
- `guides.ts` adds the report entry.
- `report.tsx` is the new `/report` landing page: four neutral findings with sources, who it's for, the disclosure and the email form.
- `enquiry.mts` adds the optional Twenty CRM copy. It is silent, has a timeout and never blocks the save or the emails.
- `automation.tsx` gets a short "AI that drafts. You decide." section.

`site/README.md` (delivered separately, not in this repo) has the setup steps, the PDF upload path and a test plan. Upload the PDF only once section 9 is in.

## Still needs Vatsal
1. **W04:** logos and screenshots (run the tool). Also fix the Yellow Pages listing: it shows a 647 number, the category "Internet Product & Service Providers" and no website.
2. **W12:** no fresh non-tariff headline exists yet. There are three candidates to check in early November; it's NEEDS-INPUT with no image.
3. **S02-2:** drafted from HR Reporter's Oct 5 story about TD email signatures, which will be 21 days old on Oct 26. Two other candidates are in the notes.
4. **Report:** section 9 text, and the 39% wording decision.
5. **R1–R6 and S09** stay HOLD until the report is live.
