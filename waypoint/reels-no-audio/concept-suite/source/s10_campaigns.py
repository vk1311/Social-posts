"""S10 — Campaigns (email). Invented business Harlow & Pine; invented clients; made-up counts.
Segment built from Clients (fall cleanup 2026 AND no winter contract) -> CASL consent-on-file filter
leaves out clients without consent -> draft with a first-name merge field -> phone preview ->
schedule Tue Oct 20, 7:30 AM -> replies routed to Helpdesk -> hand-off toast to Clients.
No open/click/revenue numbers anywhere (mechanisms, not outcomes)."""
from suite import appview, toast, icon

CHECK_W = icon('check', 22, '#F7F7F4')
CHECK_M = icon('check', 22, '#C2185B')
DOCK = ("crm", "jobs", "mail", "rep", "more")

CSS = r"""
.cp-src{display:flex;align-items:center;gap:10px;font:600 18px 'DM Sans';color:var(--slate)}
.cp-src b{color:var(--ink)}
.cp-rule{display:flex;align-items:center;gap:14px;height:76px;border:2px solid var(--ink);background:#fff;padding:0 18px}
.cp-rk{font:600 14px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:var(--slate);width:96px;line-height:1.2;flex:none}
.cp-rv{font:700 22px/1.2 Manrope}
.cp-rv em{font-style:normal;color:var(--mag)}
.cp-and{font:700 15px 'DM Sans';letter-spacing:.2em;color:var(--mag);padding:6px 0 6px 18px}
.cp-slot{position:relative;height:76px}
.cp-slot .cp-rule{position:absolute;left:0;right:0;top:0;opacity:0}
.cp-add{position:absolute;left:0;right:0;top:0;height:76px;border:2px dashed #A9B4B8;display:flex;align-items:center;justify-content:center;gap:10px;
 font:600 21px 'DM Sans';color:var(--slate)}
.cp-chips{display:flex;gap:10px;align-items:center}
.cp-chip{display:flex;align-items:center;gap:10px;font:700 20px 'DM Sans';padding:11px 16px 10px 12px;border:2px solid #A9B4B8;background:#fff;color:var(--slate)}
.cp-chip .cp-box{width:26px;height:26px;border:2.5px solid #A9B4B8;display:flex;align-items:center;justify-content:center;background:#fff}
.cp-chip.on{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.cp-chip.on .cp-box{background:var(--mag);border-color:var(--mag)}
.cp-law{font:500 17px 'DM Sans';color:var(--slate);margin-top:10px}
.cp-count{display:flex;align-items:center;gap:18px;border:2px solid var(--ink);background:#fff;padding:14px 20px;margin-top:20px;box-shadow:6px 6px 0 var(--mag)}
.cp-num{font:800 58px/1 Manrope;letter-spacing:-.02em;min-width:76px}
.cp-cl{font:700 22px Manrope}
.cp-cs{font:500 18px 'DM Sans';color:#9E1149;margin-top:3px;opacity:0}
.cp-row{display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1.5px solid #E3DED2}
.cp-row .av{width:50px;height:50px;font-size:18px}
.cp-row .rt{font-size:22px}.cp-row .rs{font-size:17px}
.cp-out .rt{position:relative}
.cp-strike{position:absolute;left:0;top:52%;height:2.5px;background:var(--ink);width:100%;transform-origin:left center;transform:scaleX(0)}
.cp-act{position:absolute;left:0;right:0;bottom:224px;padding:14px 30px 18px;background:var(--paper);border-top:2px solid var(--ink);z-index:5}
.cp-act .btn{margin-top:0}
/* draft */
.cp-to{display:flex;align-items:center;gap:10px;font:600 19px 'DM Sans';color:var(--slate);margin:4px 0 18px}
.cp-to b{color:var(--ink)}
.cp-body{border:2px solid var(--ink);background:#fff;padding:16px 18px;font:400 21px/1.42 'DM Sans'}
.cp-body p{margin-bottom:10px}
.cp-tok{display:inline-block;background:#FBE3EC;color:#9E1149;font:700 19px 'DM Sans';padding:1px 8px;border:2px solid #F4A7C4}
.cp-foot{font:500 15px/1.4 'DM Sans';color:var(--slate);border-top:1.5px solid #E3DED2;padding-top:8px;margin-top:4px}
.cp-foot u{color:var(--mag)}
.cp-tools{display:flex;gap:12px;margin-top:16px}
.cp-tools .btn{margin-top:0}
/* preview overlay */
.cp-ov{position:absolute;left:0;right:0;top:154px;bottom:224px;background:#E6E0D3;z-index:7;opacity:0;padding:20px 30px}
.cp-ovk{display:flex;justify-content:space-between;align-items:center;font:600 16px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--mag)}
.cp-ovk span:last-child{color:var(--slate);letter-spacing:.08em}
.cp-mini{position:relative;width:400px;height:770px;margin:18px auto 0;border:12px solid #12252F;border-radius:46px;background:#fff;overflow:hidden;
 box-shadow:8px 8px 0 rgba(18,37,47,.25)}
.cp-mini:before{content:"";position:absolute;left:135px;top:8px;width:106px;height:26px;border-radius:14px;background:#12252F}
.cp-msb{display:flex;justify-content:space-between;font:700 15px 'DM Sans';padding:12px 28px 0}
.cp-mh{padding:26px 22px 12px;border-bottom:1.5px solid #E3DED2}
.cp-mfrom{display:flex;align-items:center;gap:10px}
.cp-mfrom .mono{width:40px;height:40px;font-size:15px}
.cp-mfn{font:700 18px 'DM Sans'}.cp-mft{font:400 15px 'DM Sans';color:var(--slate)}
.cp-msub{font:800 22px/1.25 Manrope;margin-top:12px}
.cp-mb{padding:14px 22px;font:400 17px/1.45 'DM Sans';color:var(--ink)}
.cp-mb p{margin-bottom:10px}
.cp-hi{font:700 19px Manrope;position:relative;height:28px;margin-bottom:8px}
.cp-hi span{position:absolute;left:0;top:0;background:#FBE3EC;padding:0 4px}
.cp-mbtn{background:var(--ink);color:var(--paper);font:700 16px Manrope;text-align:center;padding:12px;margin:4px 0 12px}
.cp-mf{font:400 13px/1.4 'DM Sans';color:var(--slate);border-top:1.5px solid #E3DED2;padding-top:8px}
.cp-mf u{color:var(--mag)}
/* schedule */
.cp-opts{display:flex;gap:12px}
.cp-opt{flex:1;border:2px solid #A9B4B8;background:#fff;padding:14px 16px;font:700 21px Manrope;color:var(--slate)}
.cp-opt small{display:block;font:400 16px 'DM Sans';margin-top:2px}
.cp-opt.on{border-color:var(--ink);color:var(--ink);box-shadow:5px 5px 0 var(--mag)}
.cp-days{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:14px}
.cp-day{height:86px;border:2px solid var(--ink);background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.cp-day span{font:600 14px 'DM Sans';letter-spacing:.12em;text-transform:uppercase;color:var(--slate)}
.cp-day b{font:800 28px Manrope}
.cp-day.on{background:var(--mag);border-color:var(--mag)}.cp-day.on span,.cp-day.on b{color:#fff}
.cp-time{display:flex;align-items:center;gap:12px;margin-top:12px;height:62px;border:2px solid var(--ink);background:#fff;padding:0 18px;font:700 24px Manrope;opacity:.35}
.cp-time small{margin-left:auto;font:500 17px 'DM Sans';color:var(--slate)}
.cp-rep{display:flex;gap:14px;align-items:center;border:2px solid var(--ink);background:#fff;padding:14px 18px;border-left:7px solid var(--mag)}
.cp-repi{width:48px;height:48px;flex:none;background:var(--ink);display:flex;align-items:center;justify-content:center}
.cp-rept{font:700 21px/1.3 Manrope}.cp-reps{font:400 17px 'DM Sans';color:var(--slate);margin-top:2px}
.cp-ck{display:flex;gap:12px;align-items:center;padding:9px 0;font:600 19px 'DM Sans'}
.cp-ck i{width:30px;height:30px;flex:none;background:var(--mag);display:flex;align-items:center;justify-content:center}
.cp-bw{position:relative;height:78px;margin-top:18px}
.cp-bw .btn{position:absolute;left:0;right:0;top:0;margin-top:0}
.cp-done{background:#2F4A56;opacity:0}
"""

