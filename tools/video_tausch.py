#!/usr/bin/env python3
"""Große Hero-Hintergrundvideos gegen kompakte Fassungen tauschen (17.11.2026, SEO-Check Stufe A7, Hinweis der
Parallelsitzung: /zutrittssystem/ lud mobil 9,9 MB Video, LCP 16 s).

Die Originale (3840×2160 mit Ton, 6,2 MB; 2026×2160, 3,7 MB; 2880×2880, 15 MB) wurden mit ffmpeg ohne Tonspur auf
1920×1080, 1014×1080 und 1080×1080 (H.264, CRF siehe Technik-Check, faststart) umgerechnet und in die Mediathek
geladen. Das Werkzeug ersetzt nur die URL in `background_video_link` (auch den Verweis auf den alten Entwicklungs-
Host); alles andere bleibt.
Aufruf: python3 -I tools/video_tausch.py export.json ziel.json   (Ausgabe: Zahl der Ersetzungen)
"""
import json, pathlib, sys

NEU = "https://provision-infra.de/wp-content/uploads/2026/11/"
TAUSCH = {
    "https://provision-infra.de/wp-content/uploads/2026/08/Untitled-design.mp4": NEU + "zutritt-hero-desktop-1920.mp4",
    "https://provision-infra.de/wp-content/uploads/2026/08/Untitled-design-1.mp4": NEU + "zutritt-hero-handy-1080.mp4",
    "https://provision-infra.de/wp-content/uploads/2026/05/Main-Banner-Video-6.mp4": NEU + "banner-video-handy-1080.mp4",
    "https://dev-ls-de-532018.hostingersite.com/wp-content/uploads/2026/05/Main-Banner-Video-6.mp4": NEU + "banner-video-handy-1080.mp4",
}


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data):
    n = 0
    for e in walk(data["elements"]):
        s = e.get("settings", {})
        v = s.get("background_video_link")
        if isinstance(v, str) and v in TAUSCH:
            s["background_video_link"] = TAUSCH[v]
            n += 1
    return data, n


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
