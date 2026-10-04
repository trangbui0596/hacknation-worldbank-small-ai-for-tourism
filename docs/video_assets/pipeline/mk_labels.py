import random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
FONT="/usr/local/lib/python3.11/dist-packages/font_roboto/files/Roboto-Black.ttf"
random.seed(7)
def torn_poly(x0,y0,x1,y1,amp=7,step=18):
    pts=[]
    for x in range(x0,x1,step): pts.append((x,y0+random.uniform(-amp,amp)))
    for y in range(y0,y1,step): pts.append((x1+random.uniform(-amp,amp),y))
    for x in range(x1,x0,-step): pts.append((x,y1+random.uniform(-amp,amp)))
    for y in range(y1,y0,-step): pts.append((x0+random.uniform(-amp,amp),y))
    return pts
def label(name,lines,pos,hl,rot,size=104,pad=44):
    f=ImageFont.truetype(FONT,size)
    d0=ImageDraw.Draw(Image.new("L",(10,10)))
    ws=[d0.textlength(t,font=f) for t in lines]; lh=int(size*1.12)
    W=int(max(ws))+2*pad; H=lh*len(lines)+2*pad-10
    L=Image.new("RGBA",(W+80,H+80),(0,0,0,0))
    mask=Image.new("L",L.size,0); ImageDraw.Draw(mask).polygon(torn_poly(40,40,40+W,40+H),fill=255)
    sh=Image.new("RGBA",L.size,(0,0,0,0)); sh.paste((40,30,20,110),(8,12),mask); sh=sh.filter(ImageFilter.GaussianBlur(9))
    L=Image.alpha_composite(L,sh)
    # paper with a lighter deckle rim
    rim=mask.filter(ImageFilter.MaxFilter(9)); rimlayer=Image.new("RGBA",L.size,(250,246,236,255)); L.paste(rimlayer,(0,0),rim)
    paper=Image.new("RGBA",L.size,(244,236,218,255))
    # fibre noise
    n=Image.effect_noise(L.size,28).convert("L"); paper=Image.composite(paper,Image.new("RGBA",L.size,(225,214,190,255)),n.point(lambda v:150+v//3 if v>0 else 255))
    L.paste(paper,(0,0),mask)
    dr=ImageDraw.Draw(L)
    for i,t in enumerate(lines):
        y=40+pad-8+i*lh
        if hl and hl[0]==i:
            w=d0.textlength(t,font=f); x=40+pad
            dr.polygon(torn_poly(int(x),int(y+size*0.62),int(x+w),int(y+size*1.0),amp=3,step=22),fill=(247,196,38,235))
        dr.text((40+pad,y),t,font=f,fill=(28,26,23,255))
    L=L.rotate(rot,expand=True,resample=Image.BICUBIC)
    C=Image.new("RGBA",(1920,1080),(0,0,0,0)); C.paste(L,pos,L); C.save(f"cl/lab_{name}.png"); print(name,L.size)
label("1",["A TOURIST","WRITES IN","GERMAN."],(40,90),(2,),-2.0)
label("2",["NOOR SPEAKS","WOLOF."],(1000,640),(1,),1.8)
label("3",["THE UNREAD","MESSAGE."],(40,40),(1,),-1.6)
# reveal shadow from reveal_mask
m=Image.open("cl/reveal_mask.png").convert("L")
sh=m.filter(ImageFilter.GaussianBlur(14)).point(lambda v:int(v*0.55))
rgba=Image.new("RGBA",m.size,(20,14,6,0)); rgba.putalpha(sh); rgba.save("cl/reveal_shadow.png")
