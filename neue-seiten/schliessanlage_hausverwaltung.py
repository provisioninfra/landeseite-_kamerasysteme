import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD

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
  p('Nicht immer. Fehlt ein Wohnungsschlüssel, der nur die eigene Wohnung öffnet, reicht oft der Tausch dieses einen Zylinders. Öffnet der Schlüssel auch Haustür, Keller und Nebeneingänge, '
    'sind diese Zylinder mit betroffen. Bei einer elektronischen Anlage sperrst du den verlorenen Transponder einfach, ohne etwas zu tauschen.')),
 ('Lohnt sich eine elektronische Schließanlage im Mehrfamilienhaus?',
  p('Vor allem dort, wo oft gewechselt wird: bei häufigen Mieterwechseln, vielen Dienstleistern oder wiederholten Schlüsselverlusten. Viele Verwaltungen digitalisieren zuerst Haustür, Keller und Tiefgarage '
    'und lassen die Wohnungstüren mechanisch. Welche Systeme sich eignen, zeigt der <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.')),
 ('Wer entscheidet in einer Eigentümergemeinschaft über eine neue Schließanlage?',
  p('In der Regel die Eigentümerversammlung per Beschluss. Wir unterstützen die Verwaltung mit einem verständlichen Angebot, einem Schließplan-Entwurf und auf Wunsch einer kurzen Erläuterung der Varianten.')),
 ('Sind Wartungskosten für die Schließanlage auf die Mieter umlegbar?',
  p('Das hängt vom Mietvertrag und von der Art der Kosten ab. Bitte lass die Umlage im Einzelfall rechtlich prüfen. Wir stellen dir Wartung und Reparatur getrennt aus, damit die Abrechnung einfacher wird.')),
 ('Kann ich nur die Haustür digitalisieren?',
  p('Ja. Ein elektronischer Zylinder oder ein Wandleser an der Haustür lässt sich mit einer bestehenden mechanischen Anlage kombinieren. So bekommen Dienstleister ein Zeitfenster statt eines Schlüssels, '
    'und die Wohnungsschlüssel bleiben, wie sie sind.')),
 ('Ist Videoüberwachung im Mehrfamilienhaus erlaubt?',
  p('Nur in engen Grenzen. Gemeinschaftsflächen wie Eingang, Fahrradkeller oder Tiefgarage können in Frage kommen, wenn es einen berechtigten Anlass gibt, Hinweisschilder angebracht sind und die Rechte der Bewohner gewahrt bleiben. '
    'Das sollte vorher rechtlich geprüft und mit der Eigentümergemeinschaft abgestimmt werden. Mehr zur <a href="/kamerasysteme/">Videoüberwachung</a>.')),
 ('Wie läuft die Umrüstung in einem bewohnten Haus ab?',
  p('Wir kündigen den Termin über die Verwaltung an, tauschen Gemeinschaftstüren zuerst und Wohnungstüren nach Absprache mit den Bewohnern. Neue Schlüssel oder Transponder werden gegen Unterschrift übergeben, '
    'damit du lückenlos dokumentiert hast, wer was bekommen hat.')),
 ('Arbeitet ihr auch langfristig mit Hausverwaltungen zusammen?',
  p('Ja. Nach der Umrüstung bleiben wir Ansprechpartner für Nachschlüssel, neue Transponder, Mieterwechsel, Wartung und Erweiterungen, mit einem festen Kontakt für Verwaltung und Hausmeister.')),
]
SPEC = {
 'slug': 'schliessanlage-hausverwaltung', 'title': 'Schließanlagen für Hausverwaltungen',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Schließanlage Mehrfamilienhaus & Hausverwaltung | ProVision',
         'description': 'Schließanlagen für Hausverwaltungen und Mehrfamilienhäuser: Schließplan, Mieterwechsel ohne Zylindertausch, Schlüsselverlust, Umrüstung auf elektronisch.',
         'focuskw': 'Schließanlage Mehrfamilienhaus', 'bctitle': 'Hausverwaltungen', 'robots_noindex': '0'},
 'remove': ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb'],
 'set': {
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Schließanlagen für Hausverwaltungen</span><br>und Mehrfamilienhäuser'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Ein Mieter zieht aus und gibt nur zwei von drei Schlüsseln zurück. Die Reinigungsfirma wechselt, der alte Generalschlüssel ist noch im Umlauf. '
              'Und bei jeder Eigentümerversammlung kommt dieselbe Frage: Wer hat eigentlich noch einen Schlüssel zum Keller?<br><br>'
              '<span style="font-weight: 700;">ProVision Infra plant, montiert und betreut Schließanlagen für Wohnanlagen: mechanisch mit Sicherungskarte, elektronisch mit Transponder '
              'oder kombiniert. Damit ein Mieterwechsel wieder eine Formsache ist und kein Zylindertausch.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Weniger Schlüsselchaos, weniger Kosten, weniger Rückfragen.'},
  '7df04ae': {'editor': p('In einem Mehrfamilienhaus öffnen viele Schlüssel dieselben Türen: Haustür, Keller, Fahrradraum, Müllplatz, Tiefgarage. Jeder verlorene oder nicht zurückgegebene Schlüssel betrifft '
              'deshalb alle Bewohner, und die Kosten landen schnell bei der Gemeinschaft. Eine gut geplante Schließanlage begrenzt genau dieses Risiko.')},
  'd38dec5': {'editor': p('Wir nehmen das Objekt auf, entwerfen den Schließplan mit dir und rüsten im bewohnten Haus um, ohne dass jemand vor verschlossener Tür steht. '
              'Danach bist du nicht allein: Nachschlüssel, neue Transponder, Mieterwechsel und Wartung laufen über einen festen Ansprechpartner.')},
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
  'ca72bdb': {'editor': p('Der Auszug ist erledigt, sobald der Transponder gesperrt ist, nicht erst nach dem Handwerkertermin.')},
  'b452400': {'title': 'Schlüsselverlust: schnell und gezielt reagieren'},
  '6773460': {'editor': p('Geht ein Schlüssel verloren, prüfen wir anhand des Schließplans, welche Türen betroffen sind, und tauschen nur dort. Bei elektronischen Komponenten genügt das Sperren des Transponders. '
              'Nachschlüssel gibt es bei Anlagen mit Sicherungskarte nur gegen Vorlage der Karte.')},
  '24f8396': {'editor': p('Die Kosten bleiben überschaubar, und kein fremder Schlüssel öffnet mehr die Haustür.')},
  '5860b09': {'title': 'Zeitfenster für Dienstleister'},
  'dc25036': {'editor': p('Reinigung, Gärtner, Handwerker, Ableser: Statt Schlüssel zu verteilen, bekommen Dienstleister einen Transponder oder eine App-Berechtigung, die nur zu festgelegten Zeiten öffnet.')},
  '4838414': {'editor': p('Keine Schlüssel mehr in Briefkästen, unter Fußmatten oder beim Nachbarn.')},
  'bb8c516': {'title': 'Eingang, Keller und Tiefgarage im Blick'},
  '6414a37': {'editor': p('Wo es einen berechtigten Anlass gibt, etwa wiederholte Fahrraddiebstähle, planen wir <a href="/kamerasysteme/">Videoüberwachung</a> an Gemeinschaftsflächen: mit Hinweisschildern, '
              'eng begrenzten Bildausschnitten und nach Abstimmung mit der Eigentümergemeinschaft.')},
  'f5080c1': {'editor': p('Mechanisch mit EVVA, elektronisch mit EVVA AirKey, EVVA Xesar, SimonsVoss oder Keyota, für einzelne Türen auch NUKI. Kameras von TP-Link VIGI.')},
  '3ac3e9e': {'editor': p('Ein Konzept für Türen und Kameras, ein Angebot, ein Ansprechpartner für die Verwaltung.')},
  'd70fb3d': {'_title': 'Mechanisch oder elektronisch', '_element_id': 'vergleich'},
  'c869af6': {'_title': 'Mechanisch oder elektronisch', 'title': 'Mechanisch, elektronisch oder gemischt: was passt zu deinem Objekt?'},
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
 'ablauf': {
  'Erstgespräch': p('Ein kurzes Telefonat: Wie viele Parteien, welche Türen, was läuft heute schief? Du bekommst sofort eine ehrliche erste Einschätzung.'),
  'Termin vor Ort': p('Wir gehen mit dir oder dem Hausmeister durch das Objekt und nehmen jede Tür auf, von der Haustür bis zur Tiefgarage. Den Kostenrahmen nennen wir dir noch vor Ort.'),
  'Planung deines Systems': p('Du bekommst den Schließplan-Entwurf und ein Angebot mit Varianten, das du der Eigentümergemeinschaft vorlegen kannst.'),
  'Umsetzung': p('Wir rüsten im bewohnten Haus um, Gemeinschaftstüren zuerst, Wohnungen nach Absprache. Niemand steht vor verschlossener Tür.'),
  'Übergabe & Betreuung': p('Schlüssel und Transponder werden gegen Unterschrift übergeben. Danach bleiben wir Ansprechpartner für Mieterwechsel, Nachschlüssel und Wartung.'),
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
   '8754a23': {'editor': p('Wartung und fester Ansprechpartner: Batteriewechsel, Erweiterungen und schnelle Hilfe für Verwaltung und Hausmeister.')},
 }),
]