SEG = f"""
<div class="inner">
 <div class="cp-src">{icon('crm', 24, '#C2185B')}<span>Built from <b>Clients</b> · 214 contacts</span></div>
 <div class="sl" style="margin-top:16px">Who gets it</div>
 <div class="cp-rule"><div class="cp-rk">Job history</div><div class="cp-rv">Had a <em>fall cleanup</em> in 2026</div></div>
 <div class="cp-and" id="cp-and">AND</div>
 <div class="cp-slot">
  <div class="cp-add" id="cp-add">{icon('plus', 24)} Add a rule</div>
  <div class="cp-rule" id="cp-r2"><div class="cp-rk">Contracts</div><div class="cp-rv"><em>No</em> winter snow contract</div></div>
 </div>
 <div class="sl">Email rules · CASL</div>
 <div class="cp-chips"><div class="cp-chip" id="cp-chip"><div class="cp-box" id="cp-box"></div>Consent on file</div></div>
 <div class="cp-law">Canada's anti-spam law: only email clients who said yes.</div>
 <div class="cp-count"><div class="cp-num" id="cp-num">41</div>
  <div><div class="cp-cl">clients match</div><div class="cp-cs" id="cp-cs">8 left out · no consent on file</div></div></div>
 <div class="sl">Preview</div>
 <div class="cp-row"><div class="av">MB</div><div><div class="rt">Marcel Boudreau</div><div class="rs">Consent on file · Jun 2025</div></div><div class="rr"><span class="pill ghost">In</span></div></div>
 <div class="cp-row cp-out" id="cp-jw"><div class="av l">JW</div><div><div class="rt">Jack Whynot<i class="cp-strike" id="cp-strike"></i></div><div class="rs">No consent on file</div></div><div class="rr"><span class="pill ghost" id="cp-jwp">In</span></div></div>
 <div class="cp-row"><div class="av m">LC</div><div><div class="rt">Lena Comeau</div><div class="rs">Consent on file · May 2026</div></div><div class="rr"><span class="pill ghost">In</span></div></div>
</div>"""

