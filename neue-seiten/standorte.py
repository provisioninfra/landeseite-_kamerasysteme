import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, ORTE_NORD, ORDER, GRUENDER, PRESSE, video_kasten, cta
from gemeinsam_ablauf import ABLAUF

URL = BASE + '/standorte/'
def ort(slug, name, text):
    return f'<a href="/{slug}/" style="color: #FBC91B;">{name}</a>: {text}'
GRUPPEN = {
 'uelzen1': [ort('uelzen', 'Uelzen', 'Die Kreisstadt liegt vor unserer Haustür. Gewerbebetriebe und Arztpraxen erreichen wir hier besonders schnell.'),
             ort('bad-bevensen', 'Bad Bevensen', 'Hier sitzen wir. Für Hotels und den Handel in der Kurstadt sind wir in wenigen Minuten vor Ort.'),
             '<p>' + ort('ebstorf', 'Ebstorf', 'Zwischen Klosterflecken und Heide planen wir Schließplan und Kameras für Betriebe und Vereine.') + '</p>'],
 'uelzen2': [ort('bienenbuettel', 'Bienenbüttel', 'Unser Nachbarort an der Ilmenau. Werkstatt und Büro hängen hier oft an einer gemeinsamen Anlage.'),
             ort('wieren', 'Wieren', 'In Wieren und der Gemeinde Wrestedt sichern wir vor allem Höfe und Hallen ab.'),
             '<p>' + ort('bad-bodenteich', 'Bad Bodenteich', 'Am Elbe-Seitenkanal im Süden des Landkreises verbinden wir Zutritt und Videoüberwachung für Gewerbe und Tourismus.') + '</p>'],
 'lueneburg': [ort('lueneburg', 'Lüneburg', 'In der Hansestadt arbeiten wir in alten Gemäuern der Altstadt genauso wie in den Gewerbegebieten am Stadtrand.'),
               ort('bleckede', 'Bleckede', 'An der Elbe kümmern wir uns um Schließanlagen für Ferienhäuser und um Kameras für Hof und Halle.'),
               '<p>' + ort('winsen-luhe', 'Winsen (Luhe)', 'Zwischen Lüneburg und Hamburg schützen wir Logistikflächen mit Zutrittskontrolle und Kameras.') + '</p>'],
 'wendland': [ort('dannenberg', 'Dannenberg (Elbe)', 'In Dannenberg und der Elbtalaue sichern wir Arztpraxen und landwirtschaftliche Betriebe ab.'),
              ort('hitzacker', 'Hitzacker (Elbe)', 'Ferienwohnungen öffnen hier per App, und Gäste brauchen keine Schlüsselübergabe mehr.'),
              '<p>' + ort('luechow', 'Lüchow (Wendland)', 'In der Kreisstadt des Wendlands rüsten wir Büros und Handwerksbetriebe mit Schließanlagen und Kameras aus.') + '</p>'],
 'celle': [ort('celle', 'Celle', 'In der Residenzstadt bekommen Fachwerkhäuser der Altstadt moderne Schließtechnik, und am Stadtrand sichern wir Produktionshallen.'),
           ort('gifhorn', 'Gifhorn', 'Im Landkreis zwischen Heide und Wolfsburg sichern wir Betriebe mit Schließanlagen und Videoüberwachung.'),
           '<p>' + ort('wittingen', 'Wittingen', 'Im Nordkreis Gifhorn arbeiten wir vor allem für Gewerbe und Landwirtschaft.') + '</p>'],
}
def reihe(g):
    a, b, c = GRUPPEN[g]
    return {'4967d0c': {'title': a}, '99ee72d': {'title': b}, '8754a23': {'editor': c}}
def gruppe(titel, g, anker):
    d = reihe(g); d['f1a5d3e'] = {'_title': titel, '_element_id': anker}; d['cfa4bb1'] = {'_title': titel, 'title': titel}; return d

FAQ = [
 ('In welchen Regionen arbeitet ProVision Infra?',
  '<p>Unser Firmensitz ist in Bad Bevensen im Landkreis Uelzen. Von hier aus arbeiten wir in den Landkreisen Uelzen, Lüneburg, Lüchow-Dannenberg, Celle, Gifhorn und Harburg. '
  'Darüber hinaus sind wir im gesamten Raum zwischen Hamburg und Hannover unterwegs. Alle Orte mit eigener Seite findest du weiter oben.</p>'),
 ('Kommt ihr auch zu Projekten außerhalb der aufgeführten Orte?',
  '<p>Ja. Die Liste zeigt die Orte, in denen wir regelmäßig unterwegs sind. Für Schließanlagen und Videoüberwachung fahren wir auch in andere Orte in Norddeutschland. '
  'Melde dich einfach. Wir sagen dir offen, wie wir dein Projekt umsetzen können.</p>'),
 ('Habt ihr an jedem Ort ein eigenes Büro?',
  '<p>Nein. Wir haben einen Firmensitz in Bad Bevensen und kommen von dort zu dir. Alle Arbeiten erledigt unser eigenes Team, und für dein Projekt hast du einen festen Ansprechpartner.</p>'),
 ('Wie schnell seid ihr vor Ort?',
  '<p>Das hängt von der Entfernung ab. Im Landkreis Uelzen sind wir oft in rund 20 Minuten bei dir. Für weiter entfernte Orte wie Celle oder Winsen planen wir den Termin mit etwas mehr Vorlauf. '
  'Begehung und Montage legen wir so, dass dein Betrieb weiterläuft.</p>'),
 ('Welche Leistungen bietet ihr an allen Standorten an?',
  '<p>Überall dieselben: <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a>, <a href="/zutrittssystem/">elektronische Schließanlagen und Zutrittskontrolle</a>, '
  '<a href="/kamerasysteme/">Kamera- und Videoüberwachung</a> sowie Wartung und Erweiterung bestehender Anlagen.</p>'),
 ('Wie läuft ein Projekt ab, wenn ihr weiter weg seid?',
  '<p>Wir starten mit einem Telefonat, danach kommen wir zur Begehung. Die Montage planen wir so, dass möglichst viel an einem Termin erledigt ist. '
  'Danach bleiben wir für Service und Erweiterungen dein Ansprechpartner, egal wie weit du von Bad Bevensen entfernt bist.</p>'),
]
STADTSEITEN = ['lueneburg', 'uelzen', 'bad-bevensen', 'ebstorf', 'bienenbuettel', 'wieren', 'bad-bodenteich', 'bleckede', 'winsen-luhe',
               'dannenberg', 'hitzacker', 'luechow', 'celle', 'gifhorn', 'wittingen']
