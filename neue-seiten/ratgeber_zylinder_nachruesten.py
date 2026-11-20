import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz, ORDER, GRUENDER, PRESSE, video_kasten, cta, stell_dir_vor

URL = BASE + '/ratgeber/elektronischen-schliesszylinder-nachruesten/'
TITEL = 'Elektronischen Schließzylinder nachrüsten: Geht das in jede Tür?'
BESCHR = 'Elektronische Zylinder passen in die meisten Türen mit Profilzylinder. Was du vorher prüfen musst, welche Varianten es gibt und wie die Umrüstung abläuft.'
KARTEN = [
 ('Passt ein elektronischer Zylinder in meine Tür?',
  p('In den meisten Fällen ja. Die meisten Türen in Betrieben haben einen Profilzylinder, und elektronische Zylinder gibt es im gleichen Format. Entscheidend sind die Maße: '
    'die Länge außen und innen, gemessen von der Befestigungsschraube, sowie die Türdicke und der Beschlag. Wir messen jede Tür bei der Begehung aus.'),
  kurz('Hat deine Tür einen Profilzylinder, passt fast immer auch ein elektronischer.')),
 ('Welche Komponente passt zu welcher Tür?',
  p('Der elektronische Zylinder ersetzt den alten Zylinder eins zu eins. Ein elektronischer Beschlag ersetzt Drücker und Schild, oft die bessere Wahl für stark genutzte Innentüren. '
    'Wandleser steuern Tore und Schranken. Welche Komponente passt, hängt von der Tür und davon ab, wie oft sie geöffnet wird.'),
  kurz('Zylinder für den einfachen Tausch, Beschlag für viel Verkehr, Wandleser für Tore.')),
 ('Brauche ich Strom oder Kabel?',
  p('Elektronische Zylinder und Beschläge arbeiten mit Batterien, Kabel sind nicht nötig. Die Montage dauert deshalb meist nur Minuten pro Tür. Wandleser und vernetzte Komponenten brauchen teilweise einen Stromanschluss.'),
  kurz('Keine Bauarbeiten, keine Kabel, in der Regel wenige Minuten pro Tür.')),
 ('Flucht- und Brandschutztüren: besondere Regeln',
  p('Fluchttüren mit Panikschloss und Feuerschutztüren brauchen Zylinder, die für diesen Einsatz geeignet und zugelassen sind. Die Hersteller bieten dafür eigene Varianten an. '
    'Das prüfen wir vor der Bestellung, damit der Fluchtweg sicher bleibt.'),
  kurz('Bei Fluchtwegen und Brandschutztüren nur geeignete Varianten einsetzen.')),
 ('Außentüren und Tore',
  p('Für Außentüren gibt es wetterfeste Varianten, denen Regen und Frost nichts ausmachen. An Toren und Schranken arbeiten wir mit Wandlesern, die die vorhandene Steuerung ansprechen.'),
  kurz('Außen wetterfest, Tore über Wandleser.')),
 ('Mechanisch und elektronisch kombinieren',
  p('Du musst nicht alles auf einmal umrüsten. Viele Betriebe beginnen mit Haupteingang und Lager und lassen Nebenräume mechanisch. Eine bestehende '
    '<a href="/mechanische-schliessanlagen/">mechanische Schließanlage</a> bleibt dabei in Betrieb.'),
  kurz('Schritt für Schritt umrüsten, die bestehende Anlage läuft weiter.')),
 ('Welches System?',
  p('Wir verbauen elektronische Zylinder unter anderem von EVVA (AirKey, Xesar) und SimonsVoss (System 3060, AX, MobileKey), für einzelne Türen auch NUKI. Welches System passt, hängt davon ab, '
    'ob du lieber per Smartphone oder mit Transponder öffnest und ob du aus der Ferne verwalten willst. Einen Überblick gibt der <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.'),
  kurz('Kläre zuerst, wie verwaltet werden soll, und wähle danach das System.')),
 ('Was kostet die Umrüstung?',
  p('Das hängt vor allem von der Zahl der Türen und vom gewählten System ab. Weil elektronische Zylinder ohne Kabel auskommen, fallen in der Regel keine Bauarbeiten an. '
    'Nach der Begehung bekommst du ein schriftliches Angebot pro Tür.'),
  kurz('Kosten je Tür, ohne versteckte Bauarbeiten, nach Begehung schriftlich.')),
]
FAQ = [
 ('Kann ich einen elektronischen Schließzylinder selbst einbauen?',
  p('Der Tausch selbst ist technisch einfach, die Einrichtung des Systems, die richtigen Maße und Fluchtwegtüren sind es nicht. Wir übernehmen Aufmaß und Programmierung, damit am Ende jede Tür funktioniert.')),
 ('Passt ein elektronischer Zylinder in jede Tür?',
  p('In fast jede Tür mit Profilzylinder. Bei Sonderformen und Fluchttüren prüfen wir vorab, welche Variante geeignet ist.')),
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
 'remove': REMOVE,
 'order': ORDER, 'handy_css': True,
 'graft': stell_dir_vor([
    'Neue Mitarbeitende bekommen ihren Transponder am ersten Tag, und kein Schlüssel muss nachgemacht werden.',
    'Handwerker kommen zur vereinbarten Zeit ins Gebäude, ohne dass jemand zum Aufschließen bereitsteht.',
    'Ein verlorener Transponder ist gesperrt, bevor jemand den Verlust ausnutzen kann.',
    'Nach einem Vorfall siehst du sofort, wer zuletzt im Lager war.',
    'Du entziehst Zugänge mit einem Klick, wenn jemand den Betrieb verlässt.',
    'Niemand muss mehr in Schubladen nach dem richtigen Schlüssel suchen.',
    'Auch ein zweiter Standort lässt sich über dieselbe Software steuern.',
    'Der Serverraum bleibt den zwei Menschen vorbehalten, die dort wirklich hineindürfen.']) + [cta('So kommst du zu deinen elektronischen Zylindern', 'Im Erstgespräch klären wir, welche Türen sich zuerst lohnen und welches System passt. Danach weißt du, was die Umrüstung kostet.', nach='f1a5d3e'),
   video_kasten('Zutritt und Kameras lassen sich gemeinsam planen. Kamerasysteme mit Alarm aufs Handy zeigen dir, was an Tor und Eingang passiert.'), PRESSE], 'karten': KARTEN,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Elektronischen Schließzylinder nachrüsten:</span><br>Geht das in jede Tür?'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Viele Betriebe würden gern auf Transponder umsteigen und fürchten sich vor Bauarbeiten und neuen Türen. '
              'In den meisten Fällen ist beides unnötig.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Ja, fast jede Tür mit Profilzylinder lässt sich ohne Bauarbeiten umrüsten.'},
  '7df04ae': {'editor': p('Elektronische Zylinder haben das gleiche Format wie mechanische und arbeiten mit Batterie. Sie werden einfach getauscht, meist in wenigen Minuten pro Tür. '
              'Prüfen musst du die Maße, die Art der Tür und besondere Anforderungen an Flucht- und Brandschutztüren.')},
  'd38dec5': {'editor': p('Dieser Ratgeber gibt dir einen Überblick. Für dein Gebäude prüfen wir jede Tür bei einer Begehung. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Was du vor dem Nachrüsten <span style="font-weight: 700; ">wissen solltest</span>'},
  '43e5085': {'editor': p('Acht Fragen, die wir bei fast jeder Umrüstung hören, mit ehrlichen Antworten aus der Praxis.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste vor der Umrüstung'},
  '8b353e8': {'title': 'Alle Türen sind aufgelistet, und Fluchttüren sind gesondert markiert.'},
  '6519b8c': {'title': 'Du weißt, wer per Smartphone öffnet und wer einen Transponder bekommt.'},
  '05ac70c': {'editor': p('Die Reihenfolge steht: Stark genutzte Türen kommen zuerst, Nebenräume später.')},
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
