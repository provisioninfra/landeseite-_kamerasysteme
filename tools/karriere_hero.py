#!/usr/bin/env python3
"""Karriere-Seite (ID 4408, eine HTML-Widget-Seite), 07.11.2026, gleiches Prinzip wie der Startseiten-Hero:
  1. Handy: etwas mehr Abstand unter der Überschrift (Innenabstand unten 18 → 26 px; Tablet, Computer und das
     Handy-Querformat mit seiner eigenen Regel bleiben unverändert).
  2. Zweiter Absatz der Unterzeile leicht gekürzt („Bei uns bekommst du“ → „Du bekommst“) und fett (strong mit
     eigener Regel, font-weight 700, wie der fette Teil der Überschrift).
Aufruf: python3 -I tools/karriere_hero.py export.json ziel.json
"""
import json, pathlib, sys

ERSETZUNGEN = [
    ("#pk-karriere .hero__title{font-size:22px;line-height:28px;text-align:center;padding-bottom:18px;max-width:100%;}",
     "#pk-karriere .hero__title{font-size:22px;line-height:28px;text-align:center;padding-bottom:26px;max-width:100%;}"),
    ("<p>Elektrohandwerk, IT, Vertrieb oder Büro: Bei uns bekommst du früh eigene Aufgaben und siehst abends, was du geschafft hast.</p>",
     "<p><strong>Elektrohandwerk, IT, Vertrieb oder Büro: Du bekommst früh eigene Aufgaben und siehst abends, was du geschafft hast.</strong></p>"),
    ("#pk-karriere .hero__title b{font-weight:700;}",
     "#pk-karriere .hero__title b{font-weight:700;}#pk-karriere .hero__sub strong{font-weight:700;}"),
]

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def anwenden(data):
    w = next(e for e in walk(data["elements"]) if e.get("widgetType") == "html" and "hero__title" in e["settings"].get("html", ""))
    html = w["settings"]["html"]
    for alt, neu in ERSETZUNGEN:
        assert html.count(alt) == 1, alt[:60]
        html = html.replace(alt, neu)
    w["settings"]["html"] = html
    return data

if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Karriere-Hero angepasst:", dst)
