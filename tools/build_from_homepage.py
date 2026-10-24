#!/usr/bin/env python3
"""
Baut die Kamera-Landingpage aus den Original-Bausteinen der Startseite (provision-infra.de) zusammen.

Quelle:   elementor/quelle-startseite.json   (Elementor-Daten der Startseite, per WordPress-Export gelesen)
Medien:   elementor/medien.json              (IDs/URLs der hochgeladenen Kamera-Medien)
Ausgabe:  elementor/kamera-seite.elements.json       – Elemente + Seiteneinstellungen (zum Speichern über den Editor)
          elementor/landingpage-kamerasysteme.json   – dieselbe Seite als importierbare Elementor-Vorlage

Jeder Abschnitt ist eine Kopie eines Startseiten-Abschnitts; nur Texte, Video, Bilder, Icons und die
Anzahl der Slides/Zeilen werden geändert. Reihenfolge (20.10.): Header, Hero, Video-Rahmen + drei Punkte, Glas-Logo-Teil
(Pain-Karten), Kundenstimmen, Stell dir mal vor, Und genau das wird möglich, So arbeiten wir, Ablauf, Gründer, Technik,
Standort, FAQ, Partner, Footer. Dadurch stimmen Schriften, Farben, Abstände,
Animationen, Header und Footer exakt mit der Startseite überein.

Aufruf: python3 tools/build_from_homepage.py
"""
import copy, hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
H = json.loads((ROOT / "elementor" / "quelle-startseite.json").read_text(encoding="utf-8"))
MEDIA = json.loads((ROOT / "elementor" / "medien.json").read_text(encoding="utf-8"))
SITE = "https://provision-infra.de"

# ---------------------------------------------------------------- Hilfsfunktionen
_n = [0]
def new_id():
    _n[0] += 1
    return hashlib.md5(f"kamera-seite-{_n[0]}".encode()).hexdigest()[:7]

def clone(el):
    return copy.deepcopy(el)

def reid(el):
    el["id"] = new_id()
    for c in el.get("elements", []):
        reid(c)
    return el

def find(el, eid):
    if el["id"] == eid:
        return el
    for c in el.get("elements", []):
        r = find(c, eid)
        if r:
            return r
    return None

def must(el, eid):
    r = find(el, eid)
    assert r is not None, f"Element {eid} nicht gefunden"
    return r

def box(t, r, b, l, unit="px"):
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}

def container(settings, elements=None):
    s = {"content_width": "full"}
    s.update(settings)
    return {"id": new_id(), "elType": "container", "settings": s, "elements": elements or [], "isInner": True}

def hide_all_but_mobile():
    return {"hide_widescreen": "hidden-widescreen", "hide_desktop": "hidden-desktop", "hide_laptop": "hidden-laptop",
            "hide_tablet_extra": "hidden-tablet_extra", "hide_tablet": "hidden-tablet"}

def svg_icon(media_id, url):
    return {"value": {"url": url, "id": media_id}, "library": "svg"}

# ---------------------------------------------------------------- Texte
# Fester Zeilenumbruch nach „Gebäude“: „mit Kamera- & Videoüberwachung“ steht immer in der zweiten Zeile (ohne Gedankenstrich)
HERO_H1 = '<span style="font-weight: 700;">Wir schützen dein Unternehmen</span><br>mit Kamera- &amp; Videoüberwachung'
HERO_SUB = ('Ein einziger Einbruch kostet dich schnell zehntausende Euro. Und oft bleibt es nicht bei einem. <br>\n<br>\n'
            'ProVision Infra plant und installiert deine Kamera- und Videoüberwachung. Du siehst jederzeit per App, '
            'was auf deinem Gelände passiert, und hast im Ernstfall Aufnahmen, die etwas beweisen.')

# Drei Punkte neben dem Video-Rahmen (wie auf der Startseite: Ausgangslage, Folgen, Lösung). Icon-Schlüssel: HOME_* = Icon der
# Startseite (UNLOCK = offenes Schloss, WARN = Warndreieck, KEY = Schlüssel), ICON1-5 = Kamera-Icons aus icons.json.
PUNKTE = [
    ("HOME_UNLOCK", "Solange nichts passiert, denkt kaum jemand an Kameras."),
    ("HOME_WARN", "Erst nach dem Einbruch wird klar, was fehlt. Ohne verwertbare Aufnahmen hat die Polizei nichts in der Hand, "
                  "und die Versicherung verlangt Belege, die du nicht liefern kannst. Der Schaden bleibt an dir hängen."),
    ("ICON3", "Mit einer Videoüberwachung von ProVision Infra siehst du jederzeit per App, was auf deinem Gelände passiert. "
              "Dein Handy meldet sich bei Bewegung, und im Ernstfall hast du Aufnahmen, mit denen Polizei und Versicherung arbeiten können."),
]

SLIDER_H = 'Technik, <span style="font-weight: 700; ">die wir verbauen</span>'

# Glas-Logo-Abschnitt: links der mitlaufende Text, rechts die Karten. Jede Karte wie auf der Startseite:
# Situation („… wenn“), Verlauf, hervorgehobene Folge; die letzte Karte zusätzlich mit Hinweiszeile (Glühbirne).
PAIN_H = 'Was ohne Kameras <span style="font-weight: 700; ">auf deinem Gelände passiert?</span>'
PAIN_INTRO = '<p>Fünf Situationen, die jeden Betrieb treffen können. Ohne Kameras passiert Folgendes, wenn …</p>'
PAIN = [   # (Situation, Verlauf, Folge, Hinweiszeile oder None)
    ("… nachts jemand über den Zaun steigt,",
     "bemerkt das niemand. Der Täter hat Stunden Zeit, bis morgens der Erste aufschließt.",
     "Werkzeug und Ware sind dann längst weg, und der Betrieb steht am nächsten Morgen still. Ein fünfstelliger Schaden ist schnell erreicht.",
     None),
    ("… die Polizei nach Aufnahmen fragt,",
     "hast du nichts in der Hand. Ohne Bilder gibt es keine Täterbeschreibung, und das Verfahren wird eingestellt.",
     "Wer einmal unbemerkt reinkam, kennt jetzt den Weg und kommt wieder.",
     None),
    ("… Ware aus dem Lager verschwindet,",
     "weißt du nicht, ob es ein Einbruch war oder jemand aus dem eigenen Haus. Der Verdacht trifft alle, auch die Falschen.",
     "Inventurdifferenzen laufen so über Jahre, Monat für Monat, ohne dass du den Grund je erfährst.",
     None),
    ("… jemand nachts Fahrzeuge zerkratzt oder die Fassade besprüht,",
     "wiederholt sich das. Ohne Kamera gibt es keine Abschreckung und keinen Verursacher.",
     "Jede Reparatur zahlst du selbst. Und beim nächsten Mal wieder.",
     None),
    ("… die Versicherung den Schaden prüft,",
     "will sie wissen, wann und auf welchem Weg jemand reinkam. Ohne Nachweis kürzt sie die Leistung oder lehnt ab.",
     "Den gestohlenen Bestand und die aufgebrochene Tür zahlst du dann aus eigener Tasche.",
     "Selbst mit Versicherung musst du beweisen, dass es ein Einbruch war. Ohne Aufnahmen steht nur dein Wort."),
]

# „Stell dir mal vor …“: acht Kästen (Desktop links 1 bis 4, rechts 5 bis 8; Handy untereinander) um die Kamera-Animation
VORSTELLUNG = [
    "Du siehst nachts auf dem Handy, wer gerade auf deinem Hof steht.",
    "Dein Handy meldet sich, sobald sich jemand am Zaun oder am Lager bewegt.",
    "Nach einem Einbruch hat die Polizei innerhalb von Minuten scharfe Aufnahmen.",
    "Die Versicherung bekommt den Nachweis, den sie braucht, und zahlt.",
    "Inventurdifferenzen haben plötzlich ein Datum und ein Gesicht.",
    "Wer sprühen oder zerkratzen will, sieht die Kamera und zieht weiter.",
    "Tore und Einfahrten sind rund um die Uhr im Blick, auch wenn du im Urlaub bist.",
    "Falsche Anschuldigungen klärst du mit einem Klick auf die Aufzeichnung.",
]
# Icons der acht Kästen (gleiche Zuordnung im Computer- und im Handy-Abschnitt)
VORSTELLUNG_ICONS = ["ICON3", "HOME_WARN", "ICON5", "HOME_DOKUMENT", "ICON1", "ICON2", "HOME_CLOUD_HAUS", "HOME_X"]

