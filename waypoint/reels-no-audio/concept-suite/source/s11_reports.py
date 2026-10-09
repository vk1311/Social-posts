"""S11 — Reports. Invented business Harlow & Pine; all figures are made up for the demo.
Story: Erin's Monday morning (Mon Nov 2, 2026). Last week's tiles count up, each labelled with the app its
number comes from (nobody types numbers twice); a jobs-by-week bar chart grows. She taps the unpaid tile,
sees 3 unpaid invoices oldest first with days overdue, selects all and taps Draft reminders.
Hand-off to Quotes: drafts wait for her to send. No outcome claims."""
from suite import appview, toast, icon


def src(app_icon, label, el_id):
    return f'<div class="rp-src" id="{el_id}">{icon(app_icon, 18)}<span>from {label}</span></div>'


DASH = f"""
<div class="inner">
 <div class="rp-head"><div><div class="tl">Monday · Nov 2</div><div class="rp-wk">Last week · Oct 26 – Nov 1</div></div>
  <div class="rp-hi">Good morning, Erin</div></div>
 <div class="tiles rp-tiles">
  <div class="tile rp-tile" id="rp-t1"><div class="tl">Jobs done</div><div class="tv" id="rp-v1">0</div>{src('jobs', 'Jobs', 'rp-s1')}</div>
  <div class="tile rp-tile" id="rp-t2"><div class="tl">Invoices sent</div><div class="tv" id="rp-v2">0</div>{src('money', 'Quotes', 'rp-s2')}</div>
  <div class="tile rp-tile rp-unp" id="rp-t3"><div class="tl">Unpaid · 3</div><div class="tv" id="rp-v3">$0.00</div>{src('money', 'Quotes', 'rp-s3')}</div>
  <div class="tile rp-tile" id="rp-t4"><div class="tl">Crew hours</div><div class="tv" id="rp-v4">0.0</div>{src('pay', 'Payroll', 'rp-s4')}</div>
 </div>
 <div class="sl" style="margin-top:20px">Jobs done · by week</div>
 <div class="rp-chart">
  <div class="bars rp-bars">
   <div class="bar rp-bar" style="height:{17/26*100:.1f}%"><span>17</span></div>
   <div class="bar rp-bar" style="height:{20/26*100:.1f}%"><span>20</span></div>
   <div class="bar rp-bar" style="height:{19/26*100:.1f}%"><span>19</span></div>
   <div class="bar rp-bar" style="height:{24/26*100:.1f}%"><span>24</span></div>
   <div class="bar rp-bar" style="height:{21/26*100:.1f}%"><span>21</span></div>
   <div class="bar mag rp-bar" style="height:{23/26*100:.1f}%"><span>23</span></div>
  </div>
  <div class="bx"><div>Sep 21</div><div>Sep 28</div><div>Oct 5</div><div>Oct 12</div><div>Oct 19</div><div><b>Oct 26</b></div></div>
 </div>
 <div class="rp-foot" id="rp-foot">{icon('check', 22, '#C2185B')}<span>Filled in from the apps the work happened in. Nothing typed twice.</span></div>
</div>"""

INV = [("rp-r1", "MB", "", "Marcel Boudreau", "INV-2189", "Due Sep 30", "$1,254.00", "33 days overdue", "mag"),
       ("rp-r2", "RF", " l", "Rosa Fitzgerald", "INV-2201", "Due Oct 14", "$969.00", "19 days overdue", "soft"),
       ("rp-r3", "JW", "", "Jack Whynot", "INV-2214", "Due Oct 23", "$991.80", "10 days overdue", "soft")]

ROWS = "".join(
    f'<div class="row rp-row" id="{rid}"><div class="cb rp-cb"></div><div class="av{avc}">{ini}</div>'
    f'<div style="min-width:0"><div class="rt">{name}</div><div class="rs">{inv} · {due}</div>'
    f'<div class="rp-pl"><span class="pill {pc}">{od}</span></div></div>'
    f'<div class="rr">{amt}<div class="rp-drw"><span class="pill ghost rp-dr">Draft ready</span></div></div></div>'
    for rid, ini, avc, name, inv, due, amt, od, pc in INV)

