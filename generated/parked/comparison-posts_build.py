from PIL import Image, ImageDraw, ImageFont, ImageOps
import glob, sys
S=2; W,H=1080*S,1350*S
FD='/home/claude/fonts/'; U='/mnt/user-data/uploads/Downloads/'; R='/home/claude/sp/'
def F(fam,sz,w=700,wd=None,opt=None):
    f=ImageFont.truetype(FD+fam+'.ttf',int(sz*S)); vals=[]
    for a in f.get_variation_axes():
        n=a['name']; n=n.decode() if isinstance(n,bytes) else n
        if n=='Weight': vals.append(w)
        elif n=='Width': vals.append(wd or 100)
        elif n.lower()=='optical size': vals.append(min(a['maximum'],opt or a['maximum']))
        else: vals.append(a['default'])
    f.set_variation_by_axes(vals); return f
def photo(id_or_path):
    return id_or_path if '/' in id_or_path else glob.glob(U+'*'+id_or_path+'-unsplash.jpg')[0]
KX=Image.open(R+'keegix/brand/logo-lockup-white.png').convert('RGBA')
T={
 'wp':dict(ink=(18,37,47),acc=(194,24,91),paper=(251,249,244),hl_bg=(194,24,91),hl_fg=(251,249,244),url_c=(232,90,145),
   head=lambda sz:F('Manrope',sz,800), hl=lambda sz:F('Manrope',sz,800), kick=lambda:F('Manrope',28,800), upper=True,
   body=lambda sz,w=500:F('DMSans',sz,w), mark=Image.open(R+'waypoint/brand/waypoint-nav.png').convert('RGBA'), name='Waypoint', url='waypointns.ca'),
 'sk':dict(ink=(46,42,107),acc=(123,140,245),paper=(245,246,252),hl_bg=(255,122,89),hl_fg=(35,33,63),url_c=(164,176,250),
   head=lambda sz:F('Outfit',sz,600), hl=lambda sz:F('Outfit',sz,600), kick=lambda:F('Outfit',30,500), upper=False,
   body=lambda sz,w=400:F('Outfit',sz,w), mark=Image.open(R+'staffkin/brand/staffkin-mark-white-peri-512.png').convert('RGBA'),
   lockup=Image.open(R+'staffkin/brand/staffkin-logo-white-1600.png').convert('RGBA'), name='Staffkin', url='staffkin.com'),
 'kx':dict(ink=(21,48,74),acc=(244,196,48),paper=(255,255,255),hl_bg=(244,196,48),hl_fg=(21,48,74),url_c=(244,196,48),
   head=lambda sz:F('Newsreader',sz,500), hl=lambda sz:F('Newsreader-Italic',sz,500), kick=lambda:F('Archivo',24,800,125), upper=True,
   body=lambda sz,w=400:F('Archivo',sz,w), mark=KX.crop((150,95,310,305)), lockup=KX.crop((150,95,1090,305)), name='Keegix', url='keegix.com'),
}
def build(out,brand,top,bot,desc,vs_y=None):
    t=T[brand]; INK,ACC,PAPER=t['ink'],t['acc'],t['paper']
    im=Image.new('RGB',(W,H),INK); PH=598*S; B=PH+8*S
    def panel(spec,y,flip):
        p=Image.open(photo(spec['photo'])).convert('RGB')
        if spec.get('mirror'): p=ImageOps.mirror(p)
        if spec.get('box'):
            bx=spec['box']; p=p.crop((int(bx[0]*p.width),int(bx[1]*p.height),int(bx[2]*p.width),int(bx[3]*p.height)))
        p=ImageOps.fit(p,(W,PH),centering=spec.get('focus',(0.5,0.5)),method=Image.LANCZOS)
        g=Image.linear_gradient('L').resize((W,PH)).point(lambda v:int((v-90)*1.7) if v>90 else 0)
        if flip: g=g.transpose(Image.FLIP_TOP_BOTTOM).point(lambda v:int(v*spec.get('shade',0.6)))
        else: g=g.point(lambda v:int(min(v,235)*spec.get('shade',1.0)))
        p.paste(INK,(0,0),g.point(lambda v:min(v,235))); im.paste(p,(0,y))
    panel(top,0,False); panel(bot,B,True)
    d=ImageDraw.Draw(im); d.rectangle([0,PH,W,B],fill=ACC)
    x=64*S; MAXW=W-2*x-140*S
    def fit(fn,txt,sz):
        while d.textlength(txt,font=fn(sz))>MAXW: sz-=1
        return sz
    def block(y0,spec,is_brand,anchor_bottom):
        lines=spec['lines']; hl=spec.get('hl')
        sz=min([fit(t['head'],l,58) for l in lines]+([fit(t['hl'],hl,58)] if hl else []))
        lh=int(sz*1.2)*S; n=len(lines)+(1 if hl else 0)
        total=50*S+n*lh+(16*S if hl else 0)
        y=y0-total if anchor_bottom else y0
        k=spec['kick'].upper() if t['upper'] else spec['kick']
        kf=t['kick']()
        if is_brand:
            m=t['mark']; mh=44*S; mw=int(m.width*mh/m.height); m2=m.resize((mw,mh),Image.LANCZOS)
            im.paste(m2,(x,y-8*S),m2); d.text((x+mw+12*S,y),k,font=kf,fill=PAPER)
        else: d.text((x,y),k,font=kf,fill=PAPER)
        y+=50*S
        for l in lines: d.text((x,y),l,font=t['head'](sz),fill=PAPER); y+=lh
        if hl:
            f2=t['hl'](sz); y+=8*S; bb=d.textbbox((x,y),hl,font=f2)
            d.rectangle([bb[0]-16*S,bb[1]-12*S,bb[2]+16*S,bb[3]+14*S],fill=t['hl_bg'])
            d.text((x,y),hl,font=f2,fill=t['hl_fg'])
    block(PH-44*S,top,False,True)
    block(B+56*S,bot,True,False)
    cx,cy,r=W-120*S,PH+4*S,58*S
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=INK,outline=ACC,width=6*S)
    f=F('Manrope',40,800) if brand=='wp' else (F('Outfit',40,600) if brand=='sk' else F('Archivo',34,800,125)); tx='VS'
    bb=d.textbbox((0,0),tx,font=f); d.text((cx-(bb[0]+bb[2])/2,cy-(bb[1]+bb[3])/2),tx,font=f,fill=PAPER)
    fy=B+PH; d.rectangle([0,fy,W,H],fill=INK)
    DC=tuple(int(c*0.82+INK[i]*0.18) for i,c in enumerate(PAPER))
    if brand=='wp':
        lg=t['mark'].resize((96*S,96*S),Image.LANCZOS); im.paste(lg,(56*S,fy+25*S),lg)
        d.text((172*S,fy+28*S),t['name'],font=F('Manrope',40,800),fill=PAPER); dx,dy=172*S,fy+82*S
    else:
        lk=t['lockup']; bbx=lk.getbbox() if brand=='sk' else None
        if bbx: lk=lk.crop(bbx)
        lh_=52*S; lw_=int(lk.width*lh_/lk.height); lk=lk.resize((lw_,lh_),Image.LANCZOS)
        im.paste(lk,(60*S,fy+26*S),lk); dx,dy=64*S,fy+92*S
    fu=t['body'](24,700); uw=d.textlength(t['url'],font=fu)
    d.text((W-64*S-uw,fy+40*S),t['url'],font=fu,fill=t['url_c'])
    ds=24
    while d.textlength(desc,font=t['body'](ds))>W-dx-64*S: ds-=1
    d.text((dx,dy),desc,font=t['body'](ds),fill=DC)
    im.resize((1080,1350),Image.LANCZOS).save(out); print(out,'desc size',ds)
