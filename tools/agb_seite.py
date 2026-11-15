#!/usr/bin/env python3
"""AGB-Seite (/agb/, ID 782): die AGB-Fassung aus `inhalte/agb-2026-01.txt` in die bestehende Seite einbauen.

Die Seite besteht aus Logo-Kopf, einem Inhaltsbereich mit Überschrift (Widget 5ed217e, H1) und einem Text-Widget
(d3d6ae8) sowie dem Seiten-Footer. Geändert werden nur Überschrift und Text-Widget; alle anderen Elemente und die
Einstellungen des Text-Widgets bleiben, nur `editor` (Inhalt) und `custom_css` (Abstände, Inhaltsverzeichnis,
Formularkasten) werden gesetzt.

Aufbau des erzeugten HTML (wie die Datenschutzerklärung: Überschriften und Absätze im Text-Widget):
  - Zeile 1 der Textdatei → H1 (Überschrift-Widget), Zeile 2 und 3 (Anschrift, Stand) → Vorspann
  - Inhaltsverzeichnis mit Sprungmarken zu den Abschnitten und Ziffern
  - „Abschnitt X: …“ → h2, „N. Titel“ → h3, „(n) …“ → Absatz, Ziffer 23 mit fetten Vorspannwörtern und dem
    Muster-Widerrufsformular als Kasten mit Zeilenumbrüchen
  - gerade Anführungszeichen → deutsche („…“), Verweise auf Datenschutzerklärung, OS-Plattform, E-Mail und Telefon
    als Links; am Wortlaut wird nichts geändert
Aufruf: python3 -I tools/agb_seite.py export.json ziel.json [inhalte/agb-2026-01.txt]
"""
import html
import json
import pathlib
import re
import sys

H1_ID, TEXT_ID = "5ed217e", "d3d6ae8"

CSS = """selector h2{margin-top:2.4em;margin-bottom:.6em}
selector h3{margin-top:1.8em;margin-bottom:.5em}
selector p{margin-bottom:1em}
selector .agb-meta{opacity:.85}
selector .agb-hinweis{font-style:italic}
selector .agb-inhalt ul{list-style:none;padding-left:0;margin:0 0 1.5em}
selector .agb-inhalt li{margin:.35em 0}
selector .agb-inhalt ul ul{padding-left:1.2em;margin:.3em 0 .9em}
selector .agb-formular{border:1px solid currentColor;border-radius:12px;padding:16px 20px;margin:1.2em 0 1.6em}
selector .agb-formular p:last-child{margin-bottom:0}
selector a{text-decoration:underline}"""


def esc(s):
    return html.escape(s, quote=False)


def typografie(s):
    """Gerade doppelte Anführungszeichen paarweise durch „…“ ersetzen."""
    return re.sub(r'"([^"]+)"', "„\\1“", s)


def links(s):
    """Verweise als Links (s ist bereits HTML-sicher)."""
    s = s.replace("provision-infra.de/datenschutz", '<a href="/datenschutz/">provision-infra.de/datenschutz</a>')
    s = s.replace("ec.europa.eu/consumers/odr", '<a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener">ec.europa.eu/consumers/odr</a>')
    s = re.sub(r"\b([a-z]+@provision-infra\.de)\b", r'<a href="mailto:\1">\1</a>', s)
    s = s.replace("Telefon 05821 4049040", 'Telefon <a href="tel:+4958214049040">05821 4049040</a>')
    return s


def absatz(text, klasse=None):
    k = f' class="{klasse}"' if klasse else ""
    return f"<p{k}>{links(esc(typografie(text)))}</p>"


