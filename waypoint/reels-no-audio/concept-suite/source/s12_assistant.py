"""S12 — Assistant (AI). Invented business Harlow & Pine; invented customers Marcel Boudreau, Tom Gallant;
made-up invoices INV-2214 / INV-2218. The AI only answers and drafts; Erin approves every reminder."""
from suite import appview, toast, icon

CSS = r"""
.ai-chat{padding:20px 26px 0}
.ai-day{text-align:center;font:600 15px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:var(--mist);margin:0 0 16px}
.ai-rv{overflow:hidden}
.ai-rv>.msg{margin-bottom:0}
.ai-rv{padding-bottom:14px}
.msg.ai-wide{max-width:100%}
.ai-sw{position:relative}
.ai-sw.cur:after{content:"";position:absolute;right:-15px;top:3px;width:10px;height:24px;background:var(--mag)}
.ai-dots{display:inline-flex;gap:9px;padding:20px 22px;border:2px solid var(--ink);border-left:7px solid var(--mag);background:#fff}
.ai-dots i{display:block;width:12px;height:12px;border-radius:50%;background:var(--mag)}
.ai-list{overflow:hidden}
.ai-iv{display:flex;align-items:center;gap:14px;padding:13px 0;border-top:1.5px solid #E3DED2}
.ai-iv:first-child{margin-top:12px}
.ai-iv .av{width:48px;height:48px;font-size:17px}
.ai-ivn{font:700 22px Manrope}.ai-ivs{font:400 17px 'DM Sans';color:var(--slate);margin-top:2px}
.ai-iva{margin-left:auto;text-align:right;font:800 23px Manrope;white-space:nowrap}
.ai-iva small{display:block;font:600 15px 'DM Sans';color:var(--mag);letter-spacing:.04em}
.ai-srcs{overflow:hidden}
.ai-srck{font:600 14px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:var(--slate);margin:14px 0 8px}
.ai-src{display:inline-flex;align-items:center;gap:8px;border:2px solid var(--ink);background:#F7F7F4;padding:6px 12px 6px 8px;font:600 18px 'DM Sans';margin-right:8px}
.ai-src b{font-weight:700;color:var(--mag)}
.ai-revb{display:inline-flex;align-items:center;gap:10px;margin-top:14px;background:var(--ink);color:var(--paper);font:800 21px Manrope;padding:14px 18px;box-shadow:4px 4px 0 var(--mag)}
.ai-bar{position:absolute;left:0;right:0;bottom:224px;height:104px;background:var(--paper);border-top:2px solid var(--ink);display:flex;align-items:center;gap:12px;padding:0 22px;z-index:5}
.ai-in{flex:1;height:66px;border:2px solid var(--ink);background:#fff;padding:0 18px;display:flex;align-items:center;font:500 23px 'DM Sans';white-space:nowrap;overflow:hidden}
.ai-in.on{border-color:var(--mag);box-shadow:4px 4px 0 var(--mag)}
.ai-ph{color:var(--mist)}
.ai-send{width:66px;height:66px;flex:none;background:var(--mag);display:flex;align-items:center;justify-content:center}
/* drafts view */
.ai-lead{font:400 19px/1.4 'DM Sans';color:var(--slate);margin:-2px 0 16px}
.ai-dr{border:2px solid var(--ink);background:#fff;padding:16px 18px;margin-bottom:18px}
.ai-dr.hi{box-shadow:6px 6px 0 var(--mag)}
.ai-drh{display:flex;align-items:center;gap:12px}
.ai-tag{font:800 15px 'DM Sans';letter-spacing:.14em;padding:5px 9px 4px;border:2.5px dashed var(--mag);color:var(--mag);background:#FBE3EC}
.ai-tag.q{border:2.5px solid var(--ink);background:var(--ink);color:#fff}
.ai-drn{font:800 23px Manrope}
.ai-dra{margin-left:auto;font:800 23px Manrope}
.ai-drs{font:400 17px 'DM Sans';color:var(--slate);margin-top:6px}
.ai-subj{font:700 19px 'DM Sans';margin-top:12px;padding-top:12px;border-top:1.5px solid #E3DED2}
.ai-subj span{font-weight:500;color:var(--slate)}
.ai-txt{font:400 20px/1.45 'DM Sans';margin-top:10px;background:#FAF8F3;border:1.5px solid #E3DED2;padding:12px 14px}
.ai-txt p+p{margin-top:8px}
#ai-w{display:inline-block;padding:0 3px;margin:0 -3px}
#ai-w.sel{background:var(--mag);color:#fff}
#ai-w.ed{box-shadow:inset 0 -3px 0 var(--mag)}
.ai-ed{font:600 15px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-top:8px;opacity:0}
.ai-acts{display:flex;gap:12px;margin-top:14px}
.ai-acts .btn{margin-top:0}
.btn.ai-done{background:#2F4A56;box-shadow:none}
.ai-prev{font:400 19px 'DM Sans';color:var(--slate);margin-top:10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ai-foot{display:flex;gap:12px;align-items:center;font:600 18px/1.35 'DM Sans';color:var(--ink);border-left:6px solid var(--mag);padding:6px 0 6px 14px}
"""


