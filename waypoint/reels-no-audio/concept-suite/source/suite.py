"""Shared pieces for the Waypoint concept-suite reels.

Every reel shows ONE app of an invented client system ("Harlow & Pine", a made-up Kentville
property-services company) built by Waypoint. The point of the series: separate apps that
are really one system — every reel ends with a hand-off to another app.

Rules (house rules + brand bible):
- Made-up data only: invented names, 555 phone numbers, no real clients, no live URLs.
- Mechanisms, never outcomes (no "save 5 hours", no "+40%").
- No hype words (revolutionary, seamless, unlock, game-changer, 10x).
- Canadian English, CAD after prices in captions, HST 14%.
- AI only drafts; a person checks and decides.
- Every reel carries the "Concept demo · made-up data" badge.
"""
from shell import sb

# ---- inline icons (24x24 viewBox, currentColor) --------------------------------------------
ICONS = {
    "crm": '<path d="M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm-7 9c0-3.9 3.1-7 7-7s7 3.1 7 7" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "cal": '<rect x="3.5" y="5" width="17" height="15.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M3.5 10h17M8 3v4M16 3v4" stroke="currentColor" stroke-width="2.2"/>',
    "money": '<rect x="2.5" y="6" width="19" height="12" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="12" cy="12" r="2.6" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "jobs": '<path d="M4 7h16v13H4zM9 7V4h6v3" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M4 12h16" stroke="currentColor" stroke-width="2.2"/>',
    "team": '<circle cx="9" cy="9" r="3.2" fill="none" stroke="currentColor" stroke-width="2.2"/><circle cx="17" cy="10" r="2.4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 15.4c3 0 5.5 2 5.5 4.6" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "more": '<circle cx="5.5" cy="12" r="2" fill="currentColor"/><circle cx="12" cy="12" r="2" fill="currentColor"/><circle cx="18.5" cy="12" r="2" fill="currentColor"/>',
    "box": '<path d="M3.5 7.5 12 3l8.5 4.5v9L12 21l-8.5-4.5z M3.5 7.5 12 12l8.5-4.5M12 12v9" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linejoin="round"/>',
    "help": '<path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5" fill="none" stroke="currentColor" stroke-width="2.2"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M21 20H3" fill="none" stroke="currentColor" stroke-width="2.4"/>',
    "ai": '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9zM18.5 15.5l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z" fill="currentColor"/>',
    "pay": '<path d="M4 4h16v16H4z" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M8 9h8M8 13h8M8 17h5" stroke="currentColor" stroke-width="2.2"/>',
    "leave": '<path d="M12 21V11M5 11a7 7 0 0 1 14 0z" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>',
    "check": '<path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.8" stroke-linecap="square"/>',
    "arrow": '<path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.6"/>',
    "search": '<circle cx="10.5" cy="10.5" r="6" fill="none" stroke="currentColor" stroke-width="2.4"/><path d="m15 15 5 5" stroke="currentColor" stroke-width="2.4"/>',
    "plus": '<path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2.6"/>',
    "phone": '<path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z" fill="currentColor"/>',
}


def icon(name, size=34, color="currentColor"):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" style="color:{color};flex:none">{ICONS[name]}</svg>'


# The 12 apps of the suite, in dock / grid order. (key, label, icon)
APPS = [
    ("crm", "Clients", "crm"), ("book", "Schedule", "cal"), ("quote", "Quotes", "money"),
    ("jobs", "Jobs", "jobs"), ("hr", "People", "team"), ("pay", "Payroll", "pay"),
    ("leave", "Time off", "leave"), ("help", "Helpdesk", "help"), ("stock", "Stock", "box"),
    ("mail", "Campaigns", "mail"), ("rep", "Reports", "chart"), ("ai", "Assistant", "ai"),
]
APP = {k: (lab, ic) for k, lab, ic in APPS}


def topbar(app_key, title=None):
    """H&P app bar with the current app's name. title overrides the app label."""
    lab, ic = APP[app_key]
    return (f'<div class="appbar"><div class="mono">H&amp;P</div><div style="flex:1"><div class="bizname">{title or lab}</div>'
            f'<div class="bizsub">Harlow &amp; Pine · system</div></div>'
            f'<div class="tbicon">{icon("search", 30)}</div></div>')


def dock(active, keys=("crm", "book", "quote", "jobs", "more")):
    """Bottom tab bar. active = app key that is highlighted. Use id 'dock-<key>' for taps."""
    out = ['<div class="dock">']
    for k in keys:
        if k == "more":
            lab, ic = "All apps", "more"
        else:
            lab, ic = APP[k]
        on = " on" if k == active else ""
        out.append(f'<div class="dk{on}" id="dock-{k}">{icon(ic, 34)}<span>{lab}</span></div>')
    out.append('</div>')
    return "".join(out)


