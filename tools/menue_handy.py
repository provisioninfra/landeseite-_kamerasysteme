"""Kopfleisten-Menü: „Mehr“ nur am Bildschirm, auf dem Handy flach (Vorgabe des Kunden vom 27.10.2026).

Elementors Aufklappmenü zeigt auf dem Handy den Punkt „Mehr“ als eigene Zeile mit eingeklappten Unterpunkten. Gewünscht:
Nach dem Ausklappen sofort alle Einträge sehen, „Komm in unser Team“ als letzter Punkt (im Menü selbst als letzter
Unterpunkt von „Mehr“ angelegt). Das CSS am Menü-Widget blendet auf Handybreite die Zeile „Mehr“ aus und zeigt ihre
Unterpunkte dauerhaft als normale Zeilen. Das Skript nimmt die Markierung „verborgen“ (aria-hidden) zurück, die Elementors
Menüskript den Unterpunkten gibt, damit Vorlesehilfen alle Einträge erreichen. Gleicher Code auf allen Seiten mit dieser
Kopfleiste (Startseite, Kameraseite); die Karriere-Seite hat keine solche Kopfleiste.
"""
import hashlib

HANDY_MAX = 767   # Elementor-Breakpoint „Handy“ dieser Website


def handy_css(nav_settings):
    """Custom CSS für das Nav-Menu-Widget. Die Unterpunkte bekommen auf dem Handy die Typografie der Hauptpunkte
    (Elementor gibt ihnen sonst die globale Aufklapp-Typografie, hier Roboto 500, und einen unsichtbaren 8-px-Rahmen links)."""
    groesse = None
    for key in ("menu_typography_font_size_mobile", "menu_typography_font_size_tablet", "menu_typography_font_size"):
        v = nav_settings.get(key)
        if isinstance(v, dict) and v.get("size"):
            groesse = f'{v["size"]}{v.get("unit", "px")}'
            break
    familie = nav_settings.get("menu_typography_font_family")
    gewicht = nav_settings.get("menu_typography_font_weight")
    regeln = []
    if familie:
        regeln.append(f'font-family: "{familie}", sans-serif;')
    if gewicht:
        regeln.append(f"font-weight: {gewicht};")
    if groesse:
        regeln.append(f"font-size: {groesse};")
    regeln += ["line-height: normal;", "border-inline-start-width: 0;"]
    return ("/* Handy: Aufklappmenü flach. „Mehr“ ausblenden, seine Unterpunkte als normale Zeilen zeigen (siehe tools/menue_handy.py) */\n"
            f"@media (max-width: {HANDY_MAX}px) {{\n"
            "  selector .elementor-nav-menu--dropdown li.menu-item-has-children > a.has-submenu { display: none; }\n"
            "  selector .elementor-nav-menu--dropdown ul.sub-menu { display: block !important; }\n"
            f"  selector .elementor-nav-menu--dropdown a.elementor-sub-item {{ {' '.join(regeln)} }}\n"
            "}")


HANDY_SCRIPT = """<script>
(function () {
  if (document.body.classList.contains('elementor-editor-active')) return;
  var HANDY = %d;
  function istHandy() { return window.innerWidth <= HANDY; }
  // Auf dem Handy zeigt das CSS die Unterpunkte von „Mehr“ dauerhaft an. Elementors Menüskript markiert sie trotzdem als
  // verborgen (aria-hidden); das wird hier zurückgenommen, damit Vorlesehilfen alle Einträge erreichen.
  function freigeben(ul) {
    if (!istHandy()) return;
    ['aria-hidden', 'aria-expanded', 'role', 'aria-labelledby'].forEach(function (a) { ul.removeAttribute(a); });
  }
  function start() {
    var listen = document.querySelectorAll('.elementor-nav-menu--dropdown ul.sub-menu');
    if (!listen.length) return;
    var beobachter = new MutationObserver(function (aenderungen) {
      aenderungen.forEach(function (m) { if (m.target.getAttribute('aria-hidden') === 'true') freigeben(m.target); });
    });
    listen.forEach(function (ul) { freigeben(ul); beobachter.observe(ul, { attributes: true, attributeFilter: ['aria-hidden'] }); });
    window.addEventListener('resize', function () { listen.forEach(freigeben); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
</script>""" % HANDY_MAX


def script_widget(id_hint="steuerung-handy-menue"):
    """HTML-Widget mit dem Skript; feste ID (unabhängig vom Zähler der Build-Skripte)."""
    return {"id": hashlib.md5(id_hint.encode()).hexdigest()[:7], "elType": "widget", "widgetType": "html", "elements": [],
            "isInner": False, "settings": {"html": HANDY_SCRIPT, "_title": "Steuerung Handy-Menü"}}
