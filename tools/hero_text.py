#!/usr/bin/env python3
"""Hero der Startseite, der Kamera-Seite und der Ortsseiten (07./08.11.2026, Rückmeldung des Kunden am Handy):
  1. Etwas mehr Abstand zwischen Überschrift und Unterzeile am Handy (Überschrift 9dcea29: Innenabstand unten
     mobil 10 → 18 px; alle anderen Geräteklassen unverändert: Tablet 20, Laptop 15, Computer 35 px).
  2. Zweiter Absatz der Unterzeile (Widget e429076, Text nach dem doppelten Zeilenumbruch) leicht gekürzt und fett
     (span mit font-weight 700, dieselbe Technik wie im fetten Teil der Überschrift).
Alle Seiten tragen dieselben Element-IDs (Kamera- und Ortsseiten sind Kopien der Startseite), nur der Absatztext
unterscheidet sich; er steht je Seiten-ID in TEXTE.
Aufruf: python3 -I tools/hero_text.py export.json ziel.json [Seiten-ID, Vorgabe 31]
"""
import json, pathlib, sys

TEXTE = {
    # Startseite (/): digitales Zutrittssystem
    31: (
        "ProVision Infra plant &amp; installiert in Norddeutschland dein digitales Zutrittssystem, mit dem du Zugänge per "
        "Chip, KeyCard oder App in Sekunden vergibst und entziehst – und so Zeit und Aufwand im Alltag sparst.",
        '<span style="font-weight: 700;">ProVision Infra plant &amp; installiert in Norddeutschland dein digitales '
        'Zutrittssystem: Zugänge per Chip, KeyCard oder App in Sekunden vergeben und entziehen – das spart dir Zeit und '
        'Aufwand im Alltag.</span>',
    ),
    # Kamera-Seite (/kamerasysteme/): Kamera- und Videoüberwachung (33 → 28 Wörter, Aussage unverändert)
    4313: (
        "ProVision Infra plant und installiert Kamera- und Videoüberwachung für Unternehmen. Du siehst jederzeit per App, "
        "was auf deinem Gelände passiert, und hast im Ernstfall Aufnahmen, die etwas beweisen.",
        '<span style="font-weight: 700;">ProVision Infra plant und installiert Kamera- und Videoüberwachung für '
        'Unternehmen: Du siehst per App jederzeit, was auf deinem Gelände passiert – und hast im Ernstfall Aufnahmen, '
        'die etwas beweisen.</span>',
    ),
    # Ortsseite Lüneburg (/lueneburg/): 37 → 33 Wörter, alle Aussagen erhalten (Leistungen, Varianten, Zielgruppen,
    # Sitz Bad Bevensen, halbe Stunde Anfahrt)
    4496: (
        "ProVision Infra plant, installiert und betreut Schließanlagen und Videoüberwachung in Lüneburg – mechanisch, "
        "elektronisch oder kombiniert, für Betriebe, Praxen und Gewerbe. Von unserem Sitz in Bad Bevensen sind wir in rund "
        "einer halben Stunde bei dir vor Ort.",
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen und '
        'Videoüberwachung in Lüneburg: mechanisch, elektronisch oder kombiniert, für Betriebe, Praxen und Gewerbe – von '
        'unserem Sitz in Bad Bevensen in rund einer halben Stunde bei dir.</span>',
    ),
    # Ortsseite Uelzen (/uelzen/): 35 → 33 Wörter
    4605: (
        "ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Uelzen und im "
        "ganzen Landkreis – mechanisch, elektronisch oder beides zusammen. Unser Sitz liegt in Bad Bevensen, keine 20 "
        "Minuten von der Uelzener Innenstadt entfernt.",
        '<span style="font-weight: 700;">ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und '
        'Videoüberwachung in Uelzen und im ganzen Landkreis – mechanisch, elektronisch oder kombiniert. Unser Sitz in Bad '
        'Bevensen liegt keine 20 Minuten von der Uelzener Innenstadt entfernt.</span>',
    ),
    # Ortsseite Bad Bevensen: 32 → 30 Wörter
    4735: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bad Bevensen – mechanisch, elektronisch oder kombiniert. Unser Firmensitz liegt in der Klein Hesebecker Straße, wir sind in wenigen Minuten bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bad Bevensen: mechanisch, elektronisch oder kombiniert – von unserem Firmensitz in der Klein Hesebecker Straße in wenigen Minuten bei dir.</span>',
    ),
    # Ortsseite Bad Bodenteich: 33 → 31 Wörter
    4739: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bad Bodenteich und der Samtgemeinde Aue – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in rund 30 Minuten bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bad Bodenteich und der Samtgemeinde Aue: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in rund 30 Minuten bei dir.</span>',
    ),
    # Ortsseite Bienenbüttel: 29 → 27 Wörter
    4743: (
        'ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bienenbüttel und seinen Ortsteilen – mechanisch, elektronisch oder beides zusammen. Unser Sitz in Bad Bevensen liegt eine Viertelstunde entfernt.',
        '<span style="font-weight: 700;">ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bienenbüttel und seinen Ortsteilen: mechanisch, elektronisch oder kombiniert – eine Viertelstunde von unserem Sitz in Bad Bevensen.</span>',
    ),
    # Ortsseite Bleckede: 32 → 30 Wörter
    4747: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bleckede und an der Elbe – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in rund 30 Minuten bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Bleckede und an der Elbe: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in rund 30 Minuten bei dir.</span>',
    ),
    # Ortsseite Celle: 36 → 30 Wörter
    4751: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Celle und im Landkreis Celle – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in gut einer Stunde bei dir, das Erstgespräch ist unverbindlich.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Celle und im Landkreis Celle: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in gut einer Stunde bei dir.</span>',
    ),
    # Ortsseite Dannenberg (Elbe): 32 → 30 Wörter
    4755: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Dannenberg und der Samtgemeinde Elbtalaue – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in rund 35 Minuten bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Dannenberg und der Samtgemeinde Elbtalaue: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in rund 35 Minuten bei dir.</span>',
    ),
    # Ortsseite Ebstorf: 29 → 28 Wörter
    4759: (
        'ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Ebstorf und der Samtgemeinde Bevensen-Ebstorf – mechanisch, elektronisch oder beides. Unser Sitz in Bad Bevensen liegt eine Viertelstunde entfernt.',
        '<span style="font-weight: 700;">ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Ebstorf und der Samtgemeinde Bevensen-Ebstorf: mechanisch, elektronisch oder kombiniert – eine Viertelstunde von unserem Sitz in Bad Bevensen.</span>',
    ),
    # Ortsseite Gifhorn: 35 → 33 Wörter
    4763: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Gifhorn und im Landkreis Gifhorn – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir über die B4 in gut einer Stunde bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Gifhorn und im Landkreis Gifhorn: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus über die B4 in gut einer Stunde bei dir.</span>',
    ),
    # Ortsseite Hitzacker (Elbe): 31 → 29 Wörter
    4767: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Hitzacker und der Elbtalaue – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in rund 35 Minuten bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Hitzacker und der Elbtalaue: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in rund 35 Minuten bei dir.</span>',
    ),
    # Ortsseite Lüchow (Wendland): 33 → 31 Wörter
    4771: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Lüchow und im Landkreis Lüchow-Dannenberg – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in rund 45 Minuten in der Kreisstadt.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Lüchow und im Landkreis Lüchow-Dannenberg: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in rund 45 Minuten in der Kreisstadt.</span>',
    ),
    # Ortsseite Wieren: 31 → 30 Wörter
    4775: (
        'ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Wieren, Wrestedt und der Samtgemeinde Aue – mechanisch, elektronisch oder beides. Unser Sitz in Bad Bevensen liegt rund 25 Minuten entfernt.',
        '<span style="font-weight: 700;">ProVision Infra plant, montiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Wieren, Wrestedt und der Samtgemeinde Aue: mechanisch, elektronisch oder kombiniert – rund 25 Minuten von unserem Sitz in Bad Bevensen.</span>',
    ),
    # Ortsseite Winsen (Luhe): 40 → 34 Wörter
    4779: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Winsen (Luhe) und im Landkreis Harburg – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir über die A39 in rund 50 Minuten bei dir, das Erstgespräch ist unverbindlich.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Winsen (Luhe) und im Landkreis Harburg: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus über die A39 in rund 50 Minuten bei dir.</span>',
    ),
    # Ortsseite Wittingen: 32 → 30 Wörter
    4783: (
        'ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Wittingen und im Nordkreis Gifhorn – mechanisch, elektronisch oder kombiniert. Von Bad Bevensen aus sind wir in rund 45 Minuten bei dir.',
        '<span style="font-weight: 700;">ProVision Infra plant, installiert und betreut Schließanlagen, Zutrittskontrolle und Videoüberwachung in Wittingen und im Nordkreis Gifhorn: mechanisch, elektronisch oder kombiniert – von Bad Bevensen aus in rund 45 Minuten bei dir.</span>',
    ),
}

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def anwenden(data, seite=31):
    alt, neu = TEXTE[int(seite)]
    by = {e["id"]: e for e in walk(data["elements"])}
    h1 = by["9dcea29"]["settings"]; pad = h1["_padding_mobile"]
    assert pad.get("bottom") in ("10", 10), pad
    pad["bottom"] = "18"
    sub = by["e429076"]["settings"]
    assert sub["title"].count(alt) == 1, "Absatztext nicht gefunden"
    sub["title"] = sub["title"].replace(alt, neu)
    return data

if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    seite = sys.argv[3] if len(sys.argv) > 3 else 31
    data = anwenden(json.loads(pathlib.Path(src).read_text(encoding="utf-8")), seite)
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    print("Hero angepasst:", dst)
