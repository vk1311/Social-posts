"""S08 — Helpdesk (customer messages). Invented business Harlow & Pine; invented customers + crew; 555 numbers.
Continuity: Tom Gallant (210 Highbury Rd, 902-555-0163) from S01's client list; Owen Cleveland is crew lead."""
from suite import appview, toast, icon

# channel icons (24x24, currentColor)
CH = {
    "sms": '<rect x="6.5" y="2.5" width="11" height="19" rx="2" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M10 18h4" stroke="currentColor" stroke-width="2.2"/>',
    "web": '<rect x="3" y="4" width="18" height="16" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3 8.5h18M7 12.5h10M7 16h6" stroke="currentColor" stroke-width="2.2"/>',
}


def ch(name, size=30, color="currentColor"):
    if name == "mail":
        return icon("mail", size, color)
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" style="color:{color};flex:none">{CH[name]}</svg>'


INBOX = f"""
<div class="inner">
 <div class="hd-top"><div><div class="ct" style="font-size:30px">Inbox</div><div class="cs" style="margin-top:2px">Thu Nov 12 · first snowfall</div></div>
  <div class="rr">3 new<small>all channels</small></div></div>
 <div class="hd-chips">
  <div class="hd-chip on">All · 3</div>
  <div class="hd-chip">{ch('sms', 20)}Text · 1</div>
  <div class="hd-chip">{ch('web', 20)}Web form · 1</div>
  <div class="hd-chip">{ch('mail', 20)}Email · 1</div>
 </div>
 <div class="row h-in" id="h-tom"><div class="hd-ch sms">{ch('sms', 30, '#fff')}</div>
  <div class="hd-mid"><div class="rt">Tom Gallant</div><div class="hd-pv">Plow missed the end of my driveway</div><div class="hd-src">Text · 902-555-0163</div></div>
  <div class="rr">6:48<small><i class="hd-dot"></i></small></div></div>
 <div class="row h-in"><div class="hd-ch">{ch('web', 30, '#fff')}</div>
  <div class="hd-mid"><div class="rt">Rosa Fitzgerald</div><div class="hd-pv">Can you salt the front walkway too?</div><div class="hd-src">Web form · booking page</div></div>
  <div class="rr">6:31<small><i class="hd-dot"></i></small></div></div>
 <div class="row h-in"><div class="hd-ch">{ch('mail', 30, '#fff')}</div>
  <div class="hd-mid"><div class="rt">Jack Whynot</div><div class="hd-pv">Re: INV-2241 · sent by e-transfer</div><div class="hd-src">Email</div></div>
  <div class="rr">6:12<small><i class="hd-dot"></i></small></div></div>
 <div class="sl h-old">Earlier · resolved</div>
 <div class="row h-old" style="opacity:.55"><div class="hd-ch" style="background:#7E96A2">{ch('sms', 30, '#fff')}</div>
  <div class="hd-mid"><div class="rt">Lena Comeau</div><div class="hd-pv">Are you plowing on Park St tonight?</div><div class="hd-src" style="color:var(--slate)">Text · yesterday</div></div>
  <div class="rr"><span class="pill ok">Done</span></div></div>
 <div class="tiles h-old" style="margin-top:22px">
  <div class="tile"><div class="tl">Open</div><div class="tv">3</div><div class="cs" style="font-size:17px">Text, web form, email</div></div>
  <div class="tile"><div class="tl">Waiting on crew</div><div class="tv">1</div><div class="cs" style="font-size:17px">Linked to Jobs</div></div>
 </div>
</div>"""

