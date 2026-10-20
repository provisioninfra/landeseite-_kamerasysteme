"""Setzt die Person auf der Szenen-Grafik der Startseite (Untitled-design-14.png bzw. die Handy-Variante) als dunkle
Kapuzen-Silhouette (Einbrecher) um. Freisteller mit rembg (Modell u2net), dann Kapuze, dunkle Füllung und ein schwacher
grüner Lichtsaum. Aufruf: python3 tools/einbrecher_silhouette.py <quelle.png> <maske.png> <x1,y1,x2,y2> <ziel.jpg>
Die Maske entsteht mit: rembg (remove(crop, session=new_session('u2net'), only_mask=True)) auf dem Ausschnitt.
Verwendete Ausschnitte: Computer (2400x1104): 1680,100,2080,1000; Handy (1276x1104): 600,60,940,1104."""
import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def burglar(src_path, crop_box, mask_path, out_path):
    src = Image.open(src_path).convert('RGBA'); crop = src.crop(crop_box); w, h = crop.size
    mask = Image.open(mask_path).convert('L'); a = np.array(mask); ys, xs = np.where(a > 128)
    top = ys.min(); H = ys.max() - top
    head = a[top:top + int(H * 0.10)]; hy, hx = np.where(head > 128)
    head_l, head_r = hx.min(), hx.max(); head_w = head_r - head_l; head_h = head.shape[0]
    hood = Image.new('L', (w, h), 0); d = ImageDraw.Draw(hood)
    cx = (head_l + head_r) / 2 + head_w * 0.08; cy = top + head_h * 0.62
    rx = head_w * 0.72; ry = head_h * 0.98
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
    d.polygon([(cx + rx * 0.15, cy + ry * 0.3), (cx + rx * 0.98, cy + ry * 0.2), (cx + rx * 1.05, cy + ry * 2.3), (cx + rx * 0.35, cy + ry * 2.1)], fill=255)
    full = Image.fromarray(np.maximum(np.array(mask), np.array(hood))).filter(ImageFilter.GaussianBlur(1.0))
    grad = np.linspace(0, 1, h)[:, None]
    fill = np.zeros((h, w, 4), dtype=np.uint8)
    fill[:, :, 0] = (5 + 4 * grad).astype(np.uint8); fill[:, :, 1] = (7 + 5 * grad).astype(np.uint8); fill[:, :, 2] = (16 + 8 * grad).astype(np.uint8); fill[:, :, 3] = 255
    out = Image.composite(Image.fromarray(fill, 'RGBA'), crop, full)
    m = np.array(full).astype(np.int16); shifted = np.zeros_like(m); shifted[:, 5:] = m[:, :-5]
    rim = Image.fromarray(np.clip(m - shifted, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.6))
    rim_a = Image.fromarray((np.array(rim) * 0.5).astype(np.uint8))
    out = Image.composite(Image.new('RGBA', (w, h), (120, 255, 170, 255)), out, rim_a)
    res = src.copy(); res.paste(out, crop_box[:2]); res.convert('RGB').save(out_path, quality=92)

if __name__ == '__main__':
    src, mask, box, out = sys.argv[1:5]
    burglar(src, tuple(int(v) for v in box.split(',')), mask, out)
