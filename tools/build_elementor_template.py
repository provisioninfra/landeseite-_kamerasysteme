#!/usr/bin/env python3
"""
Erzeugt elementor/landingpage-kamerasysteme.json – eine importierbare Elementor-Vorlage
(Elementor → Vorlagen → Gespeicherte Vorlagen → Vorlagen importieren).

Jeder Text ist ein eigenes Elementor-Widget (Überschrift, Texteditor, Button) und kann
nach dem Import direkt im Elementor-Editor bearbeitet werden. Das Styling liegt gebündelt
im "Benutzerdefinierten CSS" der Seite (Seiteneinstellungen → Erweitert, Elementor Pro).

Aufruf:  python3 tools/build_elementor_template.py
"""
import json, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "elementor" / "landingpage-kamerasysteme.json"

# --- Medien auf provision-infra.de (bereits in der WordPress-Mediathek vorhanden) ---
SITE = "https://provision-infra.de"
MEDIA_GOOGLE = {"url": f"{SITE}/wp-content/uploads/2026/05/Frame-8-e1779423443644.png", "id": 397}
MEDIA_LOTTIE = {"url": f"{SITE}/wp-content/uploads/2026/05/lp10754-provision-infra-gmbh-L9-desktop-V01.json", "id": 1454, "source": "library"}
PROVEN_IMG = "https://images.provenexpert.com/96/14/0396ae496297f4d88e04693bdb8f/widget_landscape_300_de_0.png"
# Hero-Video: nach dem Upload in die Mediathek hier bzw. im Editor die URL eintragen
HERO_VIDEO = f"{SITE}/wp-content/uploads/hero.mp4"
KONTAKT = f"{SITE}/kontakt"

_counter = [0]
def eid():
    _counter[0] += 1
    return hashlib.md5(f"pv-kamera-{_counter[0]}".encode()).hexdigest()[:7]

def container(settings=None, elements=None, **kw):
    s = {"content_width": "full"}
    s.update(settings or {})
    s.update(kw)
    return {"id": eid(), "elType": "container", "settings": s, "elements": elements or [], "isInner": True}

def widget(wtype, settings):
    return {"id": eid(), "elType": "widget", "settings": settings, "elements": [], "widgetType": wtype}

def heading(title, tag="h2", cls="", extra=None):
    s = {"title": title, "header_size": tag, "_css_classes": cls}
    s.update(extra or {})
    return widget("heading", s)

def text(html, cls="", extra=None):
    s = {"editor": html, "_css_classes": cls}
    s.update(extra or {})
    return widget("text-editor", s)

def button(label=None, cls="pv-btn", extra=None):
    s = {
        "text": label or "Unverbindliches Erstgespräch vereinbaren",
        "link": {"url": KONTAKT, "is_external": "", "nofollow": "", "custom_attributes": ""},
        "size": "sm",
        "selected_icon": {"value": "fas fa-video", "library": "fa-solid"},
        "icon_align": "right",
        "hover_animation": "grow",
        "_css_classes": cls,
    }
    s.update(extra or {})
    return widget("button", s)

def icon(fa, cls, view="default"):
    return widget("icon", {"selected_icon": {"value": fa, "library": "fa-solid"}, "view": view, "_css_classes": cls})

def spacer_col(pct):
    return container({"width": {"unit": "%", "size": pct, "sizes": []}})

HIDE_MOBILE = {"hide_mobile": "hidden-mobile"}
HIDE_DESKTOP = {"hide_desktop": "hidden-desktop", "hide_tablet": "hidden-tablet", "hide_laptop": "hidden-laptop"}
HIDE_DESKTOP_ONLY = {"hide_desktop": "hidden-desktop", "hide_laptop": "hidden-laptop"}

