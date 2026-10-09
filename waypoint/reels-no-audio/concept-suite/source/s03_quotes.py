"""S03 — Quotes & invoicing. Invented business Harlow & Pine; invented customer Dana Keddy; 555 numbers.
Quote Q-1042 built from a saved price list -> sent as a link -> Signed -> one-tap invoice INV-2231
-> e-transfer matched and confirmed -> Paid -> hand-off to Reports."""
from suite import appview, toast, icon

PLUS = icon('plus', 26)
CHECK = icon('check', 26)

NEW = f"""
<div class="inner">
 <div class="qt-head">
  <div><div class="qt-no">Q-1042 · Winter snow service</div><div class="ct">Dana Keddy</div><div class="cs">14 Belcher St, Kentville</div></div>
  <span class="pill ghost">Draft</span>
 </div>
 <div class="sl">Lines</div>
 <div class="qt-lines">
  <div class="qt-ph" id="qt-ph">Tap an item from the price list</div>
  <div class="qt-ln" id="qt-l1"><div><div class="qt-lt">Driveway plowing</div><div class="qt-ls">Full season · Nov–Apr</div></div><b>$540.00</b></div>
  <div class="qt-ln" id="qt-l2"><div><div class="qt-lt">Walkway clearing + salt</div><div class="qt-ls">Full season · Nov–Apr</div></div><b>$180.00</b></div>
 </div>
 <div class="qt-tot">
  <div><span>Subtotal</span><b id="qt-sub">$0.00</b></div>
  <div id="qt-hstrow"><span>HST 14% <em class="qt-auto">auto</em></span><b id="qt-hst">$0.00</b></div>
  <div class="big"><span>Total</span><b id="qt-total">$0.00</b></div>
 </div>
 <div class="sl">Price list · Snow 2026–27</div>
 <div class="qt-pl" id="qt-p1"><div><div class="qt-lt">Driveway plowing</div><div class="qt-ls">Full season</div></div><div class="qt-pp">$540.00</div><div class="qt-add" id="qt-a1">{PLUS}</div></div>
 <div class="qt-pl" id="qt-p2"><div><div class="qt-lt">Walkway clearing + salt</div><div class="qt-ls">Full season</div></div><div class="qt-pp">$180.00</div><div class="qt-add" id="qt-a2">{PLUS}</div></div>
 <div class="qt-pl"><div><div class="qt-lt">Roof snow removal</div><div class="qt-ls">Per visit</div></div><div class="qt-pp">$95.00</div><div class="qt-add">{PLUS}</div></div>
 <div class="qt-pl"><div><div class="qt-lt">Sanding only</div><div class="qt-ls">Per visit</div></div><div class="qt-pp">$45.00</div><div class="qt-add">{PLUS}</div></div>
</div>"""

NEW_ACT = """<div class="qt-act"><div class="btn" id="qt-send"><span id="qt-sendtxt">Send as link</span></div></div>"""

STATUS = f"""
<div class="inner">
 <div class="qt-head">
  <div><div class="qt-no">Q-1042 · Winter snow service</div><div class="ct">Dana Keddy</div><div class="cs">2 lines · HST included</div></div>
 </div>
 <div class="tiles" style="margin-top:18px">
  <div class="tile"><div class="tl">Total</div><div class="tv">$820.80</div></div>
  <div class="tile" id="qt-sttile"><div class="tl">Status</div><div class="tv" id="qt-stv">Sent</div></div>
 </div>
 <div class="qt-steps"><div class="qt-fill" id="qt-fill"></div>
  <div class="qt-sp on"><i></i><span>Draft</span></div>
  <div class="qt-sp on"><i></i><span>Sent</span></div>
  <div class="qt-sp" id="qt-sp3"><i></i><span>Opened</span></div>
  <div class="qt-sp" id="qt-sp4"><i></i><span>Signed</span></div>
 </div>
 <div class="sl">Activity · Oct 8</div>
 <div class="tlx">
  <div class="ev qt-ev" id="qt-e1"><div class="evt">Link sent by text + email</div><div class="evs">9:41 AM · to 902-555-0142</div></div>
  <div class="ev qt-ev" id="qt-e2"><div class="evt">Opened by Dana</div><div class="evs">12:15 PM · on her phone</div></div>
  <div class="ev mag qt-ev" id="qt-e3"><div class="evt">Signed by Dana Keddy</div><div class="evs">4:52 PM · signed copy saved to her file</div></div>
 </div>
 <div class="btn" id="qt-conv">{icon('arrow', 30, '#F7F7F4')} Convert to invoice</div>
 <div class="qt-note" id="qt-note1">Unlocks once the quote is signed</div>
 <div class="qt-note" id="qt-note2">Copies the client, both lines and HST</div>
</div>"""

