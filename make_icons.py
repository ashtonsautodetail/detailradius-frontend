#!/usr/bin/env python3
"""DetailRadius brand icons: MIDNIGHT CHROME "Orbit D + Signal" mark.
Bold chrome D, white blip at top-right corner emitting two signal arcs.
(Ashton picked "mix of Orbit D + Radius Signal", 2026-07-23.)"""
from PIL import Image, ImageDraw
OBSIDIAN=(15,17,22,255); CH=(201,205,214,255); ICE=(255,255,255,255)
CH80=(201,205,214,204); CH45=(201,205,214,115)

def mark(size, rounded=True, path=None, scale=1.0, bg=True):
    img = Image.new("RGBA",(size,size),(0,0,0,0)); d = ImageDraw.Draw(img)
    if bg:
        if rounded: d.rounded_rectangle([0,0,size,size], radius=size*0.225, fill=OBSIDIAN)
        else: d.rectangle([0,0,size,size], fill=OBSIDIAN)
    s = size/48.0*scale; off = size*(1-scale)/2; X = lambda v: off+v*s
    # D: stem + outer half-disc, then inner cut
    d.rectangle([X(11),X(9),X(24),X(40)], fill=CH)
    d.pieslice([X(24-15.5),X(24.5-15.5),X(24+15.5),X(24.5+15.5)], start=-90, end=90, fill=CH)
    d.rectangle([X(17),X(15),X(24),X(34)], fill=OBSIDIAN)
    d.pieslice([X(24-9.5),X(24.5-9.5),X(24+9.5),X(24.5+9.5)], start=-90, end=90, fill=OBSIDIAN)
    # signal arcs from blip at (33,13), opening top-right
    w1 = max(1, int(2.6*s)); w2 = max(1, int(2.4*s))
    d.arc([X(33-6.8),X(13-6.8),X(33+6.8),X(13+6.8)], start=-90, end=0, fill=CH80, width=w1)
    d.arc([X(33-11.2),X(13-11.2),X(33+11.2),X(13+11.2)], start=-90, end=0, fill=CH45, width=w2)
    # white blip
    r = 2.9*s
    d.ellipse([X(33)-r,X(13)-r,X(33)+r,X(13)+r], fill=ICE)
    if path: img.save(path); print(path, img.size)
    return img

if __name__ == "__main__":
    mark(192, True, "icon-192.png"); mark(512, True, "icon-512.png")
    mark(512, False, "icon-512-maskable.png", 0.72); mark(180, True, "apple-touch-icon.png")