# ---------------------------------------------------------------- HERO
hero_content = container(
    {"width": {"unit": "%", "size": 100, "sizes": []}, "css_classes": "pv-hero-content", "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}},
    [
        heading('<span style="font-weight: 700">Wir schützen dein Gebäude</span> - mit Kamera- &amp; Videoüberwachung', "h1", "pv-h1"),
        text("<p>Ein Einbruch, Vandalismus oder Diebstahl &amp; deinem Unternehmen drohen schnell zehntausende Euro an Schaden.</p>"
             "<p>ProVision Infra plant &amp; installiert deine Kamera- und Videoüberwachung, mit der du dein Gebäude rund um die Uhr im Blick hast – per App, jederzeit und von überall.</p>",
             "pv-hero-text"),
        container({"css_classes": "pv-hero-cta"}, [button()]),
        # Mobil: Video als eigener Block unter dem Button
        container({"css_classes": "pv-mvideo", **HIDE_DESKTOP_ONLY}, [
            widget("video", {"video_type": "hosted", "hosted_url": {"url": HERO_VIDEO, "id": ""}, "autoplay": "yes", "mute": "yes", "play_on_mobile": "yes", "controls": "", "loop": "", "_css_classes": "pv-mvideo-widget"}),
        ]),
        # Trust-Zeile (Desktop)
        container({"flex_direction": "row", "flex_align_items": "center", "flex_gap": {"column": "40", "row": "20", "unit": "px", "size": 40}, "css_classes": "pv-trust", **HIDE_MOBILE}, [
            container({"flex_direction": "row", "flex_align_items": "center", "width": {"unit": "auto", "size": "", "sizes": []}, "flex_gap": {"column": "16", "row": "0", "unit": "px", "size": 16}}, [
                widget("image", {"image": MEDIA_GOOGLE, "image_size": "full", "_css_classes": "pv-google"}),
                container({"width": {"unit": "auto", "size": "", "sizes": []}, "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}}, [
                    heading('<span style="color:#fbc91b">★</span> <strong>5</strong> <small>von 5.0</small>', "div", "pv-score"),
                    heading("Sternen auf Google", "div", "pv-trust-label"),
                ]),
            ]),
            container({"flex_direction": "row", "flex_align_items": "center", "width": {"unit": "auto", "size": "", "sizes": []}, "flex_gap": {"column": "16", "row": "0", "unit": "px", "size": 16}}, [
                heading('<span style="color:#fbc91b">+</span>100', "div", "pv-count"),
                heading("zufriedene Kunden", "div", "pv-trust-label"),
            ]),
            widget("image", {"image": {"url": PROVEN_IMG, "id": ""}, "image_size": "full", "link_to": "custom", "link": {"url": "https://www.provenexpert.com/provision-infra/", "is_external": "on", "nofollow": ""}, "_css_classes": "pv-proven"}),
        ]),
    ],
)

hero = container(
    {
        "content_width": "boxed",
        "css_classes": "pv-sec pv-hero",
        "_element_id": "hero",
        "min_height": {"unit": "vh", "size": 80, "sizes": []},
        "flex_justify_content": "center",
        "background_background": "video",
        "background_color": "#010D30",
        "background_video_link": HERO_VIDEO,
        "background_play_once": "yes",
        "background_video_end": "",
        "background_overlay_background": "gradient",
        "background_overlay_color": "#010D30F5",
        "background_overlay_color_b": "#010D3059",
        "background_overlay_gradient_angle": {"unit": "deg", "size": 90, "sizes": []},
        "background_overlay_color_stop": {"unit": "%", "size": 0, "sizes": []},
        "background_overlay_color_b_stop": {"unit": "%", "size": 100, "sizes": []},
        "background_overlay_opacity": {"unit": "px", "size": 1, "sizes": []},
        "padding": {"unit": "px", "top": "48", "right": "0", "bottom": "64", "left": "0", "isLinked": False},
        "padding_mobile": {"unit": "px", "top": "32", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
    },
    [hero_content],
)
hero["isInner"] = False

# ---------------------------------------------------------------- KERNBOTSCHAFT
claim = container(
    {"content_width": "boxed", "css_classes": "pv-sec pv-claim-sec", "_element_id": "vorteile",
     "padding": {"unit": "px", "top": "72", "right": "0", "bottom": "72", "left": "0", "isLinked": False}},
    [container({"css_classes": "pv-claim", "padding": {"unit": "px", "top": "56", "right": "48", "bottom": "56", "left": "48", "isLinked": False},
                "padding_mobile": {"unit": "px", "top": "32", "right": "22", "bottom": "32", "left": "22", "isLinked": False}}, [
        heading("Unser Anspruch", "p", "pv-eyebrow"),
        heading("<strong>Eine Kamera montieren kann jeder.</strong> Dass sie im entscheidenden Moment das Richtige aufzeichnet, ist unsere Arbeit.", "h2", "pv-claim-title"),
        text("<p>Wir planen Videoüberwachung mit klar definierten Schutzzielen, richten sie vollständig ein und prüfen dokumentiert, ob sie leistet, was vereinbart war. Damit du weißt, was dein Sicherheitssystem im Ernstfall kann.</p>", "pv-claim-text"),
    ])],
)
claim["isInner"] = False

# ---------------------------------------------------------------- FÜNF UNTERSCHIEDE
DIFFS = [
    ("fas fa-shield-alt", "Sicherheitsanalyse statt Kameraverkauf",
     "Am Anfang steht keine Produktliste, sondern eine Begehung mit klaren Fragen. Wo kommt jemand ungesehen aufs Gelände, und welche Werte stehen dort auf dem Spiel? Welche Bereiche müssen deshalb erfasst werden, und welche lässt man bewusst weg? Erst daraus ergibt sich die Zahl der Kameras. Oft sind es weniger, als du erwartet hast.",
     "„Wir verkaufen dir keine Kameras auf Vorrat. Wir planen die Absicherung, die dein Objekt tatsächlich braucht.“"),
    ("fas fa-layer-group", "Sicherheitskonzept statt isolierter Technik",
     "Eine Kamera zeichnet einen Einbruch bestenfalls auf. Verhindert wird er durch eine Schließanlage, die den Zutritt erschwert, und durch eine Alarmierung, die im richtigen Moment Druck macht. Bei uns greifen diese Bausteine ineinander, weil wir sie von Anfang an gemeinsam planen.",
     "„Wir denken Sicherheit vom ersten Zutrittsversuch bis zur verwertbaren Aufzeichnung.“"),
    ("fas fa-mobile-alt", "Fertig eingerichtet statt nur montiert",
     "Montiert ist eine Kamera schnell. Die eigentliche Arbeit steckt in der Einrichtung: Fernzugriff auf dem Handy, Benachrichtigungen, die nicht bei jedem Blatt im Wind auslösen, Aufzeichnungszeiten und Zugriffsrechte für deine Mitarbeiter. All das übernehmen wir und zeigen es dir persönlich am Gerät.",
     "„Wir gehen erst, wenn du dein System selbst bedienen kannst.“"),
    ("fas fa-wrench", "Langfristige Betreuung statt einmaliger Installation",
     "Ein Kamerasystem altert. Festplatten füllen sich, Software braucht Updates, ein Objektiv verschmutzt oder eine Hecke wächst ins Bild. Deshalb bieten wir regelmäßige Funktionsprüfungen und einen festen Ansprechpartner bei Störungen an. Wer das verbindlich möchte, bekommt es als Wartungsvertrag.",
     "„Wir kümmern uns auch Jahre nach der Installation darum, dass deine Anlage zuverlässig läuft.“"),
    ("fas fa-clipboard-check", "Nachweisbare Übergabe statt bloßem Funktionstest",
     "Zum Abschluss prüfen wir gemeinsam mit dir, was die Anlage wirklich leistet, und halten das schriftlich fest. Dazu gehören das Kamerabild bei Tag und bei Nacht, Aufzeichnung und Wiedergabe, die Benachrichtigungen auf deinem Handy sowie die wichtigsten Systemeinstellungen. Dieses Protokoll bekommst du ausgehändigt.",
     "„Wir zeigen dir nicht, dass die Kamera läuft. Wir belegen, dass sie ihre Aufgabe erfüllt.“"),
]
cards = []
for i, (fa, title, body, quote) in enumerate(DIFFS, 1):
    cards.append(container(
        {"flex_direction": "row", "flex_direction_mobile": "column", "flex_gap": {"column": "28", "row": "18", "unit": "px", "size": 28}, "css_classes": "pv-card",
         "padding": {"unit": "px", "top": "32", "right": "36", "bottom": "32", "left": "36", "isLinked": False},
         "padding_mobile": {"unit": "px", "top": "24", "right": "20", "bottom": "24", "left": "20", "isLinked": False}},
        [
            container({"width": {"unit": "px", "size": 72, "sizes": []}, "width_mobile": {"unit": "px", "size": 60, "sizes": []}, "css_classes": "pv-card-iconcol"}, [icon(fa, "pv-card-icon")]),
            container({"width": {"unit": "%", "size": 100, "sizes": []}, "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}, "css_classes": "pv-card-body"}, [
                heading(f"{i:02d}", "div", "pv-num"),
                heading(title, "h3", "pv-card-title"),
                text(f"<p>{body}</p>", "pv-card-text"),
                text(f"<p>{quote}</p>", "pv-quote"),
            ]),
        ],
    ))

diff = container(
    {"content_width": "boxed", "css_classes": "pv-sec pv-diff", "_element_id": "unterschiede",
     "padding": {"unit": "px", "top": "96", "right": "0", "bottom": "96", "left": "0", "isLinked": False},
     "padding_mobile": {"unit": "px", "top": "64", "right": "0", "bottom": "64", "left": "0", "isLinked": False},
     "flex_gap": {"column": "20", "row": "20", "unit": "px", "size": 20}},
    [
        heading("Fünf Unterschiede, <strong>die du spürst</strong>", "h2", "pv-sec-title"),
        text("<p>„Alles aus einer Hand“ verspricht jeder Sicherheitsbetrieb. Was uns unterscheidet, erlebst du an Stellen, an denen andere längst fertig sind.</p>", "pv-sec-intro"),
        *cards,
        container({"css_classes": "pv-sec-cta", "margin": {"unit": "px", "top": "36", "right": "0", "bottom": "0", "left": "0", "isLinked": False}}, [button()]),
    ],
)
diff["isInner"] = False

# ---------------------------------------------------------------- ABLAUF DER ZUSAMMENARBEIT (Original Startseite)
STEPS = {
    "Erstgespräch": "Für eine Ersteinschätzung telefonieren wir kurz und schauen uns deine Situation an: Welche Probleme bestehen aktuell? Wo benötigst du Unterstützung? Wie schnell brauchst du deine Lösung?",
    "Termin vor Ort": "Wir gehen gemeinsam durch dein Gebäude und schauen uns an, wie deine Zugänge aktuell organisiert sind. Dabei nehmen wir direkt Aufmaß von deinen Türen und Zutrittspunkten. Du bekommst direkt eine Einschätzung zum Kostenrahmen und eine Handlungsempfehlung.",
    "Planung deines Systems": "Auf Basis des Termins erstellen unsere Experten dir ein fertiges Zutrittskonzept mit allen Komponenten und unserem Angebot, passend zu deinem Budget. Du möchtest noch etwas ändern? Wir passen deine Wünsche direkt gemeinsam im Termin an! Am Ende des Termins treffen wir gemeinsam die Entscheidung. Starten wir gemeinsam oder nicht?",
    "Umsetzung": "Hier konfigurieren wir die Software, programmieren die Hardware und montieren alles im Objekt. Danach erfolgt die Inbetriebnahme und Übergabe an dich.",
    "Übergabe &amp; Betreuung": "Du bekommst eine kurze Einweisung und kannst das System direkt nutzen. Wenn du willst, übernehmen wir danach auch die Verwaltung für dich!",
}
def step(title, anim, pct):
    return container({"width": {"unit": "%", "size": pct, "sizes": []}, "animation": anim, "css_classes": "pv-step",
                      "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}},
                     [heading(title, "h6", "pv-step-title"), text(f"<p>{STEPS[title]}</p>", "pv-step-text")])

row_top = container({"flex_direction": "row", "flex_align_items": "flex-end", "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}}, [
    spacer_col(18), step("Termin vor Ort", "fadeInDown", 26), spacer_col(10.5), step("Umsetzung", "fadeInDown", 29),
])
lottie = widget("lottie", {
    "source": "media_file", "source_json": MEDIA_LOTTIE, "caption_source": "none", "link_to": "none",
    "trigger": "bind_to_scroll", "effects_relative_to": "viewport",
    "viewport": {"unit": "%", "size": "", "sizes": {"start": 0, "end": 100}},
    "start_point": {"unit": "%", "size": 0, "sizes": []}, "end_point": {"unit": "%", "size": 100, "sizes": []},
    "renderer": "svg", "align": "center", "_css_classes": "pv-lottie",
})
row_bottom = container({"flex_direction": "row", "flex_align_items": "flex-start", "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}}, [
    step("Erstgespräch", "fadeInUp", 27), spacer_col(9.3), step("Planung deines Systems", "fadeInUp", 28), spacer_col(9.7), step("Übergabe &amp; Betreuung", "fadeInUp", 26),
])
ablauf_desktop = container({"css_classes": "pv-ablauf-desktop", **HIDE_MOBILE, "flex_gap": {"column": "0", "row": "8", "unit": "px", "size": 8}}, [row_top, lottie, row_bottom])

tl_items = []
for title in ["Erstgespräch", "Termin vor Ort", "Planung deines Systems", "Umsetzung", "Übergabe &amp; Betreuung"]:
    tl_items.append(container({"flex_direction": "row", "flex_align_items": "flex-start", "flex_gap": {"column": "22", "row": "0", "unit": "px", "size": 22}, "css_classes": "pv-tl-item",
                               "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "32", "left": "0", "isLinked": False}}, [
        container({"width": {"unit": "px", "size": 58, "sizes": []}}, [icon("fas fa-check", "pv-tl-dot")]),
        container({"width": {"unit": "%", "size": 100, "sizes": []}, "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}}, [
            heading(title, "h3", "pv-tl-title"), text(f"<p>{STEPS[title]}</p>", "pv-tl-text"),
        ]),
    ]))
ablauf_mobile = container({"css_classes": "pv-tl", **HIDE_DESKTOP, "flex_gap": {"column": "0", "row": "0", "unit": "px", "size": 0}}, tl_items)

ablauf = container(
    {"content_width": "boxed", "css_classes": "pv-sec pv-ablauf", "_element_id": "arbeiten",
     "padding": {"unit": "px", "top": "50", "right": "0", "bottom": "50", "left": "0", "isLinked": False},
     "padding_mobile": {"unit": "px", "top": "30", "right": "0", "bottom": "60", "left": "0", "isLinked": False}},
    [heading("Ablauf der Zusammenarbeit", "h2", "pv-ablauf-title"), ablauf_desktop, ablauf_mobile],
)
ablauf["isInner"] = False

# ---------------------------------------------------------------- CSS (Seiteneinstellungen → Erweitert → Benutzerdefiniertes CSS)
CSS = (ROOT / "elementor" / "custom.css").read_text(encoding="utf-8")

template = {
    "content": [hero, claim, diff, ablauf],
    "page_settings": {
        "custom_css": CSS,
        "hide_title": "yes",
        "background_background": "classic",
        "background_color": "#010D30",
    },
    "version": "0.4",
    "title": "Landingpage Kamera- & Videoüberwachung",
    "type": "page",
}
OUT.write_text(json.dumps(template, ensure_ascii=False, indent=2), encoding="utf-8")
print("geschrieben:", OUT.relative_to(ROOT), "Elemente:", _counter[0])