# „Und genau das wird möglich mit ProVision Infra“
MOEGLICH_H = 'Mit Kamera- und Videoüberwachung von ProVision Infra <span style="font-weight: 700; ">teure Schäden verhindern</span>'
MOEGLICH_T = ('<p>Bei ProVision Infra planen und installieren wir eine Videoüberwachung,<br />die nachts und am Wochenende hinsieht, '
              'wenn niemand im Betrieb ist,<br />und dir im Ernstfall Aufnahmen liefert, die etwas beweisen.</p>'
              '<p>Dafür setzen wir die Kameras an die Stellen, an denen jemand ungesehen aufs Gelände kommt. '
              'Live-Bild und Aufzeichnung siehst du per App auf dem Handy.</p>')

# Schwebender Teil nach dem Glas-Logo-Abschnitt (Format wie „ProVision Infra installiert dir genau das, damit du“)
ARBEIT_H = 'So arbeiten wir'
ARBEIT = [
    "Jede Kamera planen wir nach einer Begehung vor Ort. Im Ernstfall zeigt sie den Täter, nicht den Parkplatz.",
    "Aufzeichnung und App sind eingerichtet, bevor wir vom Hof fahren. Dein Handy schlägt ab dem ersten Tag Alarm.",
    "Übergeben wird erst, wenn du nachts Gesichter erkennst. Das Ergebnis bekommst du schriftlich.",
]

STEPS = {
    "Erstgespräch": "Ein kurzes Telefonat: Was ist passiert, oder was soll nie passieren? Du bekommst eine erste ehrliche Einschätzung.",
    "Termin vor Ort": "Wir gehen mit dir über das Gelände und suchen die Stellen, an denen jemand ungesehen reinkommt. Den Kostenrahmen nennen wir dir noch vor Ort.",
    "Planung deines Kamerasystems": "Du bekommst ein Konzept mit Kamerastandorten und ein Angebot, das zu deinem Budget passt. Dann entscheidest du.",
    "Umsetzung": "Die Kameras montieren wir, Aufzeichnung und App richten wir komplett ein. Du musst nichts selbst konfigurieren.",
    "Übergabe & Betreuung": "Gemeinsam prüfen wir, ob die Anlage leistet, was vereinbart war, und halten das schriftlich fest. Danach bleiben wir erreichbar.",
}

KONTAKT_TEXT = ('<p>Im Gespräch klären wir, welche Bereiche du im Blick haben willst und wo jemand ungesehen aufs Gelände kommt. '
                'Dazu bekommst du eine erste Einschätzung zu Aufwand und Kosten.</p>')

FAQ_H_DESKTOP = 'Häufige Fragen zu Kamera- &amp; \nVideoüberwachung mit <b>ProVision Infra</b>'
FAQ_H_MOBILE = 'Häufige Fragen zu Kamera- &amp; \nVideoüberwachung mit <br><b>ProVision Infra</b>'
FAQ = [
    ("Darf ich mein Firmengelände überhaupt per Kamera überwachen?",
     "Ja, innerhalb klarer Regeln. Erlaubt ist dein eigenes Gelände samt Zugängen, nicht der Gehweg oder das Nachbargrundstück. Mitarbeiter müssen informiert sein, ein Hinweisschild ist Pflicht. Wir planen die Kamerawinkel entsprechend und geben dir Schilder und Unterlagen mit."),
    ("Wie lange dauert die Installation einer Videoüberwachung?",
     "Vier bis acht Kameras sind meist an einem Tag montiert und eingerichtet. Größere Objekte planen wir in Abschnitten, damit dein Betrieb weiterläuft."),
    ("Kann ich die Kamerabilder auf dem Handy sehen?",
     "Ja. In der App siehst du Live-Bild und Aufzeichnungen und wirst bei Bewegung benachrichtigt. Die Einrichtung übernehmen wir und zeigen dir alles am Gerät."),
    ("Was passiert bei Stromausfall oder Internetstörung?",
     "Fällt das Internet aus, fehlt nur der Fernzugriff. Die Aufzeichnung läuft auf dem Rekorder im Gebäude weiter. Gegen Stromausfall sichern wir Rekorder und Kameras auf Wunsch mit einer Notstromversorgung ab."),
    ("Was kostet eine Videoüberwachung für mein Unternehmen?",
     "Das hängt von der Zahl der Kameras und den Wegen für die Verkabelung ab. Einen ersten Rahmen bekommst du im Erstgespräch, einen verbindlichen Preis nach dem Termin vor Ort."),
    ("Sind meine Aufnahmen vor fremdem Zugriff geschützt?",
     "Die Aufnahmen bleiben auf deinem Rekorder im Gebäude, nicht in einer fremden Cloud. Zugriff hat nur, wer von dir freigegeben ist. Wir richten Zugänge und Verschlüsselung ein und halten die Software aktuell."),
    ("In welcher Region installiert ProVision Infra Videoüberwachung?",
     "Unser Sitz ist Bad Bevensen bei Lüneburg. Unterwegs sind wir vor allem im Raum Hamburg, Hannover und Niedersachsen, bei größeren Projekten auch bundesweit."),
]

# Icons aus der Mediathek (SVG). Zuordnung siehe ICONS unten; Werte können jederzeit im Editor getauscht werden.
ICONS = {
    "ICON1": (2066, f"{SITE}/wp-content/uploads/2026/06/Frame-9-1-1.svg"),   # Warnung
    "ICON2": (2060, f"{SITE}/wp-content/uploads/2026/06/Frame-9-1.svg"),     # Schlüssel
    "ICON3": (2065, f"{SITE}/wp-content/uploads/2026/06/Frame-9-2.svg"),     # Entsperrt
    "ICON4": (2067, f"{SITE}/wp-content/uploads/2026/06/CheckCircle.svg"),   # Haken
    "ICON5": (2068, f"{SITE}/wp-content/uploads/2026/06/Quote.svg"),         # Zitat/Protokoll
}
ICON_OVERRIDES = json.loads((ROOT / "elementor" / "icons.json").read_text(encoding="utf-8")) if (ROOT / "elementor" / "icons.json").exists() else {}
for k, v in ICON_OVERRIDES.items():
    ICONS[k] = (v["id"], v["url"])

VIDEO, POSTER, PRODUKTE = MEDIA["video"], MEDIA["poster"], MEDIA["produkte"]
VIDEO_DESKTOP = MEDIA.get("video_4k", VIDEO)        # Desktop-Hero: 4K-Version (KI-hochskaliert), falls vorhanden
VIDEO_MOBILE = MEDIA.get("video_mobile", VIDEO)     # Handy-Block: kleinere Version

page = []

# ---------------------------------------------------------------- 1) Header (Original, eigenes Menü)
# Die Kopfleiste ist die der Startseite. Nur das Menü ist ein eigenes WordPress-Menü (medien.json: menue_header, Design → Menüs
# „Kamerasysteme Header“): erster Eintrag „Durch Videoüberwachung teure Schäden verhindern“ → #moeglich, „So arbeiten wir
# zusammen“ → #arbeitsweise, „Über uns“ → #Über, „FAQ“ → #FAQ, alle auf dieser Seite. Das Menü „main“ der Startseite bleibt unberührt.
header = clone(H[0])
MENUE = MEDIA["menue_header"]
must(header, "2a487ab")["settings"]["menu"] = MENUE["slug"]
page.append(header)

