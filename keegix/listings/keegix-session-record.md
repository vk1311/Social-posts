# Keegix — session record, 24 Sep 2026

Context handoff. Keegix only. Everything here is state as of the end of this
session, with the reasoning behind each decision so future-you doesn't re-litigate
settled calls.

---

## What Keegix is

Digital welcome book for short-term rental hosts. Check-in, wifi, parking,
appliances, house rules, trash day, local picks, emergency contacts, checkout
list — all on one guest link, plus a printable letter-size QR sign for the door.
Guests open it in any phone browser: no app, no account.

- **Live at:** keegix.com
- **Vendor / company name on listings:** Waypoint Labs
- **Contact email everywhere:** hello@waypointns.ca (NOT a keegix domain — this
  is settled, do not suggest changing it)
- **Pricing:** Free (1 property) · Pro $9 CAD per property/month · $39 CAD
  one-time done-for-you setup
- **Competitors it sits beside:** Touch Stay, Hostfully Guidebooks, YourWelcome

---

## Initially identified

| Item | Where it came from |
|---|---|
| Two homepage bugs — deleted-account banner showing to logged-out visitors, empty `mailto:` in footer | Found on first fetch of the live site |
| No distribution — nowhere pointing at keegix.com | Opening question of the session |
| Whether to target Cape Breton | Asked |
| Whether to add a booking tool as an upsell | Asked |
| Whether to run Google Ads | Asked |
| Request for 200 places to list the link | Asked |
| How much of the listing work could be automated | Asked |
| Whether to wrap the site as an app | Asked |

---

## Completed

**Site fixes.** Both bugs fixed by the user. Footer contact now resolves to
hello@waypointns.ca.

**Asset kit built.** Taglines at three lengths, descriptions at 25/50/100/250
words, categories, tags, founder bio, standard answers to awkward form fields,
plus the submission checklist. Everything below was pasted from it.

**Screenshots prepared.** The original desktop capture was 1440×4612 — over
AlternativeTo's 4000px limit and useless as a thumbnail anyway. Cut into four
viewport-shaped panels (hero, what-goes-in-it, how-it-works, pricing) plus a
padded phone shot. All under 2MB.

**AlternativeTo submitted.** Freemium, Proprietary, Online + SaaS platforms,
Waypoint Labs as author. Note to moderators offered a free account for
verification.

**G2 submitted and verified.** Submitted as Software (not Service Provider),
which covers G2, Capterra, GetApp and Software Advice in one form — the separate
Capterra signup is therefore unnecessary. Verification came back within hours.
Left the "3 emails for reviewers" field blank deliberately: no real customers
yet, and fake reviewers get new profiles flagged.

**STR Specialist pitched.** Via their contact form. Email tuned after seeing
their affiliate disclosure — dropped the "no paid placements" line, which would
have read as a dig.

---

## Skipped, and why

**Supabase outreach tracker.** User skipped it. Replaced with a plain checklist
at the bottom of the asset kit. Same function, no setup.

**Booking tool as an upsell.** Decided against. Calendar sync, payments,
cancellations, and double-booking risk — a double-booking ruins a guest's
vacation and the reputation in one move. It also puts Keegix in competition with
Airbnb rather than beside it. Better upsells: more $39 setups, Pro for
multi-property hosts, a cleaner's checklist view.

**Google Ads.** Not now. Zero signups means nothing to optimise against; hosts
buy in Feb–April, not September; and Cape Breton search volume for guidebook
keywords is likely near zero. Revisit in late winter with search ads (not feed
ads) once there are ~10 real users. Suggested checking actual volume free in
Google Keyword Planner rather than guessing.

**200 listing sites.** Refused the number, not the task. Most low-tier
directories are nofollow and send nobody; a focused ~30 beats a 300-site blast.
Delivered ~45 real ones instead, tiered.

**Bubblewrap / app wrapper.** No. Play Store's minimum-functionality policy
rejects thin website wrappers, iOS more so. It also contradicts the "no app for
guests" line that's now in every listing description submitted today. The real
underlying need — offline guest access for cottages with no signal — is solved
by a service worker on the guest page, not an app.

**Automating the directory submissions.** Every form differs, half have captchas,
and several directories ban listings that arrive via bulk-submit services. Worth
automating later: contact finding (n8n scrape → manual review queue), send and
7-day follow-up via Resend, and Postiz for distribution. Not before twenty
emails have been hand-sent, because you don't yet know which email gets answered.

---

## Not completed

**G2 profile claim.** Blocked by a genuine platform bug: signing in at my.G2
returns to the signup screen; attempting to create returns "already registered."
Session isn't sticking. **Action:** one-line email to G2 support asking them to
attach Keegix to hello@waypointns.ca manually. Profile is verified and live
regardless — only admin access is missing.

**Two product screenshots.** The host editor with a property half-filled, and the
QR sign PDF. Everything uploaded so far is marketing page. Moderators and buyers
want to see the software. When these exist, swap them into first position on G2
and AlternativeTo — the first screenshot renders largest.

**AlternativeTo "Suggest as alternative".** Cannot be done until the listing is
approved (a few days). Then go to the Hostfully Guidebooks page and the Touch
Stay page and suggest Keegix on both. **This is the step that actually generates
traffic** — people searching "Touch Stay alternative" are already shopping. Easy
to forget after the submission is done.

**Remaining directories:** Launching Next (10 min, free, permanent dofollow),
Crunchbase (20 min), Indie Hackers (profile + one post about the $39/$9 pricing
decision, not a launch announcement). Product Hunt deliberately deferred — it
needs a scheduled Tuesday and three or four real users first, so the comments
aren't empty.

**Direct outreach.** Twenty messages to actual hosts. Not started. This is the
highest-value remaining item; the directories are groundwork.

---

## Ongoing

**The strategic position.** Setup revenue ($39, sold on Fiverr and via Maritime
host groups) is the way in, not the business. It doesn't compound — each one
costs an evening and stops when you stop. But it's cash, it's proof, and it
fills Keegix with real properties to learn from. The $9/property subscription
won't carry the product on its own: Hostfully's free tier gives one guidebook
forever and their paid tier is ~$8–10/month, so $9 prices above a bigger
incumbent for the same job.

**Cape Breton as a market.** Yes — strongest STR market in the province, and NS
requires every short-term rental to register and display a registration number,
so hosts are a findable group rather than a guess. Timing matters: season runs
June–October, hosts buy tools February–April.

**Fiverr.** 20% commission, so $39 nets ~$31. New sellers with no reviews
struggle; consider $25 for the first five orders, then raise. Fiverr buyers are
global, so the Maritime angle is irrelevant there — it only matters in the groups.

**Host groups.** Most ban promo posts outright. Answer questions properly under a
real name with no link; people click through to the profile. Some groups have a
designated promo day — ask an admin rather than guessing.

**Keegix's place in the wider plan.** It's the first of the side tools to meet a
real customer. Whatever this launch teaches — where signup drops off, what people
email about, whether the $39 sells — applies to the next tool before its landing
page gets built, not after.

---

## Open question from this session

The deleted-account banner and the empty mailto were still present in the raw
served HTML after the fix appeared correct in the browser, suggesting the element
renders and is then hidden by JavaScript. If that's still the case it matters:
Google indexes raw HTML, and link-preview scrapers (Facebook, LinkedIn, iMessage)
don't run JavaScript, so a shared keegix.com link could show that sentence as its
description. Worth a "View page source" check.
