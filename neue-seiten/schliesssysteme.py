import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD, ORDER, GRUENDER, PRESSE, video_kasten, cta, analyse, stell_dir_vor, vorteile
from gemeinsam_ablauf import ABLAUF

URL = BASE + '/schliesssysteme/'
def p(t): return '<p>' + t + '</p>'
FAQ = [
 ('Welches Schließsystem ist das beste für mein Unternehmen?',
  p('Ein System, das für alle passt, gibt es nicht. Wichtig sind vor allem die Zahl der Türen und wie oft sich Berechtigungen ändern. Auch die Frage, ob du aus der Ferne verwalten willst, spielt mit hinein. '
    'Nach der Begehung empfehlen wir dir ein System und erklären dir, warum es zu deinem Betrieb passt.')),
 ('Wie unterscheiden sich mechanische und elektronische Schließsysteme?',
  p('Mechanische Systeme arbeiten mit Schlüssel und Zylinder, ganz ohne Strom. Elektronische Systeme öffnen per Transponder oder Smartphone, und Berechtigungen änderst du per Software. '
    'Mit „digital“ sind meist Systeme gemeint, die sich zusätzlich per App oder aus der Cloud verwalten lassen. Mehr zu den Grundlagen: '
    '<a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a> und <a href="/zutrittssystem/">elektronische Schließanlagen</a>.')),
 ('Brauchen elektronische Schließsysteme Strom oder Kabel?',
  p('Elektronische Zylinder und Beschläge laufen in der Regel mit Batterie, Kabel sind nicht nötig. Wandleser und vernetzte Komponenten brauchen teilweise einen Stromanschluss. '
    'Eine Ausnahme ist FORTLOX von SimonsVoss: Dort kommt der Zylinder ohne Batterie aus. Was das für dein Gebäude bedeutet, klären wir bei der Begehung.')),
 ('Was passiert, wenn die Batterie eines Zylinders leer ist?',
  p('Die Komponenten zeigen einen niedrigen Batteriestand rechtzeitig an, sodass der Wechsel planbar ist. Für den Notfall hat jedes System einen festgelegten Weg zur Notöffnung, '
    'den wir dir bei der Übergabe zeigen. Auf Wunsch übernehmen wir den Batteriewechsel im Rahmen der Wartung.')),
 ('Kann ich mein Smartphone als Schlüssel nutzen?',
  p('Ja. EVVA AirKey, SimonsVoss MobileKey, Keyota und NUKI machen das Smartphone zum Schlüssel. Wer kein Diensthandy hat, bekommt einen Transponder.')),
 ('Lässt sich mein bestehendes Schließsystem erweitern oder kombinieren?',
  p('Meist ja. Eine mechanische Anlage lässt sich an stark genutzten Türen um elektronische Zylinder ergänzen. Innerhalb eines Herstellers klappen Erweiterungen in der Regel problemlos, '
    'die AX-Komponenten von SimonsVoss passen zum Beispiel zu bestehenden SimonsVoss-Anlagen. Bevor wir etwas tauschen, prüfen wir deine vorhandene Anlage.')),
 ('Kann ich ein Schließsystem auch mieten?',
  p('Ja. Keyrent vermietet digitale Schließsysteme, etwa für Baustellen und befristete Projekte. Bei dauerhaften Lösungen legen wir dir Kaufpreis und laufende Kosten offen nebeneinander.')),
 ('Sind elektronische Schließsysteme datenschutzkonform?',
  p('Ja, wenn sie richtig eingerichtet sind. Zutrittsprotokolle sind personenbezogene Daten, deshalb legen wir mit dir fest, was protokolliert wird und wie lange. '
    'Ein vorhandener Betriebsrat muss bei der Einführung beteiligt werden. Eine rechtliche Prüfung im Einzelfall ersetzt das nicht.')),
 ('Welche Hersteller verbaut ProVision Infra?',
  p('Mechanisch arbeiten wir mit EVVA. Elektronisch verbauen wir EVVA AirKey und EVVA Xesar sowie SimonsVoss mit System 3060, den AX-Komponenten, MobileKey und FORTLOX. Dazu kommen Keyota, Keyrent und NUKI. '
    'An keinen dieser Hersteller sind wir gebunden.')),
 ('Wie läuft die Beratung ab?',
  p('Nach einem kurzen Telefonat kommen wir zur Begehung und nehmen Türen und Abläufe auf. Anschließend stellen wir dir zwei oder drei passende Systeme mit ihren Vor- und Nachteilen vor. '
    'Für die Variante, die du wählst, bekommst du ein schriftliches Angebot.')),
]
SPEC = {
 'slug': 'schliesssysteme', 'title': 'Schließsysteme im Vergleich',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Schließsysteme für Firmen im Vergleich | ProVision Infra',
         'description': 'EVVA AirKey und Xesar, SimonsVoss 3060, AX und MobileKey, NUKI, Keyota und Keyrent herstellerneutral verglichen: Welches Schließsystem passt zu dir?',
         'focuskw': 'Schließsysteme', 'bctitle': 'Schließsysteme im Vergleich', 'robots_noindex': '0'},
 'remove': ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb'],
 'order': ORDER, 'handy_css': True,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Schließsysteme für Unternehmen</span><br>im herstellerneutralen Vergleich'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Transponder oder Smartphone? Kaufen oder mieten? Wer ein Schließsystem sucht, findet vor allem Prospekte, die alle dasselbe versprechen.<br><br>'
              '<span style="font-weight: 700;">Wir verbauen Systeme von EVVA, SimonsVoss, Keyota, Keyrent und NUKI. Welches davon zu deinem Betrieb passt, '
              'entscheiden deine Türen und deine Abläufe. Diese Empfehlung geben wir dir ehrlich und herstellerneutral.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Das richtige Schließsystem richtet sich nach deinem Alltag im Betrieb.'},
  '7df04ae': {'editor': p('Ein Praxisteam mit sechs Türen braucht etwas anderes als ein Logistikbetrieb im Schichtdienst. Deshalb fragen wir zuerst, wer wann Zutritt braucht '
              'und wie schnell sich eine Berechtigung ändern muss. Ebenso wichtig ist, was das System über die Jahre kostet.')},
  'd38dec5': {'editor': p('Weil wir mehrere Hersteller verbauen, müssen wir dir kein bestimmtes System verkaufen. Hier stellen wir dir die Systeme vor, mit denen wir arbeiten. '
              'Die endgültige Empfehlung bekommst du nach einer Begehung bei dir.')},
  'd7f768f': {'_title': 'Systeme im Überblick', '_element_id': 'systeme'},
  '74b6d54': {'_title': 'Systeme Überschrift', 'title': 'Die Schließsysteme, die wir verbauen: <span style="font-weight: 700; ">kurz erklärt</span>'},
  '43e5085': {'editor': p('Die Bandbreite reicht von der klassischen Anlage mit Sicherungskarte bis zum App-Schloss mit eigenem Mobilfunk. Jede Systemfamilie hat ihre Stärken, und manche lassen sich kombinieren.')},
  '8cc96a4': {'title': 'Mechanisch: EVVA mit Sicherungskarte'},
  '71be80d': {'editor': p('Schlüssel und Zylinder kommen ganz ohne Strom aus. Der Schließplan legt fest, wer wo hineinkommt, und Nachschlüssel gibt es nur gegen Sicherungskarte. '
              'Mehr dazu auf der Seite <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a>.')},
  '59a04cb': {'editor': p('Passt, wenn du wenige Türen hast und dein Team selten wechselt.')},
  '5e90e79': {'title': 'EVVA AirKey'},
  '88e4e41': {'editor': p('Zylinder und Wandleser öffnen per Smartphone oder Transponder. Berechtigungen verwaltest du online, auch aus der Ferne, '
              'und schickst sie direkt auf das Handy der Person.')},
  'ca72bdb': {'editor': p('Passt für Praxen und Betriebe mit mehreren Standorten, die Zutritt aus der Ferne steuern wollen.')},
  'b452400': {'title': 'EVVA Xesar'},
  '6773460': {'editor': p('Elektronische Zylinder und Beschläge öffnen mit Karten oder Schlüsselanhängern, verwaltet wird alles in der Xesar-Software. '
              'Das System ist für Betriebe mit vielen Türen und klaren Zeitprofilen ausgelegt.')},
  '24f8396': {'editor': p('Passt für den Mittelstand mit Schichtbetrieb und wechselnden Teams.')},
  '5860b09': {'title': 'SimonsVoss: System 3060, AX, MobileKey und FORTLOX'},
  'dc25036': {'editor': p('System 3060 ist die kabellose Plattform für große Gebäude und wird per Software verwaltet. Digitalzylinder AX und SmartHandle AX gehören zur neuen AX-Generation '
              'und passen zu bestehenden Anlagen. Mit MobileKey wird das Smartphone zum Schlüssel, die Verwaltung läuft über eine Web-App. Bei FORTLOX steckt die Elektronik im Schlüssel, '
              'der Zylinder braucht keine Batterie.')},
  '4838414': {'editor': p('Passt vom kleinen Betrieb mit MobileKey bis zum großen Industriegebäude mit System 3060.')},
  'bb8c516': {'title': 'Smarte Schlösser und Miete: NUKI, Keyota, Keyrent'},
  '6414a37': {'editor': p('NUKI sitzt innen auf dem vorhandenen Zylinder und öffnet per App oder Keypad. Keyota bringt App-Schlösser mit eigener Mobilfunk-Bridge mit, '
              'WLAN braucht es dafür keins. Über eine Schnittstelle lässt sich Keyota etwa an Hotelsoftware anbinden. Keyrent vermietet digitale Schließsysteme.')},
  'f5080c1': {'editor': p('Oft ist eine Kombination die beste Lösung, zum Beispiel mechanisch für Nebenräume und elektronisch für den Eingang.')},
  '3ac3e9e': {'editor': p('Passt für einzelne Türen und Ferienwohnungen, Keyrent vor allem für Baustellen.')},
  'd70fb3d': {'_title': 'Entscheidungsfragen', '_element_id': 'entscheidung'},
  'c869af6': {'_title': 'Entscheidungsfragen', 'title': 'Diese Fragen machen die Entscheidung leichter'},
  '8b353e8': {'title': 'Online oder offline? Willst du Berechtigungen aus der Ferne ändern, oder reicht das Programmieren vor Ort?'},
  '6519b8c': {'title': 'Smartphone oder Transponder? Entscheidend ist, wie viele Menschen in deinem Betrieb ein Diensthandy haben.'},
  '05ac70c': {'editor': p('Kaufen oder mieten? Für Baustellen lohnt sich die Miete, für dauerhafte Lösungen meist der Kauf. Wir rechnen dir beides offen durch.')},
  'f1a5d3e': {'_title': 'Welches System passt', '_element_id': 'empfehlung'},
  'cfa4bb1': {'_title': 'Welches System passt', 'title': 'Welches Schließsystem passt zu welchem Betrieb?'},
  '4967d0c': {'title': 'Praxis und kleines Büro: EVVA AirKey oder SimonsVoss MobileKey. Für einzelne Türen reicht oft ein NUKI.'},
  '99ee72d': {'title': 'Handwerk mit festem Team: eine mechanische EVVA-Anlage, deren stark genutzte Eingänge elektronisch ergänzt werden.'},
  '8754a23': {'editor': p('Mittelstand im Schichtbetrieb: EVVA Xesar oder SimonsVoss System 3060 mit AX-Komponenten.')},
  '51f3331': {'title': 'Herstellerneutrale Beratung <br><span style="font-weight: 700; ">in ganz Norddeutschland</span>'},
  '5c65e03': {'editor': p('Wir beraten dich vor Ort, egal ob du in <a href="/lueneburg/">Lüneburg</a>, <a href="/uelzen/">Uelzen</a>, <a href="/celle/">Celle</a>, '
              '<a href="/winsen-luhe/">Winsen (Luhe)</a> oder im Wendland sitzt. Unser Firmensitz ist in Bad Bevensen im Landkreis Uelzen; alle Orte findest du in der '
              '<a href="/standorte/">Übersicht unserer Standorte</a>.') +
              p('Montage und Service übernehmen wir selbst, für jedes der hier vorgestellten Systeme.') + NAP},
  '7983242': {'title': 'Häufige Fragen zu <b>Schließsystemen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zu <br><b>Schließsystemen</b>'},
 },
 'graft': stell_dir_vor([
    'Neue Mitarbeitende bekommen ihre Berechtigung am ersten Arbeitstag, ohne dass jemand einen Schlüssel nachmachen lässt.',
    'Die Reinigungsfirma kommt nur zu den vereinbarten Zeiten ins Haus, und mit dem Vertrag endet auch ihr Zugang.',
    'Ein verlorener Transponder kostet dich einen Klick und keinen einzigen neuen Zylinder.',
    'Im Ernstfall siehst du sofort, welche Tür wann geöffnet wurde.',
    'Du änderst Berechtigungen am Rechner oder am Handy, wann immer es nötig ist.',
    'Schlüsselbücher und Übergabeprotokolle auf Papier brauchst du nicht mehr.',
    'Mehrere Standorte verwaltest du über eine einzige Oberfläche.',
    'Serverraum und Personalakten bleiben den Menschen vorbehalten, die dort wirklich hineindürfen.']) + [
   analyse('Bevor wir ein System empfehlen, sehen wir uns an, wie dein Betrieb heute organisiert ist:',
           ('Wer braucht wann Zugang?', 'Wie oft ändern sich Berechtigungen?', 'Wo soll verwaltet werden?'),
           'Mit diesen Antworten steht fest, welches System zu dir passt.'),
  ] + vorteile([
    ('Ein System für alle Türen:', 'Zylinder und Wandleser laufen in einer gemeinsamen Verwaltung zusammen.'),
    ('Berechtigungen in Sekunden:', 'Zugänge vergibst oder entziehst du sofort, einen Termin beim Schlüsseldienst brauchst du dafür nicht.'),
    ('Zugänge passend zur Rolle:', 'Wer im Lager arbeitet, kommt ins Lager. Das Büro bleibt dem Büroteam vorbehalten.'),
    ('Zugang nach Zeitplan:', 'Dienstleister öffnen nur an den Tagen und zu den Uhrzeiten, die du festlegst.'),
    ('Weniger Organisation:', 'Schlüsselübergaben und Fahrten zur Abholung entfallen.'),
    ('Neue Leute ohne neue Schlüssel:', 'Für neue Mitarbeitende programmierst du einen Transponder, an der Anlage selbst ändert sich nichts.'),
    ('Verlust ohne Folgekosten:', 'Ein verlorener Transponder wird gesperrt, die Zylinder bleiben in der Tür.'),
    ('Überblick über alle Zugänge:', 'Du siehst jederzeit, wer welche Berechtigung hat, und kannst sofort reagieren.'),
    ('Datenschutz mit System:', 'Zutritte sind geregelt, und Protokolle bleiben nur so lange gespeichert wie vereinbart.'),
  ]) + [
   cta('So findest du das passende Schließsystem', 'Im Erstgespräch grenzen wir ein, welche Systeme für dich in Frage kommen. Danach entscheidest du in Ruhe.'),
   video_kasten('Zutritt und Kameras lassen sich gemeinsam planen. Die Kameras zeigen dir, was an Tor und Eingang passiert, und melden sich bei Bewegung auf deinem Handy.'),
   PRESSE,
 ],
 'ablauf': {**ABLAUF, 'Planung deines Systems': '<p>Du bekommst zwei oder drei passende Systeme mit ihren Vor- und Nachteilen. Für die Variante deiner Wahl erstellen wir das Angebot.</p>',
            'Umsetzung': '<p>Wir montieren die Komponenten und richten Software oder App vollständig ein. Konfigurieren musst du nichts.</p>'},
 'faq': FAQ,
 'schema': {"@context": "https://schema.org", "@graph": [ORG, {
    "@type": "Service", "@id": URL + "#leistung", "name": "Beratung, Planung und Montage von Schließsystemen für Unternehmen",
    "serviceType": "Schließsysteme und Zutrittskontrolle", "url": URL,
    "description": "Herstellerneutrale Beratung, Planung, Montage und Wartung mechanischer und elektronischer Schließsysteme: EVVA, EVVA AirKey, EVVA Xesar, SimonsVoss System 3060, AX, MobileKey, FORTLOX, Keyota, Keyrent und NUKI.",
    "provider": {"@id": BASE + "/#organization"},
    "brand": [{"@type": "Brand", "name": n} for n in ["EVVA", "SimonsVoss", "Keyota", "Keyrent", "NUKI"]],
    "areaServed": [{"@type": "City", "name": o} for o in ORTE_NORD] + [{"@type": "State", "name": "Niedersachsen"}],
    "audience": {"@type": "BusinessAudience", "name": "Unternehmen, Praxen, Hausverwaltungen, Hotels und Vereine"}}]},
}
SPEC['clone'] = [
 ('985957a', '58762b2', '985957a', {
   '4967d0c': {'title': 'Mehrere Standorte: EVVA AirKey oder SimonsVoss MobileKey. Ohne WLAN vor Ort hilft Keyota mit eigener Mobilfunk-Bridge.'},
   '99ee72d': {'title': 'Hotel und Ferienwohnung: Keyota mit Anbindung an die Buchungssoftware oder NUKI für einzelne Einheiten.'},
   '8754a23': {'editor': p('Baustellen und befristete Projekte: digitale Schließsysteme zur Miete von Keyrent, ganz ohne Umbau.')},
 }),
]
