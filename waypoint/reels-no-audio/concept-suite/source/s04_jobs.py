"""S04 — Jobs (crew app). Invented business Harlow & Pine; invented crew + customers; 555 numbers.
Continuity: the note typed in S01 (Clients) is pinned at the top of the job; the visit booked in
S01 (Fall cleanup · Thu Oct 15, 8:00 AM) is stop 1 on Owen's route."""
from suite import appview, toast, icon

ROUTE_SVG = """<svg width="100%" height="50" viewBox="0 0 544 54" preserveAspectRatio="none" style="display:block">
<path d="M28 27 L190 27 L354 27 L516 27" stroke="#12252F" stroke-width="3" stroke-dasharray="8 7" fill="none"/>
<circle cx="28" cy="27" r="22" fill="#C2185B"/><text x="28" y="35" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="22" fill="#fff">1</text>
<circle cx="190" cy="27" r="20" fill="#fff" stroke="#12252F" stroke-width="3"/><text x="190" y="35" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="21" fill="#12252F">2</text>
<circle cx="354" cy="27" r="20" fill="#fff" stroke="#12252F" stroke-width="3"/><text x="354" y="35" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="21" fill="#12252F">3</text>
<circle cx="516" cy="27" r="20" fill="#fff" stroke="#12252F" stroke-width="3"/><text x="516" y="35" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="21" fill="#12252F">4</text>
</svg>"""

LIST = f"""
<div class="inner">
 <div class="jb-day"><div><div class="ct" style="font-size:30px">Thu Oct 15</div><div class="cs" style="margin-top:2px">Owen Cleveland · Maya Ross</div></div>
  <div class="rr">4 stops<small>in route order</small></div></div>
 <div class="jb-route">{ROUTE_SVG}
  <div class="jb-towns"><span>Kentville</span><span>Kentville</span><span>Wolfville</span><span>New Minas</span></div></div>
 <div id="j-stops">
  <div class="row j-stop" id="j-dana"><div class="jb-n on">1</div><div><div class="rt">Dana Keddy</div><div class="rs">Fall cleanup · 14 Belcher St</div></div><div class="rr">8:00<small><span class="pill mag">Next</span></small></div></div>
  <div class="row j-stop"><div class="jb-n">2</div><div><div class="rt">Marcel Boudreau</div><div class="rs">Gutter clean · 88 Main St</div></div><div class="rr">10:30<small>AM</small></div></div>
  <div class="row j-stop"><div class="jb-n">3</div><div><div class="rt">Priya Sandhu</div><div class="rs">Aerate &amp; seed · 3 Orchard Ln</div></div><div class="rr">12:45<small>PM</small></div></div>
  <div class="row j-stop"><div class="jb-n">4</div><div><div class="rt">Lena Comeau</div><div class="rs">Leaf pickup · 57 Park St</div></div><div class="rr">2:30<small>PM</small></div></div>
 </div>
 <div class="tiles j-stop" style="margin-top:20px">
  <div class="tile"><div class="tl">Truck</div><div class="tv" style="font-size:32px">Truck 2</div><div class="cs" style="font-size:17px">Leaf vac + trailer</div></div>
  <div class="tile"><div class="tl">Booked on site</div><div class="tv" style="font-size:32px">6 h 45 m</div><div class="cs" style="font-size:17px">From Schedule</div></div>
 </div>
</div>"""

CHECKS = ["Rake and bag leaves", "Cut back perennials", "Clear leaves from beds", "Final mow and edge"]

JOB = f"""
<div id="j-scroll"><div class="inner" style="padding-top:20px">
 <div class="jb-head">
  <div><div class="k" style="font-size:16px">Stop 1 of 4 · 8:00 AM</div><div class="ct" style="font-size:32px;margin-top:4px">Fall cleanup</div>
   <div class="cs" style="margin-top:2px">Dana Keddy · 14 Belcher St</div></div>
  <div class="jb-timer" id="j-timer"><i></i><span id="j-clock">0:00:00</span></div>
 </div>
 <div class="jb-note" id="j-note">
  <div class="jb-pin">{icon('crm', 22, '#C2185B')}<span>Pinned from Clients</span></div>
  <div class="jb-nt">Gate code 4471. Dog in the back yard.</div>
  <div class="cs" style="font-size:18px;margin-top:6px">Added by the office · shows on every job here</div>
 </div>
 <div class="sl" style="display:flex;justify-content:space-between"><span>Checklist</span><span id="j-cnt" style="color:var(--slate)">0 / 4</span></div>
 <div class="prog" style="margin:0 0 4px"><i id="j-prog" style="transform:scaleX(0)"></i></div>
 {''.join(f'<div class="check" id="j-ck{i}"><div class="cb" id="j-cb{i}"></div><span class="jb-ct">{c}</span></div>' for i, c in enumerate(CHECKS))}
 <div class="sl">Photos</div>
 <div class="jb-photos">
  <div class="jb-slot" id="j-s0"><div class="jb-empty">{icon('plus', 34, '#2F4A56')}<span>Before</span></div>
   <div class="jb-ph jb-before" id="j-p0"><div class="jb-lab">Before · 8:04</div></div></div>
  <div class="jb-slot" id="j-s1"><div class="jb-empty">{icon('plus', 34, '#2F4A56')}<span>After</span></div>
   <div class="jb-ph jb-after" id="j-p1"><div class="jb-lab">After · 10:12</div></div></div>
 </div>
 <div class="btn" id="j-done">{icon('check', 30, '#F7F7F4')} Mark done</div>
 <div style="height:240px"></div>
</div></div>"""

