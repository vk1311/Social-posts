"""S01 — Clients (CRM). Invented business Harlow & Pine; invented customer Dana Keddy; 555 numbers."""
from suite import appview, toast, icon

LIST = """
<div class="inner">
 <div class="input" id="c-search" style="height:58px;margin-bottom:8px"></div>
 <div id="c-rows">
  <div class="row" id="c-dana"><div class="av m">DK</div><div><div class="rt">Dana Keddy</div><div class="rs">14 Belcher St · 902-555-0142</div></div><div class="rr"><span class="pill soft">Quote out</span></div></div>
  <div class="row c-other"><div class="av">MB</div><div><div class="rt">Marcel Boudreau</div><div class="rs">88 Main St · 902-555-0177</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
  <div class="row c-other"><div class="av l">PS</div><div><div class="rt">Priya Sandhu</div><div class="rs">3 Orchard Ln · 902-555-0119</div></div><div class="rr"><span class="pill ok">Paid</span></div></div>
  <div class="row c-other"><div class="av">TG</div><div><div class="rt">Tom Gallant</div><div class="rs">210 Highbury Rd · 902-555-0163</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
  <div class="row c-other"><div class="av l">RF</div><div><div class="rt">Rosa Fitzgerald</div><div class="rs">41 Cornwallis Ave · 902-555-0108</div></div><div class="rr"><span class="pill ghost">Lead</span></div></div>
  <div class="row c-other"><div class="av">JW</div><div><div class="rt">Jack Whynot</div><div class="rs">9 Prospect Ave · 902-555-0191</div></div><div class="rr"><span class="pill ok">Paid</span></div></div>
  <div class="row c-other"><div class="av m">LC</div><div><div class="rt">Lena Comeau</div><div class="rs">57 Park St · 902-555-0124</div></div><div class="rr"><span class="pill ghost">Active</span></div></div>
 </div>
</div>"""

PROFILE = f"""
<div id="c-scroll"><div class="inner">
 <div style="display:flex;gap:18px;align-items:center">
  <div class="av m" style="width:84px;height:84px;font-size:30px">DK</div>
  <div><div class="ct" style="font-size:34px">Dana Keddy</div><div class="cs">14 Belcher St, Kentville · 902-555-0142</div></div>
 </div>
 <div class="tiles" style="margin-top:22px">
  <div class="tile"><div class="tl">Open quote</div><div class="tv">$820.80</div></div>
  <div class="tile"><div class="tl">Jobs this year</div><div class="tv">6</div></div>
 </div>
 <div class="sl">Notes</div>
 <div class="input" id="c-note" style="height:66px"></div>
 <div id="c-saved" class="card" style="margin-top:12px;opacity:0;border-left:7px solid var(--mag)"><div class="ct" style="font-size:22px" id="c-savedtxt">Gate code 4471. Dog in the back yard.</div><div class="cs">Shown to the crew on every job here</div></div>
 <div class="sl">Timeline</div>
 <div class="tlx">
  <div class="ev mag c-ev"><div class="evt">Called the office</div><div class="evs">Today 9:04 · logged from the phone line</div></div>
  <div class="ev c-ev"><div class="evt">Quote Q-1042 sent · $820.80</div><div class="evs">Yesterday · winter snow service</div></div>
  <div class="ev c-ev"><div class="evt">Invoice INV-2207 paid</div><div class="evs">Sep 18 · e-transfer matched</div></div>
  <div class="ev c-ev"><div class="evt">Job done: fall gutter clean</div><div class="evs">Sep 12 · 4 photos from the crew</div></div>
  <div class="ev c-ev"><div class="evt">Booked online</div><div class="evs">Sep 3 · from the booking page</div></div>
 </div>
 <div class="btn" id="c-book" style="margin-top:6px">{icon('cal', 30, '#F7F7F4')} Book next visit</div>
 <div style="height:200px"></div>
</div></div>"""

CRM = dict(
    name="S01_clients-crm",
    kicker="Clients · CRM",
    hook="One customer. Every call, quote and job on one screen.",
    end="A client list that knows the rest of your business, built around how you already work.",
    caps=[(3.35, 6.35, "Every customer in one list. Search by name, street or phone."),
          (6.35, 9.4, "Calls, quotes, jobs and invoices on one timeline."),
          (9.4, 12.3, "Add a note once. The crew sees it on the job."),
          (12.3, 15.5, "Book the next visit from the same page.")],
    screen=appview("v-list", "crm", LIST, time="9:12", title="Clients")
    + appview("v-prof", "crm", PROFILE, time="9:13", title="Clients",
              extra=toast("c-toast", "book", "Fall cleanup · Thu Oct 15, 8:00 AM")),
    callouts="""<div class="callout" id="co1" style="left:96px;top:1180px"><div class="ck">One record, used by</div>
<div class="cr"><i>✓</i>Schedule</div><div class="cr"><i>✓</i>Jobs (crew phones)</div><div class="cr"><i>✓</i>Quotes &amp; invoices</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,9.4,9.9,E.io)*(1-P(t,11.9,12.35,E.io));return {s:L(1,1.08,q),ox:320,oy:560}}
function renderReel(t){
 view('v-list',t,3.0,6.45);
 typeInto($('c-search'),'kedd',t,4.2,4.9);$('c-search').classList.toggle('on',t>4.0&&t<5.6);
 const f=P(t,4.9,5.3);document.querySelectorAll('.c-other').forEach(r=>{r.style.opacity=1-f;r.style.transform=`translateX(${-30*f}px)`});
 view('v-prof',t,6.3,15.9);
 grow('.c-ev',t,6.7,.18,.45);
 scrollTo($('c-scroll'),t,8.0,9.0,240);
 // note
 const n=$('c-note');const typing=t<11.35;
 if(t<11.35){typeInto(n,'Gate code 4471. Dog in the back yard.',t,9.85,11.15);n.classList.toggle('on',t>9.6)}
 else{n.innerHTML='';n.classList.remove('on')}
 const sv=P(t,11.4,11.75,E.back);S($('c-saved'),{y:L(-16,0,sv),o:sv});
 // book
 const sc2=P(t,12.4,13.2,E.io);if(t>12.4)$('c-scroll').style.transform=`translateY(${L(-240,-560,sc2)}px)`;
 const b=$('c-book');const pr=t>=13.75&&t<13.95;b.style.transform=pr?'translate(3px,3px)':'none';b.style.boxShadow=pr?'none':'';
 handoff(t,14.0,15.6,'c-toast');
 callout(t,13.0,15.45,'co1','c-toast');
 taps(t,[[4.05,'c-search'],[5.9,'c-dana'],[9.65,'c-note'],[11.3,'c-note',230,0],[13.75,'c-book']]);
}""")

ALL = [CRM]
