#!/usr/bin/env python3
"""Lüneburg-Seite (4496) nach versehentlichem Überschreiben am 02.11.2026 wiederherstellen.

Die Parallelsitzung „Uelzen Unterseite“ hatte auf 4496 und 4605 einen letzten Container „Querformat + Hero-Video
(Steuerung)“ angelegt und die beiden Hero-Videos getauscht; mein Speicherlauf überschrieb 4496 mit einem älteren Export.
Dieses Skript überträgt aus einem frischen Export von 4605 (Vorlage) den Container und die Hintergrundvideo-Einstellungen
der gleich benannten Hero-Elemente (0f0c707, d135e80) in einen frischen Export von 4496.

Aufruf: python3 -I tools/lueneburg_wiederherstellen.py export-4496.json export-4605.json ziel.json
"""
import copy, json, pathlib, sys

ziel_src, vorlage_src, dst = sys.argv[1:4]
ziel = json.loads(pathlib.Path(ziel_src).read_text(encoding="utf-8"))
vorlage = json.loads(pathlib.Path(vorlage_src).read_text(encoding="utf-8"))

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def find(els, eid):
    return next((e for e in walk(els) if e["id"] == eid), None)

# 1) Container der Parallelsitzung (letzter Container mit „Querformat“ im Titel)
quelle = next((e for e in reversed(vorlage["elements"]) if e.get("elType") == "container" and "Querformat" in e.get("settings", {}).get("_title", "")), None)
assert quelle, "Container „Querformat …“ in der Vorlage nicht gefunden"
if find(ziel["elements"], quelle["id"]):
    print(f"Container {quelle['id']} bereits vorhanden")
else:
    ziel["elements"].append(copy.deepcopy(quelle))
    print(f"Container {quelle['id']} „{quelle['settings'].get('_title')}“ übernommen ({len(list(walk([quelle])))} Elemente)")

# 2) Hintergrundvideo-Einstellungen der Hero-Elemente
for eid in ("0f0c707", "d135e80"):
    v, z = find(vorlage["elements"], eid), find(ziel["elements"], eid)
    if not v or not z:
        print(f"{eid}: nicht in beiden Seiten vorhanden, übersprungen"); continue
    keys = [k for k in v["settings"] if k.startswith("background_video")]
    changed = [k for k in keys if z["settings"].get(k) != v["settings"][k]]
    for k in keys:
        z["settings"][k] = copy.deepcopy(v["settings"][k])
    print(f"{eid}: Videoeinstellungen übernommen, geändert: {changed} -> {str(z['settings'].get('background_video_link'))[-50:]}")

pathlib.Path(dst).write_text(json.dumps(ziel, ensure_ascii=False), encoding="utf-8")
print("geschrieben:", dst)