def toast(el_id, app_key, text):
    """Cross-app hand-off toast. Animate with handoff(t, a, b, id)."""
    lab, ic = APP[app_key]
    return (f'<div class="toast" id="{el_id}"><div class="tic">{icon(ic, 30, "#F7F7F4")}</div>'
            f'<div><div class="tk">Sent to {lab}</div><div class="tt">{text}</div></div>'
            f'<div class="tar">{icon("arrow", 28, "#C2185B")}</div></div>')


def appview(view_id, app_key, body, time="9:12", title=None, dock_keys=None, active=None, extra=""):
    """A full app screen: status bar, H&P app bar, scrollable body, dock.
    body sits inside <div class="body" id="<view_id>-body">.  extra = absolutely positioned overlays."""
    d = dock(active or app_key, dock_keys) if dock_keys else dock(active or app_key, _dock_for(app_key))
    return (f'<div class="view app" id="{view_id}">{sb(time)}{topbar(app_key, title)}'
            f'<div class="body" id="{view_id}-body">{body}</div>{extra}{d}</div>')


def _dock_for(app_key):
    base = ["crm", "book", "quote", "jobs"]
    if app_key not in base:
        base = ["crm", "book", app_key, "jobs"] if app_key in ("pay", "leave", "hr") else ["crm", "jobs", app_key, "rep"]
    return tuple(base) + ("more",)


