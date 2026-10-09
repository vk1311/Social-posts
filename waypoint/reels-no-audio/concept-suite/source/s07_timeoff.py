"""S07 — Time off (leave). Invented business Harlow & Pine; invented crew Maya Ross, Erin Harlow; made-up balances."""
from suite import appview, toast, icon

CSS = r"""
.to-who{display:flex;align-items:center;gap:14px;margin-bottom:18px}
.to-who .av{width:52px;height:52px;font-size:19px}
.to-whot{font:700 23px Manrope}.to-whos{font:400 18px 'DM Sans';color:var(--slate)}
.to-chips{display:flex;gap:10px}
.to-chip{font:700 19px 'DM Sans';padding:11px 16px 10px;border:2px solid #C9C3B6;color:var(--slate);background:#fff}
.to-chip.on{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.to-strip{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}
.to-day{height:96px;border:2px solid var(--ink);background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.to-day b{font:800 30px Manrope}.to-day span{font:600 15px 'DM Sans';letter-spacing:.12em;text-transform:uppercase;color:var(--slate)}
.to-day.we{border-color:#D6D0C3;background:#F2ECE0}.to-day.we b,.to-day.we span{color:#A9B4B8}
.to-day.sel{background:var(--mag);border-color:var(--mag)}.to-day.sel b,.to-day.sel span{color:#fff}
.to-sum{border:2px solid var(--ink);background:#fff;padding:16px 20px;margin-top:18px;border-left:7px solid var(--mag);opacity:0}
.to-sumt{font:800 24px Manrope}.to-sums{font:400 19px 'DM Sans';color:var(--slate);margin-top:4px}
.to-sums b{color:var(--ink)}
.btn.to-sent{background:#2F4A56}
/* approval */
.to-req{border:2px solid var(--ink);background:#fff;padding:16px 18px;box-shadow:6px 6px 0 var(--mag)}
.to-reqh{display:flex;align-items:center;gap:14px}
.to-reqh .av{width:54px;height:54px;font-size:19px}
.to-reqd{font:400 19px/1.4 'DM Sans';color:var(--slate);margin-top:10px}
.to-reqd b{color:var(--ink);font-weight:700}
.to-grid{position:relative;border:2px solid var(--ink);background:#fff}
.to-gr{display:grid;grid-template-columns:118px repeat(5,1fr);border-top:1.5px solid #E3DED2;height:58px;align-items:center}
.to-gr:first-child{border-top:none}
.to-gr.hd{height:54px;background:#F2ECE0}
.to-gn{font:700 19px Manrope;padding-left:12px;white-space:nowrap}
.to-gh{text-align:center;font:600 14px 'DM Sans';letter-spacing:.08em;text-transform:uppercase;color:var(--slate);line-height:1.15}
.to-gh b{display:block;font:800 21px Manrope;color:var(--ink);letter-spacing:0}
.to-c{height:42px;margin:0 3px;display:flex;align-items:center;justify-content:center;font:700 14px 'DM Sans';letter-spacing:.08em;text-transform:uppercase}
.to-c.off{background:#2F4A56;color:#fff}
.to-c.req{border:2.5px dashed var(--mag);color:var(--mag);background:#FBE3EC}
.to-c.ok{background:var(--mag);color:#fff;border:none}
.to-c.to-evc{background:#12252F;color:#F4A7C4;font-size:13px;letter-spacing:.04em;white-space:nowrap}
.to-col{position:absolute;top:-4px;bottom:-4px;border:4px solid var(--mag);opacity:0;pointer-events:none}
.to-flag{border:2px solid var(--ink);background:#fff;padding:14px 18px;margin-top:16px;display:flex;gap:14px;align-items:flex-start;opacity:0}
.to-flagi{width:40px;height:40px;flex:none;background:var(--ink);display:flex;align-items:center;justify-content:center;margin-top:2px}
.to-acts{display:flex;gap:14px;margin-top:20px}
.to-acts .btn{margin-top:0}
.to-legend{display:flex;gap:18px;margin-top:10px;font:500 16px 'DM Sans';color:var(--slate)}
.to-legend i{display:inline-block;width:16px;height:16px;margin-right:6px;vertical-align:-2px}
/* done */
.to-note{border:2px solid var(--ink);background:var(--ink);color:var(--paper);padding:16px 18px;display:flex;gap:14px;align-items:center;opacity:0}
.to-noteic{width:48px;height:48px;flex:none;background:var(--mag);display:flex;align-items:center;justify-content:center}
.to-notek{font:600 15px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:#F4A7C4}
.to-notet{font:700 22px/1.3 Manrope;margin-top:2px}
.to-was{font:500 18px 'DM Sans';color:var(--slate);margin-top:4px;text-decoration:line-through;opacity:0}
"""

WEEK = [("Mon", 9), ("Tue", 10), ("Wed", 11), ("Thu", 12), ("Fri", 13), ("Sat", 14), ("Sun", 15)]
STRIP = "".join(
    f'<div class="to-day{" we" if d in ("Sat", "Sun") else ""}" id="to-d{n}"><span>{d}</span><b>{n}</b></div>' for d, n in WEEK)

