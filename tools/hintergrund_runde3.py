#!/usr/bin/env python3
"""Dritte Runde Hintergründe (17./18.11.2026): alle noch quantisierten Bilddateien gegen Fassungen aus den unberührten
Originalen tauschen und abgeschnittene Leuchtflächen an Abschnittsrändern weich auslaufen lassen.

1. Dateitausch (URL und Mediathek-ID in Bildfeldern, URLs in allen Textfeldern wie `custom_css` und `html`):
   Leuchtflächen → geglättete Fassungen (auch die Kopien der Karriere-Seite), Hero-Hintergrund, Kopffoto, Fotos,
   Kamerabilder und Karte → WebP aus den Imagify-Sicherungen (q88–q95, Alpha verlustfrei).
2. Weiche Ränder: Bei Leuchtflächen, die als Overlay (::before) mit fester Größe über den Abschnittsrand hinausragen
   (Messung mit scratchpad seo/cuts.mjs), wird per Element-CSS eine Maske gesetzt, die das Overlay zum oberen bzw.
   unteren Rand hin ausblendet. Nur `custom_css` des Elements wird ergänzt (Kennung `pv-weich`), alles andere bleibt.
3. Footer-Block ausrichten: Der Block „Leistungen/Standorte“ (a1f0071) lag als Vollbreiten-Container im 98 %-Footer,
   der übrige Footer-Inhalt ist auf 1400 px zentriert. Der Block wird zum Container mit Inhaltsbreite „boxed“
   (1400 px); Rahmenlinie und Innenabstand wandern in einen neuen inneren Container a1f0074, der die beiden Listen
   aufnimmt. So liegen Linie und Listen auf allen Breiten bündig mit Copyright-Zeile und Logo.
Aufruf: python3 -I tools/hintergrund_runde3.py export.json ziel.json   (Ausgabe: Zahl der Änderungen)
"""
import json, pathlib, re, sys

UP = "https://provision-infra.de/wp-content/uploads/"
N = UP + "2026/11/"
TAUSCH = {  # alte URL: (neue URL, neue Mediathek-ID)
    # Runde 2 (wiederholbar)
    N + "hintergrund-ellipse-3-1200.webp": (N + "hintergrund-ellipse-3-glatt.webp", 5180),
    N + "hintergrund-ellipse-4-1083.png": (N + "hintergrund-ellipse-4-glatt.webp", 5181),
    N + "hintergrund-overlay-1-1083.png": (N + "hintergrund-overlay-1-glatt.webp", 5182),
    N + "hintergrund-overlay-2-1083.png": (N + "hintergrund-overlay-2-glatt.webp", 5183),
    N + "hintergrund-rahmen-802.webp": (N + "hintergrund-rahmen-urfassung.webp", 5184),
    N + "hintergrund-verlauf-1200.webp": (N + "hintergrund-verlauf-q95.webp", 5185),
    N + "zutritt-handy-bild-1378.webp": (N + "zutritt-handy-bild-q96.webp", 5186),
    # Karriere-Seite: Kopien derselben Leuchtflächen (im HTML-Widget)
    UP + "2026/10/glow-ellipse-3-1.png": (N + "hintergrund-ellipse-3-glatt.webp", 5180),
    UP + "2026/10/glow-ellipse-4-1.png": (N + "hintergrund-ellipse-4-glatt.webp", 5181),
    UP + "2026/10/glow-left-1.png": (N + "hintergrund-overlay-1-glatt.webp", 5182),
    UP + "2026/10/glow-right-1.png": (N + "hintergrund-overlay-2-glatt.webp", 5183),
    UP + "2026/10/glow-frame.png": (N + "hintergrund-rahmen-urfassung.webp", 5184),
    UP + "2026/10/glow-ellipse-5-1.png": (N + "hintergrund-ellipse-5-glatt.webp", 5198),
    # weitere quantisierte Dateien (IDs nach Upload eintragen)
    UP + "2026/05/Ellipse-5.png": (N + "hintergrund-ellipse-5-glatt.webp", 5198),
    UP + "2026/05/Untitled-design-13.png": (N + "hintergrund-haze-2554-q95.webp", 5199),
    UP + "2026/07/Untitled-design-13.png": (N + "hintergrund-haze-2554-q95.webp", 5199),
    UP + "2026/05/provision_header_02-1.png": (N + "header-foto-1305-q92.webp", 5202),
    UP + "2026/05/Untitled-design-12.png": (N + "tuergriff-1875-q90.webp", 5205),
    UP + "2026/05/Untitled-design-14.png": (N + "foto-serverraum-2400-q88.webp", 5206),
    UP + "2026/05/Untitled-design-15.png": (N + "foto-gruender-tuer-2400-q88.webp", 5209),
    UP + "2026/08/Mask-group-7-2.png": (N + "foto-gruender-laptop-2400-q90.webp", 5212),
    UP + "2026/10/kamera-1.png": (N + "kamera-1-1600-q90.webp", None),
    UP + "2026/10/kamera-2.png": (N + "kamera-2-1600-q90.webp", None),
    UP + "2026/10/kamera-3.png": (N + "kamera-3-1600-q90.webp", None),
    UP + "2026/10/kamera-4.png": (N + "kamera-4-1600-q90.webp", None),
    UP + "2026/10/kamera-5.png": (N + "kamera-5-1600-q90.webp", None),
    UP + "2026/05/Germany.png": (N + "karte-deutschland-558-q95.webp", None),
}
VIDEO = {N + "zutritt-hero-desktop-1920.mp4": N + "zutritt-hero-desktop-2560.mp4"}