SUITE_CSS = r"""
#badge{position:absolute;left:117px;top:166px;font:600 24px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;
 color:var(--paper);border:2px solid rgba(126,150,162,.55);padding:10px 16px 9px;background:rgba(18,37,47,.6)}
#badge b{color:var(--mag);font-weight:700}
.tbicon{color:var(--ink)}
.body{position:absolute;left:0;right:0;top:154px;bottom:224px;overflow:hidden}
.inner{padding:24px 30px}
.dock{position:absolute;left:0;right:0;bottom:96px;height:128px;background:var(--paper);border-top:2px solid var(--ink);display:flex;
 justify-content:space-around;align-items:flex-start;padding:16px 10px 0;z-index:6}
.dk{display:flex;flex-direction:column;align-items:center;gap:6px;font:600 17px 'DM Sans';color:var(--mist);width:104px}
.dk.on{color:var(--ink)} .dk.on svg{color:var(--mag)}
.dk.on span{border-bottom:3px solid var(--mag);padding-bottom:1px}
.toast{position:absolute;left:22px;right:22px;bottom:246px;z-index:20;background:var(--ink);color:var(--paper);display:flex;gap:16px;
 align-items:center;padding:18px 20px;border-left:7px solid var(--mag);box-shadow:6px 6px 0 rgba(18,37,47,.25);opacity:0}
.tic{width:52px;height:52px;flex:none;background:#2F4A56;display:flex;align-items:center;justify-content:center}
.tk{font:600 16px 'DM Sans';letter-spacing:.18em;text-transform:uppercase;color:#F4A7C4}
.tt{font:700 23px/1.25 Manrope;margin-top:2px}
.tar{margin-left:auto}
/* list rows */
.row{display:flex;align-items:center;gap:16px;padding:18px 0;border-bottom:1.5px solid var(--line, #E3DED2)}
.av{width:58px;height:58px;flex:none;border-radius:50%;background:#2F4A56;color:var(--paper);display:flex;align-items:center;
 justify-content:center;font:800 21px Manrope}
.av.m{background:var(--mag)} .av.l{background:#7E96A2}
.rt{font:700 25px Manrope;line-height:1.15}
.rs{font:400 20px 'DM Sans';color:var(--slate);margin-top:3px}
.rr{margin-left:auto;text-align:right;font:700 23px Manrope;white-space:nowrap}
.rr small{display:block;font:500 17px 'DM Sans';color:var(--slate)}
.pill{display:inline-block;font:700 15px 'DM Sans';letter-spacing:.1em;text-transform:uppercase;padding:5px 10px 4px;border:2px solid var(--ink)}
.pill.mag{background:var(--mag);border-color:var(--mag);color:#fff}
.pill.soft{background:#FBE3EC;border-color:#FBE3EC;color:#9E1149}
.pill.ok{background:#12252F;color:#fff}
.pill.ghost{color:var(--slate);border-color:#C9C3B6}
/* section labels + cards */
.sl{font:600 17px 'DM Sans';letter-spacing:.2em;text-transform:uppercase;color:var(--mag);margin:22px 0 10px}
.card{border:2px solid var(--ink);background:#fff;padding:18px 20px;margin-bottom:16px}
.card.hi{box-shadow:6px 6px 0 var(--mag)}
.ct{font:800 26px/1.2 Manrope}
.cs{font:400 20px/1.4 'DM Sans';color:var(--slate);margin-top:4px}
/* stat tiles */
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:8px}
.tile{border:2px solid var(--ink);background:#fff;padding:16px 18px}
.tl{font:600 15px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--slate)}
.tv{font:800 40px/1.1 Manrope;margin-top:6px;letter-spacing:-.01em}
.tv small{font:600 18px 'DM Sans';color:var(--slate)}
/* timeline (activity) */
.tlx{position:relative;padding-left:34px}
.tlx:before{content:"";position:absolute;left:9px;top:8px;bottom:8px;width:2px;background:#C9C3B6}
.ev{position:relative;padding:0 0 22px}
.ev:before{content:"";position:absolute;left:-31px;top:6px;width:14px;height:14px;border-radius:50%;background:var(--paper);border:3px solid var(--ink)}
.ev.mag:before{background:var(--mag);border-color:var(--mag)}
.evt{font:700 22px/1.3 Manrope}
.evs{font:400 18px 'DM Sans';color:var(--slate);margin-top:2px}
/* bars */
.bars{display:flex;align-items:flex-end;gap:14px;height:240px;border-bottom:2px solid var(--ink);padding:0 6px}
.bar{flex:1;background:#2F4A56;transform-origin:bottom center;position:relative}
.bar.mag{background:var(--mag)}
.bar span{position:absolute;left:0;right:0;top:-30px;text-align:center;font:700 17px 'DM Sans';color:var(--ink)}
.bx{display:flex;gap:14px;padding:8px 6px 0}
.bx div{flex:1;text-align:center;font:600 16px 'DM Sans';color:var(--slate)}
/* chat */
.msg{max-width:84%;padding:16px 20px;font:400 22px/1.4 'DM Sans';margin-bottom:14px;border:2px solid var(--ink);background:#fff}
.msg.me{margin-left:auto;background:var(--ink);color:var(--paper);border-color:var(--ink)}
.msg.ai{border-left:7px solid var(--mag)}
.msg .who{font:600 15px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--mag);margin-bottom:6px}
/* kanban */
.kb{display:flex;gap:14px}
.kcol{flex:1;background:#F2ECE0;padding:12px 10px;min-height:520px}
.kh{font:700 16px 'DM Sans';letter-spacing:.14em;text-transform:uppercase;color:var(--slate);margin-bottom:10px;display:flex;justify-content:space-between}
.kc{background:#fff;border:2px solid var(--ink);padding:12px;margin-bottom:10px;font:700 19px/1.25 Manrope}
.kc small{display:block;font:400 16px 'DM Sans';color:var(--slate);margin-top:4px}
/* app grid (overview) */
.agrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.ag{border:2px solid var(--ink);background:#fff;height:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;
 font:700 21px Manrope;color:var(--ink)}
.ag svg{color:var(--mag)}
/* progress */
.prog{height:14px;background:#E3DED2;margin-top:10px}
.prog i{display:block;height:100%;background:var(--mag);transform-origin:left center}
.check{display:flex;gap:14px;align-items:center;padding:14px 0;border-bottom:1.5px solid #E3DED2;font:600 22px 'DM Sans'}
.cb{width:34px;height:34px;flex:none;border:2.5px solid var(--ink);display:flex;align-items:center;justify-content:center;background:#fff}
.cb.on{background:var(--mag);border-color:var(--mag);color:#fff}
"""

SUITE_JS = r"""
function handoff(t,a,b,id){const el=$(id);if(!el)return;const o=W(t,a,b,.3);S(el,{y:L(40,0,P(t,a,a+.4,E.back)),o:o})}
function grow(sel,t,a,stagger,dur){document.querySelectorAll(sel).forEach((e,i)=>{const q=P(t,a+i*stagger,a+i*stagger+(dur||.5));
 if(e.classList.contains('bar'))e.style.transform=`scaleY(${q})`;else S(e,{y:L(26,0,q),o:q})})}
function countUp(el,t,a,b,to,fmt){const q=P(t,a,b,E.out);const v=to*q;el.textContent=fmt?fmt(v):Math.round(v).toLocaleString('en-CA')}
function money(v){return '$'+v.toLocaleString('en-CA',{minimumFractionDigits:2,maximumFractionDigits:2})}
function scrollTo(el,t,a,b,px){el.style.transform=`translateY(${L(0,-px,P(t,a,b,E.io))}px)`}
function dockOn(key){document.querySelectorAll('.view').forEach(v=>{});}
"""
