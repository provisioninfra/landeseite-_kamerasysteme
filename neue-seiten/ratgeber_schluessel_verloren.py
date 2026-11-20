import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz, ORDER, GRUENDER, PRESSE, video_kasten, cta, stell_dir_vor

URL = BASE + '/ratgeber/schluessel-verloren-unternehmen/'
TITEL = 'Schlüssel im Unternehmen verloren: Was jetzt zu tun ist'
BESCHR = 'Firmenschlüssel verloren? Was jetzt zu tun ist, wer haftet, was der Austausch kostet und wie du künftig vorbeugst. Ratgeber für Unternehmen.'
KARTEN = [
 ('Schritt 1: Verlust sofort melden und Umstände klären',
  p('Je früher der Verlust bekannt ist, desto kleiner ist das Risiko. Kläre, wann der Schlüssel zuletzt da war und ob er gestohlen wurde. Wichtig ist auch, ob am Bund etwas auf deine Firma hinweist, '
    'etwa ein Anhänger mit der Adresse. Ein Schlüssel mit Firmenlogo ist deutlich riskanter als einer, der im See liegt.'),
  kurz('Melden, aufschreiben, was bekannt ist, und keine Zeit verlieren.')),
 ('Schritt 2: Im Schließplan nachsehen, welche Türen betroffen sind',
  p('Der Schließplan zeigt, was der verlorene Schlüssel öffnet. Ein Einzelschlüssel betrifft eine Tür, ein Gruppenschlüssel einen Bereich, ein Generalhauptschlüssel im Zweifel das ganze Gebäude. '
    'Ohne Schließplan wird es teuer, weil niemand sicher sagen kann, welche Zylinder getauscht werden müssen.'),
  kurz('Der Schließplan entscheidet, ob eine Tür oder das ganze Haus betroffen ist.')),
 ('Schritt 3: Risiko bewerten',
  p('Nicht jeder Verlust verlangt sofort den Austausch aller Zylinder. Entscheidend ist, ob ein Finder den Schlüssel deinem Betrieb zuordnen kann und was hinter den Türen liegt: '
    'Bargeld, Ware, Daten, Maschinen. Diese Einschätzung solltest du dokumentieren, auch für die Versicherung.'),
  kurz('Zuordenbarkeit und Wert hinter der Tür bestimmen, wie schnell gehandelt werden muss.')),
 ('Schritt 4: Gezielt tauschen oder sperren',
  p('Bei mechanischen Anlagen tauschen wir genau die Zylinder, die der verlorene Schlüssel öffnet, und tragen die Änderung im Schließplan nach. Nachschlüssel und neue Zylinder gibt es bei Anlagen '
    'mit Sicherungskarte nur gegen Vorlage der Karte. Bei <a href="/zutrittssystem/">elektronischen Schließanlagen</a> sperrst du den verlorenen Transponder in der Software, ohne etwas zu tauschen.'),
  kurz('Mechanisch gezielt tauschen, elektronisch einfach sperren.')),
 ('Wer haftet für den Schaden?',
  p('Das hängt vom Einzelfall ab. Verliert ein Mitarbeiter einen Firmenschlüssel, gelten die Grundsätze der Arbeitnehmerhaftung: Bei leichter Fahrlässigkeit haftet er in der Regel nicht, '
    'bei mittlerer Fahrlässigkeit wird der Schaden meist geteilt, bei grober Fahrlässigkeit oder Vorsatz haftet er in der Regel voll. Sind die Räume gemietet, kann zusätzlich der Vermieter den Austausch verlangen. '
    'Verbindlich klären das ein Anwalt oder deine Versicherung.'),
  kurz('Je größer das Verschulden, desto eher haftet der Mitarbeiter; im Zweifel rechtlich prüfen lassen.')),
 ('Zahlt die Versicherung?',
  p('Manche Betriebshaftpflicht- und Inhaltsversicherungen enthalten einen Baustein für Schlüsselverlust, manche private Haftpflichtversicherungen decken auch den Verlust beruflich genutzter fremder Schlüssel. '
    'Ein Blick in die Bedingungen lohnt sich vor dem Austausch. Wir erstellen dir eine Aufstellung der betroffenen Zylinder und Kosten für die Schadenmeldung.'),
  kurz('Police prüfen, bevor du beauftragst, und alles dokumentieren.')),
 ('So beugst du vor',
  p('Schlüssel nur gegen Unterschrift ausgeben, keine Anhänger mit Firmenname, Sicherungskarte getrennt von den Schlüsseln aufbewahren und den Schließplan aktuell halten. '
    'An Türen mit vielen Nutzern lohnen sich elektronische Zylinder: Dort ist ein Verlust mit einem Klick erledigt. Mehr dazu auf der Seite <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a> '
    'und im <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.'),
  kurz('Dokumentierte Ausgabe, aktueller Schließplan, elektronische Zylinder an kritischen Türen.')),
]
FAQ = [
 ('Was tun, wenn ein Firmenschlüssel verloren gegangen ist?',
  p('Verlust sofort melden, im Schließplan prüfen, welche Türen betroffen sind, das Risiko bewerten und dann gezielt Zylinder tauschen oder elektronische Medien sperren. Alles dokumentieren, auch für die Versicherung.')),
 ('Muss nach einem Schlüsselverlust die ganze Schließanlage getauscht werden?',
  p('Nein, nur die Zylinder, die der verlorene Schlüssel öffnet. Bei einem Generalhauptschlüssel können das allerdings sehr viele sein. Bei elektronischen Anlagen wird nur der Transponder gesperrt.')),
 ('Haftet der Mitarbeiter, wenn er einen Firmenschlüssel verliert?',
  p('Das hängt vom Grad des Verschuldens ab. Bei leichter Fahrlässigkeit in der Regel nicht, bei mittlerer meist anteilig, bei grober Fahrlässigkeit oder Vorsatz in der Regel voll. Im Einzelfall entscheidet die rechtliche Prüfung.')),
 ('Was kostet der Austausch nach einem Schlüsselverlust?',
  p('Das hängt vor allem von der Zahl der betroffenen Zylinder ab. Mit Schließplan lässt sich der Austausch genau eingrenzen und vorab beziffern.')),
 ('Zahlt die Versicherung den Schlüsselverlust?',
  p('Manchmal. Betriebliche und private Haftpflichtpolicen enthalten teilweise einen Baustein für den Verlust fremder oder beruflich genutzter Schlüssel. Prüfe die Bedingungen, bevor du den Austausch beauftragst.')),
 ('Wie lange dauert der Austausch?',
  p('Einzelne Zylinder tauschen wir meist kurzfristig. Bei Anlagen mit Sicherungskarte werden neue Zylinder beim Hersteller gefertigt; für die Übergangszeit besprechen wir mit dir eine Zwischenlösung.')),
 ('Lohnt sich nach einem Verlust der Umstieg auf eine elektronische Schließanlage?',
  p('Oft ja, vor allem bei vielen Nutzern und häufigen Wechseln. Viele Betriebe rüsten zuerst die stark genutzten Türen um. Wir rechnen dir beide Wege durch.')),
]
SPEC = {
 'slug': 'schluessel-verloren-unternehmen', 'parent_slug': 'ratgeber', 'title': 'Schlüssel im Unternehmen verloren',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Schlüssel verloren in der Firma: Wer haftet, was tun?',
         'description': BESCHR, 'focuskw': 'Schlüssel verloren Firma', 'bctitle': 'Schlüssel verloren', 'robots_noindex': '0'},
 'remove': REMOVE,
 'order': ORDER, 'handy_css': True,
 'graft': [cta('Schlüssel weg? Wir helfen dir weiter', 'Wir prüfen mit dir, welche Türen betroffen sind, und liefern dir die Aufstellung für die Versicherung.', nach='f1a5d3e'),
   video_kasten('Wo ein verlorener Schlüssel besonders heikel wäre, helfen Kameras zusätzlich. Wir planen beides zusammen und installieren Kamerasysteme mit Alarm aufs Handy.'), PRESSE], 'karten': KARTEN,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Schlüssel im Unternehmen verloren:</span><br>Was jetzt zu tun ist'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Ein Schlüssel fehlt, und plötzlich stehen Fragen im Raum: Wer kommt jetzt in unser Gebäude? Müssen alle Schlösser getauscht werden? Und wer bezahlt das? '
              'Dieser Ratgeber führt dich Schritt für Schritt durch die ersten Stunden und Tage nach dem Verlust.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Melde den Verlust sofort und prüfe im Schließplan, welche Türen betroffen sind.'},
  '7df04ae': {'editor': p('Nach einem Schlüsselverlust müssen nur die Türen gesichert werden, die der Schlüssel tatsächlich öffnet. Welche das sind, zeigt der Schließplan. Bei elektronischen Anlagen genügt es, den Transponder zu sperren. '
              'Wer den Schaden trägt, hängt vom Verschulden und vom Versicherungsschutz ab.')},
  'd38dec5': {'editor': p('Dieser Ratgeber gibt dir einen Überblick und ersetzt keine Rechtsberatung. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Schlüssel verloren: <span style="font-weight: 700; ">Schritt für Schritt</span>'},
  '43e5085': {'editor': p('Vier Schritte für die Sicherheit, zwei Fragen zu Haftung und Versicherung und ein Kapitel darüber, wie du dir das nächste Mal ersparst.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste für die ersten 24 Stunden'},
  '8b353e8': {'title': 'Der Verlust ist gemeldet, und du weißt, ob am Schlüsselbund etwas auf deine Firma hinweist.'},
  '6519b8c': {'title': 'Betroffene Türen im Schließplan ermittelt, besonders sensible Bereiche zuerst gesichert.'},
  '05ac70c': {'editor': p('Die Versicherung ist informiert, und der Austausch der betroffenen Zylinder ist beauftragt.')},
  'f1a5d3e': {'_title': 'Passend dazu', '_element_id': 'weiterlesen'},
  'cfa4bb1': {'_title': 'Passend dazu', 'title': 'Passend dazu'},
  '4967d0c': {'title': '<a href="/mechanische-schliessanlagen/" style="color: #FBC91B;">Mechanische Schließanlagen</a>: wie Schließplan und Sicherungskarte bei einem Verlust helfen.'},
  '99ee72d': {'title': '<a href="/zutrittssystem/" style="color: #FBC91B;">Elektronische Schließanlagen</a>: ein verlorener Transponder wird einfach gesperrt.'},
  '8754a23': {'editor': p('<a href="/schliessanlage-hausverwaltung/">Schließanlagen für Hausverwaltungen</a>: Schlüsselverlust und Mieterwechsel im Mehrfamilienhaus.')},
  '51f3331': {'title': 'Schlüssel weg? <br><span style="font-weight: 700; ">Wir helfen dir weiter</span>'},
  '5c65e03': {'editor': p('Wir prüfen mit dir, welche Türen betroffen sind, und tauschen gezielt. Für die Versicherung bekommst du von uns eine Aufstellung der Kosten. '
              'Im Einsatz sind wir in ganz Norddeutschland, alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zum <b>Schlüsselverlust im Unternehmen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zum <br><b>Schlüsselverlust im Unternehmen</b>'},
 },
 'faq': FAQ,
 'schema': artikel_schema(URL, TITEL, BESCHR),
}