DONE = f"""
<div class="inner">
 <div class="jb-dhead j-dn"><div class="jb-big">{icon('check', 46, '#fff')}</div>
  <div><div class="ct" style="font-size:34px">Job done</div><div class="cs">Dana Keddy · Fall cleanup · 10:16 AM</div></div></div>
 <div class="tiles j-dn" style="margin-top:22px">
  <div class="tile"><div class="tl">Time on job</div><div class="tv">2<small> h </small>14<small> m</small></div></div>
  <div class="tile"><div class="tl">Checklist</div><div class="tv">4 / 4</div></div>
 </div>
 <div class="sl j-dn">Photos · on Dana's timeline</div>
 <div class="jb-thumbs j-dn"><div class="jb-ph jb-before" style="opacity:1"></div><div class="jb-ph jb-after" style="opacity:1"></div></div>
 <div class="sl j-dn">Hours logged</div>
 <div class="row j-dn" style="padding:12px 0"><div class="av m" style="width:50px;height:50px;font-size:18px">OC</div><div><div class="rt" style="font-size:23px">Owen Cleveland</div></div><div class="rr">2 h 14 m</div></div>
 <div class="row j-dn" style="padding:12px 0"><div class="av l" style="width:50px;height:50px;font-size:18px">MR</div><div><div class="rt" style="font-size:23px">Maya Ross</div></div><div class="rr">2 h 14 m</div></div>
 </div>"""

CSS = r"""
.jb-day{display:flex;justify-content:space-between;align-items:center}
.jb-route{border:2px solid var(--ink);background:#fff;padding:14px 16px 10px;margin:16px 0 4px}
.jb-towns{display:flex;justify-content:space-between;font:600 15px 'DM Sans';letter-spacing:.06em;text-transform:uppercase;color:var(--slate);margin-top:6px}
.jb-n{width:46px;height:46px;flex:none;border:2.5px solid var(--ink);display:flex;align-items:center;justify-content:center;font:800 22px Manrope;background:#fff}
.jb-n.on{background:var(--mag);border-color:var(--mag);color:#fff}
#j-dana{transition:none}
.jb-head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.jb-timer{display:flex;align-items:center;gap:10px;background:var(--ink);color:var(--paper);font:800 23px Manrope;padding:10px 14px;margin-top:6px;white-space:nowrap}
.jb-timer i{width:12px;height:12px;border-radius:50%;background:var(--mag);display:block}
.jb-note{margin-top:18px;background:#fff;border:2px solid var(--ink);border-left:9px solid var(--mag);padding:14px 18px 14px;box-shadow:6px 6px 0 var(--mag)}
.jb-pin{display:flex;align-items:center;gap:8px;font:700 15px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:var(--mag)}
.jb-nt{font:800 27px/1.22 Manrope;margin-top:6px}
.jb-ct{transition:none}
.check.jb-ok .jb-ct{color:var(--slate);text-decoration:line-through;text-decoration-color:var(--mag);text-decoration-thickness:2px}
.jb-photos{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.jb-slot{position:relative;height:190px;border:2.5px dashed #9AA9B0;background:#FBFAF6}
.jb-empty{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;font:700 20px 'DM Sans';color:var(--slate)}
.jb-ph{position:absolute;inset:-2.5px;opacity:0;border:2px solid var(--ink)}
.jb-before{background-color:#5F7536;background-image:
 radial-gradient(circle at 30% 40%,#D9822B 0 7px,transparent 8px),radial-gradient(circle at 70% 60%,#A64B1C 0 6px,transparent 7px),
 radial-gradient(circle at 50% 20%,#E3A93A 0 5px,transparent 6px),radial-gradient(circle at 15% 80%,#B8642A 0 6px,transparent 7px);
 background-size:34px 30px,42px 38px,28px 34px,46px 40px;background-position:0 0,9px 13px,5px 3px,17px 7px}
.jb-after{background:repeating-linear-gradient(90deg,#5D8C3A 0 34px,#71A04A 34px 68px)}
.jb-before:before,.jb-after:before{content:"";position:absolute;left:0;right:0;top:0;height:44px;background:#8C6A44;
 background-image:repeating-linear-gradient(90deg,#8C6A44 0 22px,#6E5233 22px 25px);border-bottom:3px solid #5A4329}
.jb-lab{position:absolute;left:8px;bottom:8px;background:var(--ink);color:var(--paper);font:700 15px 'DM Sans';letter-spacing:.1em;text-transform:uppercase;padding:5px 9px}
.jb-dhead{display:flex;gap:18px;align-items:center}
.jb-big{width:80px;height:80px;flex:none;background:var(--mag);display:flex;align-items:center;justify-content:center}
.jb-thumbs{display:flex;gap:12px}
.jb-thumbs .jb-ph{position:relative;inset:auto;width:120px;height:84px}
.jb-thumbs .jb-ph:before{height:20px}
"""

