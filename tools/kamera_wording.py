#!/usr/bin/env python3
"""Kamera-Seite (/kamerasysteme/, ID 4313): Wording „Kamera- & Videoüberwachung“ → „Kamera- & Videosicherheitssysteme“
(17.11.2026, Vorgabe des Kunden mit Bildschirmfoto des Heros).

Geändert werden nur die drei Überschriften, die die Wortverbindung tragen; die Grammatik folgt dem Satz
(nach „mit“ Dativ „…systemen“, als Objekt „…systeme“). Einzelne Nennungen von „Videoüberwachung“ in Fließtexten,
FAQ und Tagline bleiben, ebenso Yoast-Titel, Beschreibung und Strukturdaten (Suchbegriff).
Aufruf: python3 -I tools/kamera_wording.py export.json ziel.json
"""
import json, pathlib, sys

ERSETZUNGEN = {
    # Hero-Überschrift (H1)
    "9dcea29": ("mit Kamera- &amp; Videoüberwachung", "mit Kamera- &amp; Videosicherheitssystemen"),
    # Hero-Unterzeile, zweiter (fetter) Absatz
    "e429076": ("plant und installiert Kamera- und Videoüberwachung für Unternehmen:",
                "plant und installiert Kamera- &amp; Videosicherheitssysteme für Unternehmen:"),
    # Überschrift des Leistungsabschnitts
    "d673c65": ("Mit Kamera- und Videoüberwachung von ProVision Infra",
                "Mit Kamera- &amp; Videosicherheitssystemen von ProVision Infra"),
}


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data):
    by = {e["id"]: e for e in walk(data["elements"])}
    for eid, (alt, neu) in ERSETZUNGEN.items():
        s = by[eid]["settings"]
        assert s.get("title", "").count(alt) == 1, (eid, "Text nicht genau einmal gefunden")
        s["title"] = s["title"].replace(alt, neu)
    return data


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Wording angepasst:", ", ".join(ERSETZUNGEN), "→", dst)
