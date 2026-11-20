import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR

URL = BASE + '/ratgeber/'
def p(t): return '<p>' + t + '</p>'
def a(href, text): return f'<a href="{href}" style="color: #FBC91B;">{text}</a>'
ARTIKEL = [('/ratgeber/videoueberwachung-firmengelaende/', 'Videoüberwachung auf dem Firmengelände: Was ist erlaubt?'),
           ('/ratgeber/schluessel-verloren-unternehmen/', 'Schlüssel im Unternehmen verloren: Was jetzt zu tun ist'),
           ('/ratgeber/elektronischen-schliesszylinder-nachruesten/', 'Elektronischen Schließzylinder nachrüsten: Geht das in jede Tür?')]
SPEC = {
 'slug': 'ratgeber', 'title': 'Ratgeber',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Ratgeber Schließanlagen & Videoüberwachung | ProVision Infra',
         'description': 'Verständliche Antworten zu Schließanlagen, elektronischen Zylindern und Videoüberwachung: Recht, Kosten, Technik und was bei Schlüsselverlust zu tun ist.',
         'focuskw': 'Ratgeber Schließanlagen', 'bctitle': 'Ratgeber', 'robots_noindex': '0'},
 'remove': ['d7f768f', 'a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb', 'a3437e1', 'b0720cd'],
 'set': {
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Ratgeber</span><br>Schließanlagen &amp; Videoüberwachung'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Was ist erlaubt, was kostet es, was ist zu tun, wenn etwas schiefgeht? Hier beantworten wir die Fragen, die Betriebe, Praxen und Hausverwaltungen uns am häufigsten stellen.<br><br>'
              '<span style="font-weight: 700;">Verständlich, ohne Werbesprech und aus der Praxis von Planung, Montage und Service.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Wissen aus der Praxis, nicht aus dem Prospekt.'},
  '7df04ae': {'editor': p('Wir planen, montieren und betreuen Schließanlagen und Videoüberwachung in ganz Norddeutschland. Dabei hören wir immer wieder dieselben Fragen. '
              'Die Antworten haben wir hier aufgeschrieben, damit du dich vorab informieren und besser entscheiden kannst.')},
  'd38dec5': {'editor': p('Unsere Ratgeber ersetzen keine Rechtsberatung. Für deinen Einzelfall sprechen wir gern mit dir, unverbindlich und ehrlich.')},
  'd70fb3d': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'c869af6': {'_title': 'Leistungen', 'title': 'Von der Frage zur Lösung'},
  '8b353e8': {'title': a('/mechanische-schliessanlagen/', 'Mechanische Schließanlagen') + ': Schließplan, Sicherungskarte, Nachschlüssel und Austausch bei Verlust.'},
  '6519b8c': {'title': a('/zutrittssystem/', 'Elektronische Schließanlagen') + ': Transponder, Smartphone und Zutrittskontrolle mit Service.'},
  '05ac70c': {'editor': p('<a href="/kamerasysteme/">Videoüberwachung für Unternehmen</a>: Kameras planen, die erlaubt sind und im Ernstfall helfen.')},
  'f1a5d3e': {'_title': 'Artikel', '_element_id': 'artikel'},
  'cfa4bb1': {'_title': 'Artikel', 'title': 'Alle Ratgeber'},
  '4967d0c': {'title': a(*ARTIKEL[0]) + ': Rechtsgrundlage, Hinweisschild, Speicherdauer, Mitarbeitende und Betriebsrat.'},
  '99ee72d': {'title': a(*ARTIKEL[1]) + ': Schritt für Schritt, mit Haftung und Versicherung.'},
  '8754a23': {'editor': p('<a href="' + ARTIKEL[2][0] + '">' + ARTIKEL[2][1] + '</a>: Maße, Varianten, Fluchttüren und Ablauf.')},
  '51f3331': {'title': 'Lieber persönlich? <br><span style="font-weight: 700; ">Ruf uns an</span>'},
  '5c65e03': {'editor': p('Manche Fragen lassen sich am besten vor Ort beantworten. Wir kommen zu dir, in ganz Norddeutschland; alle Orte findest du in der '
              '<a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
 },
 'schema': {"@context": "https://schema.org", "@graph": [ORG, AUTOR, {
    "@type": "ItemList", "@id": URL + "#artikel", "name": "Ratgeber von ProVision Infra",
    "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": BASE + u} for i, (u, t) in enumerate(ARTIKEL)]}]},
}
