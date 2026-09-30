// Builds the Staffkin carousel and photo posts (1080x1350 PNG) with Playwright.
// node slides.mjs   -> writes ../out/posts/<post>/<n>.png
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';

const ROOT = '/home/claude/staffkin-video';
const OUT = `${ROOT}/out/posts`;
const W = 1080, H = 1350;

const RINGS = (c1 = '#2E2A6B', c2 = '#7B8CF5', sw = 4) => `<svg viewBox="3 8 34 24" width="100%" height="100%"><circle cx="15" cy="20" r="10" fill="none" stroke="${c1}" stroke-width="${sw}"/><circle cx="25" cy="20" r="10" fill="none" stroke="${c2}" stroke-width="${sw}"/></svg>`;
const OK = (c = '#1F8A5B', s = 30) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>`;
const NO = (c = '#C0392B', s = 30) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="${c}" stroke-width="3" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>`;

const CSS = `
@font-face { font-family: Outfit; font-weight: 400; src: url(file://${ROOT}/fonts/outfit-latin-400-normal.woff2); }
@font-face { font-family: Outfit; font-weight: 500; src: url(file://${ROOT}/fonts/outfit-latin-500-normal.woff2); }
@font-face { font-family: Outfit; font-weight: 600; src: url(file://${ROOT}/fonts/outfit-latin-600-normal.woff2); }
@font-face { font-family: Outfit; font-weight: 700; src: url(file://${ROOT}/fonts/outfit-latin-700-normal.woff2); }
:root { --indigo:#2E2A6B; --peri:#7B8CF5; --peri-soft:#E3E7FE; --paper:#F5F6FC; --ink:#23213F; --muted:#5F5C85; --line:#E1E3F0; --good:#1F8A5B; --good-soft:#DDF3E8; --bad:#C0392B; --bad-soft:#FBE3E0; --warn:#9A6414; --warn-soft:#FDF1D8; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { width: ${W}px; height: ${H}px; overflow: hidden; font-family: Outfit, sans-serif; color: var(--ink); -webkit-font-smoothing: antialiased; }
.slide { position: relative; width: ${W}px; height: ${H}px; overflow: hidden; padding: 96px 90px 190px; display: flex; flex-direction: column; justify-content: center; }
.slide.cov { justify-content: flex-start; padding-top: 110px; }
.paper { background: var(--paper); } .white { background: #fff; } .indigo { background: var(--indigo); color: #fff; }
.deco { position: absolute; width: 900px; height: 635px; right: -300px; bottom: -180px; opacity: .07; }
.indigo .deco { opacity: .12; }
.foot { position: absolute; left: 90px; right: 90px; bottom: 58px; display: flex; align-items: center; justify-content: space-between; font-size: 26px; }
.brand { display: flex; align-items: center; gap: 12px; font-weight: 500; color: var(--indigo); font-size: 30px; }
.indigo .brand { color: #fff; }
.brand i { width: 46px; height: 33px; display: inline-block; }
.count { color: var(--muted); font-weight: 500; } .indigo .count { color: #B9BCE6; }
.eyebrow { font-size: 26px; font-weight: 700; letter-spacing: .12em; color: var(--peri); text-transform: uppercase; margin-bottom: 28px; }
.indigo .eyebrow { color: #AEB8FF; }
h1 { font-size: 110px; line-height: 1.02; letter-spacing: -.025em; font-weight: 700; color: var(--indigo); }
.indigo h1 { color: #fff; }
h1 em, h2 em { font-style: normal; color: var(--peri); } .indigo h1 em { color: #AEB8FF; }
h2 { font-size: 78px; line-height: 1.05; letter-spacing: -.02em; font-weight: 700; color: var(--indigo); margin-bottom: 30px; }
.num { width: 76px; height: 76px; border-radius: 50%; background: var(--indigo); color: #fff; display: grid; place-items: center; font-size: 36px; font-weight: 700; margin-bottom: 34px; }
p.body { font-size: 40px; line-height: 1.36; color: var(--ink); max-width: 880px; } p.body b { color: var(--indigo); }
.indigo p.body { color: #E4E6FF; }
.sub { font-size: 42px; line-height: 1.3; color: var(--muted); margin-top: 34px; max-width: 860px; }
.indigo .sub { color: #D3D6FF; }
.swipe { margin-top: auto; font-size: 30px; font-weight: 600; color: var(--peri); display: flex; align-items: center; gap: 12px; }
.indigo .swipe { color: #AEB8FF; }
.src { position: absolute; left: 90px; right: 90px; bottom: 112px; font-size: 20px; color: var(--muted); line-height: 1.35; }
.indigo .src { color: #A9ACD9; }
.card { background: #fff; border: 2px solid var(--line); border-radius: 28px; padding: 36px 40px; }
.row { display: flex; gap: 22px; align-items: center; }
.pill { display: inline-block; font-size: 24px; font-weight: 700; padding: 8px 18px; border-radius: 999px; }
.bars .b { margin-bottom: 30px; } .bars .lab { font-size: 32px; margin-bottom: 10px; display: flex; justify-content: space-between; } .bars .lab b { font-size: 40px; color: var(--indigo); }
.bars .track { height: 30px; border-radius: 15px; background: var(--peri-soft); overflow: hidden; } .bars .track i { display: block; height: 100%; border-radius: 15px; }
.split { display: flex; height: 90px; border-radius: 18px; overflow: hidden; margin: 10px 0 28px; }
.split i { display: block; height: 100%; }
.legend { display: grid; grid-template-columns: 1fr; gap: 16px; font-size: 33px; }
.legend div { display: flex; gap: 12px; align-items: center; } .legend s { width: 24px; height: 24px; border-radius: 6px; flex: none; }
.legend b { margin-left: auto; color: var(--indigo); }
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.cols h3 { font-size: 36px; margin-bottom: 18px; }
.li { display: flex; gap: 16px; font-size: 35px; line-height: 1.3; margin-bottom: 18px; } .li svg { flex: none; margin-top: 3px; }
.q { font-size: 37px; line-height: 1.3; padding: 26px 30px; border-radius: 22px; background: #fff; border: 2px solid var(--line); margin-bottom: 20px; }
.q small { display: block; font-size: 22px; font-weight: 700; letter-spacing: .08em; color: var(--peri); margin-bottom: 8px; }
table { width: 100%; border-collapse: collapse; font-size: 32px; }
td, th { text-align: left; padding: 20px 18px; border-bottom: 2px solid var(--line); vertical-align: top; }
th { font-size: 22px; letter-spacing: .08em; color: var(--indigo); background: var(--peri-soft); }
.url { margin-top: 40px; font-size: 34px; font-weight: 600; background: #fff; color: var(--indigo); padding: 22px 30px; border-radius: 18px; display: inline-block; }
.btn { display: inline-block; background: var(--peri); color: #fff; font-weight: 700; font-size: 40px; padding: 26px 52px; border-radius: 999px; margin-top: 44px; }
`;

