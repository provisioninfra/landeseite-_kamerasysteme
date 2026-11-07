"""Darstellung am Smartphone (Hoch- und Querformat), Rückmeldung des Kunden vom 02.11.2026.

Sechs Punkte, als CSS in einem HTML-Widget am Seitenende (Container „Steuerung …“, Widget-Titel
„Steuerung Handy-Darstellung“). Die Regeln sind an Element-IDs gebunden und werden je Seite aus der ID-Tabelle
SEITEN erzeugt; fehlt ein Block auf einer Seite, entfällt die Regel.

Hochformat (bis 767 px):
  1. Footer-Menü: Untermenü von „Mehr“ öffnete als Aufklappfenster links außerhalb des Bildes (SmartMenus positioniert
     es absolut mit negativem Rand). Jetzt: „Mehr“ ausgeblendet, Unterpunkte stehen fest in der Liste, Optik wie die
     Hauptpunkte (weiß, Poppins, zentriert).
  2. „Stell dir mal vor“ (Handy-Variante): Das Bild bzw. die Animation saß absolut mit festen Versätzen (34/45 px für
     375 px Breite) und stand auf breiteren Handys links; jetzt im Fluss unter den Karten, 62 % der Breite (max. 300 px),
     per Auto-Rand zentriert und je Seite um einen Versatz verschoben, damit die Platte (nicht der Hebel) mittig steht.
     Die Klasse „floating“ (Schwebe-Animation) bleibt wirksam, deshalb keine transform-Regel. Die blaue Leuchtfläche
     dahinter (SVG-Kreis) wird am Handy ausgeblendet.
  3. Festes ProvenExpert-Siegel verdeckte Text am rechten Rand; am Handy nur noch 60 px breit.

Querformat (Höhe bis 520 px, z. B. 932×430):
  1. Footer-Menü ebenfalls flach (gleiche Optik wie die Hauptpunkte im Tablet-Schriftgrad).
  4. Erklärvideo-Abschnitt: Video und Text wieder nebeneinander (Video links 46 %, Text rechts), wie am PC.
  5. „Warum immer mehr KMUs …“: linke Textspalte neben den Karten und beim Scrollen mitlaufend wie am Desktop. CSS
     position:sticky haftet auf der Seite nicht (html/body mit overflow-x: clip), deshalb wird Elementors eigene
     Sticky-Funktion der Spalte (sticky_on) per Skript um „tablet“ ergänzt, nur auf Handys (kurze Seite bis 520 px).
     Beim Drehen zurück ins Hochformat lässt Elementor die Spalte fixiert; das Skript hebt die Fixierung dort auf.
  6. „Stell dir mal vor“: Die Desktop/Tablet-Variante zieht die absolut gesetzten Lotties ohne Tablet-Breite auf volle
     Breite und nach oben; sie überdecken die Überschrift. Im Querformat wird stattdessen die Handy-Variante gezeigt,
     angeordnet wie am PC: Karten links, Griff/Animation in der Mitte, Karten rechts; die Überschrift bekommt Luft.
     Die Erklärvideo-Zeilen stehen wie am PC mit Icon links und Text rechts (statt Icon über Text).
  7. Abschnitt mit dem Türfoto („Und genau das wird möglich …“): Mindesthöhe 950 px ließ das Hintergrundbild
     (2400×1104, cover) seitlich so stark beschneiden, dass die Person im Bild fehlte. Im Querformat keine
     Mindesthöhe mehr, das Bild zeigt wie am PC Tür und Person.
"""
import hashlib, json

