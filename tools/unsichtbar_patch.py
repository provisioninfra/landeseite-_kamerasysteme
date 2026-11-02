#!/usr/bin/env python3
"""Unsichtbare SEO-/Ladezeit-Änderungen auf einen Elementor-Export anwenden (02.11.2026, Freigabe des Kunden:
„alles ändern, aber in der Ansicht darf sich nichts ändern“).

Aufruf: python3 -I tools/unsichtbar_patch.py export.json ziel.json lottie-uploads.json
  1. Lottie-Widgets auf die pixelidentisch verkleinerten Dateien umstellen (tools/lottie_webp.py, Zuordnung aus
     lottie-uploads.json: Originaldateiname -> {id, url}),
  2. Strukturdaten: Kennung „#organisation“ -> „#organization“ (eine Entität auf allen Seiten, wie Karriere/Yoast),
  3. Steuerungs-Widget anhängen (tools/ladeverhalten.py): ausgeblendete Lotties/Videos nicht laden, Product-Schema des
     Bewertungssiegels aus dem gerenderten DOM nehmen.
Alles andere bleibt byteidentisch; das Skript meldet jede Änderung.
"""
import hashlib, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import ladeverhalten

src, dst, upl = sys.argv[1:4]
data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
uploads = json.loads(pathlib.Path(upl).read_text(encoding="utf-8"))
page = data["elements"]; log = []

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def box(v):
    return {"unit": "px", "top": str(v), "right": str(v), "bottom": str(v), "left": str(v), "isLinked": True}

# 1) Lottie-Quellen
for e in walk(page):
    if e.get("widgetType") != "lottie":
        continue
    src_json = e["settings"].get("source_json") or {}
    name = (src_json.get("url") or "").split("/")[-1]
    if name in uploads:
        e["settings"]["source_json"] = {"url": uploads[name]["url"], "id": uploads[name]["id"]}
        log.append(f"Lottie {e['id']}: {name} -> Medien-ID {uploads[name]['id']}")

# 2) Strukturdaten-Kennung
for e in walk(page):
    h = e.get("settings", {}).get("html")
    if isinstance(h, str) and "application/ld+json" in h and "#organisation" in h:
        e["settings"]["html"] = h.replace("https://provision-infra.de/#organisation", "https://provision-infra.de/#organization")
        log.append(f"Schema {e['id']}: #organisation -> #organization")

# 3) Steuerungs-Widget
widget = ladeverhalten.script_widget(f"ladeverhalten-{pathlib.Path(src).stem}")
vorhanden = [e for e in walk(page) if e.get("widgetType") == "html" and e.get("settings", {}).get("_title") == widget["settings"]["_title"]]
if vorhanden:
    for e in vorhanden:   # bestehendes Widget auf den aktuellen Stand bringen (Skript, Ausblendung)
        if e["settings"].get("html") != widget["settings"]["html"] or e["settings"].get("custom_css") != widget["settings"]["custom_css"]:
            e["settings"]["html"] = widget["settings"]["html"]; e["settings"]["custom_css"] = widget["settings"]["custom_css"]
            log.append(f"Steuerungs-Widget {e['id']} aktualisiert")
    if not any("aktualisiert" in l for l in log): log.append("Steuerungs-Widget bereits vorhanden")
else:
    # nur eigene Steuerungs-Container (Titel beginnt mit „Steuerung“), nicht den Container der Parallelsitzung
    ziel = next((e for e in page if e.get("elType") == "container" and e.get("settings", {}).get("_title", "").startswith("Steuerung")), None)
    if ziel is None:
        ziel = {"id": hashlib.md5(f"steuerung-{pathlib.Path(src).stem}".encode()).hexdigest()[:7], "elType": "container", "isInner": False,
                "elements": [], "settings": {"content_width": "full", "padding": box(0), "margin": box(0),
                                             "min_height": {"unit": "px", "size": 0, "sizes": []}, "_title": "Steuerung Ladeverhalten"}}
        page.append(ziel); log.append(f"Neuer Steuerungs-Container {ziel['id']} am Seitenende")
    ziel["elements"].append(widget); log.append(f"Steuerungs-Widget {widget['id']} in Container {ziel['id']}")

pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
print("\n".join(log) or "keine Änderungen")