UNPAID = f"""
<div class="inner">
 <div class="rp-back">‹ Reports · last week</div>
 <div class="ct" style="font-size:34px;margin-top:12px">Unpaid invoices</div>
 <div class="cs">3 invoices · $3,214.80 incl. HST</div>
 <div class="rp-bar2"><div class="rp-sel" id="rp-all"><div class="cb" id="rp-allcb"></div><span>Select all</span></div>
  <div class="rp-sort">Oldest first ▾</div></div>
 <div id="rp-rows">{ROWS}</div>
 <div class="btn" id="rp-draft"><span id="rp-dt">{icon('mail', 30, '#F7F7F4')} Draft reminders</span></div>
 <div class="rp-small" id="rp-note">Drafts only. Nothing goes out until you send it.</div>
</div>"""

CSS = r"""
.rp-head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid var(--ink);padding-bottom:14px}
.rp-wk{font:800 27px Manrope;margin-top:4px}
.rp-hi{font:600 18px 'DM Sans';color:var(--slate);text-align:right;width:130px;line-height:1.3}
.rp-tiles{margin-top:18px;gap:12px}
.rp-tile{padding:14px 16px 14px}
.rp-tile .tv{font-size:38px;margin-top:4px}
.rp-unp{border-color:var(--mag);box-shadow:5px 5px 0 var(--mag)}
.rp-unp .tv{color:var(--mag)}
.rp-src{display:inline-flex;align-items:center;gap:7px;margin-top:10px;padding:5px 10px 5px 8px;background:#ECEEEC;color:var(--slate);
 font:700 16px 'DM Sans';letter-spacing:.02em;opacity:0}
.rp-src.on{background:var(--ink);color:var(--paper)}
.rp-src.on svg{color:#F4A7C4}
.rp-chart{border:2px solid var(--ink);background:#fff;padding:44px 12px 12px}
.rp-bars{height:200px;gap:12px}
.rp-bar{transform:scaleY(0)}
.rp-chart .bx{gap:12px}
.rp-chart .bx div{font-size:15px}
.rp-chart .bx b{color:var(--mag)}
.rp-foot{display:flex;gap:10px;align-items:flex-start;margin-top:16px;font:600 19px/1.35 'DM Sans';color:var(--slate);opacity:0}
.rp-foot svg{margin-top:2px}
.rp-back{font:600 21px 'DM Sans';color:var(--mag)}
.rp-bar2{display:flex;justify-content:space-between;align-items:center;margin-top:18px;padding:12px 0;border-top:2px solid var(--ink);border-bottom:2px solid var(--ink)}
.rp-sel{display:flex;align-items:center;gap:12px;font:700 21px 'DM Sans'}
.rp-sort{font:600 19px 'DM Sans';color:var(--slate)}
.rp-row{align-items:flex-start;gap:12px;padding:18px 0}
.rp-row .cb{margin-top:12px}
.rp-row .av{width:52px;height:52px;font-size:19px;margin-top:3px}
.rp-row .rt{font-size:24px}
.rp-row .rs{font-size:19px}
.rp-row .rr{font-size:24px;padding-top:4px}
.rp-pl{margin-top:8px;display:flex;gap:8px;flex-wrap:nowrap}
.rp-pl .pill,.rp-dr{white-space:nowrap}
.rp-drw{margin-top:10px}
.rp-dr{opacity:0}
#rp-toast{bottom:430px}
.rp-small{font:400 18px/1.4 'DM Sans';color:var(--slate);margin-top:14px}
"""

