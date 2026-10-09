"""S05 — People (HR onboarding). Invented business Harlow & Pine; invented new hire Theo Burgess; 555 numbers."""
from suite import appview, toast, icon

CHK = icon('check', 24, '#FFFFFF')

LIST = f"""
<div class="inner">
 <div class="sl" style="margin-top:4px">Starting soon</div>
 <div class="card hi hr-li" id="hr-theo">
  <div style="display:flex;gap:16px;align-items:center">
   <div class="av m">TB</div>
   <div style="flex:1"><div class="rt">Theo Burgess</div><div class="rs">Crew · starts Mon Oct 19</div></div>
   <span class="pill soft">New hire</span>
  </div>
  <div class="hr-mini"><span>Onboarding</span><b>1 of 7 done</b></div>
  <div class="prog"><i style="transform:scaleX(.143)"></i></div>
  <div class="hr-ping" id="hr-ping"><i class="hr-dot"></i>Theo opened his onboarding link · 4:10 PM</div>
 </div>
 <div class="sl">Team · 5</div>
 <div class="row hr-li"><div class="av m">EH</div><div><div class="rt">Erin Harlow</div><div class="rs">Owner · office</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
 <div class="row hr-li"><div class="av l">SP</div><div><div class="rt">Sam Pine</div><div class="rs">Office · scheduling</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
 <div class="row hr-li"><div class="av">OC</div><div><div class="rt">Owen Cleveland</div><div class="rs">Crew lead · 902-555-0131</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
 <div class="row hr-li"><div class="av l">MR</div><div><div class="rt">Maya Ross</div><div class="rs">Crew · 902-555-0158</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
 <div class="row hr-li"><div class="av">JL</div><div><div class="rt">Jordan Lantz</div><div class="rs">Crew · 902-555-0172</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
</div>"""

# (title, pending text, done text)
ITEMS = [
    ("Offer letter signed", "", "Signed Mon Oct 12 · e-signature"),
    ("Federal TD1", "Waiting on Theo", "Filled in 4:11 PM · Theo's phone"),
    ("Nova Scotia TD1", "Waiting on Theo", "Filled in 4:13 PM · Theo's phone"),
    ("Direct deposit details", "Waiting on Theo", "Added 4:15 PM · Theo's phone"),
    ("WHMIS training", "Waiting on Theo", "Course done 4:38 PM · certificate saved"),
    ("Safety orientation", "Waiting on Theo", "Video + sign-off 4:52 PM · Theo's phone"),
    ("Gear issued: boots, radio", "Hand over in person · Erin", "Boots size 10, radio #07 · Erin, 4:58 PM"),
]


def _rows():
    out = []
    for i, (t, a, b) in enumerate(ITEMS):
        on = " on" if i == 0 else ""
        dst = ' style="opacity:1"' if i == 0 else ""
        out.append(f'<div class="hr-row" id="hr-r{i}"><div class="cb{on}" id="hr-cb{i}"><span class="hr-ck">{CHK}</span></div>'
                   f'<div class="hr-tx"><div class="hr-t">{t}</div><div class="hr-s"><span class="hr-p">{a}</span>'
                   f'<span class="hr-d"{dst}>{b}</span></div></div></div>')
    return "".join(out)


CHECK = f"""
<div id="hr-scroll"><div class="inner">
 <div style="display:flex;gap:16px;align-items:center">
  <div class="av m" style="width:72px;height:72px;font-size:26px">TB</div>
  <div style="flex:1"><div class="ct" style="font-size:30px">Theo Burgess</div><div class="cs" style="margin-top:2px">Crew · starts Mon Oct 19</div></div>
 </div>
 <div class="hr-ph"><span class="tl">Onboarding</span><b id="hr-ct">1 of 7 done</b></div>
 <div class="prog" style="height:18px"><i id="hr-bar" style="transform:scaleX(.143)"></i></div>
 <div class="hr-live" id="hr-live"><i class="hr-dot"></i><span id="hr-livetxt">Theo is filling in his forms on his phone</span></div>
 <div class="sl" style="margin-top:18px">Checklist</div>
 {_rows()}
 <div class="hr-ready" id="hr-ready">{icon('check', 26, '#C2185B')} Everything Payroll needs is on file</div>
 <div class="btn" id="hr-review" style="margin-top:14px">Review profile {icon('arrow', 28, '#F7F7F4')}</div>
 <div style="height:200px"></div>
</div></div>"""