const frame = (inner, { bg = 'paper', n, total, deco = true, src = '' } = {}) => `
<div class="slide ${bg}${inner.includes('class="swipe"') ? ' cov' : ''}">
  ${deco ? `<div class="deco">${bg === 'indigo' ? RINGS('#fff', '#AEB8FF', 3) : RINGS('#2E2A6B', '#7B8CF5', 3)}</div>` : ''}
  ${inner}
  ${src ? `<div class="src">${src}</div>` : ''}
  <div class="foot"><span class="brand"><i>${bg === 'indigo' ? RINGS('#fff', '#AEB8FF') : RINGS()}</i>staffkin</span><span class="count">${total ? `${n} / ${total}` : 'staffkin.com'}</span></div>
</div>`;
const cover = (eyebrow, title, sub = '', swipe = 'Swipe') => `<div class="eyebrow">${eyebrow}</div><h1>${title}</h1>${sub ? `<div class="sub">${sub}</div>` : ''}${swipe ? `<div class="swipe">${swipe} <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>` : ''}`;
const point = (num, title, body, visual = '') => `${num ? `<div class="num">${num}</div>` : ''}<h2>${title}</h2>${body ? `<p class="body">${body}</p>` : ''}${visual ? `<div style="margin-top:46px">${visual}</div>` : ''}`;
const cta = (title, sub, url, button = '') => `<div class="eyebrow">Free template</div><h1 style="font-size:96px">${title}</h1><div class="sub">${sub}</div>${button ? `<div><span class="btn">${button}</span></div>` : ''}<div><span class="url">${url}</span></div>`;
const liOk = (t) => `<div class="li">${OK()}<span>${t}</span></div>`;
const liNo = (t) => `<div class="li">${NO()}<span>${t}</span></div>`;
const PAL = ['#2E2A6B', '#4B4AA8', '#7B8CF5', '#A9B4FA', '#C9D0FC', '#1F8A5B', '#8FD1B2'];
const splitBar = (parts) => `<div class="card"><div class="split">${parts.map(([, p], i) => `<i style="width:${p}%;background:${PAL[i]}"></i>`).join('')}</div><div class="legend">${parts.map(([l, p], i) => `<div><s style="background:${PAL[i]}"></s>${l}<b>${p}%</b></div>`).join('')}</div></div>`;
const questions = (qs, tag = 'ASK') => qs.map((q) => `<div class="q"><small>${tag}</small>${q}</div>`).join('');