REQ = f"""
<div class="inner">
 <div class="to-who"><div class="av m">MR</div><div><div class="to-whot">Maya Ross</div><div class="to-whos">Crew · Kentville yard</div></div></div>
 <div class="tiles">
  <div class="tile"><div class="tl">Vacation left</div><div class="tv">6.5 <small>days</small></div></div>
  <div class="tile"><div class="tl">Sick days left</div><div class="tv">3 <small>days</small></div></div>
 </div>
 <div class="sl">Type</div>
 <div class="to-chips"><div class="to-chip on">Vacation</div><div class="to-chip">Sick</div><div class="to-chip">Unpaid</div><div class="to-chip">Other</div></div>
 <div class="sl">Pick days · November</div>
 <div class="to-strip">{STRIP}</div>
 <div class="to-sum" id="to-sum"><div class="to-sumt">Thu Nov 12 – Fri Nov 13 · 2 days</div>
  <div class="to-sums">Vacation left after: <b>4.5 days</b></div></div>
 <div class="btn" id="to-send"><span id="to-sendtxt">Send to Erin</span></div>
 <div class="sl">Your requests</div>
 <div class="row"><div class="av l">{icon('leave', 28, '#fff')}</div><div><div class="rt">Aug 17 – 21</div><div class="rs">Vacation · 5 days</div></div><div class="rr"><span class="pill ghost">Taken</span></div></div>
</div>"""


def cell(kind, text, cid=""):
    i = f' id="{cid}"' if cid else ""
    return f'<div class="to-c {kind}"{i}>{text}</div>' if kind else "<div></div>"


GRID_ROWS = [
    ("Events", ["", "", "", ("to-evc", "Prep day", "to-ev"), ""]),
    ("Owen C.", ["", "", "", "", ""]),
    ("Maya R.", ["", "", "", ("req", "Asked", "to-m12"), ("req", "Asked", "to-m13")]),
    ("Jordan L.", [("off", "Off"), ("off", "Off"), "", "", ""]),
    ("Theo B.", ["", "", "", "", ""]),
]


def grid():
    out = ['<div class="to-grid" id="to-grid"><div class="to-col" id="to-col"></div>',
           '<div class="to-gr hd"><div></div>' + "".join(f'<div class="to-gh">{d}<b>{n}</b></div>' for d, n in WEEK[:5]) + '</div>']
    for name, cells in GRID_ROWS:
        cs = "".join(cell(*c) if c else "<div></div>" for c in cells)
        out.append(f'<div class="to-gr to-row"><div class="to-gn">{name}</div>{cs}</div>')
    out.append('</div>')
    return "".join(out)


APPR = f"""
<div class="inner">
 <div class="to-req" id="to-req">
  <div class="to-reqh"><div class="av m">MR</div><div style="flex:1"><div class="rt">Maya Ross</div><div class="rs">Vacation · sent 7:42 AM</div></div>
   <span class="pill soft" id="to-pill">Pending</span></div>
  <div class="to-reqd"><b>Thu Nov 12 – Fri Nov 13</b> · 2 days<br>Balance 6.5 days → <b>4.5 after</b></div>
 </div>
 <div class="sl">Week of Nov 9 · crew</div>
 {grid()}
 <div class="to-legend"><span><i style="background:#2F4A56"></i>Off</span><span><i style="background:#FBE3EC;border:2px dashed #C2185B"></i>Asked</span><span><i style="background:#12252F"></i>Booked day</span></div>
 <div class="to-flag" id="to-flag"><div class="to-flagi">{icon('cal', 26, '#F4A7C4')}</div>
  <div><div class="ct" style="font-size:22px">Thu Nov 12 · snow-season prep day</div>
  <div class="cs" style="font-size:18px">Booked in Schedule. Owen, Jordan and Theo are on.</div></div></div>
 <div class="to-acts"><div class="btn sm ghost" id="to-other">Suggest other days</div><div class="btn sm" id="to-ok">{icon('check', 26, '#F7F7F4')} Approve</div></div>
</div>"""

DONE = f"""
<div class="inner">
 <div class="to-note" id="to-note"><div class="to-noteic">{icon('check', 28, '#fff')}</div>
  <div><div class="to-notek">Approved by Erin</div><div class="to-notet">Thu Nov 12 – Fri Nov 13. Enjoy the days off.</div></div></div>
 <div class="tiles" style="margin-top:20px">
  <div class="tile" id="to-baltile"><div class="tl">Vacation left</div><div class="tv"><span id="to-bal">6.5</span> <small>days</small></div><div class="to-was" id="to-was">was 6.5 days</div></div>
  <div class="tile"><div class="tl">Sick days left</div><div class="tv">3 <small>days</small></div></div>
 </div>
 <div class="sl">Your time off</div>
 <div class="row to-up"><div class="av m">{icon('leave', 28, '#fff')}</div><div><div class="rt">Nov 12 – 13</div><div class="rs">Vacation · 2 days</div></div><div class="rr"><span class="pill ok">Approved</span></div></div>
 <div class="row to-up"><div class="av l">{icon('leave', 28, '#fff')}</div><div><div class="rt">Dec 24 – 31</div><div class="rs">Holiday shutdown · company-wide</div></div><div class="rr"><span class="pill ghost">Set</span></div></div>
 <div class="row to-up"><div class="av">{icon('leave', 28, '#fff')}</div><div><div class="rt">Aug 17 – 21</div><div class="rs">Vacation · 5 days · taken</div></div><div class="rr"><span class="pill ghost">Done</span></div></div>
</div>"""

