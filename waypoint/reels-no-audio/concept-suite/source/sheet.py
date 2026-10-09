"""python3 sheet.py <name-prefix> -> stills/<prefix>_sheet.png (contact sheet of that reel's stills)"""
import sys, glob, os
from PIL import Image, ImageDraw
pre = sys.argv[1]; fs = sorted(f for f in glob.glob(f"stills/{pre}*_*.png") if "sheet" not in f)
ims = [Image.open(f).resize((360, 640)) for f in fs]
cols = 5; rows = (len(ims)+cols-1)//cols
S = Image.new("RGB", (cols*370, rows*680), "white"); d = ImageDraw.Draw(S)
for i,(im,f) in enumerate(zip(ims,fs)):
    x,y = (i%cols)*370, (i//cols)*680; S.paste(im,(x+5,y+5)); d.text((x+8,y+650), os.path.basename(f)[-9:-4], fill="black")
S.save(f"stills/{pre}_sheet.png"); print(f"stills/{pre}_sheet.png", len(ims))
