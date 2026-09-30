import os, sys, subprocess
from playwright.sync_api import sync_playwright

W = '/tmp/claude-0/-home-claude/c55a830d-2bf7-5686-8eae-0c9939c60360/scratchpad/work'
V = W + '/v2'
OUTV = W + '/out2/JJ-Pumps-Social-Posts/Reels'
OUTI = W + '/out2/JJ-Pumps-Social-Posts/Images'
os.makedirs(OUTV, exist_ok=True)
FPS = 30

DEEP = '#0C2631'; ROYAL = '#1E4485'; SKY = '#B7D2FF'; SUB = '#3E5570'; LINE = '#D5E2F6'


def img(k):
    return f'file://{V}/{k}.png'


BASE_CSS = f"""*{{box-sizing:border-box}} body{{margin:0;font-family:'Poppins',sans-serif;-webkit-font-smoothing:antialiased;background:#fff}}
#st{{position:relative;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(ellipse 120% 70% at 50% 45%,#FFFFFF 0%,#F4F7FB 60%,#E9EFF7 100%)}}
.a{{position:absolute}} h1,p{{margin:0}}
.t{{font-weight:700;color:{DEEP};letter-spacing:-.5px;line-height:1.06}}
.shine{{position:absolute;-webkit-mask-size:100% 100%;mask-size:100% 100%;background:linear-gradient(105deg,rgba(255,255,255,0) 42%,rgba(255,255,255,.75) 50%,rgba(255,255,255,0) 58%);background-size:320% 100%;background-repeat:no-repeat;mix-blend-mode:screen;pointer-events:none}}
.chip{{display:inline-block;padding:18px 40px;border-radius:999px;background:{ROYAL};color:#fff;font-size:44px;font-weight:600}}
.lab{{font-size:34px;font-weight:600;color:{DEEP};white-space:nowrap}}
.lab small{{display:block;font-size:26px;font-weight:400;color:{SUB}}}
"""

JS_BASE = """
const E={io:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2, out:t=>1-Math.pow(1-t,3), in:t=>t*t*t, lin:t=>t,
 back:t=>{const c1=1.3,c3=c1+1;return 1+c3*Math.pow(t-1,3)+c1*Math.pow(t-1,2)}};
function kf(t,k){ if(t<=k[0][0]) return k[0][1];
 for(let i=1;i<k.length;i++){ if(t<=k[i][0]){const [t0,v0]=k[i-1];const [t1,v1,e]=k[i];const p=(t-t0)/(t1-t0);return v0+(v1-v0)*E[e||'io'](p);} }
 return k[k.length-1][1]; }
const $=id=>document.getElementById(id);
function css(id,o){const e=$(id); for(const k in o) e.style[k]=o[k];}
function fadeUp(id,t,t0,t1,dy){ if(dy===undefined) dy=40; const o=kf(t,[[t0,0],[t0+.6,1,'out'],[t1,1],[t1+.4,0]]); const y=kf(t,[[t0,dy],[t0+.6,0,'out']]);
 css(id,{opacity:o,transform:`translateY(${y}px)`}); }
"""

LOGO = (f"<div class='a' style='left:60px;top:110px;display:flex;align-items:center;gap:16px'>"
        f"<img src='file://{W}/jj-mark-dark.png' style='height:74px;mix-blend-mode:multiply'>"
        f"<div style='display:flex;flex-direction:column'><span style='font-size:26px;font-weight:700;color:{ROYAL};line-height:1.2'>Jay Jalaram Pumps &amp; Spares</span>"
        f"<span style='font-size:20px;color:{SUB}'>Bakrol, Ahmedabad</span></div></div>")


def endcard(head, sub, left=520, top=720, width=500, extra=''):
    return (f"<div id='end' class='a' style='left:{left}px;top:{top}px;width:{width}px;opacity:0;display:flex;flex-direction:column;gap:26px'>"
            f"<h1 class='t' style='font-size:76px'>{head}</h1><div style='width:88px;height:4px;background:{ROYAL};border-radius:2px'></div>"
            f"<p style='font-size:32px;line-height:1.4;color:{SUB}'>{sub}</p>"
            f"<div><span class='chip'>+91 92271 06108</span></div>"
            f"<p style='font-size:26px;color:{SUB}'>WhatsApp or call · www.jayjalarampumps.in</p>{extra}</div>")


def page(body, script):
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{BASE_CSS}</style></head><body><div id='st'>{body}</div>"
            f"<script>{JS_BASE}{script}</script></body></html>")


# ---------------- assembled-pump geometry shared by R1 and R5 ----------------
PL, PT = 560, 330          # pump left/top on stage
PARTS = [('head', 0, 135), ('stages', 135, 600), ('strainer', 600, 712), ('motor', 712, 1414)]
PW = 254


def pump_parts(ids_prefix='', extra_style=''):
    s = ''
    for n, a, b in PARTS:
        s += (f"<img id='{ids_prefix}{n}' class='a' src='{img('part-' + n)}' style='left:0;top:{a}px;width:{PW}px;height:{b - a}px;{extra_style}'>")
    return s


