#!/usr/bin/env python3
"""Lottie-Dateien verkleinern, ohne ein Pixel zu verändern: eingebettete PNG-Bilder werden als verlustfreies WebP neu
kodiert (nur wenn das kleiner ist). Vektordaten, Ebenen, Zeiten und Abmessungen bleiben unverändert; lottie-web
rendert eingebettete WebP-Bilder in allen aktuellen Browsern.

Aufruf: python3 -I tools/lottie_webp.py quelle.json ziel.json
Prüft nach dem Kodieren jedes Bild Pixel für Pixel gegen das Original und bricht bei Abweichung ab.
"""
import base64, io, json, sys
from PIL import Image

def convert(src, dst):
    d = json.loads(open(src, "rb").read())
    before = len(open(src, "rb").read()); saved = 0; n = 0
    for a in d.get("assets", []):
        p = a.get("p")
        if not isinstance(p, str) or not p.startswith("data:image/png;base64,"):
            continue
        raw = base64.b64decode(p[p.find(",") + 1:])
        im = Image.open(io.BytesIO(raw)); im.load()
        out = io.BytesIO(); im.save(out, format="WEBP", lossless=True, quality=100, method=6, exact=True); webp = out.getvalue()   # exact: auch Farbwerte unter voll transparenten Pixeln erhalten
        if len(webp) >= len(raw):
            continue
        back = Image.open(io.BytesIO(webp)); back.load()
        if back.size != im.size or back.convert("RGBA").tobytes() != im.convert("RGBA").tobytes():
            raise SystemExit(f"Abweichung bei Asset {a.get('id')} in {src}")
        a["p"] = "data:image/webp;base64," + base64.b64encode(webp).decode("ascii")
        saved += len(raw) - len(webp); n += 1
    data = json.dumps(d, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    open(dst, "wb").write(data)
    return before, len(data), n

if __name__ == "__main__":
    b, a, n = convert(sys.argv[1], sys.argv[2])
    print(f"{sys.argv[1].split('/')[-1]}: {b // 1024} KB -> {a // 1024} KB, {n} Bilder umkodiert, identische Pixel")