SEG_ACT = f"""<div class="cp-act"><div class="btn" id="cp-draft">{icon('mail', 30, '#F7F7F4')} Draft email to <span id="cp-n2">41</span></div></div>"""

DRAFT = f"""
<div class="inner">
 <div class="qt-no" style="font:600 17px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--mag)">Draft · Winter snow 2026</div>
 <div class="cp-to">{icon('crm', 22, '#2F4A56')}<span>To <b>23 clients</b> · consent on file</span></div>
 <div class="field"><label>Subject</label><div class="input" id="cp-subj"></div></div>
 <div class="field"><label>Message</label>
 <div class="cp-body">
  <p class="cp-p">Hi <span class="cp-tok" id="cp-tok">First name</span>,</p>
  <p class="cp-p">Thanks for having us for your fall cleanup. Want the same crew on your driveway this winter?</p>
  <p class="cp-p">Full-season plowing and walkway salting, Nov to Apr. Just reply and Sam will set it up.</p>
  <p class="cp-p">Erin Harlow, Harlow &amp; Pine</p>
  <div class="cp-foot cp-p">Harlow &amp; Pine Property Services · Kentville, NS · <u>Unsubscribe</u></div>
 </div></div>
 <div class="cp-tools"><div class="btn sm ghost" id="cp-prev">{icon('phone', 24)} Preview on phone</div></div>
</div>"""

