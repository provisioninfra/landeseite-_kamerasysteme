import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD, ORDER, GRUENDER, PRESSE, video_kasten, cta, analyse, stell_dir_vor, vorteile

URL = BASE + '/schliessanlage-hausverwaltung/'
def p(t): return '<p>' + t + '</p>'
FAQ = [
 ('Was kostet eine Schließanlage für ein Mehrfamilienhaus?',
  p('Den größten Einfluss haben die Zahl der Türen und die Entscheidung zwischen mechanisch und elektronisch. Dazu kommt, wie viele Schlüssel oder Transponder im Umlauf sein sollen. '
    'Nach der Begehung bekommst du ein schriftliches Angebot, das du direkt der Eigentümergemeinschaft oder dem Eigentümer vorlegen kannst.')),
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
  p('Nur in engen Grenzen. Gemeinschaftsflächen wie Fahrradkeller oder Tiefgarage können in Frage kommen, wenn es einen berechtigten Anlass gibt und die Rechte der Bewohner gewahrt bleiben. Hinweisschilder sind dabei Pflicht. '
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
  'e429076': {'_title': 'Hero-Text', 'title': 'Ein Mieter zieht aus und gibt nur zwei von drei Schlüsseln zurück. Auf der nächsten Eigentümerversammlung will dann jemand wissen, wer eigentlich noch in den Keller kommt.<br><br>'
              '<span style="font-weight: 700;">ProVision Infra plant und betreut Schließanlagen für Wohnanlagen, mechanisch mit Sicherungskarte oder elektronisch mit Transponder. '
              'Damit wird der nächste Mieterwechsel zur Formsache.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Ein verlorener Schlüssel darf nicht das ganze Haus kosten.'},
  '7df04ae': {'editor': p('Im Mehrfamilienhaus hängt an jedem Wohnungsschlüssel mehr als die eigene Tür. Er öffnet meist auch Haustür und Keller. Geht er verloren, sind plötzlich alle Bewohner betroffen, '
              'und die Rechnung für neue Zylinder landet bei der Gemeinschaft. Mit einem durchdachten Schließplan bleibt so ein Verlust, was er sein sollte: ein kleiner Vorfall.')},
  'd38dec5': {'editor': p('Wir nehmen das Objekt auf und entwerfen den Schließplan gemeinsam mit dir. Umgerüstet wird im bewohnten Haus, und dabei steht niemand vor verschlossener Tür. '
              'Für Mieterwechsel und Nachschlüssel bleibt danach ein fester Ansprechpartner bei uns zuständig.')},
  'd7f768f': {'_title': 'Lösungen für Wohnanlagen', '_element_id': 'loesungen'},
  '74b6d54': {'_title': 'Lösungen Überschrift', 'title': 'Was eine Schließanlage im Mehrfamilienhaus <span style="font-weight: 700; ">leisten muss</span>'},
  '43e5085': {'editor': p('Diese fünf Situationen kennt jede Verwaltung. So bekommst du sie in den Griff.')},
  '8cc96a4': {'title': 'Ein Schließplan für das ganze Haus'},
  '71be80d': {'editor': p('Mieter öffnen ihre Wohnung und die gemeinsamen Türen. Der Hausmeister kommt zusätzlich in Technik- und Nebenräume. '
              'Festgehalten ist das im Schließplan, den du schriftlich bekommst und jederzeit vorzeigen kannst.')},
  '59a04cb': {'editor': p('Jede Ausgabe und Rückgabe lässt sich nachvollziehen, auch nach Jahren und Verwalterwechseln.')},
  '5e90e79': {'title': 'Mieterwechsel ohne Zylindertausch'},
  '88e4e41': {'editor': p('Mit elektronischen Zylindern an Haustür und Gemeinschaftstüren sperrst du alte Transponder und gibst neue aus. Bei mechanischen Anlagen tauschen wir gezielt nur den Wohnungszylinder, '
              'die gemeinsamen Türen bleiben unberührt.')},
  'ca72bdb': {'editor': p('Der Auszug ist erledigt, sobald der alte Transponder gesperrt ist. Auf einen Handwerker wartest du dabei nicht.')},
  'b452400': {'title': 'Schlüssel weg? Getauscht wird nur, was betroffen ist'},
  '6773460': {'editor': p('Geht ein Schlüssel verloren, prüfen wir anhand des Schließplans, welche Türen betroffen sind, und tauschen nur dort. Bei elektronischen Komponenten genügt das Sperren des Transponders. '
              'Nachschlüssel gibt es bei Anlagen mit Sicherungskarte nur gegen Vorlage der Karte.')},
  '24f8396': {'editor': p('Die Kosten bleiben überschaubar, und kein fremder Schlüssel öffnet mehr die Haustür.')},
  '5860b09': {'title': 'Zeitfenster für Dienstleister'},
  'dc25036': {'editor': p('Reinigung und Gartenpflege bekommen einen Transponder oder eine App-Berechtigung, die nur zu festgelegten Zeiten öffnet. Schlüssel musst du dafür nicht mehr verteilen.')},
  '4838414': {'editor': p('Endet der Vertrag mit der Firma, endet am selben Tag auch ihr Zugang.')},
  'bb8c516': {'title': 'Gemeinschaftsflächen im Blick'},
  '6414a37': {'editor': p('Wo es einen berechtigten Anlass gibt, etwa wiederholte Fahrraddiebstähle, planen wir <a href="/kamerasysteme/">Videoüberwachung</a> an Gemeinschaftsflächen. Hinweisschilder und eng begrenzte '
              'Bildausschnitte gehören dazu, und vorher stimmen wir alles mit der Eigentümergemeinschaft ab.')},
  'f5080c1': {'editor': p('Mechanisch arbeiten wir mit EVVA, elektronisch unter anderem mit EVVA AirKey und SimonsVoss. Die Kameras stammen von TP-Link VIGI.')},
  '3ac3e9e': {'editor': p('Für Türen und Kameras hast du damit einen einzigen Ansprechpartner.')},
  'd70fb3d': {'_title': 'Mechanisch oder elektronisch', '_element_id': 'vergleich'},
  'c869af6': {'_title': 'Mechanisch oder elektronisch', 'title': 'Welche Anlage passt zu deinem Objekt?'},
  '8b353e8': {'title': 'Mechanisch: ideal für kleinere Häuser mit wenigen Parteien, in denen selten jemand umzieht. Die Anlage läuft ohne Strom, und die Sicherungskarte schützt vor unerlaubten Kopien.'},
  '6519b8c': {'title': 'Elektronisch: für große Wohnanlagen mit häufigen Mieterwechseln und vielen Dienstleistern. Verlorene Transponder sind mit einem Klick gesperrt.'},
  '05ac70c': {'editor': p('Gemischt: Gemeinschaftstüren elektronisch, Wohnungen mechanisch. Für viele Verwaltungen der wirtschaftlichste Weg. Mehr dazu im '
              '<a href="/schliesssysteme/">Vergleich der Schließsysteme</a> und auf der Seite <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a>.')},
  'f1a5d3e': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'cfa4bb1': {'_title': 'Leistungen', 'title': 'Unsere Leistungen für Hausverwaltungen'},
  '4967d0c': {'title': 'Bestandsaufnahme und Planung: Wir nehmen alle Türen des Objekts auf und entwerfen den Schließplan mit dir.'},
  '99ee72d': {'title': 'Unterlagen für die Eigentümerversammlung: verständliches Angebot und Varianten, die du vorlegen kannst.'},
  '8754a23': {'editor': p('Umrüstung im bewohnten Haus: Wir beginnen mit den Gemeinschaftstüren und tauschen die Wohnungszylinder nach Absprache. Jede Übergabe wird quittiert.')},
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
    'Ein verlorener Schlüssel betrifft nur noch eine Wohnung. Das übrige Haus bleibt sicher.',
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
  'Erstgespräch': p('Am Telefon erzählst du uns, wie viele Parteien das Haus hat und wo es heute hakt. Eine ehrliche erste Einschätzung bekommst du noch im selben Gespräch.'),
  'Termin vor Ort': p('Wir gehen mit dir oder dem Hausmeister durch das Objekt und nehmen jede Tür auf, von der Haustür bis zur Tiefgarage. Den Kostenrahmen nennen wir dir noch vor Ort.'),
  'Planung deines Systems': p('Du bekommst den Schließplan-Entwurf und ein Angebot mit Varianten, das du der Eigentümergemeinschaft vorlegen kannst.'),
  'Umsetzung': p('Wir rüsten im bewohnten Haus um und stimmen jeden Wohnungstermin mit den Bewohnern ab. Jede Partei bekommt ihren neuen Schlüssel oder Transponder direkt beim Termin in die Hand.'),
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
   '8754a23': {'editor': p('Wartung und Erweiterung: Wir wechseln Batterien und nehmen neue Türen in die Anlage auf. Ruft der Hausmeister an, bekommt er schnell Hilfe.')},
 }),
]
