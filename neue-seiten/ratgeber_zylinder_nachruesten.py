import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz

URL = BASE + '/ratgeber/elektronischen-schliesszylinder-nachruesten/'
TITEL = 'Elektronischen Schließzylinder nachrüsten: Geht das in jede Tür?'
BESCHR = 'Elektronische Zylinder passen in die meisten Türen mit Profilzylinder. Was du vorher prüfen musst, welche Varianten es gibt und wie die Umrüstung abläuft.'
KARTEN = [
 ('Passt ein elektronischer Zylinder in meine Tür?',
  p('In den meisten Fällen ja. Die meisten Türen in Betrieben haben einen Profilzylinder, und elektronische Zylinder gibt es im gleichen Format. Entscheidend sind die Maße: '
    'die Länge außen und innen, gemessen von der Befestigungsschraube, sowie die Türdicke und der Beschlag. Wir messen jede Tür bei der Begehung aus.'),
  kurz('Hat deine Tür einen Profilzylinder, passt fast immer auch ein elektronischer.')),
 ('Zylinder, Beschlag oder Wandleser?',
  p('Der elektronische Zylinder ersetzt den alten Zylinder eins zu eins. Ein elektronischer Beschlag ersetzt Drücker und Schild, oft die bessere Wahl für stark genutzte Innentüren. '
    'Wandleser steuern Tore, Schranken und automatische Türen. Welche Komponente passt, hängt von der Tür und davon ab, wie oft sie geöffnet wird.'),
  kurz('Zylinder für den einfachen Tausch, Beschlag für viel Verkehr, Wandleser für Tore.')),
 ('Brauche ich Strom oder Kabel?',
  p('Elektronische Zylinder und Beschläge arbeiten mit Batterien, Kabel sind nicht nötig. Die Montage dauert deshalb meist nur Minuten pro Tür. Wandleser und vernetzte Komponenten brauchen teilweise einen Stromanschluss.'),
  kurz('Keine Bauarbeiten, keine Kabel, in der Regel wenige Minuten pro Tür.')),
 ('Flucht- und Brandschutztüren: besondere Regeln',
  p('Fluchttüren mit Panikschloss und Feuerschutztüren brauchen Zylinder, die für diesen Einsatz geeignet und zugelassen sind. Die Hersteller bieten dafür eigene Varianten an. '
    'Das prüfen wir vor der Bestellung, damit Fluchtweg und Brandschutz nicht beeinträchtigt werden.'),
  kurz('Bei Fluchtwegen und Brandschutztüren nur geeignete Varianten einsetzen.')),
 ('Außentüren und Tore',
  p('Für Außentüren gibt es wetterfeste Varianten, die Regen, Kälte und Staub aushalten. An Toren und Schranken arbeiten wir mit Wandlesern, die die vorhandene Steuerung ansprechen.'),
  kurz('Außen wetterfest, Tore über Wandleser.')),
 ('Mechanisch und elektronisch kombinieren',
  p('Du musst nicht alles auf einmal umrüsten. Viele Betriebe beginnen mit Haupteingang, Lager und Serverraum und lassen Nebenräume mechanisch. Eine bestehende '
    '<a href="/mechanische-schliessanlagen/">mechanische Schließanlage</a> bleibt dabei in Betrieb.'),
  kurz('Schritt für Schritt umrüsten, die bestehende Anlage läuft weiter.')),
 ('Welches System?',
  p('Wir verbauen elektronische Zylinder unter anderem von EVVA (AirKey, Xesar) und SimonsVoss (System 3060, AX, MobileKey), für einzelne Türen auch NUKI. Welches System passt, hängt davon ab, '
    'ob du per Smartphone, Transponder oder Karte öffnen und ob du online oder vor Ort verwalten willst. Einen Überblick gibt der <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.'),
  kurz('Erst klären, wie verwaltet und geöffnet werden soll, dann das System wählen.')),
 ('Was kostet die Umrüstung?',
  p('Das hängt von der Zahl der Türen, der Art der Komponenten, dem System und der Verwaltung ab. Weil elektronische Zylinder ohne Kabel auskommen, fallen in der Regel keine Bauarbeiten an. '
    'Nach der Begehung bekommst du ein schriftliches Angebot pro Tür.'),
  kurz('Kosten je Tür, ohne versteckte Bauarbeiten, nach Begehung schriftlich.')),
]
FAQ = [
 ('Kann ich einen elektronischen Schließzylinder selbst einbauen?',
  p('Der Tausch selbst ist technisch einfach, die Einrichtung des Systems, die richtigen Maße und Fluchtwegtüren sind es nicht. Wir übernehmen Aufmaß, Montage und Programmierung, damit am Ende jede Tür funktioniert.')),
 ('Passt ein elektronischer Zylinder in jede Tür?',
  p('In fast jede Tür mit Profilzylinder. Bei Sonderformen, sehr dicken Türen, Flucht- und Feuerschutztüren prüfen wir vorab, welche Variante geeignet ist.')),
 ('Wie lange hält die Batterie eines elektronischen Zylinders?',
  p('Das hängt vom Modell und davon ab, wie oft die Tür geöffnet wird. Die Zylinder melden einen niedrigen Batteriestand rechtzeitig, sodass der Wechsel planbar ist.')),
 ('Was passiert bei leerer Batterie?',
  p('Vorher warnt das System. Für den Notfall gibt es je nach Hersteller einen festgelegten Weg zur Notöffnung, den wir dir bei der Übergabe zeigen.')),
 ('Kann ich mit dem Smartphone öffnen?',
  p('Ja, mit Systemen wie EVVA AirKey, SimonsVoss MobileKey oder NUKI. Für Mitarbeitende ohne Diensthandy gibt es Transponder oder Karten.')),
 ('Muss ich alle Türen gleichzeitig umrüsten?',
  p('Nein. Du kannst mit den wichtigsten Türen beginnen und später erweitern. Die übrigen Türen bleiben mechanisch.')),
 ('Ist ein elektronischer Zylinder sicherer als ein mechanischer?',
  p('Er ist vor allem besser kontrollierbar: Verlorene Transponder sind sofort gesperrt, und jede Öffnung lässt sich protokollieren. Mechanisch hochwertige Zylinder mit Sicherungskarte sind ebenfalls sehr sicher, aber ein verlorener Schlüssel bleibt ein Risiko, bis der Zylinder getauscht ist.')),
]
SPEC = {
 'slug': 'elektronischen-schliesszylinder-nachruesten', 'parent_slug': 'ratgeber', 'title': 'Elektronischen Schließzylinder nachrüsten',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Elektronischen Schließzylinder nachrüsten: So geht’s',
         'description': BESCHR, 'focuskw': 'elektronischen Schließzylinder nachrüsten', 'bctitle': 'Schließzylinder nachrüsten', 'robots_noindex': '0'},
 'remove': REMOVE, 'karten': KARTEN,
 'set': {
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Elektronischen Schließzylinder nachrüsten:</span><br>Geht das in jede Tür?'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Transponder statt Schlüsselbund, Berechtigungen per Klick statt Zylindertausch: Viele Betriebe wollen umsteigen und fürchten Bauarbeiten, Kabel und neue Türen. '
              'Die gute Nachricht: In den meisten Fällen ist nichts davon nötig.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Ja, in fast jede Tür mit Profilzylinder, ohne Kabel und ohne Bauarbeiten.'},
  '7df04ae': {'editor': p('Elektronische Zylinder haben das gleiche Format wie mechanische und arbeiten mit Batterie. Sie werden einfach getauscht, meist in wenigen Minuten pro Tür. '
              'Prüfen musst du die Maße, die Art der Tür und besondere Anforderungen an Flucht- und Brandschutztüren.')},
  'd38dec5': {'editor': p('Dieser Ratgeber gibt dir einen Überblick. Für dein Gebäude prüfen wir jede Tür bei einer Begehung. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Was du vor dem Nachrüsten <span style="font-weight: 700; ">wissen solltest</span>'},
  '43e5085': {'editor': p('Acht Fragen, die wir bei fast jeder Umrüstung hören, mit ehrlichen Antworten aus der Praxis.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste vor der Umrüstung'},
  '8b353e8': {'title': 'Alle Türen aufgelistet, Zylinderlängen gemessen, Flucht- und Brandschutztüren markiert.'},
  '6519b8c': {'title': 'Festgelegt, wer per Smartphone, Transponder oder Karte öffnet, und ob online verwaltet wird.'},
  '05ac70c': {'editor': p('Reihenfolge geplant: zuerst stark genutzte und sensible Türen, Nebenräume später oder mechanisch.')},
  'f1a5d3e': {'_title': 'Passend dazu', '_element_id': 'weiterlesen'},
  'cfa4bb1': {'_title': 'Passend dazu', 'title': 'Passend dazu'},
  '4967d0c': {'title': '<a href="/zutrittssystem/" style="color: #FBC91B;">Elektronische Schließanlagen</a>: unsere Pakete für Zutrittskontrolle mit Service.'},
  '99ee72d': {'title': '<a href="/schliesssysteme/" style="color: #FBC91B;">Schließsysteme im Vergleich</a>: EVVA, SimonsVoss, Keyota, Keyrent und NUKI.'},
  '8754a23': {'editor': p('<a href="/ratgeber/schluessel-verloren-unternehmen/">Schlüssel im Unternehmen verloren</a>: was jetzt zu tun ist.')},
  '51f3331': {'title': 'Umrüsten ohne <br><span style="font-weight: 700; ">Betriebsstillstand</span>'},
  '5c65e03': {'editor': p('Wir rüsten Tür für Tür um, während dein Betrieb weiterläuft, und richten Software oder App vollständig ein. Im Einsatz sind wir in ganz Norddeutschland, '
              'alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zum <b>Nachrüsten elektronischer Zylinder</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zum <br><b>Nachrüsten elektronischer Zylinder</b>'},
 },
 'faq': FAQ,
 'schema': artikel_schema(URL, TITEL, BESCHR),
}
