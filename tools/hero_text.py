#!/usr/bin/env python3
"""Startseiten-Hero (07.11.2026, Rückmeldung des Kunden am Handy):
  1. Etwas mehr Abstand zwischen Überschrift und Unterzeile am Handy (Überschrift 9dcea29: Innenabstand unten
     mobil 10 → 18 px; alle anderen Geräteklassen unverändert: Tablet 20, Laptop 15, Computer 35 px).
  2. Zweiter Absatz der Unterzeile (Widget e429076, Text nach dem doppelten Zeilenumbruch) leicht gekürzt und fett
     (span mit font-weight 700, dieselbe Technik wie im fetten Teil der Überschrift).
Aufruf: python3 -I tools/hero_text.py export.json ziel.json
"""
import json, pathlib, sys

ALT = ("ProVision Infra plant &amp; installiert in Norddeutschland dein digitales Zutrittssystem, mit dem du Zugänge per "
       "Chip, KeyCard oder App in Sekunden vergibst und entziehst – und so Zeit und Aufwand im Alltag sparst.")
NEU = ('<span style="font-weight: 700;">ProVision Infra plant &amp; installiert in Norddeutschland dein digitales '
       'Zutrittssystem: Zugänge per Chip, KeyCard oder App in Sekunden vergeben und entziehen – das spart dir Zeit und '
       'Aufwand im Alltag.</span>')

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def anwenden(data):
    by = {e["id"]: e for e in walk(data["elements"])}
    h1 = by["9dcea29"]["settings"]; pad = h1["_padding_mobile"]
    assert pad.get("bottom") in ("10", 10), pad
    pad["bottom"] = "18"
    sub = by["e429076"]["settings"]
    assert sub["title"].count(ALT) == 1, "Absatztext nicht gefunden"
    sub["title"] = sub["title"].replace(ALT, NEU)
    return data

if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Hero angepasst:", dst)
