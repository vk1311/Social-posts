"""S09 — Stock. Invented business Harlow & Pine; invented supplier Valley Turf & Supply; made-up prices.
Story: the yard's stock list with on-hand counts. Job completions from the Jobs app take ice melt bags off the
count; ice melt crosses its reorder point and is flagged Low; a purchase order is drafted and waits for Erin.
Nothing is ordered until she taps Approve. Hand-off to Reports (ice melt cost added to job costs)."""
from suite import appview, toast, icon


def _row(rid, name, sub, n, unit, pct, reorder_pct, mag=False):
    sq = "sk-sq mag" if mag else "sk-sq"
    rida = f' id="{rid}"' if rid else ""
    nid = f' id="{rid}-n"' if rid else ""
    bid = f' id="{rid}-bar"' if rid else ""
    low = f'<span class="pill mag sk-low" id="{rid}-low">Low</span>' if rid else ""
    delta = '<div class="sk-delta" id="sk-delta">−3</div>' if rid else ""
    return (f'<div class="row sk-row"{rida}>{delta}'
            f'<div class="{sq}">{icon("box", 30, "#F7F7F4")}</div>'
            f'<div style="flex:1;min-width:0"><div class="rt">{name}{low}</div><div class="rs">{sub}</div>'
            f'<div class="sk-bar"><i{bid} style="transform:scaleX({pct})"></i><em style="left:{reorder_pct}%"></em></div></div>'
            f'<div class="rr sk-n"><span{nid}>{n}</span><small>{unit}</small></div></div>')


ROWS = (_row("sk-ice", "Ice melt", "20 kg bags · reorder at 30", 41, "bags", 41 / 80, 37.5, mag=True)
        + _row(None, "Sand", "Winter mix · reorder at 6", 14, "yd³", .58, 25)
        + _row(None, "Lawn bags", "Paper, 30 gal · reorder at 100", 240, "bags", .8, 33)
        + _row(None, "Fuel cans", "20 L, full · reorder at 4", 8, "cans", .67, 33)
        + _row(None, "Cutting edges", "Plow blade · reorder at 2", 6, "edges", .6, 20))

EVENTS = [("14 Belcher St · salted", "Owen · job done 6:12 AM", 3),
          ("88 Main St · salted", "Maya · job done 6:25 AM", 2),
          ("3 Orchard Ln · salted", "Jordan · job done 6:41 AM", 4),
          ("210 Highbury Rd · salted", "Theo · job done 6:58 AM", 3)]

FEED = "".join(f'<div class="sk-ev"><div class="sk-evi">{icon("jobs", 24, "#C2185B")}</div>'
               f'<div style="flex:1"><div class="sk-evt">{a}</div><div class="sk-evs">{b}</div></div>'
               f'<div class="sk-evq">−{q} bags</div></div>' for a, b, q in EVENTS)

LIST = f"""
<div class="inner" style="padding-top:20px">
 <div class="sk-head"><div><div class="tl">Kentville yard · on hand</div><div class="sk-hd">Wed Nov 18 · 5 items</div></div>
  <span class="pill soft">Counts from Jobs</span></div>
 <div id="sk-rows">{ROWS}</div>
 <div class="sk-feedh" id="sk-feedh">{icon('jobs', 22, '#C2185B')}<span>Used on jobs today · from the Jobs app</span></div>
 <div id="sk-feed">{FEED}</div>
</div>"""

SHEET = f"""
<div class="sk-dim" id="sk-dim"></div>
<div class="sk-sheet" id="sk-sheet">
 <div class="sk-grab"></div>
 <div class="k">Below reorder point</div>
 <div class="ct" style="font-size:30px;margin-top:6px">Ice melt · 29 bags left</div>
 <div class="cs">Reorder point 30. Purchase order PO-0318 drafted for review. Nothing is ordered yet.</div>
 <div class="btn" id="sk-draft">{icon('pay', 28, '#F7F7F4')} Review draft order</div>
</div>"""

CHECK = '<svg width="30" height="30" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#F7F7F4" stroke-width="2.8"/></svg>'

