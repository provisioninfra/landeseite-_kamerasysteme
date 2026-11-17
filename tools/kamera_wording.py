#!/usr/bin/env python3
"""Kamera-Seite (/kamerasysteme/, ID 4313): Wording „Kamera- & Videoüberwachung“ → „Kamera- & Videosicherheitssysteme“
(17.11.2026, Vorgabe des Kunden mit Bildschirmfoto des Heros).

Geändert werden nur die drei Überschriften, die die Wortverbindung tragen; die Grammatik folgt dem Satz
(nach „mit“ Dativ „…systemen“, als Objekt „…systeme“). Einzelne Nennungen von „Videoüberwachung“ in Fließtexten,
FAQ und Tagline bleiben, ebenso Yoast-Titel, Beschreibung und Strukturdaten (Suchbegriff).
Aufruf: python3 -I tools/kamera_wording.py export.json ziel.json [hero|seo]
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


# Strukturdaten-Widget (JSON-LD, Service): Google-Eintrag „Kamera- & Videosicherheit“ (Nachtrag 17.11.2026, Modus „seo“);
# Yoast-Titel, Beschreibung und WordPress-Seitentitel werden getrennt über den Editor gesetzt (Technik-Check).
SEO_ERSETZUNGEN = {
    "dca37dc": [
        ('"name": "Kamera- und Videoüberwachung für Unternehmen"', '"name": "Kamera- & Videosicherheit für Unternehmen"'),
        ('"description": "Kamera- & Videoüberwachung für Unternehmen zwischen Hamburg und Hannover',
         '"description": "Kamera- & Videosicherheit für Unternehmen zwischen Hamburg und Hannover'),
    ],
}


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data, modus="hero"):
    by = {e["id"]: e for e in walk(data["elements"])}
    if modus == "hero":
        for eid, (alt, neu) in ERSETZUNGEN.items():
            s = by[eid]["settings"]
            assert s.get("title", "").count(alt) == 1, (eid, "Text nicht genau einmal gefunden")
            s["title"] = s["title"].replace(alt, neu)
    elif modus == "seo":
        for eid, paare in SEO_ERSETZUNGEN.items():
            s = by[eid]["settings"]
            for alt, neu in paare:
                assert s.get("html", "").count(alt) == 1, (eid, alt[:40], "Text nicht genau einmal gefunden")
                s["html"] = s["html"].replace(alt, neu)
        # WordPress-Seitentitel steckt in den Seiteneinstellungen des Exports; sonst würde ein Elementor-Speichern den
        # über den Editor gesetzten Titel wieder überschreiben
        if data.get("settings", {}).get("post_title"):
            data["settings"]["post_title"] = "Kamera- & Videosicherheit"
    else:
        raise SystemExit("Modus hero oder seo")
    return data


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    modus = sys.argv[3] if len(sys.argv) > 3 else "hero"
    data = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")), modus)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Wording angepasst (Modus", modus + "):", ", ".join(ERSETZUNGEN if modus == "hero" else SEO_ERSETZUNGEN), "→", dst)
