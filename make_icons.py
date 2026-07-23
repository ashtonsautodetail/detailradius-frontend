#!/usr/bin/env python3
"""DetailRadius brand icons: obsidian tile + MIDNIGHT CHROME radar-ring mark.
Chrome-silver ring/dot, white blip. Semantic greens elsewhere are unrelated."""
from PIL import Image, ImageDraw
OBSIDIAN=(15,17,22,255); CH=(201,205,214,255); CH_SOFT=(201,205,214,76); ICE=(255,255,255,255)

def radar(size, rounded=True, path="icon.png", scale=1.0):
    img = Image.new("RGBA",(size,size),(0,0,0,0)); d = ImageDraw.Draw(img)
    if rounded: d.rounded_rectangle([0,0,size,size], radius=size*0.225, fill=OBSIDIAN)
    else: d.rectangle([0,0,size,size], fill=OBSIDIAN)
    s = size/48.0*scale; off = size*(1-scale)/2; X = lambda v: off+v*s
    w = max(2, int(size*0.073))
    d.ellipse([X(5),X(5),X(43),X(43)], outline=CH, width=w)
    d.pieslice([X(5),X(5),X(43),X(43)], start=-90, end=-30, fill=CH_SOFT)
    r=size*0.088; cx=cy=size*scale/2+off
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=CH)
    bx,by,br = X(33.5),X(11.5),size*0.062
    d.ellipse([bx-br,by-br,bx+br,by+br], fill=ICE)
    img.save(path); print(path, img.size)

if __name__ == "__main__":
    radar(192, True, "icon-192.png"); radar(512, True, "icon-512.png")
    radar(512, False, "icon-512-maskable.png", 0.72); radar(180, True, "apple-touch-icon.png")