PO = f"""
<div class="inner" style="padding-top:20px">
 <div class="sk-back sk-p">‹ Stock · Ice melt</div>
 <div class="sk-p" style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:10px">
  <div><div class="k">Purchase order</div><div class="ct" style="font-size:36px;margin-top:4px">PO-0318</div></div>
  <span class="pill soft" id="sk-status">Waiting for Erin</span></div>
 <div class="card sk-p" style="margin-top:16px;margin-bottom:12px"><div class="ct" style="font-size:25px">Valley Turf &amp; Supply</div>
  <div class="cs">New Minas · 902-555-0156 · deliver to Kentville yard</div></div>
 <div class="sk-why sk-p">Drafted from Stock at 7:02 AM · ice melt at 29, reorder point 30</div>
 <table class="items sk-t">
  <tr class="sk-p"><td>Ice melt · 20 kg bag × 60</td><td>$675.00</td></tr>
  <tr class="sub sk-p"><td>Unit price $11.25 CAD</td><td></td></tr>
  <tr class="sub sk-p"><td>HST 14%</td><td>$94.50</td></tr>
  <tr class="tot sk-p"><td>Total</td><td>$769.50</td></tr>
 </table>
 <div class="sk-row2 sk-p">
  <div class="btn ghost sk-edit">Edit</div>
  <div class="btn sk-apv" id="sk-approve"><span id="sk-apt">{CHECK} Approve</span></div>
 </div>
 <div class="sk-small" id="sk-aps">Nothing is ordered until Erin approves.</div>
 <div class="sk-onord" id="sk-onord">{icon('box', 28, '#C2185B')}<div><div class="sk-ot">Ice melt · 60 bags on order</div>
  <div class="sk-os">29 on hand · shown in Stock until delivery</div></div></div>
</div>"""

CSS = r"""
.sk-head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid var(--ink);padding-bottom:12px}
.sk-hd{font:800 27px Manrope;margin-top:4px}
.sk-row{position:relative;padding:15px 0;gap:14px}
.sk-row.lowbg{background:#FBE3EC;box-shadow:-30px 0 0 #FBE3EC,30px 0 0 #FBE3EC}
.sk-sq{width:54px;height:54px;flex:none;background:#2F4A56;display:flex;align-items:center;justify-content:center}
.sk-sq.mag{background:var(--mag)}
.sk-n span{font:800 34px Manrope}
.sk-low{margin-left:10px;vertical-align:3px;opacity:0;display:inline-block}
.sk-bar{position:relative;height:10px;background:#E3DED2;margin-top:9px}
.sk-bar i{position:absolute;left:0;top:0;bottom:0;width:100%;background:#2F4A56;transform-origin:left center}
.sk-bar i.mag{background:var(--mag)}
.sk-bar em{position:absolute;top:-5px;bottom:-5px;width:3px;background:var(--ink)}
.sk-delta{position:absolute;right:66px;top:12px;font:800 30px Manrope;color:var(--mag);opacity:0;z-index:3}
.sk-feedh{display:flex;align-items:center;gap:10px;margin:22px 0 4px;font:600 17px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:var(--mag);opacity:0}
.sk-ev{display:flex;align-items:center;gap:14px;padding:11px 0;border-bottom:1.5px solid #E3DED2;opacity:0}
.sk-evi{width:40px;height:40px;flex:none;background:#FBE3EC;display:flex;align-items:center;justify-content:center}
.sk-evt{font:700 21px Manrope}
.sk-evs{font:400 17px 'DM Sans';color:var(--slate);margin-top:1px}
.sk-evq{font:800 22px Manrope;color:var(--mag);white-space:nowrap}
.sk-dim{position:absolute;left:0;right:0;top:154px;bottom:224px;background:rgba(18,37,47,.45);opacity:0;z-index:7}
.sk-sheet{position:absolute;left:0;right:0;bottom:224px;z-index:8;background:var(--paper);border-top:3px solid var(--ink);
 padding:14px 30px 30px;box-shadow:0 -8px 0 rgba(194,24,91,.9);opacity:0}
.sk-grab{width:80px;height:7px;background:#C9C3B6;margin:0 auto 16px}
.sk-back{font:600 21px 'DM Sans';color:var(--mag)}
.sk-why{border-left:6px solid var(--mag);padding:8px 14px;font:500 20px/1.35 'DM Sans';color:var(--slate)}
.sk-t{margin-top:16px;font-size:22px}
.sk-t td{padding:12px 16px}
.sk-t tr.tot td{font-size:28px}
.sk-row2{display:flex;gap:14px;margin-top:22px}
.sk-edit{width:150px;flex:none;margin-top:0;box-shadow:4px 4px 0 var(--ink)}
.sk-apv{flex:1;margin-top:0}
.sk-small{font:400 19px/1.4 'DM Sans';color:var(--slate);margin-top:14px}
.sk-onord{display:flex;gap:14px;align-items:center;margin-top:18px;border:2px solid var(--ink);background:#fff;padding:14px 16px;opacity:0}
.sk-ot{font:800 23px Manrope}
.sk-os{font:400 18px 'DM Sans';color:var(--slate);margin-top:2px}
"""