ONFILE = ["Offer letter · signed Oct 12", "TD1 federal + Nova Scotia", "Direct deposit details",
          "WHMIS certificate", "Safety orientation sign-off", "Gear: boots size 10, radio #07", "Emergency contact"]

PROFILE = f"""
<div class="inner">
 <div style="display:flex;gap:18px;align-items:center">
  <div class="av m" style="width:84px;height:84px;font-size:30px">TB</div>
  <div style="flex:1"><div class="ct" style="font-size:32px">Theo Burgess</div><div class="cs">Crew · Kentville · 902-555-0186</div></div>
 </div>
 <div class="hr-stamp" id="hr-stamp">{icon('check', 26, '#FFFFFF')} Profile complete</div>
 <div class="tiles" style="margin-top:18px">
  <div class="tile"><div class="tl">Start date</div><div class="tv" style="font-size:34px">Oct 19</div></div>
  <div class="tile"><div class="tl">Pay group</div><div class="tv" style="font-size:34px">Crew <small>biweekly</small></div></div>
 </div>
 <div class="sl">On file</div>
 {''.join(f'<div class="hr-of">{icon("check", 24, "#C2185B")}<span>{x}</span></div>' for x in ONFILE)}
 <div class="btn" id="hr-send">{icon('pay', 30, '#F7F7F4')} <span id="hr-sendtxt">Send to Payroll</span></div>
</div>"""

DOCK = ("hr", "pay", "leave", "book", "more")

