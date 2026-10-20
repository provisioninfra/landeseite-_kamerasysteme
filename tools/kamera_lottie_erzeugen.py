"""Aufruf: python3 tools/kamera_lottie_erzeugen.py  (Ausgabe in build/, dann in die Mediathek laden)
Erzeugt die Lottie-Animation der Schwenk-Neige-Kamera (Produktbild 3): schwenkt um den Wandhalter, schwebt leicht,
rote Status-LED blinkt (gelber Lichtschein per CSS auf dem Widget). Zwei Varianten: Desktop (1512x769, Position wie das Schloss
der Startseite) und Mobil (kompakte Bühne)."""
import json, base64, io, pathlib
from PIL import Image, ImageDraw, ImageFilter
HERE = pathlib.Path(__file__).resolve().parent.parent / 'build'; HERE.mkdir(exist_ok=True)
SRC = Image.open(pathlib.Path(__file__).resolve().parent.parent / 'assets' / 'img' / 'produkte' / 'kamera-3.png').convert('RGBA')
cam = SRC.crop(SRC.getbbox())                       # 587 x 1008
SCALE = 270 / cam.width
cam = cam.resize((270, round(cam.height * SCALE)), Image.LANCZOS)   # 270 x 464
CW, CH = cam.size
buf = io.BytesIO(); cam.save(buf, 'PNG', optimize=True); cam_b64 = base64.b64encode(buf.getvalue()).decode()
# Lichtschein (gelb, weich) als Bild
G = 520
glow = Image.new('RGBA', (G, G), (0, 0, 0, 0)); d = ImageDraw.Draw(glow)
for i in range(60, 0, -1):
    r = G / 2 * i / 60; a = int(70 * (1 - i / 60) ** 1.6)
    d.ellipse([G / 2 - r, G / 2 - r, G / 2 + r, G / 2 + r], fill=(251, 201, 27, a))
glow = glow.filter(ImageFilter.GaussianBlur(18))
buf = io.BytesIO(); glow.save(buf, 'PNG', optimize=True); glow_b64 = base64.b64encode(buf.getvalue()).decode()
# Koordinaten im Kamerabild (270 x 464): Halterung (Drehpunkt) und Linse/LED
MOUNT = [228, 228]; LED = [86, 386]
def ease(t, s, nxt=None):
    k = {"t": t, "s": s, "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}}
    return k
def build(W, H, cam_pos, glow_pos, glow_scale, fps=25, frames=150):
    # Position (Anker = Halterung) mit leichtem Schweben, Rotation = Schwenk
    px, py = cam_pos
    pos = [{"t": 0, "s": [px, py, 0], "i": {"x": [0.42, 0.42, 0.42], "y": [1, 1, 1]}, "o": {"x": [0.58, 0.58, 0.58], "y": [0, 0, 0]}},
           {"t": frames // 2, "s": [px, py + 6, 0], "i": {"x": [0.42, 0.42, 0.42], "y": [1, 1, 1]}, "o": {"x": [0.58, 0.58, 0.58], "y": [0, 0, 0]}},
           {"t": frames, "s": [px, py, 0]}]
    rot = [ease(0, [0]), ease(frames // 4, [-6]), ease(frames // 2, [0]), ease(3 * frames // 4, [6]), {"t": frames, "s": [0]}]
    blink = []
    for t in range(0, frames, 25):
        blink += [{"t": t, "s": [0], "h": 1}, {"t": t + 4, "s": [100], "h": 1}, {"t": t + 9, "s": [0], "h": 1}]
    blink += [{"t": frames, "s": [0], "h": 1}]
    led_shapes = [
        {"ty": "gr", "nm": "LED-Schein", "it": [{"ty": "el", "p": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [30, 30]}}, {"ty": "fl", "c": {"a": 0, "k": [1, 0.15, 0.1, 1]}, "o": {"a": 0, "k": 35}}, {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}]},
        {"ty": "gr", "nm": "LED", "it": [{"ty": "el", "p": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [11, 11]}}, {"ty": "fl", "c": {"a": 0, "k": [1, 0.2, 0.15, 1]}, "o": {"a": 0, "k": 100}}, {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}]},
    ]
    layers = [
        {"ddd": 0, "ind": 1, "ty": 4, "nm": "LED", "parent": 2, "sr": 1, "ks": {"o": {"a": 1, "k": blink}, "r": {"a": 0, "k": 0}, "p": {"a": 0, "k": LED + [0]}, "a": {"a": 0, "k": [0, 0, 0]}, "s": {"a": 0, "k": [100, 100, 100]}}, "ao": 0, "shapes": led_shapes, "ip": 0, "op": frames, "st": 0, "bm": 0},
        {"ddd": 0, "ind": 2, "ty": 2, "nm": "Kamera", "refId": "cam", "sr": 1, "ks": {"o": {"a": 0, "k": 100}, "r": {"a": 1, "k": rot}, "p": {"a": 1, "k": pos}, "a": {"a": 0, "k": MOUNT + [0]}, "s": {"a": 0, "k": [100, 100, 100]}}, "ao": 0, "ip": 0, "op": frames, "st": 0, "bm": 0},
    ]   # kein Lichtschein in der Datei: der gelbe Schein kommt per CSS (drop-shadow) auf das Widget und wird so nicht an der Bühnenkante abgeschnitten
    return {"v": "5.6.6", "fr": fps, "ip": 0, "op": frames, "w": W, "h": H, "nm": "kamera-schwenk", "ddd": 0,
            "assets": [{"id": "cam", "w": CW, "h": CH, "u": "", "p": "data:image/png;base64," + cam_b64, "e": 1}],
            "layers": layers, "markers": []}
# Desktop: Kamerabild oben links bei (575, 20) -> Halterung bei (575+228, 20+228); Lichtschein hinter dem Kamerakopf (ca. 672, 330)
desk = build(1512, 769, (575 + MOUNT[0], 20 + MOUNT[1]), (672, 330), 100)
# Mobil: kompakte Bühne 360 x 520, Kamera mittig
mob = build(360, 520, (45 + MOUNT[0], 28 + MOUNT[1]), (142, 340), 90)
for name, data in (("kamera-schwenk-desktop.json", desk), ("kamera-schwenk-mobil.json", mob)):
    s = json.dumps(data, separators=(",", ":")); (HERE / name).write_text(s); print(name, len(s) // 1024, "KB")