MINI = f"""
<div class="cp-ov" id="cp-ov">
 <div class="cp-ovk"><span>Preview</span><span id="cp-as">as Marcel Boudreau · 1 of 23</span></div>
 <div class="cp-mini" id="cp-mini">
  <div class="cp-msb"><span>7:30</span><span>●●●</span></div>
  <div class="cp-mh">
   <div class="cp-mfrom"><div class="mono">H&amp;P</div><div><div class="cp-mfn">Harlow &amp; Pine</div><div class="cp-mft">Tue Oct 20 · 7:30 AM</div></div></div>
   <div class="cp-msub">Your driveway this winter</div>
  </div>
  <div class="cp-mb">
   <div class="cp-hi"><span id="cp-hi1">Hi Marcel,</span><span id="cp-hi2" style="opacity:0">Hi Lena,</span></div>
   <p>Thanks for having us for your fall cleanup. Want the same crew on your driveway this winter?</p>
   <p>Full-season plowing and walkway salting, Nov to Apr. Just reply and Sam will set it up.</p>
   <div class="cp-mbtn">Reply to Harlow &amp; Pine</div>
   <p>Erin Harlow, Harlow &amp; Pine</p>
   <div class="cp-mf">Harlow &amp; Pine Property Services · Kentville, NS<br><u>Unsubscribe</u></div>
  </div>
 </div>
</div>"""

SCHED = f"""
<div class="inner">
 <div class="qt-no" style="font:600 17px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--mag)">Winter snow 2026 · 23 clients</div>
 <div class="ct" style="margin-top:6px">Your driveway this winter</div>
 <div class="sl">When</div>
 <div class="cp-opts"><div class="cp-opt">Send now<small>Right away</small></div><div class="cp-opt on">Schedule<small>Pick a day + time</small></div></div>
 <div class="cp-days">
  <div class="cp-day"><span>Mon</span><b>19</b></div>
  <div class="cp-day" id="cp-tue"><span>Tue</span><b>20</b></div>
  <div class="cp-day"><span>Wed</span><b>21</b></div>
  <div class="cp-day"><span>Thu</span><b>22</b></div>
  <div class="cp-day"><span>Fri</span><b>23</b></div>
 </div>
 <div class="cp-time" id="cp-time">{icon('cal', 26)} 7:30 AM<small>before crews head out</small></div>
 <div class="sl">Replies</div>
 <div class="cp-rep"><div class="cp-repi">{icon('help', 28, '#F7F7F4')}</div>
  <div><div class="cp-rept">Replies go to Helpdesk</div><div class="cp-reps">and onto each client's timeline in Clients</div></div></div>
 <div class="sl">Before it goes</div>
 <div class="cp-ck cp-g"><i>{CHECK_W}</i>Only clients with consent on file</div>
 <div class="cp-ck cp-g"><i>{CHECK_W}</i>Unsubscribe link in the footer</div>
 <div class="cp-ck cp-g"><i>{CHECK_W}</i>Sender name + mailing address shown</div>
 <div class="cp-bw"><div class="btn" id="cp-sch">{icon('cal', 28, '#F7F7F4')} Schedule for 23</div>
  <div class="btn cp-done" id="cp-done">{icon('check', 28, '#F7F7F4')} Scheduled · Tue Oct 20, 7:30 AM</div></div>
</div>"""