# ---------------------------------------------------------------- 2) Hero (Original, neue Texte, neues Video)
hero = clone(H[1])
h1 = must(hero, "9dcea29")["settings"]
h1["title"] = HERO_H1
# Überschrift größer als auf der Startseite. Die zweite Zeile („mit Kamera- & Videoüberwachung“, Poppins 400,
# ca. 18,4 em breit) muss in jeder Breite in EINE Zeile passen; deshalb ist die Textbox breiter als auf der Startseite
# und auf Tablet/Handy (Box skaliert mit der Bildschirmbreite) wird die Größe per min()-Formel gedeckelt.
h1["typography_font_size"] = {"unit": "px", "size": 52, "sizes": []}                      # ab 1441 px: zweite Zeile endet vor dem Schloss im Video (bei 1536 px max. 52 px)
h1["typography_font_size_laptop"] = {"unit": "px", "size": 50, "sizes": []}               # 1281-1440 px, Box 940 px
h1["typography_font_size_tablet_extra"] = {"unit": "px", "size": 44, "sizes": []}         # 1025-1280 px, Box 940 px
h1["typography_font_size_tablet"] = {"unit": "custom", "size": "min(36px, 4vw - 1.5px)", "sizes": []}   # 768-1024 px: 29 px bei 768, 36 px ab 940
h1["typography_font_size_mobile"] = {"unit": "custom", "size": "min(28px, 5.9vw - 2px)", "sizes": []}   # bis 767 px: 1. Zeile (fett, „… dein Unternehmen“) bleibt einzeilig
h1["typography_line_height_tablet_extra"] = {"unit": "px", "size": 53, "sizes": []}
h1["typography_line_height_tablet"] = {"unit": "em", "size": 1.25, "sizes": []}
h1["typography_line_height_mobile"] = {"unit": "em", "size": 1.23, "sizes": []}
h1["_element_custom_width"] = {"unit": "%", "size": 88, "sizes": []}
h1["_element_custom_width_laptop"] = {"unit": "px", "size": 940, "sizes": []}
must(hero, "e429076")["settings"]["title"] = HERO_SUB
hs = hero["settings"]
hs["background_video_link"] = VIDEO_DESKTOP["url"]
# Kameras im Video frei sichtbar, knapp über der Headline: Text rutscht nach unten, am Desktop bei gleicher Hero-Höhe
# (oben +80, unten -80), damit der Videoausschnitt gleich bleibt. Laptop/Tablet: oben +70, Höhe darf wachsen.
hs["padding"] = box(280, 20, 20, 20)
# Schloss im Video neben statt hinter der Headline: ab 1441 px über die Schriftgröße (52 px), bei 1025-1440 px über eine
# kleine Verschiebung des Videobilds nach rechts (linke Kante weich ausgeblendet). Elementor zentriert das Video mit
# translate(-50%, -50%).
hs["custom_css"] = (hs.get("custom_css", "") + """
/* Ab 1441 px keine Verschiebung (Tür bleibt an Ort und Stelle); dort endet die Headline mit 52 px vor dem Schloss. */
/* Laptop (1281-1440 px, Headline 50 px): Verschiebung wächst mit kleinerer Breite (26 px bei 1440, 106 px bei 1281) */
@media (min-width: 1281px) and (max-width: 1440px) {
  .elementor-element-0f0c707 video.elementor-background-video-hosted {
    transform: translate(calc(-50% + 746px - 50vw), -50%) !important;
    -webkit-mask-image: linear-gradient(to right, transparent 0, #000 220px);
    mask-image: linear-gradient(to right, transparent 0, #000 220px);
  }
}
/* 1025-1280 px (Headline 44 px): nur so weit wie nötig (5 px bei 1280, 132 px bei 1025) */
@media (min-width: 1025px) and (max-width: 1280px) {
  .elementor-element-0f0c707 video.elementor-background-video-hosted {
    transform: translate(calc(-50% + max(0px, 645px - 50vw)), -50%) !important;
    -webkit-mask-image: linear-gradient(to right, transparent 0, #000 220px);
    mask-image: linear-gradient(to right, transparent 0, #000 220px);
  }
}""")
hs["padding_laptop"] = box(220, 40, 50, 40)
hs["padding_tablet"] = box(220, 20, 50, 20)
hs["background_video_start"] = ""
hs["background_video_end"] = ""            # ganzes Video abspielen, danach stehen bleiben (background_play_once bleibt "yes")
hs["background_play_on_mobile"] = ""       # mobil einfarbig (eigenes Custom-CSS des Hero), Video folgt als Block unter dem Button
hs.pop("background_video_fallback", None)   # kein Ersatzbild: es würde mobil hinter dem Text erscheinen (einfarbig per Custom-CSS des Hero)
page.append(hero)

# ---------------------------------------------------------------- 3) Mobiler Video-Block (Original-Block der Startseite, nur mobil)
mvideo = clone(H[2])
ms = mvideo["settings"]
ms["background_video_link"] = VIDEO_MOBILE["url"]
ms["background_video_start"] = ""
ms["background_video_end"] = ""
ms["background_video_fallback"] = {"url": POSTER["url"], "id": POSTER["id"], "size": "", "alt": "", "source": "library"}
for k in list(ms.keys()):
    if k.startswith("_transform_") or k.startswith("hide_"):
        del ms[k]
ms.update(hide_all_but_mobile())
ms["_title"] = "Hero-Video (nur mobil)"
# Bildausschnitt: Video rechtsbündig, Blockhöhe so, dass Kameras und Tür komplett im Bild sind (Video ist 16:9).
ms["min_height_mobile"] = {"unit": "px", "size": 330, "sizes": []}
ms["background_position_mobile"] = "center right"   # Ersatzbild (bis das Video läuft) mit demselben Ausschnitt wie das Video
ms["custom_css"] = """@media (min-width: 475px) and (max-width: 767px) {
selector { min-height: 470px; }
}
@media (max-width: 767px) {
selector video.elementor-background-video-hosted {
  object-position: 100% 50% !important;
}
}"""
page.append(mvideo)

# ---------------------------------------------------------------- 4) Mobile Bewertungszeile (Original)
page.append(clone(H[3]))

# ---------------------------------------------------------------- 5) Video-Rahmen + drei Punkte (Original-Abschnitt direkt unter dem Hero)
# Kopie des Startseiten-Abschnitts unter dem Hero: links der gelb umrandete Rahmen mit dem Unternehmensfilm (Vimeo,
# Vorschaubild und Play-Button wie auf der Startseite), rechts drei Icon-Zeilen. Tablet/Handy: Rahmen oben, Punkte darunter.
# Der schwebende Teil des Originals („… installiert dir genau das, damit du“) folgt weiter unten als eigener Abschnitt.
HOME_ICONS = {"HOME_KEY": must(H[4], "087e23e")["settings"]["selected_icon"],
              "HOME_WARN": must(H[4], "3e8f2d1")["settings"]["selected_icon"],
              "HOME_UNLOCK": must(H[4], "63855c5")["settings"]["selected_icon"],
              "HOME_X": must(H[6], "75e83d7")["settings"]["selected_icon"],
              "HOME_DOKUMENT": must(H[9], "4199019")["settings"]["selected_icon"],
              "HOME_CLOUD_HAUS": must(H[9], "8b077e4")["settings"]["selected_icon"]}
def icon_for(key):
    return clone(HOME_ICONS[key]) if key in HOME_ICONS else svg_icon(*ICONS[key])

punkte = clone(H[4])
punkte["elements"] = [e for e in punkte["elements"] if e["id"] == "7dfcfda"]
for wid, iid, (key, text) in zip(("d05eab3", "7df04ae", "d38dec5"), ("087e23e", "3e8f2d1", "63855c5"), PUNKTE):
    w = must(punkte, wid)["settings"]
    if "editor" in w:
        w["editor"] = f"<p>{text}</p>"
    else:
        w["title"] = text
    w["_title"] = text[:40]
    must(punkte, iid)["settings"]["selected_icon"] = icon_for(key)
# Im Rahmen kein Video (Wunsch vom 20.10.), sondern das Logo mit Link zur Startseite
LOGO = MEDIA["logo"]
frame = must(punkte, "0a52747")
frame["elements"] = [{"id": new_id(), "elType": "widget", "widgetType": "image", "elements": [], "isInner": False, "settings": {
    "image": {"url": LOGO["url"], "id": LOGO["id"], "size": "", "alt": "ProVision Infra GmbH", "source": "library"},
    "image_size": "full", "align": "center", "link_to": "custom",
    "link": {"url": SITE + "/", "is_external": "", "nofollow": "", "custom_attributes": ""},
    # Breite per CSS: das Bild steckt wegen des Links in einem <a>; die Prozent-Breite des Bild-Elements greift dort nicht
    # Breite per CSS auf dem Element selbst: das Bild steckt wegen des Links in einem <a>, und als Flex-Kind des zentrierten
    # Rahmens schrumpft das Element sonst auf die natürliche Bildbreite
    "custom_css": ("selector { width: 88%; max-width: 88%; }\n"
                   "selector > a { display: block; width: 100%; }\n"
                   "selector img { width: 100%; height: auto; }\n"
                   "@media (max-width: 1024px) { selector { width: 72%; max-width: 72%; } }\n"
                   "@media (max-width: 767px) { selector { width: 86%; max-width: 86%; } }"),
    "_title": "Logo mit Link zur Startseite"}}]
frame["settings"].update({"_title": "Logo-Rahmen", "flex_direction": "column", "flex_justify_content": "center", "flex_align_items": "center",
                          "padding": box(40, 24, 40, 24), "padding_tablet": box(30, 20, 30, 20), "padding_mobile": box(28, 14, 28, 14),
                          "min_height": {"unit": "px", "size": 320, "sizes": []}, "min_height_tablet": {"unit": "px", "size": 240, "sizes": []},
                          "min_height_mobile": {"unit": "px", "size": 190, "sizes": []}})
