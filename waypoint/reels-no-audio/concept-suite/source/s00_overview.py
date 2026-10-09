"""S00 — Suite overview (series trailer). Invented business Harlow & Pine; invented customer Dana Keddy.
Story: the "All apps" grid pops in → search Dana → one record lights up a chain across five apps
(Schedule → Jobs → Quotes → Payroll → Reports) → back to the grid: switch off the apps this business
doesn't need. Continuity: Fall cleanup Thu Oct 15 (S01/S02), Owen & Maya 2 h 14 m + INV-2232 (S04)."""
from suite import appview, toast, icon, APPS

CHAIN = ("book", "jobs", "quote", "pay", "rep")
OFF = ("help", "stock", "mail", "ai")


def tiles(prefix):
    return "".join(f'<div class="ag ov-t" id="{prefix}-{k}">{icon(ic, 46)}<span>{lab}</span>'
                   f'<em class="ov-nn">Not needed</em></div>' for k, lab, ic in APPS)


GRID = f"""
<div class="inner">
 <div class="input" id="ov-search" style="height:58px;margin-bottom:10px;gap:12px">{icon('search', 26, '#7E96A2')}<span id="ov-q"></span></div>
 <div class="ov-lab">12 apps · one customer record</div>
 <div class="agrid ov-grid">{tiles('ov-g')}</div>
 <div class="ov-res" id="ov-res"><div class="av m">DK</div><div><div class="rt">Dana Keddy</div><div class="rs">14 Belcher St · on 5 apps</div></div>
  <div class="rr">{icon('arrow', 30, '#C2185B')}</div></div>
</div>"""

STEPS = [
    ("book", "cal", "Schedule", "Booked online", "Fall cleanup · Thu Oct 15, 8:00 AM"),
    ("jobs", "jobs", "Jobs", "Job done, photos", "Owen &amp; Maya · 2 h 14 m · before + after"),
    ("quote", "money", "Quotes", "Invoice from the job", "INV-2232 · drafted for review"),
    ("pay", "pay", "Payroll", "Hours to the pay run", "Oct 3–16 run · waits for Erin's OK"),
    ("rep", "chart", "Reports", "In Monday's numbers", "Mon Oct 19 · revenue + labour by job"),
]

TRAIL = f"""
<div class="inner" style="padding-top:22px">
 <div class="ov-hd" id="ov-hd"><div class="av m" style="width:72px;height:72px;font-size:26px">DK</div>
  <div><div class="ct" style="font-size:31px">Dana Keddy</div><div class="cs" style="margin-top:2px">14 Belcher St, Kentville · 902-555-0142</div></div></div>
 <div class="sl" id="ov-sl">One record · five apps</div>
 <div class="ov-steps">
  <div class="ov-line"></div><div class="ov-fill" id="ov-fill"></div>
  {''.join(f'''<div class="ov-st" id="ov-s{i}"><div class="ov-ic" id="ov-ic{i}">{icon(ic, 34)}</div>
   <div class="ov-card" id="ov-c{i}"><div class="ov-ap">{lab}</div><div class="ov-tt">{tt}</div><div class="ov-ts">{ts}</div>
   <div class="ov-ok" id="ov-ok{i}">{icon('check', 24, '#F7F7F4')}</div></div></div>''' for i, (k, ic, lab, tt, ts) in enumerate(STEPS))}
 </div>
</div>"""

PICK = f"""
<div class="inner">
 <div class="ov-cntrow">
  <div><div class="tl">Apps in Harlow &amp; Pine's build</div><div class="tv"><span id="ov-cnt">12</span> <small>of 12 concepts</small></div></div>
  <div class="pill soft">Concept</div>
 </div>
 <div class="agrid ov-grid ov-pgrid">{tiles('ov-p')}</div>
 <div class="ov-foot" id="ov-foot">Same customer record underneath. Add an app later.</div>
</div>"""

CSS = r"""
.ov-lab{font:600 17px 'DM Sans';letter-spacing:.2em;text-transform:uppercase;color:var(--mag);margin:14px 0 14px}
.ov-grid{gap:16px}
.ov-grid .ag{height:146px;position:relative;gap:10px;font-size:22px}
.ov-grid .ag.ov-hi{box-shadow:6px 6px 0 var(--mag)}
.ov-nn{position:absolute;left:0;right:0;bottom:10px;text-align:center;font:600 13px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;
 color:var(--slate);font-style:normal;opacity:0}
.ag.ov-off{border-style:dashed;border-color:#B9B3A6;background:#EFECE4;color:#7E96A2}
.ag.ov-off svg{color:#A9B7BE}
.ag.ov-off span{text-decoration:line-through}
.ag.ov-off .ov-nn{opacity:1}
.ov-res{position:absolute;left:30px;right:30px;top:94px;z-index:4;display:flex;align-items:center;gap:16px;background:#fff;border:2px solid var(--ink);
 box-shadow:6px 6px 0 var(--mag);padding:16px 18px;opacity:0}
.ov-hd{display:flex;gap:18px;align-items:center}
.ov-steps{position:relative;margin-top:4px}
.ov-line{position:absolute;left:33px;top:76px;height:608px;width:4px;background:#D8D2C4}
.ov-fill{position:absolute;left:33px;top:76px;height:608px;width:4px;background:var(--mag);transform-origin:top center;transform:scaleY(0)}
.ov-st{display:flex;gap:18px;align-items:center;height:152px;position:relative}
.ov-ic{width:70px;height:70px;flex:none;border:2.5px solid var(--ink);background:var(--paper);display:flex;align-items:center;justify-content:center;
 color:var(--slate);position:relative;z-index:1}
.ov-ic.on{background:var(--mag);border-color:var(--mag);color:#fff}
.ov-card{flex:1;position:relative;border:2px solid var(--ink);background:#fff;padding:16px 60px 16px 18px}
.ov-card.on{box-shadow:6px 6px 0 var(--mag)}
.ov-ap{font:700 16px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:var(--slate)}
.ov-card.on .ov-ap{color:var(--mag)}
.ov-tt{font:800 27px/1.2 Manrope;margin-top:3px}
.ov-ts{font:400 19px 'DM Sans';color:var(--slate);margin-top:3px;white-space:nowrap}
.ov-ok{position:absolute;right:14px;top:50%;margin-top:-19px;width:38px;height:38px;border-radius:50%;background:var(--ink);display:flex;
 align-items:center;justify-content:center;opacity:0}
.ov-cntrow{display:flex;justify-content:space-between;align-items:center;border:2px solid var(--ink);background:#fff;padding:14px 18px;margin-bottom:18px}
.ov-cntrow .tv{font-size:42px}
.ov-foot{margin-top:22px;border-left:6px solid var(--mag);padding:8px 14px;font:600 21px 'DM Sans';opacity:0}
"""

