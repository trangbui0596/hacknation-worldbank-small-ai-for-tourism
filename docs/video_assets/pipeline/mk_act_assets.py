import random, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageEnhance
L="pc/L/"
FB="/usr/local/lib/python3.11/dist-packages/font_roboto/files/Roboto-Black.ttf"
FR="/usr/local/lib/python3.11/dist-packages/font_roboto/files/Roboto-Bold.ttf"
random.seed(11)
def torn_poly(x0,y0,x1,y1,amp=6,step=16):
    pts=[]
    for x in range(int(x0),int(x1),step): pts.append((x,y0+random.uniform(-amp,amp)))
    for y in range(int(y0),int(y1),step): pts.append((x1+random.uniform(-amp,amp),y))
    for x in range(int(x1),int(x0),-step): pts.append((x,y1+random.uniform(-amp,amp)))
    for y in range(int(y1),int(y0),-step): pts.append((x0+random.uniform(-amp,amp),y))
    return pts
def ld(n): return Image.open(f"{L}c_{n}.png").convert("RGBA")
def scale_w(im,w): return im.resize((int(w),int(im.height*w/im.width)),Image.LANCZOS)
def scale_h(im,h): return im.resize((int(im.width*h/im.height),int(h)),Image.LANCZOS)
def tint(im,col,a):
    solid=Image.new("RGB",im.size,col); rgb=Image.blend(im.convert("RGB"),solid,a)
    out=rgb.convert("RGBA"); 
    if im.mode=="RGBA": out.putalpha(im.getchannel("A"))
    return out
def shadowed(im,off=(10,14),blur=12,alpha=120,pad=60):
    W,H=im.width+2*pad,im.height+2*pad
    out=Image.new("RGBA",(W,H),(0,0,0,0)); sh=Image.new("RGBA",(W,H),(30,20,10,0))
    sh.putalpha(im.getchannel("A").point(lambda v:int(v*alpha/255)).copy().resize(im.size)) if False else None
    a=Image.new("L",(W,H),0); a.paste(im.getchannel("A").point(lambda v:int(v*alpha/255)),(pad+off[0],pad+off[1])); a=a.filter(ImageFilter.GaussianBlur(blur))
    sh.putalpha(a); out=Image.alpha_composite(out,sh); out.alpha_composite(im,(pad,pad)); return out
W,H=2112,1188
def backdrop(name,skytint,skyline_flip,sky_off,river_tint):
    sky=Image.open(L+"sky.png").convert("RGB").resize((W,int(W*752/1344)),Image.LANCZOS)
    sky=sky.crop((0,0,W,H)) if sky.height>=H else sky.resize((W,H))
    sky=ImageEnhance.Color(sky).enhance(skytint[2]); sky=Image.blend(sky,Image.new("RGB",sky.size,skytint[0]),skytint[1])
    bg=sky.convert("RGBA")
    sl=scale_w(ld("skyline"),2300)
    if skyline_flip: sl=sl.transpose(Image.FLIP_LEFT_RIGHT)
    sl=tint(sl,skytint[0],skytint[1]*0.5)
    bg.alpha_composite(sl,(-sky_off,760-sl.height))
    rv=scale_w(ld("river"),W+80)
    rv=tint(rv,river_tint[0],river_tint[1])
    bg.alpha_composite(rv,(-40,745))
    bg.convert("RGB").save(f"cl5/bg_{name}.png")
backdrop("n",((255,206,150),0.0,1.0),False,100,((0,0,0),0.0))
backdrop("t",((255,150,90),0.38,1.05),True,40,((255,190,120),0.18))
backdrop("c",((40,60,120),0.50,0.9),False,160,((20,40,110),0.35))
# figures
def fig(name,cut,h):
    im=scale_h(ld(cut),h); out=shadowed(im); out.save(f"cl5/fig_{name}.png"); print(name,out.size)
fig("n","noor",900); fig("t","tourist",880); fig("c","champ",900)
# foreground (full-frame transparent)
def fgl(name,items):
    C=Image.new("RGBA",(1920,1080),(0,0,0,0))
    for im,x,y in items: C.alpha_composite(im,(int(x),int(y))) if x>=0 and y>=0 else C.alpha_composite(im.crop((max(0,-int(x)),max(0,-int(y)),im.width,im.height)),(max(0,int(x)),max(0,int(y))))
    C.save(f"cl5/fg_{name}.png")
