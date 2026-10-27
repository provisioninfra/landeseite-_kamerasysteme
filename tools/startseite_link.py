#!/usr/bin/env python3
"""Startseite (Seiten-ID 31): Link zur Kameraseite einbauen.

Liest die Sicherung der aktuellen Startseiten-Daten (elementor/startseite-sicherung-2026-10-26.json, aus dem Elementor-
Editor exportiert) und schreibt elementor/startseite-mit-link.elements.json mit drei Änderungen:
  1. Teaser-Abschnitt „Videoüberwachung aus einer Hand“ vor dem Gründer-Abschnitt (Kasten im Stil des Standort-Kastens,
     zwei Sätze, gelber Button „Videoüberwachung für Unternehmen“ auf /kamerasysteme/),
  2. Footer-Zeile „Leistungen: Schließsysteme | Videoüberwachung“ neben Datenschutz, Impressum, AGB,
  3. Footer-Menü-Widgets fest auf das Menü „main“ (bisher Verweis auf ein nicht vorhandenes Menü),
  4. Kopfleisten-Menü auf dem Handy flach („Mehr“ nur am Bildschirm; tools/menue_handy.py), Vorgabe vom 27.10.2026.
Alles andere bleibt byteidentisch. Freigabe des Kunden vom 26.10.2026 (1–3) und 27.10.2026 (4).
"""
import copy, hashlib, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))   # tools/ auch im isolierten Modus (python3 -I)
import menue_handy   # Handy-Menü: CSS und Skript (gleich auf Start- und Kameraseite)

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "elementor" / "startseite-sicherung-2026-10-26.json"
DST = ROOT / "elementor" / "startseite-mit-link.elements.json"
SITE = "https://provision-infra.de"
KAMERA_URL = f"{SITE}/kamerasysteme/"

TEASER_H = 'Videoüberwachung <span style="font-weight: 700; ">aus einer Hand</span>'
TEASER_T = ("<p>Einbruch, Diebstahl und Vandalismus auf dem Firmengelände: Wir planen und installieren Kamerasysteme mit Alarm "
            "aufs Handy. Zutritt und Überwachung kommen so aus einer Hand.</p>")
TEASER_BTN = "Videoüberwachung für Unternehmen"

_n = [0]
def new_id():
    _n[0] += 1
    return hashlib.md5(f"startseite-link-{_n[0]}".encode()).hexdigest()[:7]

def clone(el):
    return copy.deepcopy(el)

def reid(el):
    el["id"] = new_id()
    for c in el.get("elements", []):
        reid(c)
    return el

def find(el, eid):
    if el.get("id") == eid:
        return el
    for c in el.get("elements", []):
        r = find(c, eid)
        if r:
            return r
    return None

def must(root, eid):
    for sec in (root if isinstance(root, list) else [root]):
        r = find(sec, eid)
        if r:
            return r
    raise AssertionError(f"Element {eid} nicht gefunden")

def box(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}

data = json.loads(SRC.read_text(encoding="utf-8"))
page = data["elements"]
assert len(page) == 23, len(page)

# ---------------------------------------------------------------- 1) Teaser vor dem Gründer-Abschnitt
gruender_index = next(i for i, sec in enumerate(page) if sec["settings"].get("_element_id") == "Über")
standort_box = must(page, "0fd35f5")           # Kasten rechts im Standort-Abschnitt (Rahmen, Radius, Polster)
teaser_box = reid(clone(standort_box))
teaser_box["settings"].update({
    "_title": "Teaser-Kasten",
    "width": {"unit": "px", "size": 820, "sizes": []},
    "width_tablet": {"unit": "%", "size": 100, "sizes": []},
    "width_mobile": {"unit": "%", "size": 100, "sizes": []},
    "padding": box(48, 56, 48, 56), "padding_laptop": box(44, 48, 44, 48),
})
inner = teaser_box["elements"][0]
heading = next(w for w in inner["elements"] if w.get("widgetType") == "heading")
text = next(w for w in inner["elements"] if w.get("widgetType") == "text-editor")
button = next(w for w in inner["elements"] if w.get("widgetType") == "button")
inner["elements"] = [heading, text, button]
heading["settings"].update({"title": TEASER_H, "_title": "Überschrift", "header_size": "h2",
                            "typography_font_size": {"unit": "px", "size": 36, "sizes": []},
                            "typography_font_size_tablet_extra": {"unit": "px", "size": 32, "sizes": []},
                            "typography_font_size_tablet": {"unit": "px", "size": 27, "sizes": []},
                            "typography_font_size_mobile": {"unit": "px", "size": 23, "sizes": []}})
