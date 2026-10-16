"""Produktfotos freistellen: Masken-Vereinigung (u2net + isnet-general-use), Kantenglättung, 4:3-Leinwand mit Transparenz.
Aufruf: python produkt_freistellen.py "quelle.png|ziel.png|vorschau.jpg" ... (Umgebung mit rembg + onnxruntime, siehe TECHNIK-CHECK.md)"""
import sys, numpy as np
from PIL import Image, ImageFilter
from rembg import remove, new_session
W, H, PAD = 1600, 1200, 0.08
sessions = {m: new_session(m) for m in ['u2net', 'isnet-general-use']}
def mask(im, m):
    return np.asarray(remove(im, session=sessions[m], only_mask=True, post_process_mask=True), dtype=np.float32)
jobs = [l.split('|') for l in sys.argv[1:]]
for src, dst, prev in jobs:
    im = Image.open(src).convert('RGB')
    a = np.maximum(mask(im, 'u2net'), mask(im, 'isnet-general-use'))          # Vereinigung: Löcher des einen füllt der andere
    # Reinweiße Pixel weit außerhalb der Kante sicher transparent (Hintergrund ist 255/255/255)
    rgb = np.asarray(im, dtype=np.int16)
    white = (rgb.min(axis=2) >= 252)
    am = Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    a = np.asarray(am, dtype=np.float32)
    inner = np.asarray(Image.fromarray((a > 128).astype(np.uint8) * 255).filter(ImageFilter.MinFilter(9)), dtype=np.float32) > 0
    a[white & ~inner] = 0
    alpha = Image.fromarray(a.astype(np.uint8))
    out = im.convert('RGBA'); out.putalpha(alpha)
    arr = np.asarray(alpha); ys, xs = np.where(arr > 10)
    box = (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)
    cut = out.crop(box)
    sc = min(W * (1 - 2 * PAD) / cut.width, H * (1 - 2 * PAD) / cut.height)
    cut = cut.resize((round(cut.width * sc), round(cut.height * sc)), Image.LANCZOS)
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    canvas.paste(cut, ((W - cut.width) // 2, (H - cut.height) // 2), cut)
    canvas.save(dst, optimize=True)
    bg = Image.new('RGBA', (W, H), (1, 10, 44, 255)); bg.alpha_composite(canvas)
    bg.convert('RGB').resize((800, 600), Image.LANCZOS).save(prev, quality=88)
    print(dst, 'Box', box, 'Skalierung', round(sc, 2), 'Ausschnitt', cut.size, flush=True)
