#!/usr/bin/env python3
"""Footer je Seite: Firmendaten-Zeile und Link-Block „Leistungen“ / „Standorte“ ergänzen (17.11.2026, SEO-Check Stufe A3).

Die Seiten haben keinen globalen Footer, sondern je Seite einen Footer-Bereich mit derselben Struktur: unterste Zeile mit
Copyright-Text und der Linkliste Datenschutz/Impressum/AGB (auf der Startseite zusätzlich eine kleine Liste
„Leistungen:“). Das Werkzeug
  1. hängt an den Copyright-Text eine zweite Zeile mit Anschrift, Telefon und E-Mail an (Local-SEO: Firmendaten auf
     jeder Seite),
  2. fügt oberhalb der untersten Zeile eine neue Zeile ein, im selben Stil (Trennlinie, kleine Schrift), mit den
     Listen „Leistungen:“ (nur, wenn die Seite noch keine hat) und „Standorte:“ (alle 15 Ortsseiten),
  3. ergänzt eine vorhandene Liste „Leistungen:“ um Zutrittssystem und Schlachthöfe.
Alle anderen Elemente bleiben unverändert; läuft das Werkzeug zweimal, ändert der zweite Lauf nichts.
Aufruf: python3 -I tools/footer_block.py export.json ziel.json   (Ausgabe: was ergänzt wurde)
"""
import copy, json, pathlib, sys

FIRMENZEILE = ('<p>Klein Hesebecker Straße 11 · 29549 Bad Bevensen · Tel. <a href="tel:+4958214049040">05821 4049040</a> · '
               '<a href="mailto:hey@provision-infra.de">hey@provision-infra.de</a></p>')
LEISTUNGEN = [("Leistungen:", None), ("Schließanlagen", "/"), ("Zutrittssystem", "/zutrittssystem/"),
              ("Kamera- & Videosicherheit", "/kamerasysteme/"), ("Schlachthöfe", "/videoueberwachung-schlachthoefe/"),
              ("Karriere", "/karriere/")]
STANDORTE = [("Standorte:", None), ("Lüneburg", "/lueneburg/"), ("Uelzen", "/uelzen/"), ("Bad Bevensen", "/bad-bevensen/"),
             ("Bad Bodenteich", "/bad-bodenteich/"), ("Bienenbüttel", "/bienenbuettel/"), ("Bleckede", "/bleckede/"),
             ("Celle", "/celle/"), ("Dannenberg", "/dannenberg/"), ("Ebstorf", "/ebstorf/"), ("Gifhorn", "/gifhorn/"),
             ("Hitzacker", "/hitzacker/"), ("Lüchow", "/luechow/"), ("Wieren", "/wieren/"), ("Winsen (Luhe)", "/winsen-luhe/"),
             ("Wittingen", "/wittingen/")]
ERGAENZUNG_LEISTUNGEN = [("Zutrittssystem", "/zutrittssystem/"), ("Schlachthöfe", "/videoueberwachung-schlachthoefe/")]
MOBIL_CSS = ("@media (max-width: 767px) { selector .elementor-icon-list-items > li:first-child { flex-basis: 100%; "
             "justify-content: center; margin: 0 0 6px !important; } }")
ID_ZEILE, ID_LEISTUNGEN, ID_STANDORTE = "a1f0071", "a1f0072", "a1f0073"


def walk(els, parent=None):
    for e in els:
        yield e, parent
        yield from walk(e.get("elements", []), e)


def eintrag(text, url, nr):
    e = {"text": text, "selected_icon": {"value": "", "library": ""}, "_id": f"{0xa1f100 + nr:07x}"}
    if url:
        e["link"] = {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""}
    return e


def liste(wid, titel, eintraege, vorlage):
    s = {k: copy.deepcopy(v) for k, v in vorlage["settings"].items() if k in ("view", "icon_align_mobile", "_element_width_mobile", "__globals__", "space_between", "icon_typography_typography", "text_color", "text_color_hover")}
    s.update({"view": "inline", "icon_list": [eintrag(t, u, i) for i, (t, u) in enumerate(eintraege)], "icon_align_mobile": "center",
              "_element_width_mobile": "inherit", "_title": titel, "custom_css": MOBIL_CSS})
    return {"id": wid, "elType": "widget", "widgetType": "icon-list", "isInner": False, "elements": [], "settings": s}


def anwenden(data):
    getan = []
    paare = list(walk(data["elements"]))
    # unterste Footer-Zeile: Container mit der Liste Datenschutz/Impressum/AGB
    rechtsliste = next((e for e, p in paare if e.get("widgetType") == "icon-list" and any(i.get("text") == "Impressum" for i in e["settings"].get("icon_list", []))), None)
    if not rechtsliste:
        return data, ["kein Footer gefunden"]
    zeile = next(p for e, p in paare if e is rechtsliste)            # eeafe4e / c8ec6d2
    rahmen = next(p for e, p in paare if e is zeile)                  # 691e145 / 73349a5
    spalte = next(p for e, p in paare if e is rahmen)                 # ddbba36 / ebac46e
    # 1. Firmenzeile im Copyright-Text
    copyright = next((e for e in zeile["elements"] if e.get("widgetType") == "text-editor" and "Alle Rechte vorbehalten" in e["settings"].get("editor", "")), None)
    if copyright and "Klein Hesebecker" not in copyright["settings"]["editor"]:
        copyright["settings"]["editor"] = copyright["settings"]["editor"].rstrip() + "\n" + FIRMENZEILE
        getan.append("Firmenzeile")
    # 3. vorhandene Leistungen-Liste ergänzen
    leistungen_alt = next((e for e, p in paare if e.get("widgetType") == "icon-list" and (e["settings"].get("icon_list") or [{}])[0].get("text") == "Leistungen:"), None)
    if leistungen_alt:
        vorhanden = {i.get("link", {}).get("url", "").replace("https://provision-infra.de", "") for i in leistungen_alt["settings"]["icon_list"]}
        for n, (t, u) in enumerate(ERGAENZUNG_LEISTUNGEN):
            if u not in vorhanden:
                leistungen_alt["settings"]["icon_list"].append(eintrag(t, u, 50 + n)); getan.append(f"Leistungen + {t}")
    # 2. neue Zeile mit Listen
    if not any(e.get("id") == ID_ZEILE for e, p in paare):
        kinder = [liste(ID_STANDORTE, "Standorte", STANDORTE, rechtsliste)]
        if not leistungen_alt:
            kinder.insert(0, liste(ID_LEISTUNGEN, "Leistungen", LEISTUNGEN, rechtsliste))
        neu = {"id": ID_ZEILE, "elType": "container", "isInner": True, "elements": kinder, "settings": {
            "content_width": "full", "flex_direction": "column", "flex_gap": {"unit": "px", "size": 8, "column": "8", "row": "8", "isLinked": True},
            "border_border": "solid", "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
            "border_color": "#FFFFFF52", "padding": {"unit": "px", "top": "24", "right": "0", "bottom": "24", "left": "0", "isLinked": False},
            "boxed_width": {"unit": "px", "size": 1400, "sizes": []}, "_title": "Footer: Leistungen und Standorte"}}
        idx = spalte["elements"].index(rahmen)
        spalte["elements"].insert(idx, neu)
        getan.append("Zeile Leistungen/Standorte")
    return data, getan


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, getan = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Footer:", ", ".join(getan) if getan else "nichts zu tun")
