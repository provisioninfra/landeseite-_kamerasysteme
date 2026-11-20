import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORDER, GRUENDER, PRESSE, video_kasten, cta
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
 'order': ORDER, 'handy_css': True,
 'graft': [cta('Lieber direkt mit uns sprechen?', 'Manche Fragen lassen sich am besten bei dir vor Ort klären. Im Erstgespräch hören wir zu und sagen dir, was in deinem Fall sinnvoll ist.', nach='f1a5d3e'),
   video_kasten('Neben Schließanlagen installieren wir Kamerasysteme mit Alarm aufs Handy. Wie das rechtlich sauber gelingt, steht im Ratgeber zur Videoüberwachung auf dem Firmengelände.'), PRESSE],
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Ratgeber</span><br>Schließanlagen &amp; Videoüberwachung'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Was ist erlaubt, und was tust du, wenn etwas schiefgeht? Hier beantworten wir die Fragen, die uns Betriebe und Hausverwaltungen am häufigsten stellen.<br><br>'
              '<span style="font-weight: 700;">Verständlich geschrieben und aus unserer täglichen Arbeit in Betrieben und Wohnanlagen.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Antworten aus unserer täglichen Arbeit.'},
  '7df04ae': {'editor': p('Wir planen und betreuen Schließanlagen und Videoüberwachung in ganz Norddeutschland. Dabei hören wir oft dieselben Fragen. '
              'Die Antworten haben wir hier aufgeschrieben, damit du dich vorab informieren kannst.')},
  'd38dec5': {'editor': p('Unsere Ratgeber ersetzen keine Rechtsberatung. Über deinen Einzelfall sprechen wir gern unverbindlich mit dir.')},
  'd70fb3d': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'c869af6': {'_title': 'Leistungen', 'title': 'Von der Frage zur Lösung'},
  '8b353e8': {'title': a('/mechanische-schliessanlagen/', 'Mechanische Schließanlagen') + ': alles zu Schließplan und Sicherungskarte.'},
  '6519b8c': {'title': a('/zutrittssystem/', 'Elektronische Schließanlagen') + ': Zutritt per Transponder oder Smartphone, auf Wunsch mit Service.'},
  '05ac70c': {'editor': p('<a href="/kamerasysteme/">Videoüberwachung für Unternehmen</a>: Kameras planen, die erlaubt sind und im Ernstfall helfen.')},
  'f1a5d3e': {'_title': 'Artikel', '_element_id': 'artikel'},
  'cfa4bb1': {'_title': 'Artikel', 'title': 'Alle Ratgeber'},
  '4967d0c': {'title': a(*ARTIKEL[0]) + ': was beim Hinweisschild und bei der Speicherdauer gilt.'},
  '99ee72d': {'title': a(*ARTIKEL[1]) + ': Schritt für Schritt, mit Haftung und Versicherung.'},
  '8754a23': {'editor': p('<a href="' + ARTIKEL[2][0] + '">' + ARTIKEL[2][1] + '</a>: worauf du bei Maßen und Fluchttüren achten musst.')},
  '51f3331': {'title': 'Lieber persönlich? <br><span style="font-weight: 700; ">Ruf uns an</span>'},
  '5c65e03': {'editor': p('Manche Fragen lassen sich am besten vor Ort beantworten. Wir kommen zu dir, in ganz Norddeutschland; alle Orte findest du in der '
              '<a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
 },
 'schema': {"@context": "https://schema.org", "@graph": [ORG, AUTOR, {
    "@type": "ItemList", "@id": URL + "#artikel", "name": "Ratgeber von ProVision Infra",
    "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": BASE + u} for i, (u, t) in enumerate(ARTIKEL)]}]},
}
