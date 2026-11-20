#!/usr/bin/env python3
"""Footer-Menüzeile wie auf der Startseite (Kundenentscheidung 20.11.2026): Die beiden Footer-Nav-Widgets (Bildschirm
waagerecht, Handy senkrecht) zeigen dasselbe WordPress-Menü wie die Kopfzeile der Seite – mit den Gruppen „Schließanlagen“
und „Videoüberwachung“ (am Bildschirm Aufklappen, auf dem Handy flach durch das Steuerungs-Widget „Handy-Darstellung“).

`footer_setzen(data, menu_slug)`: Feld `menu` der Footer-Nav-Widgets (59b27e3/a430424, auf Zutrittssystem
333801ae/3dcb5ac1) auf das Menü der Kopfzeile setzen.
`handy_widget_ergaenzen(data, seiten_id)`: Auf Seiten ohne das Steuerungs-Widget „Handy-Darstellung“ (die 13 Ortsseiten-
Kopien 4735–4783 hatten es nie) das Widget aus `tools/handy_darstellung.py` (ID-Tabelle der Lüneburg-Seite, gleiche
Element-IDs) in den Steuerungs-Container 09632f6 einfügen – damit auch dort das Footer-Menü auf dem Handy flach ist.

Aufruf: python3 -I tools/footer_menue.py <menu_slug> export.json ziel.json   (Ausgabe: Zahl der Änderungen)
"""
import json, pathlib, sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import handy_darstellung as hd  # noqa: E402

FOOTER_NAVS = ("59b27e3", "a430424", "333801ae", "3dcb5ac1")
STEUERUNG = "09632f6"
HANDY_KENNUNG = "pv-handy-darstellung"
VORLAGE_IDS = 4496   # Ortsseiten-Kopien tragen die Element-IDs der Lüneburg-Seite


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def footer_setzen(data, menu_slug):
    n = 0
    for e in walk(data["elements"]):
        if e.get("widgetType") == "nav-menu" and e["id"] in FOOTER_NAVS and e["settings"].get("menu") != menu_slug:
            e["settings"]["menu"] = menu_slug
            n += 1
    return n


def handy_widget_ergaenzen(data):
    if any(e.get("widgetType") == "html" and HANDY_KENNUNG in (e["settings"].get("html") or "") for e in walk(data["elements"])):
        return 0
    steuerung = next((e for e in data["elements"] if e.get("id") == STEUERUNG), None)
    if steuerung is None:
        raise SystemExit(f"Steuerungs-Container {STEUERUNG} fehlt – Seite hat eine andere Struktur")
    vorhanden = {e["id"] for e in walk(data["elements"])}
    ids = hd.SEITEN[VORLAGE_IDS]
    for key, val in ids.items():
        pruef = val if key == "footer_nav" else ([x for t in val for x in t] if key == "video_rows" else [val] if isinstance(val, str) and len(val) == 7 else [])
        fehlend = [x for x in pruef if x not in vorhanden]
        if fehlend:
            raise SystemExit(f"Element-IDs der Vorlage fehlen auf dieser Seite: {fehlend}")
    steuerung.setdefault("elements", []).append(hd.style_widget(ids))
    return 1


if __name__ == "__main__":
    menu_slug, src, dst = sys.argv[1:4]
    data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    n = footer_setzen(data, menu_slug) + handy_widget_ergaenzen(data)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