text["settings"].update({"editor": TEASER_T, "_title": "Text"})
button["settings"].update({"text": TEASER_BTN, "_title": "Button zur Kameraseite",
                           "link": {"url": KAMERA_URL, "is_external": "", "nofollow": "", "custom_attributes": ""}})
teaser = {"id": new_id(), "elType": "container", "isInner": False, "elements": [teaser_box], "settings": {
    "content_width": "boxed", "flex_direction": "column", "flex_align_items": "center", "flex_justify_content": "center",
    "background_background": "classic", "background_color": "#000D3000",
    "padding": box(60, 20, 60, 20), "padding_laptop": box(60, 20, 60, 20), "padding_tablet": box(50, 20, 50, 20),
    "padding_mobile": box(40, 20, 40, 20),
    "_element_id": "videoueberwachung", "_title": "Videoüberwachung aus einer Hand (Teaser)"}}
page.insert(gruender_index, teaser)

# ---------------------------------------------------------------- 2) Footer-Zeile „Leistungen“
legal = must(page, "1f95880")                  # Icon-Liste Datenschutz | Impressum | AGB
row = must(page, "eeafe4e")
leistungen = reid(clone(legal))
item_tpl = legal["settings"]["icon_list"][0]
def item(text, url=None):
    it = clone(item_tpl)
    it["_id"] = new_id()
    it["text"] = text
    it["link"] = {"url": url or "", "is_external": "", "nofollow": "", "custom_attributes": ""}
    return it
leistungen["settings"]["icon_list"] = [item("Leistungen:"), item("Schließsysteme", f"{SITE}/"), item("Videoüberwachung", KAMERA_URL)]
leistungen["settings"]["_title"] = "Leistungen"
# Handy: „Leistungen:“ in eigener Zeile, darunter die beiden Links (sonst bricht die Zeile mittendrin um)
leistungen["settings"]["custom_css"] = ("@media (max-width: 767px) { selector .elementor-icon-list-items > li:first-child "
                                       "{ flex-basis: 100%; justify-content: center; margin: 0 0 6px !important; } }")
row["elements"].insert(row["elements"].index(legal), leistungen)

# ---------------------------------------------------------------- 3) Footer-Menüs fest auf „main“
for wid in ("59b27e3", "a430424"):
    w = must(page, wid)
    assert w.get("widgetType") == "nav-menu"
    w["settings"]["menu"] = "main"

# ---------------------------------------------------------------- 4) Kopfleisten-Menü auf dem Handy flach
nav = must(page, "2a487ab")
assert nav.get("widgetType") == "nav-menu"
nav["settings"]["custom_css"] = menue_handy.handy_css(nav["settings"])
steuerung = {"id": new_id(), "elType": "container", "isInner": False, "elements": [menue_handy.script_widget("startseite-handy-menue")],
             "settings": {"content_width": "full", "padding": box(0, 0, 0, 0), "margin": box(0, 0, 0, 0),
                          "min_height": {"unit": "px", "size": 0, "sizes": []}, "_title": "Steuerung Handy-Menü"}}
page.append(steuerung)

DST.write_text(json.dumps({"elements": page, "settings": data["settings"], "title": data["title"], "status": data["status"]},
                          ensure_ascii=False), encoding="utf-8")
print(f"Abschnitte: {len(page)} (Teaser an Position {gruender_index}), Datei: {DST.name}, Größe: {DST.stat().st_size // 1024} KB")
