# Source files

Scripts used to make the JJ Pumps posts, reels, cut-outs and guides. They were run in a Claude workspace, so the file paths at the top of each script point to that workspace; change them to your own folders before re-running.

| Script | Makes |
| --- | --- |
| cutouts.py | Background-removed pump images with nameplates hidden (uses rembg) |
| posts.py | The 38 post images (HTML rendered to JPG with Playwright) |
| reels.py | The 5 reel MP4s (HTML animation rendered frame by frame, encoded with ffmpeg) |
| posting-guide.py | captions.txt and posting-guide.pdf |
| reels-pack.py | The reel audio guide and voiceover scripts |

Needs: Python 3, Playwright with Chromium, Pillow, ffmpeg, rembg, and the Poppins font.
