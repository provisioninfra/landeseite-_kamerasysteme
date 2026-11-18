#!/usr/bin/env python3
"""Footer angleichen, Nachtrag zu Runde 3 (18.11.2026):
1. Außenabstand des Footer-Blocks a1f0071 auf 0 (sonst 10 px Standard-Innenabstand des Containers, Listen bei schmalen
   Breiten 10 px gegenüber Copyright eingerückt).
2. Startseite: Die alte Liste „Leistungen:“ in der Copyright-Zeile (d38bcbe, auf vier Einträge erweitert) ließ die Zeile
   bei 2560 px umbrechen („Schlachthöfe“ und „AGB“ allein in zweiter Zeile). Die Liste wandert als Zeile „Leistungen“
   in den Footer-Block (wie auf allen anderen Seiten), die Copyright-Zeile hat wieder Copyright und Rechtslinks.
3. Barrierefreiheit (Lighthouse nach dem Footer-Block: „target-size“ und „link-in-text-block“): Links der beiden Listen
   bekommen 5 px Innenabstand oben/unten (Tippfläche ≥ 24 px), die Beschriftungen „Leistungen:“/„Standorte:“ eine
   gedämpfte Farbe (#8A94B0), damit Links und Text ohne Unterstreichung unterscheidbar sind (Kontrast ≥ 3:1).
Aufruf: python3 -I tools/footer_start_angleichen.py export.json ziel.json   (Ausgabe: Zahl der Änderungen)
"""
import importlib.util, json, pathlib, sys

HIER = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("footer_block", HIER / "footer_block.py")
fb = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(fb)
NULL = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
A11Y_CSS = ("/* pv-a11y */ selector .elementor-icon-list-item a { display: inline-block; padding: 5px 0; } "
            "selector .elementor-icon-list-items > li:first-child .elementor-icon-list-text { color: #8A94B0; }")


def walk(els, parent=None):
    for e in els:
        yield e, parent
        yield from walk(e.get("elements", []), e)


def anwenden(data):
    n = 0
    paare = list(walk(data["elements"]))
    block = next((e for e, _ in paare if e.get("id") == "a1f0071"), None)
    innen = next((e for e, _ in paare if e.get("id") == "a1f0074"), None)
    if block is not None and block.get("settings", {}).get("padding") != NULL:
        block.setdefault("settings", {})["padding"] = NULL
        n += 1
    for e, _ in paare:
        if e.get("id") in ("a1f0072", "a1f0073") and "pv-a11y" not in (e.get("settings", {}).get("custom_css") or ""):
            css = e.setdefault("settings", {}).get("custom_css") or ""
            e["settings"]["custom_css"] = (css.rstrip() + "\n" if css.strip() else "") + A11Y_CSS
            n += 1
    if innen is None:
        return data, n
    alt = next(((e, p) for e, p in paare if e.get("widgetType") == "icon-list" and e.get("id") != "a1f0072"
                and (e["settings"].get("icon_list") or [{}])[0].get("text") == "Leistungen:"), None)
    hat_block_leistungen = any(c.get("id") == "a1f0072" for c in innen.get("elements", []))
    if alt and not hat_block_leistungen:
        widget, zeile = alt
        vorlage = next(e for e, _ in paare if e.get("id") == "a1f0073")
        innen["elements"].insert(0, fb.liste(fb.ID_LEISTUNGEN, "Leistungen", fb.LEISTUNGEN, vorlage))
        zeile["elements"] = [c for c in zeile["elements"] if c is not widget]
        n += 2
    return data, n


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data, n = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