def sw(text):
    """Words as spans so the reply can stream in word by word without re-flowing."""
    return " ".join(f'<span class="ai-sw">{w}</span>' for w in text.split())


CHAT = f"""
<div class="ai-chat" id="ai-chat">
 <div class="ai-day">Today · 8:14 AM</div>
 <div class="ai-rv"><div class="msg ai"><div class="who">Assistant</div>Hi Erin. Ask about clients, jobs, invoices or the schedule. I draft; you decide.</div></div>
 <div class="ai-rv" id="ai-me1"><div class="msg me">Who still owes us from September?</div></div>
 <div class="ai-rv" id="ai-d1"><div class="ai-dots"><i></i><i></i><i></i></div></div>
 <div class="ai-rv" id="ai-a1"><div class="msg ai ai-wide"><div class="who">Assistant</div>
  <div id="ai-s1">{sw("Two September invoices are still open, $798.00 in total:")}</div>
  <div class="ai-list" id="ai-list">
   <div class="ai-iv"><div class="av">MB</div><div><div class="ai-ivn">Marcel Boudreau</div><div class="ai-ivs">INV-2214 · fall aeration · due Sep 30</div></div><div class="ai-iva">$456.00<small>9 days late</small></div></div>
   <div class="ai-iv"><div class="av l">TG</div><div><div class="ai-ivn">Tom Gallant</div><div class="ai-ivs">INV-2218 · hedge trim · due Sep 30</div></div><div class="ai-iva">$342.00<small>9 days late</small></div></div>
  </div>
  <div class="ai-srcs" id="ai-srcs"><div class="ai-srck">Sources</div>
   <span class="ai-src">{icon('money', 24, '#C2185B')}from <b>Quotes &amp; invoices</b></span><span class="ai-src">{icon('crm', 24, '#C2185B')}<b>Clients</b></span></div>
 </div></div>
 <div class="ai-rv" id="ai-me2"><div class="msg me">Draft a friendly reminder for each</div></div>
 <div class="ai-rv" id="ai-d2"><div class="ai-dots"><i></i><i></i><i></i></div></div>
 <div class="ai-rv" id="ai-a2"><div class="msg ai ai-wide"><div class="who">Assistant</div>
  <div id="ai-s2">{sw("Two drafts are ready, one per client. Nothing is sent until you approve each one.")}</div>
  <div class="ai-srcs" id="ai-rvw"><div class="ai-revb" id="ai-review">Review 2 drafts {icon('arrow', 26, '#F7F7F4')}</div></div>
 </div></div>
 <div style="height:40px"></div>
</div>"""

BAR = f"""<div class="ai-bar"><div class="ai-in" id="ai-in"></div><div class="ai-send" id="ai-send">{icon('arrow', 32, '#fff')}</div></div>"""

