# Waypoint — everything, one folder

## What's in here

| Item | What it is |
|---|---|
| `waypoint-site.zip` | The full website source. Unzip, push to GitHub, connect to Netlify. |
| `waypoint-brand/` | Logo system and social assets in chart magenta. |
| `NOTES.md` | Deployment, email setup, content rules, open checklist. |

## Do these three things, in order

**1. Deploy the site.**
Unzip `waypoint-site.zip`, push the folder to a new GitHub repo, then in Netlify:
Add new site → Import an existing project → GitHub → pick the repo. It reads
`netlify.toml` and builds itself. Do this before adding more content, so any build
error shows up while the change set is small.

**2. Set up hello@waypointns.ca.**
Full step-by-step in `NOTES.md` section 2. Read the SPF warning in that section
before you touch DNS — you already send through Resend, and a second SPF record
would break your invoice delivery.

**3. Set Supabase to `ca-central-1`.**
The site says your data stays in Canada. Make that true before it goes live.

## Brand assets — which file where

| File | Use |
|---|---|
| `waypoint-mark.svg` / `.png` | Primary. Anything above 64px. |
| `waypoint-mark-reversed.svg` / `.png` | Same, on dark backgrounds. |
| `waypoint-nav.svg` / `.png` | Nav, app icon, anything small. Tile version. |
| `waypoint-favicon.svg` / `.png` | Browser tab. |
| `waypoint-fb-profile.png` | 512×512, safe under Facebook's circular crop. |
| `waypoint-fb-cover.png` | 1640×856, content held inside the mobile-safe centre. |

The site already has its own copies in `public/`, so these are for Facebook, print,
email signatures and anywhere else off-site.

## Palette

```
Chart ink       #12252F    dark sections, body text
Ink 800         #1B333F    raised surfaces on dark
Chart magenta   #C2185B    CTAs, the fix dot, accents
Magenta dark    #9E1149    accent text on light
Magenta soft    #FBE3EC    tints and pills
Paper           #FBF9F4    page background
Cloud           #F2ECE0    soft sections
Line            #E3DED2    borders
Muted           #5A6B75    secondary text
```

Fonts: **Manrope** headings, **DM Sans** body. Both load from Google Fonts.

## Still open

Full checklist at the bottom of `NOTES.md`. The two that matter most:

- **The six guides on `/resources` do not exist.** The form captures an email but
  nothing is sent yet. Write them, or remove the cards.
- **Re-record the invoicing demo.** Your personal email and the live app URL are both
  visible in the current clip.