CAMP = dict(
    name="S10_campaigns-email",
    kicker="Campaigns · Email",
    hook="Who had a fall cleanup but no snow contract yet?",
    end="Email campaigns that start from your own client list, set up the way you already talk to customers.",
    caps=[(3.35, 6.4, "Pick who gets it: fall cleanup, no winter contract."),
          (6.4, 9.4, "Consent on file only. Everyone else is left out."),
          (9.4, 12.4, "Write it once. Each client sees their own first name."),
          (12.4, 15.5, "Schedule Tuesday 7:30 AM. Replies come back to Helpdesk.")],
    css=CSS,
    screen=appview("v-seg", "crm", SEG, time="8:12", title="New segment", dock_keys=DOCK, extra=SEG_ACT)
    + appview("v-draft", "mail", DRAFT, time="8:14", title="Campaigns", dock_keys=DOCK, extra=MINI)
    + appview("v-sch", "mail", SCHED, time="8:16", title="Campaigns", dock_keys=DOCK,
              extra=toast("cp-toast", "crm", "Campaign logged on 23 client timelines")),
    callouts="""<div class="callout" id="cp-co" style="left:96px;top:1232px"><div class="ck">One campaign, used by</div>
<div class="cr"><i>✓</i>Clients · 23 timelines</div><div class="cr"><i>✓</i>Helpdesk · replies</div><div class="cr"><i>✓</i>Quotes · winter quotes</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,11.35,11.75,E.io)*(1-P(t,12.25,12.6,E.io));return {s:L(1,1.06,q),ox:320,oy:520}}
function press(el,on){el.style.transform=on?'translate(3px,3px)':'none';el.style.boxShadow=on?'none':''}
function renderReel(t){
 // ---- 1. segment from Clients
 view('v-seg',t,3.0,9.15);
 const r2=P(t,4.6,4.95,E.back);S($('cp-r2'),{y:L(-14,0,r2),o:P(t,4.6,4.8)});
 $('cp-add').style.opacity=1-P(t,4.5,4.65);
 $('cp-add').style.background=`rgba(251,227,236,${W(t,4.15,4.6,.12)})`;
 const on=t>=6.8;$('cp-chip').classList.toggle('on',on);$('cp-box').innerHTML=on?CHKW:'';
 let n=41;if(t>=4.8)n=Math.round(L(41,31,P(t,4.8,5.35)));if(t>=7.05)n=Math.round(L(31,23,P(t,7.05,7.6)));
 $('cp-num').textContent=n;$('cp-n2').textContent=n;
 S($('cp-cs'),{x:L(-12,0,P(t,7.2,7.55)),o:P(t,7.2,7.55)});
 const ex=P(t,7.15,7.5);$('cp-jw').style.opacity=L(1,.45,ex);$('cp-strike').style.transform=`scaleX(${P(t,7.15,7.5,E.io)})`;
 const jp=$('cp-jwp');jp.textContent=t>=7.2?'Left out':'In';jp.className='pill '+(t>=7.2?'soft':'ghost');
 press($('cp-draft'),t>=8.5&&t<8.7);
 // ---- 2. draft + phone preview
 view('v-draft',t,8.9,12.85);
 const sj=$('cp-subj');typeInto(sj,'Your driveway this winter',t,9.35,10.15);sj.classList.toggle('on',t>9.15&&t<10.5);
 grow('.cp-p',t,10.2,.14,.35);
 const tk=W(t,10.4,10.95,.15);$('cp-tok').style.boxShadow=`${4*tk}px ${4*tk}px 0 var(--mag)`;
 press($('cp-prev'),t>=11.0&&t<11.2);
 const ov=P(t,11.25,11.6,E.out);S($('cp-mini'),{y:L(120,0,ov),o:1});
 $('cp-ov').style.opacity=P(t,11.25,11.45);
 $('cp-hi1').style.opacity=1-P(t,11.85,11.95);$('cp-hi2').style.opacity=P(t,11.95,12.07);
 $('cp-as').textContent=t<11.95?'as Marcel Boudreau · 1 of 23':'as Lena Comeau · 2 of 23';
 // ---- 3. schedule
 view('v-sch',t,12.6,15.9);
 const tu=t>=13.0;$('cp-tue').classList.toggle('on',tu);
 const tm=P(t,13.05,13.3);$('cp-time').style.opacity=L(.35,1,tm);$('cp-time').style.borderColor=tu?'var(--mag)':'';
 grow('.cp-g',t,12.85,.12,.3);
 press($('cp-sch'),t>=13.55&&t<13.75);
 const dn=P(t,13.7,13.95);$('cp-sch').style.opacity=1-dn;S($('cp-done'),{y:L(10,0,dn),o:dn});
 handoff(t,13.85,15.6,'cp-toast');
 callout(t,14.0,15.45,'cp-co','cp-toast');
 taps(t,[[4.2,'cp-add'],[6.75,'cp-chip'],[8.5,'cp-draft'],[11.0,'cp-prev'],[13.0,'cp-tue'],[13.55,'cp-sch']]);
}""".replace("CHKW", repr(CHECK_W)))

ALL = [CAMP]
