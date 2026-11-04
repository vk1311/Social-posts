# Post batches

Finished posts for Waypoint, Keegix, Staffkin and JJ Pumps. Each batch has one folder per post (named by post ID), a `manifest.csv` and a `SUMMARY.md`. Nothing in here posts by itself: schedule each post from its manifest row.

| Batch | Covers | What's in it |
|---|---|---|
| [batch-1-2026-10-06](batch-1-2026-10-06/SUMMARY.md) | Oct 13 – Nov 17, plus holds into 2027 | First run for all four brands |
| [batch-2-2026-10-06](batch-2-2026-10-06/SUMMARY.md) | Revisions to batch 1, plus new posts and 4 silent reels | Replaces the batch-1 versions of W04, W06, W08, W12, R1–R6, S01-3, S02-2, S08-1…3, K06 and J04 |
| [batch-3-2026-10-07](batch-3-2026-10-07/SUMMARY.md) | Nov 14 – Dec 18, plus Jan 1, 2027 | Calendar fill, Waypoint builder posts, Google Business Profile posts, JJ voiceover scripts, LinkedIn captions |

## Reading a manifest

`manifest.csv` has one row per post, with these columns: `post_id, brand, date, time_halifax, channels, format, files, caption_facebook, caption_instagram, caption_linkedin, first_comment, alt_text, sources, status, notes`.

- `files` lists the images or videos in that post's folder, in posting order. Carousel slides are numbered `_1ofN`, `_2ofN`, and so on.
- `status` is READY, NEEDS-INPUT (something still to decide or supply; the `notes` column says what) or HOLD (waiting on an outside event, such as a launch or a report going live).
- `alt_text` holds one entry per image, separated by ` || `.
- Times are Halifax time. JJ Pumps posts at 7:30 PM India time, which is 11:00 Halifax until Oct 31 and 10:00 from Nov 1.

## Superseded or not used

- Batch 1: W05 and W09 were rejected, K03 is parked, and W08 had three options (option 2 was chosen; see batch 2). For any post ID that appears in both batches, the batch-2 version wins.
- W11 (a client before/after) isn't in this public repo until the client agrees.
- Batch 2's report PDF and website files aren't here. The report is the email-gated download on the Waypoint site, and the site files belong in the website repo.
- Batch 3's `repo_docs/` became the root `README.md` and `STATUS.md`.
