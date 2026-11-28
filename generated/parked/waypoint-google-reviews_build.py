from PIL import Image, ImageDraw, ImageFont, ImageOps
S=2; W,H=1080*S,1350*S
INK=(18,37,47); MAG=(194,24,91); PAPER=(251,249,244); MUTED=(160,176,184)
def F(sz,w=800,fam='Manrope'):
    f=ImageFont.truetype('/home/claude/fonts/%s.ttf'%fam,sz*S); vals=[]
    for a in f.get_variation_axes():
        n=a.get('name',b''); n=n.decode() if isinstance(n,bytes) else n
        vals.append(w if 'eight' in n else a['default'])
    f.set_variation_by_axes(vals); return f
im=Image.new('RGB',(W,H),INK); d=ImageDraw.Draw(im)
PH=690*S
p=Image.open('/mnt/user-data/uploads/Downloads/tim-mossholder-XU84U7xhQ_4-unsplash.jpg').convert('RGB')
p=ImageOps.fit(p,(W,PH),centering=(0.5,0.66),method=Image.LANCZOS)
g=Image.linear_gradient('L').resize((W,PH)).point(lambda v:int((v-100)*1.9) if v>100 else 0)
p.paste(INK,(0,0),g.point(lambda v:min(v,255)))
im.paste(p,(0,0))
x=64*S; y=PH-215*S
d.text((x,y),'GOOGLE REVIEWS',font=F(28,800),fill=PAPER)
d.text((x,y+46*S),'Real businesses.',font=F(58,800),fill=PAPER)
f2=F(58,800); bb=d.textbbox((x,y+116*S),'Real words.',font=f2)
d.rectangle([bb[0]-16*S,bb[1]-12*S,bb[2]+16*S,bb[3]+14*S],fill=MAG)
d.text((x,y+116*S),'Real words.',font=f2,fill=PAPER)
Q=[('“I had a great experience working with Waypoint…”','Dino John · DJ Movers & Junk Removal'),
   ('“Highly Recommended!!”','Parshil Kaur · Malvaci'),
   ('“Vatsal does an amazing job… Would highly recommend!”','Anmol Kaur')]
qy=PH+50*S
for i,(q,n) in enumerate(Q):
    # wrap
    fq=F(36,700); words=q.split(); lines=[];cur=''
    for w_ in words:
        t=(cur+' '+w_).strip()
        if d.textlength(t,font=fq)>W-2*x-40*S: lines.append(cur);cur=w_
        else: cur=t
    lines.append(cur)
    ty=qy
    for l in lines: d.text((x+30*S,ty),l,font=fq,fill=PAPER); ty+=48*S
    d.text((x+30*S,ty+8*S),n,font=F(24,500,'DMSans'),fill=MUTED)
    d.rectangle([x,qy+6*S,x+6*S,ty+40*S],fill=MAG)
    qy=ty+70*S
print('quotes end',qy/S)
fy=1204*S
d.line([0,fy,W,fy],fill=(40,62,74),width=2*S)
logo=Image.open('/home/claude/sp/waypoint/brand/waypoint-nav.png').convert('RGBA').resize((96*S,96*S),Image.LANCZOS)
im.paste(logo,(56*S,fy+25*S),logo)
d.text((172*S,fy+28*S),'Waypoint',font=F(40,800),fill=PAPER)
d.text((172*S,fy+82*S),'Custom software that runs your business while you’re away.',font=F(24,500,'DMSans'),fill=(200,208,212))
u='waypointns.ca'; fu=F(24,700,'DMSans'); d.text((W-64*S-d.textlength(u,font=fu),fy+40*S),u,font=fu,fill=(232,90,145))
im.resize((1080,1350),Image.LANCZOS).save('/home/claude/work/wp5/waypoint-google-reviews.png')
