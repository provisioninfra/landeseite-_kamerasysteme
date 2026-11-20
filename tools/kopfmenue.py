#!/usr/bin/env python3
"""Einheitliches Kopfmenü auf allen Seiten (Kundenauftrag 20.11.2026, Screenshot des Handy-Menüs der neuen Seiten).

Drei Eingriffe, je nach Seite:
1. `nav_setzen(data, menu_slug)` – Seiten mit der Pillen-Kopfzeile (Container 192a273 bzw. 20a7a089): im Nav-Menü-Widget
   der Kopfzeile das Feld `menu` auf das Zielmenü setzen, das Element-CSS einheitlich auf `handy_css_einheitlich`
   stellen und die Maße angleichen (Punktabstand 20 px, Pillenrand 60 px).
2. `karriere_kopf(data, vorlage)` – Karriere-Seite (HTML-Widget mit eigener Kopfzeile): die Pillen-Kopfzeile aus einer
   Vorlagenseite als ersten Abschnitt einfügen (Menü „menue-karriere“), die HTML-Kopfzeile `.pk-header` per CSS ausblenden.
3. `rechtliches_kopf(data, vorlage)` – (nicht verwendet: Kunde will auf Impressum, Datenschutz, AGB nur das Logo lassen)
   im Balken das Logo durch die Pillen-Zeile (Logo + Menü „menue-rechtliches“) ersetzen, Balkenbreite 1400 px wie die Kopfzeile der übrigen Seiten.

Aufruf: python3 -I tools/kopfmenue.py MODUS export.json ziel.json [vorlage.json]   (MODUS: nav:<slug> | karriere | rechtliches)
Ausgabe: Zahl der Änderungen.
"""
import copy, json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from menue_handy import handy_css_einheitlich  # noqa: E402

KOPF_IDS = ("192a273", "20a7a089")
PILLE_IDS = ("f07a3e3", "5391d65")   # Zeile mit Logo und Menü (Startseiten-Vorlage bzw. Zutrittssystem)
ABSTAND = {"unit": "px", "size": 20, "sizes": []}   # Menüpunkt-Abstand am Bildschirm (vorher 30 px; 7 Punkte brauchen Platz)
PILLEN_RAND = "60"                                   # Innenabstand der Pille links/rechts (vorher 80 px)
KARRIERE_CSS = ("/* pv-menue: eigene HTML-Kopfzeile der Karriere-Seite ausgeblendet, Pillen-Kopfzeile wie auf allen Seiten (tools/kopfmenue.py) */\n"
                ".pk-header { display: none !important; }")


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def kopf_container(data):
    for e in data["elements"]:
        if e.get("id") in KOPF_IDS:
            return e
    return None


def nav_widget(container):
    for e in walk([container]):
        if e.get("widgetType") == "nav-menu":
            return e
    return None


def kopf_angleichen(kopf):
    """Einheitliche Maße: Menüpunkt-Abstand 20 px, Pillen-Innenabstand 60 px links/rechts (sonst bricht das Menü mit
    sieben Punkten ab 1441 px Fensterbreite in zwei Zeilen um). Gibt die Zahl der Änderungen zurück."""
    n = 0
    nav = nav_widget(kopf)
    if nav["settings"].get("menu_space_between") != ABSTAND:
        nav["settings"]["menu_space_between"] = dict(ABSTAND)
        n += 1
    for e in walk([kopf]):
        if e.get("id") in PILLE_IDS:
            pad = dict(e["settings"].get("padding") or {"unit": "px", "top": "16", "bottom": "16", "isLinked": False})
            if pad.get("left") != PILLEN_RAND or pad.get("right") != PILLEN_RAND:
                pad.update({"left": PILLEN_RAND, "right": PILLEN_RAND, "isLinked": False})
                e["settings"]["padding"] = pad
                n += 1
    return n


def nav_setzen(data, menu_slug):
    kopf = kopf_container(data)
    if kopf is None:
        raise SystemExit("keine Pillen-Kopfzeile (192a273/20a7a089) gefunden")
    nav = nav_widget(kopf)
    if nav is None:
        raise SystemExit("kein Nav-Menü-Widget in der Kopfzeile")
    s = nav["settings"]
    css = handy_css_einheitlich(s)
    n = 0
    if s.get("menu") != menu_slug:
        s["menu"] = menu_slug
        n += 1
    if (s.get("custom_css") or "") != css:
        s["custom_css"] = css
        n += 1
    n += kopf_angleichen(kopf)
    return data, n


def kopf_vorlage(vorlage, menu_slug):
    """Kopie der Pillen-Kopfzeile 192a273 einer Vorlagenseite mit gesetztem Menü und einheitlichem CSS."""
    kopf = copy.deepcopy(kopf_container(vorlage))
    if kopf is None:
        raise SystemExit("Vorlage ohne Kopfzeile 192a273")
    nav = nav_widget(kopf)
    nav["settings"]["menu"] = menu_slug
    nav["settings"]["custom_css"] = handy_css_einheitlich(nav["settings"])
    kopf_angleichen(kopf)
    return kopf


def karriere_kopf(data, vorlage):
    if kopf_container(data) is not None:
        return data, 0
    kopf = kopf_vorlage(vorlage, "menue-karriere")
    kopf["settings"]["custom_css"] = (kopf["settings"].get("custom_css") or "").rstrip("\n") + ("\n\n" if kopf["settings"].get("custom_css") else "") + KARRIERE_CSS
    data["elements"].insert(0, kopf)
    return data, 1


def rechtliches_kopf(data, vorlage):
    balken = data["elements"][0]
    if any(e.get("widgetType") == "nav-menu" for e in walk([balken])):
        return data, 0
    logos = [e for e in balken.get("elements", []) if e.get("widgetType") == "image"]
    if len(balken.get("elements", [])) != 1 or len(logos) != 1:
        raise SystemExit(f"unerwarteter Kopfbalken {balken.get('id')}: {[e.get('widgetType') or e.get('elType') for e in balken.get('elements', [])]}")
    kopf = kopf_vorlage(vorlage, "menue-rechtliches")
    pille = kopf["elements"][0]            # f07a3e3: Zeile mit Logo und Menü
    balken["elements"] = [pille]
    balken["settings"]["boxed_width"] = {"unit": "px", "size": 1400, "sizes": []}
    return data, 1


if __name__ == "__main__":
    modus, src, dst = sys.argv[1:4]
    data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    if modus.startswith("nav:"):
        data, n = nav_setzen(data, modus[4:])
    else:
        vorlage = json.loads(pathlib.Path(sys.argv[4]).read_text(encoding="utf-8"))
        data, n = karriere_kopf(data, vorlage) if modus == "karriere" else rechtliches_kopf(data, vorlage)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
