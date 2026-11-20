import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz, ORDER, GRUENDER, PRESSE, video_kasten, cta, stell_dir_vor

URL = BASE + '/ratgeber/schluessel-verloren-unternehmen/'
TITEL = 'Schlüssel im Unternehmen verloren: Was jetzt zu tun ist'
BESCHR = 'Firmenschlüssel verloren? Was jetzt zu tun ist, wer haftet, was der Austausch kostet und wie du künftig vorbeugst. Ratgeber für Unternehmen.'
KARTEN = [
 ('Schritt 1: Verlust sofort melden und Umstände klären',
  p('Je früher alle Bescheid wissen, desto kleiner das Risiko. Finde heraus, wann der Schlüssel zuletzt sicher da war und ob er gestohlen wurde. '
    'Genauso wichtig: Verrät etwas am Bund, zu welcher Firma er gehört, zum Beispiel ein Anhänger mit Adresse? '
    'Ein Schlüssel mit Firmenlogo ist ein ganz anderes Risiko als einer, der auf dem Grund eines Sees liegt.'),
  kurz('Sofort melden und aufschreiben, was du weißt.')),
 ('Schritt 2: Im Schließplan nachsehen, welche Türen betroffen sind',
  p('Der Schließplan zeigt dir, was der verlorene Schlüssel öffnet. Fehlt ein Einzelschlüssel, ist eine Tür betroffen, beim Gruppenschlüssel ein ganzer Bereich. '
    'Ein Generalhauptschlüssel öffnet im schlimmsten Fall das gesamte Gebäude. Gibt es keinen Schließplan, wird es teuer, '
    'denn dann kann niemand sicher sagen, welche Zylinder raus müssen.'),
  kurz('Ob eine Tür betroffen ist oder das ganze Haus, steht im Schließplan.')),
 ('Schritt 3: Risiko bewerten',
  p('Ein Verlust zwingt dich nicht automatisch, sofort alle Zylinder zu tauschen. Es kommt auf zwei Fragen an. Kann ein Finder den Schlüssel deinem Betrieb zuordnen? '
    'Und was liegt hinter den Türen, die er öffnet? Ein Lager voller Ware wiegt schwerer als ein Abstellraum. '
    'Halte deine Einschätzung schriftlich fest, das hilft dir später auch gegenüber der Versicherung.'),
  kurz('Zuordenbarkeit und der Wert hinter der Tür bestimmen, wie schnell du handeln musst.')),
 ('Schritt 4: Gezielt tauschen oder sperren',
  p('In einer mechanischen Anlage tauschen wir genau die Zylinder, die der verlorene Schlüssel öffnet, und tragen die Änderung im Schließplan nach. '
    'Bei Anlagen mit Sicherungskarte gibt es neue Zylinder und Nachschlüssel nur gegen Vorlage der Karte. '
    'Einfacher geht es mit einer <a href="/zutrittssystem/">elektronischen Schließanlage</a>: Dort sperrst du den verlorenen Transponder in der Software, getauscht wird gar nichts.'),
  kurz('Mechanisch wird gezielt getauscht, elektronisch genügt die Sperre.')),
 ('Wer haftet für den Schaden?',
  p('Das hängt vom Einzelfall ab. Verliert ein Mitarbeiter einen Firmenschlüssel, greifen die Grundsätze der Arbeitnehmerhaftung. Bei leichter Fahrlässigkeit haftet er in der Regel gar nicht. '
    'Bei mittlerer Fahrlässigkeit wird der Schaden meist zwischen Betrieb und Mitarbeiter geteilt. Handelt er grob fahrlässig oder vorsätzlich, haftet er in der Regel voll. '
    'Sind die Räume gemietet, kann außerdem der Vermieter den Austausch verlangen. Verbindlich klärt das ein Anwalt oder deine Versicherung.'),
  kurz('Je größer das Verschulden, desto eher haftet der Mitarbeiter. Im Zweifel lässt du das rechtlich prüfen.')),
 ('Zahlt die Versicherung?',
  p('Manchmal ja. Einige Betriebshaftpflicht- und Inhaltsversicherungen enthalten einen Baustein für Schlüsselverlust. '
    'Auch manche private Haftpflichtversicherung zahlt, wenn beruflich genutzte fremde Schlüssel verloren gehen. Lies die Bedingungen, bevor du den Austausch beauftragst. '
    'Für die Schadenmeldung stellen wir dir die betroffenen Zylinder und die Kosten zusammen.'),
  kurz('Erst die Police prüfen, dann beauftragen. Und jeden Schritt dokumentieren.')),
 ('So beugst du vor',
  p('Gib Schlüssel nur gegen Unterschrift aus und verzichte auf Anhänger mit Firmennamen. Die Sicherungskarte gehört an einen anderen Ort als die Schlüssel, '
    'und der Schließplan sollte immer aktuell sein. An Türen mit vielen Nutzern lohnen sich elektronische Zylinder, denn dort erledigst du einen Verlust mit einem Klick. '
    'Mehr dazu auf der Seite <a href="/mechanische-schliessanlagen/">mechanische Schließanlagen</a> und im <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.'),
  kurz('Eine dokumentierte Schlüsselausgabe und elektronische Zylinder an den kritischen Türen ersparen dir den nächsten Ernstfall.')),
]
FAQ = [
 ('Was tun, wenn ein Firmenschlüssel verloren gegangen ist?',
  p('Melde den Verlust sofort und prüfe im Schließplan, welche Türen betroffen sind. Danach bewertest du das Risiko und lässt gezielt Zylinder tauschen oder sperrst elektronische Medien. '
    'Dokumentiere jeden Schritt, auch für die Versicherung.')),
 ('Muss nach einem Schlüsselverlust die ganze Schließanlage getauscht werden?',
  p('Nein. Getauscht werden nur die Zylinder, die der verlorene Schlüssel öffnet. Bei einem Generalhauptschlüssel können das allerdings sehr viele sein. In elektronischen Anlagen sperrst du einfach den Transponder.')),
 ('Haftet der Mitarbeiter, wenn er einen Firmenschlüssel verliert?',
  p('Das hängt vom Grad des Verschuldens ab. Bei leichter Fahrlässigkeit haftet er in der Regel nicht, bei mittlerer meist anteilig. '
    'Bei grober Fahrlässigkeit oder Vorsatz haftet er in der Regel voll. Verbindlich klärt das im Einzelfall erst die rechtliche Prüfung.')),
 ('Was kostet der Austausch nach einem Schlüsselverlust?',
  p('Entscheidend ist die Zahl der betroffenen Zylinder. Mit einem Schließplan lässt sich der Austausch genau eingrenzen, und wir nennen dir den Preis vorab.')),
 ('Zahlt die Versicherung den Schlüsselverlust?',
  p('Manchmal. Betriebliche und private Haftpflichtpolicen enthalten teilweise einen Baustein für den Verlust fremder oder beruflich genutzter Schlüssel. Prüfe die Bedingungen, bevor du den Austausch beauftragst.')),
 ('Wie lange dauert der Austausch?',
  p('Einzelne Zylinder tauschen wir meist kurzfristig. Bei Anlagen mit Sicherungskarte fertigt der Hersteller die neuen Zylinder; für die Zeit bis zur Lieferung vereinbaren wir mit dir eine Zwischenlösung.')),
 ('Lohnt sich nach einem Verlust der Umstieg auf eine elektronische Schließanlage?',
  p('Oft ja, vor allem wenn viele Leute Schlüssel haben und das Team häufig wechselt. Ein guter Anfang sind die Türen, die am stärksten genutzt werden. Wir rechnen dir beide Wege durch.')),
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
  'e429076': {'_title': 'Hero-Text', 'title': 'Montagmorgen, ein Mitarbeiter meldet: Schlüssel verloren, vermutlich schon am Freitag. Sofort steht die Frage im Raum, wer jetzt in euer Gebäude kommt und ob alle Schlösser raus müssen. '
              'Dieser Ratgeber führt dich durch die ersten Stunden nach dem Verlust und klärt, wer am Ende bezahlt.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Verlust sofort melden, dann im Schließplan nachsehen, welche Türen betroffen sind.'},
  '7df04ae': {'editor': p('Nach einem Schlüsselverlust sicherst du nur die Türen, die der Schlüssel tatsächlich öffnet. Welche das sind, verrät dir der Schließplan. In einer elektronischen Anlage sperrst du einfach den Transponder. '
              'Wer den Schaden trägt, hängt vom Verschulden ab und davon, was deine Versicherung abdeckt.')},
  'd38dec5': {'editor': p('Dieser Ratgeber gibt dir einen Überblick und ersetzt keine Rechtsberatung. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Schlüssel verloren: <span style="font-weight: 700; ">Schritt für Schritt</span>'},
  '43e5085': {'editor': p('In vier Schritten sicherst du zuerst dein Gebäude. Danach geht es um Haftung und Versicherung, und am Ende zeigen wir dir, wie du dem nächsten Verlust vorbeugst.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste für die ersten 24 Stunden'},
  '8b353e8': {'title': 'Der Verlust ist gemeldet, und du weißt, ob am Schlüsselbund etwas auf deine Firma hinweist.'},
  '6519b8c': {'title': 'Die betroffenen Türen sind im Schließplan ermittelt, sensible Bereiche zuerst gesichert.'},
  '05ac70c': {'editor': p('Die Versicherung ist informiert, und der Austausch der betroffenen Zylinder ist beauftragt.')},
  'f1a5d3e': {'_title': 'Passend dazu', '_element_id': 'weiterlesen'},
  'cfa4bb1': {'_title': 'Passend dazu', 'title': 'Passend dazu'},
  '4967d0c': {'title': '<a href="/mechanische-schliessanlagen/" style="color: #FBC91B;">Mechanische Schließanlagen</a>: wie Schließplan und Sicherungskarte bei einem Verlust helfen.'},
  '99ee72d': {'title': '<a href="/zutrittssystem/" style="color: #FBC91B;">Elektronische Schließanlagen</a>: ein verlorener Transponder wird einfach gesperrt.'},
  '8754a23': {'editor': p('<a href="/schliessanlage-hausverwaltung/">Schließanlagen für Hausverwaltungen</a>: Schlüsselverlust und Mieterwechsel im Mehrfamilienhaus.')},
  '51f3331': {'title': 'Schlüssel weg? <br><span style="font-weight: 700; ">Wir helfen dir weiter</span>'},
  '5c65e03': {'editor': p('Wir prüfen mit dir, welche Türen betroffen sind, und tauschen nur, was getauscht werden muss. Die Aufstellung der Kosten für deine Versicherung bekommst du gleich dazu. '
              'Wir sind in ganz Norddeutschland unterwegs; alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zum <b>Schlüsselverlust im Unternehmen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zum <br><b>Schlüsselverlust im Unternehmen</b>'},
 },
 'faq': FAQ,
 'schema': artikel_schema(URL, TITEL, BESCHR),
}
