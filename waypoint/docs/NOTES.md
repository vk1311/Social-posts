# Waypoint — site notes

Built on the NorthStar codebase: TanStack Start + Vite + React 19 + Tailwind 4.
Rebranded to Waypoint, repalette to chart magenta, all fabricated content removed.

---

## 1. Deploying

This project has a build step. You **cannot** drag the folder onto Netlify.

1. Create a new repo on GitHub and push this folder to it.
2. In Netlify: **Add new site → Import an existing project → GitHub**, pick the repo.
3. Netlify reads `netlify.toml` and uses:
   - build command `vite build`
   - publish directory `dist/client`
4. Every push to the default branch redeploys automatically.

Do the first deploy **now**, before adding more content. If something in the build
breaks, you want to find it while the change set is small.

Local, if you ever get to a laptop:
```
npm install
npm run dev      # http://localhost:3000
npm run build
```

---

## 2. Email — hello@waypointns.ca into your personal inbox

Netlify hosts DNS but does not do email. You need a mail provider. Below is the free
route that lets you **send as well as receive** from your own domain, which matters:
if someone emails hello@waypointns.ca and gets a reply from a gmail.com address, it
undercuts everything the site says about being a real business.

### Option A — Zoho Mail (recommended: send *and* receive, free)

**Step 1.** Sign up at zoho.com/mail → "Sign up with a domain I already own" → enter
`waypointns.ca`. Choose the free Forever plan (1 domain, up to 5 users).

**Step 2.** Zoho gives you a domain-verification `TXT` record. In Netlify:
**Domains → waypointns.ca → DNS records → Add a record.**
- Type: `TXT`
- Name: `@`
- Value: the string Zoho gave you

Wait a few minutes, then click Verify in Zoho.

**Step 3.** Create the mailbox `hello@waypointns.ca` inside Zoho.

**Step 4.** Add Zoho's MX records in Netlify (same DNS panel). Zoho shows the exact
hostnames on screen — use theirs, not these from memory:
- `MX` · name `@` · value `mx.zoho.com` · priority `10`
- `MX` · name `@` · value `mx2.zoho.com` · priority `20`
- `MX` · name `@` · value `mx3.zoho.com` · priority `50`

**Step 5.** Add the DKIM `TXT` record Zoho provides (name looks like
`zmail._domainkey`). This is what stops your mail landing in spam.

**Step 6.** Pull it into the Gmail app on your phone so you are not checking two
inboxes:
- Gmail → Settings → Add account → Other
- Incoming: `imap.zoho.com`, port 993, SSL
- Outgoing: `smtp.zoho.com`, port 465, SSL
- Username: `hello@waypointns.ca`, password: your Zoho password (or an app password
  if you turn on two-factor)

Now mail to hello@waypointns.ca arrives in Gmail, and replies go out *as*
hello@waypointns.ca.

### Option B — ImprovMX (faster, receive only)

Free, five minutes, but replies come from your personal address.

1. improvmx.com → add `waypointns.ca` → alias `hello@` → your personal Gmail.
2. In Netlify DNS add:
   - `MX` · `@` · `mx1.improvmx.com` · priority `10`
   - `MX` · `@` · `mx2.improvmx.com` · priority `20`
3. Add SPF — but see the warning below first.

### ⚠️ The SPF trap — read this before adding any TXT record

You already send transactional email through **Resend** on this domain. A domain can
have **only one** SPF record. Adding a second one breaks authentication for *both*
senders, and your invoices start landing in spam.

Find your existing SPF `TXT` record (starts with `v=spf1`) and **edit** it to include
the new provider. Do not create a second one.

```
v=spf1 include:_spf.resend.com include:zoho.com ~all      ← Zoho
v=spf1 include:_spf.resend.com include:spf.improvmx.com ~all   ← ImprovMX
```

Use whatever include value the provider tells you; the ones above are illustrative.

### Verifying