JOBS = dict(
    name="S04_jobs-crew",
    kicker="Jobs · Crew app",
    hook="The crew knows the gate code before the truck pulls in.",
    end="A job app for the crew, built around the way your jobs already run.",
    caps=[(3.35, 6.35, "Today's jobs, in route order, on the crew lead's phone."),
          (6.35, 9.4, "The office note from Clients is pinned at the top."),
          (9.4, 12.3, "Tick the checklist. Add before and after photos."),
          (12.3, 15.5, "Mark it done. Hours are logged; Quotes drafts the invoice.")],
    css=CSS,
    screen=appview("v-list", "jobs", LIST, time="7:52", title="Today's jobs")
    + appview("v-job", "jobs", JOB, time="8:02", title="Jobs")
    + appview("v-done", "jobs", DONE, time="10:16", title="Jobs",
              extra=toast("j-toast", "quote", "Invoice drafted · INV-2232 from this job")),
    callouts="""<div class="callout" id="jco" style="left:96px;top:1300px"><div class="ck">One finished job feeds</div>
<div class="cr"><i>✓</i>Quotes (invoice draft)</div><div class="cr"><i>✓</i>Payroll (hours, for approval)</div><div class="cr"><i>✓</i>Clients (photos on the timeline)</div></div>""",
    js=r"""
const JCK=[9.35,9.75,10.15,10.55];
function zoomAt(t){const q=P(t,7.0,7.5,E.io)*(1-P(t,8.75,9.25,E.io));return {s:L(1,1.1,q),ox:320,oy:400}}
function clk(s){s=Math.floor(s);const h=Math.floor(s/3600),m=Math.floor(s/60)%60,x=s%60;return h+':'+String(m).padStart(2,'0')+':'+String(x).padStart(2,'0')}
function renderReel(t){
 // route list
 view('v-list',t,3.0,6.45);
 grow('.j-stop',t,3.55,.14,.45);
 const d=$('j-dana');d.style.background=(t>=5.85&&t<6.25)?'#FBE3EC':'transparent';
 // job
 view('v-job',t,6.3,13.3);
 const nq=P(t,6.6,6.95,E.back);S($('j-note'),{y:L(-18,0,nq),o:Math.min(1,nq*1.2)});
 $('j-clock').textContent=clk(L(0,8040,P(t,7.0,12.6,E.lin)));
 $('j-timer').querySelector('i').style.opacity=(Math.floor(t*2.5)%2===0)?1:.25;
 let n=0;JCK.forEach((a,i)=>{const on=t>=a+.05;if(on)n++;const cb=$('j-cb'+i);cb.classList.toggle('on',on);
  cb.innerHTML=on?'"""+icon('check', 24, '#fff').replace("'", "\\'")+r"""':'';$('j-ck'+i).classList.toggle('jb-ok',on);
  if(on){const s=L(.7,1,P(t,a+.05,a+.25,E.back));cb.style.transform=`scale(${s})`}else cb.style.transform='none'});
 $('j-cnt').textContent=n+' / 4';$('j-prog').style.transform=`scaleX(${n/4})`;
 [[11.65,'j-p0'],[12.05,'j-p1']].forEach(([a,id])=>{const q=P(t,a+.15,a+.4,E.back);S($(id),{s:L(.85,1,q),o:P(t,a+.15,a+.3)})});
 const b=$('j-done');const pr=t>=12.7&&t<12.9;b.style.transform=pr?'translate(3px,3px)':'none';b.style.boxShadow=pr?'none':'';
 // done
 view('v-done',t,13.1,15.9);
 grow('.j-dn',t,13.1,.07,.35);
 handoff(t,13.8,15.6,'j-toast');
 callout(t,13.6,15.45,'jco','j-toast');
 taps(t,[[5.85,'j-dana'],[9.35,'j-cb0'],[9.75,'j-cb1'],[10.15,'j-cb2'],[10.55,'j-cb3'],[11.65,'j-s0'],[12.05,'j-s1'],[12.7,'j-done']]);
}""")

ALL = [JOBS]