// ------------------------------------------------------------------ posts
const POSTS = {};

POSTS['02-carousel-line-cook-job-description'] = [
  ['indigo', cover('Job description of the week · 01', 'Hiring a line cook? <em>Your job ad is probably missing these 5 things.</em>', 'Nova Scotia edition.')],
  ['paper', point(1, 'Say the pay. <em>Out loud.</em>', 'Job Bank’s Nova Scotia median for cooks is <b>$17.00/hr</b>. Minimum wage rose to <b>$17.00</b> on October 1. If your ad says “competitive wage”, cooks assume that’s the floor.',
    `<div class="card bars"><div class="b"><div class="lab"><span>NS median wage, cooks (2025 data)</span><b>$17.00</b></div><div class="track"><i style="width:76%;background:var(--indigo)"></i></div></div><div class="b" style="margin:0"><div class="lab"><span>NS minimum wage since Oct 1, 2026</span><b>$17.00</b></div><div class="track"><i style="width:76%;background:var(--peri)"></i></div></div></div>`),
    'Sources: Job Bank wages, Cooks (NOC 63200), Nova Scotia, 2025 · Government of Nova Scotia, minimum wage news release, Dec 2, 2025.'],
  ['paper', point(2, 'Show what the <em>shift</em> looks like.', 'People apply faster when they can picture the job. A realistic split of a line cook’s time:', splitBar([['Line cooking', 30], ['Prep and mise en place', 20], ['Food safety', 15], ['Stock and waste', 10], ['Equipment and cleaning', 10], ['Shift handover', 10], ['Quality checks', 5]]))],
  ['paper', point(3, 'Must-haves <em>vs</em> nice-to-haves.', 'Split them, or you’ll scare off good cooks who tick 8 of 10 boxes.',
    `<div class="cols"><div class="card"><h3 style="color:var(--good)">Must-have</h3>${liOk('Experience on a busy line')}${liOk('Knife and station skills')}${liOk('Evening and weekend shifts as scheduled')}</div><div class="card"><h3 style="color:var(--peri)">Nice-to-have</h3>${liOk('Red Seal Cook (voluntary in NS)')}${liOk('Culinary diploma')}${liOk('Grill, fry and sauté stations')}</div></div>`),
    'Red Seal Cook is not one of Nova Scotia’s compulsory certified trades (NS Apprenticeship Agency).'],
  ['paper', point(4, 'Food safety: <em>the NS rule.</em>', 'The operator, or a staff member with a recognized <b>food hygiene certificate</b>, must be on site. Everyone else who handles food needs training suited to their job.<br><br>Say in the ad whether you’ll pay for the course.'),
    'Source: Nova Scotia Food Safety Regulations, s. 28 · NS Government, food hygiene and handling courses.'],
  ['paper', point(5, 'Leave these <em>out.</em>', '',
    `<div class="card">${liNo('“Canadian experience required”')}${liNo('“Young, energetic team”')}${liNo('“Must be available any time, any day”')}<div style="height:10px"></div>${liOk('“Evening and weekend shifts. Schedule posted two weeks ahead.”')}</div>`) + `<p class="body" style="margin-top:34px;font-size:30px;color:var(--muted)">Age, family status and place of origin are protected under human rights law. Ask about the job, not the person.</p>`],
  ['indigo', cta('Get the full line cook <em>job description.</em>', 'Duties, skills, working conditions and performance measures. Free, and ready to download as Word.', 'staffkin.com/job-descriptions/line-cook')],
];

