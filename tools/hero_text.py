#!/usr/bin/env python3
"""Hero der Startseite und der Kamera-Seite (07.11.2026, Rückmeldung des Kunden am Handy):
  1. Etwas mehr Abstand zwischen Überschrift und Unterzeile am Handy (Überschrift 9dcea29: Innenabstand unten
     mobil 10 → 18 px; alle anderen Geräteklassen unverändert: Tablet 20, Laptop 15, Computer 35 px).
  2. Zweiter Absatz der Unterzeile (Widget e429076, Text nach dem doppelten Zeilenumbruch) leicht gekürzt und fett
     (span mit font-weight 700, dieselbe Technik wie im fetten Teil der Überschrift).
Beide Seiten tragen dieselben Element-IDs (die Kamera-Seite ist eine Kopie der Startseite), nur der Absatztext
unterscheidet sich; er steht je Seiten-ID in TEXTE.
Aufruf: python3 -I tools/hero_text.py export.json ziel.json [Seiten-ID, Vorgabe 31]
"""
import json, pathlib, sys

TEXTE = {
    # Startseite (/): digitales Zutrittssystem
    31: (
        "ProVision Infra plant &amp; installiert in Norddeutschland dein digitales Zutrittssystem, mit dem du Zugänge per "
        "Chip, KeyCard oder App in Sekunden vergibst und entziehst – und so Zeit und Aufwand im Alltag sparst.",
        '<span style="font-weight: 700;">ProVision Infra plant &amp; installiert in Norddeutschland dein digitales '
        'Zutrittssystem: Zugänge per Chip, KeyCard oder App in Sekunden vergeben und entziehen – das spart dir Zeit und '
        'Aufwand im Alltag.</span>',
    ),
    # Kamera-Seite (/kamerasysteme/): Kamera- und Videoüberwachung (33 → 28 Wörter, Aussage unverändert)
    4313: (
        "ProVision Infra plant und installiert Kamera- und Videoüberwachung für Unternehmen. Du siehst jederzeit per App, "
        "was auf deinem Gelände passiert, und hast im Ernstfall Aufnahmen, die etwas beweisen.",
        '<span style="font-weight: 700;">ProVision Infra plant und installiert Kamera- und Videoüberwachung für '
        'Unternehmen: Du siehst per App jederzeit, was auf deinem Gelände passiert – und hast im Ernstfall Aufnahmen, '
        'die etwas beweisen.</span>',
    ),
}

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def anwenden(data, seite=31):
    alt, neu = TEXTE[int(seite)]
    by = {e["id"]: e for e in walk(data["elements"])}
    h1 = by["9dcea29"]["settings"]; pad = h1["_padding_mobile"]
    assert pad.get("bottom") in ("10", 10), pad
    pad["bottom"] = "18"
    sub = by["e429076"]["settings"]
    assert sub["title"].count(alt) == 1, "Absatztext nicht gefunden"
    sub["title"] = sub["title"].replace(alt, neu)
    return data

if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    seite = sys.argv[3] if len(sys.argv) > 3 else 31
    data = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")), seite)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Hero angepasst:", dst)
