#!/usr/bin/env python3
"""
Baut die Kamera-Landingpage aus den Original-Bausteinen der Startseite (provision-infra.de) zusammen.

Quelle:   elementor/quelle-startseite.json   (Elementor-Daten der Startseite, per WordPress-Export gelesen)
Medien:   elementor/medien.json              (IDs/URLs der hochgeladenen Kamera-Medien)
Ausgabe:  elementor/kamera-seite.elements.json       – Elemente + Seiteneinstellungen (zum Speichern über den Editor)
          elementor/landingpage-kamerasysteme.json   – dieselbe Seite als importierbare Elementor-Vorlage

Jeder Abschnitt ist eine Kopie eines Startseiten-Abschnitts; nur Texte, Video, Bilder und die
Anzahl der Slides/Zeilen werden geändert. Dadurch stimmen Schriften, Farben, Abstände,
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
HERO_H1 = '<span style="font-weight: 700;">Wir schützen dein Gebäude</span> - mit Kamera- &amp; Videoüberwachung'
HERO_SUB = ('Ein Einbruch, Vandalismus oder Diebstahl &amp; deinem Unternehmen drohen schnell zehntausende Euro an Schaden. <br>\n<br>\n'
            'ProVision Infra plant &amp; installiert deine Kamera- und Videoüberwachung, mit der du dein Gebäude rund um die Uhr im Blick hast – per App, jederzeit und von überall.')

CLAIM_H = 'Eine Kamera montieren kann jeder. <span style="font-weight: 700; ">Dass sie im Ernstfall das Richtige zeigt, ist unsere Arbeit.</span>'
CLAIM_T = ('<p>Der Einbruch passiert nachts um drei. Morgens siehst du eine Aufnahme, auf der niemand zu erkennen ist. '
           'Die Versicherung fragt trotzdem nach Belegen. Genau diesen Moment planen wir von Anfang an mit.</p>')

SLIDER_H = 'Technik, <span style="font-weight: 700; ">die wir verbauen</span>'

DIFF_H = 'Fünf Unterschiede, <span style="font-weight: 700; ">die du im Ernstfall spürst</span>'
DIFF_INTRO = '<p>„Alles aus einer Hand“ steht auf jeder Website. Ob es stimmt, merkst du erst, wenn etwas passiert.</p>'
# (Icon-Media-ID, Titel, Text, Versprechen)
DIFFS = [
    ("ICON1", "Sicherheitsanalyse statt Kameraverkauf",
     "Wer dir ohne Begehung ein Angebot schickt, verkauft Technik. Wir gehen erst mit dir über das Gelände und suchen die Stellen, an denen jemand ungesehen reinkommt. Oft brauchst du weniger Kameras, als du denkst.",
     "„Wir verkaufen dir keine Kameras auf Vorrat.“"),
    ("ICON2", "Sicherheitskonzept statt isolierter Technik",
     "Eine Kamera filmt den Einbruch. Verhindern kann sie ihn nicht. Erst wenn Schließanlage und Alarm mitspielen, bekommt der Täter ein Problem. Deshalb planen wir alles zusammen.",
     "„Vom ersten Zutrittsversuch bis zur verwertbaren Aufnahme.“"),
    ("ICON3", "Fertig eingerichtet statt nur montiert",
     "Viele Anlagen hängen an der Wand und melden nichts, weil nie jemand die App eingerichtet hat. Bei uns verlässt niemand das Gebäude, bevor dein Handy Alarm schlägt und du das System selbst bedienen kannst.",
     "„Wir gehen erst, wenn du dein System selbst bedienen kannst.“"),
    ("ICON4", "Langfristige Betreuung statt einmaliger Installation",
     "Festplatten laufen voll, und irgendwann wächst eine Hecke ins Bild. Fällt das erst nach dem Einbruch auf, ist es zu spät. Wir prüfen deine Anlage regelmäßig, auf Wunsch per Wartungsvertrag.",
     "„Wir sind auch Jahre später noch für dich da.“"),
    ("ICON5", "Nachweisbare Übergabe statt bloßem Funktionstest",
     "„Läuft“ reicht nicht. Bei der Übergabe prüfen wir mit dir, ob Gesichter auch nachts erkennbar sind und ob dein Handy wirklich Alarm schlägt. Das Ergebnis bekommst du schriftlich.",
     "„Wir belegen, dass die Kamera ihre Aufgabe erfüllt.“"),
]
CTA_LEAD = '<p>Im Erstgespräch sagen wir dir in 15 Minuten, wo dein Gebäude angreifbar ist.</p>'

STEPS = {
    "Erstgespräch": "Ein kurzes Telefonat: Was ist passiert, oder was soll nie passieren? Welche Bereiche machen dir Sorgen? Du bekommst eine erste ehrliche Einschätzung.",
    "Termin vor Ort": "Wir gehen mit dir über das Gelände und schauen, wo jemand ungesehen reinkommt. Noch vor Ort nennen wir dir den Kostenrahmen.",
    "Planung deines Systems": "Du bekommst ein Konzept mit Kamerastandorten und Angebot, passend zu deinem Budget. Änderungswünsche bauen wir direkt ein. Dann entscheidest du.",
    "Umsetzung": "Wir montieren die Kameras und richten Aufzeichnung und App komplett ein. Du musst nichts selbst konfigurieren.",
    "Übergabe & Betreuung": "Wir prüfen gemeinsam, ob die Anlage leistet, was vereinbart war, und halten das schriftlich fest. Danach bleiben wir erreichbar.",
}

FAQ_H_DESKTOP = 'Häufige Fragen zu Kamera- &amp; \nVideoüberwachung mit <b>ProVision Infra</b>'
FAQ_H_MOBILE = 'Häufige Fragen zu Kamera- &amp; \nVideoüberwachung mit <br><b>ProVision Infra</b>'
FAQ = [
    ("Darf ich mein Firmengelände überhaupt per Kamera überwachen?",
     "Ja, innerhalb klarer Regeln. Erlaubt ist die Überwachung deines eigenen Geländes und deiner Zugänge, nicht die von Gehweg oder Nachbargrundstück. Mitarbeiter müssen informiert sein, ein Hinweisschild ist Pflicht. Wir planen die Kamerawinkel so, dass du auf der sicheren Seite bist, und geben dir die passenden Hinweisschilder und Unterlagen mit."),
    ("Wie lange dauert die Installation?",
     "Eine Anlage mit vier bis acht Kameras ist in der Regel an einem Tag montiert und eingerichtet. Größere Objekte planen wir in Abschnitten, damit dein Betrieb weiterläuft."),
    ("Kann ich die Bilder auf dem Handy sehen?",
     "Ja. Du bekommst eine App, in der du Live-Bild und Aufzeichnungen siehst und bei Bewegung benachrichtigt wirst. Die Einrichtung übernehmen wir und zeigen dir alles am Gerät."),
    ("Was passiert bei Stromausfall oder Internetstörung?",
     "Die Aufzeichnung läuft lokal auf dem Rekorder weiter, solange Strom da ist. Auf Wunsch sichern wir Rekorder und Kameras mit einer unterbrechungsfreien Stromversorgung ab. Fällt das Internet aus, fehlt nur der Fernzugriff, nicht die Aufzeichnung."),
    ("Was kostet eine Videoüberwachung?",
     "Das hängt von der Zahl der Kameras, den Entfernungen und den vorhandenen Leitungen ab. Einen ersten Rahmen bekommst du schon im Erstgespräch, nach dem Termin vor Ort einen verbindlichen Preis."),
    ("Sind meine Aufnahmen vor fremdem Zugriff geschützt?",
     "Die Aufnahmen bleiben auf deinem Rekorder im Gebäude und nicht in einer fremden Cloud. Zugriff hat nur, wer von dir freigegeben ist. Wir richten Zugänge und Verschlüsselung entsprechend ein und halten die Software aktuell."),
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

page = []

# ---------------------------------------------------------------- 1) Header (Original)
page.append(clone(H[0]))

# ---------------------------------------------------------------- 2) Hero (Original, neue Texte, neues Video)
hero = clone(H[1])
must(hero, "9dcea29")["settings"]["title"] = HERO_H1
must(hero, "e429076")["settings"]["title"] = HERO_SUB
hs = hero["settings"]
hs["background_video_link"] = VIDEO["url"]
hs["background_video_start"] = ""
hs["background_video_end"] = ""            # ganzes Video abspielen, danach stehen bleiben (background_play_once bleibt "yes")
hs["background_play_on_mobile"] = ""       # mobil einfarbig (eigenes Custom-CSS des Hero), Video folgt als Block unter dem Button
hs["background_video_fallback"] = {"url": POSTER["url"], "id": POSTER["id"], "size": "", "alt": "", "source": "library"}  # Standbild, bis das Video geladen ist
page.append(hero)

# ---------------------------------------------------------------- 3) Mobiler Video-Block (Original-Block der Startseite, nur mobil)
mvideo = clone(H[2])
ms = mvideo["settings"]
ms["background_video_link"] = VIDEO["url"]
ms["background_video_start"] = ""
ms["background_video_end"] = ""
ms["background_video_fallback"] = {"url": POSTER["url"], "id": POSTER["id"], "size": "", "alt": "", "source": "library"}
for k in list(ms.keys()):
    if k.startswith("_transform_") or k.startswith("hide_"):
        del ms[k]
ms.update(hide_all_but_mobile())
ms["_title"] = "Hero-Video (nur mobil)"
page.append(mvideo)

# ---------------------------------------------------------------- 4) Mobile Bewertungszeile (Original)
page.append(clone(H[3]))

# ---------------------------------------------------------------- 5) Unser Anspruch – Glas-Box im Stil der Startseite
glass = clone(must(H[15], "bea5923"))
must(glass, "cba15a6")["settings"]["title"] = CLAIM_H
must(glass, "4e4df2b")["settings"]["editor"] = CLAIM_T
glass["settings"]["width"] = {"unit": "%", "size": 72, "sizes": []}
glass["settings"]["width_tablet"] = {"unit": "%", "size": 100, "sizes": []}
glass["settings"]["width_mobile"] = {"unit": "%", "size": 100, "sizes": []}
glass["settings"]["animation"] = "fadeInUp"
glass["settings"]["_title"] = "Unser Anspruch"
claim = container({
    "content_width": "boxed", "css_classes": "shadeup", "_element_id": "digitalen", "_title": "Unser Anspruch",
    "flex_direction": "column", "flex_align_items": "center",
    "padding": box(80, 20, 50, 20), "padding_mobile": box(40, 20, 30, 20),
}, [glass])
claim["isInner"] = False
page.append(claim)

# ---------------------------------------------------------------- 6) Produkt-Slider – Kopie des Kundenstimmen-Sliders mit Bildern
slider = clone(H[5])
must(slider, "556df520")["settings"]["title"] = SLIDER_H
row = must(slider, "55a57e52")
row["elements"] = [e for e in row["elements"] if e["id"] != "63020976"]      # Bewertungszeile entfernen
car = must(slider, "2b91cf92")
slide_tpl = must(slider, "547b551e")
car["settings"]["carousel_items"] = []
car["elements"] = []
for i, img in enumerate(PRODUKTE, 1):
    item_id = new_id()
    car["settings"]["carousel_items"].append({"slide_title": f"Produktbild {i}", "_id": item_id})
    s = clone(slide_tpl)
    s["settings"].pop("custom_css", None)
    s["settings"].pop("background_color", None)
    s["settings"]["padding"] = box(0, 0, 0, 0)
    s["settings"]["_title"] = f"Produktbild {i}"
    s["elements"] = [{
        "id": new_id(), "elType": "widget", "widgetType": "image", "elements": [], "isInner": False,
        "settings": {
            "image": {"url": img["url"], "id": img["id"], "size": "", "alt": f"Produktbild {i}", "source": "library"},
            "image_size": "large", "align": "center",
            "width": {"unit": "%", "size": 100, "sizes": []},
            "image_border_radius": box(25, 25, 25, 25),
            "_title": f"Produktbild {i}",
        },
    }]
    car["elements"].append(s)
slider["settings"]["_element_id"] = "produkte"
slider["settings"]["_title"] = "Produkt-Slider"
reid(slider)
page.append(slider)

# ---------------------------------------------------------------- 7) Fünf Unterschiede – Icon-Zeilen im Stil der Startseite
sec_tpl = H[4]
heading_tpl = must(H[5], "556df520")
text_tpl = must(H[15], "4e4df2b")
row_tpl = must(H[4], "1625f47")
col_tpl = must(H[4], "9148472")
btn_tpl = must(H[12], "c7ed38d")

d_heading = clone(heading_tpl); d_heading["settings"]["title"] = DIFF_H; d_heading["settings"]["_title"] = "Fünf Unterschiede"
d_intro = clone(text_tpl)
d_intro["settings"].update({"editor": DIFF_INTRO, "align": "center", "align_mobile": "center",
                            "_element_custom_width": {"unit": "%", "size": 70, "sizes": []},
                            "_element_custom_width_tablet": {"unit": "%", "size": 100, "sizes": []},
                            "_flex_align_self": "center", "_margin": box(10, 0, 30, 0), "_title": "Einleitung"})

rows = []
for key, title, body, quote in DIFFS:
    r = clone(row_tpl)
    tile = r["elements"][0]
    tile["elements"][0]["settings"]["selected_icon"] = svg_icon(*ICONS[key])
    tile["elements"][0]["settings"]["_title"] = "Icon"
    t_title = clone(must(H[4], "d05eab3"))
    t_title["settings"].update({
        "title": title, "_title": title, "header_size": "h3",
        "typography_font_weight": "700",
        "typography_font_size": {"unit": "px", "size": 20, "sizes": []},
        "typography_font_size_laptop": {"unit": "px", "size": 18, "sizes": []},
        "typography_font_size_tablet_extra": {"unit": "px", "size": 16, "sizes": []},
        "typography_font_size_tablet": {"unit": "px", "size": 16, "sizes": []},
        "typography_font_size_mobile": {"unit": "px", "size": 15, "sizes": []},
        "_element_custom_width": {"unit": "%", "size": 100, "sizes": []},
        "_element_custom_width_tablet": {"unit": "%", "size": 100, "sizes": []},
        "_element_custom_width_mobile": {"unit": "%", "size": 100, "sizes": []},
    })
    t_body = clone(must(H[4], "7df04ae"))
    t_body["settings"].update({
        "editor": f'<p>{body}</p>\n<p><span style="color: #fbc91b; font-weight: 500;">{quote}</span></p>',
        "_title": title,
        "_element_custom_width": {"unit": "%", "size": 100, "sizes": []},
        "_element_custom_width_tablet": {"unit": "%", "size": 100, "sizes": []},
        "_element_custom_width_mobile": {"unit": "%", "size": 100, "sizes": []},
    })
    textcol = container({
        "width": {"unit": "%", "size": 80, "sizes": []}, "width_tablet": {"unit": "%", "size": 80, "sizes": []},
        "width_mobile": {"unit": "%", "size": 74, "sizes": []},
        "flex_direction": "column", "flex_gap": {"column": "6", "row": "6", "isLinked": True, "unit": "px", "size": 6},
        "padding": box(0, 0, 0, 0), "_title": "Text",
    }, [t_title, t_body])
    r["elements"] = [tile, textcol]
    r["settings"]["_title"] = title
    rows.append(reid(r))
col = clone(col_tpl); col["elements"] = rows
col["settings"].update({"flex_gap_laptop": {"column": "28", "row": "28", "isLinked": True, "unit": "px", "size": 28},
                        "flex_gap_tablet_extra": {"column": "24", "row": "24", "isLinked": True, "unit": "px", "size": 24},
                        "_title": "Unterschiede"})
reid(col)

cta_lead = clone(text_tpl)
cta_lead["settings"].update({"editor": CTA_LEAD, "align": "center", "align_mobile": "center", "typography_font_weight": "500",
                             "typography_font_size": {"unit": "px", "size": 18, "sizes": []},
                             "_element_custom_width": {"unit": "%", "size": 100, "sizes": []}, "_title": "Aufruf"})
cta_btn = clone(btn_tpl); cta_btn["settings"]["align"] = "center"; cta_btn["settings"]["_title"] = "Erstgespräch"
cta = container({"flex_direction": "column", "flex_align_items": "center",
                 "flex_gap": {"column": "20", "row": "20", "isLinked": True, "unit": "px", "size": 20},
                 "padding": box(40, 0, 0, 0), "_title": "Erstgespräch"}, [reid(cta_lead), reid(cta_btn)])

diff = {"id": new_id(), "elType": "container", "isInner": False, "settings": clone(sec_tpl["settings"]),
        "elements": [reid(d_heading), reid(d_intro), col, cta]}
diff["settings"].update({"_element_id": "unterschiede", "_title": "Fünf Unterschiede",
                         "padding": box(60, 20, 60, 20), "padding_mobile": box(40, 20, 40, 20),
                         "flex_gap": {"column": "20", "row": "20", "isLinked": True, "unit": "px", "size": 20}})
page.append(diff)

# ---------------------------------------------------------------- 8) Kundenstimmen (Original)
page.append(clone(H[5]))

# ---------------------------------------------------------------- 9) Ablauf der Zusammenarbeit (Original, Kamera-Texte)
ablauf = clone(H[14])
for wid, step in [("20734e0", "Erstgespräch"), ("8595654", "Termin vor Ort"), ("2f2676e", "Planung deines Systems"),
                  ("933e53d", "Umsetzung"), ("d11be39", "Übergabe & Betreuung")]:
    must(ablauf, wid)["settings"]["editor"] = f"<p>{STEPS[step]}</p>"
tl = must(ablauf, "756a14f")
for item in tl["settings"]["eael_coustom_content_posts"]:
    t = re.sub(r"\s+", " ", item["eael_custom_title"]).strip().replace("&amp;", "&")
    assert t in STEPS, t
    item["eael_custom_excerpt"] = f"<p>{STEPS[t]}</p>"
page.append(ablauf)

# ---------------------------------------------------------------- 10) Gründer, Partner, Standort mit Erstgespräch (Original)
page.append(clone(H[16]))
page.append(clone(H[17]))
page.append(clone(H[18]))
page.append(clone(H[19]))

# ---------------------------------------------------------------- 11) FAQ (Original-Akkordeon, Kamera-Fragen)
faq = clone(H[20])
must(faq, "7983242")["settings"]["title"] = FAQ_H_DESKTOP
must(faq, "45eaf1f")["settings"]["title"] = FAQ_H_MOBILE
acc = must(faq, "ed852c3")
acc["settings"]["eael_adv_accordion_tab"] = [
    {"eael_adv_accordion_tab_title": q, "_id": new_id(), "eael_adv_accordion_tab_icon_show": "",
     "eael_adv_accordion_tab_content": f'<p><span style="font-weight: 400;">{a}</span></p>'}
    for q, a in FAQ
]
page.append(faq)

# ---------------------------------------------------------------- 12) Footer (Original)
page.append(clone(H[21]))
page.append(clone(H[22]))

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
"""
settings = {"template": "default", "background_background": "classic", "background_color": "#010D30",
            "__globals__": {"background_color": ""}, "custom_css": PAGE_CSS}

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
(out / "landingpage-kamerasysteme.json").write_text(json.dumps({
    "content": page, "page_settings": settings, "version": "0.4",
    "title": "Landingpage Kamera- & Videoüberwachung", "type": "page"}, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Abschnitte: {len(page)}, Elemente: {len(ids)}, Größe: {len(json.dumps(page, ensure_ascii=False)) // 1024} KB")
