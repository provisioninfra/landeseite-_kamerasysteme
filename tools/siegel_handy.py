#!/usr/bin/env python3
"""Schwebendes ProvenExpert-Siegel auch auf dem Handy zeigen (02.11.2026, Wunsch des Kunden).

Das HTML-Widget mit dem feststehenden Siegel (unten rechts, Elementor „feste Positionierung“) hat auf Start-, Kamera- und
Stadtseiten die Einstellung „auf Handy ausblenden“, obwohl es eigene Handy-Werte besitzt (Abstand 5 px, Bild 80 px). Der
Kunde will das Siegel auf dem Smartphone sehen, unten rechts mitlaufend. Dieses Skript entfernt nur die Ausblendung.

Aufruf: python3 -I tools/siegel_handy.py quelle.json ziel.json
"""
import json, pathlib, sys

src, dst = sys.argv[1:3]
data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

n = 0
for e in walk(data["elements"]):
    s = e.get("settings", {})
    if e.get("widgetType") == "html" and "pe-badge-fixed" in s.get("html", "") and s.get("_position") == "fixed" and s.get("hide_mobile"):
        del s["hide_mobile"]; n += 1
        print(f"Siegel-Widget {e['id']}: Handy-Ausblendung entfernt")
pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
print(f"{n} Widget(s) geändert")