# Weiche Ränder: Element-ID -> Kanten, die ausgeblendet werden (aus der Messung); Prozentwerte beziehen sich auf die Höhe
MASKEN = {
    "55b8573": "unten",   # Regions-Abschnitt mit Karte: Ellipse-4-Overlay (40 % Breite, −25 px) ragt unten heraus (bis 15 Stufen)
    "9a7495a": "unten",   # dito Zutrittssystem-Seite
    "ddbba36": "beide",   # Footer-Box der Inhaltsseiten: Ellipse-3-Overlay (94 % Breite, −472/−6xx px) oben und unten abgeschnitten
    "772b72df": "beide",  # Footer-Box Zutrittssystem
    "67f4447": "beide",   # Footer-Box Impressum
    "3a939b6": "beide",   # Footer-Box Datenschutz
    "ebac46e": "beide",   # Footer-Box AGB
}
MASKE_CSS = {
    "oben": "linear-gradient(to bottom,transparent 0,#000 18%,#000 100%)",
    "unten": "linear-gradient(to bottom,#000 0,#000 82%,transparent 100%)",
    "beide": "linear-gradient(to bottom,transparent 0,#000 18%,#000 82%,transparent 100%)",
}


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def footer_ausrichten(data):
    """a1f0071 auf Inhaltsbreite boxed 1400 setzen; Linie/Abstand in neuen inneren Container a1f0074 mit den Listen."""
    for e in walk(data["elements"]):
        if e.get("id") != "a1f0071":
            continue
        kinder = e.get("elements", [])
        if any(k.get("id") == "a1f0074" for k in kinder):
            return 0  # schon umgebaut
        s = e.setdefault("settings", {})
        innen = {
            "id": "a1f0074", "elType": "container", "isInner": True, "elements": kinder,
            "settings": {
                "content_width": "full", "flex_direction": "column", "_title": "Footer: Leistungen und Standorte (innen)",
                "border_border": s.get("border_border", "solid"), "border_width": s.get("border_width"), "border_color": s.get("border_color"),
                "padding": s.get("padding"),
            },
        }
        innen["settings"] = {k: v for k, v in innen["settings"].items() if v is not None}
        e["elements"] = [innen]
        s["content_width"] = "boxed"
        s["boxed_width"] = {"unit": "px", "size": 1400, "sizes": []}
        for k in ("border_border", "border_width", "border_color", "padding"):
            s.pop(k, None)
        return 1
    return 0


def anwenden(data):
    fehlend = [alt for alt, (_, i) in TAUSCH.items() if i is None]
    assert not fehlend, f"Mediathek-IDs fehlen für {len(fehlend)} Einträge"
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
            elif isinstance(v, str) and k == "background_video_link" and v in VIDEO:
                s[k] = VIDEO[v]
                n += 1
            elif isinstance(v, str) and "wp-content/uploads/" in v:
                neu = v
                for alt, (neu_url, _) in TAUSCH.items():
                    neu = neu.replace(alt, neu_url)
                if neu != v:
                    s[k] = neu
                    n += 1
        kante = MASKEN.get(e.get("id"))
        if kante:
            css = s.get("custom_css") or ""
            if "pv-weich" not in css:
                g = MASKE_CSS[kante]
                s["custom_css"] = (css.rstrip() + "\n" if css.strip() else "") + f"/* pv-weich */ selector::before{{-webkit-mask-image:{g};mask-image:{g};}}"
                n += 1
    n += footer_ausrichten(data)
    return data, n


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
