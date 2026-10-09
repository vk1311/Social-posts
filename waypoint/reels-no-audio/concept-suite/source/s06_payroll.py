"""S06 — Payroll. Invented business Harlow & Pine; invented crew; made-up amounts (not real tax tables).
Story: pay period Oct 17–30. Hours arrive from Jobs, two flags are raised, Erin fixes a missed punch with a
note, checks one pay line, and nothing is paid until she taps Review and approve. Hand-off to Reports."""
from suite import appview, toast, icon

LIST = f"""
<div class="inner">
 <div class="py-period"><div><div class="tl">Pay period</div><div class="py-pd">Oct 17 – Oct 30</div></div>
  <div style="text-align:right"><div class="tl">Pay date</div><div class="py-pd">Nov 6</div></div></div>
 <div class="tiles" style="margin-top:16px">
  <div class="tile"><div class="tl">Hours from Jobs</div><div class="tv" id="py-tot">0.0</div></div>
  <div class="tile"><div class="tl">Flags to review</div><div class="tv" id="py-flags">0</div></div>
 </div>
 <div class="py-sync"><div class="py-synct" id="py-synct">{icon('jobs', 24, '#C2185B')}<span id="py-syncs">Pulling hours from Jobs…</span></div>
  <div class="prog"><i id="py-prog"></i></div></div>
 <div class="py-banner" id="py-banner"><b id="py-bn">2</b><span id="py-bt">flags to review before approval</span></div>
 <div id="py-rows">
  <div class="row py-row" id="py-owen"><div class="av m">OC</div><div><div class="rt">Owen Cleveland</div><div class="rs">From Jobs · 11 shifts</div>
   <div class="py-fl"><span class="pill mag py-flag" id="py-oflag">Overtime · 4.5 h</span></div></div><div class="rr py-h" data-h="84.5">0.0 h</div></div>
  <div class="row py-row"><div class="av l">MR</div><div><div class="rt">Maya Ross</div><div class="rs">From Jobs · 10 shifts</div></div><div class="rr py-h" data-h="76">0.0 h</div></div>
  <div class="row py-row" id="py-jordan"><div class="av">JL</div><div><div class="rt">Jordan Lantz</div><div class="rs" id="py-js">From Jobs · 10 shifts</div>
   <div class="py-fl"><span class="pill mag py-flag" id="py-jflag">Missed clock-out · Oct 22</span></div></div><div class="rr py-h" id="py-jh" data-h="68">0.0 h</div></div>
  <div class="row py-row"><div class="av l">TB</div><div><div class="rt">Theo Burgess</div><div class="rs">From Jobs · 7 shifts · first pay</div></div><div class="rr py-h" data-h="52">0.0 h</div></div>
 </div>
</div>"""

SHEET = f"""
<div class="py-dim" id="py-dim"></div>
<div class="py-sheet" id="py-sheet">
 <div class="py-grab"></div>
 <div class="k">Missed clock-out</div>
 <div class="ct" style="font-size:30px;margin-top:6px">Jordan Lantz · Thu Oct 22</div>
 <div class="cs">Belcher St job · punches from Jordan's phone</div>
 <div class="py-punch"><span>Clock in</span><b>7:30 AM</b></div>
 <div class="field" style="margin-top:14px"><label>Clock out</label><div class="input" id="py-out"></div></div>
 <div class="field"><label>Note · kept with the record</label><div class="py-note" id="py-note"></div></div>
 <div class="btn" id="py-save" style="margin-top:8px">{icon('check', 28, '#F7F7F4')} Save fix</div>
</div>"""

LINE = f"""
<div id="py-scroll"><div class="inner">
 <div class="py-back">‹ Pay run · Oct 17–30</div>
 <div style="display:flex;gap:18px;align-items:center;margin-top:14px">
  <div class="av m" style="width:76px;height:76px;font-size:27px">OC</div>
  <div><div class="ct" style="font-size:32px">Owen Cleveland</div><div class="cs">Crew lead · $26.00 an hour</div></div>
 </div>
 <div class="sl">Hours · from Jobs</div>
 <table class="items py-t">
  <tr class="py-l"><td>Regular · 80.0 h</td><td>$2,080.00</td></tr>
  <tr class="py-l"><td>Overtime · 4.5 h × 1.5</td><td>$175.50</td></tr>
  <tr class="tot py-l"><td>Gross</td><td>$2,255.50</td></tr>
 </table>
 <div class="check py-l" id="py-ot"><div class="cb" id="py-otcb"></div><div>Overtime checked<div class="py-cs">Oct 27 · storm cleanup, Wolfville</div></div></div>
 <div class="sl">Deductions · for review</div>
 <table class="items py-t" style="margin-top:0">
  <tr class="py-d"><td>CPP</td><td>– $126.19</td></tr>
  <tr class="py-d"><td>EI</td><td>– $36.76</td></tr>
  <tr class="py-d"><td>Income tax</td><td>– $338.33</td></tr>
  <tr class="tot py-d"><td>Net pay</td><td>$1,754.22</td></tr>
 </table>
 <div class="py-small">Worked out from the rates set up for this business. A person checks them.</div>
 <div class="btn" id="py-approve"><span id="py-apt">{icon('check', 30, '#F7F7F4')} Review and approve</span></div>
 <div class="py-small" id="py-aps">Nothing is paid until you approve · 4 pay lines · $6,637.50 gross</div>
 <div class="py-stubs" id="py-stubs">
  <div class="k" style="margin-bottom:10px">Pay stubs sent to phones</div>
  <div class="py-sg">
   <div class="py-st">{icon('phone', 22, '#C2185B')}Owen</div><div class="py-st">{icon('phone', 22, '#C2185B')}Maya</div>
   <div class="py-st">{icon('phone', 22, '#C2185B')}Jordan</div><div class="py-st">{icon('phone', 22, '#C2185B')}Theo</div>
  </div>
 </div>
 <div style="height:260px"></div>
</div></div>"""

