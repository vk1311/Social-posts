"""S02 — Schedule (booking). Invented business Harlow & Pine; invented customer Dana Keddy; 555 numbers."""
from suite import appview, toast, icon
from shell import sb

# ---- existing (made-up) bookings for the week of Oct 12-16, 2026 ---------------------------
# (slot row, day col) -> (customer surname, town, crew)  crew: "o" = Owen's crew, "m" = Maya's crew
DAYS = [("Mon", 12), ("Tue", 13), ("Wed", 14), ("Thu", 15), ("Fri", 16)]
SLOTS = ["8 AM", "10", "12 PM", "2"]
BOOK = {
    (0, 0): ("Boudreau", "New Minas", "m"), (1, 0): ("Whynot", "Kentville", "o"), (3, 0): ("Rafuse", "Wolfville", "m"),
    (0, 1): ("Hiltz", "Berwick", "m"), (2, 1): ("Fitzgerald", "Kentville", "o"),
    (1, 2): ("Sandhu", "Wolfville", "m"), (2, 2): ("Pineo", "New Minas", "o"), (3, 2): ("Eaton", "Berwick", "m"),
    (1, 3): ("Gallant", "Kentville", "o"), (2, 3): ("Comeau", "Kentville", "o"), (3, 3): ("Morine", "Berwick", "m"),
    (0, 4): ("Bishop", "Wolfville", "m"), (2, 4): ("Lohnes", "Kentville", "o"),
}


def week_grid():
    out = ['<div class="bk-wk"><div></div>']
    for i, (d, n) in enumerate(DAYS):
        thu = ' id="bk-thuh"' if i == 3 else ""
        out.append(f'<div class="bk-dh"{thu}>{d}<b>{n}</b></div>')
    for r, s in enumerate(SLOTS):
        out.append(f'<div class="bk-tm">{s}</div>')
        for c in range(5):
            cls = "bk-cell bk-thu" if c == 3 else "bk-cell"
            cid = ' id="bk-slot"' if (r, c) == (0, 3) else ""
            inner = ""
            if (r, c) in BOOK:
                name, town, crew = BOOK[(r, c)]
                hit = " bk-kv" if (c == 3 and town == "Kentville") else ""
                inner = (f'<div class="bk-b {crew}"><div class="n">{name}</div>'
                         f'<div class="a{hit}">{town}</div></div>')
            if (r, c) == (0, 3):
                inner = ('<div class="bk-new" id="bk-new"><div class="n" id="bk-newn">Keddy</div>'
                         '<div class="a">Kentville</div></div>')
            out.append(f'<div class="{cls}"{cid}>{inner}</div>')
    out.append('</div>')
    return "".join(out)


WEB = f"""
<div class="view" id="bk-web" style="background:#fff;color:#12252F">{sb('8:02')}
 <div class="bk-url"><i></i>Harlow &amp; Pine · Book online</div>
 <div class="pad" style="padding-top:22px">
  <div class="k">Harlow &amp; Pine Property Services</div><h2 style="margin:6px 0 18px">Book a visit</h2>
  <div class="bk-me"><div class="av m">DK</div><div><div class="rt" style="font-size:23px">Dana Keddy</div>
   <div class="rs" style="font-size:19px">902-555-0142 · we text to confirm</div></div></div>
  <div class="field"><label>Service</label><div class="bk-chips"><span id="bk-c-fall">Fall cleanup</span><span>Aeration</span><span>Snow</span></div></div>
  <div class="field"><label>Address</label><div class="input" id="bk-addr"></div></div>
  <div class="field"><label>Preferred day</label><div class="bk-chips"><span>Wed 14</span><span id="bk-d-thu">Thu 15</span><span>Fri 16</span></div></div>
  <div class="btn" id="bk-send">Request booking</div>
 </div>
 <div class="bk-doneov" id="bk-doneov"><div class="bk-dcheck">✓</div><div class="bk-dt">Request sent</div>
  <div class="bk-dd">Harlow &amp; Pine will text 902-555-0142 once a crew is booked.</div></div>
</div>"""

