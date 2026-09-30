"""The four scheduled Waypoint reels. Invented business (Harlow & Pine) and customers throughout."""
from shell import sb, PHONE_ICON, MSG_ICON

BIZ_BAR = '<div class="appbar"><div class="mono">H&amp;P</div><div><div class="bizname">{t}</div><div class="bizsub">{s}</div></div></div>'
SIG = ("M 40 118 C 52 70, 70 38, 86 44 C 104 52, 92 112, 70 124 C 54 132, 50 108, 72 96 C 98 82, 120 94, 118 112 "
       "C 116 126, 132 124, 146 100 C 154 86, 160 96, 158 112 C 156 126, 172 120, 186 100 C 196 86, 204 90, 202 108 "
       "C 200 124, 214 124, 230 104 M 272 42 C 266 74, 258 104, 252 132 M 318 56 C 298 78, 280 92, 262 98 "
       "C 282 104, 300 120, 320 128 C 338 134, 352 112, 366 104 C 380 96, 386 112, 376 120 C 364 128, 354 108, 378 100 "
       "C 398 94, 414 114, 444 106 C 474 98, 494 90, 508 84")

# ------------------------------------------------------------------ R1 signing
R1 = dict(
    name="R1_quote-signed",
    kicker="Quotes",
    hook="Signed at 6:40 in the morning, on a phone, in a truck.",
    end="The signed PDF is emailed to you and to them the moment they tap sign.",
    caps=[(3.35, 5.2, "6:40am. The quote arrives as a link."),
          (5.2, 8.0, "They read the whole thing on their phone."),
          (8.0, 11.0, "Type a name. Sign with a finger."),
          (11.0, 15.5, "The signed PDF lands in both inboxes.")],
    screen=f"""
<div class="view" id="v-lock" style="background:#17303B;color:#F7F7F4">{sb('6:40', True)}
 <div class="lockdate">Tuesday, September 29</div><div class="locktime">6:40</div>
 <div class="notif" id="r1notif"><div class="nicon">{MSG_ICON}</div><div><div class="ntop"><b>Harlow &amp; Pine Property</b><span>now</span></div>
 <div class="ntext">Your winter snow quote is ready. Tap to review and sign.</div></div></div>
</div>
<div class="view app" id="v-quote">{sb('6:40')}{BIZ_BAR.format(t='Harlow &amp; Pine', s='Property Services')}
 <div class="banner" id="r1banner"><b>✓</b>&nbsp; Signed by Dana Keddy · 6:41 AM</div>
 <div class="scrollwrap"><div id="r1scroll"><div class="pad">
  <div class="k">Quote · Q-1042</div><h2>Winter 2026–27 snow service</h2>
  <div class="meta">For Dana Keddy<br>14 Belcher St, Kentville</div>
  <table class="items">
   <tr><td>Driveway plowing, full season</td><td>$540.00</td></tr>
   <tr><td>Walkway clearing + salt</td><td>$180.00</td></tr>
   <tr class="sub"><td>Subtotal</td><td>$720.00</td></tr>
   <tr class="sub"><td>HST 14%</td><td>$100.80</td></tr>
   <tr class="tot"><td>Total</td><td>$820.80</td></tr></table>
  <div class="valid">Valid until October 31, 2026</div>
  <div class="k" style="margin:34px 0 16px">Sign to accept</div>
  <div class="field"><label>Full name</label><div class="input" id="r1name"></div></div>
  <div class="sigbox" id="r1sigbox"><div class="sigx">×</div><div class="sigline"></div>
   <svg width="532" height="166" viewBox="0 0 532 166"><path id="r1sig" d="{SIG}" fill="none" stroke="#12252F" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
  <div class="btn" id="r1btn">Sign quote</div>
 </div></div></div>
</div>
<div class="view mail" id="v-inbox">{sb('6:41')}
 <div class="mhead"><div class="mback">‹ Mailboxes</div><div class="mtitle">Inbox</div></div>
 <div class="mrow" id="r1mail"><i class="mdot"></i><div class="mfrom"><b>Harlow &amp; Pine · Quotes</b><span>6:41 AM</span></div>
  <div class="msub">Signed: Q-1042 — Dana Keddy</div><div class="mprev">Accepted at 6:41 AM. Signed copy attached.</div>
  <div class="chip" id="r1chip"><span class="pdf">PDF</span>Q-1042-signed.pdf</div></div>
 <div id="r1old">
  <div class="mrow"><div class="mfrom"><b>Supplier</b><span>Yesterday</span></div><div class="msub">Order #4471 has shipped</div><div class="mprev">Two pallets of ice melt, arriving Thursday.</div></div>
  <div class="mrow"><div class="mfrom"><b>Fuel card</b><span>Yesterday</span></div><div class="msub">Monthly statement ready</div><div class="mprev">Your September statement is available.</div></div>
  <div class="mrow"><div class="mfrom"><b>Equipment dealer</b><span>Mon</span></div><div class="msub">Blade parts in stock</div><div class="mprev">Cutting edges for the 8 ft blade are back in.</div></div>
 </div>
</div>""",
    callouts="""<div class="callout" id="co1" style="left:96px;top:1190px"><div class="ck">Signed copy sent to</div>
<div class="cr"><i>✓</i>Harlow &amp; Pine office</div><div class="cr"><i>✓</i>Dana Keddy, customer</div></div>""",
    js=r"""
let SIGLEN=0,MAILH=0;
function initReel(){const p=$('r1sig');SIGLEN=p.getTotalLength();p.style.strokeDasharray=SIGLEN;MAILH=$('r1mail').offsetHeight}
function zoomAt(t){const q=P(t,7.95,8.5,E.io)*(1-P(t,10.55,11.0,E.io));return {s:L(1,1.1,q),ox:320,oy:720}}
function renderReel(t){
 view('v-lock',t,3.0,5.15);
 const np=P(t,3.85,4.3,E.back);S($('r1notif'),{y:L(-70,0,np),o:Math.min(1,np)*(1-P(t,4.85,5.05))});
 view('v-quote',t,4.95,11.25);
 $('r1scroll').style.transform=`translateY(${L(0,-352,P(t,6.6,7.7,E.io))}px)`;
 typeInto($('r1name'),'Dana Keddy',t,8.05,8.85);$('r1name').classList.toggle('on',t>7.95&&t<9.0);
 const sp=P(t,9.0,9.95,E.io);$('r1sig').style.strokeDashoffset=SIGLEN*(1-sp);
 const btn=$('r1btn');const pr=t>=10.2&&t<10.42;btn.style.transform=pr?'translate(3px,3px)':'none';btn.style.boxShadow=pr?'none':'';
 btn.innerHTML=t>=10.42?'<span style="color:#C2185B">✓</span> Signed · 6:41 AM':'Sign quote';
 S($('r1banner'),{y:L(-60,0,P(t,10.45,10.8)),o:P(t,10.45,10.8)});
 view('v-inbox',t,11.0,15.9);
 const mp=P(t,11.55,12.0,E.out);S($('r1mail'),{y:L(-24,0,mp),o:mp});$('r1old').style.transform=`translateY(${L(-MAILH,0,mp)}px)`;
 callout(t,12.35,15.45,'co1','r1chip');
 const active=taps(t,[[4.7,'r1notif'],[8.0,'r1name'],[10.2,'r1btn']]);
 if(!active&&t>=8.95&&t<=10.05){const p=$('r1sig'),pt=p.getPointAtLength(SIGLEN*sp),b=rel($('r1sigbox'));
  finger(b.x-b.w/2+2+pt.x,b.y-b.h/2+2+pt.y,Math.min(P(t,8.95,9.05),1-P(t,9.95,10.05)))}
}""")