# Element-IDs je Seite (Elementor-Export). Schlüssel, die eine Seite nicht hat, weglassen.
SEITEN = {
    31: {  # Startseite
        "footer_nav": ["59b27e3"],
        "video_row": "7dfcfda", "video_col": "0a52747", "video_text": "478e545",
        "kmu_parent": "f86d566", "kmu_sticky": "8c98faa",
        "video_rows": [("1625f47", "3f048a0", "d05eab3"), ("996fecc", "4f94b84", "7df04ae"), ("502aa9e", "4393ccd", "d38dec5")],
        "stelldir_desktop": "af8c629", "stelldir_mobile": "1a6dd74", "stelldir_bild": "02add21",
        "stelldir_kreis": "00282d7", "stelldir_bildspalte": "1f03386", "stelldir_heading": "00fec0c",
        "stelldir_links": "13ae847", "stelldir_rechts": "134945e",
        # Platte und Zylinder liegen bei 23–29 % der Bildbreite (Hebel bis zum rechten Rand): Bild um 24 % seiner Breite
        # nach rechts, damit das Symbol mittig steht (Breite 62 % der Spalte, max. 300 px → 14.9 % bzw. 72 px)
        "stelldir_bild_versatz": "min(14.9%, 72px)", "stelldir_bild_versatz_quer": "min(24%, 62px)",
        "badge": "86d54af", "tuer": "c567c71",
    },
    4313: {  # Kamerasysteme: Logo-Rahmen statt Video; „Stell dir mal vor“ (Computer) ist eine normale Zeile, bleibt im Querformat
        "footer_nav": ["59b27e3"],
        "video_row": "29f65fd", "video_col": "a80975c", "video_text": "44c75f4",
        "video_rows": [("18c0c38", "859930d", "e54550b"), ("78965cb", "e38a5dc", "47ef5fe"), ("78459e1", "22705df", "3efeb2a")],
        "kmu_parent": "74b6d54", "kmu_sticky": "43e5085", "kmu_cards": "94cb6e5",
        "stelldir_mobile": "57840b0", "stelldir_kreis": "039908a",
        "badge": "86d54af", "tuer": "2419932",
    },
    4496: {  # Lüneburg (Kopie der Startseite mit Kamera-Lottie)
        "footer_nav": ["59b27e3"],
        "video_row": "7dfcfda", "video_col": "0a52747", "video_text": "478e545",
        "video_rows": [("1625f47", "3f048a0", "d05eab3"), ("996fecc", "4f94b84", "7df04ae"), ("502aa9e", "4393ccd", "d38dec5")],
        "kmu_parent": "4a79ecb", "kmu_sticky": "3e06cb6", "kmu_cards": "c407c9d",
        "stelldir_mobile": "7dfd9f6", "stelldir_kreis": "a191679",
        "badge": "86d54af",
    },
    3316: {  # Zutrittssystem: eigenes Design, fünf absolute Lotties in der Computer-Variante
        "footer_nav": ["333801ae"],
        "stelldir_desktop": "cb32d04", "stelldir_mobile": "364cd94", "stelldir_bild": "8df30cf",
        "stelldir_kreis": "70a288e", "stelldir_bildspalte": "3bb5900", "stelldir_heading": "23eaae5d",
        "stelldir_links": "2cf2087", "stelldir_rechts": "e6a539a",
        "badge": "6c473b9", "tuer": "1ef97f25",
    },
}
SEITEN[4605] = dict(SEITEN[4496])  # Uelzen: gleiche Struktur wie Lüneburg
SEITEN[4870] = dict(SEITEN[4313])  # Videoüberwachung Schlachthöfe (07.11.2026): aus der Kamera-Seite gebaut, gleiche Element-IDs

def _sel(ids):
    return ", ".join(f".elementor-element-{i}" for i in ([ids] if isinstance(ids, str) else ids))