- Send a test from another address to hello@waypointns.ca.
- Send one *from* hello@ to a Gmail address, open it, and check "show original" —
  SPF, DKIM and DMARC should all say PASS.
- Send a test invoice from the DJ Movers tool afterwards, to confirm you did not
  break Resend.

---

## 3. Forms

All four forms post to Netlify Forms via `public/__forms.html`:
`newsletter`, `resource-request`, `contact`, `system-audit`.

Submissions appear in **Netlify → Forms**. Turn on email notifications there so they
reach your inbox.

**The resource downloads capture an email but do not yet send anything.** The
`resource-request` form records which guide was asked for in a `guide` field. To
actually deliver the PDF you need either:
- a Netlify Function that fires Resend on submit — you already have this exact
  pattern in the DJ Movers invoice sender, so it is copy-and-adapt, or
- manual sending until the volume justifies automating it.

Until one of those exists, the confirmation message overpromises slightly. Either
wire it up or soften the wording in `src/components/ResourceForm.tsx`.

Also: the six guides do not exist yet. Write them or remove the cards.

---

## 4. Content rules — do not change these

1. **Every figure on the site is a mechanism, never an outcome.** "~30 sec to send an
   invoice", "day 7 reminder" — settings a client can verify on day one. Never
   "+42% bookings". Under Canada's Competition Act, performance claims need adequate
   and proper testing behind them *before* you make them.
2. **No invented testimonials.** The three cards on `/work` are labelled pending on
   purpose. Replace them only with real quotes and real names.
3. **No ranking promises.** The line on the site is that nobody can promise the top
   slot; what is achievable is being readable.
4. **Data residency: "Canada", not "Nova Scotia".** Netlify is a global CDN and
   Supabase's nearest region is `ca-central-1` in Montréal. Set Supabase to
   `ca-central-1` before this claim goes live, or remove it.
5. **DJ Movers is named on `/work` only.** Elsewhere it is "a Valley moving company".

---

## 5. Where things live

| What | File |
|---|---|
| Palette, all design tokens | `src/styles.css` → `:root` |
| Logo component | `src/components/Logo.tsx` |
| Nav, footer, CTA band | `src/components/SiteShell.tsx` |
| Services, industries, mechanisms, guides, video IDs | `src/data/site.ts` |
| Hero panel, video player, diagrams | `src/components/Visuals.tsx` |
| Pages | `src/routes/*.tsx` |

Adding a route: drop a file in `src/routes/`. The router regenerates `routeTree.gen`
automatically on build.

### Palette
```
--ink-900   #12252F   chart ink, dark sections, body text
--ink-800   #1B333F   raised surfaces on dark
--accent    #C2185B   chart magenta — CTAs, the fix dot, eyebrow rules
--accent-dark #9E1149  accent text on light backgrounds
--accent-soft #FBE3EC  accent tints and pills
--paper     #FBF9F4   page background
--cloud     #F2ECE0   soft section background
--line      #E3DED2   borders
--muted     #5A6B75   secondary text
```

On charts, magenta is the colour reserved for critical overlay information — lights,
beacons, restricted areas. Everything printed in magenta is there because missing it
is dangerous. Keep it under ~10% of any surface.

### Logo sizing rule
`<WaypointMark full />` above 64px. Default (`full={false}`) below — the hairlines and
darts collapse into grey mush at nav size. The nav and favicon both use the small one.

---

## 6. Still open

- [ ] First deploy via GitHub → Netlify
- [ ] Set Supabase region to `ca-central-1`
- [ ] Set up hello@waypointns.ca (section 2)
- [ ] Turn on Netlify Forms email notifications
- [ ] Add your photo → replace `/public/portrait-placeholder.svg`, update `src` in `src/routes/about.tsx`
- [ ] Write the six guides, or remove the cards on `/resources`
- [ ] Wire resource delivery to Resend, or soften the confirmation wording
- [ ] Re-record the invoicing demo without your personal email and the app URL visible
- [ ] Replace pending review cards as real ones arrive