# ------------------------------------------------------------------ R2 missed call
R2 = dict(
    name="R2_missed-call",
    kicker="Missed calls",
    hook="The call you didn't catch.",
    end="Every missed call gets a text back in seconds. Automatically.",
    caps=[(3.35, 5.9, "7:12am. You're on a roof. It rings out."),
          (5.9, 8.8, "A text goes back to them. Automatically."),
          (8.8, 10.8, "They reply with what they need."),
          (10.8, 15.5, "It lands in your enquiries. Not in voicemail.")],
    css="""
.callsmall{text-align:center;font:600 20px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:#7E96A2;margin-top:66px}
.callnum{text-align:center;font:800 56px Manrope;margin-top:14px}
.callloc{text-align:center;font:500 24px 'DM Sans';color:#7E96A2;margin-top:8px}
.avwrap{position:absolute;left:217px;top:360px;width:170px;height:170px}
.avwrap i{position:absolute;inset:0;border-radius:50%;border:3px solid rgba(247,247,244,.5)}
.av{position:absolute;inset:0;border-radius:50%;background:#2F4A56;display:flex;align-items:center;justify-content:center;font:800 60px Manrope;color:#F7F7F4}
.callbtns{position:absolute;left:0;right:0;top:700px;display:flex;justify-content:space-around;padding:0 70px}
.cb{display:flex;flex-direction:column;align-items:center;gap:12px;font:500 22px 'DM Sans'}
.cb div{width:112px;height:112px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#F7F7F4}
.cb.dec div{background:#C2185B} .cb.dec svg{transform:rotate(135deg)} .cb.acc div{background:#7E96A2}
.missed{position:absolute;left:0;right:0;top:716px;text-align:center;font:800 38px Manrope;color:#C2185B;opacity:0}
.missed span{display:block;font:500 24px 'DM Sans';color:#7E96A2;margin-top:10px}
.thead{padding:10px 0 20px;text-align:center;border-bottom:1px solid #DDE2E4}
.tav{width:70px;height:70px;border-radius:50%;background:#12252F;color:#F7F7F4;font:800 24px Manrope;display:flex;align-items:center;justify-content:center;margin:0 auto 8px}
.tname{font:700 24px 'DM Sans'} .tnum{font:400 19px 'DM Sans';color:#2F4A56;margin-top:2px}
.thread{display:flex;flex-direction:column;gap:10px;padding:24px 26px}
.sys{align-self:center;font:500 19px 'DM Sans';color:#7E96A2;margin-bottom:8px}
.bub{max-width:440px;padding:16px 20px;border-radius:26px;font:400 25px/1.36 'DM Sans';transform-origin:left bottom}
.bub.in{background:#E8ECEE;color:#12252F;align-self:flex-start;border-bottom-left-radius:8px}
.bub.out{background:#12252F;color:#F7F7F4;align-self:flex-end;border-bottom-right-radius:8px;transform-origin:right bottom}
.typing{display:flex;gap:8px;padding:20px 22px}
.typing i{width:14px;height:14px;border-radius:50%;background:#7E96A2}
.ts{font:500 18px 'DM Sans';color:#7E96A2;padding-left:10px} .ts.r{align-self:flex-end;padding-right:10px}
.tabs{display:flex;gap:28px;padding:18px 34px 0;border-bottom:2px solid #12252F;font:600 22px 'DM Sans';color:#2F4A56}
.tabs span{padding-bottom:14px} .tabs span.on{color:#12252F;border-bottom:6px solid #C2185B;margin-bottom:-2px}
.tabs b{display:inline-block;min-width:30px;margin-left:6px;background:#C2185B;color:#fff;font:800 17px Manrope;padding:3px 8px;text-align:center}
.ecard{border:2px solid #12252F;box-shadow:6px 6px 0 #12252F;background:#fff;padding:20px 22px;margin-bottom:22px}
.ephone{font:800 34px Manrope;margin-top:8px}
.equote{font:500 24px/1.4 'DM Sans';margin-top:10px;border-left:4px solid #C2185B;padding-left:14px}
.eauto{font:500 18px 'DM Sans';color:#2F4A56;margin-top:12px;letter-spacing:.02em}
.ebtns{display:flex;gap:14px;margin-top:18px}
.erow{display:flex;justify-content:space-between;align-items:center;padding:20px 4px;border-top:1px solid rgba(18,37,47,.18);font:400 21px 'DM Sans';color:#2F4A56}
.erow b{font:700 23px 'DM Sans';color:#12252F}
""",
    screen=f"""
<div class="view" id="v-call" style="background:#17303B;color:#F7F7F4">{sb('7:12', True)}
 <div class="callsmall">Work line · Harlow &amp; Pine</div><div class="callnum">(902) 555-0148</div><div class="callloc">Kentville, NS</div>
 <div class="avwrap"><i id="rg0"></i><i id="rg1"></i><i id="rg2"></i><div class="av">?</div></div>
 <div class="callbtns" id="r2btns"><div class="cb dec"><div>{PHONE_ICON}</div>Decline</div><div class="cb acc"><div id="r2acc">{PHONE_ICON}</div>Accept</div></div>
 <div class="missed" id="r2missed">Missed call<span>7:12 AM · no voicemail</span></div>
</div>
<div class="view" id="v-msg" style="background:#fff;color:#12252F">{sb('7:12')}
 <div class="thead"><div class="tav">HP</div><div class="tname">Harlow &amp; Pine</div><div class="tnum">(902) 555-0100</div></div>
 <div class="thread">
  <div class="sys">Outgoing call · no answer · 7:12 AM</div>
  <div class="bub in typing" id="r2typing"><i></i><i></i><i></i></div>
  <div class="bub in" id="r2in">Hi, it's Harlow &amp; Pine. Sorry we missed you, we're out on a job. What can we help with? Reply here and we'll get back to you today.</div>
  <div class="ts" id="r2ts">7:12 AM</div>
  <div class="bub out" id="r2out">Need a quote for plowing. 22 Cornwallis St.</div>
  <div class="ts r" id="r2del">Delivered · 7:13 AM</div>
 </div>
</div>
<div class="view app" id="v-crm">{sb('7:13')}{BIZ_BAR.format(t='Enquiries', s='Harlow &amp; Pine')}
 <div class="tabs"><span class="on">New<b id="r2count">0</b></span><span>Quoted</span><span>Won</span></div>
 <div class="pad" style="padding-top:24px">
  <div class="ecard" id="r2card"><div class="k">New · from missed call</div><div class="ephone">(902) 555-0148</div>
   <div class="equote">“Need a quote for plowing. 22 Cornwallis St.”</div>
   <div class="eauto">Call 7:12 AM · auto-text sent 7:12 AM · reply 7:13 AM</div>
   <div class="ebtns"><div class="btn sm">Call back</div><div class="btn sm ghost">Start quote</div></div></div>
  <div id="r2older">
   <div class="erow"><b>14 Belcher St</b><span>Quoted · Sep 28</span></div>
   <div class="erow"><b>47 Chipman Dr</b><span>Quoted · Sep 27</span></div>
   <div class="erow"><b>8 Webster St</b><span>Won · Sep 25</span></div>
  </div></div>
</div>""",
    callouts="""<div class="callout" id="co2" style="left:96px;top:1215px"><div class="ck">Logged together</div>
<div class="cr"><i>✓</i>The missed call, with the time</div><div class="cr"><i>✓</i>The text that went back</div><div class="cr"><i>✓</i>Their reply</div></div>""",
    js=r"""
let CARDH=0;
function initReel(){CARDH=$('r2card').offsetHeight+22}
function zoomAt(t){const q=P(t,6.2,6.8,E.io)*(1-P(t,10.3,10.8,E.io));return {s:L(1,1.08,q),ox:320,oy:520}}
function renderReel(t){
 view('v-call',t,3.0,6.15);
 const ringing=t<5.25;
 [0,1,2].forEach(i=>{const ph=((t*1.05)+i/3)%1;S($('rg'+i),{s:L(1,1.85,ph),o:ringing?(1-ph)*.9:0})});
 const buzz=ringing?Math.sin(t*38)*3*(Math.floor(t*1.6)%2):0;S($('r2acc'),{x:buzz});
 S($('r2btns'),{o:1-P(t,5.15,5.4)});S($('r2missed'),{y:L(16,0,P(t,5.35,5.7)),o:P(t,5.35,5.7)});
 view('v-msg',t,5.9,10.95);
 show($('r2typing'),t>=6.4&&t<7.25);
 document.querySelectorAll('#r2typing i').forEach((d,i)=>{S(d,{y:-7*Math.max(0,Math.sin(t*7-i*.8))})});
 show($('r2in'),t>=7.25);S($('r2in'),{s:L(.9,1,P(t,7.25,7.55,E.back)),o:P(t,7.25,7.45)});
 show($('r2ts'),t>=7.4);S($('r2ts'),{o:P(t,7.4,7.7)});
 show($('r2out'),t>=9.0);S($('r2out'),{s:L(.9,1,P(t,9.0,9.3,E.back)),o:P(t,9.0,9.2)});
 show($('r2del'),t>=9.35);S($('r2del'),{o:P(t,9.35,9.65)});
 view('v-crm',t,10.8,15.9);
 const cp=P(t,11.35,11.8,E.out);S($('r2card'),{y:L(-30,0,cp),o:cp});$('r2older').style.transform=`translateY(${L(-CARDH,0,cp)}px)`;
 $('r2count').textContent=t>=11.4?'1':'0';
 callout(t,12.3,15.45,'co2','r2card','r');
 taps(t,[]);
}""")