CSS = r"""
.py-period{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid var(--ink);padding-bottom:14px}
.py-pd{font:800 30px Manrope;margin-top:4px}
.py-sync{margin:10px 0 4px}
.py-synct{display:flex;align-items:center;gap:10px;font:600 19px 'DM Sans';color:var(--slate)}
.py-banner{display:flex;align-items:center;gap:14px;background:var(--ink);color:var(--paper);padding:12px 18px;margin-top:14px;
 font:700 21px 'DM Sans';border-left:7px solid var(--mag);opacity:0}
.py-banner b{font:800 30px Manrope;color:#F4A7C4}
.py-row{padding:16px 0;align-items:flex-start}
.py-row .av{margin-top:2px}
.py-h{font:800 28px Manrope;padding-top:8px}
.py-fl{margin-top:8px;height:30px}
.py-flag{opacity:0;transform-origin:left center}
.py-dim{position:absolute;left:0;right:0;top:154px;bottom:224px;background:rgba(18,37,47,.45);opacity:0;z-index:7}
.py-sheet{position:absolute;left:0;right:0;bottom:224px;z-index:8;background:var(--paper);border-top:3px solid var(--ink);
 padding:14px 30px 28px;box-shadow:0 -8px 0 rgba(194,24,91,.9);opacity:0}
.py-grab{width:80px;height:7px;background:#C9C3B6;margin:0 auto 16px}
.py-punch{display:flex;justify-content:space-between;align-items:center;margin-top:18px;padding:14px 18px;background:#ECEEEC;
 font:600 22px 'DM Sans';color:var(--slate)}
.py-punch b{font:800 25px Manrope;color:var(--ink)}
.py-note{min-height:96px;border:2px solid var(--ink);background:#fff;padding:12px 18px;font:500 23px/1.35 'DM Sans'}
.py-note.on{border-color:var(--mag);box-shadow:4px 4px 0 var(--mag)}
.py-back{font:600 21px 'DM Sans';color:var(--mag)}
.py-t{margin-top:0;font-size:22px}
.py-t td{padding:12px 16px}
.py-t tr.tot td{font-size:26px}
.py-cs{font:400 18px 'DM Sans';color:var(--slate);margin-top:2px}
.py-small{font:400 18px/1.4 'DM Sans';color:var(--slate);margin-top:12px}
.py-stubs{margin-top:22px;border:2px solid var(--ink);background:#fff;padding:16px 18px;opacity:0}
.py-sg{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.py-st{display:flex;align-items:center;gap:10px;font:700 22px Manrope;padding:8px 10px;background:#FBE3EC;opacity:0}
"""

