#!/usr/bin/env python3
"""Zutrittssystem-Seite (ID 3316), 18.11.2026: Im Block „Zusätzlich bekommst du“ (Container cb32d04) zeichnen fünf
Lottie-Ebenen die Kästchen, Icons und Verbindungslinien um den Türgriff; sie skalieren mit der Blockbreite. Die fünf
Beschriftungen liegen in absolut positionierten Containern mit festen Pixelwerten je Elementor-Breakpoint. Dadurch
passten Text und Kästchen nur bei je einer Breite pro Breakpoint zusammen (Desktop ab 1512 px, wo der Block fest
1512 px breit ist); bei Tablets quer und Laptops (1024–1511 px) rutschten die Texte aus den Kästchen und über die Icons.

Lösung ohne Strukturänderung: Element-CSS am Block (Kennung `pv-griff`), das Position, Breite und Mindesthöhe der fünf
Beschriftungs-Container zwischen 768 und 1511 px proportional zur Fensterbreite setzt – genau auf die gemessenen
Kästchen (Anteile aus der Lottie-Geometrie, siehe TECHNIK-CHECK). Ab 1512 px bleibt alles wie vom Designer eingestellt;
Schrift, Animationen (Einblenden, Hover-Vergrößerung, Lottie-Hover) bleiben unverändert.

Aufruf: python3 -I tools/zutritt_griff_beschriftung.py export.json ziel.json   (Ausgabe: Zahl der Änderungen)
"""
import json, pathlib, sys

BLOCK = "cb32d04"
KENNUNG = "pv-griff"
A = 0.4818            # Höhe/Breite der Lottie-Ebene
FW, FH = 0.2239, 0.1470   # Kästchenbreite/-höhe als Anteil der Ebenenbreite/-höhe
KARTEN = [  # (Container, Anteil x, Anteil y, Spalte)
    ("08fd7c8", 0.1250, 0.2316, "links"), ("b76492c", 0.1250, 0.4046, "links"), ("4d000ef", 0.1250, 0.5777, "links"),
    ("d20cee8", 0.6510, 0.2986, "rechts"), ("38aacf7", 0.6510, 0.4716, "rechts")]
BEREICHE = [  # (min, max, Ebene x, Ebene y, Randabzug Ebenen 1–4, Randabzug Ebene 5, Spalten-Oberkante)
    (768, 1024, 30, 90, 40, 20, 60), (1025, 1280, 30, 80, 40, 20, 10), (1281, 1440, 10, 120, 20, 20, 10), (1441, 1511, 10, 70, 20, 20, 10)]


def _px(v):
    return f"{'+' if v >= 0 else '-'} {abs(v):.2f}px"


def _vw(v):
    return f"{v * 100:.4f}vw"


def css():
    out = [f"/* {KENNUNG}: Beschriftungen folgen den gezeichneten Kaestchen (Lottie-Ebenen) bei 768-1511 px; ab 1512 px (feste Blockbreite) unveraendert */"]
    for lo, hi, xl, yl, pad4, pad5, yc in BEREICHE:
        out.append(f"@media (min-width:{lo}px) and (max-width:{hi}px) {{")
        for i, (cid, fx, fy, spalte) in enumerate(KARTEN):
            pad = pad5 if i == 4 else pad4
            if spalte == "links":
                left_vw, left_px = fx, -fx * pad + xl - 30
            else:  # rechte Spalte beginnt bei 30 px + 65 % von (Fensterbreite - 60 px)
                left_vw, left_px = fx - 0.65, -fx * pad + xl + 9
            top_vw, top_px = fy * A, -fy * A * pad + yl - yc
            out.append(f"  selector .elementor-element.elementor-element-{cid} {{ top: calc({_vw(top_vw)} {_px(top_px)}); --width: calc({_vw(FW)} {_px(-FW * pad)}); --min-height: calc({_vw(FH * A)} {_px(-FH * A * pad)}); }}")
            out.append(f"  body:not(.rtl) selector .elementor-element.elementor-element-{cid} {{ left: calc({_vw(left_vw)} {_px(left_px)}); }}")
        out.append("}")
    out.append(f"/* /{KENNUNG} */")
    return "\n".join(out)


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data):
    for e in walk(data["elements"]):
        if e.get("id") == BLOCK:
            s = e.setdefault("settings", {})
            alt = s.get("custom_css") or ""
            if KENNUNG in alt:
                return data, 0
            s["custom_css"] = alt.rstrip("\n") + "\n\n" + css() + "\n"
            return data, 1
    raise SystemExit(f"Block {BLOCK} nicht gefunden – falsche Seite?")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "css":
        print(css())
        sys.exit(0)
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
