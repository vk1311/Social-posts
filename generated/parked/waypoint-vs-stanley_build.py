from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance
S=2; W,H=1080*S,1350*S
INK=(18,37,47); MAG=(194,24,91); PAPER=(251,249,244); GREY=(150,150,158)
U='/mnt/user-data/uploads/Downloads/'
def F(sz,w=800,fam='Manrope'):
    f=ImageFont.truetype('/home/claude/fonts/%s.ttf'%fam,sz*S)
    vals=[]
    for a in f.get_variation_axes():
        n=a.get('name',b''); n=n.decode() if isinstance(n,bytes) else n
        vals.append(w if 'eight' in n else a['default'])
    f.set_variation_by_axes(vals); return f
im=Image.new('RGB',(W,H),INK)
PH=598*S
def panel(path,y,focus,bright=1.0,top=False):
    p=Image.open(path).convert('RGB')
    p=ImageOps.fit(p,(W,PH),centering=focus,method=Image.LANCZOS)
    if bright!=1: p=ImageEnhance.Brightness(p).enhance(bright)
    # bottom gradient
    g=Image.linear_gradient('L').resize((W,PH))
    g=g.point(lambda v:int((v-90)*1.7) if v>90 else 0)
    if top: g=g.transpose(Image.FLIP_TOP_BOTTOM).point(lambda v:int(v*0.6))
    p.paste(INK,(0,0),g.point(lambda v:min(v,235)))
    im.paste(p,(0,y))
panel(U+'denis-morozov-7KU0GPdSUSE-unsplash.jpg',0,(0.6,0.62),0.95)
B=PH+8*S
panel(U+'willian-justen-de-vasconcellos-KzSWlvLnHMA-unsplash.jpg',B,(0.55,0.7),top=True)
d=ImageDraw.Draw(im)
d.rectangle([0,PH,W,B],fill=MAG)
def block(y,kick,kc,l1,l2,l2c):
    x=64*S
    if kick=='WAYPOINT':
        lg=Image.open('/home/claude/sp/waypoint/brand/waypoint-nav.png').convert('RGBA').resize((44*S,44*S),Image.LANCZOS)
        im.paste(lg,(x,y-6*S),lg); d.text((x+56*S,y),kick,font=F(28,800),fill=kc)
    else: d.text((x,y),kick,font=F(28,800),fill=kc)
    d.text((x,y+48*S),l1,font=F(56,800),fill=PAPER)
    f2=F(56,800)
    if l2c==MAG:
        bb=d.textbbox((x,y+114*S),l2,font=f2)
        d.rectangle([bb[0]-16*S,bb[1]-12*S,bb[2]+16*S,bb[3]+14*S],fill=MAG)
        d.text((x,y+114*S),l2,font=f2,fill=PAPER)
    else: d.text((x,y+114*S),l2,font=f2,fill=l2c)
block(PH-236*S,'STANLEY',PAPER,'Survived a car fire.','Ice still inside.',PAPER)
block(B+56*S,'WAYPOINT',PAPER,'Took a week off.','Bookings kept coming in.',MAG)
# VS badge
cx,cy,r=W-120*S,PH+4*S,58*S
d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=INK,outline=MAG,width=6*S)
f=F(40,900); t='VS'; tw=d.textlength(t,font=f); bb=d.textbbox((0,0),t,font=f)
d.text((cx-tw/2,cy-(bb[1]+bb[3])/2),t,font=f,fill=PAPER)
# footer
fy=B+PH
logo=Image.open('/home/claude/sp/waypoint/brand/waypoint-nav.png').convert('RGBA').resize((96*S,96*S),Image.LANCZOS)
im.paste(logo,(56*S,fy+25*S),logo)
d.text((172*S,fy+28*S),'Waypoint',font=F(40,800),fill=PAPER)
d.text((172*S,fy+82*S),'Custom software that runs your business while you’re away.',font=F(24,500,'DMSans'),fill=(200,208,212))
u='waypointns.ca'; fu=F(24,700,'DMSans'); d.text((W-64*S-d.textlength(u,font=fu),fy+40*S),u,font=fu,fill=(232,90,145))
im.resize((1080,1350),Image.LANCZOS).save('/home/claude/work/wp4/waypoint-vs-stanley-v3.png')
print(fy/S)