must(punkte, "478e545")["settings"]["_title"] = "Drei Punkte"
punkte["settings"].update({"_element_id": "digitalen", "_title": "Video und drei Punkte"})   # Anker des ersten Menüpunkts
reid(punkte)
page.append(punkte)

# ---------------------------------------------------------------- 6) Produkt-Slider – Kopie des Kundenstimmen-Sliders mit Bildern (steht weiter unten)
slider = clone(H[5])
must(slider, "556df520")["settings"]["title"] = SLIDER_H
row = must(slider, "55a57e52")
row["elements"] = [e for e in row["elements"] if e["id"] != "63020976"]      # Bewertungszeile entfernen
car = must(slider, "2b91cf92")
slide_tpl = must(slider, "547b551e")
car["settings"]["carousel_items"] = []
car["settings"]["pause_on_hover"] = "no"          # Produktbilder laufen auch am Computer durch, auch wenn die Maus darüber steht
car["settings"]["pause_on_interaction"] = "no"    # ... und nach einem Klick auf die Pfeile weiter
car["elements"] = []
for i, img in enumerate(PRODUKTE, 1):
    item_id = new_id()
    car["settings"]["carousel_items"].append({"slide_title": f"Produktbild {i}", "_id": item_id})
    s = clone(slide_tpl)
    s["settings"].pop("custom_css", None)
    s["settings"].pop("background_color", None)
    s["settings"]["padding"] = box(0, 0, 0, 0)
    s["settings"]["_title"] = img.get("alt", f"Produktbild {i}")
    s["elements"] = [{
        "id": new_id(), "elType": "widget", "widgetType": "image", "elements": [], "isInner": False,
        "settings": {
            "image": {"url": img["url"], "id": img["id"], "size": "", "alt": img.get("alt", f"Produktbild {i}"), "source": "library"},
            "image_size": "large", "align": "center",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "image_border_radius": box(25, 25, 25, 25),
            "_title": f"Produktbild {i}",
        },
    }]
    car["elements"].append(s)
def slider_spacing(sec):
    """Pfeile und Punkte liegen 136 px unter dem Carousel (Tablet/Handy): Sektion unten entsprechend auspolstern."""
    sec["settings"]["padding_tablet"] = {"unit": "px", "top": "50", "right": "20", "bottom": "90", "left": "50", "isLinked": False}
    sec["settings"]["padding_mobile"] = {"unit": "px", "top": "10", "right": "10", "bottom": "90", "left": "10", "isLinked": False}
slider_spacing(slider)
slider["settings"]["_element_id"] = "produkte"
slider["settings"]["_title"] = "Produkt-Slider"
reid(slider)

# ---------------------------------------------------------------- 7) Glas-Logo-Abschnitt: mitlaufender Text links, Pain-Karten rechts
sec_tpl = H[4]
heading_tpl = must(H[5], "556df520")
text_tpl = must(H[15], "4e4df2b")
card_tpl = must(H[6], "7d36acb")      # Karte der Startseite: 2-px-Rahmen, beim Hover gelb mit Glow
card_tip_tpl = must(H[6], "067ce5f")  # letzte Karte der Startseite: zusätzlich Trennlinie + Hinweiszeile mit Glühbirne
tile_tpl = must(H[4], "3f048a0")      # Icon-Kachel (das SVG bringt die gelbe Fläche mit)
btn_tpl = must(H[12], "c7ed38d")

d_heading = clone(heading_tpl); d_heading["settings"]["title"] = PAIN_H; d_heading["settings"]["_title"] = "Was ohne Kameras passiert"
d_heading["settings"]["_element_custom_width_mobile"] = {"unit": "%", "size": 100, "sizes": []}   # mittig auf dem Handy
d_heading["settings"]["_flex_align_self"] = "center"
d_intro = clone(text_tpl)
d_intro["settings"].update({"editor": PAIN_INTRO, "align": "center", "align_mobile": "center",
                            "typography_font_size": {"unit": "px", "size": 20, "sizes": []},          # etwas größer (Wunsch vom 20.10.)
                            "typography_font_size_laptop": {"unit": "px", "size": 19, "sizes": []},
                            "typography_font_size_tablet_extra": {"unit": "px", "size": 18, "sizes": []},
                            "typography_font_size_tablet": {"unit": "px", "size": 18, "sizes": []},
                            "typography_font_size_mobile": {"unit": "px", "size": 17, "sizes": []},
                            "_element_custom_width": {"unit": "%", "size": 70, "sizes": []},
                            "_element_custom_width_tablet": {"unit": "%", "size": 100, "sizes": []},
                            "_flex_align_self": "center", "_margin": box(10, 0, 30, 0), "_title": "Einleitung"})

small = {"unit": "px", "size": 14, "sizes": []}
cards = []
for title, body, pain, tip in PAIN:
    card = clone(card_tip_tpl if tip else card_tpl)
    if tip:   # Rahmen (2 px) und Hintergrund wie die anderen Karten (die letzte Karte der Startseite hat 1 px und keinen Hintergrund)
        for k in ("border_width", "background_background", "background_color"):
            card["settings"][k] = clone(card_tpl["settings"][k])
    row = card["elements"][0]                                   # Zeile: Kachel + Text (bricht auf Tablet/Handy um, Handy zentriert)
    _, textcol = row["elements"]
    tile = clone(tile_tpl)
    tile["elements"] = [tile["elements"][0]]
    tile["elements"][0]["settings"]["selected_icon"] = icon_for("HOME_X")   # wie auf der Startseite: X-Symbol bei jeder Pain-Karte
    tile["elements"][0]["settings"]["_title"] = "Icon"
    tile["settings"].update({"width": {"unit": "%", "size": 10.34, "sizes": []},
                             "width_tablet": {"unit": "px", "size": 72, "sizes": []},
                             "width_mobile": {"unit": "px", "size": 72, "sizes": []},
                             "padding": box(0, 0, 0, 0), "padding_tablet": box(0, 0, 0, 0), "padding_mobile": box(0, 0, 0, 0),
                             "_title": "Kachel"})
    t_title = next(e for e in textcol["elements"] if e.get("widgetType") == "heading")
    t_body = next(e for e in textcol["elements"] if e.get("widgetType") == "text-editor")
    pill = next(e for e in textcol["elements"] if e["elType"] == "container" and e["settings"].get("_title") == "Frame 2147224700")
    t_title["settings"].update({"title": title, "_title": title, "header_size": "h3"})
    t_body["settings"].update({"editor": f"<p>{body}</p>", "_title": "Text", "typography_font_size_tablet": small})
    pill["elements"][0]["settings"].update({"editor": f"<p>{pain}</p>", "_title": "Folge", "typography_font_size_tablet": small})
    pill["settings"]["_title"] = "Folge-Box"
    if tip:
        tip_row = next(e for e in textcol["elements"] if e["elType"] == "container" and e["settings"].get("_title") == "Frame 2147224854")
        tip_text = next(e for e in tip_row["elements"] if e.get("widgetType") == "text-editor")
        tip_text["settings"].update({"editor": f"<p>{tip}</p>", "_title": "Hinweis", "typography_font_size_tablet": small})
        tip_row["settings"]["_title"] = "Hinweiszeile"
    row["elements"] = [tile, textcol]
    row["settings"]["_title"] = "Zeile"
    textcol["settings"]["_title"] = "Text"
    card["settings"]["_title"] = title
    cards.append(reid(card))
col = container({"flex_direction": "column",
                 "width": {"unit": "px", "size": 900, "sizes": []},
                 "width_tablet": {"unit": "%", "size": 100, "sizes": []},
                 "width_mobile": {"unit": "%", "size": 100, "sizes": []},
                 "flex_gap": {"column": "20", "row": "20", "isLinked": True, "unit": "px", "size": 20},
                 "flex_gap_mobile": {"column": "16", "row": "16", "isLinked": True, "unit": "px", "size": 16},
                 "padding": box(0, 0, 0, 0), "_title": "Karten"}, cards)

# Nur der Button, kein Einleitungstext davor (Wunsch vom 16.10.)
cta_btn = clone(btn_tpl); cta_btn["settings"]["align"] = "center"; cta_btn["settings"]["_title"] = "Erstgespräch"
cta = container({"flex_direction": "column", "flex_align_items": "center",
                 "padding": box(30, 0, 0, 0), "_title": "Erstgespräch"}, [reid(cta_btn)])