def bauen_html(zeilen):
    zeilen = [z.rstrip() for z in zeilen]
    titel, anschrift, stand = zeilen[0], zeilen[1], zeilen[2]
    rest = [z for z in zeilen[3:] if z.strip()]
    abschnitte = []  # (buchstabe, titel, [(nummer, titel)])
    koerper = []
    for z in rest:
        m = re.match(r"^Abschnitt ([A-F]): (.+)$", z)
        if m:
            abschnitte.append((m.group(1), m.group(2), []))
            koerper.append(f'<h2 id="abschnitt-{m.group(1).lower()}">{esc(z)}</h2>')
            continue
        m = re.match(r"^\((Ziffern [^)]+)\)$", z)
        if m:
            koerper.append(f'<p class="agb-hinweis">{esc(z)}</p>')
            continue
        m = re.match(r"^(\d{1,2})\. (.+)$", z)
        if m:
            abschnitte[-1][2].append((m.group(1), m.group(2)))
            koerper.append(f'<h3 id="ziffer-{m.group(1)}">{esc(typografie(z))}</h3>')
            continue
        if re.match(r"^\(\d+\) ", z):
            koerper.append(absatz(z))
            continue
        m = re.match(r"^(Widerrufsrecht|Folgen des Widerrufs|Vorzeitiges Erlöschen): (.+)$", z)
        if m:
            koerper.append(f"<p><strong>{esc(m.group(1))}:</strong> {links(esc(typografie(m.group(2))))}</p>")
            continue
        m = re.match(r"^Muster-Widerrufsformular \((.+?)\): (An .+?\.) (Hiermit .+?) … (Bestellt .+?) … (Name .+?) … (Anschrift .+?) … (Unterschrift .+?) … (Datum: …) (\(\*\) Unzutreffendes streichen\.)$", z)
        if m:
            kopf = f"<p><strong>Muster-Widerrufsformular</strong><br>({esc(m.group(1))}):</p>"
            zeilen_formular = [m.group(2)] + [m.group(i) + " …" for i in range(3, 8)] + [m.group(8), m.group(9)]
            koerper.append(f'<div class="agb-formular">{kopf}<p>' + "<br>".join(links(esc(t)) for t in zeilen_formular) + "</p></div>")
            continue
        m = re.match(r"^ProVision Infra GmbH, Bad Bevensen, Stand .+$", z)
        if m:
            koerper.append(absatz(z, "agb-meta"))
            continue
        # Absatz ohne Nummer (z. B. Ziffer 12)
        koerper.append(absatz(z))
    inhalt = ['<nav class="agb-inhalt" aria-label="Inhalt"><p><strong>Inhalt</strong></p><ul>']
    for buchstabe, atitel, ziffern in abschnitte:
        inhalt.append(f'<li><a href="#abschnitt-{buchstabe.lower()}">Abschnitt {buchstabe}: {esc(atitel)}</a><ul>')
        for nummer, ztitel in ziffern:
            inhalt.append(f'<li><a href="#ziffer-{nummer}">{nummer}. {esc(typografie(ztitel))}</a></li>')
        inhalt.append("</ul></li>")
    inhalt.append("</ul></nav>")
    vorspann = f'<p class="agb-meta">{esc(anschrift)}<br>{esc(stand)}</p>'
    return titel, vorspann + "\n" + "\n".join(inhalt) + "\n" + "\n".join(koerper), abschnitte


def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))


def anwenden(data, textdatei):
    zeilen = pathlib.Path(textdatei).read_text(encoding="utf-8").splitlines()
    titel, html_inhalt, abschnitte = bauen_html(zeilen)
    by = {e["id"]: e for e in walk(data["elements"])}
    by[H1_ID]["settings"]["title"] = titel
    by[TEXT_ID]["settings"]["editor"] = html_inhalt
    by[TEXT_ID]["settings"]["custom_css"] = CSS
    return data, titel, html_inhalt, abschnitte


if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    textdatei = sys.argv[3] if len(sys.argv) > 3 else pathlib.Path(__file__).resolve().parent.parent / "inhalte" / "agb-2026-01.txt"
    data = json.loads(pathlib.Path(src).read_text(encoding="utf-8"))
    data, titel, html_inhalt, abschnitte = anwenden(data, textdatei)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print(f"AGB eingebaut: H1 {titel!r}, {len(abschnitte)} Abschnitte, {sum(len(a[2]) for a in abschnitte)} Ziffern, {html_inhalt.count('<p')} Absätze → {dst}")
