#!/usr/bin/env python3
"""Generate PWA icons matching the DetailRadius favicon (navy rounded square, cyan car)."""
from PIL import Image, ImageDraw

NAVY = (11, 21, 51, 255)      # #0B1533
CYAN = (56, 189, 248, 255)    # #38BDF8

def make(size, maskable=False, path="icon.png"):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    s = size / 40.0  # favicon viewBox is 40x40

    if maskable:
        # maskable: full-bleed background, art shrunk into the 80% safe zone
        d.rectangle([0, 0, size, size], fill=NAVY)
        scale = 0.72
        off = size * (1 - scale) / 2
        s2 = s * scale
        def X(v): return off + v * s2
    else:
        r = size * 0.225  # rounded corner radius
        d.rounded_rectangle([0, 0, size, size], radius=r, fill=NAVY)
        def X(v): return v * s
        s2 = s

    # car body bar: x=4 y=21 w=32 h=7 rx=3.5
    d.rounded_rectangle([X(4), X(21), X(4+32), X(21+7)], radius=3.5*s2, fill=CYAN)
    # cab: trapezoid M9 21 L13 13 H27 L31 21 Z
    d.polygon([(X(9), X(21)), (X(13), X(13)), (X(27), X(13)), (X(31), X(21))], fill=CYAN)
    # wheels: circles (12,29) r3 and (28,29) r3 in navy
    for cx in (12, 28):
        d.ellipse([X(cx-3), X(29-3), X(cx+3), X(29+3)], fill=NAVY)

    img.save(path, "PNG")
    print(path, img.size)

make(192, False, "/tmp/frontend/icon-192.png")
make(512, False, "/tmp/frontend/icon-512.png")
make(512, True,  "/tmp/frontend/icon-512-maskable.png")
make(180, False, "/tmp/frontend/apple-touch-icon.png")