WEEK = f"""
<div id="bk-wscroll"><div class="inner" style="padding:20px 22px">
 <div class="card hi" id="bk-req" style="border-left:7px solid var(--mag);padding:16px 18px;margin-bottom:0">
  <div style="display:flex;align-items:flex-start;gap:12px">
   <div style="flex:1"><div class="k" style="font-size:15px">New request · online · 8:02 AM</div>
    <div class="ct" style="font-size:25px;margin-top:6px">Dana Keddy · Fall cleanup</div>
    <div class="cs" style="font-size:19px">14 Belcher St, Kentville · prefers Thu</div></div>
   <div class="btn sm" id="bk-place" style="flex:none;width:112px;height:56px;margin-top:6px">Place</div>
  </div>
 </div>
 <div class="bk-leg"><div class="bk-wkof">Week of Oct 12</div>
  <div class="bk-lg"><span><i class="bk-sw"></i>Owen's crew</span><span><i class="bk-sw m"></i>Maya's crew</span></div></div>
 {week_grid()}
</div></div>
<div class="bk-sheet" id="bk-sheet">
 <div class="bk-shh"><div class="sl" style="margin:0">Suggested by area · Thu Oct 15</div><div class="bk-yc">You choose</div></div>
 <div class="bk-sug" id="bk-s1"><div class="av">OC</div><div style="flex:1"><div class="rt" style="font-size:24px">Owen's crew</div>
  <div class="rs" style="font-size:19px">Owen C., Theo B. · 2 jobs in Kentville</div></div><div class="rr"><span class="pill" id="bk-best">Closest</span></div></div>
 <div class="bk-sug" id="bk-s2"><div class="av l">MR</div><div style="flex:1"><div class="rt" style="font-size:24px">Maya's crew</div>
  <div class="rs" style="font-size:19px">Maya R., Jordan L. · in Berwick</div></div><div class="rr"><span class="pill ghost">20 km</span></div></div>
 <div class="btn" id="bk-confirm" style="margin-top:14px">{icon('check', 30, '#F7F7F4')}<span id="bk-ctxt">Confirm · Thu 8:00 AM</span></div>
</div>"""

BOOKED = f"""
<div class="inner">
 <div class="card hi bk-g" style="border-left:7px solid var(--mag)">
  <div style="display:flex;justify-content:space-between;align-items:center"><div class="k" style="font-size:16px">Booked</div><span class="pill mag">Confirmed</span></div>
  <div class="ct" style="font-size:30px;margin-top:8px">Fall cleanup · Dana Keddy</div>
  <div class="cs">Thu Oct 15 · 8:00 AM · Owen's crew</div>
  <div class="cs">14 Belcher St, Kentville</div>
  <div class="cs" style="font-size:17px;margin-top:8px">Confirmed by Sam P. · 8:06 AM</div>
 </div>
 <div class="sl bk-g">Text to Dana · 902-555-0142</div>
 <div class="bk-thread bk-g">
  <div class="bk-dots" id="bk-dots"><i></i><i></i><i></i></div>
  <div class="bk-bub" id="bk-bub">Hi Dana, your fall cleanup is booked for Thu Oct 15 at 8:00 AM. Owen's crew will be there. Reply to this text to change it. – Harlow &amp; Pine</div>
  <div class="bk-dl" id="bk-dl">Delivered · 8:06 AM</div>
 </div>
 <div class="card bk-g" style="margin-top:18px;border-left:7px solid var(--ink)"><div class="tl">From Dana's client record</div>
  <div class="ct" style="font-size:22px;margin-top:6px">Gate code 4471. Dog in the back yard.</div></div>
</div>"""