# ------------------------------------------------------------------ R3 mark paid
R3 = dict(
    name="R3_mark-paid",
    kicker="Invoicing",
    hook="Mark it paid.",
    end="Marking it paid sends the receipt. You don't write a second email.",
    caps=[(3.35, 5.6, "The e-Transfer came in. Open the invoice."),
          (5.6, 8.4, "Tap Mark paid. Pick how they paid."),
          (8.4, 10.9, "The receipt builds itself and sends."),
          (10.9, 15.5, "They have proof. You have the date.")],
    css="""
.tabs{display:flex;gap:28px;padding:18px 34px 0;border-bottom:2px solid #12252F;font:600 22px 'DM Sans';color:#2F4A56}
.tabs span{padding-bottom:14px} .tabs span.on{color:#12252F;border-bottom:6px solid #C2185B;margin-bottom:-2px}
.tabs b{font:800 18px Manrope;margin-left:6px}
.irow{display:flex;justify-content:space-between;align-items:center;padding:22px 34px;border-bottom:1px solid rgba(18,37,47,.18);background:var(--paper)}
.inum{font:600 18px 'DM Sans';letter-spacing:.12em;color:#2F4A56} .iname{font:700 26px 'DM Sans';margin-top:4px}
.iright{text-align:right} .iamt{font:800 28px Manrope}
.pill{display:inline-block;margin-top:6px;border:2px solid #7E96A2;color:#2F4A56;font:700 15px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;padding:4px 10px}
.pill.paid{border-color:#C2185B;color:#fff;background:#C2185B}
.pill.big{font-size:19px;padding:7px 14px}
.bigamt{font:800 80px/1 Manrope;letter-spacing:-.02em;margin:14px 0 14px}
.items.slim{font-size:21px;margin-top:22px} .items.slim td{padding:11px 14px}
.stamp{position:absolute;left:374px;top:196px;font:800 58px Manrope;color:#C2185B;border:6px solid #C2185B;padding:4px 20px;letter-spacing:.06em;opacity:0;z-index:4}
.shade{position:absolute;inset:0;background:rgba(18,37,47,.45);opacity:0;z-index:6}
.sheet{position:absolute;left:0;right:0;top:440px;height:1100px;background:#F7F7F4;border-top:4px solid #12252F;padding:28px 34px;z-index:7}
.opt{height:84px;border:2px solid #12252F;margin-top:14px;display:flex;align-items:center;padding:0 24px;font:700 27px 'DM Sans';background:#fff}
.opt.sel{background:#12252F;color:#F7F7F4;box-shadow:5px 5px 0 #C2185B}
.sdate{font:500 21px 'DM Sans';color:#2F4A56;margin-top:22px}
.prog{margin-top:26px;opacity:0} .pl{font:600 21px 'DM Sans';color:#2F4A56}
.pbar{height:14px;border:2px solid #12252F;margin-top:10px;background:#fff} .pbar b{display:block;height:100%;width:0;background:#C2185B}
.toast{margin-top:18px;background:#12252F;color:#F7F7F4;font:700 23px 'DM Sans';padding:18px 22px;border-left:8px solid #C2185B;opacity:0}
.msubj{font:800 34px/1.2 Manrope;margin:6px 0 18px}
.mfrom2{display:flex;gap:16px;align-items:center;font:400 19px 'DM Sans';color:#2F4A56}
.mfrom2 b{font:700 23px 'DM Sans';color:#12252F;display:block}
.tav{width:58px;height:58px;border-radius:50%;background:#12252F;color:#F7F7F4;font:800 20px Manrope;display:flex;align-items:center;justify-content:center;flex:none}
.doc{margin-top:30px;border:2px solid #12252F;box-shadow:8px 8px 0 #12252F;background:#fff;opacity:0}
.dhead{background:#12252F;color:#F7F7F4;display:flex;align-items:center;gap:16px;padding:14px 20px}
.dhead .mono{background:#F7F7F4;color:#12252F;width:44px;height:44px;font-size:16px}
.dbody{padding:22px 24px 26px}
.dpaid{font:600 18px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:#C2185B}
.damt{font:800 60px/1.05 Manrope;margin:8px 0 12px}
.dline{font:400 21px/1.5 'DM Sans';color:#2F4A56}
.dthanks{font:700 22px 'DM Sans';margin-top:14px}
""",
    screen=f"""
<div class="view app" id="v-list">{sb('9:05')}{BIZ_BAR.format(t='Invoices', s='Harlow &amp; Pine')}
 <div class="tabs"><span class="on">All</span><span>Unpaid<b>3</b></span><span>Paid</span></div>
 <div class="irow" id="r3row"><div><div class="inum">INV-2087</div><div class="iname">Dana Keddy</div></div><div class="iright"><div class="iamt">$820.80</div><div class="pill">Unpaid</div></div></div>
 <div class="irow"><div><div class="inum">INV-2086</div><div class="iname">M. Coldwell</div></div><div class="iright"><div class="iamt">$295.00</div><div class="pill">Unpaid</div></div></div>
 <div class="irow"><div><div class="inum">INV-2085</div><div class="iname">A. Sheehan</div></div><div class="iright"><div class="iamt">$410.00</div><div class="pill paid">Paid</div></div></div>
 <div class="irow"><div><div class="inum">INV-2084</div><div class="iname">J. Borden</div></div><div class="iright"><div class="iamt">$1,140.00</div><div class="pill">Unpaid</div></div></div>
</div>
<div class="view app" id="v-inv">{sb('9:05')}
 <div class="appbar"><div class="aback">‹</div><div><div class="bizname">INV-2087</div><div class="bizsub">Dana Keddy</div></div></div>
 <div class="pad">
  <div class="k">Invoice · INV-2087</div><div class="bigamt">$820.80</div>
  <div class="meta">Dana Keddy · 14 Belcher St, Kentville<br>Issued Oct 1 · Due Oct 31</div>
  <div style="margin-top:16px"><span class="pill big" id="r3pill">Unpaid</span></div>
  <table class="items slim"><tr><td>Driveway plowing, season</td><td>$540.00</td></tr>
   <tr><td>Walkway + salt</td><td>$180.00</td></tr><tr class="sub"><td>HST 14%</td><td>$100.80</td></tr></table>
  <div class="btn" id="r3btn" style="margin-top:26px">Mark paid</div>
  <div class="prog" id="r3prog"><div class="pl" id="r3pl">Building receipt R-2087…</div><div class="pbar"><b id="r3bar"></b></div></div>
  <div class="toast" id="r3toast">✓&nbsp; Receipt sent to Dana Keddy</div>
 </div>
 <div class="stamp" id="r3stamp">PAID</div>
 <div class="shade" id="r3shade"></div>
 <div class="sheet" id="r3sheet"><div class="k">How was it paid?</div>
  <div class="opt" id="r3etr">e-Transfer</div><div class="opt">Cheque</div><div class="opt">Card</div><div class="opt">Cash</div>
  <div class="sdate">Paid on · Today, October 13</div></div>
</div>
<div class="view mail" id="v-rcpt">{sb('9:06')}
 <div class="mhead"><div class="mback">‹ Inbox</div></div>
 <div class="pad" style="padding-top:4px">
  <div class="msubj">Receipt for INV-2087 — paid in full</div>
  <div class="mfrom2"><div class="tav">HP</div><div><b>Harlow &amp; Pine</b>to Dana Keddy · 9:06 AM</div></div>
  <div class="chip"><span class="pdf">PDF</span>Receipt-R-2087.pdf</div>
  <div class="doc" id="r3doc"><div class="dhead"><div class="mono">H&amp;P</div><div class="k" style="color:#F7F7F4">Receipt · R-2087</div></div>
   <div class="dbody"><div class="dpaid">Paid in full</div><div class="damt">$820.80</div>
   <div class="dline">e-Transfer · October 13, 2026</div><div class="dline">Invoice INV-2087 · 14 Belcher St</div>
   <div class="dthanks">Thank you, Dana.</div></div></div>
 </div>
</div>""",
    callouts="""<div class="callout" id="co3" style="left:96px;top:1215px"><div class="ck">In your records</div>
<div class="cr"><i>✓</i>Paid October 13, 2026</div><div class="cr"><i>✓</i>Method: e-Transfer</div><div class="cr"><i>✓</i>Receipt R-2087 sent</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,6.35,6.9,E.io)*(1-P(t,8.25,8.8,E.io));return {s:L(1,1.08,q),ox:320,oy:760}}
function renderReel(t){
 view('v-list',t,3.0,5.75);
 $('r3row').style.background=(t>=4.95&&t<5.7)?'#E3E8E9':'';
 view('v-inv',t,5.55,11.05);
 $('r3shade').style.opacity=P(t,6.75,7.0)*(1-P(t,7.95,8.2));
 $('r3sheet').style.transform=`translateY(${L(1150,0,P(t,6.75,7.15,E.out))+L(0,1150,P(t,7.95,8.3,E.in))}px)`;
 $('r3etr').classList.toggle('sel',t>=7.62);
 const paid=t>=8.3;const pill=$('r3pill');pill.textContent=paid?'Paid':'Unpaid';pill.classList.toggle('paid',paid);
 const st=P(t,8.3,8.7,E.back);S($('r3stamp'),{s:L(1.9,1,st),r:-8,o:P(t,8.3,8.45)});
 const btn=$('r3btn');const pr=t>=6.6&&t<6.82;btn.style.transform=pr?'translate(3px,3px)':'none';btn.style.boxShadow=pr?'none':'';
 btn.classList.toggle('ghost',paid);btn.innerHTML=paid?'<span style="color:#C2185B">✓</span> Paid · e-Transfer':'Mark paid';
 S($('r3prog'),{o:P(t,8.85,9.05)});$('r3bar').style.width=(100*P(t,9.0,9.7,E.io))+'%';
 $('r3pl').textContent=t>=9.7?'Receipt R-2087 ready':'Building receipt R-2087…';
 S($('r3toast'),{y:L(20,0,P(t,9.8,10.15,E.back)),o:P(t,9.8,10.0)});
 view('v-rcpt',t,10.9,15.9);
 const dp=P(t,11.45,11.95,E.out);S($('r3doc'),{y:L(70,0,dp),r:L(0,-1.4,dp),o:dp});
 callout(t,12.35,15.45,'co3','r3doc','r');
 taps(t,[[5.1,'r3row'],[6.6,'r3btn'],[7.6,'r3etr']]);
}""")

