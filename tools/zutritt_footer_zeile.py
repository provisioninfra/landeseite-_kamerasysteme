#!/usr/bin/env python3
"""Zutrittssystem-Seite (ID 3316), 18.11.2026: Die Footer-Zeile mit ProvenExpert-Bewertung und Social-Icons
(Container 6ad6b91) hat eine feste Breite von 1400 px. Auf Laptops bis 1440 px, Tablets und Handys im Querformat ragt
sie deshalb links und rechts aus dem Bildschirm – die Bewertungszeile war angeschnitten („xpert.com“), die Icons
unsichtbar. Lösung ohne Strukturänderung: ab dem Elementor-Breakpoint „Laptop“ (max. 1440 px) Breite 100 %; am
Desktop (ab 1441 px) bleibt alles wie bisher, Handy hochkant war schon korrekt (Elementor setzt dort 100 %).
Aufruf: python3 -I tools/zutritt_footer_zeile.py export.json ziel.json   (Ausgabe: Zahl der Änderungen)
"""
import json, pathlib, sys

CONTAINER = "6ad6b91"
BREITE_LAPTOP = {"unit": "%", "size": 100, "sizes": []}


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data):
    for e in walk(data["elements"]):
        if e.get("id") == CONTAINER:
            s = e.setdefault("settings", {})
            if s.get("width_laptop") == BREITE_LAPTOP:
                return data, 0
            s["width_laptop"] = dict(BREITE_LAPTOP)
            return data, 1
    raise SystemExit(f"Container {CONTAINER} nicht gefunden – falsche Seite?")


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