CSS = r"""
.bk-url{margin:4px 22px 0;height:54px;border-radius:14px;background:#EEF1F2;display:flex;align-items:center;justify-content:center;gap:10px;font:500 21px 'DM Sans';color:#2F4A56}
.bk-url i{display:block;width:13px;height:16px;border:2.5px solid #2F4A56;border-radius:3px}
.bk-me{border:2px solid #12252F;background:#F7F7F4;padding:12px 16px;display:flex;align-items:center;gap:14px;margin-bottom:18px}
.bk-chips{display:flex;gap:12px}
.bk-chips span{border:2px solid #12252F;padding:12px 18px;font:600 22px 'DM Sans';background:#fff}
.bk-chips span.on{background:#12252F;color:#F7F7F4;box-shadow:4px 4px 0 #C2185B}
.bk-doneov{position:absolute;left:0;right:0;top:126px;bottom:0;background:#fff;display:flex;flex-direction:column;align-items:center;padding-top:200px;opacity:0}
.bk-dcheck{width:120px;height:120px;border:5px solid #12252F;box-shadow:8px 8px 0 #C2185B;display:flex;align-items:center;justify-content:center;font:800 64px Manrope;color:#C2185B}
.bk-dt{font:800 42px Manrope;margin-top:40px}
.bk-dd{font:400 23px/1.45 'DM Sans';color:#2F4A56;margin-top:14px;text-align:center;padding:0 60px}
.bk-leg{display:flex;justify-content:space-between;align-items:center;margin:20px 0 10px}
.bk-wkof{font:800 24px Manrope}
.bk-lg{display:flex;gap:14px;font:600 17px 'DM Sans';color:var(--slate)}
.bk-sw{display:inline-block;width:16px;height:16px;background:var(--ink);vertical-align:-2px;margin-right:6px}
.bk-sw.m{background:#fff;border:2px solid #7E96A2;border-left:5px solid #7E96A2}
.bk-wk{display:grid;grid-template-columns:48px repeat(5,1fr);gap:4px}
.bk-dh{text-align:center;font:600 15px 'DM Sans';letter-spacing:.12em;text-transform:uppercase;color:var(--slate);padding:2px 0 6px}
.bk-dh b{display:block;font:800 26px Manrope;color:var(--ink);letter-spacing:0;margin-top:1px}
.bk-dh.on,.bk-dh.on b{color:var(--mag)}
.bk-tm{font:600 15px 'DM Sans';color:var(--slate);padding-top:6px}
.bk-cell{height:96px;background:#EFEBE2;position:relative}
.bk-b{position:absolute;left:4px;right:4px;top:4px;bottom:4px;padding:8px 7px;background:var(--ink);color:var(--paper);overflow:hidden}
.bk-b.m{background:#fff;color:var(--ink);border:2px solid #7E96A2;border-left:6px solid #7E96A2;padding-left:5px}
.bk-b .n,.bk-new .n{font:800 17px/1.15 Manrope;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bk-b .a,.bk-new .a{display:inline-block;font:500 14px 'DM Sans';margin:6px 0 0 -3px;padding:2px 3px 1px;opacity:.85}
.bk-b .a.hit{background:var(--mag);color:#fff;opacity:1}
.bk-new{position:absolute;left:4px;right:4px;top:4px;bottom:4px;padding:7px 6px;border:3px dashed var(--mag);background:#FBE3EC;color:#9E1149;opacity:0}
.bk-new.ok{border-style:solid;background:var(--mag);color:#fff}
.bk-new.ok .a{opacity:1}
.bk-sheet{position:absolute;left:0;right:0;top:700px;z-index:4;background:#fff;border-top:3px solid var(--ink);padding:18px 24px 22px;box-shadow:0 -12px 0 rgba(18,37,47,.07);opacity:0}
.bk-shh{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.bk-yc{font:600 16px 'DM Sans';color:var(--slate);border:1.5px solid #C9C3B6;padding:4px 9px}
.bk-sug{display:flex;align-items:center;gap:14px;padding:12px 12px;border:2px solid transparent;margin-bottom:6px}
.bk-sug.best{border-color:var(--mag);background:#FFF6F9}
#bk-best{border-color:#C9C3B6;color:var(--slate)}
#bk-best.on{background:var(--mag);border-color:var(--mag);color:#fff}
.bk-thread{background:#EEF1F2;padding:20px 20px 16px;min-height:250px;position:relative}
.bk-bub{background:#fff;border:2px solid var(--ink);border-radius:22px 22px 22px 4px;padding:16px 20px;font:400 22px/1.42 'DM Sans';max-width:92%;opacity:0}
.bk-dl{font:600 16px 'DM Sans';color:var(--slate);margin-top:10px;letter-spacing:.06em;opacity:0}
.bk-dots{position:absolute;left:20px;top:20px;display:flex;gap:8px;background:#fff;border:2px solid var(--ink);border-radius:22px;padding:16px 20px;opacity:0}
.bk-dots i{width:12px;height:12px;border-radius:50%;background:var(--mist)}
"""