POSTS['04-carousel-ai-in-hiring'] = [
  ['indigo', cover('AI in hiring', 'Should AI pick your <em>next hire?</em>', 'Our answer is no. Here’s what we let it do, and what it never touches.')],
  ['paper', point('', 'What AI <em>does</em> in Staffkin', '', `<div class="card">${liOk('Drafts interview questions from the job details you type')}${liOk('Rewrites a question so it’s clearer')}${liOk('That’s it. You edit and approve every word.')}</div>`)],
  ['paper', point('', 'What AI <em>never</em> does', '', `<div class="card">${liNo('Read resumes')}${liNo('See a candidate’s answers')}${liNo('Score, rank or reject anyone')}</div><p class="body" style="margin-top:34px">Your interviewers enter every score. The compare table shows their numbers, not ours.</p>`)],
  ['paper', point('', 'Why we drew the line <em>there.</em>', 'Hiring is a judgment about a person. What makes it fair is asking everyone the same questions and scoring answers against the same guide.<br><br><b>AI can help write better questions. People should make the call.</b>')],
  ['white', `<div class="eyebrow">Hiring in Ontario?</div><h2>New job posting rules since <em>Jan 1, 2026.</em></h2><p class="body" style="font-size:31px;margin-bottom:26px">For employers with 25+ employees, public job postings must:</p><div class="card">${liOk('Say if AI is used to screen, assess or select applicants')}${liOk('Include the pay or a pay range')}${liOk('Say whether the job is an existing vacancy')}${liNo('Not require “Canadian experience”')}</div>`,
    'Source: Government of Ontario, Your guide to the Employment Standards Act, requirements for publicly advertised job postings.'],
  ['indigo', cta('See exactly how we use <em>AI.</em>', 'Plain answers, no fine print. Staffkin is free for your first job.', 'staffkin.com/ai-in-hiring').replace('Free template', 'Hire people, not paperwork')],
];

POSTS['05-carousel-cca-job-description'] = [
  ['indigo', cover('Job description of the week · 02', 'Hiring a continuing care assistant <em>in Nova Scotia?</em>', 'What’s required, what to check, and what to ask.')],
  ['paper', point(1, 'The <em>certificate.</em>', 'Licensed nursing homes and approved home support agencies must hire people with a <b>Nova Scotia CCA certificate</b>, or an accepted equivalent:', `<div class="card" style="font-size:31px;line-height:1.6">Personal Care Worker · Home Health Provider · Home Health Aide · Home Support Worker</div>`),
    'Source: NS Department of Health and Wellness, CCA Entry to Practice Policy (effective Nov 9, 2021).'],
  ['paper', point(2, 'Conditional hires: <em>allowed, with conditions.</em>', 'No certificate yet? The policy allows a conditional hire if the person has:', `<div class="card">${liOk('Standard First Aid and CPR level C before day one')}${liOk('A plan to earn the CCA certificate within 3 years')}</div>`),
    'Source: CCA Entry to Practice Policy, NS Department of Health and Wellness.'],
  ['paper', point(3, 'Check the <em>CCA Registry.</em>', 'Every CCA working in Nova Scotia must be on the provincial registry, in any setting, and renew every year.<br><br><b>Check it when you hire, and again at renewal.</b>'),
    'Source: Continuing Care Assistants Registry Act and Regulations · novascotiacca.ca registry FAQ.'],
  ['paper', point(4, 'Long-term care? <em>Vulnerable sector check.</em>', 'Nursing homes must complete a vulnerable sector check at the time of hire for staff, students and volunteers.<br><br>Put it in the job ad so no one is surprised.'),
    'Source: NS Long-Term Care Program Requirements (2026), s. 11.1.'],
  ['paper', point(5, 'Three questions <em>worth asking.</em>', '', questions(['A client refuses care you’re scheduled to give. What do you do?', 'How do you protect a client’s dignity during personal care?', 'You notice a change in a client’s condition. What do you do?'], 'INTERVIEW'))],
  ['indigo', cta('Get the full CCA <em>job description.</em>', 'Duties, qualifications, working conditions, plus interview questions with a 1 to 5 scoring guide. Free.', 'staffkin.com/job-descriptions/continuing-care-assistant')],
];