TICKET = f"""
<div class="hd-th">
 <div><div class="k" style="font-size:16px">H-318 · Text message</div><div class="ct" style="font-size:25px;margin-top:4px">Plow missed the end of my driveway</div></div>
 <span class="pill" id="h-status">Open</span>
</div>
<div class="hd-sw"><div id="h-scroll"><div class="inner" style="padding-top:20px">
 <div class="hd-bub">Plow missed the end of my driveway. Can't get the car out.
  <div class="hd-bm">{ch('sms', 18, '#C2185B')} Tom Gallant · 6:48 AM · 902-555-0163</div></div>
 <div class="sl" style="display:flex;justify-content:space-between"><span>Linked automatically</span><span style="color:var(--slate);letter-spacing:.08em">by phone number</span></div>
 <div class="hd-lk h-lk" id="h-lc"><div class="av">TG</div>
  <div class="hd-mid"><div class="rt" style="font-size:23px">Tom Gallant</div><div class="rs" style="font-size:18px">210 Highbury Rd, Kentville</div></div>
  <span class="pill ghost">Client</span></div>
 <div class="hd-lk h-lk" id="h-lj"><div class="hd-jb">{icon('jobs', 30, '#F7F7F4')}</div>
  <div class="hd-mid"><div class="rt" style="font-size:23px">Plow job · last night</div><div class="rs" style="font-size:18px">Route stop 7 · Owen's crew · 11:52 PM</div></div>
  <span class="pill ghost">Job</span></div>
 <div class="sl">Assigned to</div>
 <div style="position:relative">
  <div class="input" id="h-asg" style="gap:12px"><span id="h-asgv" style="color:var(--mist)">Unassigned</span><span style="margin-left:auto;color:var(--slate);font-size:20px">▾</span></div>
  <div class="hd-dd" id="h-dd">
   <div class="hd-ddr" id="h-ddo"><div class="av m" style="width:44px;height:44px;font-size:16px">OC</div><div><b>Owen Cleveland</b><small>Crew lead · route stop 7</small></div></div>
   <div class="hd-ddr"><div class="av l" style="width:44px;height:44px;font-size:16px">MR</div><div><b>Maya Ross</b><small>Crew</small></div></div>
   <div class="hd-ddr"><div class="av" style="width:44px;height:44px;font-size:16px">JL</div><div><b>Jordan Lantz</b><small>Crew</small></div></div>
  </div>
 </div>
 <div class="sl">Reply · by text</div>
 <div class="hd-srs"><span class="hd-srl">Saved replies</span><span class="hd-sr" id="h-sr">Missed spot</span><span class="hd-sr">Running late</span></div>
 <div class="hd-rep" id="h-rep"><span id="h-hint" style="color:var(--mist)">Write a reply…</span><span id="h-tpl">Hi Tom, sorry we missed it. </span><span class="hd-ph" id="h-ph">[Crew] will be back by [time].</span><span id="h-typed"></span></div>
 <div class="btn" id="h-send">{ch('sms', 28, '#F7F7F4')} Send by text</div>
 <div style="height:260px"></div>
</div></div></div>"""

DETAIL = f"""
<div class="inner">
 <div class="hd-top" style="align-items:flex-start;gap:14px"><div><div class="k" style="font-size:16px">H-318 · Tom Gallant</div>
  <div class="ct" style="font-size:25px;margin-top:4px">Plow missed the end of my driveway</div></div>
  <span class="pill soft" id="h-st3">Waiting</span></div>
 <div class="hd-trk">
  <div class="hd-step on"><i>{icon('check', 22, '#fff')}</i><span>Open</span></div>
  <div class="hd-bar"><b style="transform:scaleX(1)"></b></div>
  <div class="hd-step on"><i>{icon('check', 22, '#fff')}</i><span>Waiting</span></div>
  <div class="hd-bar"><b id="h-bar2"></b></div>
  <div class="hd-step" id="h-s2"><i>{icon('check', 22, '#fff')}</i><span>Resolved</span></div>
 </div>
 <div class="sl">Activity</div>
 <div class="tlx">
  <div class="ev"><div class="evt">Text received · linked to Tom</div><div class="evs">6:48 AM · client record + last night's job</div></div>
  <div class="ev"><div class="evt">Assigned to Owen · reply sent</div><div class="evs">6:55 AM · saved reply, edited by Sam</div></div>
  <div class="ev mag h-ev"><div class="evt">Owen marked the revisit done</div><div class="evs">9:38 AM · from the Jobs app · 1 photo</div></div>
  <div class="ev h-ev"><div class="evt">Status: Resolved</div><div class="evs">9:38 AM · set when the revisit was done</div></div>
 </div>
</div>"""