def floor_el(id_, cx, y, w):
    return (f"<div id='{id_}' class='a' style='left:{cx - w // 2}px;top:{y - 22}px;width:{w}px;height:44px;border-radius:50%;"
            f"background:radial-gradient(ellipse at center,rgba(12,38,49,.32) 0%,rgba(12,38,49,0) 70%)'></div>")


def callout(id_, y, title, small, x_text=60, x_line_end=540):
    return (f"<div id='{id_}' class='a' style='left:{x_text}px;top:{y - 40}px;width:{x_line_end - x_text}px;opacity:0;display:flex;align-items:center;gap:18px'>"
            f"<div class='lab'>{title}<small>{small}</small></div><div style='flex-grow:1;height:2px;background:{ROYAL};position:relative'>"
            f"<div style='position:absolute;right:-6px;top:-5px;width:12px;height:12px;border-radius:50%;background:{ROYAL}'></div></div></div>")


# ============ R1: Built piece by piece ============
def reel1():
    body = LOGO
    body += (f"<div id='ttl' class='a' style='left:60px;top:200px;width:470px'><h1 class='t' style='font-size:62px'>Built piece<br><span style='color:{ROYAL}'>by piece.</span></h1></div>")
    body += floor_el('flr', PL + PW // 2, PT + 1414, 420)
    body += (f"<div id='pw' class='a' style='left:{PL}px;top:{PT}px;width:{PW}px;height:1414px;transform-origin:50% 100%'>"
             + pump_parts() +
             f"<img id='full' class='a' src='{img('p-tall')}' style='left:0;top:0;width:{PW}px;height:1414px;opacity:0'>"
             f"<div id='sh' class='shine' style='left:0;top:0;width:{PW}px;height:1414px;-webkit-mask-image:url({img('p-tall')});opacity:0'></div>"
             + ''.join(f"<div id='j{k}' class='a' style='left:-20px;top:{y}px;width:{PW + 40}px;height:3px;background:{SKY};opacity:0;box-shadow:0 0 18px {SKY}'></div>" for k, y in [(1, 135), (2, 600), (3, 712)]) +
             "</div>")
    cy = lambda a, b: PT + (a + b) // 2
    body += callout('c4', cy(712, 1414), 'Copper-rotor motor', 'the power inside')
    body += callout('c3', cy(600, 712), 'Stainless strainer', 'keeps sand out')
    body += callout('c2', cy(135, 600), 'Pump stages', 'lift the water up')
    body += callout('c1', cy(0, 135), 'Discharge head', 'water out')
    body += (f"<div id='sub' class='a' style='left:60px;top:1500px;width:460px;opacity:0'><p style='font-size:36px;line-height:1.35;color:{SUB}'>Checked at every joint.<br>Made in our Ahmedabad workshop.</p></div>")
    body += endcard(f"Water for <span style='color:{ROYAL}'>every field.</span>", 'V6 submersible pump sets, motors and spares.')
    script = """
function render(t){
 fadeUp('ttl',t,.2,9.2);
 css('motor',{transform:`translateY(${kf(t,[[1.0,900],[2.1,0,'out']])}px)`,opacity:kf(t,[[1.0,0],[1.4,1]])});
 css('strainer',{transform:`translateY(${kf(t,[[2.6,-1100],[3.5,0,'back']])}px)`,opacity:kf(t,[[2.6,0],[2.9,1]])});
 css('stages',{transform:`translateY(${kf(t,[[4.0,-1400],[5.0,0,'back']])}px)`,opacity:kf(t,[[4.0,0],[4.3,1]])});
 css('head',{transform:`translateY(${kf(t,[[5.6,-1600],[6.5,0,'back']])}px)`,opacity:kf(t,[[5.6,0],[5.9,1]])});
 [[3,3.5],[2,5.0],[1,6.5]].forEach(([k,ta])=>css('j'+k,{opacity:kf(t,[[ta-.05,0],[ta+.05,1],[ta+.6,0]])}));
 fadeUp('c4',t,2.0,8.2,0); fadeUp('c3',t,3.5,8.2,0); fadeUp('c2',t,5.0,8.2,0); fadeUp('c1',t,6.5,8.2,0);
 css('full',{opacity:t>7.2?1:0});
 css('sh',{opacity:kf(t,[[7.2,0],[7.4,1],[11.8,1],[12.2,0]]),backgroundPosition:`${kf(t,[[7.3,110],[8.8,-10],[10.2,110,'lin'],[11.7,-10]])}% 0`});
 fadeUp('sub',t,8.6,10.0);
 const mv=kf(t,[[10.0,0],[11.2,1]]);
 css('pw',{transform:`translateX(${-360*mv}px) scale(${1-.12*mv})`});
 css('flr',{transform:`translateX(${-360*mv}px) scale(${1-.12*mv})`});
 fadeUp('end',t,11.0,99);
}"""
    return page(body, script), 15.0, 13.5


# ============ R2: Inside the pump (technical cutaway) ============
def reel2():
    S = 1.1; OX, OY = 580, 170
    X = lambda x: OX + x * S
    Y = lambda y: OY + y * S
    lam = ''.join(f"<line x1='118' x2='158' y1='{y}' y2='{y}'/><line x1='242' x2='282' y1='{y}' y2='{y}'/>" for y in range(884, 1420, 9))
    holes = ''.join(f"<rect x='{x}' y='{y}' width='10' height='20' rx='4'/>" for y in range(702, 812, 30) for x in (102, 288))
    stages = ''
    for k in range(5):
        y0 = 150 + k * 108
        stages += (f"<g><path d='M114 {y0 + 4} L286 {y0 + 4}' stroke='#0C2631' stroke-opacity='.35' stroke-width='1.2'/>"
                   f"<path d='M118 {y0 + 100} C150 {y0 + 60}, 170 {y0 + 40}, 188 {y0 + 12} M282 {y0 + 100} C250 {y0 + 60}, 230 {y0 + 40}, 212 {y0 + 12}' fill='none' stroke='#8E99A5' stroke-width='3'/>"
                   f"<path d='M126 {y0 + 78} L150 {y0 + 44} L250 {y0 + 44} L274 {y0 + 78} Z' fill='url(#stl)' fill-opacity='.45'/>"
                   f"<ellipse cx='200' cy='{y0 + 78}' rx='74' ry='9' fill='url(#stl)' stroke='#5C6772' stroke-width='1'/>"
                   f"<ellipse cx='200' cy='{y0 + 44}' rx='52' ry='6' fill='url(#stl)' stroke='#5C6772' stroke-width='1'/>"
                   f"<g id='vn{k}'></g></g>")
    svg = f"""<svg id='cut' class='a' style='left:{OX}px;top:{OY}px;opacity:0' width='{400 * S}' height='{1500 * S}' viewBox='0 0 400 1500'>
<defs>
 <linearGradient id='stl' x1='0' x2='1'><stop offset='0' stop-color='#7D8894'/><stop offset='.35' stop-color='#E9EEF3'/><stop offset='.5' stop-color='#FFFFFF'/><stop offset='.72' stop-color='#C4CCD5'/><stop offset='1' stop-color='#6E7985'/></linearGradient>
 <linearGradient id='cu' x1='0' x2='1'><stop offset='0' stop-color='#7A3E15'/><stop offset='.35' stop-color='#E39B55'/><stop offset='.5' stop-color='#FFD2A0'/><stop offset='.7' stop-color='#C27A3A'/><stop offset='1' stop-color='#6E3512'/></linearGradient>
 <linearGradient id='dk' x1='0' x2='1'><stop offset='0' stop-color='#1E252D'/><stop offset='.5' stop-color='#5B6671'/><stop offset='1' stop-color='#1E252D'/></linearGradient>
 <linearGradient id='cyl' x1='0' x2='1'><stop offset='0' stop-color='#000' stop-opacity='.45'/><stop offset='.4' stop-color='#fff' stop-opacity='.35'/><stop offset='.55' stop-color='#fff' stop-opacity='.1'/><stop offset='1' stop-color='#000' stop-opacity='.5'/></linearGradient>
 <pattern id='bars' patternUnits='userSpaceOnUse' x='0' y='890' width='22' height='520'><rect width='22' height='520' fill='#3A434C'/><path d='M4 0 L14 0 L22 520 L12 520 Z' fill='url(#cu)'/></pattern>
 <pattern id='sht' patternUnits='userSpaceOnUse' width='12' height='40'><rect width='12' height='40' fill='url(#stl)'/><rect x='0' y='0' width='3' height='40' fill='#5C6772' opacity='.35'/></pattern>
 <clipPath id='rc'><rect x='166' y='890' width='68' height='520' rx='4'/></clipPath>
</defs>
<rect x='114' y='40' width='172' height='1430' fill='#F4F7FB'/>
<g id='gHead'>
 <path d='M150 40 L150 0 L250 0 L250 40' fill='none' stroke='url(#stl)' stroke-width='12'/>
 <rect x='96' y='128' width='208' height='16' rx='3' fill='url(#dk)'/>
</g>
<g id='gShaft'><rect id='shaft' x='194' y='52' width='12' height='1400' fill='url(#sht)'/></g>
<g id='gStages'>{stages}</g>
<g id='gStrainer'><rect x='100' y='690' width='14' height='130' fill='url(#stl)'/><rect x='286' y='690' width='14' height='130' fill='url(#stl)'/><g fill='#2B333C'>{holes}</g></g>
<g id='gMotor'>
 <rect x='114' y='822' width='172' height='40' fill='url(#dk)'/>
 <rect x='118' y='880' width='40' height='540' fill='url(#cu)'/><rect x='242' y='880' width='40' height='540' fill='url(#cu)'/>
 <g stroke='#5A2C0E' stroke-opacity='.45' stroke-width='1'>{lam}</g>
 <g clip-path='url(#rc)'><rect id='rotor' x='120' y='890' width='160' height='520' fill='url(#bars)'/></g>
 <rect x='166' y='890' width='68' height='520' rx='4' fill='url(#cyl)'/>
 <rect x='114' y='1420' width='172' height='50' fill='url(#dk)'/>
</g>
<rect x='100' y='40' width='14' height='650' fill='url(#stl)'/><rect x='286' y='40' width='14' height='650' fill='url(#stl)'/>
<rect x='100' y='820' width='14' height='650' fill='url(#stl)'/><rect x='286' y='820' width='14' height='650' fill='url(#stl)'/>
<g id='water'></g>
</svg>"""
    body = LOGO
    body += (f"<img id='photo' class='a' src='{img('p-tall')}' style='left:{X(200) - 142}px;top:{Y(40)}px;height:{1430 * S}px'>")
    body += "<div id='cam' class='a' style='left:0;top:0;width:1080px;height:1920px;transform-origin:0 0'>" + svg + "</div>"
    body += f"<div id='wipe' class='a' style='left:{X(60)}px;top:{Y(0)}px;width:6px;height:{1500 * S}px;background:{SKY};box-shadow:0 0 30px {SKY};opacity:0'></div>"
    body += f"<div id='ttl' class='a' style='left:60px;top:250px;width:480px'><h1 class='t' style='font-size:66px'>What's inside<br><span style='color:{ROYAL}'>your pump?</span></h1></div>"
    body += callout('k1', 1150, 'The copper rotor spins', 'about 2,900 turns a minute', 60, 700)
    body += callout('k2', 900, 'Impellers lift the water', 'stage by stage', 60, 590)
    body += (f"<div id='k3' class='a' style='left:60px;top:{int(Y(40)) + 60}px;width:500px;opacity:0'><div class='lab'>More stages = more height</div>"
             f"<div style='display:flex;gap:10px;margin-top:18px'>" + ''.join(f"<div id='sb{i}' style='width:64px;height:64px;border-radius:14px;border:2px solid {ROYAL};color:{ROYAL};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:600'>{i + 1}</div>" for i in range(5)) + "</div></div>")
    body += endcard(f"Engineered <span style='color:{ROYAL}'>inside and out.</span>", 'V6 submersible pump sets with copper-rotor motors.', 60, 1120, 470)
    script = f"""
const NS='http://www.w3.org/2000/svg';
function mk(tag,attrs){{const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);return e;}}
function spin(t){{ const s=kf(t,[[3.5,0],[5.5,1,'in']]); return s; }}
let ang=0,last=0;
function render(t){{
 fadeUp('ttl',t,.2,3.4);
 const rev=kf(t,[[2.4,0],[3.8,1]]);
 css('photo',{{opacity:1-rev}});
 css('cut',{{opacity:t<2.4?0:1,clipPath:`inset(0 ${{(1-rev)*100}}% 0 0)`}});
 css('wipe',{{opacity:rev>0&&rev<1?1:0,left:`{X(60)}px`,transform:`translateX(${{rev*{400 * S}}}px)`}});
 // rotation angle integrates speed
 const sp=spin(t); ang = 6.0*Math.max(0,t-3.5)*sp;
 const off=(ang*40)%22; $('rotor').setAttribute('x',120-22+off);
 $('shaft').setAttribute('transform',`translate(${{(ang*6)%12-12}},0)`);
 for(let k=0;k<5;k++){{
  const g=$('vn'+k); g.innerHTML=''; const y0=150+k*108;
  for(let i=0;i<9;i++){{ const th=i*2*Math.PI/9+ang*.55; const c=Math.cos(th);
   const xb=200+70*Math.sin(th), xt=200+50*Math.sin(th+.45);
   g.appendChild(mk('path',{{d:`M${{xb}} ${{y0+76}} Q${{(xb+xt)/2+6*c}} ${{y0+60}} ${{xt}} ${{y0+46}}`,stroke:c>0?'#2B333C':'#9AA6B2','stroke-width':c>0?3.2:2,'stroke-opacity':c>0?1:.35,fill:'none'}}));}}
 }}
 // water particles
 const wg=$('water'); wg.innerHTML=''; const wo=kf(t,[[6.2,0],[7.2,1]]);
 if(wo>0){{ const flow=kf(t,[[6.2,.35],[12,.6],[13.5,.9]]);
  for(let i=0;i<150;i++){{ const ph=(i*0.6180339)%1; let u=(ph+ (t-6.2)*0.11*flow*2)%1;
   let x,y,d=1; const phi=i*2.39996;
   if(u<.08){{ const q=u/.08; const side=i%2?1:-1; x=200+side*(150-80*q); y=760-10*q; }}
   else if(u<.92){{ const q=(u-.08)/.84; y=750-q*700; const r=y>150?62:30+32*(y-40)/110; const a=phi+ang*.55+q*9; x=200+r*Math.sin(a); d=Math.cos(a); }}
   else {{ const q=(u-.92)/.08; x=200+20*Math.sin(phi); y=50-q*120; }}
   wg.appendChild(mk('circle',{{cx:x,cy:y,r:d>0?4.2:2.8,fill:d>0?'#2F66C8':'#8FB3EE','fill-opacity':wo*(d>0?.9:.45)}}));}} }}
 const wm=kf(t,[[4.0,0],[5.0,1],[7.8,1],[8.6,0]]), ws=kf(t,[[7.8,0],[8.6,1],[11.4,1],[12.2,0]]);
 $('cam').style.transform=`translate(${{-580*wm-500*ws}}px,${{-1289.5*wm-111*ws}}px) scale(${{1+.7*wm+.6*ws}})`;
 // focus dimming
 const fm=kf(t,[[4.2,0],[4.8,1],[7.6,1],[8.2,0]]), fs=kf(t,[[8.2,0],[8.8,1],[11.4,1],[12,0]]);
 $('gStages').style.opacity=1-.6*fm; $('gHead').style.opacity=1-.6*fm; $('gStrainer').style.opacity=1-.6*fm;
 $('gMotor').style.opacity=1-.6*fs;
 fadeUp('k1',t,4.4,7.8,0); fadeUp('k2',t,8.4,11.6,0); fadeUp('k3',t,11.8,14.6,20);
 for(let i=0;i<5;i++){{ const on=t>12.2+i*.35; const e=$('sb'+i); e.style.background=on?'{ROYAL}':'transparent'; e.style.color=on?'#fff':'{ROYAL}'; }}
 fadeUp('end',t,15.0,99);
 fadeUp('ttl',t,.2,3.4);
}}"""
    return page(body, script), 18.0, 9.5


# ============ R3: Dealer lineup ============
def reel3():
    lineup = [('old-mixflow', 90, 900), ('old-ktype', 250, 900), ('p-tall', 430, 900), ('blue', 600, 900), ('old-ssjacket', 690, 900), ('sealed', 900, 640)]
    body = LOGO
    body += f"<div id='ttl' class='a' style='left:60px;top:250px;width:960px'><h1 class='t' style='font-size:78px'>Looking for <span style='color:{ROYAL}'>dealers.</span></h1></div>"
    body += f"<div id='ttl2' class='a' style='left:60px;top:370px;width:960px;opacity:0'><p style='font-size:38px;color:{SUB}'>Hardware, pipe and agri shops across Gujarat and India.</p></div>"
    body += floor_el('flr', 540, 1500, 1000)
    for n, (k, x, hh) in enumerate(lineup):
        src = img(k if k.startswith('p-') else 'p-' + k)
        body += (f"<div id='L{n}' class='a' style='left:{x}px;top:{1500 - hh}px;height:{hh}px;opacity:0'>"
                 f"<img src='{src}' style='height:{hh}px;display:block;filter:drop-shadow(0 16px 20px rgba(12,38,49,.28))'>"
                 f"<div id='LS{n}' class='shine' style='left:0;top:0;width:100%;height:100%;-webkit-mask-image:url({src})'></div></div>")
    body += f"<img id='ow' class='a' src='{img('p-openwell')}' style='left:310px;top:1300px;width:460px;opacity:0;filter:drop-shadow(0 16px 20px rgba(12,38,49,.3))'>"
    items = ['V6 pump sets', 'Copper-rotor motors', 'Openwell pumps', 'Spares &amp; job work']
    body += "<div class='a' style='left:60px;top:1560px;width:960px;display:flex;flex-wrap:wrap;gap:16px'>" + ''.join(
        f"<div id='it{i}' style='opacity:0;padding:14px 28px;border-radius:999px;border:2px solid {ROYAL};color:{ROYAL};font-size:32px;font-weight:600'>{t}</div>" for i, t in enumerate(items)) + "</div>"
    body += (f"<div id='end' class='a' style='left:60px;top:500px;width:960px;opacity:0;display:flex;flex-direction:column;gap:22px;align-items:flex-start'>"
             f"<p style='font-size:38px;color:{SUB}'>WhatsApp</p><h1 class='t' style='font-size:150px;color:{ROYAL};letter-spacing:4px'>DEALER</h1>"
             f"<p style='font-size:38px;color:{SUB}'>to</p><span class='chip' style='font-size:56px'>+91 92271 06108</span>"
             f"<p style='font-size:30px;color:{SUB};margin-top:10px'>Reliable supply from our Ahmedabad workshop.</p></div>")
    script = f"""
function render(t){{
 fadeUp('ttl',t,.2,9.4); fadeUp('ttl2',t,.8,9.4);
 for(let n=0;n<6;n++){{ const t0=1.2+n*.45; const x=kf(t,[[t0,700],[t0+.9,0,'out']]);
   const fin=kf(t,[[9.6,0],[10.4,1]]);
   css('L'+n,{{opacity:kf(t,[[t0,0],[t0+.4,1]])*(1-fin),transform:`translateX(${{x}}px)`}});
   css('LS'+n,{{backgroundPosition:`${{kf(t,[[4.6+n*.12,110],[5.8+n*.12,-10]])}}% 0`}}); }}
 css('ow',{{opacity:kf(t,[[6.0,0],[6.6,1],[9.6,1],[10.2,0]]),transform:`translateY(${{kf(t,[[6.0,60],[6.8,0,'out']])}}px)`}});
 for(let i=0;i<4;i++) fadeUp('it'+i,t,6.4+i*.45,9.6,20);
 css('flr',{{opacity:1-kf(t,[[9.6,0],[10.4,1]])}});
 fadeUp('end',t,10.4,99);
}}"""
    return page(body, script), 15.0, 7.4


# ============ R4: 3 mistakes ============
def reel4():
    hatch = ("<pattern id='ht' patternUnits='userSpaceOnUse' width='16' height='16' patternTransform='rotate(45)'><rect width='16' height='16' fill='#E6EBF1'/><rect width='3' height='16' fill='#CFD7E1'/></pattern>")
    body = LOGO
    # numeral + titles per scene
    scenes = [('1', 'Running it dry', 'When the water drops below the pump, the motor overheats.'),
              ('2', 'Low voltage, no protection', 'Weak supply cooks the motor winding.'),
              ('3', 'Wrong size for your borewell', 'Match the pump to your borewell every time.')]
    for i, (n, a, b) in enumerate(scenes):
        body += (f"<div id='s{i}' class='a' style='left:60px;top:230px;width:960px;opacity:0;display:flex;align-items:flex-start;gap:34px'>"
                 f"<div style='font-size:230px;line-height:.85;font-weight:700;color:{ROYAL}'>{n}</div>"
                 f"<div style='display:flex;flex-direction:column;gap:16px;padding-top:14px'><h1 class='t' style='font-size:62px'>{a}</h1><p style='font-size:32px;line-height:1.4;color:{SUB}'>{b}</p></div></div>")
    body += f"<div id='intro' class='a' style='left:60px;top:560px;width:960px'><h1 class='t' style='font-size:92px'>3 mistakes that<br><span style='color:{ROYAL}'>damage your pump.</span></h1></div>"
    # scene 1: borewell
    body += (f"<svg id='d0' class='a' style='left:240px;top:700px;opacity:0' width='600' height='1050' viewBox='0 0 600 1050'><defs>{hatch}</defs>"
             f"<rect x='0' y='0' width='150' height='1050' fill='url(#ht)'/><rect x='450' y='0' width='150' height='1050' fill='url(#ht)'/>"
             f"<rect x='150' y='0' width='300' height='1050' fill='#F8FAFD'/><rect x='146' y='0' width='6' height='1050' fill='#9AA6B2'/><rect x='448' y='0' width='6' height='1050' fill='#9AA6B2'/>"
             f"<rect id='wat' x='152' y='120' width='296' height='930' fill='#1E4485' fill-opacity='.18'/><rect id='wln' x='152' y='120' width='296' height='4' fill='{ROYAL}'/>"
             f"<image href='{img('p-tall')}' x='245' y='330' height='700' width='126'/>"
             f"<rect id='hot' x='236' y='690' width='144' height='340' rx='20' fill='none' stroke='#C0392B' stroke-width='5' opacity='0'/></svg>")
    body += f"<div id='w0' class='a' style='left:60px;top:1780px;width:960px;text-align:center;opacity:0'><span style='font-size:34px;font-weight:600;color:#B03A2E'>Water below the intake: switch off.</span></div>"
    # scene 2: gauge
    ticks = ''.join(f"<line x1='{300 + 250 * __import__('math').cos(__import__('math').pi * (1 - k / 20))}' y1='{320 - 250 * __import__('math').sin(__import__('math').pi * (1 - k / 20))}' x2='{300 + (225 if k % 5 else 205) * __import__('math').cos(__import__('math').pi * (1 - k / 20))}' y2='{320 - (225 if k % 5 else 205) * __import__('math').sin(__import__('math').pi * (1 - k / 20))}' stroke='#0C2631' stroke-width='{3 if k % 5 == 0 else 1.5}'/>" for k in range(21))
    body += (f"<svg id='d1' class='a' style='left:240px;top:820px;opacity:0' width='600' height='560' viewBox='0 0 600 560'>"
             f"<path d='M50 320 A250 250 0 0 1 550 320' fill='none' stroke='#E3E9F1' stroke-width='34'/>"
             f"<path d='M50 320 A250 250 0 0 1 177 103' fill='none' stroke='#C0392B' stroke-opacity='.75' stroke-width='34'/>"
             f"<path d='M300 70 A250 250 0 0 1 473 140' fill='none' stroke='{ROYAL}' stroke-width='34'/>{ticks}"
             f"<g id='ndl'><path d='M296 320 L300 95 L304 320 Z' fill='{DEEP}'/></g><circle cx='300' cy='320' r='22' fill='{DEEP}'/>"
             f"<text id='vt' x='300' y='450' text-anchor='middle' font-family='Poppins' font-size='64' font-weight='700' fill='{DEEP}'>230 V</text>"
             f"<text x='60' y='390' font-family='Poppins' font-size='26' fill='#B03A2E'>LOW</text><text x='470' y='390' font-family='Poppins' font-size='26' fill='{ROYAL}'>NORMAL</text></svg>")
    body += f"<div id='w1' class='a' style='left:60px;top:1450px;width:960px;text-align:center;opacity:0'><span style='font-size:34px;font-weight:600;color:{DEEP}'>Fit a proper starter with voltage protection.</span></div>"
    # scene 3: top-view fit
    body += (f"<svg id='d2' class='a' style='left:240px;top:760px;opacity:0' width='600' height='700' viewBox='0 0 600 700'>"
             f"<circle cx='300' cy='330' r='230' fill='#F1F4F8' stroke='#9AA6B2' stroke-width='14'/><circle cx='300' cy='330' r='214' fill='none' stroke='#C9D2DC' stroke-width='2'/>"
             f"<g id='pc'><circle cx='300' cy='330' r='250' fill='#B03A2E' fill-opacity='.08' stroke='#B03A2E' stroke-width='6' stroke-dasharray='18 12'/></g>"
             f"<g id='pg' opacity='0'><circle cx='300' cy='330' r='170' fill='url(#g)' stroke='{ROYAL}' stroke-width='6'/></g>"
             f"<defs><radialGradient id='g'><stop offset='0' stop-color='#FFFFFF'/><stop offset='.7' stop-color='#DDE4EC'/><stop offset='1' stop-color='#9AA6B2'/></radialGradient></defs>"
             f"<text x='300' y='660' text-anchor='middle' font-family='Poppins' font-size='28' fill='{SUB}'>Top view · borewell and pump</text></svg>")
    body += f"<div id='w2' class='a' style='left:60px;top:1500px;width:960px;text-align:center;opacity:0'><span id='w2t' style='font-size:36px;font-weight:600;color:#B03A2E'>Too big: it won't go down.</span></div>"
    body += (f"<div id='end' class='a' style='left:60px;top:620px;width:960px;opacity:0;display:flex;flex-direction:column;gap:28px;align-items:flex-start'>"
             f"<h1 class='t' style='font-size:84px'>Avoid these 3.<br><span style='color:{ROYAL}'>Your pump lasts longer.</span></h1>"
             f"<p style='font-size:36px;line-height:1.4;color:{SUB}'>Not sure what fits your borewell? Ask us before you buy.</p>"
             f"<span class='chip' style='font-size:52px'>+91 92271 06108</span></div>"
             f"<img id='endp' class='a' src='{img('p-tall')}' style='left:760px;top:1060px;height:760px;opacity:0;filter:drop-shadow(0 16px 20px rgba(12,38,49,.28))'>")
    script = f"""
function render(t){{
 fadeUp('intro',t,.1,1.8);
 fadeUp('s0',t,2.0,6.2,20); css('d0',{{opacity:kf(t,[[2.1,0],[2.6,1],[6.1,1],[6.5,0]])}});
 const lv=kf(t,[[2.8,120],[5.0,760,'io']]); $('wat').setAttribute('y',lv); $('wat').setAttribute('height',1050-lv); $('wln').setAttribute('y',lv);
 const hot=t>4.7&&t<6.2?(0.55+0.45*Math.sin((t-4.7)*10)):0; $('hot').setAttribute('opacity',hot);
 fadeUp('w0',t,4.8,6.2,10);
 fadeUp('s1',t,6.6,10.6,20); css('d1',{{opacity:kf(t,[[6.7,0],[7.2,1],[10.5,1],[10.9,0]])}});
 const a=kf(t,[[7.4,40],[9.2,-62,'io']]); $('ndl').setAttribute('transform',`rotate(${{a}} 300 320)`);
 $('vt').textContent=Math.round(kf(t,[[7.4,230],[9.2,165,'io']]))+' V'; $('vt').setAttribute('fill',t>8.6?'#B03A2E':'{DEEP}');
 fadeUp('w1',t,9.2,10.6,10);
 fadeUp('s2',t,11.0,15.0,20); css('d2',{{opacity:kf(t,[[11.1,0],[11.6,1],[14.9,1],[15.3,0]])}});
 const sh=t>11.8&&t<13.0?Math.sin(t*40)*8:0; $('pc').setAttribute('transform',`translate(${{sh}},0)`);
 $('pc').setAttribute('opacity',kf(t,[[13.0,1],[13.4,0]])); $('pg').setAttribute('opacity',kf(t,[[13.2,0],[13.7,1]]));
 fadeUp('w2',t,11.8,15.0,10); $('w2t').textContent=t<13.2?"Wrong size: it won't sit right.":'Right size: smooth fit, full flow.'; $('w2t').style.color=t<13.2?'#B03A2E':'{ROYAL}';
 fadeUp('end',t,15.4,99); fadeUp('endp',t,15.8,99);
}}"""
    return page(body, script), 19.0, 3.0


# ============ R5: Repair and job work ============
def reel5():
    body = LOGO
    body += f"<div id='ttl' class='a' style='left:60px;top:230px;width:470px'><h1 class='t' style='font-size:66px'>Pump not<br><span style='color:{ROYAL}'>working?</span></h1></div>"
    body += floor_el('flr', PL + PW // 2, PT + 1414, 420)
    body += (f"<div id='pw' class='a' style='left:{PL}px;top:{PT}px;width:{PW}px;height:1414px;transform-origin:50% 100%'>"
             + pump_parts() +
             f"<img id='nst' class='a' src='{img('part-stages')}' style='left:0;top:135px;width:{PW}px;height:465px;opacity:0;filter:brightness(1.06) contrast(1.06)'>"
             f"<div id='nsh' class='shine' style='left:0;top:135px;width:{PW}px;height:465px;-webkit-mask-image:url({img('part-stages')});opacity:0'></div>"
             "</div>")
    cy = lambda a, b: PT + (a + b) // 2
    body += callout('c1', cy(0, 1414), 'We open it up', 'and inspect every part')
    body += callout('c2', cy(135, 600), 'Worn part out', 'new spare in')
    body += (f"<div id='chk' class='a' style='left:60px;top:1250px;width:470px;opacity:0;display:flex;align-items:center;gap:22px'>"
             f"<svg width='110' height='110' viewBox='0 0 110 110'><circle cx='55' cy='55' r='50' fill='none' stroke='{ROYAL}' stroke-width='5'/>"
             f"<path id='tk' d='M32 57 L49 73 L80 40' fill='none' stroke='{ROYAL}' stroke-width='7' stroke-linecap='round' stroke-linejoin='round' stroke-dasharray='80' stroke-dashoffset='80'/></svg>"
             f"<div class='lab'>Tested before<br>it goes back</div></div>")
    body += endcard(f"Repair · Spares · <span style='color:{ROYAL}'>Job work.</span>", 'Bring your pump to our Bakrol workshop.')
    script = """
function render(t){
 fadeUp('ttl',t,.2,11.0);
 const ex=kf(t,[[1.4,0],[2.6,1,'io'],[8.2,1],[9.4,0,'io']]);
 css('head',{transform:`translateY(${-150*ex}px)`}); css('stages',{opacity:t>4.8?0:1,transform:`translateY(${-75*ex}px) translateX(${kf(t,[[3.8,0],[4.8,720,'in']])}px)`,filter:`grayscale(${kf(t,[[3.0,0],[3.6,.75]])}) sepia(${kf(t,[[3.0,0],[3.6,.35]])}) brightness(${kf(t,[[3.0,1],[3.6,.85]])})`});
 css('strainer',{transform:`translateY(${10*ex}px)`}); css('motor',{transform:`translateY(${90*ex}px)`});
 const nx=kf(t,[[5.2,-760],[6.3,0,'out']]);
 css('nst',{opacity:t>5.2?1:0,transform:`translateY(${-75*ex}px) translateX(${nx}px)`});
 css('nsh',{opacity:kf(t,[[6.3,0],[6.4,1],[7.6,1],[7.8,0]]),transform:`translateY(${-75*ex}px)`,backgroundPosition:`${kf(t,[[6.3,110],[7.6,-10]])}% 0`});
 fadeUp('c1',t,2.4,3.8,0); fadeUp('c2',t,4.0,7.8,0);
 css('chk',{opacity:kf(t,[[9.6,0],[10.0,1],[11.2,1],[11.5,0]])}); document.getElementById('tk').style.strokeDashoffset=kf(t,[[9.8,80],[10.5,0]]);
 const mv=kf(t,[[11.2,0],[12.3,1]]);
 css('pw',{transform:`translateX(${-360*mv}px) scale(${1-.12*mv})`}); css('flr',{transform:`translateX(${-360*mv}px) scale(${1-.12*mv})`});
 fadeUp('end',t,12.2,99);
}"""
    return page(body, script), 16.0, 6.6


REELS = [('03_Sat-03-Oct_reel_built-piece-by-piece', reel1), ('07_Tue-13-Oct_reel_inside-the-pump', reel2),
         ('11_Thu-22-Oct_reel_dealers-wanted', reel3), ('14_Thu-29-Oct_reel_3-mistakes', reel4), ('16_Tue-03-Nov_reel_repair-and-job-work', reel5)]

only = sys.argv[1:]
preview = '--preview' in only
only = [o for o in only if not o.startswith('--')]
os.makedirs(W + '/rhtml', exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1080, 'height': 1920})
    for name, fn in REELS:
        if only and not any(o in name for o in only):
            continue
        html, dur, cover_t = fn()
        hp = f'{W}/rhtml/{name}.html'
        open(hp, 'w').write(html)
        pg.goto('file://' + hp)
        pg.wait_for_timeout(400)
        if preview:
            for tt in [cover_t, dur * .15, dur * .35, dur * .55, dur * .75, dur - .1]:
                pg.evaluate(f'render({tt})')
                pg.screenshot(path=f'{W}/rhtml/{name}_{tt:05.2f}.jpg', type='jpeg', quality=70)
            continue
        ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                               '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium', '-movflags', '+faststart',
                               f'{OUTV}/{name}.mp4'], stdin=subprocess.PIPE)
        n = int(dur * FPS)
        for f in range(n):
            pg.evaluate(f'render({f / FPS})')
            ff.stdin.write(pg.screenshot(type='jpeg', quality=93))
        ff.stdin.close(); ff.wait()
        pg.evaluate(f'render({cover_t})')
        pg.screenshot(path=f'{OUTI}/{name.replace("_reel_", "_reel-cover_")}.jpg', type='jpeg', quality=92)
        print('done', name, n, 'frames', flush=True)
    b.close()