SPEC = {
 'slug': 'standorte', 'title': 'Standorte',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': ['Veerßen', 'Oldenstadt', 'Holdenstedt', 'Uelzener', 'Suderburg', 'Rosche', 'Himbergen', 'Altenmedingen'], 'erlaubt': [],
 'seo': {'title': 'Standorte: Schließanlagen & Videoüberwachung im Norden',
         'description': 'Schließanlagen, Zutrittskontrolle und Videoüberwachung in Lüneburg, Uelzen, Celle, Winsen, im Wendland und ganz Norddeutschland. Alle Standorte im Überblick.',
         'focuskw': 'Schließanlagen Norddeutschland', 'bctitle': 'Standorte', 'robots_noindex': '0'},
 'remove': ['d7f768f', 'd70fb3d', 'aed8a2d', 'a3564b7', '7dfd9f6', 'f9348eb'],
 'order': ORDER, 'handy_css': True,
 'graft': [cta('Wann können wir bei dir sein?', 'Ruf uns an oder vereinbare ein Erstgespräch. Wir nennen dir einen Termin für die Begehung und sagen dir danach klar, was dein Projekt kostet.'),
   video_kasten('Neben Schließanlagen installieren wir an allen Standorten Kamerasysteme mit Alarm aufs Handy. Zutritt und Überwachung planen wir dabei gemeinsam.'), PRESSE],
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Unsere Standorte</span><br>für Schließanlagen &amp; Videoüberwachung in Norddeutschland'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Von Bad Bevensen aus sichern wir Türen und Gelände in der Lüneburger Heide und entlang der Elbe, bis vor die Tore von Hamburg und Hannover.<br><br>'
              '<span style="font-weight: 700;">Hier findest du alle Orte, in denen wir regelmäßig Schließanlagen und Videoüberwachung planen und betreuen. '
              'Klick auf deinen Ort und lies, worauf es dort ankommt.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Ein Team aus Bad Bevensen für den ganzen Norden.'},
  '7df04ae': {'editor': '<p>ProVision Infra sitzt in Bad Bevensen im Landkreis Uelzen. Von hier fährt unser eigenes Team zu dir, ob nach Lüneburg oder bis ins Wendland. '
              'In Winsen sprichst du deshalb mit denselben Leuten wie in Uelzen, und die Montage übernimmt keine fremde Firma.</p>'},
  'd38dec5': {'editor': '<p>Jeder Ort stellt eigene Anforderungen. In Celle geht es oft um Fachwerk, in Hitzacker um Ferienwohnungen. '
              'Auf den Seiten der einzelnen Orte zeigen wir dir, worauf es bei dir ankommt.</p>'},
  '51f3331': {'title': 'Unser Einsatzgebiet <br><span style="font-weight: 700; ">zwischen Hamburg und Hannover</span>'},
  '5c65e03': {'editor': '<p>Auch in den Gemeinden rund um diese Orte sind wir für dich da, etwa in Suderburg, Altenmedingen, Amt Neuhaus, Adendorf, Munster und Soltau. '
              'Größere Projekte setzen wir in ganz Norddeutschland um, auch in Hamburg und Hannover.</p>'
              '<p>An jedem Standort planen wir <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a> und <a href="/zutrittssystem/">elektronische Schließanlagen</a>. '
              'Dazu kommt <a href="/kamerasysteme/">Videoüberwachung für Unternehmen</a>, auf Wunsch aus einer Hand mit der Zutrittskontrolle.</p>' + NAP},
  '7983242': {'title': 'Häufige Fragen zu <b>unseren Standorten</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zu <br><b>unseren Standorten</b>'},
 },
 'ablauf': ABLAUF, 'faq': FAQ,
 'schema': {"@context": "https://schema.org", "@graph": [ORG, {
    "@type": "ItemList", "@id": URL + "#orte", "name": "Standorte von ProVision Infra",
    "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{BASE}/{s}/"} for i, s in enumerate(STADTSEITEN)]}]},
}
SPEC['clone'] = [
 ('f1a5d3e', None, 'f1a5d3e', gruppe('Landkreise Celle und Gifhorn', 'celle', 'celle-gifhorn')),
 ('f1a5d3e', None, 'f1a5d3e', gruppe('Wendland: Landkreis Lüchow-Dannenberg', 'wendland', 'wendland')),
 ('f1a5d3e', None, 'f1a5d3e', gruppe('Landkreise Lüneburg und Harburg', 'lueneburg', 'lueneburg-harburg')),
 ('985957a', '58762b2', '985957a', reihe('uelzen2')),
]
SPEC['set'].update(reihe('uelzen1'))
SPEC['set'].update({'f1a5d3e': {'_title': 'Landkreis Uelzen', '_element_id': 'landkreis-uelzen'}, 'cfa4bb1': {'_title': 'Landkreis Uelzen', 'title': 'Landkreis Uelzen'}})