def handy_css(ids):
    g = ids.get
    hoch, quer = [], []
    if g("footer_nav"):
        nav = _sel(g("footer_nav"))
        for ziel, fs in ((hoch, "14.08px"), (quer, "15.04px")):
            ziel.append(f"""  /* Footer-Menü: „Mehr“ flach, Unterpunkte wie Hauptpunkte */
  {nav} nav.elementor-nav-menu--main li.menu-item-has-children > a.has-submenu {{ display: none !important; }}
  {nav} nav.elementor-nav-menu--main ul.sub-menu {{
    display: flex !important; flex-direction: column; align-items: center; position: static !important;
    margin: 0 !important; padding: 0 !important; width: auto !important; min-width: 0 !important; max-width: none !important;
    background: transparent !important; box-shadow: none !important; border: 0 !important;
  }}
  {nav} nav.elementor-nav-menu--main ul.sub-menu a.elementor-sub-item {{
    color: #fff !important; background: transparent !important; font-family: "Poppins", sans-serif !important;
    font-weight: 400 !important; font-size: {fs} !important; line-height: 1.44 !important; padding: 6px 5px !important;
    text-align: center !important; border-inline-start: 0 !important;
  }}""")
    if g("stelldir_mobile"):
        m = _sel(g("stelldir_mobile"))
        kreis = f"  {m} {_sel(g('stelldir_kreis'))} {{ display: none !important; }}\n" if g("stelldir_kreis") else ""
        if g("stelldir_bild"):
            b = _sel(g("stelldir_bild"))
            versatz = g("stelldir_bild_versatz") or "0px"
            hoch.append(f"""  /* „Stell dir mal vor“: Griff mittig unter den Karten, frei schwebend (Klasse „floating“ animiert weiter) */
  {m} {{ padding-bottom: 40px !important; }}
  {m} {b} {{
    position: relative !important; left: {versatz} !important; right: auto !important; top: auto !important; bottom: auto !important;
    margin: 24px auto 0 !important; display: block !important; order: 99; flex: 0 0 auto !important;
    width: 62% !important; max-width: 300px !important;
  }}
  {m} {b} img, {m} {b} svg {{ width: 100% !important; height: auto !important; display: block; }}
{kreis}""".rstrip())
        elif kreis:
            hoch.append("  /* „Stell dir mal vor“: versetzte Leuchtfläche ausblenden */\n" + kreis.rstrip())
        if g("stelldir_desktop"):
            # Querformat: Desktop-Variante (absolute Lotties) ausblenden, Handy-Variante zeigen
            b = _sel(g("stelldir_bild")) if g("stelldir_bild") else None
            spalte = f"  {m} {_sel(g('stelldir_bildspalte'))} {{ justify-content: center !important; align-items: center !important; }}\n" if g("stelldir_bildspalte") else ""
            head = f"  {_sel(g('stelldir_heading'))} {{ padding-bottom: 14px !important; position: relative; z-index: 2; }}\n" if g("stelldir_heading") else ""
            bild = (f"""  {m} {b} {{
    position: relative !important; left: {g("stelldir_bild_versatz_quer") or "0px"} !important; right: auto !important; top: auto !important; bottom: auto !important;
    margin: 0 auto !important; display: block !important; flex: 0 0 auto !important;
    width: 100% !important; max-width: 260px !important;
  }}
  {m} {b} img, {m} {b} svg {{ width: 100% !important; height: auto !important; display: block; }}
""" if b else "")
            anordnung = ""
            if g("stelldir_links") and g("stelldir_rechts") and g("stelldir_bildspalte"):
                # Wie am PC: Karten links, Griff/Animation in der Mitte, Karten rechts
                anordnung = f"""  {m}, {m} > .e-con-inner {{ flex-direction: row !important; flex-wrap: nowrap !important; align-items: center !important; justify-content: center !important; gap: 12px !important; }}
  {m} {_sel(g('stelldir_links'))} {{ order: 1; --width: auto !important; width: auto !important; flex: 1 1 0 !important; min-width: 0; }}
  {m} {_sel(g('stelldir_bildspalte'))} {{ order: 2; --width: 26% !important; width: 26% !important; flex: 0 0 26% !important; min-height: 0 !important; }}
  {m} {_sel(g('stelldir_rechts'))} {{ order: 3; --width: auto !important; width: auto !important; flex: 1 1 0 !important; min-width: 0; }}
"""
            quer.append(f"""  /* „Stell dir mal vor“: Handy-Variante in PC-Anordnung statt der absoluten Desktop-Komposition */
  {_sel(g('stelldir_desktop'))} {{ display: none !important; }}
  {m} {{ display: flex !important; min-height: 0 !important; padding-bottom: 40px !important; }}
{anordnung}{spalte}{bild}{kreis}{head}""".rstrip())
    if g("badge"):
        hoch.append(f"  /* Siegel kleiner, damit weniger Text verdeckt wird */\n  {_sel(g('badge'))} img {{ max-width: 60px !important; }}")
    if g("video_row"):
        zeilen = ""
        for zeile, icon, text in g("video_rows") or []:
            zeilen += f"""  {_sel(zeile)} {{ flex-direction: row !important; flex-wrap: nowrap !important; align-items: center !important; gap: 14px !important; }}
  {_sel(icon)} {{ --width: 60px !important; width: 60px !important; flex: 0 0 60px !important; min-width: 0; }}
  {_sel(text)} {{ --container-widget-width: auto !important; width: auto !important; max-width: none !important; flex: 1 1 auto !important; min-width: 0; }}
"""
        quer.append(f"""  /* Erklärvideo links, Text rechts, Zeilen mit Icon links und Text rechts wie am PC */
  {_sel(g('video_row'))} {{ flex-direction: row !important; align-items: center !important; gap: 20px; }}
  {_sel(g('video_col'))} {{ --width: 46% !important; width: 46% !important; flex: 0 0 46% !important; }}
  {_sel(g('video_text'))} {{ --width: 52% !important; width: 52% !important; flex: 1 1 auto !important; }}
{zeilen}""".rstrip())
    if g("kmu_sticky"):
        par, col = _sel(g("kmu_parent")), _sel(g("kmu_sticky"))
        karten = f"  {_sel(g('kmu_cards'))} {{ --width: auto !important; width: auto !important; flex: 1 1 auto !important; min-width: 0; }}\n" if g("kmu_cards") else ""
        breite = "--width: 40% !important; width: 40% !important; flex: 0 0 40% !important; " if g("kmu_cards") else ""
        quer.append(f"""  /* Linke Textspalte neben den Karten (Mitlaufen übernimmt Elementors Sticky, siehe Skript) */
  {par}, {par} > .e-con-inner {{ flex-direction: row !important; align-items: flex-start !important; }}
  {col} {{ align-self: flex-start !important; {breite}}}
{karten}""".rstrip())
    if g("tuer"):
        quer.append(f"  /* Türfoto: keine Mindesthöhe (Bild sonst seitlich beschnitten), kein negativer Abstand nach oben (würde die Karten verdecken) */\n  {_sel(g('tuer'))} {{ min-height: 0 !important; --min-height: 0 !important; margin-top: 0 !important; }}")
    out = ["/* Handy-Darstellung (ProVision Infra), erzeugt aus tools/handy_darstellung.py */"]
    if hoch: out.append("@media (max-width: 767px) {\n" + "\n".join(hoch) + "\n}")
    if quer: out.append("@media (orientation: landscape) and (max-height: 520px) {\n" + "\n".join(quer) + "\n}")
    return "\n".join(out) + "\n"

