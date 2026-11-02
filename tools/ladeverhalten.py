"""Ladeverhalten: ausgeblendete Lotties und Hintergrundvideos auf dem jeweiligen Gerät nicht laden (02.11.2026).

Elementor lädt Lottie-Dateien und Hintergrundvideos auch dann, wenn ihr Container auf dem aktuellen Gerät ausgeblendet
ist (Startseite am Handy: acht Lottie-Dateien mit rund 7 MB und ein zweites Hero-Video). Das Skript läuft vor Elementors
Initialisierung (HTML-Widget im Seiteninhalt, Elementors Skripte folgen im Footer) und nimmt diesen Elementen auf dem
ausgeblendeten Gerät ihre Initialisierung: Lottie-Widgets bekommen vorübergehend einen anderen Widget-Typ, bei
Hintergrundvideos wird der Videolink aus den Einstellungen entfernt. Wechselt das Gerät durch eine Größenänderung in
eine sichtbare Breite, wird alles wiederhergestellt und Elementor initialisiert die Elemente nach. Sichtbar ändert sich
nichts: Die Elemente waren ohnehin ausgeblendet. Das Hover-Skript der Lottie-Kästen (Custom Code „Animation Hover“)
bleibt unberührt, weil sichtbare Lotties wie bisher sofort laden.
"""
import hashlib

# Breakpoints dieser Website (Elementor: mobile 767, tablet 1024, tablet_extra 1280, laptop 1440, widescreen 2400)
BREAKPOINTS_JS = ("[['mobile',0,767],['tablet',768,1024],['tablet_extra',1025,1280],['laptop',1281,1440],"
                  "['desktop',1441,2399],['widescreen',2400,99999]]")

LADE_SCRIPT = r"""<script>
(function () {
  if (document.body.classList.contains('elementor-editor-active')) return;
  var STUFEN = %s;
  function stufe() { var w = window.innerWidth; for (var i = 0; i < STUFEN.length; i++) { if (w >= STUFEN[i][1] && w <= STUFEN[i][2]) return STUFEN[i][0]; } return 'desktop'; }
  function ausgeblendet(el, s) { var k = 'elementor-hidden-' + s; var n = el; while (n && n !== document.body) { if (n.classList && n.classList.contains(k)) return true; n = n.parentElement; } return false; }
  var merker = [];
  function anwenden() {
    var s = stufe();
    document.querySelectorAll('.elementor-widget-lottie[data-widget_type]').forEach(function (w) {
      if (ausgeblendet(w, s)) { merker.push({ el: w, art: 'lottie', wert: w.getAttribute('data-widget_type') }); w.setAttribute('data-widget_type', 'lottie-ausgeblendet.default'); }
    });
    document.querySelectorAll('[data-settings*="background_video_link"]').forEach(function (c) {
      if (!ausgeblendet(c, s)) return;
      var roh = c.getAttribute('data-settings');
      try { var o = JSON.parse(roh); if (!o.background_video_link) return; merker.push({ el: c, art: 'video', wert: roh }); delete o.background_video_link; c.setAttribute('data-settings', JSON.stringify(o)); } catch (e) {}
    });
  }
  function wiederherstellen() {
    var s = stufe(); var rest = [];
    merker.forEach(function (m) {
      if (ausgeblendet(m.el, s)) { rest.push(m); return; }
      if (m.art === 'lottie') m.el.setAttribute('data-widget_type', m.wert); else m.el.setAttribute('data-settings', m.wert);
      try { window.elementorFrontend && elementorFrontend.elementsHandler.runReadyTrigger(m.el); } catch (e) {}
    });
    merker = rest;
  }
  anwenden();
  var t; window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(wiederherstellen, 300); });
  // Bewertungssiegel: Das Siegel liefert ein „Product“-Schema mit Sternen für das Unternehmen. Google wertet das als
  // irreführende Strukturdaten. Bis es im ProvenExpert-Konto abgeschaltet ist, wird der Block aus dem gerenderten DOM
  // entfernt, den Google für Strukturdaten auswertet. Sichtbar ändert sich nichts.
  function schemaBereinigen() {
    document.querySelectorAll('script[type="application/ld+json"]').forEach(function (s) {
      var t = s.textContent || '';
      if (/"@type"\s*:\s*"Product"/.test(t) && /aggregateRating/.test(t) && s.parentNode) s.parentNode.removeChild(s);
    });
  }
  schemaBereinigen();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', schemaBereinigen);
})();
</script>""" % BREAKPOINTS_JS


def script_widget(id_hint):
    return {"id": hashlib.md5(id_hint.encode()).hexdigest()[:7], "elType": "widget", "widgetType": "html", "elements": [],
            "isInner": False, "settings": {"html": LADE_SCRIPT, "_title": "Steuerung Ladeverhalten und Schema",
                                           # ausgeblendet: so erzeugt das Widget keinen Flex-Abstand im Container (Skript läuft trotzdem)
                                           "custom_css": "selector { display: none; }"}}