# ------------------------------------------------------------------ R4 request form to route
PINS = [(60, 330), (112, 282), (170, 302), (222, 242), (282, 262), (322, 202), (382, 216), (430, 160), (474, 192), (522, 130), (562, 164)]
NEWPIN = (486, 300)
route_d = "M" + " L".join(f"{x} {y}" for x, y in PINS)
pins_svg = "".join(
    f'<g transform="translate({x} {y})"><rect x="-15" y="-15" width="30" height="30" fill="#12252F"/>'
    f'<text y="6" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="15" fill="#F7F7F4">{i+1}</text></g>'
    for i, (x, y) in enumerate(PINS))
MAP = f"""<svg width="604" height="400" viewBox="0 0 604 400" style="display:block">
<rect width="604" height="400" fill="#EEF1F0"/>
{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="400" stroke="rgba(126,150,162,.22)" stroke-width="1"/>' for x in range(40, 604, 40))}
{''.join(f'<line x1="0" y1="{y}" x2="604" y2="{y}" stroke="rgba(126,150,162,.22)" stroke-width="1"/>' for y in range(40, 400, 40))}
<g stroke="#D3DADD" stroke-width="16" fill="none" stroke-linecap="round">
<path d="M-10 350 L614 250"/><path d="M40 -10 L210 410"/><path d="M300 -10 L360 410"/><path d="M-10 120 L614 60"/><path d="M450 -10 L560 410"/></g>
<path d="{route_d}" fill="none" stroke="#C2185B" stroke-width="5" stroke-linejoin="round"/>
<path id="r4ext" d="M{PINS[-1][0]} {PINS[-1][1]} L{NEWPIN[0]} {NEWPIN[1]}" fill="none" stroke="#C2185B" stroke-width="5" stroke-dasharray="6 0"/>
{pins_svg}
<circle id="r4pulse" cx="{NEWPIN[0]}" cy="{NEWPIN[1]}" r="20" fill="none" stroke="#C2185B" stroke-width="4"/>
<g id="r4pin"><g transform="translate({NEWPIN[0]} {NEWPIN[1]})"><rect x="-20" y="-20" width="40" height="40" fill="#C2185B" stroke="#12252F" stroke-width="3"/>
<text y="7" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="19" fill="#fff">12</text></g></g>
</svg>"""