SCHED = dict(
    name="S02_schedule-booking",
    kicker="Schedule · Booking",
    hook="Fall cleanup request in. Which crew is already nearby Thursday?",
    end="A schedule that knows where every crew is, set up the way your office already books work.",
    caps=[(3.35, 6.45, "Dana books a fall cleanup from your website."),
          (6.45, 9.4, "It lands in Sam's week view, beside every booking."),
          (9.4, 12.3, "Thursday fits. Owen's crew is already in Kentville."),
          (12.3, 15.5, "One tap confirms. Dana gets a text. The crew gets the job.")],
    css=CSS,
    screen=WEB
    + appview("bk-week", "book", WEEK, time="8:05", title="Schedule")
    + appview("bk-booked", "book", BOOKED, time="8:06", title="Schedule",
              extra=toast("bk-toast", "jobs", "Job created ·<br>Fall cleanup, 14&nbsp;Belcher St")),
    callouts="""<div class="callout" id="bk-co" style="left:96px;top:1360px"><div class="ck">One booking, used by</div>
<div class="cr"><i>✓</i>Jobs (Owen's crew phones)</div><div class="cr"><i>✓</i>Clients (Dana's timeline)</div><div class="cr"><i>✓</i>Quotes &amp; invoices</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,12.35,12.8,E.io)*(1-P(t,13.35,13.8,E.io));return {s:L(1,1.08,q),ox:320,oy:560}}
function press(el,t,a){const pr=t>=a&&t<a+.2;el.style.transform=pr?'translate(3px,3px)':'none';el.style.boxShadow=pr?'none':''}
const C0=[239,235,226],C1=[251,227,236];
function renderReel(t){
 // 1. customer books online
 view('bk-web',t,3.0,6.95);
 $('bk-c-fall').classList.toggle('on',t>=3.9);
 typeInto($('bk-addr'),'14 Belcher St, Kentville',t,4.6,5.3);$('bk-addr').classList.toggle('on',t>4.4&&t<5.5);
 $('bk-d-thu').classList.toggle('on',t>=5.6);
 press($('bk-send'),t,6.2);
 S($('bk-doneov'),{o:P(t,6.45,6.7)});S(document.querySelector('.bk-dcheck'),{s:L(.6,1,P(t,6.5,6.9,E.back))});
 // 2. lands in Sam's week view
 view('bk-week',t,6.8,12.0);
 const rq=P(t,7.0,7.4,E.back);S($('bk-req'),{y:L(-24,0,rq),o:P(t,7.0,7.2)});
 grow('.bk-b',t,7.15,.04,.3);
 press($('bk-place'),t,8.1);
 scrollTo($('bk-wscroll'),t,8.45,8.95,150);
 const hq=P(t,8.5,8.8);const c=C0.map((v,i)=>Math.round(L(v,C1[i],hq)));
 document.querySelectorAll('.bk-thu').forEach(e=>e.style.background=`rgb(${c})`);
 $('bk-thuh').classList.toggle('on',t>=8.55);
 const nq=P(t,8.7,9.05,E.back);S($('bk-new'),{s:L(.6,1,nq),o:P(t,8.7,8.85)});
 document.querySelectorAll('.bk-kv').forEach(e=>e.classList.toggle('hit',t>=9.05));
 const sq=P(t,9.15,9.55,E.out);S($('bk-sheet'),{y:L(380,0,sq),o:P(t,9.15,9.3)});
 grow('.bk-sug',t,9.4,.2,.35);
 $('bk-s1').classList.toggle('best',t>=9.95);$('bk-best').classList.toggle('on',t>=9.95);
 press($('bk-confirm'),t,10.95);
 const ok=t>=11.15;$('bk-new').classList.toggle('ok',ok);$('bk-newn').textContent=ok?'✓ Keddy':'Keddy';
 $('bk-ctxt').textContent=ok?'Booked · Owen\'s crew':'Confirm · Thu 8:00 AM';
 // 3. confirmed + text to the customer
 view('bk-booked',t,11.85,15.9);
 grow('.bk-g',t,12.0,.12,.35);
 $('bk-dots').style.opacity=t>=12.3&&t<12.7?1:0;
 const bq=P(t,12.7,13.0,E.back);S($('bk-bub'),{y:L(16,0,bq),o:P(t,12.7,12.85)});
 S($('bk-dl'),{o:P(t,13.1,13.3)});
 callout(t,13.6,15.45,'bk-co','bk-toast');
 handoff(t,14.0,15.6,'bk-toast');
 taps(t,[[3.9,'bk-c-fall'],[4.5,'bk-addr'],[5.6,'bk-d-thu'],[6.2,'bk-send'],[8.1,'bk-place'],[10.95,'bk-confirm']]);
}""")

ALL = [SCHED]
