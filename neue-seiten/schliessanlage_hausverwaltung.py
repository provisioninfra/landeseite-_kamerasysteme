import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD, ORDER, GRUENDER, PRESSE, video_kasten, cta, analyse, stell_dir_vor, vorteile

URL = BASE + '/schliessanlage-hausverwaltung/'
def p(t): return '<p>' + t + '</p>'
FAQ = [
 ('Was kostet eine Schließanlage für ein Mehrfamilienhaus?',
  p('Das hängt von der Zahl der Wohnungen und Gemeinschaftstüren ab, von der Frage mechanisch oder elektronisch und davon, wie viele Schlüssel oder Transponder im Umlauf sein sollen. '
    'Nach einer Begehung bekommst du ein schriftliches Angebot, das du der Eigentümergemeinschaft oder dem Eigentümer vorlegen kannst.')),
 ('Ein Mieter hat seinen Schlüssel verloren. Wer zahlt den Austausch?',
  p('Das regeln der Mietvertrag und im Streitfall die Gerichte, und es hängt davon ab, ob der Verlust verschuldet war und ob tatsächlich ein Missbrauchsrisiko besteht. '
    'Viele private Haftpflichtversicherungen decken den Verlust fremder Schlüssel ab; ein Blick in die Police lohnt sich. Wir liefern die technische Einschätzung, welche Zylinder betroffen sind und was der Austausch kostet.')),
 ('Muss bei Schlüsselverlust die ganze Schließanlage getauscht werden?',
  p('Nicht immer. Öffnet der verlorene Schlüssel nur die eigene Wohnung, reicht oft der Tausch dieses einen Zylinders. Passt er auch zu den Gemeinschaftstüren, '
    'sind deren Zylinder ebenfalls betroffen. Bei einer elektronischen Anlage sperrst du den verlorenen Transponder einfach, ohne etwas zu tauschen.')),
 ('Lohnt sich eine elektronische Schließanlage im Mehrfamilienhaus?',
  p('Vor allem dort, wo Mieter häufig wechseln oder Schlüssel immer wieder verloren gehen. Viele Verwaltungen digitalisieren zuerst die Gemeinschaftstüren '
    'und lassen die Wohnungstüren mechanisch. Welche Systeme sich eignen, zeigt der <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.')),
 ('Wer entscheidet in einer Eigentümergemeinschaft über eine neue Schließanlage?',
  p('In der Regel die Eigentümerversammlung per Beschluss. Wir unterstützen die Verwaltung mit einem verständlichen Angebot und einem Entwurf des Schließplans. Auf Wunsch erläutern wir die Varianten auch persönlich.')),
 ('Sind Wartungskosten für die Schließanlage auf die Mieter umlegbar?',
  p('Das hängt vom Mietvertrag und von der Art der Kosten ab. Bitte lass die Umlage im Einzelfall rechtlich prüfen. Wir stellen dir Wartung und Reparatur getrennt aus, damit die Abrechnung einfacher wird.')),
 ('Kann ich nur die Haustür digitalisieren?',
  p('Ja. Ein elektronischer Zylinder oder ein Wandleser an der Haustür lässt sich mit einer bestehenden mechanischen Anlage kombinieren. Dienstleister bekommen dann ein Zeitfenster, '
    'und die Wohnungsschlüssel bleiben, wie sie sind.')),
 ('Ist Videoüberwachung im Mehrfamilienhaus erlaubt?',
  p('Nur in engen Grenzen. Gemeinschaftsflächen wie Fahrradkeller oder Tiefgarage können in Frage kommen, wenn es einen berechtigten Anlass gibt, Hinweisschilder angebracht sind und die Rechte der Bewohner gewahrt bleiben. '
    'Das sollte vorher rechtlich geprüft und mit der Eigentümergemeinschaft abgestimmt werden. Mehr zur <a href="/kamerasysteme/">Videoüberwachung</a>.')),
 ('Wie läuft die Umrüstung in einem bewohnten Haus ab?',
  p('Wir kündigen den Termin über die Verwaltung an, tauschen Gemeinschaftstüren zuerst und Wohnungstüren nach Absprache mit den Bewohnern. Neue Schlüssel oder Transponder werden gegen Unterschrift übergeben, '
    'damit du lückenlos dokumentiert hast, wer was bekommen hat.')),
 ('Arbeitet ihr auch langfristig mit Hausverwaltungen zusammen?',
  p('Ja. Nach der Umrüstung bleiben wir Ansprechpartner für Mieterwechsel und Wartung. Verwaltung und Hausmeister haben dafür einen festen Kontakt bei uns.')),
]
SPEC = {
 'slug': 'schliessanlage-hausverwaltung', 'title': 'Schließanlagen für Hausverwaltungen',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Schließanlage Mehrfamilienhaus & Hausverwaltung | ProVision',
         'description': 'Schließanlagen für Hausverwaltungen und Mehrfamilienhäuser: Schließplan, Mieterwechsel ohne Zylindertausch, Schlüsselverlust, Umrüstung auf elektronisch.',
         'focuskw': 'Schließanlage Mehrfamilienhaus', 'bctitle': 'Hausverwaltungen', 'robots_noindex': '0'},
 'remove': ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb'],
 'order': ORDER, 'handy_css': True,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Schließanlagen für Hausverwaltungen</span><br>und Mehrfamilienhäuser'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Ein Mieter zieht aus und gibt nur zwei von drei Schlüsseln zurück. Bei der nächsten Eigentümerversammlung fragt dann jemand, wer eigentlich noch einen Schlüssel zum Keller hat.<br><br>'
              '<span style="font-weight: 700;">ProVision Infra plant und betreut Schließanlagen für Wohnanlagen, mechanisch mit Sicherungskarte oder elektronisch mit Transponder. '
              'So wird ein Mieterwechsel wieder zur Formsache.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Weniger Schlüsselchaos, weniger Kosten, weniger Rückfragen.'},
  '7df04ae': {'editor': p('In einem Mehrfamilienhaus öffnen viele Schlüssel dieselben Türen, von der Haustür bis zur Tiefgarage. Ein verlorener Schlüssel betrifft deshalb alle Bewohner, '
              'und die Kosten landen schnell bei der Gemeinschaft. Eine gut geplante Schließanlage begrenzt genau dieses Risiko.')},
  'd38dec5': {'editor': p('Wir nehmen das Objekt auf, entwerfen den Schließplan mit dir und rüsten im bewohnten Haus um, ohne dass jemand vor verschlossener Tür steht. '
              'Auch danach hast du einen festen Ansprechpartner, etwa für Mieterwechsel oder Nachschlüssel.')},
  'd7f768f': {'_title': 'Lösungen für Wohnanlagen', '_element_id': 'loesungen'},
  '74b6d54': {'_title': 'Lösungen Überschrift', 'title': 'Was eine Schließanlage im Mehrfamilienhaus <span style="font-weight: 700; ">leisten muss</span>'},
  '43e5085': {'editor': p('Fünf Aufgaben, die in Wohnanlagen immer wieder auftauchen, und wie wir sie lösen.')},
  '8cc96a4': {'title': 'Ein Schließplan für das ganze Haus'},
  '71be80d': {'editor': p('Jeder Wohnungsschlüssel öffnet die eigene Wohnung und die gemeinsamen Türen, der Hausmeister kommt in Technik- und Nebenräume, die Verwaltung behält den Überblick. '
              'Alles steht im Schließplan, den du schriftlich bekommst.')},
  '59a04cb': {'editor': p('Jede Ausgabe und Rückgabe lässt sich nachvollziehen, auch nach Jahren und Verwalterwechseln.')},
  '5e90e79': {'title': 'Mieterwechsel ohne Zylindertausch'},
  '88e4e41': {'editor': p('Mit elektronischen Zylindern an Haustür und Gemeinschaftstüren sperrst du alte Transponder und gibst neue aus. Bei mechanischen Anlagen tauschen wir gezielt nur den Wohnungszylinder, '
              'die gemeinsamen Türen bleiben unberührt.')},
  'ca72bdb': {'editor': p('Mit dem Sperren des Transponders ist der Auszug erledigt. Einen Handwerkertermin braucht es dafür nicht.')},
  'b452400': {'title': 'Schlüsselverlust: schnell und gezielt reagieren'},
  '6773460': {'editor': p('Geht ein Schlüssel verloren, prüfen wir anhand des Schließplans, welche Türen betroffen sind, und tauschen nur dort. Bei elektronischen Komponenten genügt das Sperren des Transponders. '
              'Nachschlüssel gibt es bei Anlagen mit Sicherungskarte nur gegen Vorlage der Karte.')},
  '24f8396': {'editor': p('Die Kosten bleiben überschaubar, und kein fremder Schlüssel öffnet mehr die Haustür.')},
  '5860b09': {'title': 'Zeitfenster für Dienstleister'},
  'dc25036': {'editor': p('Reinigung und Gartenpflege bekommen einen Transponder oder eine App-Berechtigung, die nur zu festgelegten Zeiten öffnet. Schlüssel musst du dafür nicht mehr verteilen.')},
  '4838414': {'editor': p('Kein Schlüssel muss mehr unter der Fußmatte liegen.')},
  'bb8c516': {'title': 'Gemeinschaftsflächen im Blick'},
  '6414a37': {'editor': p('Wo es einen berechtigten Anlass gibt, etwa wiederholte Fahrraddiebstähle, planen wir <a href="/kamerasysteme/">Videoüberwachung</a> an Gemeinschaftsflächen: mit Hinweisschildern, '
              'eng begrenzten Bildausschnitten und nach Abstimmung mit der Eigentümergemeinschaft.')},
  'f5080c1': {'editor': p('Mechanisch arbeiten wir mit EVVA, elektronisch unter anderem mit EVVA AirKey und SimonsVoss. Die Kameras stammen von TP-Link VIGI.')},
  '3ac3e9e': {'editor': p('Türen und Kameras plant die Verwaltung so mit einem einzigen Ansprechpartner.')},
  'd70fb3d': {'_title': 'Mechanisch oder elektronisch', '_element_id': 'vergleich'},
  'c869af6': {'_title': 'Mechanisch oder elektronisch', 'title': 'Welche Anlage passt zu deinem Objekt?'},
  '8b353e8': {'title': 'Mechanisch: für kleine Häuser mit wenigen Parteien und seltenen Wechseln. Robust, ohne Strom, mit Sicherungskarte gegen Kopien.'},
  '6519b8c': {'title': 'Elektronisch: für große Wohnanlagen mit häufigen Mieterwechseln und vielen Dienstleistern. Verlorene Transponder sind mit einem Klick gesperrt.'},
  '05ac70c': {'editor': p('Gemischt: Gemeinschaftstüren elektronisch, Wohnungen mechanisch. Für viele Verwaltungen der wirtschaftlichste Weg. Mehr dazu im '
              '<a href="/schliesssysteme/">Vergleich der Schließsysteme</a> und auf der Seite <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a>.')},
  'f1a5d3e': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'cfa4bb1': {'_title': 'Leistungen', 'title': 'Unsere Leistungen für Hausverwaltungen'},
  '4967d0c': {'title': 'Bestandsaufnahme und Planung: Wir nehmen alle Türen des Objekts auf und entwerfen den Schließplan mit dir.'},
  '99ee72d': {'title': 'Unterlagen für die Eigentümerversammlung: verständliches Angebot und Varianten, die du vorlegen kannst.'},
  '8754a23': {'editor': p('Umrüstung im bewohnten Haus: Gemeinschaftstüren zuerst, Wohnungen nach Absprache, Schlüsselübergabe gegen Unterschrift.')},
  '51f3331': {'title': 'Für Hausverwaltungen <br><span style="font-weight: 700; ">in ganz Norddeutschland</span>'},
  '5c65e03': {'editor': p('Wir betreuen Wohnanlagen in <a href="/lueneburg/">Lüneburg</a>, <a href="/uelzen/">Uelzen</a>, <a href="/celle/">Celle</a>, <a href="/winsen-luhe/">Winsen (Luhe)</a>, '
              'im Wendland und im ganzen Raum zwischen Hamburg und Hannover. Unser Firmensitz ist in Bad Bevensen im Landkreis Uelzen; alle Orte findest du in der '
              '<a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zu <b>Schließanlagen im Mehrfamilienhaus</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zu <br><b>Schließanlagen im Mehrfamilienhaus</b>'},
 },
 'graft': stell_dir_vor([
    'Ein Mieter zieht aus, und sein Transponder für die Haustür ist noch am selben Tag gesperrt.',
    'Der Hausmeister kommt in die Technikräume, ohne einen Generalschlüssel mit sich herumzutragen.',
    'Ein verlorener Schlüssel betrifft nur noch eine Wohnung und nicht mehr das ganze Haus.',
    'Nach einem Diebstahl im Fahrradkeller weißt du sofort, wann die Tür geöffnet wurde.',
    'Neue Mieter bekommen ihren Zugang, bevor der Umzugswagen vor der Tür steht.',
    'Kein Schlüssel muss mehr unter der Fußmatte oder beim Nachbarn liegen.',
    'Alle Objekte deiner Verwaltung steuerst du über eine einzige Oberfläche.',
    'Heizungsraum und Dachzugang bleiben den Fachfirmen vorbehalten, die dort arbeiten dürfen.']) + [
   analyse('Bevor wir umrüsten, sehen wir uns dein Objekt genau an:',
           ('Wie viele Parteien und Türen gibt es?', 'Wie oft wechseln die Mieter?', 'Wer braucht Zugang zur Technik?'),
           'Daraus entsteht ein Schließplan, den du der Eigentümergemeinschaft vorlegen kannst.'),
  ] + vorteile([
    ('Übersicht über das ganze Objekt:', 'Du siehst auf einen Blick, wer welche Tür öffnen darf.'),
    ('Mieterwechsel in Minuten:', 'Den alten Transponder sperrst du, den neuen gibst du bei der Wohnungsübergabe aus.'),
    ('Zugänge nach Funktion:', 'Mieter öffnen Haustür und Keller, der Hausmeister zusätzlich die Technikräume.'),
    ('Zeitfenster für Dienstleister:', 'Die Reinigung kommt nur an ihren Tagen ins Haus.'),
    ('Weniger Wege für die Verwaltung:', 'Schlüssel müssen nicht mehr abgeholt und zurückgebracht werden.'),
    ('Geringere Kosten bei Verlust:', 'Gesperrt wird ein Transponder, die Zylinder der Gemeinschaftstüren bleiben.'),
    ('Klare Abrechnung:', 'Wartung und Reparatur stellen wir getrennt aus, das erleichtert die Nebenkostenabrechnung.'),
    ('Dokumentierte Ausgabe:', 'Jede Ausgabe von Schlüsseln und Transpondern ist mit Unterschrift belegt.'),
    ('Gute Grundlage für Beschlüsse:', 'Die Eigentümerversammlung entscheidet auf Basis eines klaren Angebots mit Varianten.'),
  ]) + [
   cta('So kommt dein Objekt zu einer neuen Schließanlage', 'Im Erstgespräch klären wir, ob sich eine elektronische Haustür lohnt oder eine mechanische Anlage reicht. Danach bekommst du Unterlagen, die du direkt weitergeben kannst.'),
   video_kasten('Für Fahrradkeller und Tiefgarage planen wir Kameras nur dort, wo es einen berechtigten Anlass gibt. Hinweisschilder und eng begrenzte Bildausschnitte gehören immer dazu.'),
   PRESSE,
 ],
 'ablauf': {
  'Erstgespräch': p('In einem kurzen Telefonat erzählst du uns, wie viele Parteien das Haus hat und wo es heute hakt. Du bekommst sofort eine ehrliche erste Einschätzung.'),
  'Termin vor Ort': p('Wir gehen mit dir oder dem Hausmeister durch das Objekt und nehmen jede Tür auf, von der Haustür bis zur Tiefgarage. Den Kostenrahmen nennen wir dir noch vor Ort.'),
  'Planung deines Systems': p('Du bekommst den Schließplan-Entwurf und ein Angebot mit Varianten, das du der Eigentümergemeinschaft vorlegen kannst.'),
  'Umsetzung': p('Wir rüsten im bewohnten Haus um, Gemeinschaftstüren zuerst, Wohnungen nach Absprache. Niemand steht vor verschlossener Tür.'),
  'Übergabe & Betreuung': p('Schlüssel und Transponder werden gegen Unterschrift übergeben. Auch danach kümmern wir uns um Mieterwechsel und Wartung.'),
 },
 'faq': FAQ,
 'schema': {"@context": "https://schema.org", "@graph": [ORG, {
    "@type": "Service", "@id": URL + "#leistung", "name": "Schließanlagen für Hausverwaltungen und Mehrfamilienhäuser",
    "serviceType": "Schließanlage Mehrfamilienhaus", "url": URL,
    "description": "Planung, Montage, Umrüstung und Betreuung mechanischer und elektronischer Schließanlagen für Wohnanlagen: Schließplan, Mieterwechsel, Schlüsselverlust, Zeitfenster für Dienstleister.",
    "provider": {"@id": BASE + "/#organization"},
    "areaServed": [{"@type": "City", "name": o} for o in ORTE_NORD] + [{"@type": "State", "name": "Niedersachsen"}],
    "audience": {"@type": "BusinessAudience", "name": "Hausverwaltungen, Eigentümergemeinschaften und Vermieter"}}]},
}
SPEC['clone'] = [
 ('985957a', '58762b2', '985957a', {
   '4967d0c': {'title': 'Nachschlüssel und Transponder: Nachbestellung gegen Sicherungskarte, neue Transponder bei Mieterwechsel.'},
   '99ee72d': {'title': 'Austausch bei Verlust: gezielt nur die betroffenen Zylinder, Schließplan wird aktualisiert.'},
   '8754a23': {'editor': p('Wartung: Wir wechseln Batterien, erweitern die Anlage und helfen Verwaltung und Hausmeister schnell weiter.')},
 }),
]
