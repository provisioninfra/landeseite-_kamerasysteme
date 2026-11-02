#!/usr/bin/env python3
"""Darstellungs-CSS für Smartphones (tools/handy_darstellung.py) als HTML-Widget in den eigenen Steuerungs-Container
eines Elementor-Exports einfügen oder aktualisieren. Aufruf: python3 -I tools/handy_patch.py export.json ziel.json [Seiten-ID]
"""
import hashlib, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import handy_darstellung

src, dst = sys.argv[1:3]; seite = int(sys.argv[3]) if len(sys.argv) > 3 else int(pathlib.Path(src).stem[:4] if pathlib.Path(src).stem[:4].isdigit() else pathlib.Path(src).stem[:2])
data = json.loads(pathlib.Path(src).read_text(encoding="utf-8")); page = data["elements"]
def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))
def box(v): return {"unit": "px", "top": str(v), "right": str(v), "bottom": str(v), "left": str(v), "isLinked": True}
widget = handy_darstellung.style_widget(handy_darstellung.SEITEN[seite])
vorhanden = [e for e in walk(page) if e.get("widgetType") == "html" and e.get("settings", {}).get("_title") == widget["settings"]["_title"]]
if vorhanden:
    for e in vorhanden:
        e["settings"]["html"] = widget["settings"]["html"]; e["settings"]["custom_css"] = widget["settings"]["custom_css"]
    print(f"Widget aktualisiert: {[e['id'] for e in vorhanden]}")
else:
    ziel = next((e for e in page if e.get("elType") == "container" and e.get("settings", {}).get("_title", "").startswith("Steuerung")), None)
    if ziel is None:
        ziel = {"id": hashlib.md5(f"steuerung-handy-{pathlib.Path(src).stem}".encode()).hexdigest()[:7], "elType": "container", "isInner": False,
                "elements": [], "settings": {"content_width": "full", "padding": box(0), "margin": box(0),
                                             "min_height": {"unit": "px", "size": 0, "sizes": []}, "_title": "Steuerung Handy-Darstellung"}}
        page.append(ziel); print(f"Neuer Container {ziel['id']}")
    ziel["elements"].append(widget); print(f"Widget {widget['id']} in Container {ziel['id']}")
pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