INVOICE = f"""
<div class="inner" style="position:relative">
 <div class="qt-head">
  <div><div class="qt-no">INV-2231 · from Q-1042</div><div class="ct">Dana Keddy</div><div class="cs">Created Oct 8 · due Oct 31</div></div>
  <span class="pill soft" id="qt-st3">Unpaid</span>
 </div>
 <div class="sl">Lines · copied from Q-1042</div>
 <div class="qt-ln qt-il"><div><div class="qt-lt">Driveway plowing</div><div class="qt-ls">Full season · Nov–Apr</div></div><b>$540.00</b></div>
 <div class="qt-ln qt-il"><div><div class="qt-lt">Walkway clearing + salt</div><div class="qt-ls">Full season · Nov–Apr</div></div><b>$180.00</b></div>
 <div class="qt-tot qt-il">
  <div><span>Subtotal</span><b>$720.00</b></div>
  <div><span>HST 14%</span><b>$100.80</b></div>
  <div class="big"><span>Total</span><b>$820.80</b></div>
 </div>
 <div class="qt-stamp" id="qt-stamp">PAID</div>
 <div class="sl">Payment</div>
 <div class="qt-pay">
  <div class="card" id="qt-wait"><div class="ct" style="font-size:22px">Waiting for payment</div><div class="cs">E-transfer or card · link already with Dana</div></div>
  <div class="card hi" id="qt-etr">
   <div class="qt-er"><div><div class="qt-no" style="margin:0">E-transfer received</div><div class="qt-lt" style="margin-top:6px">From Dana Keddy</div></div><div class="qt-amt">$820.80</div></div>
   <div class="qt-ls" style="margin-top:4px">Oct 9 · 8:06 AM · memo “INV-2231”</div>
   <div class="qt-match" id="qt-match">{icon('check', 24, '#C2185B')}<span>Matches INV-2231 on amount + memo</span></div>
   <div class="qt-bw"><div class="qt-btns" id="qt-btns"><div class="btn sm" id="qt-ok">Confirm match</div><div class="btn sm ghost">Not this one</div></div>
   <div class="qt-done" id="qt-done">{icon('check', 24, '#F7F7F4')}<span>Payment recorded · invoice marked Paid</span></div></div>
  </div>
 </div>
</div>"""