POSTS['08-carousel-server-job-description'] = [
  ['indigo', cover('Job description of the week · 03', 'Hiring a server? <em>Check the alcohol training rule first.</em>', 'Nova Scotia and beyond.')],
  ['paper', point('', 'Nova Scotia, since <em>Dec 1, 2024.</em>', 'Everyone who serves alcohol in licensed bars and restaurants must complete an <b>approved responsible alcohol service course</b>.', `<div class="card" style="font-size:30px;line-height:1.5">Courses listed by the Restaurant Association of Nova Scotia include <b>SafeCheck</b> and <b>Serve Right</b>.</div>`),
    'Sources: NS Liquor Licensing Regulations, s. 66A · NS Government news release, Aug 6, 2024 · rans.ca.'],
  ['paper', point('', 'Other <em>provinces.</em>', '', `<div class="card" style="padding:10px 10px"><table><tr><th>PROVINCE</th><th>COURSE</th><th>REQUIRED?</th></tr><tr><td>Ontario</td><td>Smart Serve</td><td>Yes, before the first shift</td></tr><tr><td>British Columbia</td><td>Serving It Right</td><td>Yes, before working</td></tr><tr><td style="border:0">Alberta</td><td style="border:0">ProServe</td><td style="border:0">Yes</td></tr></table></div>`),
    'Sources: AGCO (Ontario) · Responsible Service BC · AGLC (Alberta).'],
  ['paper', point('', 'Age <em>matters.</em>', 'In Nova Scotia, staff must be <b>19 or older to pour or dispense</b> alcohol.<br><br>Staff under 19 can serve it at the table in restaurants and, since June 1, 2026, in lounges.'),
    'Sources: NS Liquor Licensing Regulations, s. 48 · NS Government news release, May 27, 2026.'],
  ['paper', point('', 'What the job <em>really</em> is.', '', splitBar([['Guest service', 25], ['Food and drink delivery', 20], ['POS and payments', 15], ['Food safety', 15], ['Responsible alcohol service', 10], ['Side work', 10], ['Teamwork', 5]]))],
  ['paper', point('', 'Ask these in the <em>interview.</em>', '', questions(['A guest tells you about a food allergy. Walk me through what you do next.', 'Your section fills up all at once. How do you handle it?', 'How do you suggest add-ons or specials without being pushy?'], 'INTERVIEW'))],
  ['indigo', cta('Get the full server <em>job description.</em>', 'Duties, skills, working conditions and a scored interview guide. Free, and ready to download as Word.', 'staffkin.com/job-descriptions/server')],
];

// photos (single images)
POSTS['03-photo-why-reference-checks'] = [
  ['indigo', `<div class="eyebrow">Why check references?</div>
    <div style="font-size:230px;font-weight:700;line-height:.9;letter-spacing:-.04em;color:#fff;margin-top:10px">3 <span style="color:#AEB8FF">in</span> 4</div>
    <p class="body" style="font-size:46px;line-height:1.25;margin-top:28px;color:#fff">employers found something that didn’t add up in a candidate’s background in the past year.*</p>
    <p class="body" style="font-size:36px;margin-top:40px;color:#D3D6FF">A resume is what someone says.<br>A reference is what someone else saw.</p>
    <div><span class="btn" style="font-size:34px;padding:22px 40px">Reference checks in one click · $9</span></div>`,
    '*More than three-quarters of respondents. HireRight 2025 Global Benchmark Report, 1,000+ HR and risk professionals worldwide.'],
];