STOCK = dict(
    name="S09_stock-inventory",
    kicker="Stock · Inventory",
    hook="Every salted driveway comes off the ice melt count.",
    end="Stock counts that move with the crew's jobs, built around how your yard already runs.",
    caps=[(3.35, 5.9, "Everything in the yard, with what's on hand."),
          (5.9, 8.9, "Each salted driveway in Jobs takes bags off the count."),
          (8.9, 12.0, "Below the reorder point: flagged Low, purchase order drafted."),
          (12.0, 15.5, "Nothing is ordered until Erin taps Approve.")],
    css=CSS,
    screen=appview("sk-list", "stock", LIST, time="7:02", title="Stock", extra=SHEET)
    + appview("sk-po", "stock", PO, time="7:03", title="Stock",
              extra=toast("sk-toast", "rep", "Ice melt cost added to job costs")),
    callouts="""<div class="callout" id="sk-co" style="left:96px;top:1452px"><div class="ck">Approved order, used by</div>
<div class="cr"><i>✓</i>Stock (60 bags on order)</div><div class="cr"><i>✓</i>Reports (job costs)</div></div>""",
    js=r"""
const EVT=[5.7,6.4,7.1,7.8],DQ=[3,2,4,3];
function iceAt(t){let n=41;EVT.forEach((a,i)=>{if(t>=a+.15)n-=Math.min(DQ[i],Math.floor((t-a-.15)/.1)+1)});return n}
const CK='<svg width="30" height="30" viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="#F7F7F4" stroke-width="2.8"/></svg>';
function renderReel(t){
 // ---- view 1: stock list ----
 view('sk-list',t,3.0,10.25);
 grow('.sk-row',t,3.45,.1,.4);
 const fh=P(t,5.25,5.6);S($('sk-feedh'),{y:L(16,0,fh),o:fh});
 grow('.sk-ev',t,EVT[0]-.12,.7,.35);
 const n=iceAt(t);$('sk-ice-n').textContent=n;
 const bar=$('sk-ice-bar');bar.style.transform=`scaleX(${n/80})`;
 const low=n<30;bar.classList.toggle('mag',low);$('sk-ice').classList.toggle('lowbg',low);
 const lp=P(t,8.15,8.45,E.back);S($('sk-ice-low'),{s:L(.5,1,lp),o:lp});
 // floating delta next to the count
 let di=-1;EVT.forEach((a,i)=>{if(t>=a+.05&&t<a+.75)di=i});const d=$('sk-delta');
 if(di<0)d.style.opacity=0;else{const q=P(t,EVT[di]+.05,EVT[di]+.75,E.lin);d.textContent='−'+DQ[di];
  S(d,{y:L(8,-14,q),o:Math.min(1,q*5)*(1-P(t,EVT[di]+.5,EVT[di]+.75))})}
 // low-stock sheet
 const so=P(t,8.75,9.15,E.out);
 S($('sk-sheet'),{y:L(520,0,so),o:t>8.75?1:0});$('sk-dim').style.opacity=so;
 const dr=$('sk-draft');const dp=t>=9.55&&t<9.75;dr.style.transform=dp?'translate(3px,3px)':'none';dr.style.boxShadow=dp?'none':'';
 // ---- view 2: draft purchase order ----
 view('sk-po',t,9.95,15.9);
 grow('.sk-p',t,10.2,.16,.4);
 const ap=$('sk-approve');const apr=t>=13.0&&t<13.2;ap.style.transform=apr?'translate(3px,3px)':'none';
 const done=t>=13.2;ap.style.background=done?'var(--mag)':'';ap.style.boxShadow=apr?'none':(done?'5px 5px 0 var(--ink)':'');
 $('sk-apt').innerHTML=CK+(done?' Approved · sent':' Approve');
 $('sk-aps').textContent=done?'Approved by Erin 7:04 AM · sent to Valley Turf & Supply':'Nothing is ordered until Erin approves.';
 const st=$('sk-status');st.textContent=done?'Sent':'Waiting for Erin';st.className='pill '+(done?'ok':'soft');
 const oo=P(t,13.45,13.8);S($('sk-onord'),{y:L(20,0,oo),o:oo});
 handoff(t,13.35,15.6,'sk-toast');
 callout(t,13.5,15.45,'sk-co','sk-toast');
 taps(t,[[9.55,'sk-draft'],[13.0,'sk-approve']]);
}""")

ALL = [STOCK]
