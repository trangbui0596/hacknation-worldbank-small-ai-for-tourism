exec(open("pc/mk_act_assets.py").read().split("W,H=2112")[0])   # helpers (ld, scale_*, shadowed, torn_poly)
exec("def _x(): pass")
import re
src=open("pc/mk_act_assets.py").read()
# bring in paper_tag/S without running the rest
start=src.index("def paper_tag"); end=src.index("caps={")
exec(src[start:end])
FF="/tmp/fonts/Fraunces-Black.ttf"; FA="/tmp/fonts/Atkinson-Regular.ttf"; FAB="/tmp/fonts/Atkinson-Bold.ttf"
paper=Image.open("cl/paper.png").convert("RGB")
# ---- page A: NEXT ----
paper_tag([S(("NEXT",1),(" ON THE ROAD",0))],110,(90,50),rot=-2.0).save("cl5/end_next.png")
def card(name,cut,caption,x,y,rot):
    ill=scale_h(ld(cut),470) if ld(cut).height>=ld(cut).width*1.2 else scale_w(ld(cut),540)
    ill=ill.rotate(rot,expand=True,resample=Image.BICUBIC,fillcolor=(0,0,0,0)) if False else ill
    C=Image.new("RGBA",(1920,1080),(0,0,0,0))
    sh=shadowed(ill,pad=24); C.alpha_composite(sh,(int(x-sh.width/2),y))
    cap=paper_tag(caption,60,(0,0))
    bb=cap.getchannel("A").getbbox(); capc=cap.crop(bb)
    C.alpha_composite(capc,(int(x-capc.width/2),y+sh.height-20))
    C.save(f"cl5/end_card_{name}.png")
card("sms","i_sms",[S(("Live ",0),("SMS",1))],380,250,0)
card("check","i_check",[S(("Native ",0),("Wolof",1)),S(("review",0))],960,250,0)
card("globe","i_globe",[S(("More ",0),("languages",1))],1540,250,0)
# ---- page B: closing (1920x1180 static) ----
B=Image.new("RGB",(1920,1180)); B.paste(paper,(0,0)); B.paste(paper.crop((0,0,1920,100)).transpose(Image.FLIP_TOP_BOTTOM),(0,1080))
Bd=B.convert("RGBA"); d=ImageDraw.Draw(Bd)
logo=Image.open("cl/logo_crop.png").convert("RGB"); logo=logo.resize((820,int(logo.height*820/logo.width)),Image.LANCZOS)
Bd.paste(logo,(100,70))
f1=ImageFont.truetype(FF,74); y=315
lines=[[("Teranga gives Noor her ",0),("voice,",1)],[("and her community its ",0),("champion.",1)]]
for segs in lines:
    x=110
    for t,hl in segs:
        w=d.textlength(t,font=f1)
        if hl: d.polygon(torn_poly(int(x),int(y+52),int(x+w),int(y+88),amp=3,step=22),fill=(247,196,38,235))
        d.text((x,y),t,font=f1,fill=(28,26,23,255)); x+=w
    y+=100
fl=ImageFont.truetype(FAB,46); d.text((110,620),"teranga-gambia.lovable.app",font=fl,fill=(15,118,110,255))
d.text((110,690),"github.com/trangbui0596/teranga-gambia",font=ImageFont.truetype(FA,34),fill=(28,26,23,255))
ff=ImageFont.truetype(FA,26)
d.text((110,940),"World Bank × Hack-Nation · Small AI for Development · Tourism",font=ff,fill=(70,66,60,255))
d.text((110,980),"Prototype. Noor is fictional. Wolof audio is synthetic.",font=ff,fill=(70,66,60,255))
Bd.convert("RGB").save("cl5/end_pageB.png")
# bridge scene pieces
br=shadowed(scale_w(ld("bridge"),820),pad=20); br.save("cl5/end_bridge.png")
shadowed(scale_h(ld("tourist"),270),pad=20).save("cl5/end_tourist.png")
shadowed(scale_h(ld("noor"),270),pad=20).save("cl5/end_noor.png")
scale_w(ld("plane"),330).save("cl5/end_plane.png")
print("ok",br.size)
