"""Shared shell for Waypoint reel videos: stage, hook, captions, phone, end card, sting."""
import math, html

FONTS = "file:///home/claude/fonts"

SURVEY = [(55.10,107.56,43.43,24.59),(30.73,34.51,108.42,65.90),
          (106.17,49.93,40.15,101.52),(64.00,9.44,64.00,114.84)]
SLIVERS = [[(70.20,62.14),(70.20,65.86),(118.56,64.00)],
           [(57.80,62.14),(57.80,65.86),(9.44,64.00)]]
BEARINGS = [(46.40,74.15,59.70,51.10),(81.60,74.15,68.30,51.10)]
TRI = [(64.00,37.96),(86.55,77.02),(41.45,77.02)]


def mark_svg(el_id, size, survey, tri, dot, vb="0 0 128 128", w=(1.15, 2.0, 3.6, 3.9, 4.9)):
    ws, wb, wt, dr, cr = w
    out = [f'<svg id="{el_id}" class="mark" width="{size}" height="{size}" viewBox="{vb}">']
    for x1, y1, x2, y2 in SURVEY:
        L = math.hypot(x2 - x1, y2 - y1)
        out.append(f'<line class="mk-l" data-len="{L:.2f}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                   f'stroke="{survey}" stroke-width="{ws}" stroke-linecap="butt"/>')
    out.append('<g class="mk-s">')
    for poly in SLIVERS:
        pts = " ".join(f"{x},{y}" for x, y in poly)
        out.append(f'<polygon points="{pts}" fill="{survey}"/>')
    out.append('</g>')
    for x1, y1, x2, y2 in BEARINGS:
        L = math.hypot(x2 - x1, y2 - y1)
        out.append(f'<line class="mk-b" data-len="{L:.2f}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                   f'stroke="{dot}" stroke-width="{wb}"/>')
    per = sum(math.hypot(TRI[(i+1) % 3][0]-TRI[i][0], TRI[(i+1) % 3][1]-TRI[i][1]) for i in range(3))
    d = f"M{TRI[0][0]} {TRI[0][1]} L{TRI[1][0]} {TRI[1][1]} L{TRI[2][0]} {TRI[2][1]} Z"
    out.append(f'<path class="mk-t" data-len="{per:.2f}" d="{d}" fill="none" stroke="{tri}" '
               f'stroke-width="{wt}" stroke-linejoin="round"/>')
    for x, y in TRI:
        out.append(f'<circle class="mk-d" data-r="{dr}" cx="{x}" cy="{y}" r="{dr}" fill="{dot}"/>')
    out.append(f'<circle class="mk-c" data-r="{cr}" cx="64" cy="64" r="{cr}" fill="{dot}"/>')
    out.append('</svg>')
    return "".join(out)


def words(text):
    return " ".join(f'<span class="w">{html.escape(w)}</span>' for w in text.split())


def sb(time, dark=False):
    c = "dark" if dark else "light"
    return (f'<div class="sb {c}"><span>{time}</span><span class="sbi">'
            '<i style="height:9px"></i><i style="height:13px"></i><i style="height:17px"></i><i style="height:21px"></i>'
            '<b class="bat"><b></b></b></span></div>')


PHONE_ICON = ('<svg width="44" height="44" viewBox="0 0 24 24"><path fill="currentColor" d="M6.6 10.8c1.4 2.8 '
              '3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 '
              '3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/></svg>')
MSG_ICON = ('<svg width="34" height="34" viewBox="0 0 24 24"><path fill="#F7F7F4" d="M12 3C6.5 3 2 6.6 2 11c0 2.4 '
            '1.3 4.5 3.4 6L4.5 21l4.3-2.3c1 .2 2.1.3 3.2.3 5.5 0 10-3.6 10-8s-4.5-8-10-8z"/></svg>')

CSS = r"""
@font-face{font-family:Manrope;src:url('%%F%%/Manrope.woff2');font-weight:200 800}
@font-face{font-family:'DM Sans';src:url('%%F%%/DMSans.woff2');font-weight:100 1000}
:root{--ink:#12252F;--slate:#2F4A56;--paper:#F7F7F4;--mist:#7E96A2;--mag:#C2185B}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#12252F}
body{font-family:'DM Sans';color:var(--paper);-webkit-font-smoothing:antialiased;font-feature-settings:"tnum"}
#stage{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:hidden;background:var(--ink)}
#grid{position:absolute;left:-234px;top:-234px;width:1560px;height:2400px;
 background-image:linear-gradient(rgba(126,150,162,.10) 1.3px,transparent 1.3px),linear-gradient(90deg,rgba(126,150,162,.10) 1.3px,transparent 1.3px);
 background-size:117px 117px}
#diag{position:absolute;left:-60px;top:0}
#coord{position:absolute;left:117px;top:106px;font:500 31px 'DM Sans';letter-spacing:.16em;color:var(--mist)}
#hook{position:absolute;left:117px;top:640px;width:846px}
.kick{font:500 34px 'DM Sans';letter-spacing:.22em;text-transform:uppercase;color:var(--mag)}
.rule{width:247px;height:16px;background:var(--mag);transform-origin:left center}
#hook .rule{margin:38px 0 54px}
.htext{font:800 99px/1.10 Manrope;letter-spacing:-.015em;color:var(--paper)}
.w{display:inline-block}
#footer{position:absolute;left:117px;right:117px;top:1241px;height:120px;display:flex;justify-content:space-between;align-items:center}
.url{font:500 31px 'DM Sans';letter-spacing:.12em;color:var(--paper)}
#caps{position:absolute;left:117px;top:236px;width:846px}
.cap{position:absolute;left:0;top:0;width:846px;opacity:0}
.capk{font:600 28px 'DM Sans';letter-spacing:.22em;color:var(--mag);margin-bottom:14px}
.capt{font:800 54px/1.14 Manrope;color:var(--paper);letter-spacing:-.01em}
#phone{position:absolute;left:220px;top:520px;width:640px;height:1500px;border-radius:84px;background:#0A1418;
 box-shadow:0 0 0 2px rgba(126,150,162,.55),16px 16px 0 0 #2F4A56}
.screen{position:absolute;left:18px;top:18px;width:604px;height:1464px;border-radius:66px;overflow:hidden;background:#000}
.island{position:absolute;left:227px;top:16px;width:150px;height:42px;background:#05090B;border-radius:22px;z-index:60}
.view{position:absolute;left:0;top:0;width:604px;height:1464px;overflow:hidden;opacity:0}
.app{background:var(--paper);color:var(--ink)}
.sb{height:62px;display:flex;justify-content:space-between;align-items:center;padding:4px 46px 0 56px;font:600 24px 'DM Sans'}
.sb.dark{color:var(--paper)} .sb.light{color:var(--ink)}
.sbi{display:flex;align-items:flex-end;gap:4px;height:22px}
.sbi i{display:block;width:5px;background:currentColor;border-radius:1px}
.bat{display:block;width:40px;height:20px;border:2px solid currentColor;border-radius:5px;margin-left:8px;padding:2px}
.bat b{display:block;width:70%;height:100%;background:currentColor;border-radius:2px}
.appbar{height:92px;display:flex;align-items:center;gap:16px;padding:0 32px;border-bottom:2px solid var(--ink)}
.mono{width:52px;height:52px;flex:none;background:var(--ink);color:var(--paper);font:800 19px Manrope;display:flex;align-items:center;justify-content:center}
.bizname{font:800 26px Manrope;line-height:1.05}
.bizsub{font:500 17px 'DM Sans';color:var(--slate);letter-spacing:.14em;text-transform:uppercase;margin-top:3px}
.aback{font:700 40px Manrope;color:var(--ink);margin-right:4px}
.pad{padding:28px 34px}
.k{font:600 19px 'DM Sans';letter-spacing:.2em;text-transform:uppercase;color:var(--mag)}
h2{font:800 40px/1.12 Manrope;letter-spacing:-.01em;margin:10px 0 12px}
.meta{font:400 23px/1.45 'DM Sans';color:var(--slate)}
.items{width:100%;border:2px solid var(--ink);border-collapse:collapse;margin-top:22px;font:400 23px 'DM Sans'}
.items td{padding:14px 16px;border-top:2px solid var(--ink)}
.items td:last-child{text-align:right;font-weight:600;white-space:nowrap}
.items tr.sub td{color:var(--slate);border-top:1px solid rgba(18,37,47,.22);padding:10px 16px}
.items tr.tot td{font:800 30px Manrope;border-top:2px solid var(--ink);background:#ECEEEC}
.valid{margin-top:20px;border-left:6px solid var(--mag);padding:10px 16px;font:500 22px 'DM Sans'}
.field{margin-bottom:16px}
.field label{display:block;font:600 17px 'DM Sans';letter-spacing:.16em;text-transform:uppercase;color:var(--slate);margin-bottom:7px}
.input{height:62px;border:2px solid var(--ink);background:#fff;padding:0 18px;display:flex;align-items:center;font:500 25px 'DM Sans';white-space:nowrap;overflow:hidden}
.input.on{border-color:var(--mag);box-shadow:4px 4px 0 var(--mag)}
.caret{display:inline-block;width:3px;height:30px;background:var(--mag);margin-left:2px}
.sigbox{position:relative;height:170px;border:2px solid var(--ink);background:#fff;margin-top:6px}
.sigbox svg{position:absolute;left:0;top:0}
.sigx{position:absolute;left:18px;bottom:26px;font:400 30px 'DM Sans';color:var(--mist)}
.sigline{position:absolute;left:50px;right:24px;bottom:34px;height:2px;background:rgba(18,37,47,.25)}
.btn{height:78px;background:var(--ink);color:var(--paper);display:flex;align-items:center;justify-content:center;gap:12px;font:800 27px Manrope;box-shadow:5px 5px 0 var(--mag);margin-top:22px}
.btn.sm{height:60px;font-size:22px;box-shadow:4px 4px 0 var(--ink);margin-top:0;flex:1}
.btn.ghost{background:var(--paper);color:var(--ink);border:2px solid var(--ink)}
.banner{position:absolute;left:0;right:0;top:154px;z-index:5;background:var(--ink);color:var(--paper);font:700 23px 'DM Sans';padding:18px 34px;border-bottom:4px solid var(--mag);opacity:0}
.banner b{color:var(--mag)}
.scrollwrap{position:absolute;left:0;right:0;top:154px;bottom:0;overflow:hidden}
/* lock */
.lockdate{text-align:center;font:600 27px 'DM Sans';margin-top:62px;opacity:.9}
.locktime{text-align:center;font:700 150px/1 Manrope;letter-spacing:-.02em;margin-top:6px}
.notif{position:absolute;left:18px;right:18px;top:390px;background:rgba(247,247,244,.95);color:var(--ink);border-radius:30px;padding:22px 22px 24px;display:flex;gap:18px;opacity:0}
.nicon{width:56px;height:56px;flex:none;border-radius:14px;background:#2F4A56;display:flex;align-items:center;justify-content:center}
.ntop{display:flex;justify-content:space-between;font:400 20px 'DM Sans';color:var(--slate)}
.ntop b{font:700 23px 'DM Sans';color:var(--ink)}
.ntext{font:400 23px/1.35 'DM Sans';margin-top:4px}
/* mail */
.mail{background:#fff;color:var(--ink)}
.mhead{padding:8px 30px 16px}
.mback{font:500 23px 'DM Sans';color:var(--mag)}
.mtitle{font:800 56px Manrope;margin-top:4px;letter-spacing:-.01em}
.mrow{position:relative;padding:20px 30px 22px 50px;border-top:1px solid #DDE2E4;background:#fff}
.mdot{position:absolute;left:20px;top:31px;width:14px;height:14px;border-radius:50%;background:var(--mag)}
.mfrom{display:flex;justify-content:space-between;align-items:baseline;font:400 20px 'DM Sans';color:var(--slate)}
.mfrom b{font:700 24px 'DM Sans';color:var(--ink)}
.msub{font:600 23px 'DM Sans';margin-top:4px}
.mprev{font:400 21px/1.35 'DM Sans';color:var(--slate);margin-top:4px}
.chip{display:inline-flex;align-items:center;gap:12px;margin-top:14px;border:2px solid var(--ink);padding:7px 16px 7px 7px;font:600 21px 'DM Sans';box-shadow:4px 4px 0 var(--ink);background:#fff}
.pdf{background:var(--mag);color:#fff;font:800 15px Manrope;padding:8px 8px;letter-spacing:.04em}
/* callouts */
#conn{position:absolute;left:0;top:0;overflow:visible}
.callout{position:absolute;background:var(--paper);color:var(--ink);border:2px solid var(--ink);box-shadow:9px 9px 0 var(--mag);padding:24px 28px 18px;width:560px;opacity:0}
.ck{font:600 20px 'DM Sans';letter-spacing:.2em;text-transform:uppercase;color:var(--mag);margin-bottom:12px}
.cr{font:700 28px/1.3 Manrope;display:flex;gap:14px;margin-bottom:8px}
.cr i{font-style:normal;color:var(--mag)}
/* tap */
#tap{position:absolute;left:0;top:0;width:78px;height:78px;margin:-39px 0 0 -39px;border-radius:50%;background:rgba(18,37,47,.26);border:2px solid rgba(247,247,244,.8);z-index:80;opacity:0}
#ring{position:absolute;left:0;top:0;width:78px;height:78px;margin:-39px 0 0 -39px;border-radius:50%;border:4px solid var(--mag);z-index:79;opacity:0}
/* end + sting */
#end{position:absolute;left:117px;top:640px;width:846px}
#end .rule{margin:0 0 54px}
.etext{font:700 76px/1.17 Manrope;letter-spacing:-.01em;color:var(--paper)}
.esub{font:500 33px 'DM Sans';letter-spacing:.08em;color:var(--mist);margin-top:48px}
#sting{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0}
#bigmark{position:absolute;left:330px;top:400px}
.tag{position:absolute;left:0;right:0;top:900px;text-align:center;font:800 66px Manrope;letter-spacing:-.01em;color:var(--paper)}
.surl{position:absolute;left:0;right:0;top:1010px;text-align:center;font:600 36px 'DM Sans';letter-spacing:.16em;color:var(--mag)}
.stel{position:absolute;left:0;right:0;top:1072px;text-align:center;font:500 32px 'DM Sans';letter-spacing:.1em;color:var(--mist)}
""".replace("%%F%%", FONTS)

JS = r"""
const E={lin:x=>x,out:x=>1-Math.pow(1-x,3),in:x=>x*x*x,io:x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2,
 back:x=>{const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)}};
function P(t,a,b,e){e=e||E.out;if(t<=a)return 0;if(t>=b)return 1;return e((t-a)/(b-a));}
function L(a,b,p){return a+(b-a)*p}
function $(id){return document.getElementById(id)}
function S(el,o){o=o||{};const x=o.x||0,y=o.y||0,s=(o.s===undefined?1:o.s),r=o.r||0;
 el.style.transform=`translate(${x}px,${y}px) scale(${s}) rotate(${r}deg)`;el.style.opacity=(o.o===undefined?1:o.o);}
function W(t,a,b,d){d=d||.3;return Math.max(0,Math.min(P(t,a,a+d),1-P(t,b-d,b)))}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
function typeInto(el,str,t,a,b){const f=Math.max(0,Math.min(1,(t-a)/(b-a)));const n=Math.round(str.length*f);
 const showCaret=t>=a-.25&&t<=b+.45&&(t<b||Math.floor(t*2.4)%2===0);
 el.innerHTML=esc(str.slice(0,n))+(showCaret?'<span class="caret"></span>':'');}
function show(el,v){el.style.display=v?'':'none'}
function view(id,t,a,b){const el=$(id);const o=W(t,a,b,.28);S(el,{x:L(46,0,P(t,a,a+.35)),o:o});el.style.visibility=o>0?'visible':'hidden';return o}
function rel(el){const r=el.getBoundingClientRect(),s=document.querySelector('.screen').getBoundingClientRect();
 return {x:r.left-s.left+r.width/2,y:r.top-s.top+r.height/2,w:r.width,h:r.height}}
function taps(t,list){const el=$('tap'),ring=$('ring');let a=null;
 for(const k of list){if(t>=k[0]-.35&&t<=k[0]+.6){a=k;break}}
 if(!a){el.style.opacity=0;ring.style.opacity=0;return false}
 const t0=a[0];const p=rel($(a[1]));const x=p.x+(a[2]||0),y=p.y+(a[3]||0);
 const pre=P(t,t0-.35,t0-.08);const s=t<t0?L(1.25,1,pre):L(.82,1,P(t,t0,t0+.22));
 const fade=1-P(t,t0+.28,t0+.6);el.style.left=x+'px';el.style.top=y+'px';S(el,{s:s,o:Math.min(pre,fade)});
 const rp=P(t,t0,t0+.5);ring.style.left=x+'px';ring.style.top=y+'px';S(ring,{s:L(.6,2.3,rp),o:t<t0?0:1-rp});return true}
function finger(x,y,o){const el=$('tap');el.style.left=x+'px';el.style.top=y+'px';S(el,{s:.9,o:o});$('ring').style.opacity=0}
function prepMark(svg){svg.querySelectorAll('[data-len]').forEach(e=>{const l=+e.dataset.len;e.style.strokeDasharray=l;e.style.strokeDashoffset=l})}
function drawMark(svg,p){
 svg.querySelectorAll('.mk-l').forEach((e,i)=>{const q=P(p,i*.06,.34+i*.06,E.io);e.style.strokeDashoffset=e.dataset.len*(1-q)});
 const s=P(p,.18,.5,E.out);svg.querySelector('.mk-s').setAttribute('transform',`translate(64 64) scale(${s} 1) translate(-64 -64)`);
 const tq=P(p,.34,.7,E.io);const tr=svg.querySelector('.mk-t');tr.style.strokeDashoffset=tr.dataset.len*(1-tq);
 svg.querySelectorAll('.mk-b').forEach(e=>{const q=P(p,.58,.8);e.style.strokeDashoffset=e.dataset.len*(1-q)});
 svg.querySelectorAll('.mk-d').forEach((e,j)=>{const q=P(p,.62+j*.06,.82+j*.06,E.back);e.setAttribute('r',Math.max(0,e.dataset.r*q))});
 const c=svg.querySelector('.mk-c');c.setAttribute('r',Math.max(0,c.dataset.r*P(p,.84,1,E.back)));}
function callout(t,a,b,id,anchorId,side){const c=$(id);const o=W(t,a,b,.3);S(c,{y:L(34,0,P(t,a,a+.4)),o:o});
 c.querySelectorAll('.cr').forEach((r,i)=>{const q=P(t,a+.2+i*.12,a+.5+i*.12);S(r,{x:L(-18,0,q),o:q})});
 const path=$('connp'),dot=$('connd');if(o<=0){path.style.opacity=0;dot.style.opacity=0;return}
 const an=$(anchorId).getBoundingClientRect(),cr=c.getBoundingClientRect();
 const ax=an.left-4,ay=an.top+Math.min(an.height/2,44);const cx=cr.left+52,cy=cr.top;
 const d=`M${ax} ${ay} L${cx} ${ay} L${cx} ${cy}`;path.setAttribute('d',d);
 const len=path.getTotalLength();path.style.strokeDasharray=len;path.style.strokeDashoffset=len*(1-P(t,a+.05,a+.5,E.io));
 path.style.opacity=o;dot.setAttribute('cx',ax);dot.setAttribute('cy',ay);dot.style.opacity=o}
let HW=[],EW=[],CAPEL=[];
function init(){HW=[...document.querySelectorAll('#hook .w')];EW=[...document.querySelectorAll('#end .w')];
 CAPEL=[...document.querySelectorAll('.cap')];document.querySelectorAll('.mark').forEach(prepMark);
 if(window.initReel)initReel();window.READY=true}
function render(t){
 $('grid').style.transform=`translate(${-t*2.4}px,${-t*3.4}px)`;
 $('diag').style.transform=`translate(${t*1.8}px,0)`;
 // hook
 const hOut=P(t,2.85,3.25,E.in);const hook=$('hook');hook.style.opacity=1-hOut;hook.style.transform=`translateY(${-90*hOut}px)`;
 S(document.querySelector('#hook .kick'),{y:L(20,0,P(t,.05,.45)),o:P(t,.05,.45)});
 document.querySelector('#hook .rule').style.transform=`scaleX(${P(t,.25,.75,E.io)})`;
 HW.forEach((w,i)=>{const q=P(t,.35+i*.075,.85+i*.075);S(w,{y:L(64,0,q),o:q})});
 const fo=P(t,.4,.9)*(1-P(t,2.75,3.05));$('footer').style.opacity=fo;drawMark($('footmark'),P(t,.4,1.6,E.lin));
 // phone
 const pin=P(t,3.0,3.8,E.out),pout=P(t,15.5,16.05,E.in);const z=window.zoomAt?zoomAt(t):{s:1,ox:320,oy:600};
 const ph=$('phone');ph.style.transformOrigin=`${z.ox}px ${z.oy}px`;
 ph.style.transform=`translateY(${L(1500,0,pin)+L(0,1650,pout)}px) scale(${z.s})`;ph.style.visibility=(t>2.9&&t<16.2)?'visible':'hidden';
 // captions
 CAPS.forEach((c,i)=>{const el=CAPEL[i];const o=W(t,c[0],c[1],.3);S(el,{y:L(28,0,P(t,c[0],c[0]+.4))-L(0,16,P(t,c[1]-.3,c[1])),o:o})});
 renderReel(t);
 // end card
 const eo=1-P(t,18.55,18.85);const end=$('end');end.style.opacity=eo;end.style.visibility=t>15.8&&t<18.9?'visible':'hidden';
 document.querySelector('#end .rule').style.transform=`scaleX(${P(t,15.95,16.45,E.io)})`;
 EW.forEach((w,i)=>{const q=P(t,16.1+i*.06,16.6+i*.06);S(w,{y:L(56,0,q),o:q})});
 S(document.querySelector('.esub'),{y:L(20,0,P(t,17.1,17.5)),o:P(t,17.1,17.5)});
 // sting
 $('sting').style.opacity=P(t,18.85,19.05);drawMark($('bigmark'),P(t,18.95,20.25,E.lin));
 S(document.querySelector('.tag'),{y:L(30,0,P(t,19.85,20.3)),o:P(t,19.85,20.3)});
 S(document.querySelector('.surl'),{y:L(20,0,P(t,20.1,20.5)),o:P(t,20.1,20.5)});
 S(document.querySelector('.stel'),{y:L(20,0,P(t,20.25,20.65)),o:P(t,20.25,20.65)});
}
"""


def page(reel):
    from suite import SUITE_CSS, SUITE_JS
    hook = f'<div id="hook"><div class="kick">{html.escape(reel["kicker"])}</div><div class="rule"></div><div class="htext">{words(reel["hook"])}</div></div>'
    caps = "".join(
        f'<div class="cap"><div class="capk">{i+1:02d} / {len(reel["caps"]):02d}</div><div class="capt">{html.escape(c[2])}</div></div>'
        for i, c in enumerate(reel["caps"]))
    capjs = "const CAPS=[" + ",".join(f"[{c[0]},{c[1]}]" for c in reel["caps"]) + "];"
    foot = mark_svg("footmark", 120, "#2F4A56", "#F7F7F4", "#C2185B", vb="22 18 84 84", w=(1.9, 3.2, 6.2, 4.4, 5.6))
    big = mark_svg("bigmark", 420, "#7E96A2", "#F7F7F4", "#C2185B")
    diag = ('<svg id="diag" width="1200" height="1920"><line x1="0" y1="576" x2="1200" y2="1190" stroke="rgba(126,150,162,.10)" stroke-width="2.6"/>'
            '<line x1="254" y1="-40" x2="860" y2="1960" stroke="rgba(126,150,162,.10)" stroke-width="2.6"/></svg>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{SUITE_CSS}{reel.get('css','')}</style></head><body>
<div id="stage">
<div id="grid"></div>{diag}
<div id="coord">45.0774° N&nbsp;&nbsp;64.4956° W</div>
<div id="badge">Concept demo · <b>made-up data</b></div>
{hook}
<div id="footer">{foot}<div class="url">waypointns.ca</div></div>
<div id="caps">{caps}</div>
<div id="phone"><div class="screen"><div class="island"></div>{reel['screen']}<div id="ring"></div><div id="tap"></div></div></div>
<svg id="conn" width="1080" height="1920"><path id="connp" fill="none" stroke="#C2185B" stroke-width="4"/><circle id="connd" r="9" fill="#C2185B"/></svg>
{reel.get('callouts','')}
<div id="end"><div class="rule"></div><div class="etext">{words(reel['end'])}</div><div class="esub">Text 902-670-9297 · waypointns.ca</div></div>
<div id="sting">{big}<div class="tag">{reel.get("tag","Built around your process.")}</div><div class="surl">waypointns.ca</div><div class="stel">902-670-9297 · Kentville, NS</div></div>
</div>
<script>{JS}
{SUITE_JS}
{capjs}
{reel['js']}
document.fonts.ready.then(()=>{{init();render(0)}});
</script></body></html>"""