PAY = dict(
    name="S06_payroll",
    kicker="Payroll · Pay runs",
    hook="Two weeks of crew hours, checked before anyone gets paid.",
    end="Pay runs that follow your crew's real hours, built around the way you already do payroll.",
    caps=[(3.35, 6.2, "Hours come in from the Jobs app, per crew member."),
          (6.2, 8.9, "Two flags for review: a missed clock-out and overtime."),
          (8.9, 11.9, "Erin fixes the punch and leaves a note on the record."),
          (11.9, 15.4, "Deductions listed for review. Nothing is paid until she approves.")],
    css=CSS,
    screen=appview("py-list", "pay", LIST, time="4:02", title="Payroll", extra=SHEET)
    + appview("py-line", "pay", LINE, time="4:11", title="Payroll",
              extra=toast("py-toast", "rep", "Pay run Oct 17–30 · labour by job")),
    callouts="""<div class="callout" id="py-co" style="left:96px;top:1420px"><div class="ck">Approved pay run, used by</div>
<div class="cr"><i>✓</i>People (stubs on file)</div><div class="cr"><i>✓</i>Reports (labour by job)</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,8.0,8.5,E.io)*(1-P(t,9.95,10.4,E.io));return {s:L(1,1.07,q),ox:320,oy:1000}}
const hfmt=v=>v.toFixed(1)+' h';
function renderReel(t){
 // ---- view 1: pay run list ----
 view('py-list',t,3.0,11.8);
 const rows=[...document.querySelectorAll('.py-h')];
 rows.forEach((el,i)=>{const a=3.75+i*.32;countUp(el,t,a,a+1.0,+el.dataset.h,hfmt)});
 grow('.py-row',t,3.45,.1,.4);
 const jfix=P(t,10.6,11.0);const jh=$('py-jh');if(t>10.6)jh.textContent=hfmt(68+8*jfix);
 const totA=280.5*P(t,3.75,5.95,E.out);$('py-tot').textContent=(t<10.6?totA:280.5+8*jfix).toFixed(1);
 $('py-prog').style.transform=`scaleX(${P(t,3.6,5.7,E.io)})`;
 $('py-syncs').textContent=t<5.7?'Pulling hours from Jobs…':'4 of 4 crew · synced from Jobs 4:02 PM';
 // flags
 const of=P(t,5.85,6.2,E.back),jf=P(t,6.05,6.4,E.back);
 S($('py-oflag'),{s:L(.6,1,of),o:of});S($('py-jflag'),{s:L(.6,1,jf),o:jf});
 const nf=t<5.85?0:(t<6.05?1:(t<10.6?2:1));$('py-flags').textContent=nf;
 const bn=P(t,6.3,6.65);S($('py-banner'),{y:L(-12,0,bn),o:bn});
 const fixed=t>=10.6;$('py-bn').textContent=fixed?'1':'2';
 $('py-bt').textContent=fixed?"flag left · Owen's overtime":'flags to review before approval';
 const jfl=$('py-jflag');jfl.textContent=fixed?'Fixed · note added':'Missed clock-out · Oct 22';
 jfl.className='pill py-flag '+(fixed?'ok':'mag');
 $('py-js').textContent=fixed?'Oct 22 out 4:00 PM · note by Erin':'From Jobs · 10 shifts';
 // sheet
 const so=P(t,7.35,7.75,E.out)*(1-P(t,10.35,10.7,E.in));
 S($('py-sheet'),{y:L(640,0,so),o:t>7.35&&t<10.7?1:0});$('py-dim').style.opacity=so;
 const out=$('py-out');
 if(t<10.0){typeInto(out,'4:00 PM',t,8.15,8.55);out.classList.toggle('on',t>7.95&&t<8.75)}
 else{out.innerHTML='4:00 PM';out.classList.remove('on')}
 if(t<8.0)out.innerHTML='';
 const note=$('py-note');
 typeInto(note,'Phone died on site. Owen confirmed she left at 4.',t,8.95,9.9);note.classList.toggle('on',t>8.75&&t<10.15);
 if(t>=10.15)note.innerHTML=esc('Phone died on site. Owen confirmed she left at 4.');
 const sv=$('py-save');const pr=t>=10.2&&t<10.4;sv.style.transform=pr?'translate(3px,3px)':'none';sv.style.boxShadow=pr?'none':'';
 // ---- view 2: Owen's pay line ----
 view('py-line',t,11.55,15.9);
 grow('.py-l',t,11.75,.1,.4);grow('.py-d',t,12.15,.12,.4);
 const ck=t>=12.6;const cb=$('py-otcb');cb.classList.toggle('on',ck);cb.innerHTML=ck?'<svg width="24" height="24" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3"/></svg>':'';
 scrollTo($('py-scroll'),t,12.95,13.55,450);
 const ap=$('py-approve');const apr=t>=13.9&&t<14.1;ap.style.transform=apr?'translate(3px,3px)':'none';
 const done=t>=14.1;ap.style.background=done?'var(--mag)':'';ap.style.boxShadow=apr?'none':(done?'5px 5px 0 var(--ink)':'');
 $('py-apt').innerHTML=done?'<svg width="30" height="30" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#F7F7F4" stroke-width="2.8"/></svg> Approved by Erin · 4:12 PM':'<svg width="30" height="30" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#F7F7F4" stroke-width="2.8"/></svg> Review and approve';
 $('py-aps').textContent=done?'4 pay lines approved · $6,637.50 gross':'Nothing is paid until you approve · 4 pay lines · $6,637.50 gross';
 const st=P(t,14.15,14.45);S($('py-stubs'),{y:L(20,0,st),o:st});grow('.py-st',t,14.25,.08,.25);
 handoff(t,14.5,15.6,'py-toast');

 // taps: correct for the phone zoom (rel() measures scaled px; the tap layer lives in unscaled screen px)
 const zs=zoomAt(t).s;const tl=[[7.0,'py-jflag'],[7.95,'py-out'],[8.75,'py-note'],[10.2,'py-save'],[11.15,'py-owen'],[12.6,'py-otcb'],[13.9,'py-approve']]
  .map(k=>{const r=rel($(k[1]));return [k[0],k[1],r.x/zs-r.x,r.y/zs-r.y]});
 taps(t,tl);
}""")

ALL = [PAY]