fl=scale_w(ld("flowers"),560); flm=fl.transpose(Image.FLIP_LEFT_RIGHT)
fgl("n",[(shadowed(fl,pad=20),1380,640)])
fgl("t",[(shadowed(flm,pad=20),1340,650)])
grp=scale_w(ld("group"),620)
fgl("c",[(shadowed(grp,pad=20),1280,610)])
# ---------- tags ----------
def paper_tag(segs_lines,size,pos,rot=0,pad=34,font=FB,lh=1.14,minw=0):
    f=ImageFont.truetype(font,size); d0=ImageDraw.Draw(Image.new("L",(10,10)))
    def lw(segs): return sum(d0.textlength(t,font=f) for t,_ in segs)
    Wd=int(max(max(lw(s) for s in segs_lines),minw))+2*pad; Ht=int(size*lh)*len(segs_lines)+2*pad-6
    Lr=Image.new("RGBA",(Wd+80,Ht+80),(0,0,0,0)); mask=Image.new("L",Lr.size,0)
    ImageDraw.Draw(mask).polygon(torn_poly(40,40,40+Wd,40+Ht),fill=255)
    sh=Image.new("RGBA",Lr.size,(0,0,0,0)); sh.paste((40,30,20,110),(8,12),mask); sh=sh.filter(ImageFilter.GaussianBlur(9)); Lr=Image.alpha_composite(Lr,sh)
    rim=mask.filter(ImageFilter.MaxFilter(9)); Lr.paste(Image.new("RGBA",Lr.size,(250,246,236,255)),(0,0),rim)
    n=Image.effect_noise(Lr.size,28).convert("L"); paper=Image.composite(Image.new("RGBA",Lr.size,(244,236,218,255)),Image.new("RGBA",Lr.size,(225,214,190,255)),n.point(lambda v:150+v//3 if v>0 else 255))
    Lr.paste(paper,(0,0),mask); dr=ImageDraw.Draw(Lr)
    for i,segs in enumerate(segs_lines):
        x=40+pad; y=40+pad-6+i*int(size*lh)
        for t,hl in segs:
            w=d0.textlength(t,font=f)
            if hl: dr.polygon(torn_poly(int(x),int(y+size*0.64),int(x+w),int(y+size*1.02),amp=3,step=22),fill=(247,196,38,235))
            dr.text((x,y),t,font=f,fill=(28,26,23,255)); x+=w
    Lr=Lr.rotate(rot,expand=True,resample=Image.BICUBIC)
    C=Image.new("RGBA",(1920,1080),(0,0,0,0)); C.alpha_composite(Lr,(int(pos[0]),int(pos[1]))); return C
def S(*p): return [(t,h) for t,h in p]
caps={
 "j1":([S(("Noor answers each",0)),S(("question by ",0),("voice",1))],(1210,330)),
 "j2":([S(("Question by question,",0)),S(("in ",0),("Wolof",1))],(1210,330)),
 "g1":([S(("A Google listing,",0)),S(("drafted for her",1))],(1210,330)),
 "a1":([S(("The tourist ",0),("asks",1)),S(("in her own language",0))],(1210,330)),
 "a2":([S(("Noor's answer,",0)),S(("as a ",0),("voice note",1)),S(("(AI voice)",0))],(1210,300)),
 "f1":([S(("A ",0),("voice review",1),(",",0)),S(("cleaned up",0))],(1210,330)),
 "f2":([S(("She ",0),("pastes",1),(" it into",0)),S(("Google and posts",0)),S(("it herself",0))],(1210,300)),
 "d1":([S(("One ",0),("flood notice",1)),S(("to the community",0))],(1210,300)),
 "d2":([S(("Shown under",0)),S(("every answer",1))],(1210,300)),
 "r1":([S(("A visitor wants",0)),S(("something else",1))],(1210,250)),
 "r2":([S(("Teranga suggests",0)),S(("a ",0),("neighbour",1),(", in turn",0))],(1210,250)),
 "r3":([S(("A ",0),("person",1),(" connects",0)),S(("them",0))],(1210,250)),
 "h1":([S(("Noor ",0),("approves",1)),S(("each answer",0)),S(("with one digit",0))],(1210,300)),
 "h2":([S(("Nothing goes out",0)),S(("without ",0),("her",1))],(1210,300)),
}
for k,(lines,pos) in caps.items(): paper_tag(lines,50,pos,rot=random.choice([-1.6,1.4,-1.0,1.8])).save(f"cl5/cap_{k}.png")
# act title tags (big, centre-left)
paper_tag([S(("1 · ",0),("NOOR",1))],120,(110,330),rot=-2.0).save("cl5/title_n.png")
paper_tag([S(("2 · THE ",0),("TOURIST",1))],104,(90,330),rot=-2.0).save("cl5/title_t.png")
paper_tag([S(("3 · THE ",0),("COMMUNITY",1))],96,(70,330),rot=-2.0).save("cl5/title_c.png")
# small corner tags
paper_tag([S(("1 · ",0),("NOOR",1))],34,(36,26),rot=-1.5,pad=22).save("cl5/corner_n.png")
paper_tag([S(("2 · THE ",0),("TOURIST",1))],34,(36,26),rot=-1.5,pad=22).save("cl5/corner_t.png")
paper_tag([S(("3 · THE ",0),("COMMUNITY",1))],34,(36,26),rot=-1.5,pad=22).save("cl5/corner_c.png")
# chips top-right
paper_tag([S(("SMS + VOICE · ",0),("NO INTERNET",1))],34,(1230,34),rot=1.2,pad=22).save("cl5/chip_a.png")
paper_tag([S(("WHATSAPP · ",0),("WEEKLY SYNC ONLY",1))],34,(1160,34),rot=1.2,pad=22).save("cl5/chip_b.png")
paper_tag([S(("SHOWN ON WHATSAPP · ",0),("SAME COMMANDS BY SMS",1))],30,(1090,34),rot=1.0,pad=20).save("cl5/chip_c.png")
# coaching card
paper_tag([S(("AI",1),(" COACHING",0))],86,(1200,150),rot=-1.2,pad=30).save("cl5/coach_h.png")
paper_tag([S(("Latest ",0),("reviews",1),(" + tourist questions",0))],38,(1210,350),rot=1.0,pad=24,font=FR).save("cl5/coach_1.png")
paper_tag([S(("AI",1),(" analyses the data",0))],38,(1210,470),rot=-1.0,pad=24,font=FR).save("cl5/coach_2.png")
paper_tag([S(("Wolof SMS tips",1)),S(("to improve her service",0))],38,(1210,590),rot=1.2,pad=24,font=FR).save("cl5/coach_3.png")
paper_tag([S(("AI",1),("-suggested questions",0)),S(("Price · Meeting point",0)),S(("Duration · What's included",0)),S(("How to book · Cancellation",0)),S(("…and more about her business",0))],40,(1190,170),rot=-1.0,pad=28,font=FR).save("cl5/qlist.png")
print("done")