OVERVIEW = dict(
    name="S00_suite-overview",
    kicker="All apps · The suite",
    hook="Dana's address, typed into five apps. Or typed once.",
    end="Waypoint builds the suite around how the business already works.",
    caps=[(3.35, 6.4, "Twelve apps. One customer record behind all of them."),
          (6.4, 9.4, "Dana books online. The crew's job and photos join her record."),
          (9.4, 12.4, "The invoice, the crew's hours and Monday's numbers follow."),
          (12.4, 15.5, "Every app here is a concept. Yours gets only what you need.")],
    css=CSS,
    screen=appview("ov-gridv", "crm", GRID, time="9:12", title="All apps", active="more")
    + appview("ov-trail", "crm", TRAIL, time="9:13", title="Clients",
              extra=toast("ov-toast", "rep", "Fall cleanup · in Monday's numbers"))
    + appview("ov-pick", "crm", PICK, time="9:14", title="All apps", active="more"),
    js=r"""
const CHAIN=%s, OFF=%s, ST=[7.35,8.35,9.6,10.5,11.4], OFFT=[12.95,13.4,13.85,14.3];
function renderReel(t){
 // 1 · All apps grid
 view('ov-gridv',t,3.0,6.95);
 const dim=P(t,5.95,6.35);
 document.querySelectorAll('#ov-gridv .ov-t').forEach((e,i)=>{const a=3.55+i*.12;const q=P(t,a,a+.38,E.back);
  const inChain=CHAIN.includes(e.id.slice(5));e.classList.toggle('ov-hi',inChain&&t>6.0);
  S(e,{s:L(.6,1,q),o:Math.min(1,P(t,a,a+.18))*(inChain?1:L(1,.35,dim))})});
 const s=$('ov-search');s.classList.toggle('on',t>5.3&&t<6.9);
 typeInto($('ov-q'),'dana',t,5.5,5.85);if(t<5.3)$('ov-q').innerHTML='<span style="color:#7E96A2">Search every app</span>';
 const r=P(t,5.95,6.3,E.back);S($('ov-res'),{y:L(-14,0,r),o:P(t,5.95,6.15)});
 const pr=t>=6.55&&t<6.75;$('ov-res').style.boxShadow=pr?'none':'';
 // 2 · one record, five apps
 view('ov-trail',t,6.9,12.75);
 grow('#ov-hd,#ov-sl',t,7.0,.12,.4);
 let f=0;for(let i=1;i<5;i++)f+=P(t,ST[i]-.5,ST[i]-.05,E.io)/4;$('ov-fill').style.transform=`scaleY(${f})`;
 ST.forEach((a,i)=>{const on=t>=a;const q=P(t,a,a+.35,E.back);
  $('ov-ic'+i).classList.toggle('on',on);$('ov-c'+i).classList.toggle('on',on);
  S($('ov-s'+i),{x:L(0,0,1),o:L(.4,1,P(t,a-.1,a+.2))});S($('ov-ic'+i),{s:on?L(.7,1,q):1});
  S($('ov-ok'+i),{s:L(.4,1,q),o:P(t,a+.1,a+.3)})});
 handoff(t,11.6,12.75,'ov-toast');
 // 3 · only the apps this business needs
 view('ov-pick',t,12.55,15.9);
 let n=12;document.querySelectorAll('#ov-pick .ov-t').forEach(e=>{const k=e.id.slice(5);const j=OFF.indexOf(k);
  const off=j>=0&&t>=OFFT[j]+.05;e.classList.toggle('ov-off',off);if(off)n--;
  const pr=j>=0&&t>=OFFT[j]&&t<OFFT[j]+.18;S(e,{s:pr?.95:1})});
 $('ov-cnt').textContent=n;
 const fq=P(t,14.6,14.95);S($('ov-foot'),{y:L(16,0,fq),o:fq});
 taps(t,[[5.3,'ov-search'],[6.55,'ov-res',190,0],[12.95,'ov-p-help'],[13.4,'ov-p-stock'],[13.85,'ov-p-mail'],[14.3,'ov-p-ai']]);
}""" % (list(CHAIN).__repr__().replace("'", '"'), list(OFF).__repr__().replace("'", '"')))

ALL = [OVERVIEW]
