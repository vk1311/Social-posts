# Waypoint concept suite — reels (no audio)

13 vertical reels (1080×1920, 30 fps, 21.5 s, silent): a trailer (S00) plus one per app of a concept
12-app suite for an invented client, Harlow & Pine. Every frame carries "Concept demo · made-up data".

- `S00`–`S12` MP4s: add a cleared business-library track when posting (house rule 9).
- `covers/`: cover frame for each reel.
- `CAPTIONS.md`: hooks and draft post captions — drafts only, nothing scheduled.
- `source/`: HTML-scene renderer. Needs Playwright + Chromium, ffmpeg, and Manrope/DM Sans fonts at
  /home/claude/fonts (`Manrope.woff2`, `DMSans.woff2`, from @fontsource-variable). Re-render one reel:
  `python3 render.py --video s03_quotes` · check frames: `python3 render.py --stills s03_quotes 5 9 13`.