P={
'waypoint-vs-gta6':('wp',dict(photo='4ZHaSWRNkEo',kick='GTA 6',lines=['Kept fans waiting','13 years.'],box=(0,0.3,1,1),focus=(0.5,0.0)),
   dict(photo='idzUojjazCg',kick='Waypoint',lines=['Your customers don’t wait.'],hl='They just book.',focus=(0.6,0.6)),
   'Custom software that books your customers. No phone tag.'),
'waypoint-vs-lamborghini':('wp',dict(photo='D1ikFIycIHk',kick='Lamborghini Aventador',lines=['0 to 100 km/h','in under 3 seconds.'],box=(0.16,0.1,1,1),focus=(0.5,0.45)),
   dict(photo='ACnFSTBlnts',kick='Waypoint',lines=['Enquiry to reply','in under 60 seconds.'],hl='You never touched your phone.',mirror=True,box=(0,0.08,0.8,1.0),focus=(0.5,0.8),shade=0.75),
   'Custom software that answers your customers for you.'),
'staffkin-vs-john-deere':('sk',dict(photo='cfD0LrqEMmk',kick='John Deere',lines=['Does the heavy work','on the farm.'],focus=(0.4,0.6)),
   dict(photo='IESB4iFVuzA',kick='Staffkin',lines=['Does the heavy','paperwork in hiring.'],hl='You make the hire.',mirror=True,box=(0,0.04,0.8,1.0),focus=(0.5,0.3),shade=0.7),
   'Hiring software for small Canadian employers. AI does the paperwork. People make the hire.'),
'keegix-vs-cat':('kx',dict(photo='-mx0XkVtbYE',kick='Cat',lines=['Moves mountains','for a living.'],focus=(0.6,0.55)),
   dict(photo='/home/claude/sp/keegix/photos/cottage-porch-yellow-door.jpg',kick='Keegix',lines=['Moves guest questions'],hl='off your phone.',focus=(0.5,0.75),shade=0.45),
   'A digital welcome book and QR sign for your rental.'),
}
for k in (sys.argv[1:] or P):
    b,tp,bt,ds=P[k]; build('/home/claude/work/cmp/%s.png'%k,b,tp,bt,ds)
