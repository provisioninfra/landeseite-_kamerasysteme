"""Erzeugt die Lottie-Animation der Schwenk-Neige-Kamera (Produktbild 3): schwenkt um den Wandhalter, schwebt leicht,
rote Status-LED blinkt. Der gelbe Lichtschein kommt per CSS (drop-shadow) auf das Widget, damit er nicht an der Bühnenkante
abgeschnitten wird. Bühne 360 x 520, Kamera mittig; dieselbe Datei läuft am Computer (mittlere Spalte) und am Handy.
Bildquelle: assets/img/produkte/kamera-3-scharf.webp (Ausschnitt des Produktbilds, mit Real-ESRGAN auf 880 px Breite
hochgerechnet, damit die Kamera auch auf Retina-Displays scharf bleibt).
Aufruf: python3 tools/kamera_lottie_erzeugen.py  (Ausgabe in build/, dann in die Mediathek laden)"""
import json, base64, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / 'build'; OUT.mkdir(exist_ok=True)
SRC = ROOT / 'assets' / 'img' / 'produkte' / 'kamera-3-scharf.webp'
CW, CH = Image.open(SRC).size                       # 880 x 1511
cam_b64 = base64.b64encode(SRC.read_bytes()).decode()
# Geometrie wurde für ein 270 px breites Bild entworfen; das große Bild wird auf diese Größe skaliert
BASE_W = 270
K = CW / BASE_W                                      # Bildpixel je Entwurfspixel
SCALE = 100 * BASE_W / CW                           # Ebenen-Skalierung in Prozent
MOUNT = [228 * K, 228 * K]                          # Drehpunkt (Wandhalter) in Bildpixeln
LED = [86 * K, 386 * K]                             # Status-LED neben der Linse in Bildpixeln
W, H, FPS, FRAMES = 360, 520, 25, 150
cam_pos = (45 + 228, 28 + 228)                      # Position des Drehpunkts auf der Bühne

def ease(t, s):
    return {"t": t, "s": s, "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}}

px, py = cam_pos
pos = [{"t": 0, "s": [px, py, 0], "i": {"x": [0.42] * 3, "y": [1] * 3}, "o": {"x": [0.58] * 3, "y": [0] * 3}},
       {"t": FRAMES // 2, "s": [px, py + 6, 0], "i": {"x": [0.42] * 3, "y": [1] * 3}, "o": {"x": [0.58] * 3, "y": [0] * 3}},
       {"t": FRAMES, "s": [px, py, 0]}]
rot = [ease(0, [0]), ease(FRAMES // 4, [-6]), ease(FRAMES // 2, [0]), ease(3 * FRAMES // 4, [6]), {"t": FRAMES, "s": [0]}]
blink = []
for t in range(0, FRAMES, 25):
    blink += [{"t": t, "s": [0], "h": 1}, {"t": t + 4, "s": [100], "h": 1}, {"t": t + 9, "s": [0], "h": 1}]
blink += [{"t": FRAMES, "s": [0], "h": 1}]
def tr():
    return {"ty": "tr", "p": {"a": 0, "k": [0, 0]}, "a": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [100, 100]}, "r": {"a": 0, "k": 0}, "o": {"a": 0, "k": 100}}
led_shapes = [   # Größen in Bildpixeln (die LED-Ebene hängt an der skalierten Kamera-Ebene)
    {"ty": "gr", "nm": "LED-Schein", "it": [{"ty": "el", "p": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [30 * K, 30 * K]}}, {"ty": "fl", "c": {"a": 0, "k": [1, 0.15, 0.1, 1]}, "o": {"a": 0, "k": 35}}, tr()]},
    {"ty": "gr", "nm": "LED", "it": [{"ty": "el", "p": {"a": 0, "k": [0, 0]}, "s": {"a": 0, "k": [11 * K, 11 * K]}}, {"ty": "fl", "c": {"a": 0, "k": [1, 0.2, 0.15, 1]}, "o": {"a": 0, "k": 100}}, tr()]},
]
layers = [
    {"ddd": 0, "ind": 1, "ty": 4, "nm": "LED", "parent": 2, "sr": 1, "ks": {"o": {"a": 1, "k": blink}, "r": {"a": 0, "k": 0}, "p": {"a": 0, "k": LED + [0]}, "a": {"a": 0, "k": [0, 0, 0]}, "s": {"a": 0, "k": [100, 100, 100]}}, "ao": 0, "shapes": led_shapes, "ip": 0, "op": FRAMES, "st": 0, "bm": 0},
    {"ddd": 0, "ind": 2, "ty": 2, "nm": "Kamera", "refId": "cam", "sr": 1, "ks": {"o": {"a": 0, "k": 100}, "r": {"a": 1, "k": rot}, "p": {"a": 1, "k": pos}, "a": {"a": 0, "k": MOUNT + [0]}, "s": {"a": 0, "k": [SCALE, SCALE, 100]}}, "ao": 0, "ip": 0, "op": FRAMES, "st": 0, "bm": 0},
]
data = {"v": "5.6.6", "fr": FPS, "ip": 0, "op": FRAMES, "w": W, "h": H, "nm": "kamera-schwenk", "ddd": 0,
        "assets": [{"id": "cam", "w": CW, "h": CH, "u": "", "p": "data:image/webp;base64," + cam_b64, "e": 1}],
        "layers": layers, "markers": []}
s = json.dumps(data, separators=(",", ":")); (OUT / "kamera-schwenk.json").write_text(s)
print("kamera-schwenk.json", len(s) // 1024, "KB", "Bild", CW, "x", CH, "Skalierung", round(SCALE, 2), "%")
