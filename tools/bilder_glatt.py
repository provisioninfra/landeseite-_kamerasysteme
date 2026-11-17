#!/usr/bin/env python3
"""Zweite Runde Hintergrundbilder (17.11.2026, nach Kundenhinweis auf harte Farbstufen).

Die erste Runde (`bilder_tausch.py`) hatte verkleinerte, verlustbehaftete Dateien gesetzt; dazu hatte Imagify die
Uploads nochmals komprimiert. Ergebnis: sichtbare Ringe und getönte Rechtecke. Ersatz aus den unberührten Original-
dateien (Imagify-Sicherung unter uploads/backup):
- vier Leuchtflächen: Alphakanal mit Gauß-Filter geglättet (141 statt 14 Stufen), Farbe und Ausdehnung unverändert,
  verlustfreies WebP, 45–85 KB;
- V-Rahmen verlustfrei (112 KB), Gründerfoto mit Rahmen WebP q95 (247 KB), Handybild WebP q96 (213 KB);
- Zutrittssystem-Hero-Video für große Bildschirme 2560×1440 (CRF 21, 1,3 MB) statt 1920×1080.
Das Werkzeug ersetzt nur URL und Mediathek-ID in Bildfeldern mit passender URL, URLs in `custom_css` und den
Videoverweis in `background_video_link`; alles andere bleibt. Hochgeladen mit ausgeschalteter Imagify-Automatik.
Aufruf: python3 -I tools/bilder_glatt.py export.json ziel.json   (Ausgabe: Zahl der Ersetzungen)
"""
import json, pathlib, sys

UP = "https://provision-infra.de/wp-content/uploads/2026/11/"
TAUSCH = {  # alte URL: (neue URL, neue Mediathek-ID)
    UP + "hintergrund-ellipse-3-1200.webp": (UP + "hintergrund-ellipse-3-glatt.webp", 5180),
    UP + "hintergrund-ellipse-4-1083.png": (UP + "hintergrund-ellipse-4-glatt.webp", 5181),
    UP + "hintergrund-overlay-1-1083.png": (UP + "hintergrund-overlay-1-glatt.webp", 5182),
    UP + "hintergrund-overlay-2-1083.png": (UP + "hintergrund-overlay-2-glatt.webp", 5183),
    UP + "hintergrund-rahmen-802.webp": (UP + "hintergrund-rahmen-urfassung.webp", 5184),
    UP + "hintergrund-verlauf-1200.webp": (UP + "hintergrund-verlauf-q95.webp", 5185),
    UP + "zutritt-handy-bild-1378.webp": (UP + "zutritt-handy-bild-q96.webp", 5186),
}
VIDEO = {UP + "zutritt-hero-desktop-1920.mp4": UP + "zutritt-hero-desktop-2560.mp4"}


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data):
    n = 0
    for e in walk(data["elements"]):
        s = e.get("settings", {})
        for k, v in list(s.items()):
            if isinstance(v, dict) and v.get("url") in TAUSCH:
                neu_url, neu_id = TAUSCH[v["url"]]
                v["url"] = neu_url
                if "id" in v:
                    v["id"] = neu_id
                n += 1
            elif isinstance(v, str) and k == "custom_css":
                for alt, (neu_url, _) in TAUSCH.items():
                    if alt in v:
                        s[k] = v = v.replace(alt, neu_url)
                        n += 1
            elif isinstance(v, str) and k == "background_video_link" and v in VIDEO:
                s[k] = VIDEO[v]
                n += 1
    return data, n


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