REP = dict(
    name="S11_reports",
    kicker="Reports · Dashboards",
    hook="Monday morning: last week's jobs, invoices and who still owes.",
    end="Reports that read straight from the work you log, built around how your business already runs.",
    caps=[(3.35, 6.4, "Monday morning. Last week's numbers are already filled in."),
          (6.4, 9.4, "Each number comes from Jobs, Quotes or Payroll. No retyping."),
          (9.4, 12.4, "Tap unpaid: three invoices, oldest first, with days overdue."),
          (12.4, 15.5, "Reminders go to Quotes as drafts. Erin sends them herself.")],
    css=CSS,
    screen=appview("rp-dash", "rep", DASH, time="7:42", title="Reports",
                   dock_keys=("crm", "jobs", "quote", "rep", "more"))
    + appview("rp-unpaid", "rep", UNPAID, time="7:43", title="Reports",
              dock_keys=("crm", "jobs", "quote", "rep", "more"),
              extra=toast("rp-toast", "quote", "3 reminders drafted · waiting for you to send")),
    callouts="""<div class="callout" id="rp-co" style="left:96px;top:1640px"><div class="ck">Every number comes from</div>
<div class="cr"><i>✓</i>Jobs (work done)</div><div class="cr"><i>✓</i>Quotes (invoices, payments)</div><div class="cr"><i>✓</i>Payroll (crew hours)</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,6.5,7.0,E.io)*(1-P(t,8.5,8.95,E.io));return {s:L(1,1.07,q),ox:320,oy:420}}
const c0=v=>Math.round(v).toLocaleString('en-CA');
function renderReel(t){
 // ---- view 1: Monday dashboard ----
 view('rp-dash',t,3.0,9.65);
 grow('.rp-tile',t,3.3,.12,.4);
 countUp($('rp-v1'),t,3.6,5.0,23,c0);
 countUp($('rp-v2'),t,3.75,5.15,18,c0);
 countUp($('rp-v3'),t,3.9,5.3,3214.80,money);
 countUp($('rp-v4'),t,4.05,5.45,186.5,v=>v.toFixed(1));
 // source tags appear, then light up one by one while caption 2 runs
 ['rp-s1','rp-s2','rp-s3','rp-s4'].forEach((id,i)=>{const el=$(id);const q=P(t,4.9+i*.15,5.3+i*.15);S(el,{y:L(10,0,q),o:q});
  const a=6.7+i*.45;el.classList.toggle('on',t>=a&&t<a+.75)});
 grow('.rp-bar',t,5.5,.12,.5);
 const f=P(t,7.9,8.3);S($('rp-foot'),{y:L(14,0,f),o:f});
 // unpaid tile press
 const t3=$('rp-t3');const pr=t>=9.0&&t<9.2;if(pr)t3.style.transform='translate(3px,3px)';t3.style.boxShadow=pr?'none':'';
 // ---- view 2: unpaid list ----
 view('rp-unpaid',t,9.4,15.9);
 grow('.rp-row',t,9.7,.14,.4);
 const sel=[11.05,11.17,11.29];
 const ac=t>=10.95;const acb=$('rp-allcb');acb.classList.toggle('on',ac);acb.innerHTML=ac?CHK:'';
 document.querySelectorAll('.rp-cb').forEach((c,i)=>{const on=t>=sel[i];c.classList.toggle('on',on);c.innerHTML=on?CHK:'';
  c.style.transform=on?`scale(${L(1.25,1,P(t,sel[i],sel[i]+.2))})`:''});
 const d=$('rp-draft');const dpr=t>=11.95&&t<12.15;const done=t>=12.15;
 d.style.transform=dpr?'translate(3px,3px)':'none';d.style.boxShadow=dpr?'none':(done?'5px 5px 0 var(--ink)':'');
 d.style.background=done?'var(--mag)':'';
 $('rp-dt').innerHTML=done?CHKW+' 3 drafts ready in Quotes':(t>=11.3?MAILW+' Draft reminders (3)':MAILW+' Draft reminders');
 document.querySelectorAll('.rp-dr').forEach((e,i)=>{const q=P(t,12.3+i*.12,12.6+i*.12,E.back);S(e,{s:L(.6,1,q),o:q})});
 $('rp-note').textContent=done?'Drafted from each invoice. Erin reads and sends each one.':'Drafts only. Nothing goes out until you send it.';
 handoff(t,12.9,15.6,'rp-toast');
 callout(t,13.3,15.45,'rp-co','rp-toast');
 const zs=zoomAt(t).s;const tl=[[9.0,'rp-t3'],[10.95,'rp-allcb'],[11.95,'rp-draft']]
  .map(k=>{const r=rel($(k[1]));return [k[0],k[1],r.x/zs-r.x,r.y/zs-r.y]});
 taps(t,tl);
}
const CHK='<svg width="24" height="24" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3"/></svg>';
const CHKW='<svg width="30" height="30" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#F7F7F4" stroke-width="2.8"/></svg>';
const MAILW='<svg width="30" height="30" viewBox="0 0 24 24" style="color:#F7F7F4"><rect x="3" y="5.5" width="18" height="13" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>';
""")

ALL = [REP]