CSS = r"""
.hd-top{display:flex;justify-content:space-between;align-items:flex-end}
.hd-chips{display:flex;gap:9px;margin:18px 0 4px}
.hd-chip{display:flex;align-items:center;gap:6px;border:2px solid #C9C3B6;padding:7px 11px 6px;font:700 17px 'DM Sans';color:var(--slate);white-space:nowrap;background:#fff}
.hd-chip.on{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.hd-ch{width:58px;height:58px;flex:none;background:#2F4A56;display:flex;align-items:center;justify-content:center}
.hd-ch.sms{background:var(--mag)}
.hd-mid{flex:1;min-width:0}
.hd-pv{font:500 20px 'DM Sans';color:var(--ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;margin-top:3px}
.hd-src{font:700 14px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:var(--mag);margin-top:5px}
.hd-dot{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--mag);margin-top:8px}
.hd-th{position:absolute;left:0;right:0;top:0;height:132px;z-index:3;background:var(--paper);border-bottom:2px solid #E3DED2;
 padding:18px 30px 14px;display:flex;gap:14px;justify-content:space-between;align-items:flex-start}
.hd-sw{position:absolute;left:0;right:0;top:132px;bottom:0;overflow:hidden}
.hd-bub{background:#fff;border:2px solid var(--ink);border-left:7px solid var(--mag);padding:14px 18px 12px;font:600 23px/1.35 'DM Sans'}
.hd-bm{display:flex;align-items:center;gap:8px;font:500 17px 'DM Sans';color:var(--slate);margin-top:8px}
.hd-lk{display:flex;gap:14px;align-items:center;border:2px solid var(--ink);background:#fff;padding:13px 16px;margin-bottom:14px;box-shadow:5px 5px 0 var(--mag)}
.hd-jb{width:58px;height:58px;flex:none;background:var(--ink);display:flex;align-items:center;justify-content:center}
.hd-dd{position:absolute;left:0;right:0;top:66px;z-index:4;background:#fff;border:2px solid var(--ink);box-shadow:6px 6px 0 var(--ink);opacity:0}
.hd-ddr{display:flex;align-items:center;gap:12px;padding:11px 14px;border-bottom:1.5px solid #E3DED2;font:400 21px 'DM Sans'}
.hd-ddr b{display:block;font:700 21px Manrope}
.hd-ddr small{display:block;font:400 16px 'DM Sans';color:var(--slate)}
.hd-srs{display:flex;align-items:center;gap:10px;margin-bottom:12px}
.hd-srl{font:600 17px 'DM Sans';color:var(--slate)}
.hd-sr{border:2px solid var(--ink);background:#fff;padding:7px 13px 6px;font:700 18px 'DM Sans';box-shadow:3px 3px 0 var(--ink)}
.hd-rep{border:2px solid var(--ink);background:#fff;min-height:118px;padding:14px 18px;font:500 23px/1.4 'DM Sans';white-space:normal}
.hd-rep.on{border-color:var(--mag);box-shadow:4px 4px 0 var(--mag)}
.hd-ph{background:#FBE3EC;color:#9E1149;font-weight:700}
.hd-trk{display:flex;align-items:flex-start;margin:22px 0 4px}
.hd-step{display:flex;flex-direction:column;align-items:center;gap:8px;width:110px;flex:none;font:700 18px 'DM Sans';color:var(--slate)}
.hd-step i{width:44px;height:44px;border:2.5px solid var(--ink);background:#fff;display:flex;align-items:center;justify-content:center}
.hd-step i svg{opacity:0}
.hd-step.on{color:var(--ink)} .hd-step.on i{background:var(--mag);border-color:var(--mag)} .hd-step.on i svg{opacity:1}
.hd-bar{flex:1;height:5px;background:#E3DED2;margin:20px -26px 0}
.hd-bar b{display:block;height:100%;background:var(--mag);transform-origin:left center;transform:scaleX(0)}
"""

