#!/usr/bin/env python3
"""Eine vorhandene Textstelle in einem Elementor-Textwidget verlinken, ohne den Text zu ändern (SEO-Check Stufe A5).

Aufruf: python3 -I tools/text_link.py export.json ziel.json WIDGET_ID "genauer Text" https://ziel/
Ersetzt im Feld `editor` (oder `description_text`) des Widgets die erste Fundstelle des Textes, die nicht schon in
einem Link steht, durch <a href="…">Text</a>. Alles andere bleibt unverändert; ohne Fundstelle wird nichts geschrieben.
"""
import json, pathlib, re, sys


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def verlinken(data, widget_id, text, url):
    for e in walk(data["elements"]):
        if e.get("id") != widget_id:
            continue
        s = e.setdefault("settings", {})
        feld = "editor" if isinstance(s.get("editor"), str) else "description_text"
        inhalt = s.get(feld)
        if not isinstance(inhalt, str):
            raise SystemExit(f"Widget {widget_id} hat kein Textfeld")
        # Fundstellen außerhalb bestehender Links suchen
        for m in re.finditer(re.escape(text), inhalt):
            davor = inhalt[: m.start()]
            if davor.count("<a ") > davor.count("</a>"):
                continue  # liegt in einem Link
            s[feld] = inhalt[: m.start()] + f'<a href="{url}">{text}</a>' + inhalt[m.end():]
            return 1
        raise SystemExit(f"Text „{text}“ nicht (unverlinkt) im Widget {widget_id} gefunden")
    raise SystemExit(f"Widget {widget_id} nicht gefunden")


if __name__ == "__main__":
    src, dst, wid, text, url = sys.argv[1:6]
    data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    n = verlinken(data, wid, text, url)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"Ersetzungen: {n}")
