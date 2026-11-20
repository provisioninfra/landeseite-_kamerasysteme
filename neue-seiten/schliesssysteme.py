import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD
from gemeinsam_ablauf import ABLAUF

URL = BASE + '/schliesssysteme/'
def p(t): return '<p>' + t + '</p>'
FAQ = [
 ('Welches Schließsystem ist das beste für mein Unternehmen?',
  p('Es gibt kein bestes System für alle. Entscheidend sind die Zahl der Türen und Nutzer, wie oft Berechtigungen wechseln, ob du aus der Ferne verwalten willst und wie groß dein Budget ist. '
    'Nach einer Begehung empfehlen wir dir ein System und begründen, warum es zu deinem Betrieb passt.')),
 ('Was ist der Unterschied zwischen mechanischen, elektronischen und digitalen Schließsystemen?',
  p('Mechanische Systeme arbeiten mit Schlüssel und Zylinder, ganz ohne Strom. Elektronische Systeme öffnen per Transponder, Karte oder Smartphone; Berechtigungen änderst du per Software. '
    '„Digital“ wird oft gleichbedeutend verwendet und meint meist Systeme, die zusätzlich per App oder aus der Cloud verwaltet werden. Mehr zu den Grundlagen: '
    '<a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a> und <a href="/zutrittssystem/">elektronische Schließanlagen</a>.')),
 ('Brauchen elektronische Schließsysteme Strom oder Kabel?',
  p('Elektronische Zylinder und Beschläge arbeiten in der Regel mit Batterien und ohne Kabel. Wandleser und vernetzte Komponenten brauchen teilweise einen Stromanschluss. '
    'Eine Ausnahme ist FORTLOX von SimonsVoss: Dort kommt der Zylinder ohne Batterie aus. Was das für dein Gebäude bedeutet, klären wir bei der Begehung.')),
 ('Was passiert, wenn die Batterie eines Zylinders leer ist?',
  p('Die Komponenten zeigen einen niedrigen Batteriestand rechtzeitig an, sodass der Wechsel planbar ist. Für den Notfall hat jedes System einen festgelegten Weg zur Notöffnung, '
    'den wir dir bei der Übergabe zeigen. Auf Wunsch übernehmen wir den Batteriewechsel im Rahmen der Wartung.')),
 ('Kann ich mein Smartphone als Schlüssel nutzen?',
  p('Ja, bei mehreren Systemen: EVVA AirKey, SimonsVoss MobileKey, Keyota und NUKI unterstützen das Smartphone als Schlüssel. Für Mitarbeitende ohne Diensthandy '
    'kombinieren wir das mit Transpondern oder Karten.')),
 ('Lässt sich mein bestehendes Schließsystem erweitern oder kombinieren?',
  p('Meist ja. Mechanische Anlagen lassen sich um elektronische Zylinder an stark genutzten Türen ergänzen. Innerhalb eines Herstellers sind Erweiterungen in der Regel problemlos; '
    'die AX-Komponenten von SimonsVoss sind zum Beispiel mit bestehenden SimonsVoss-Anlagen kompatibel. Wir prüfen deine vorhandene Anlage, bevor wir etwas tauschen.')),
 ('Kann ich ein Schließsystem mieten statt kaufen?',
  p('Ja. Mit Keyrent gibt es digitale Schließsysteme zur Miete, zum Beispiel für Baustellen und befristete Projekte. Für dauerhafte Lösungen rechnen wir dir Kauf und laufende Kosten offen gegeneinander.')),
 ('Sind elektronische Schließsysteme datenschutzkonform?',
  p('Ja, wenn sie richtig eingerichtet sind. Zutrittsprotokolle sind personenbezogene Daten. Deshalb legen wir mit dir fest, was protokolliert wird und wie lange die Daten gespeichert bleiben. '
    'Gibt es einen Betriebsrat, ist er bei der Einführung zu beteiligen. Die rechtliche Prüfung im Einzelfall ersetzt das nicht.')),
 ('Welche Hersteller verbaut ProVision Infra?',
  p('Mechanisch EVVA. Elektronisch EVVA AirKey und EVVA Xesar, SimonsVoss mit System 3060, den AX-Komponenten, MobileKey und FORTLOX, außerdem Keyota, Keyrent und NUKI. '
    'Wir sind an keinen Hersteller gebunden und empfehlen das System, das zu deinem Betrieb passt.')),
 ('Wie läuft die Beratung ab?',
  p('Nach einem kurzen Telefonat kommen wir zur Begehung, nehmen Türen und Abläufe auf und stellen dir zwei bis drei passende Systeme mit Vor- und Nachteilen vor. '
    'Danach bekommst du ein schriftliches Angebot für die Variante, die du wählst.')),
]
SPEC = {
 'slug': 'schliesssysteme', 'title': 'Schließsysteme im Vergleich',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Schließsysteme für Firmen im Vergleich | ProVision Infra',
         'description': 'EVVA AirKey und Xesar, SimonsVoss 3060, AX und MobileKey, NUKI, Keyota und Keyrent herstellerneutral verglichen: Welches Schließsystem passt zu dir?',
         'focuskw': 'Schließsysteme', 'bctitle': 'Schließsysteme im Vergleich', 'robots_noindex': '0'},
 'remove': ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb'],
 'set': {
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Schließsysteme für Unternehmen</span><br>im herstellerneutralen Vergleich'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Transponder oder Smartphone? Kaufen oder mieten? Cloud oder eigene Software? Wer ein Schließsystem sucht, findet vor allem Prospekte, die alle dasselbe versprechen.<br><br>'
              '<span style="font-weight: 700;">Wir verbauen Systeme von EVVA, SimonsVoss, Keyota, Keyrent und NUKI und sagen dir ehrlich, welches zu deinem Betrieb passt: '
              'nach Türen, Nutzern, Abläufen und Budget, nicht nach Marge.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Das richtige Schließsystem richtet sich nach deinem Betrieb, nicht nach dem Prospekt.'},
  '7df04ae': {'editor': p('Ein Praxisteam mit sechs Türen braucht etwas anderes als ein Logistikbetrieb im Schichtdienst oder eine Hausverwaltung mit hundert Wohnungen. '
              'Deshalb vergleichen wir nicht Datenblätter, sondern das, was im Alltag zählt: Wer bekommt wann Zutritt, wie schnell lässt sich eine Berechtigung ändern, '
              'was passiert bei Verlust, und was kostet das System über die Jahre.')},
  'd38dec5': {'editor': p('Weil wir mehrere Hersteller verbauen, müssen wir dir kein bestimmtes System verkaufen. Auf dieser Seite findest du die Systeme, mit denen wir arbeiten, '
              'und für welche Betriebe sie sich eignen. Die endgültige Empfehlung geben wir nach einer Begehung bei dir.')},
  'd7f768f': {'_title': 'Systeme im Überblick', '_element_id': 'systeme'},
  '74b6d54': {'_title': 'Systeme Überschrift', 'title': 'Die Schließsysteme, die wir verbauen: <span style="font-weight: 700; ">kurz erklärt</span>'},
  '43e5085': {'editor': p('Fünf Systemfamilien, von der klassischen Anlage mit Sicherungskarte bis zum App-Schloss mit Mobilfunk. Jede hat ihre Stärken, und manche lassen sich kombinieren.')},
  '8cc96a4': {'title': 'Mechanisch: EVVA mit Sicherungskarte'},
  '71be80d': {'editor': p('Schlüssel und Zylinder, ganz ohne Strom und Software. Der Schließplan legt fest, wer wo hineinkommt, Nachschlüssel gibt es nur gegen Sicherungskarte. '
              'Mehr dazu auf der Seite <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a>.')},
  '59a04cb': {'editor': p('Passt, wenn du wenige Türen, ein festes Team und seltene Wechsel hast.')},
  '5e90e79': {'title': 'EVVA AirKey'},
  '88e4e41': {'editor': p('Elektronische Zylinder und Wandleser, die per Smartphone oder Transponder öffnen. Berechtigungen vergibst und entziehst du online, auch aus der Ferne, '
              'und schickst sie direkt auf das Smartphone der Person.')},
  'ca72bdb': {'editor': p('Passt für Praxen, Büros und Betriebe mit mehreren Standorten, die Zutritt flexibel aus der Ferne steuern wollen.')},
  'b452400': {'title': 'EVVA Xesar'},
  '6773460': {'editor': p('Elektronische Zylinder, Beschläge und Wandleser für Karten, Schlüsselanhänger oder Kombischlüssel, verwaltet über die Xesar-Software. '
              'Ausgelegt für Betriebe mit vielen Türen, vielen Nutzern und klaren Zeitprofilen.')},
  '24f8396': {'editor': p('Passt für den Mittelstand mit Schichtbetrieb, Verwaltung, Lager und wechselnden Teams.')},
  '5860b09': {'title': 'SimonsVoss: System 3060, AX, MobileKey und FORTLOX'},
  'dc25036': {'editor': p('System 3060 ist die Plattform für große und komplexe Gebäude, kabellos und per Software verwaltet. Die AX-Generation mit Digitalzylinder AX und SmartHandle AX '
              'ist mit bestehenden Anlagen kompatibel. MobileKey macht das Smartphone zum Schlüssel und wird einfach per Web-App verwaltet. FORTLOX kombiniert einen Zylinder '
              'ohne Batterie mit einem Schlüssel mit Transponder und Bluetooth.')},
  '4838414': {'editor': p('Passt vom kleinen Betrieb mit MobileKey bis zum großen Gebäude mit System 3060, auch für Industrie und öffentliche Einrichtungen.')},
  'bb8c516': {'title': 'Smarte Schlösser und Miete: NUKI, Keyota, Keyrent'},
  '6414a37': {'editor': p('NUKI wird innen auf den vorhandenen Zylinder gesetzt und öffnet per App, Keypad oder Fob. Keyota bringt App-Schlösser mit eigener Mobilfunk-Bridge, '
              'ohne WLAN und ohne Kabel, und lässt sich über eine Schnittstelle an andere Software anbinden, etwa an Hotelsysteme. Keyrent bietet digitale Schließsysteme zur Miete.')},
  'f5080c1': {'editor': p('Kein System passt für alles. Oft ist eine Kombination die beste Lösung, zum Beispiel mechanisch für Nebenräume und elektronisch für Eingang und Lager.')},
  '3ac3e9e': {'editor': p('Passt für einzelne Türen, Ferienwohnungen und Hotels, Vereinsheime sowie Baustellen und befristete Projekte.')},
  'd70fb3d': {'_title': 'Entscheidungsfragen', '_element_id': 'entscheidung'},
  'c869af6': {'_title': 'Entscheidungsfragen', 'title': 'Drei Fragen, die die Entscheidung leichter machen'},
  '8b353e8': {'title': 'Online oder offline? Willst du Berechtigungen aus der Ferne ändern, oder reicht es, sie vor Ort an einem Gerät zu programmieren?'},
  '6519b8c': {'title': 'Smartphone, Transponder oder Schlüssel? Wer trägt was, und wie viele Menschen haben kein Diensthandy?'},
  '05ac70c': {'editor': p('Kaufen oder mieten? Für Baustellen und befristete Projekte lohnt sich Miete, für dauerhafte Lösungen meist der Kauf. Wir rechnen dir beides offen durch.')},
  'f1a5d3e': {'_title': 'Welches System passt', '_element_id': 'empfehlung'},
  'cfa4bb1': {'_title': 'Welches System passt', 'title': 'Welches Schließsystem passt zu welchem Betrieb?'},
  '4967d0c': {'title': 'Praxis, Kanzlei, kleines Büro: EVVA AirKey oder SimonsVoss MobileKey; für einzelne Türen reicht oft ein NUKI.'},
  '99ee72d': {'title': 'Handwerk und Produktion mit festem Team: mechanische EVVA-Anlage, stark genutzte Eingänge elektronisch ergänzt.'},
  '8754a23': {'editor': p('Mittelstand mit vielen Mitarbeitenden und Schichtbetrieb: EVVA Xesar oder SimonsVoss System 3060 mit AX-Komponenten.')},
  '51f3331': {'title': 'Herstellerneutrale Beratung <br><span style="font-weight: 700; ">in ganz Norddeutschland</span>'},
  '5c65e03': {'editor': p('Wir beraten dich vor Ort, egal ob du in <a href="/lueneburg/">Lüneburg</a>, <a href="/uelzen/">Uelzen</a>, <a href="/celle/">Celle</a>, '
              '<a href="/winsen-luhe/">Winsen (Luhe)</a> oder im Wendland sitzt. Unser Firmensitz ist in Bad Bevensen im Landkreis Uelzen; alle Orte findest du in der '
              '<a href="/standorte/">Übersicht unserer Standorte</a>.') +
              p('Planung, Montage und Service machen wir selbst, für jedes der hier vorgestellten Systeme.') + NAP},
  '7983242': {'title': 'Häufige Fragen zu <b>Schließsystemen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zu <br><b>Schließsystemen</b>'},
 },
 'ablauf': {**ABLAUF, 'Planung deines Systems': '<p>Du bekommst zwei bis drei passende Systeme mit Vor- und Nachteilen und ein Angebot für die Variante, die du wählst. Entscheiden kannst du in Ruhe.</p>',
            'Umsetzung': '<p>Wir montieren Zylinder, Beschläge und Wandleser und richten Software oder App vollständig ein. Konfigurieren musst du nichts.</p>'},
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
   '4967d0c': {'title': 'Mehrere Standorte und Fernverwaltung: EVVA AirKey, SimonsVoss MobileKey oder Keyota mit eigener Mobilfunk-Bridge.'},
   '99ee72d': {'title': 'Hotel, Ferienwohnung und Vermietung: Keyota mit Anbindung an die Buchungssoftware oder NUKI für einzelne Einheiten.'},
   '8754a23': {'editor': p('Baustellen und befristete Projekte: digitale Schließsysteme zur Miete von Keyrent, ohne Kauf und ohne Umbau.')},
 }),
]
