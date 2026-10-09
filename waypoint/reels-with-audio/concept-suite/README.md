# Waypoint concept suite — reels with audio

Same 13 reels as `../../reels-no-audio/concept-suite/`, with original audio added:
a composed music bed (different chords/tempo per reel) plus UI sounds timed to the
on-screen action — taps, typing, screen changes, the cross-app hand-off chime and the logo sting.

- All audio is synthesised from code (`reels-no-audio/concept-suite/source/audio.py`),
  so it is original and cleared for business use (house rule 9). No library tracks.
- Loudness: about −16 LUFS integrated, true peak −1.5 dB (suits Reels / Shorts / TikTok).
- Captions and covers: see `../../reels-no-audio/concept-suite/`.
- To swap in a different track, use the silent versions instead.
- Re-make: `python3 audio.py` (needs numpy, scipy, ffmpeg; reads the scene modules for timings).
