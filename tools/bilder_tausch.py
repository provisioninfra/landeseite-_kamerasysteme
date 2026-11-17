#!/usr/bin/env python3
"""Große Hintergrund-PNGs gegen verkleinerte Versionen tauschen (17.11.2026, SEO-Check Stufe A7).

Sechs dekorative Hintergrundbilder (Verläufe, Ellipsen, Rahmen) lagen als PNG mit zusammen 1,9 MB in Elementor-
Hintergrund- und Overlay-Einstellungen vieler Seiten. Die Ersatzdateien (gleiche Motive, 1.200 px bzw. 1.083 px breit,
WebP oder 8-Bit-PNG, zusammen 0,8 MB) liegen in der Mediathek; optischer Vergleich der Abschnitte: mittlere Abweichung
unter 3/255. Das Werkzeug ersetzt nur URL und Mediathek-ID in `background_image`, `background_overlay_image` (und
weiteren Bildfeldern mit derselben URL) sowie die URL in `custom_css`; alles andere bleibt.
Aufruf: python3 -I tools/bilder_tausch.py export.json ziel.json   (Ausgabe: Zahl der Ersetzungen; 0 = Seite nicht betroffen)
"""
import json, pathlib, sys

UPLOADS = "https://provision-infra.de/wp-content/uploads/"
TAUSCH = {  # alte URL: (neue URL, neue Mediathek-ID)
    UPLOADS + "2026/05/Untitled-design-1.png": (UPLOADS + "2026/11/hintergrund-verlauf-1200.webp", 5066),
    UPLOADS + "2026/05/Frame-2147224855.png": (UPLOADS + "2026/11/hintergrund-rahmen-802.webp", 5067),
    UPLOADS + "2026/05/Ellipse-3.png": (UPLOADS + "2026/11/hintergrund-ellipse-3-1200.webp", 5068),
    UPLOADS + "2026/05/Ellipse-4.png": (UPLOADS + "2026/11/hintergrund-ellipse-4-1083.png", 5069),
    UPLOADS + "2026/06/1.png": (UPLOADS + "2026/11/hintergrund-overlay-1-1083.png", 5070),
    UPLOADS + "2026/06/2.png": (UPLOADS + "2026/11/hintergrund-overlay-2-1083.png", 5071),
    # Zutrittssystem-Seite (3316): eigene Kopien der Hintergründe von Juli und ein 2,2-MB-Handybild
    UPLOADS + "2026/07/Ellipse-3.png": (UPLOADS + "2026/11/hintergrund-ellipse-3-1200.webp", 5068),
    UPLOADS + "2026/07/Frame-2147224855.png": (UPLOADS + "2026/11/hintergrund-rahmen-802.webp", 5067),
    UPLOADS + "2026/08/Untitled-design-3.png": (UPLOADS + "2026/11/zutritt-handy-bild-1378.webp", 5105),
}


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
    return data, n


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
