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
 'graft': [cta('Lieber direkt mit uns sprechen?', 'Jeder Betrieb ist anders, und manche Frage klärt sich erst mit Blick auf deine Türen und dein Gelände. Im Erstgespräch hören wir zu und sagen dir offen, was sich bei dir lohnt.', nach='f1a5d3e'),
   video_kasten('Neben Schließanlagen installieren wir Kamerasysteme mit Alarm aufs Handy. Wie du dabei rechtlich sauber bleibst, erklärt der Ratgeber zur Videoüberwachung auf dem Firmengelände.'), PRESSE],
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Ratgeber</span><br>Schließanlagen &amp; Videoüberwachung'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Darf die Kamera den Hof filmen? Und was tust du, wenn der Generalschlüssel plötzlich weg ist? Solche Fragen hören wir jede Woche von Betrieben und Hausverwaltungen. Hier stehen unsere Antworten.<br><br>'
              '<span style="font-weight: 700;">Verständlich erklärt, mit Beispielen aus unserer Arbeit vor Ort.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Wissen aus der Praxis, für deine nächste Entscheidung.'},
  '7df04ae': {'editor': p('Wir planen und betreuen Schließanlagen und Videoüberwachung in ganz Norddeutschland. Viele Fragen tauchen dabei immer wieder auf, ob in der Arztpraxis oder auf dem Logistikhof. '
              'Die Antworten haben wir aufgeschrieben, damit du gut vorbereitet ins Gespräch gehst.')},
  'd38dec5': {'editor': p('Unsere Ratgeber ersetzen keine Rechtsberatung. Über deinen Einzelfall sprechen wir gern unverbindlich mit dir.')},
  'd70fb3d': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'c869af6': {'_title': 'Leistungen', 'title': 'Von der Frage zur Lösung'},
  '8b353e8': {'title': a('/mechanische-schliessanlagen/', 'Mechanische Schließanlagen') + ': wie Schließplan und Sicherungskarte zusammenspielen.'},
  '6519b8c': {'title': a('/zutrittssystem/', 'Elektronische Schließanlagen') + ': Zutritt per Transponder oder Smartphone, auf Wunsch mit Service.'},
  '05ac70c': {'editor': p('<a href="/kamerasysteme/">Videoüberwachung für Unternehmen</a>: Kameras, die erlaubt sind und im Ernstfall verwertbare Bilder liefern.')},
  'f1a5d3e': {'_title': 'Artikel', '_element_id': 'artikel'},
  'cfa4bb1': {'_title': 'Artikel', 'title': 'Alle Ratgeber'},
  '4967d0c': {'title': a(*ARTIKEL[0]) + ': Darf die Kamera auf den Parkplatz zeigen? Was aufs Hinweisschild gehört und wie lange du speichern darfst.'},
  '99ee72d': {'title': a(*ARTIKEL[1]) + ': Die ersten Stunden entscheiden. So begrenzt du den Schaden und klärst, wer haftet und was die Versicherung zahlt.'},
  '8754a23': {'editor': p('<a href="' + ARTIKEL[2][0] + '">' + ARTIKEL[2][1] + '</a>: Meist geht es ohne Bauarbeiten. Woran du das erkennst und worauf es bei Fluchttüren ankommt.')},
  '51f3331': {'title': 'Lieber persönlich? <br><span style="font-weight: 700; ">Ruf uns an</span>'},
  '5c65e03': {'editor': p('Manches klärt sich am schnellsten bei dir vor Ort. Wir kommen überall in Norddeutschland vorbei, alle Orte findest du in der '
              '<a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
 },
 'schema': {"@context": "https://schema.org", "@graph": [ORG, AUTOR, {
    "@type": "ItemList", "@id": URL + "#artikel", "name": "Ratgeber von ProVision Infra",
    "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": BASE + u} for i, (u, t) in enumerate(ARTIKEL)]}]},
}