HELP = dict(
    name="S08_helpdesk",
    kicker="Helpdesk · Customer messages",
    hook="Plow missed a driveway. The text reaches the right crew.",
    end="One inbox that already knows your clients and routes, built around the way your office answers them.",
    caps=[(3.35, 6.35, "Texts, web forms and emails land in one inbox."),
          (6.35, 9.0, "Already linked: Tom's client record and last night's plow job."),
          (9.0, 12.3, "Assign it to Owen. Edit a saved reply. Send."),
          (12.3, 15.5, "Waiting until Owen marks the revisit done. Then Resolved.")],
    css=CSS,
    screen=appview("h-v1", "help", INBOX, time="6:52", title="Helpdesk")
    + appview("h-v2", "help", TICKET, time="6:54", title="Helpdesk")
    + appview("h-v3", "help", DETAIL, time="9:41", title="Helpdesk",
              extra=toast("h-toast", "jobs", "Revisit created · 210 Highbury Rd")),
    callouts="""<div class="callout" id="hco" style="left:96px;top:1290px"><div class="ck">This ticket also shows in</div>
<div class="cr"><i>✓</i>Clients (Tom's timeline)</div><div class="cr"><i>✓</i>Jobs (revisit on Owen's route)</div><div class="cr"><i>✓</i>Reports (tickets by route)</div></div>""",
    js=r"""
function zoomAt(t){const q=P(t,6.75,7.2,E.io)*(1-P(t,8.0,8.4,E.io));return {s:L(1,1.08,q),ox:320,oy:660}}
function setPill(el,cls,txt){el.className='pill'+(cls?' '+cls:'');el.textContent=txt}
function renderReel(t){
 // inbox
 view('h-v1',t,3.0,6.45);
 grow('.h-in',t,3.55,.4,.45);
 grow('.h-old',t,4.9,.12,.4);document.querySelectorAll(".row.h-old").forEach(r=>r.style.opacity=Math.min(+r.style.opacity,.55));
 $('h-tom').style.background=(t>=5.9&&t<6.35)?'#FBE3EC':'transparent';
 // ticket
 view('h-v2',t,6.3,12.95);
 grow('.h-lk',t,6.75,.3,.45);
 const asgOn=t>=8.9&&t<9.6;$('h-asg').classList.toggle('on',asgOn);
 const dd=P(t,9.0,9.2)*(1-P(t,9.55,9.7));S($('h-dd'),{y:L(-10,0,P(t,9.0,9.2)),o:dd});
 $('h-ddo').style.background=(t>=9.4&&t<9.7)?'#FBE3EC':'transparent';
 const av=$('h-asgv');
 if(t>=9.6){av.innerHTML='<span class="av m" style="display:inline-flex;width:40px;height:40px;font-size:15px;vertical-align:middle;margin-right:10px">OC</span>Owen Cleveland';av.style.color='var(--ink)';av.style.fontWeight='700'}
 else{av.textContent='Unassigned';av.style.color='var(--mist)';av.style.fontWeight='500'}
 scrollTo($('h-scroll'),t,9.85,10.4,290);
 const srp=t>=10.5&&t<10.7;$('h-sr').style.transform=srp?'translate(3px,3px)':'none';$('h-sr').style.boxShadow=srp?'none':'';
 const tplOn=t>=10.7;$('h-hint').style.display=tplOn?'none':'';
 $('h-tpl').style.display=tplOn?'':'none';$('h-tpl').style.opacity=P(t,10.7,10.9);
 const ph=$('h-ph');ph.style.display=(tplOn&&t<11.05)?'':'none';ph.style.opacity=P(t,10.7,10.9);
 $('h-rep').classList.toggle('on',t>=10.9&&t<12.1);
 if(t>=11.05)typeInto($('h-typed'),"Owen's crew will be back by 10 AM.",t,11.15,11.95);else $('h-typed').innerHTML='';
 const sp=t>=12.25&&t<12.45;$('h-send').style.transform=sp?'translate(3px,3px)':'none';$('h-send').style.boxShadow=sp?'none':'';
 const st=$('h-status');if(t>=12.45){setPill(st,'soft','Waiting');st.style.transform=`scale(${L(.7,1,P(t,12.45,12.7,E.back))})`}else{setPill(st,'','Open');st.style.transform='none'}
 // ticket detail, later that morning
 view('h-v3',t,12.8,15.9);
 grow('.h-ev',t,13.3,.42,.4);
 const res=t>=13.75;$('h-s2').classList.toggle('on',res);
 $('h-bar2').style.transform=`scaleX(${P(t,13.5,13.8,E.io)})`;
 const s3=$('h-st3');if(res){setPill(s3,'ok','Resolved');s3.style.transform=`scale(${L(.7,1,P(t,13.75,14.0,E.back))})`}else{setPill(s3,'soft','Waiting');s3.style.transform='none'}
 handoff(t,13.6,15.6,'h-toast');
 callout(t,13.75,15.45,'hco','h-toast');
 taps(t,[[5.9,'h-tom'],[8.9,'h-asg'],[9.45,'h-ddo'],[10.5,'h-sr'],[10.95,'h-rep',150,10],[12.25,'h-send']]);
}""")

ALL = [HELP]