HANDY_SCRIPT = r"""<script id="pv-handy-sticky">
/* 1. Handy-Querformat: Elementor behandelt es als Tablet. CSS position:sticky haftet hier nicht (Elementor/Theme clippen
      html/body), deshalb Elementors eigene Sticky-Funktion der Textspalten (Einstellung „sticky_on“) um „tablet“
      ergänzen – nur auf Handys (kurze Bildschirmseite bis 520 px), echte Tablets und Computer bleiben unverändert.
      Läuft vor Elementors Initialisierung, weil das Widget am Seitenende steht.
   2. Die Handy-Variante von „Stell dir mal vor“ ist für Tablet ausgeblendet; das Ladeverhalten-Skript schaltet deshalb
      ihre Lottie-Animation im Querformat ab. Da das CSS die Variante dort zeigt, wird die Animation wieder freigegeben
      (bei DOMContentLoaded, nach dem Ladeverhalten-Skript und vor Elementors Initialisierung; bei Drehung nachträglich). */
(function () {
  var HANDY_VARIANTEN = %s;
  try {
    if (Math.min(window.screen.width, window.screen.height) > 520) return;
    var els = document.querySelectorAll('.e-con[data-settings*="sticky"]');
    for (var i = 0; i < els.length; i++) {
      var s = JSON.parse(els[i].getAttribute('data-settings'));
      if (!s || !s.sticky || !Array.isArray(s.sticky_on) || s.sticky_on.indexOf('tablet') !== -1) continue;
      s.sticky_on.push('tablet');
      if (s.sticky_offset_tablet === undefined) s.sticky_offset_tablet = 16;
      els[i].setAttribute('data-settings', JSON.stringify(s));
    }
  } catch (e) {}
  function quer() { return window.matchMedia('(orientation: landscape) and (max-height: 520px)').matches; }
  function lottiesFreigeben(nachtraeglich) {
    if (!quer()) return;
    HANDY_VARIANTEN.forEach(function (id) {
      document.querySelectorAll('.elementor-element-' + id + ' .elementor-widget-lottie[data-widget_type="lottie-ausgeblendet.default"]').forEach(function (w) {
        w.setAttribute('data-widget_type', 'lottie.default');
        if (nachtraeglich) { try { window.elementorFrontend && elementorFrontend.elementsHandler.runReadyTrigger(w); } catch (e) {} }
      });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { lottiesFreigeben(false); });
  else lottiesFreigeben(false);
  /* 3. Dreht man das Handy vom Quer- ins Hochformat, lässt Elementor die im Querformat fixierte Textspalte fixiert
        (position: fixed) – sie legt sich dann hochkant über die Karten. Im Hochformat wird die Fixierung deshalb
        aufgehoben (über Elementors eigenes Sticky-Plugin, damit es beim Zurückdrehen wieder sauber startet). */
  function stickyAufraeumen() {
    if (window.innerWidth > 767) return;
    document.querySelectorAll('.e-con.elementor-sticky--active').forEach(function (el) {
      var erledigt = false;
      try { if (window.jQuery && jQuery.fn && jQuery.fn.sticky && jQuery(el).data('sticky')) { jQuery(el).sticky('destroy'); erledigt = true; } } catch (e) {}
      if (!erledigt) {
        el.classList.remove('elementor-sticky--active');
        ['position', 'width', 'margin-top', 'margin-bottom', 'top', 'inset-inline-start', 'left'].forEach(function (p) { el.style.removeProperty(p); });
        [el.previousElementSibling, el.nextElementSibling].forEach(function (n) { if (n && n.classList && n.classList.contains('elementor-sticky__spacer')) n.parentNode.removeChild(n); });
      }
    });
  }
  var t, t2;
  window.addEventListener('resize', function () {
    clearTimeout(t); t = setTimeout(function () { lottiesFreigeben(true); }, 450);
    clearTimeout(t2); t2 = setTimeout(stickyAufraeumen, 700);
  });
})();
</script>"""

def style_widget(ids, id_hint="steuerung-handy-darstellung"):
    return {"id": hashlib.md5(id_hint.encode()).hexdigest()[:7], "elType": "widget", "widgetType": "html", "elements": [],
            "isInner": False, "settings": {"html": "<style id=\"pv-handy-darstellung\">\n" + handy_css(ids) + "</style>\n"
                                                   + HANDY_SCRIPT % json.dumps([ids["stelldir_mobile"]] if ids.get("stelldir_desktop") and ids.get("stelldir_mobile") else []),
                                           "_title": "Steuerung Handy-Darstellung", "custom_css": "selector { display: none; }"}}

if __name__ == "__main__":
    import sys
    print(handy_css(SEITEN[int(sys.argv[1]) if len(sys.argv) > 1 else 31]))