CSS = r"""
.qt-head{display:flex;justify-content:space-between;align-items:flex-start;gap:14px}
.qt-no{font:600 17px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--mag);margin-bottom:6px}
.qt-lines{position:relative;height:164px}
.qt-ph{position:absolute;left:0;right:0;top:0;height:156px;border:2px dashed #C9C3B6;display:flex;align-items:center;justify-content:center;
 font:500 21px 'DM Sans';color:var(--mist)}
.qt-ln{display:flex;justify-content:space-between;align-items:center;height:74px;border:2px solid var(--ink);background:#fff;padding:0 18px;margin-bottom:8px}
.qt-lines .qt-ln{opacity:0}
.qt-ln b{font:800 24px Manrope}
.qt-lt{font:700 22px/1.2 Manrope}
.qt-ls{font:400 17px 'DM Sans';color:var(--slate);margin-top:2px}
.qt-tot{margin-top:6px;border-top:2px solid var(--ink)}
.qt-tot>div{display:flex;justify-content:space-between;align-items:center;padding:8px 6px;font:500 21px 'DM Sans';color:var(--slate)}
.qt-tot b{font:700 22px Manrope;color:var(--ink)}
.qt-tot>.big{border-top:2px solid var(--ink);padding-top:10px}
.qt-tot>.big span{font:800 26px Manrope;color:var(--ink)} .qt-tot>.big b{font:800 32px Manrope}
.qt-auto{font:700 13px 'DM Sans';font-style:normal;letter-spacing:.12em;text-transform:uppercase;background:#FBE3EC;color:#9E1149;padding:3px 7px 2px;margin-left:6px;vertical-align:2px}
#qt-hstrow{transition:none}
.qt-pl{display:flex;align-items:center;gap:16px;padding:11px 8px;border-bottom:1.5px solid #E3DED2}
.qt-pp{margin-left:auto;font:700 22px Manrope}
.qt-add{width:52px;height:52px;flex:none;border:2px solid var(--ink);display:flex;align-items:center;justify-content:center;background:#fff;color:var(--ink)}
.qt-add.on{background:var(--mag);border-color:var(--mag);color:#fff}
.qt-act{position:absolute;left:0;right:0;bottom:224px;padding:14px 30px 18px;background:var(--paper);border-top:2px solid var(--ink);z-index:5}
.qt-act .btn{margin-top:0}
.qt-steps{display:flex;margin:22px 0 4px;position:relative}
.qt-steps:before{content:"";position:absolute;left:12.5%;right:12.5%;top:13px;height:3px;background:#C9C3B6}
.qt-fill{position:absolute;left:12.5%;top:13px;height:3px;width:75%;background:var(--mag);transform-origin:left center}
.qt-sp{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;font:600 17px 'DM Sans';color:var(--mist);position:relative;z-index:1}
.qt-sp i{width:28px;height:28px;border-radius:50%;background:var(--paper);border:3px solid #C9C3B6}
.qt-sp.on{color:var(--ink)} .qt-sp.on i{background:var(--mag);border-color:var(--mag)}
.qt-note{font:500 19px 'DM Sans';color:var(--slate);text-align:center;margin-top:12px}
#qt-note2{margin-top:-34px}
.qt-stamp{position:absolute;left:200px;top:338px;border:5px solid var(--mag);color:var(--mag);font:800 60px Manrope;letter-spacing:.08em;
 padding:4px 20px 0;background:rgba(247,247,244,.82);opacity:0;z-index:3}
.qt-pay{position:relative;height:300px}
.qt-pay .card{position:absolute;left:0;right:0;top:0}
.qt-er{display:flex;justify-content:space-between;align-items:flex-start}
.qt-amt{font:800 34px Manrope}
.qt-match{display:flex;gap:10px;align-items:center;margin-top:12px;padding:10px 12px;background:#FBE3EC;font:600 19px 'DM Sans';color:#9E1149}
.qt-bw{position:relative;height:60px;margin-top:14px}
.qt-btns{position:absolute;left:0;right:0;top:0;display:flex;gap:14px}
.qt-done{position:absolute;left:0;right:0;top:0;display:flex;gap:10px;align-items:center;height:60px;padding:0 16px;background:var(--ink);color:var(--paper);font:700 20px 'DM Sans';opacity:0}
"""