# Zweispaltig wie der Startseiten-Abschnitt „Warum immer mehr KMUs …“ (H[6]): links der Text, der am Computer beim
# Scrollen stehen bleibt, bis die Karten rechts zu Ende sind (Elementor-Sticky, „an Eltern-Container“), rechts die
# Karten. Glas-Logo als Hintergrund-Overlay der Zeile (Computer und Handy wie auf der Startseite, Tablet ohne). Auf Tablet und Handy stehen Text und Karten untereinander, zentriert, ohne Overlays.
home_row = must(H[6], "f86d566")
home_left, home_right = must(H[6], "8c98faa"), must(H[6], "b72e86b")
full = lambda: {"unit": "%", "size": 100, "sizes": []}
for w in (d_heading, d_intro):
    w["settings"].pop("_flex_align_self", None)
    w["settings"].update({"align": "left", "align_tablet": "center", "align_mobile": "center",
                          "_element_custom_width": full(), "_element_custom_width_tablet": full(), "_element_custom_width_mobile": full()})
d_intro["settings"]["_margin"] = box(0, 0, 0, 0)
col["settings"]["width"] = full()
left = clone(home_left)                      # 40 %, sticky top (widescreen/desktop/laptop), sticky_parent = yes
left["elements"] = [reid(d_heading), reid(d_intro)]
left["settings"].update({"width_tablet": full(), "_title": "Text (am Computer sticky)"})
right = clone(home_right)                    # 60 %
right["elements"] = [col, cta]
right["settings"].update({"width_tablet": full(), "_title": "Karten"})
row = clone(home_row)                        # Zeile mit Glas-Logo (Overlay links, 50 % breit, Maus-Effekt)
row["elements"] = [left, right]
row["settings"].update({"flex_direction_tablet": "column", "width": full(),
                        "margin": box(0, 0, 0, 0), "margin_laptop": box(0, 0, 0, 0),
                        "background_overlay_opacity_tablet": {"unit": "px", "size": 0, "sizes": []},
                        # Handy: Glas-V wie auf der Startseite (oben mittig, Deckkraft 0,64); Tablet ohne
                        "background_overlay_opacity_mobile": {"unit": "px", "size": 0.64, "sizes": []},
                        "_title": "Text + Karten"})
diff = {"id": new_id(), "elType": "container", "isInner": False, "settings": clone(sec_tpl["settings"]),
        "elements": [reid(row)]}
# Kein Verlaufs-Overlay am oberen Rand (würde die Überschrift abdunkeln); Hintergrund wie die Seite (wie beim Original H[6]).
diff["settings"].pop("custom_css", None)
diff["settings"].pop("css_classes", None)
for k in [k for k in diff["settings"] if k.startswith("background_")]:
    diff["settings"].pop(k)
diff["settings"].update({"_element_id": "folgen", "_title": "Was ohne Kameras passiert",
                         "padding": box(60, 20, 60, 20), "padding_mobile": box(50, 20, 50, 20),
                         "flex_align_items": "center",
                         "flex_gap": {"column": "20", "row": "20", "isLinked": True, "unit": "px", "size": 20}})
# Hinweis: Der Startseiten-Abschnitt trägt zusätzlich ein gelbes Lichtschein-Overlay (2.png). Es ist dort aber nicht
# sichtbar, weil die Klasse „shadeup“ das Overlay-Pseudo-Element auf einen 30-px-Streifen zusammendrückt. Damit die
# Optik dem sichtbaren Original entspricht, wird es hier bewusst nicht übernommen.
page.append(diff)

# ---------------------------------------------------------------- 8) Kundenstimmen (Original, mit Platz für die Pfeile; nach dem Glas-Logo-Abschnitt)
kunden = clone(H[5])
slider_spacing(kunden)
page.append(kunden)

# ---------------------------------------------------------------- 8b) „Stell dir mal vor …“ (Original-Abschnitte H[7], H[8] Desktop, H[9] Handy)
# Statt Schließzylinder und Türgriff läuft in der Mitte eine eigene Lottie-Animation (Schwenk-Neige-Kamera aus den Produktbildern:
# schwenkt, schwebt, LED blinkt; erzeugt mit tools/kamera_lottie_erzeugen.py, medien.json: kamera_lottie_mobil).
KAMERA_LOTTIE_MOBIL = MEDIA["kamera_lottie_mobil"]      # kompakte Bühne (360 x 520), Computer und Handy

stell = clone(H[7]); stell["settings"]["_title"] = "Stell dir mal vor"
page.append(reid(stell))

stell_d = clone(H[8])
# Desktop/Tablet: Die Startseite zeichnet Rahmen, Icons und Leuchtlinie der acht Kästen in acht Lottie-Dateien an festen Positionen;
# bei anderen Textlängen und Breiten laufen Rahmen und Text auseinander. Hier bekommen die Kästen Rahmen, Icon und das Aufleuchten
# selbst (Vorlage: Handy-Kasten der Startseite), die gelbe Linie zum Kamerakopf zeichnet ein kleines Skript genau von der
# tatsächlichen Kastenkante aus (tools/kamera-linien.html). Die Kamera-Animation steht in der mittleren Spalte.
row_s = must(stell_d, "c1d1015")
left_col, mid_col, right_col = must(stell_d, "b6936eb"), must(stell_d, "a319592"), must(stell_d, "eaa1402")
box_tpl = must(H[9], "65b45ef")          # Handy-Kasten der Startseite: Rahmen 1 px, Icon-Kachel, Text
def make_box(n, text, anim):
    b = clone(box_tpl)
    tile, txt = b["elements"]
    tile["elements"][0]["settings"]["selected_icon"] = icon_for(VORSTELLUNG_ICONS[n - 1])
    tile["elements"][0]["settings"]["_title"] = "Icon"
    tile["settings"]["_title"] = "Kachel"
    txt["settings"].update({"editor": f"<p>{text}</p>", "_title": text[:40],
                            "typography_font_size": {"unit": "px", "size": 14, "sizes": []},
                            "typography_font_size_laptop": {"unit": "px", "size": 13, "sizes": []},
                            "typography_font_size_tablet_extra": {"unit": "px", "size": 12, "sizes": []},
                            "typography_font_size_tablet": {"unit": "px", "size": 11, "sizes": []},
                            "_element_custom_width": {"unit": "%", "size": 74, "sizes": []},
                            "_element_custom_width_tablet": {"unit": "%", "size": 74, "sizes": []}})
    b["settings"].update({"width": {"unit": "px", "size": 400, "sizes": []}, "width_laptop": {"unit": "px", "size": 380, "sizes": []},
                          "width_tablet_extra": {"unit": "px", "size": 330, "sizes": []}, "width_tablet": {"unit": "%", "size": 100, "sizes": []},   # Tablet: volle Spaltenbreite (bei 768 px sonst breiter als die Spalte)
                          "flex_align_items": "center", "padding": box(22, 20, 22, 20), "padding_tablet": box(12, 12, 12, 12),
                          "flex_gap_tablet": {"column": "10", "row": "10", "isLinked": True, "unit": "px", "size": 10},
                          "animation": anim, "_attributes": f"data-pv-box|{n}", "_title": f"Kasten {n}"})
    return reid(b)
left_col["elements"] = [make_box(n, VORSTELLUNG[n - 1], "fadeInLeft") for n in (1, 2, 3, 4)]
right_col["elements"] = [make_box(n, VORSTELLUNG[n - 1], "fadeInRight") for n in (5, 6, 7, 8)]
gap = {"column": "24", "row": "24", "isLinked": True, "unit": "px", "size": 24}
for col, title in ((left_col, "Kästen links"), (right_col, "Kästen rechts")):
    col["settings"].update({"flex_justify_content": "center", "flex_align_items": "center", "flex_gap": gap, "_title": title,
                            "flex_gap_tablet": {"column": "14", "row": "14", "isLinked": True, "unit": "px", "size": 14}})
    col["settings"].pop("_flex_align_self_tablet", None)
mid_col["elements"] = [{"id": new_id(), "elType": "widget", "widgetType": "lottie", "elements": [], "isInner": False, "settings": {
    "source_json": {"url": KAMERA_LOTTIE_MOBIL["url"], "id": KAMERA_LOTTIE_MOBIL["id"], "size": "", "alt": "", "source": "library"},
    "loop": "yes", "trigger": "arriving_to_viewport", "_element_id": "pv-kamera", "_z_index": 3,
    "_element_width": "initial", "_element_custom_width": {"unit": "%", "size": 74, "sizes": []},
    "_element_custom_width_tablet": {"unit": "%", "size": 92, "sizes": []}, "custom_css": "selector svg { overflow: visible; filter: drop-shadow(0 0 26px rgba(251, 201, 27, 0.55)) drop-shadow(0 0 70px rgba(251, 201, 27, 0.3)); }", "_title": "Kamera (schwenkt, LED blinkt)"}}]
