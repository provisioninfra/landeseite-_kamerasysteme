import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz, ORDER, GRUENDER, PRESSE, video_kasten, cta, stell_dir_vor

URL = BASE + '/ratgeber/elektronischen-schliesszylinder-nachruesten/'
TITEL = 'Elektronischen Schließzylinder nachrüsten: Geht das in jede Tür?'
BESCHR = 'Elektronische Zylinder passen in die meisten Türen mit Profilzylinder. Was du vorher prüfen musst, welche Varianten es gibt und wie die Umrüstung abläuft.'
KARTEN = [
 ('Passt ein elektronischer Zylinder in meine Tür?',
  p('Sehr wahrscheinlich. In den meisten Betriebstüren steckt ein Profilzylinder, und elektronische Zylinder gibt es in genau diesem Format. Wichtig sind die Maße: '
    'Gemessen wird von der Stulpschraube nach außen und nach innen, dazu kommen Türblatt und Beschlag. Bei der Begehung messen wir jede Tür selbst aus, damit kein Zylinder zu kurz geliefert wird oder zu weit übersteht.'),
  kurz('Steckt ein Profilzylinder in der Tür, passt fast immer auch ein elektronischer.')),
 ('Welche Komponente passt zu welcher Tür?',
  p('Für den einfachen Tausch nimmst du den elektronischen Zylinder, er ersetzt den alten eins zu eins. An stark genutzten Innentüren ist ein elektronischer Beschlag oft die bessere Wahl. '
    'Er übernimmt Drücker und Schild und lässt sich bequem über die Klinke bedienen. Tore und Schranken steuerst du über einen Wandleser, der an die vorhandene Torsteuerung angeschlossen wird.'),
  kurz('Wie oft eine Tür benutzt wird, entscheidet über die passende Komponente.')),
 ('Brauche ich Strom oder Kabel?',
  p('Für Zylinder und Beschläge nicht. Beide laufen mit Batterie, deshalb muss niemand Leitungen verlegen oder die Zarge anbohren. '
    'Anders beim Wandleser und bei vernetzten Komponenten: Sie brauchen in vielen Fällen einen Stromanschluss in der Nähe.'),
  kurz('Zylinder und Beschlag kommen mit Batterie aus, der Wandleser braucht meist Strom.')),
 ('Flucht- und Brandschutztüren: besondere Regeln',
  p('Hier lohnt sich ein zweiter Blick. In einer Fluchttür mit Panikschloss muss der Zylinder zum Schloss passen, oft ist dafür eine Variante mit Freilauf nötig, damit der Schließbart die Panikfunktion nicht blockiert. '
    'Feuerschutztüren brauchen Zylinder, die für diesen Einsatz zugelassen sind, und die Hersteller haben dafür eigene Modelle. Wir prüfen das vor der Bestellung, damit dein Fluchtweg im Ernstfall frei bleibt.'),
  kurz('An Fluchtwegen und Feuerschutztüren kommen nur geeignete Varianten in Frage.')),
 ('Außentüren und Tore',
  p('Am Haupteingang bekommt die Außenseite Regen ab, im Winter auch Frost. Dafür gibt es wetterfeste Varianten. Tore und Schranken binden wir über Wandleser an, die mit der vorhandenen Steuerung zusammenarbeiten.'),
  kurz('Draußen kommen wetterfeste Modelle zum Einsatz, Tore laufen über Wandleser.')),
 ('Mechanisch und elektronisch kombinieren',
  p('Du musst nicht alles auf einmal umrüsten. Viele Betriebe starten mit Haupteingang und Lager, die Nebenräume bleiben vorerst mechanisch. Deine bestehende '
    '<a href="/mechanische-schliessanlagen/">mechanische Schließanlage</a> läuft dabei einfach weiter.'),
  kurz('Umrüsten geht Schritt für Schritt, die alte Anlage bleibt in Betrieb.')),
 ('Welches System?',
  p('Elektronische Zylinder verbauen wir unter anderem von EVVA (AirKey, Xesar) und SimonsVoss (System 3060, AX, MobileKey), für einzelne Türen auch NUKI. Den Ausschlag gibt meist die Verwaltung. '
    'Willst du per Smartphone öffnen und Berechtigungen von unterwegs vergeben? Oder reichen Transponder, die das Büro ausgibt? Einen Überblick gibt der <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.'),
  kurz('Erst klären, wie verwaltet wird. Danach steht das System fast von selbst fest.')),
 ('Was kostet die Umrüstung?',
  p('Am meisten zählt, wie viele Türen umgerüstet werden und für welches System du dich entscheidest. Bauarbeiten fallen in der Regel keine an, denn Zylinder und Beschläge kommen ohne Kabel aus. '
    'Nach der Begehung bekommst du ein schriftliches Angebot, in dem jede Tür einzeln aufgeführt ist.'),
  kurz('Nach der Begehung bekommst du den Preis für jede Tür schriftlich.')),
]
FAQ = [
 ('Kann ich einen elektronischen Schließzylinder selbst einbauen?',
  p('Der Tausch selbst ist handwerklich einfach. Knifflig wird es bei den Maßen und bei Fluchtwegtüren, und auch die Software will sauber eingerichtet sein. Wir übernehmen Aufmaß und Programmierung, damit am Ende jede Tür so schließt, wie sie soll.')),
 ('Passt ein elektronischer Zylinder in jede Tür?',
  p('In fast jede Tür mit Profilzylinder. Bei Sonderformen und Fluchttüren prüfen wir vorher, welche Variante geeignet ist.')),
 ('Wie lange hält die Batterie eines elektronischen Zylinders?',
  p('Das hängt vom Modell ab und davon, wie oft die Tür am Tag geöffnet wird. Rechtzeitig vorher meldet der Zylinder einen niedrigen Batteriestand, so kannst du den Wechsel in Ruhe einplanen.')),
 ('Was passiert bei leerer Batterie?',
  p('So weit kommt es selten, denn das System warnt vorher. Für den Notfall sieht jeder Hersteller einen eigenen Weg zur Notöffnung vor. Den zeigen wir dir bei der Übergabe.')),
 ('Kann ich mit dem Smartphone öffnen?',
  p('Ja, zum Beispiel mit EVVA AirKey, SimonsVoss MobileKey oder NUKI. Wer kein Diensthandy hat, bekommt einen Transponder oder eine Karte.')),
 ('Muss ich alle Türen gleichzeitig umrüsten?',
  p('Nein. Fang mit den wichtigsten Türen an und erweitere später. Bis dahin bleiben die übrigen Türen mechanisch.')),
 ('Ist ein elektronischer Zylinder sicherer als ein mechanischer?',
  p('Vor allem lässt er sich besser kontrollieren. Einen verlorenen Transponder sperrst du sofort, und auf Wunsch wird jede Öffnung protokolliert. Hochwertige mechanische Zylinder mit Sicherungskarte sind ebenfalls sehr sicher. Ein verlorener Schlüssel bleibt dort aber ein Risiko, bis der Zylinder getauscht ist.')),
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
    'Der Serverraum bleibt den zwei Menschen vorbehalten, die dort wirklich hineindürfen.']) + [cta('So kommst du zu deinen elektronischen Zylindern', 'Im Erstgespräch klären wir, welche Türen sich zuerst lohnen und welches System dazu passt. Danach weißt du, was die Umrüstung kostet.', nach='f1a5d3e'),
   video_kasten('Zutritt und Kameras lassen sich gut zusammen planen. Mit Alarm aufs Handy siehst du sofort, was an Tor und Eingang los ist.'), PRESSE], 'karten': KARTEN,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Elektronischen Schließzylinder nachrüsten:</span><br>Geht das in jede Tür?'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Stahltür am Lager, Glastür am Eingang: Die Türen in deinem Betrieb sehen ganz unterschiedlich aus. Für den elektronischen Zylinder zählt trotzdem meist nur eine Frage. '
              'Steckt ein Profilzylinder in der Tür? Dann musst du für Transponder oder Smartphone weder Wände aufstemmen noch Türen tauschen.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Ja. Fast jede Tür mit Profilzylinder lässt sich ohne Bauarbeiten umrüsten.'},
  '7df04ae': {'editor': p('Ein elektronischer Zylinder hat dieselbe Bauform wie dein bisheriger und holt seinen Strom aus einer Batterie. Wir lösen die Stulpschraube, ziehen den alten Zylinder heraus und setzen den neuen ein. '
              'Pro Tür dauert das meist wenige Minuten. Vorher klären wir zwei Dinge: ob die Maße stimmen und ob die Tür an einem Fluchtweg oder Brandabschnitt liegt.')},
  'd38dec5': {'editor': p('Dieser Ratgeber verschafft dir einen Überblick. Ob deine Türen Besonderheiten haben, sehen wir bei der Begehung vor Ort. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Was du vor dem Nachrüsten <span style="font-weight: 700; ">wissen solltest</span>'},
  '43e5085': {'editor': p('Diese acht Fragen hören wir bei fast jeder Umrüstung. Hier sind unsere Antworten aus der Praxis.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste vor der Umrüstung'},
  '8b353e8': {'title': 'Jede Tür steht auf einer Liste, Fluchttüren sind gesondert markiert.'},
  '6519b8c': {'title': 'Du weißt, wer per Smartphone öffnet und wer einen Transponder bekommt.'},
  '05ac70c': {'editor': p('Die Reihenfolge steht fest: Stark genutzte Türen kommen zuerst, Nebenräume später.')},
  'f1a5d3e': {'_title': 'Passend dazu', '_element_id': 'weiterlesen'},
  'cfa4bb1': {'_title': 'Passend dazu', 'title': 'Passend dazu'},
  '4967d0c': {'title': '<a href="/zutrittssystem/" style="color: #FBC91B;">Elektronische Schließanlagen</a>: unsere Pakete für Zutrittskontrolle mit Service.'},
  '99ee72d': {'title': '<a href="/schliesssysteme/" style="color: #FBC91B;">Schließsysteme im Vergleich</a>: EVVA, SimonsVoss, Keyota, Keyrent und NUKI.'},
  '8754a23': {'editor': p('<a href="/ratgeber/schluessel-verloren-unternehmen/">Schlüssel im Unternehmen verloren</a>: was jetzt zu tun ist.')},
  '51f3331': {'title': 'Umrüsten ohne <br><span style="font-weight: 700; ">Betriebsstillstand</span>'},
  '5c65e03': {'editor': p('Wir rüsten Tür für Tür um, dein Betrieb läuft dabei weiter. Bevor wir gehen, ist die Software oder App fertig eingerichtet. Unterwegs sind wir in ganz Norddeutschland, '
              'alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zum <b>Nachrüsten elektronischer Zylinder</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zum <br><b>Nachrüsten elektronischer Zylinder</b>'},
 },
 'faq': FAQ,
 'schema': artikel_schema(URL, TITEL, BESCHR),
}