QUOTE = dict(
    name="S03_quotes-invoicing",
    kicker="Quotes · Invoicing",
    hook="Price the driveway, get it signed, match the e-transfer.",
    end="Quotes that turn into invoices from your own price list, built around how you already bill.",
    caps=[(3.35, 6.4, "Tap items from your price list. HST adds itself."),
          (6.4, 9.4, "Send it as a link. Watch the status flip to Signed."),
          (9.4, 12.4, "One tap turns the signed quote into an invoice."),
          (12.4, 15.5, "An e-transfer comes in. You confirm the match. Paid.")],
    css=CSS,
    screen=appview("v-new", "quote", NEW, time="9:40", title="New quote", extra=NEW_ACT)
    + appview("v-q", "quote", STATUS, time="9:41", title="Quotes")
    + appview("v-inv", "quote", INVOICE, time="4:53", title="Invoices",
              extra=toast("qt-toast", "rep", "INV-2231 · $820.80 · October income")),
    callouts="""<div class="callout" id="qt-co" style="left:96px;top:1270px"><div class="ck">One payment, used by</div>
<div class="cr"><i>✓</i>Clients · Dana's timeline</div><div class="cr"><i>✓</i>Reports · October income</div><div class="cr"><i>✓</i>Jobs · season contract</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,8.3,8.75,E.io)*(1-P(t,9.35,9.75,E.io));return {s:L(1,1.07,q),ox:320,oy:330}}
function press(el,on){el.style.transform=on?'translate(3px,3px)':'none';el.style.boxShadow=on?'none':''}
function renderReel(t){
 // ---- 1. build the quote from the price list
 view('v-new',t,3.0,7.35);
 const l1=P(t,4.45,4.8,E.back),l2=P(t,5.45,5.8,E.back);
 S($('qt-l1'),{y:L(-20,0,l1),o:P(t,4.45,4.7)});S($('qt-l2'),{y:L(-20,0,l2),o:P(t,5.45,5.7)});
 $('qt-ph').style.opacity=1-P(t,4.35,4.55);
 const sub=540*P(t,4.5,4.95)+180*P(t,5.5,5.95);
 $('qt-sub').textContent=money(Math.round(sub*100)/100);
 $('qt-hst').textContent=money(Math.round(sub*14)/100);
 $('qt-total').textContent=money(Math.round(sub*114)/100);
 const hp=Math.max(W(t,4.55,5.25,.2),W(t,5.55,6.25,.2));
 $('qt-hstrow').style.background=`rgba(251,227,236,${hp})`;
 [['qt-p1','qt-a1',4.2],['qt-p2','qt-a2',5.2]].forEach(([r,a,ta])=>{
  $(r).style.background=`rgba(251,227,236,${W(t,ta,ta+.55,.15)})`;
  const on=t>=ta+.05;const b=$(a);b.classList.toggle('on',on);b.innerHTML=on?CHK:PLS});
 const sd=$('qt-send');sd.style.opacity=L(.35,1,P(t,5.7,6.0));press(sd,t>=6.65&&t<6.85);
 $('qt-sendtxt').textContent=t>=6.8?'✓ Link sent to Dana':'Send as link';
 // ---- 2. status: sent -> opened -> signed
 view('v-q',t,7.15,10.6);
 $('v-q').querySelector('.sb span').textContent=t<7.95?'9:41':t<8.6?'12:15':'4:52';
 const st=t<7.95?1:t<8.6?2:3;
 $('qt-stv').textContent=['','Sent','Opened','Signed'][st];
 $('qt-stv').style.color=st==3?'var(--mag)':'';
 const sg=P(t,8.6,8.95,E.back);$('qt-sttile').style.boxShadow=`${6*sg}px ${6*sg}px 0 var(--mag)`;
 $('qt-sp3').classList.toggle('on',st>=2);$('qt-sp4').classList.toggle('on',st>=3);
 $('qt-fill').style.transform=`scaleX(${(1+P(t,7.95,8.3)+P(t,8.6,8.95))/3})`;
 S($('qt-e1'),{y:0,o:1});
 [['qt-e2',7.95],['qt-e3',8.6]].forEach(([id,a])=>{const q=P(t,a,a+.4);S($(id),{y:L(24,0,q),o:q})});
 const cu=P(t,8.95,9.25);const cv=$('qt-conv');cv.style.opacity=L(.35,1,cu);press(cv,t>=9.9&&t<10.1);
 $('qt-note1').style.opacity=1-cu;$('qt-note2').style.opacity=cu;
 // ---- 3. invoice INV-2231, e-transfer matched, paid
 view('v-inv',t,10.3,15.9);
 $('v-inv').querySelector('.sb span').textContent=t<11.75?'4:53':'8:07';
 grow('.qt-il',t,10.65,.16,.4);
 const ar=P(t,11.85,12.3,E.back);$('qt-wait').style.opacity=1-P(t,11.75,11.95);
 S($('qt-etr'),{y:L(60,0,ar),o:P(t,11.85,12.15)});
 S($('qt-match'),{x:L(-14,0,P(t,12.25,12.55)),o:P(t,12.25,12.55)});
 press($('qt-ok'),t>=12.85&&t<13.05);
 const dn=P(t,13.15,13.4);$('qt-btns').style.opacity=1-dn;S($('qt-done'),{y:L(12,0,dn),o:dn});
 const pd=t>=13.25;const pl=$('qt-st3');pl.textContent=pd?'Paid':'Unpaid';pl.className='pill '+(pd?'ok':'soft');
 const sp=P(t,13.25,13.55,E.back);S($('qt-stamp'),{s:L(1.7,1,sp),r:-8,o:P(t,13.25,13.4)});
 handoff(t,14.0,15.6,'qt-toast');
 callout(t,13.75,15.45,'qt-co','qt-toast');
 taps(t,[[4.2,'qt-a1'],[5.2,'qt-a2'],[6.65,'qt-send'],[9.9,'qt-conv'],[12.85,'qt-ok']]);
}""".replace("CHK", repr(CHECK)).replace("PLS", repr(PLUS)))

ALL = [QUOTE]