mid_col["settings"].update({"flex_justify_content": "center", "flex_align_items": "center", "_title": "Kamera"})
LINIEN_HTML = (ROOT / "tools" / "kamera-linien.html").read_text(encoding="utf-8")
linien = {"id": new_id(), "elType": "widget", "widgetType": "html", "elements": [], "isInner": False, "settings": {
    "html": LINIEN_HTML, "custom_css": "selector { position: absolute; inset: 0; width: 100%; height: 100%; margin: 0; pointer-events: none; z-index: 1; }",
    "_title": "Leuchtlinie zur Kamera"}}
row_s["elements"] = [left_col, mid_col, right_col, linien]
row_s["settings"]["css_classes"] = (row_s["settings"].get("css_classes", "") + " pv-stell").strip()
row_s["settings"]["_title"] = "Kästen + Kamera"
stell_d["elements"] = [e for e in stell_d["elements"] if e["id"] != "b0f015c"]   # Lottie-Container der Startseite entfällt
stell_d["settings"]["_title"] = "Stell dir mal vor (Computer/Tablet)"
page.append(reid(stell_d))

stell_m = clone(H[9])
for wid, text in zip(("196a01d", "95203a8", "b640c54", "b7ef4bd", "8f999b2", "ba5311c", "c325747", "13ec65b"), VORSTELLUNG):
    w = must(stell_m, wid)["settings"]
    if "editor" in w:
        w["editor"] = f"<p>{text}</p>"
    else:
        w["title"] = text
    w["_title"] = text[:40]
for wid, key in zip(("20fb6a9", "be97d3f", "5e4fd62", "4199019", "ac64bd9", "770ea05", "8b077e4", "545759b"), VORSTELLUNG_ICONS):
    must(stell_m, wid)["settings"]["selected_icon"] = icon_for(key)
mcol = must(stell_m, "1f03386")
mcol["elements"] = [{"id": new_id(), "elType": "widget", "widgetType": "lottie", "elements": [], "isInner": False, "settings": {
    "source_json": {"url": KAMERA_LOTTIE_MOBIL["url"], "id": KAMERA_LOTTIE_MOBIL["id"], "size": "", "alt": "", "source": "library"},
    "loop": "yes", "trigger": "arriving_to_viewport", "_element_id": "pv-kamera-mobil",
    "_element_width": "initial", "_element_custom_width": {"unit": "px", "size": 300, "sizes": []},
    "_element_custom_width_mobile": {"unit": "px", "size": 280, "sizes": []}, "custom_css": "selector svg { overflow: visible; filter: drop-shadow(0 0 26px rgba(251, 201, 27, 0.55)) drop-shadow(0 0 70px rgba(251, 201, 27, 0.3)); }", "_title": "Kamera (schwenkt, LED blinkt)"}}]
mcol["settings"].update({"flex_align_items": "center", "flex_justify_content": "center", "flex_align_items_mobile": "center",
                         "min_height_mobile": {"unit": "px", "size": 440, "sizes": []}, "_title": "Kamera"})
stell_m["settings"]["_title"] = "Stell dir mal vor (Handy)"
page.append(reid(stell_m))

# ---------------------------------------------------------------- 8c) „Und genau das wird möglich mit ProVision Infra“ (Original H[10])
# Grafik der Startseite als Hintergrund übernommen, die Person darauf als dunkle Kapuzen-Silhouette (Einbrecher) neu gesetzt
# (tools/einbrecher_silhouette.py).
SZENE, SZENE_MOBIL = MEDIA["szene_bild"], MEDIA["szene_bild_mobil"]
moeglich = clone(H[10])
must(moeglich, "ecdc807")["settings"].update({"title": MOEGLICH_H, "_title": "Überschrift"})
# Vorzeile: „ProVision Infra:“ bleibt zusammen und steht am Handy allein in der zweiten Zeile (geschütztes Leerzeichen)
must(moeglich, "4ae8a09")["settings"].update({"title": "Und genau das wird möglich mit ProVision&nbsp;Infra:", "_title": "Vorzeile"})
must(moeglich, "f085e1b")["settings"].update({"editor": MOEGLICH_T, "_title": "Text"})
ms_ = moeglich["settings"]
ms_["background_image"] = {"url": SZENE["url"], "id": "", "size": "", "alt": "", "source": "library"}   # ohne ID: Elementor ersetzt die URL sonst durch die 2560-px-Kopie („-scaled“)
ms_["background_image_mobile"] = {"url": SZENE_MOBIL["url"], "id": SZENE_MOBIL["id"], "size": "", "alt": "", "source": "library"}
ms_.update({"_element_id": "moeglich", "_title": "Und genau das wird möglich"})
# Keine eingefügten Kameras über der Szene (Wunsch vom 20.10., zweite Runde); die Silhouette bleibt.
page.append(reid(moeglich))

# ---------------------------------------------------------------- 8d) So arbeiten wir – schwebende Kästen (Original: „… installiert dir genau das, damit du“); seit 20.10. abends direkt vor dem Ablauf
arbeit = {"id": new_id(), "elType": "container", "isInner": False, "settings": clone(H[4]["settings"]),
          "elements": [clone(must(H[4], "18e7c8b"))]}
# Der Startseiten-Abschnitt dunkelt am Handy die oberen 100 px mit einem Verlauf ab (Übergang vom Hero). Hier stünde die
# Überschrift darunter und würde grau; deshalb ohne diese Zusatzregel (es bleibt der normale 30-px-Streifen der Klasse shadeup).
arbeit["settings"].pop("custom_css", None)
must(arbeit, "58d331d")["settings"].update({"title": ARBEIT_H, "_title": ARBEIT_H})
for wid, text in zip(("b4a337a", "334a7dd", "28dae90"), ARBEIT):
    w = must(arbeit, wid)["settings"]
    if "editor" in w:
        w["editor"] = f"<p>{text}</p>"
    else:
        w["title"] = text
    w["_title"] = text[:40]
must(arbeit, "18e7c8b")["settings"]["_title"] = "Kästen"
arbeit["settings"].update({"_element_id": "arbeitsweise", "_title": "So arbeiten wir",
                           "padding": box(0, 20, 50, 20), "padding_laptop": box(0, 20, 50, 20),
                           # Tablet/Handy: innerer Container hat dort kein Polster, der dunkle Verlaufsstreifen (shadeup) der
                           # Abschnittskante würde die Überschrift abdunkeln; deshalb 30 px Abstand wie auf der Startseite
                           "padding_tablet": box(30, 20, 40, 20), "padding_mobile": box(30, 20, 30, 20)})
reid(arbeit)
page.append(arbeit)

# ---------------------------------------------------------------- 9) Ablauf der Zusammenarbeit (Original, Kamera-Texte)
ablauf = clone(H[14])
for wid, step in [("20734e0", "Erstgespräch"), ("8595654", "Termin vor Ort"), ("2f2676e", "Planung deines Kamerasystems"),
                  ("933e53d", "Umsetzung"), ("d11be39", "Übergabe & Betreuung")]:
    must(ablauf, wid)["settings"]["editor"] = f"<p>{STEPS[step]}</p>"
# Schritt 3 heißt hier „Planung deines Kamerasystems“ (Startseite: „Planung deines Systems“): Überschrift und Zeitstrahl
STEP_RENAME = {"Planung deines Systems": "Planung deines Kamerasystems"}
assert must(ablauf, "01d6be7")["settings"]["title"] == "Planung deines Systems"
must(ablauf, "01d6be7")["settings"]["title"] = STEP_RENAME["Planung deines Systems"]
tl = must(ablauf, "756a14f")
for item in tl["settings"]["eael_coustom_content_posts"]:
    roh = re.sub(r"\s+", " ", item["eael_custom_title"]).strip().replace("&amp;", "&")
    t = STEP_RENAME.get(roh, roh)
    if t != roh:
        item["eael_custom_title"] = t
    assert t in STEPS, t
    item["eael_custom_excerpt"] = f"<p>{STEPS[t]}</p>"
page.append(ablauf)