POSTS['07-photo-reference-speak-translated'] = [
  ['paper', `<div class="eyebrow">Reference speak, translated</div><h2 style="font-size:74px">What referees say, and <em>what to ask next.</em></h2>
    ${[['“She was… always on time.”', 'What would you want her to work on?'], ['“I’d have to check my notes.”', 'Would you hire him again? Why or why not?'], ['“He did what was asked.”', 'Tell me about a time he went beyond that.']].map(([a, b]) => `
      <div class="card" style="margin-bottom:22px;padding:26px 30px"><div style="font-size:34px;font-weight:600;color:var(--ink)">${a}</div>
      <div style="display:flex;gap:14px;align-items:center;margin-top:12px;font-size:31px;color:var(--indigo)"><svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#7B8CF5" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg><span>${b}</span></div></div>`).join('')}
    <p class="body" style="font-size:29px;color:var(--muted);margin-top:14px">Staffkin asks every referee the same 9 questions, in writing, with the candidate’s consent. $9 a check.</p>`],
];

POSTS['09-photo-your-hiring-system-honestly'] = [
  ['paper', `<div class="eyebrow">Your hiring system, honestly</div>
    <div style="position:relative;height:640px;margin-top:10px">
      <div class="card" style="position:absolute;left:0;top:20px;width:430px;transform:rotate(-4deg);box-shadow:0 20px 40px -20px rgba(35,33,63,.4)">
        <div style="display:flex;justify-content:space-between;font-size:26px;font-weight:600;color:var(--indigo)">Inbox <span class="pill" style="background:#C0392B;color:#fff;font-size:22px">47 unread</span></div>
        ${['RE: RE: line cook job??', 'Fwd: resume (1).pdf', 'is the job still open', 'Missed call from 902…'].map((s) => `<div style="font-size:23px;padding:12px 0;border-bottom:2px solid var(--line);color:var(--ink)">${s}</div>`).join('')}
      </div>
      <div class="card" style="position:absolute;right:-10px;top:0;width:470px;transform:rotate(3deg);padding:0;overflow:hidden;box-shadow:0 20px 40px -20px rgba(35,33,63,.4)">
        <div style="background:#1D6F42;color:#fff;font-size:22px;padding:12px 18px;font-weight:600">hiring_FINAL_v3_REAL.xlsx</div>
        <table style="font-size:20px"><tr><td>Name</td><td>Called?</td><td>Notes</td></tr><tr><td>Jordan</td><td>??</td><td>good i think</td></tr><tr><td>Sam</td><td>left vm</td><td>which Sam</td></tr><tr><td style="border:0">Priya</td><td style="border:0">yes</td><td style="border:0">#REF!</td></tr></table>
      </div>
      <div style="position:absolute;left:300px;top:300px;width:260px;height:260px;background:#FFE58A;transform:rotate(-7deg);padding:26px;font-size:36px;font-weight:600;color:#5b4a00;box-shadow:0 18px 30px -16px rgba(35,33,63,.5);line-height:1.15">call Jordan back?? refs??</div>
      <div class="card" style="position:absolute;right:30px;top:360px;width:380px;transform:rotate(-2deg);box-shadow:0 20px 40px -20px rgba(35,33,63,.4)">
        <div style="font-size:24px;font-weight:700;color:var(--indigo)">Interview scorecard</div>
        <div style="font-size:22px;color:var(--muted);margin-top:6px">Candidate: ________</div>
        <div style="position:absolute;right:30px;bottom:20px;width:120px;height:120px;border-radius:50%;border:10px solid rgba(120,72,30,.22)"></div>
        <div style="font-size:22px;color:var(--muted);margin-top:40px">Score: 4? 3? (ask Dave)</div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:26px;margin-top:6px">
      <div style="font-size:40px;font-weight:700;color:var(--peri)">vs</div>
      <div class="card" style="flex:1;display:flex;gap:22px;align-items:center;border-color:var(--peri);box-shadow:0 20px 40px -24px rgba(46,42,107,.4)">
        <i style="width:62px;height:44px;display:inline-block">${RINGS()}</i>
        <div><div style="font-size:33px;font-weight:700;color:var(--indigo)">Line cook · 3 candidates</div><div style="font-size:25px;color:var(--muted)">Scored side by side · 2 references in · 1 link</div></div>
      </div>
    </div>`],
];

// ------------------------------------------------------------------ render
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: W, height: H } });
fs.writeFileSync(`${ROOT}/posts/blank.html`, '<!doctype html><html><head><meta charset="utf-8"></head><body></body></html>');
await p.goto(`file://${ROOT}/posts/blank.html`);
const only = process.argv[2];
for (const [name, slides] of Object.entries(POSTS)) {
  if (only && !name.startsWith(only)) continue;
  const dir = `${OUT}/${name}`; fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
  for (let i = 0; i < slides.length; i++) {
    const [bg, inner, src] = slides[i];
    const html = frame(inner, { bg, n: i + 1, total: slides.length > 1 ? slides.length : 0, src });
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    const overflow = await p.evaluate(() => { const s = document.querySelector('.slide'); const f = document.querySelector('.foot').getBoundingClientRect().top; const src = document.querySelector('.src'); const lim = src ? src.getBoundingClientRect().top : f; let max = 0; s.querySelectorAll('.slide > *:not(.foot):not(.src):not(.deco)').forEach((e) => { max = Math.max(max, e.getBoundingClientRect().bottom); }); return max > lim - 10 ? Math.round(max - lim) : 0; });
    if (overflow) console.log(`! ${name} slide ${i + 1} overflows by ${overflow}px`);
    await p.screenshot({ path: `${dir}/${String(i + 1).padStart(2, '0')}.png` });
  }
  console.log('built', name, slides.length);
}
await b.close();