DRAFTS = f"""
<div class="inner">
 <div class="sl" style="margin-top:4px">2 drafts · waiting for Erin</div>
 <div class="ai-lead">Written by the Assistant from INV-2214 and INV-2218. Edit anything before you approve.</div>
 <div class="ai-dr hi" id="ai-c1">
  <div class="ai-drh"><span class="ai-tag" id="ai-t1">DRAFT</span><div class="ai-drn">Marcel Boudreau</div><div class="ai-dra">$456.00</div></div>
  <div class="ai-subj"><span>Subject:</span> Friendly reminder · INV-2214</div>
  <div class="ai-txt">
   <p>Hi Marcel,</p>
   <p>Just a friendly reminder that invoice INV-2214 for your fall aeration ($456.00) is still open. You can pay by e-transfer, or reply with any questions.</p>
   <p><span id="ai-w">Thanks,</span><br>Erin · Harlow &amp; Pine</p>
  </div>
  <div class="ai-ed" id="ai-ed">Edited by Erin</div>
  <div class="ai-acts"><div class="btn sm ghost" style="flex:0 0 120px">Skip</div><div class="btn sm" id="ai-ok1"><span id="ai-ok1t">Approve &amp; queue</span></div></div>
 </div>
 <div class="ai-dr" id="ai-c2">
  <div class="ai-drh"><span class="ai-tag" id="ai-t2">DRAFT</span><div class="ai-drn">Tom Gallant</div><div class="ai-dra">$342.00</div></div>
  <div class="ai-prev">Hi Tom, just a friendly reminder that INV-2218 for your hedge trim…</div>
  <div class="ai-acts"><div class="btn sm ghost" style="flex:0 0 120px">Open</div><div class="btn sm" id="ai-ok2"><span id="ai-ok2t">Approve &amp; queue</span></div></div>
 </div>
 <div class="ai-foot">{icon('ai', 30, '#C2185B')}<span>The Assistant drafts. Nothing goes out until you approve it.</span></div>
</div>"""