# ---------------------------------------------------------------- 11) Gründer (mit Fortsetzung), Technik, Partner, Standort mit Erstgespräch (Original)
page.append(clone(H[16]))
entstanden = clone(H[17])
entstanden["settings"]["padding_mobile"] = box(0, 0, 40, 0)      # Handy: Box samt Schein frei vom Streifen des folgenden Slider-Abschnitts
entstanden["settings"]["padding_tablet"] = box(20, 0, 60, 0)
page.append(entstanden)
page.append(slider)
page.append(clone(H[19]))          # Standort mit Erstgespräch; die Partner (H[18]) folgen nach dem FAQ

# ---------------------------------------------------------------- 12) FAQ (Original-Akkordeon, Kamera-Fragen)
faq = clone(H[20])
must(faq, "7983242")["settings"]["title"] = FAQ_H_DESKTOP
must(faq, "45eaf1f")["settings"]["title"] = FAQ_H_MOBILE
acc = must(faq, "ed852c3")
acc["settings"]["eael_adv_accordion_tab"] = [
    {"eael_adv_accordion_tab_title": q, "_id": new_id(), "eael_adv_accordion_tab_icon_show": "",
     "eael_adv_accordion_text_type": "content", "eael_adv_accordion_tab_content": f"<p>{a}</p>"}
    for q, a in FAQ
]
# SEO: Fragen als Zwischenüberschriften (h3), das Widget gibt dazu FAQPage-Strukturdaten aus (Schema.org)
acc["settings"].update({"eael_adv_accordion_title_tag": "h3", "eael_adv_accordion_faq_schema_show": "yes"})
page.append(faq)
page.append(clone(H[18]))          # Unsere Partner (Wunsch vom 20.10.: ans Ende des FAQ)

# ---------------------------------------------------------------- 11b) Eigene Kontaktseite (Kopie der Seite /kontakt, eigenes Formular)
# Wie beim Original öffnet der Fragebogen eine eigene Seite. Die Elementor-Daten der Kontaktseite (quelle-kontakt.json)
# werden nur gelesen; die Kopie bekommt den kameraspezifischen Text und das Formular „Anfrageformular Kamerasysteme“
# (medien.json: formular_id). Ausgabe: elementor/kontakt-kamerasysteme.elements.json (eigene WordPress-Seite).
KONTAKT = json.loads((ROOT / "elementor" / "quelle-kontakt.json").read_text(encoding="utf-8"))
FORM_ID = MEDIA.get("formular_id")
KONTAKT_URL = MEDIA.get("kontakt_url", "/kontakt-kamerasysteme/")
kontakt_page = []
if FORM_ID:
    ksec = clone(KONTAKT[0])
    ksec["settings"]["_title"] = "Kontakt"
    for w in ksec["elements"]:
        if w["widgetType"] == "text-editor":
            w["settings"]["editor"] = KONTAKT_TEXT
        if w["widgetType"] == "eael-gravity-form":
            w["settings"]["contact_form_list"] = str(FORM_ID)
            w["settings"]["_title"] = "Anfrageformular Kamerasysteme"
    ksec["isInner"] = False
    kontakt_page.append(reid(ksec))

# ---------------------------------------------------------------- 12) Footer (Original)
footer_oben = clone(H[21])
# SEO/Barrierefreiheit: Das Footer-Logo verlinkt auf die Startseite, seine Mediathek-Datei hat aber keinen Alternativtext,
# der Link bleibt damit ohne Namen. Hier eine eigene Kopie der Datei mit Alt-Text (medien.json: footer_logo, gleiches Bild).
FOOTER_LOGO = MEDIA["footer_logo"]
def footer_logo_alt(el):
    if el.get("widgetType") == "image" and "ProVision-Infra-GmbH-blau" in el["settings"].get("image", {}).get("url", ""):
        el["settings"]["image"] = {"url": FOOTER_LOGO["url"], "id": FOOTER_LOGO["id"], "size": "", "alt": FOOTER_LOGO["alt"], "source": "library"}
    for c in el.get("elements", []):
        footer_logo_alt(c)
footer_logo_alt(footer_oben)
page.append(footer_oben)
page.append(clone(H[22]))

# ---------------------------------------------------------------- 13) Steuerung der Hintergrundvideos
# Elementor blendet ein "einmal abgespieltes" Video nach dem Ende aus. Gewünscht: letztes Bild bleibt stehen,
# und sobald der Bereich aus dem Bild gescrollt war und wieder sichtbar wird, läuft das Video erneut.
VIDEO_SCRIPT = """<script>
(function () {
  if (document.body.classList.contains('elementor-editor-active')) return;
  function steuern(id) {
    var bereich = document.querySelector('.elementor-element-' + id);
    if (!bereich) return;
    var video = bereich.querySelector('video.elementor-background-video-hosted');
    if (!video) return;
    var warAusserhalb = false;
    video.loop = false;
    video.addEventListener('ended', function () {
      // nach Elementors eigenem Ausblenden wieder einblenden: letztes Bild bleibt stehen
      setTimeout(function () { video.style.display = ''; }, 0);
    });
    if (!('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (!e.isIntersecting) { warAusserhalb = true; return; }
        if (!warAusserhalb) return;
        warAusserhalb = false;
        video.style.display = '';
        try { video.currentTime = 0; } catch (err) {}
        var p = video.play();
        if (p && p.catch) p.catch(function () {});
      });
    }, { threshold: 0 }).observe(bereich);
  }
  // Der Handy-Videoblock ist am Computer und Tablet ausgeblendet; Elementor lädt sein Video dort trotzdem (1,5 MB).
  // Deshalb ohne Autoplay und ohne Vorladen, solange der Block unsichtbar ist. Wird er durch eine Größenänderung
  // sichtbar, startet das Video nach.
  function nurLadenWennSichtbar(id) {
    var bereich = document.querySelector('.elementor-element-' + id);
    if (!bereich || getComputedStyle(bereich).display !== 'none') return;
    var video = bereich.querySelector('video.elementor-background-video-hosted');
    if (!video) return;
    video.removeAttribute('autoplay');
    video.preload = 'none';
    var zurueck = function () {
      if (getComputedStyle(bereich).display === 'none') return;
      window.removeEventListener('resize', zurueck);
      video.preload = 'auto';
      video.setAttribute('autoplay', '');
      var p = video.play();
      if (p && p.catch) p.catch(function () {});
    };
    window.addEventListener('resize', zurueck);
  }
  nurLadenWennSichtbar('d135e80');
  function start() {
    ['0f0c707', 'd135e80'].forEach(steuern);   // Hero (Desktop/Tablet) und Video-Block (Handy)
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
  // Elementor initialisiert Hintergrundvideos erst nach dem Laden seiner Skripte: Steuerung dann erneut anbinden
  window.addEventListener('load', function () { setTimeout(start, 800); });
})();
</script>"""
steuerung = {"id": new_id(), "elType": "container", "isInner": False, "elements": [{
    "id": new_id(), "elType": "widget", "widgetType": "html", "elements": [], "isInner": False,
    "settings": {"html": VIDEO_SCRIPT, "_title": "Steuerung Hintergrundvideo"},
}], "settings": {"content_width": "full", "padding": box(0, 0, 0, 0), "margin": box(0, 0, 0, 0),
                 "min_height": {"unit": "px", "size": 0, "sizes": []}, "_title": "Steuerung Hintergrundvideo"}}
page.append(steuerung)

# ---------------------------------------------------------------- 14) SEO: Überschriften-Hierarchie
# Die Startseite setzt viele Abschnittsüberschriften als <div>. Hier bekommen sie echte Überschriften-Tags (h2/h3), Fließtext
# in Überschriften-Widgets wird <p>. Das Aussehen bleibt gleich: jede dieser Überschriften hat ihre eigene (oder eine
# globale) Typografie, die nicht vom Tag abhängt.
HEADING_TAGS = [   # (Textanfang ohne HTML, Tag)
    ("Solange nichts passiert", "h2"), ("Stell dir mal vor", "h2"), ("Und genau das wird möglich", "p"),
    ("Mit Kamera- und Videoüberwachung von ProVision Infra", "h2"), ("So arbeiten wir", "h2"),
    ("Ablauf der Zusammenarbeit", "h2"), ("Genau daraus ist ProVision Infra entstanden", "h3"),
    ("Hier findest du", "h2"), ("Unsere Partner", "h2"),
    ("Jede Kamera planen wir", "p"), ("Aufzeichnung und App sind eingerichtet", "p"),
    ("5.0", "p"), ("Sterne bei Google", "p"),
] + [(step, "h3") for step in STEPS]   # Schritte des Ablaufs: h3 statt h6 (Reihenfolge der Überschriften)