R4 = dict(
    name="R4_request-to-route",
    kicker="Bookings",
    hook="From your website to the route. Without retyping.",
    end="A request becomes a stop on the route, address already on it.",
    caps=[(3.35, 6.1, "A customer fills in the form on your website."),
          (6.1, 9.7, "Address, service, notes. Typed once, by them."),
          (9.9, 12.6, "It lands on your route. Address already on it."),
          (12.6, 15.5, "Every driver sees it on the next run.")],
    css="""
.urlbar{margin:4px 22px 0;height:54px;border-radius:14px;background:#EEF1F2;display:flex;align-items:center;justify-content:center;gap:10px;font:500 21px 'DM Sans';color:#2F4A56}
.urlbar i{display:block;width:13px;height:16px;border:2.5px solid #2F4A56;border-radius:3px}
.chips{display:flex;gap:12px}
.chips span{border:2px solid #12252F;padding:12px 18px;font:600 22px 'DM Sans';background:#fff}
.chips span.on{background:#12252F;color:#F7F7F4;box-shadow:4px 4px 0 #C2185B}
.done{position:absolute;left:0;right:0;top:126px;bottom:0;background:#fff;display:flex;flex-direction:column;align-items:center;padding-top:190px;opacity:0}
.dcheck{width:120px;height:120px;border:5px solid #12252F;box-shadow:8px 8px 0 #C2185B;display:flex;align-items:center;justify-content:center;font:800 64px Manrope;color:#C2185B}
.dt{font:800 42px Manrope;margin-top:40px} .dd{font:400 23px/1.45 'DM Sans';color:#2F4A56;margin-top:14px;text-align:center;padding:0 60px}
.map{border-bottom:2px solid #12252F}
.rrow{display:flex;gap:18px;align-items:center;padding:18px 26px;border-bottom:1px solid rgba(18,37,47,.18);background:#F7F7F4;position:relative}
.rn{width:40px;height:40px;flex:none;background:#12252F;color:#F7F7F4;font:800 18px Manrope;display:flex;align-items:center;justify-content:center}
.ra{font:700 24px 'DM Sans'} .rs{font:400 19px 'DM Sans';color:#2F4A56;margin-top:3px}
.rrow.new{background:#fff;border-left:8px solid #C2185B;padding-left:18px}
.rrow.new .rn{background:#C2185B}
.tag{position:absolute;right:22px;top:16px;font:700 14px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:#C2185B;border:2px solid #C2185B;padding:3px 8px}
""",
    screen=f"""
<div class="view" id="v-form" style="background:#fff;color:#12252F">{sb('8:02')}
 <div class="urlbar"><i></i>harlowpine.ca/request</div>
 <div class="pad" style="padding-top:22px">
  <div class="k">Harlow &amp; Pine</div><h2 style="margin:6px 0 20px">Request snow service</h2>
  <div class="field"><label>Name</label><div class="input" id="r4f1"></div></div>
  <div class="field"><label>Address</label><div class="input" id="r4f2"></div></div>
  <div class="field"><label>Mobile</label><div class="input" id="r4f3"></div></div>
  <div class="field"><label>Service</label><div class="chips"><span id="r4c1">Driveway</span><span id="r4c2">Walkway</span><span>Salt only</span></div></div>
  <div class="field"><label>Notes</label><div class="input" id="r4f4"></div></div>
  <div class="btn" id="r4sub">Send request</div>
 </div>
 <div class="done" id="r4done"><div class="dcheck">✓</div><div class="dt">Request received</div><div class="dd">Harlow &amp; Pine will text you at (902) 555-0193 to confirm.</div></div>
</div>
<div class="view app" id="v-route">{sb('8:03')}
 <div class="appbar"><div class="mono">H&amp;P</div><div><div class="bizname">Tuesday route</div><div class="bizsub" id="r4count">11 stops</div></div></div>
 <div class="map">{MAP}</div>
 <div class="rrow new" id="r4new"><div class="rn">12</div><div><div class="ra">31 Prospect Ave</div><div class="rs">Driveway + walkway · Gate on the left</div></div><div class="tag">New · website</div></div>
 <div id="r4old">
  <div class="rrow"><div class="rn">1</div><div><div class="ra">8 Webster St</div><div class="rs">Driveway</div></div></div>
  <div class="rrow"><div class="rn">2</div><div><div class="ra">47 Chipman Dr</div><div class="rs">Driveway + salt</div></div></div>
  <div class="rrow"><div class="rn">3</div><div><div class="ra">14 Belcher St</div><div class="rs">Driveway + walkway</div></div></div>
  <div class="rrow"><div class="rn">4</div><div><div class="ra">22 Cornwallis St</div><div class="rs">Driveway</div></div></div>
 </div>
</div>""",
    callouts="""<div class="callout" id="co4" style="left:96px;top:1235px"><div class="ck">Typed once, by them</div>
<div class="cr"><i>✓</i>31 Prospect Ave, Kentville</div><div class="cr"><i>✓</i>Driveway + walkway</div><div class="cr"><i>✓</i>Gate on the left</div></div>""",
    js=r"""
let NEWH=0,EXTLEN=0;
function initReel(){NEWH=$('r4new').offsetHeight;const e=$('r4ext');EXTLEN=e.getTotalLength();e.style.strokeDasharray=EXTLEN}
function zoomAt(t){const q=P(t,4.6,5.1,E.io)*(1-P(t,8.7,9.2,E.io));return {s:L(1,1.07,q),ox:320,oy:640}}
function renderReel(t){
 view('v-form',t,3.0,10.05);
 const F=[['r4f1','Priya Nair',4.0,4.6,3.9,4.75],['r4f2','31 Prospect Ave, Kentville',4.9,6.0,4.8,6.15],
          ['r4f3','(902) 555-0193',6.3,6.85,6.2,6.95],['r4f4','Long driveway. Gate on the left.',7.8,8.6,7.7,8.75]];
 F.forEach(f=>{typeInto($(f[0]),f[1],t,f[2],f[3]);$(f[0]).classList.toggle('on',t>f[4]&&t<f[5])});
 $('r4c1').classList.toggle('on',t>=7.05);$('r4c2').classList.toggle('on',t>=7.4);
 const sub=$('r4sub');const pr=t>=8.95&&t<9.15;sub.style.transform=pr?'translate(3px,3px)':'none';sub.style.boxShadow=pr?'none':'';
 const dn=P(t,9.15,9.45);S($('r4done'),{o:dn});S(document.querySelector('.dcheck'),{s:L(.6,1,P(t,9.2,9.6,E.back))});
 view('v-route',t,9.9,15.9);
 const pp=P(t,10.55,10.95,E.back);$('r4pin').setAttribute('transform',`translate(0 ${L(-130,0,pp)})`);$('r4pin').style.opacity=P(t,10.55,10.65);
 const ph=t>11.0?((t-11.0)*.9)%1:0;$('r4pulse').setAttribute('r',L(20,48,ph));$('r4pulse').style.opacity=t>11.0?(1-ph):0;
 $('r4ext').style.strokeDashoffset=EXTLEN*(1-P(t,10.95,11.45,E.io));
 $('r4count').textContent=t>=11.0?'12 stops':'11 stops';
 const np=P(t,11.3,11.75,E.out);S($('r4new'),{y:L(-24,0,np),o:np});$('r4old').style.transform=`translateY(${L(-NEWH,0,np)}px)`;
 callout(t,12.35,15.45,'co4','r4new');
 taps(t,[[3.95,'r4f1'],[4.85,'r4f2'],[6.25,'r4f3'],[7.05,'r4c1'],[7.4,'r4c2'],[7.75,'r4f4'],[8.95,'r4sub']]);
}""")

ALL = [R1, R2, R3, R4]