PEOPLE = dict(
    name="S05_people-hr",
    kicker="People · Onboarding",
    hook="New hire Monday. His paperwork comes in from his own phone.",
    end="Onboarding that follows your checklist, your forms and your gear list, built the way you already hire.",
    caps=[(3.35, 6.35, "Theo starts Monday. His onboarding checklist is already waiting."),
          (6.35, 9.4, "He fills in his TD1s and banking from his own phone."),
          (9.4, 12.4, "Boots and radio handed over? Erin ticks that one herself."),
          (12.4, 15.5, "Profile complete. Payroll picks Theo up from there.")],
    screen=appview("v-hrlist", "hr", LIST, time="4:10", title="People", dock_keys=DOCK)
    + appview("v-hrcheck", "hr", CHECK, time="4:11", title="People", dock_keys=DOCK)
    + appview("v-hrprof", "hr", PROFILE, time="4:59", title="People", dock_keys=DOCK,
              extra=toast("hr-toast", "pay", "Theo added · first pay period Oct 30")),
    css=r"""
.hr-mini{display:flex;justify-content:space-between;margin-top:16px;font:600 17px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:var(--slate)}
.hr-mini b{font:800 20px Manrope;letter-spacing:0;text-transform:none;color:var(--ink)}
.hr-ping{display:flex;align-items:center;gap:10px;margin-top:14px;padding:10px 14px;background:#FBE3EC;color:#9E1149;font:700 19px 'DM Sans';opacity:0}
.hr-dot{display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--mag);flex:none}
.hr-ph{display:flex;justify-content:space-between;align-items:baseline;margin-top:22px}
.hr-ph b{font:800 24px Manrope}
.hr-live{display:flex;align-items:center;gap:12px;margin-top:16px;background:var(--ink);color:var(--paper);padding:13px 16px;font:700 20px 'DM Sans';border-left:6px solid var(--mag)}
.hr-row{position:relative;display:flex;gap:16px;align-items:center;padding:12px 10px;margin:0 -10px;border-bottom:1.5px solid #E3DED2}
.hr-row .cb{transition:none}
.hr-ck{display:flex;opacity:0}
.cb.on .hr-ck{opacity:1}
.hr-t{font:700 23px/1.2 Manrope}
.hr-s{position:relative;height:24px;margin-top:3px;font:500 18px 'DM Sans'}
.hr-s span{position:absolute;left:0;top:0;white-space:nowrap}
.hr-p{color:var(--mist)} .hr-d{color:#9E1149;opacity:0}
.hr-ready{display:flex;align-items:center;gap:10px;margin-top:20px;font:700 21px 'DM Sans';color:var(--ink);opacity:0}
.hr-stamp{display:inline-flex;align-items:center;gap:10px;margin-top:18px;background:var(--mag);color:#fff;font:800 22px Manrope;padding:10px 16px}
.hr-of{display:flex;align-items:center;gap:12px;padding:9px 0;border-bottom:1.5px solid #E3DED2;font:600 21px 'DM Sans'}
""",
    callouts="""<div class="callout" id="hr-co" style="left:96px;top:1180px"><div class="ck">One profile, used by</div>
<div class="cr"><i>✓</i>Payroll</div><div class="cr"><i>✓</i>Schedule (crew list)</div><div class="cr"><i>✓</i>Time off</div></div>""",
    js=r"""
const HRT=[null,6.95,7.6,8.25,8.9,9.55,10.75];
const HRCLK=['4:11','4:11','4:13','4:15','4:38','4:52','4:58'];
function zoomAt(t){const q=P(t,6.5,7.0,E.io)*(1-P(t,9.85,10.3,E.io));return {s:L(1,1.06,q),ox:320,oy:820}}
function renderReel(t){
 // list
 view('v-hrlist',t,3.0,6.45);
 grow('.hr-li',t,3.45,.1,.4);
 const pg=P(t,4.5,4.9,E.back);S($('hr-ping'),{y:L(-10,0,pg),o:P(t,4.5,4.8)});
 // checklist
 view('v-hrcheck',t,6.3,12.1);
 let done=1,last=0,bar=1;
 for(let i=1;i<7;i++){
  const ti=HRT[i],q=P(t,ti,ti+.3,E.back),on=t>=ti;
  if(on){done++;last=i}
  bar+=P(t,ti,ti+.4,E.io);
  const cb=$('hr-cb'+i);cb.classList.toggle('on',on);cb.style.transform=`scale(${on?L(.6,1,q):1})`;
  const r=$('hr-r'+i);const fl=on?1-P(t,ti+.25,ti+.9):0;r.style.background=`rgba(251,227,236,${fl})`;
  const p=r.querySelector('.hr-p'),d=r.querySelector('.hr-d');
  S(p,{y:L(0,-10,P(t,ti,ti+.2)),o:1-P(t,ti,ti+.2)});S(d,{y:L(10,0,P(t,ti+.05,ti+.3)),o:P(t,ti+.05,ti+.3)});
 }
 $('hr-ct').textContent=(done===7?'7 of 7 · complete':done+' of 7 done');
 $('hr-bar').style.transform=`scaleX(${bar/7})`;
 document.querySelector('#v-hrcheck .sb span').textContent=HRCLK[last];
 $('hr-livetxt').textContent=t<9.85?'Theo is filling in his forms on his phone':"Theo's part is done · now Erin's turn";
 scrollTo($('hr-scroll'),t,10.0,10.5,190);
 const rd=P(t,11.0,11.3,E.back);S($('hr-ready'),{y:L(12,0,rd),o:P(t,11.0,11.25)});
 const rv=$('hr-review');const pr=t>=11.5&&t<11.7;rv.style.transform=pr?'translate(3px,3px)':'none';rv.style.boxShadow=pr?'none':'';
 // profile
 view('v-hrprof',t,11.9,15.9);
 const st=P(t,12.25,12.6,E.back);S($('hr-stamp'),{s:L(.7,1,st),o:P(t,12.25,12.45)});
 grow('.hr-of',t,12.4,.08,.35);
 const sd=$('hr-send');const sp=t>=13.4&&t<13.6;sd.style.transform=sp?'translate(3px,3px)':'none';sd.style.boxShadow=sp?'none':'';
 $('hr-sendtxt').textContent=t<13.6?'Send to Payroll':'Sent to Payroll';
 handoff(t,13.65,15.6,'hr-toast');
 callout(t,13.8,15.45,'hr-co','hr-toast');
 taps(t,[[5.85,'hr-theo'],[10.75,'hr-cb6'],[11.5,'hr-review'],[13.4,'hr-send']]);
}""")

ALL = [PEOPLE]
