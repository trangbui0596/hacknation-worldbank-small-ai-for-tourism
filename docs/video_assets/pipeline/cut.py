import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage as ndi
def cutout(name, outline=0, thr=246, grow=0):
    im=Image.open(f"{name}.png").convert("RGB"); a=np.asarray(im).astype(int)
    near=(a.min(axis=2)>=thr)
    lab,n=ndi.label(near)
    border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    bg=np.isin(lab,list(border))
    fg=~bg
    # remove tiny speckle, fill holes
    fg=ndi.binary_opening(fg,iterations=1); fg=ndi.binary_fill_holes(fg)
    al=Image.fromarray((fg*255).astype("uint8")).filter(ImageFilter.GaussianBlur(0.8))
    rgba=im.convert("RGBA"); rgba.putalpha(al)
    if outline:
        m=np.asarray(al)>128
        big=ndi.binary_dilation(m,iterations=outline)
        big=Image.fromarray((big*255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.2))
        base=Image.new("RGBA",im.size,(250,246,236,255)); base.putalpha(big)
        rgba=Image.alpha_composite(base,rgba)
    bb=rgba.getchannel("A").point(lambda v:255 if v>20 else 0).getbbox()
    rgba=rgba.crop(bb); rgba.save(f"c_{name}.png"); print(name,rgba.size)
for n,o in [("tourist",7),("noor",7),("skyline",0),("river",0),("banks",0),("bridge",0),("flowers",0),("plane",0),("bubble",0)]:
    cutout(n,o)