def set_heading_tags(el):
    if el.get("widgetType") == "heading":
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", el["settings"].get("title", ""))).strip()
        for start, tag in HEADING_TAGS:
            if text.startswith(start):
                el["settings"]["header_size"] = tag
    for c in el.get("elements", []):
        set_heading_tags(c)

for sec in page:
    set_heading_tags(sec)

# ---------------------------------------------------------------- 15) SEO: Strukturierte Daten (Anbieter und Leistung)
# Yoast liefert WebPage, Breadcrumb und WebSite, das FAQ-Akkordeon die FAQPage. Hier kommen Anbieter (LocalBusiness,
# Daten aus dem Impressum) und die Leistung (Service) dazu. Die Texte für Titel und Beschreibung stehen in SEO (unten)
# und werden nach elementor/seo.json geschrieben (Yoast-Felder der Seite, siehe ANLEITUNG-WORDPRESS.md).
PAGE_URL = f"{SITE}/kamerasysteme/"
SEO = {
    "title": "Kamera- & Videoüberwachung für Unternehmen | ProVision Infra",
    "description": ("Videoüberwachung für Unternehmen in Hamburg, Hannover und Niedersachsen. ProVision Infra plant und "
                    "installiert dein Kamerasystem, mit Alarm aufs Handy."),
    "focus_keyphrase": "Videoüberwachung für Unternehmen",
    "og_title": "Wir schützen dein Unternehmen mit Kamera- & Videoüberwachung",
    "og_image": MEDIA.get("vorschaubild", {}).get("url", ""),
}
assert len(SEO["description"]) <= 155, len(SEO["description"])
AREA = [{"@type": "City", "name": "Hamburg"}, {"@type": "City", "name": "Hannover"},
        {"@type": "State", "name": "Niedersachsen"}, {"@type": "Country", "name": "Deutschland"}]
SCHEMA = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "LocalBusiness", "@id": f"{SITE}/#organisation", "name": "ProVision Infra GmbH", "url": f"{SITE}/",
         "logo": LOGO["url"], "image": LOGO["url"], "telephone": "+49 5821 4049040", "email": "info@provision-infra.de",
         "address": {"@type": "PostalAddress", "streetAddress": "Klein Hesebecker Straße 11", "postalCode": "29549",
                     "addressLocality": "Bad Bevensen", "addressRegion": "Niedersachsen", "addressCountry": "DE"},
         "openingHoursSpecification": [
             {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
              "opens": "09:00", "closes": "18:00"},
             {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "09:00", "closes": "14:00"}],
         "areaServed": AREA,
         "sameAs": ["https://www.instagram.com/provision_infra_gmbh/", "https://www.facebook.com/share/1CWs2rohMt/",
                    "https://www.linkedin.com/company/provision-infra-gmbh-i-g/"]},
        {"@type": "Service", "@id": f"{PAGE_URL}#leistung", "name": "Kamera- und Videoüberwachung für Unternehmen",
         "serviceType": "Videoüberwachung", "url": PAGE_URL, "image": SEO["og_image"] or LOGO["url"],
         "description": SEO["description"], "provider": {"@id": f"{SITE}/#organisation"}, "areaServed": AREA,
         "audience": {"@type": "BusinessAudience", "name": "Unternehmen, Betriebe und Gewerbe"}},
    ],
}
schema_widget = {"id": new_id(), "elType": "widget", "widgetType": "html", "elements": [], "isInner": False, "settings": {
    "html": '<script type="application/ld+json">' + json.dumps(SCHEMA, ensure_ascii=False) + "</script>",
    "_title": "Strukturierte Daten (SEO)"}}
steuerung["elements"].append(schema_widget)

# ---------------------------------------------------------------- 16) Handy: Standbild des Videoblocks früh laden (LCP)
# Am Handy ist das größte sichtbare Element das Standbild hinter dem Videoblock. Der Browser entdeckt es sonst erst spät
# (Hintergrundbild per CSS, nachgeladen per Skript). Ein Preload-Hinweis am Seitenanfang, nur für Handybreiten.
standbild = must(page[2], "d135e80")["settings"]["background_video_fallback"]["url"]
preload = {"id": new_id(), "elType": "widget", "widgetType": "html", "elements": [], "isInner": False, "settings": {
    "html": f'<link rel="preload" as="image" href="{standbild}" media="(max-width: 767px)" fetchpriority="high">',
    "custom_css": "selector { display: none; }", "_title": "Vorladen Standbild (Handy)"}}
page[1]["elements"].insert(0, preload)

(ROOT / "elementor" / "seo.json").write_text(json.dumps(SEO, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- Seiteneinstellungen (wie Startseite)
PAGE_CSS = """html, body {
  max-width: 100%;
  overflow-x: clip;
}

.shadeup {
  position: relative;
}

.shadeup::before {
  content: "";
  position: absolute;
  top: -10px;
  left: 0;
  width: 100%;
  height: 30px;
  background: linear-gradient(to bottom, transparent 0%, #010c2d 0%, transparent 100%);
  pointer-events: none;
  z-index: 10;
}

/* Hintergrundvideo nach dem Ende nicht ausblenden: letztes Bild bleibt stehen */
.elementor-element-0f0c707 video.elementor-background-video-hosted,
.elementor-element-d135e80 video.elementor-background-video-hosted {
  display: block !important;
}
"""
settings = {"template": "default", "background_background": "classic", "background_color": "#010D30",
            "__globals__": {"background_color": ""}, "custom_css": PAGE_CSS}

# ---------------------------------------------------------------- Buttons: zur eigenen Kontaktseite (wie das Original auf /kontakt)
if FORM_ID:
    def relink(el):
        if el.get("widgetType") == "button" and el["settings"].get("link", {}).get("url") in ("/kontakt", "#kontakt"):
            el["settings"]["link"]["url"] = KONTAKT_URL
        for c in el.get("elements", []):
            relink(c)
    for e in page:
        relink(e)

# ---------------------------------------------------------------- Prüfungen
ids = []
def collect(el):
    ids.append(el["id"])
    for c in el.get("elements", []):
        collect(c)
for e in page:
    collect(e)
assert len(ids) == len(set(ids)), "doppelte Element-IDs"
for e in page:
    e["isInner"] = False

out = ROOT / "elementor"
(out / "kamera-seite.elements.json").write_text(json.dumps({"elements": page, "settings": settings}, ensure_ascii=False), encoding="utf-8")
# Terminseiten für das Kamera-Formular: Kopien der Seiten „Termin“ (3617) und „Termin Gebucht“ (823) mit dem
# Calendly-Termintyp „Telefonisches Erstgespräch Kamerasysteme“ statt „… Schließsysteme“ (medien.json: calendly_kamera_url).
CALENDLY_KAMERA = MEDIA.get("calendly_kamera_url")
for quelle, ziel in (("quelle-termin.json", "termin-kamerasysteme.elements.json"),
                     ("quelle-termin-gebucht.json", "termin-gebucht-kamerasysteme.elements.json")):
    if not CALENDLY_KAMERA or not (ROOT / "elementor" / quelle).exists():
        continue
    tdata = json.loads((ROOT / "elementor" / quelle).read_text(encoding="utf-8"))
    tpage = [reid(clone(sec)) for sec in tdata]
    def swap_calendly(el):
        if el.get("widgetType") == "html" and "calendly.com/provision-infra/erstgespraech" in el["settings"].get("html", ""):
            el["settings"]["html"] = el["settings"]["html"].replace("https://calendly.com/provision-infra/erstgespraech", CALENDLY_KAMERA)
        for c in el.get("elements", []):
            swap_calendly(c)
    for sec in tpage:
        sec["isInner"] = False
        swap_calendly(sec)
    assert CALENDLY_KAMERA in json.dumps(tpage), "Calendly-Link nicht ersetzt: " + quelle
    (out / ziel).write_text(json.dumps({"elements": tpage, "settings": {"template": "default"}}, ensure_ascii=False), encoding="utf-8")
(out / "kontakt-kamerasysteme.elements.json").write_text(json.dumps({"elements": kontakt_page, "settings": {"template": "default"}}, ensure_ascii=False), encoding="utf-8")
(out / "landingpage-kamerasysteme.json").write_text(json.dumps({
    "content": page, "page_settings": settings, "version": "0.4",
    "title": "Landingpage Kamera- & Videoüberwachung", "type": "page"}, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Abschnitte: {len(page)}, Elemente: {len(ids)}, Größe: {len(json.dumps(page, ensure_ascii=False)) // 1024} KB")