ASSISTANT = dict(
    name="S12_ai-assistant",
    kicker="Assistant · AI drafts",
    hook="Ask who still owes you. Get names, not a dashboard.",
    end="An assistant that drafts from your own records and waits for your yes, built around your office's routine.",
    caps=[(3.35, 6.4, "Erin asks a plain question. No report to build."),
          (6.4, 9.4, "The answer comes from her own invoices, sources shown."),
          (9.4, 12.0, "She asks for reminders. The assistant only drafts them."),
          (12.0, 15.5, "Erin changes a word and approves each one herself.")],
    css=CSS,
    screen=appview("ai-v1", "ai", CHAT, time="8:14", title="Assistant", extra=BAR)
    + appview("ai-v2", "ai", DRAFTS, time="8:16", title="Assistant · drafts",
              extra=toast("ai-toast", "quote", "2 reminders queued · sent from your address")),
    callouts="""<div class="callout" id="ai-co" style="left:96px;top:1250px"><div class="ck">One question, read from</div>
<div class="cr"><i>✓</i>Quotes &amp; invoices</div><div class="cr"><i>✓</i>Clients (who to email)</div><div class="cr"><i>✓</i>Jobs (what was done)</div></div>""",
    js=r"""
function rv(id,t,a,d){// reveal: grow height from 0 so the chat pushes up like a real thread
 const el=$(id);if(t<a){el.style.display='none';return 0}
 el.style.display='';const q=P(t,a,a+(d||.32),E.out);el.style.maxHeight='none';const h=el.scrollHeight;
 el.style.maxHeight=(q>=1?'none':(h*q)+'px');const k=el.firstElementChild;if(k)S(k,{y:L(18,0,q),o:q});return q}
function rvOut(id,t,b){if(t>=b)$(id).style.display='none'}
function stream(id,t,a,b){const ws=[...$(id).querySelectorAll('.ai-sw')];const n=ws.length;let last=-1;
 ws.forEach((w,i)=>{const s=a+(b-a)*i/n;const q=P(t,s,s+.1,E.lin);w.style.opacity=q;if(t>=s)last=i;w.classList.remove('cur')});
 if(last>=0&&t<b+.35&&t>=a)ws[last].classList.add('cur')}
function dots(id,t){$(id).querySelectorAll('i').forEach((d,i)=>{d.style.opacity=.3+.7*Math.max(0,Math.sin((t*7-i*.9)))})}
function press(el,t,a){const pr=t>=a&&t<a+.2;el.style.transform=pr?'translate(3px,3px)':'none';el.style.boxShadow=pr?'none':''}
function renderReel(t){
 // ---- 1. chat
 view('ai-v1',t,3.0,11.4);
 const inp=$('ai-in');
 if(t<3.95||(t>=5.3&&t<7.95)||t>=9.1)inp.innerHTML='<span class="ai-ph">Ask about your business…</span>';
 if(t>=3.95&&t<5.3)typeInto(inp,'Who still owes us from September?',t,3.95,5.0);
 if(t>=7.95&&t<9.1)typeInto(inp,'Draft a friendly reminder for each',t,7.95,8.85);
 inp.classList.toggle('on',(t>3.75&&t<5.3)||(t>7.75&&t<9.1));
 press($('ai-send'),t,t<7?5.2:9.0);
 rv('ai-me1',t,5.3);
 rv('ai-d1',t,5.45,.2);rvOut('ai-d1',t,5.95);dots('ai-d1',t);
 rv('ai-a1',t,5.95,.25);stream('ai-s1',t,6.0,6.8);
 rv('ai-list',t,6.8,.4);grow('#ai-list .ai-iv',t,6.85,.16,.35);
 rv('ai-srcs',t,7.3,.3);
 rv('ai-me2',t,9.1);
 rv('ai-d2',t,9.25,.2);rvOut('ai-d2',t,9.6);dots('ai-d2',t);
 rv('ai-a2',t,9.6,.25);stream('ai-s2',t,9.65,10.3);
 rv('ai-rvw',t,10.3,.3);press($('ai-review'),t,10.75);
 // keep the newest message just above the input bar
 const ch=$('ai-chat'),vis=$('ai-v1-body').offsetHeight-104;
 ch.style.transform=`translateY(${-Math.max(0,ch.scrollHeight-vis)}px)`;
 // ---- 2. drafts: Erin edits one word, approves each
 view('ai-v2',t,11.1,15.9);
 grow('#ai-v2 .ai-dr',t,11.25,.18,.4);S(document.querySelector('#ai-v2 .ai-foot'),{o:P(t,11.7,12.1)});
 const w=$('ai-w');
 if(t<12.05){w.textContent='Thanks,';w.className=t>=11.85?'sel':''}
 else{typeInto(w,'Cheers,',t,12.05,12.45);w.className='ed';if(t>12.75)w.textContent='Cheers,'}
 S($('ai-ed'),{y:L(-8,0,P(t,12.55,12.85)),o:P(t,12.55,12.85)});
 [['ai-ok1','ai-ok1t','ai-t1',12.95],['ai-ok2','ai-ok2t','ai-t2',13.6]].forEach(([b,bt,tg,a])=>{
  press($(b),t,a);const q=t>=a+.18;$(b).classList.toggle('ai-done',q);
  $(bt).textContent=q?'✓ Approved · queued':'Approve & queue';
  $(tg).textContent=q?'QUEUED':'DRAFT';$(tg).classList.toggle('q',q)});
 handoff(t,13.9,15.6,'ai-toast');
 callout(t,14.0,15.45,'ai-co','ai-toast');
 taps(t,[[3.85,'ai-in'],[5.2,'ai-send'],[7.85,'ai-in'],[9.0,'ai-send'],[10.75,'ai-review'],[11.75,'ai-w'],[12.95,'ai-ok1'],[13.6,'ai-ok2']]);
}""")

ALL = [ASSISTANT]