TIMEOFF = dict(
    name="S07_time-off",
    kicker="Time off · Leave requests",
    hook="Maya wants two days off. Is snow-prep week covered?",
    end="Time off that checks the schedule first, built the way your crew already asks for it.",
    caps=[(3.35, 6.4, "Maya picks her days. Her balance shows as she goes."),
          (6.4, 9.4, "Erin sees the request next to the crew's week."),
          (9.4, 12.3, "Thursday's snow-prep day is flagged before she decides."),
          (12.3, 15.5, "Approved. Maya's balance updates and Schedule plans around her.")],
    css=CSS,
    screen=appview("to-v1", "leave", REQ, time="7:41", title="Time off")
    + appview("to-v2", "leave", APPR, time="8:05", title="Time off · approvals")
    + appview("to-v3", "leave", DONE, time="8:06", title="Time off",
              extra=toast("to-toast", "book", "Maya blocked off · Nov 12–13; crew suggestions updated")),
    callouts="""<div class="callout" id="to-co" style="left:96px;top:1330px"><div class="ck">One approval, used by</div>
<div class="cr"><i>✓</i>Schedule (crew picks)</div><div class="cr"><i>✓</i>Payroll (vacation pay)</div><div class="cr"><i>✓</i>People (Maya's balance)</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,9.5,10.0,E.io)*(1-P(t,10.75,11.15,E.io));return {s:L(1,1.07,q),ox:320,oy:760}}
function press(el,t,a){const pr=t>=a&&t<a+.2;el.style.transform=pr?'translate(3px,3px)':'none';el.style.boxShadow=pr?'none':''}
function renderReel(t){
 // 1 — Maya requests
 view('to-v1',t,3.0,7.0);
 const s12=t>=4.35,s13=t>=4.95;
 $('to-d12').classList.toggle('sel',s12);$('to-d13').classList.toggle('sel',s13);
 const sm=P(t,5.25,5.6,E.back);S($('to-sum'),{y:L(-14,0,sm),o:sm});
 press($('to-send'),t,6.25);
 const sent=t>=6.45;$('to-send').classList.toggle('to-sent',sent);
 $('to-sendtxt').textContent=sent?'Sent to Erin ✓':'Send to Erin';
 // 2 — Erin reviews
 view('to-v2',t,6.85,12.05);
 S($('to-req'),{y:L(30,0,P(t,7.1,7.5)),o:P(t,7.1,7.5)});
 grow('.to-row',t,7.6,.13,.4);
 const fl=P(t,9.55,9.95,E.back);S($('to-flag'),{y:L(-14,0,fl),o:fl});
 // column highlight on Thu
 const g=$('to-grid'),hd=g.querySelectorAll('.to-gh')[3];
 if(hd){const gr=g.getBoundingClientRect(),hr=hd.getBoundingClientRect(),z=gr.width/g.offsetWidth;
  const col=$('to-col');col.style.left=((hr.left-gr.left)/z-2)+'px';col.style.width=(hr.width/z+4)+'px';
  col.style.opacity=W(t,9.6,11.0,.3)}
 press($('to-ok'),t,11.25);
 const ok=t>=11.45;
 ['to-m12','to-m13'].forEach(id=>{const c=$(id);c.className='to-c '+(ok?'ok':'req');c.textContent=ok?'Off':'Asked'});
 const pill=$('to-pill');pill.textContent=ok?'Approved':'Pending';pill.className='pill '+(ok?'ok':'soft');
 // 3 — Maya notified, balance updates
 view('to-v3',t,11.95,15.9);
 const nt=P(t,12.3,12.7,E.back);S($('to-note'),{y:L(-20,0,nt),o:nt});
 const b=P(t,12.8,13.5,E.out);$('to-bal').textContent=(6.5-2*b).toFixed(1);
 $('to-was').style.opacity=P(t,13.4,13.7);
 $('to-baltile').style.borderColor=t>12.8&&t<14?'#C2185B':'';
 grow('.to-up',t,12.5,.14,.4);
 handoff(t,13.2,15.6,'to-toast');
 callout(t,13.35,15.45,'to-co','to-toast');
 taps(t,[[4.35,'to-d12'],[4.95,'to-d13'],[6.25,'to-send'],[11.25,'to-ok']]);
}""")

ALL = [TIMEOFF]
