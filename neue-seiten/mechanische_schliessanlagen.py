import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD

URL = BASE + '/mechanische-schliessanlagen/'
FAQ = [
 ('Was kostet eine mechanische Schließanlage?',
  '<p>Der Preis hängt von der Zahl der Türen und Schlüssel, den Zylinderlängen, dem Schutzgrad des Systems und dem Umfang des Schließplans ab. '
  'Eine kleine Anlage für ein Büro mit wenigen Türen ist deutlich günstiger als eine Anlage für Halle, Verwaltung und Außentore. '
  'Den konkreten Kostenrahmen nennen wir dir nach der Begehung, schriftlich und ohne versteckte Posten.</p>'),
 ('Was ist der Unterschied zwischen Generalhauptschlüssel, Gruppenschlüssel und Einzelschlüssel?',
  '<p>Der Generalhauptschlüssel öffnet alle Türen der Anlage. Ein Gruppenschlüssel öffnet einen Bereich, zum Beispiel Verwaltung, Lager oder Werkstatt. '
  'Ein Einzelschlüssel öffnet genau eine Tür oder einen Raum. Zentrale Türen wie Haupteingang oder Tor lassen sich so einstellen, dass alle Schlüssel sie öffnen. '
  'Welche Ebenen du brauchst, legen wir gemeinsam im Schließplan fest.</p>'),
 ('Wozu brauche ich eine Sicherungskarte?',
  '<p>Die Sicherungskarte ist der Eigentumsnachweis für deine Anlage. Nachschlüssel und weitere Zylinder werden nur gegen Vorlage der Karte gefertigt. '
  'So weißt du jederzeit, wie viele Schlüssel es gibt, und niemand kann sich unbemerkt einen weiteren besorgen. '
  'Bewahre die Karte getrennt von den Schlüsseln auf.</p>'),
 ('Was passiert, wenn ein Schlüssel der Schließanlage verloren geht?',
  '<p>Das hängt davon ab, welcher Schlüssel fehlt. Ein Einzelschlüssel lässt sich meist mit dem Tausch eines Zylinders auffangen. '
  'Bei einem Gruppen- oder Generalhauptschlüssel prüfen wir anhand des Schließplans, welche Zylinder betroffen sind, und tauschen gezielt. '
  'Geht es häufiger um verlorene Schlüssel, rechnen wir dir vor, ab wann sich <a href="/zutrittssystem/">elektronische Zylinder</a> lohnen.</p>'),
 ('Wer haftet, wenn ein Mitarbeiter einen Schlüssel verliert?',
  '<p>Das hängt vom Einzelfall ab, unter anderem vom Arbeitsvertrag und davon, wie der Schlüssel verloren ging. Rechtlich verbindlich klären das deine Versicherung oder ein Anwalt. '
  'Technisch gilt: Je sauberer der Schließplan dokumentiert ist, desto genauer lässt sich der Austausch und damit der Schaden begrenzen.</p>'),
 ('Kann ich meine mechanische Schließanlage später erweitern?',
  '<p>Ja. Weil jede Anlage auf einem Schließplan aufbaut, lassen sich neue Türen, Räume oder ganze Gebäudeteile nachträglich aufnehmen. '
  'Wir bestellen die passenden Zylinder und Schlüssel und tragen die Änderung im Schließplan nach.</p>'),
 ('Lässt sich eine mechanische Anlage mit elektronischen Zylindern kombinieren?',
  '<p>Ja, und für viele Betriebe ist das die wirtschaftlichste Lösung: elektronische Zylinder für stark genutzte Türen wie Eingang, Lager oder Serverraum, '
  'mechanische für Nebenräume. Einen Überblick über die Systeme findest du im <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.</p>'),
 ('Wie lange dauert der Einbau einer mechanischen Schließanlage?',
  '<p>Nach der Freigabe des Schließplans fertigt der Hersteller die Anlage. Der Einbau selbst ist bei kleineren Objekten meist an einem Tag erledigt. '
  'Größere Gebäude bauen wir in Abschnitten um, damit dein Betrieb weiterläuft. Den Zeitplan bekommst du mit dem Angebot.</p>'),
 ('Welche Hersteller verbaut ProVision Infra?',
  '<p>Mechanische Schließanlagen bauen wir mit EVVA. Für elektronische Komponenten arbeiten wir mit EVVA, SimonsVoss, Keyota, Keyrent und NUKI. '
  'Welches System zu deinem Gebäude passt, entscheiden wir nach der Begehung und nicht nach Prospekt.</p>'),
 ('Übernehmt ihr Wartung und Service für bestehende Anlagen?',
  '<p>Ja. Wir warten Zylinder, ersetzen verschlissene Teile, bestellen Nachschlüssel gegen Sicherungskarte und erweitern deine Anlage. '
  'Für die Planung neuer Anlagen beraten wir dich herstellerneutral und übernehmen auf Wunsch die komplette Projektierung.</p>'),
]
SPEC = {
 'slug': 'mechanische-schliessanlagen',
 'title': 'Mechanische Schließanlagen',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', 'href="/uelzen/"', '>Uelzen<', '/uelzen/', '"name": "Uelzen"'],
 'seo': {'title': 'Mechanische Schließanlage für Unternehmen | ProVision Infra',
         'description': 'Mechanische Schließanlagen von EVVA mit Sicherungskarte für Betriebe in Norddeutschland: Beratung, Schließplan, Montage, Nachschlüssel und Service.',
         'focuskw': 'mechanische Schließanlage', 'bctitle': 'Mechanische Schließanlagen', 'robots_noindex': '0'},
 'remove': ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb'],
 'clone': [
   # zweite Dreierreihe für die Leistungen: Reihe 985957a im Zielgruppen-Block klonen (wird unten zum Leistungsblock)
 ],
 'set': {
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Mechanische Schließanlagen</span><br>für Unternehmen in Norddeutschland'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Zwölf Schlüssel im Umlauf, keiner weiß genau, wer welchen hat, und der Generalschlüssel ist mit einem ehemaligen Mitarbeiter gegangen. '
              'Spätestens dann zeigt sich, ob eine Schließanlage geplant wurde oder nur gewachsen ist.<br><br>'
              '<span style="font-weight: 700;">ProVision Infra plant, montiert und betreut mechanische Schließanlagen von EVVA mit Sicherungskarte: '
              'mit sauberem Schließplan, geschützten Nachschlüsseln und einem festen Ansprechpartner, von der ersten Beratung bis zur Erweiterung.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Eine Schließanlage ist nur so sicher wie ihr Schließplan.'},
  '7df04ae': {'editor': '<p>Eine mechanische Schließanlage regelt mit einem einzigen System, wer welche Tür öffnen darf: Die Geschäftsführung schließt alles, '
              'das Lagerteam Halle und Rampe, die Reinigung nur Eingang und Sozialräume. Jeder trägt genau einen Schlüssel. Damit das über Jahre so bleibt, '
              'braucht es zwei Dinge: einen durchdachten Schließplan und einen Schlüssel, den niemand ohne Berechtigung nachmachen kann.</p>'},
  'd38dec5': {'editor': '<p>Genau dafür sind wir da. Wir beraten dich herstellerneutral, planen und projektieren die Anlage mit dir, montieren Zylinder von EVVA '
              'mit Sicherungskarte und bleiben danach dein Ansprechpartner für Nachschlüssel, Erweiterungen und Wartung. Beratung, Planung, Montage und Service '
              'machen wir selbst, ohne Subunternehmer.</p>'},
  'd7f768f': {'_title': 'Aufbau mechanische Schließanlage'},
  '74b6d54': {'_title': 'Aufbau Überschrift', 'title': 'So funktioniert eine mechanische Schließanlage: <span style="font-weight: 700; ">vom Schließplan bis zum Nachschlüssel</span>'},
  '43e5085': {'editor': '<p>Fünf Bausteine entscheiden darüber, ob deine Anlage nach Jahren noch stimmt oder ob irgendwann niemand mehr weiß, welcher Schlüssel welche Tür öffnet.</p>'},
  '8cc96a4': {'title': 'Der Schließplan'},
  '71be80d': {'editor': '<p>Der Schließplan ist das Herz der Anlage: eine Übersicht aller Türen und aller Schlüssel. Er legt fest, wer wo hineinkommt, und wird vor der '
              'Bestellung mit dir abgestimmt. Jede spätere Erweiterung baut auf ihm auf.</p>'},
  '59a04cb': {'editor': '<p>Du bekommst den Schließplan schriftlich. Bei uns ist er ebenfalls dokumentiert, damit jede Nachbestellung genau passt.</p>'},
  '5e90e79': {'title': 'Hauptschlüssel, Gruppen- und Einzelschlüssel'},
  '88e4e41': {'editor': '<p>Ein Generalhauptschlüssel öffnet alle Türen, ein Gruppenschlüssel einen Bereich wie Büro, Lager oder Werkstatt, ein Einzelschlüssel genau eine Tür. '
              'Haupteingang und Tor öffnen trotzdem alle. So trägt jeder nur einen Schlüssel am Bund.</p>'},
  'ca72bdb': {'editor': '<p>Klare Verantwortung und kein Raten mehr, wer eigentlich wo hineinkommt.</p>'},
  'b452400': {'title': 'Sicherungskarte und Kopierschutz'},
  '6773460': {'editor': '<p>Bei EVVA-Anlagen mit Sicherungskarte werden Nachschlüssel nur gegen Vorlage der Karte gefertigt. Das Schlüsselprofil ist geschützt '
              'und lässt sich nicht einfach an einer Kopiermaschine nachmachen.</p>'},
  '24f8396': {'editor': '<p>Du behältst die Kontrolle darüber, wie viele Schlüssel es gibt. Nachschlüssel bestellen wir für dich, sobald du die Karte vorlegst.</p>'},
  '5860b09': {'title': 'Austausch bei Schlüsselverlust'},
  'dc25036': {'editor': '<p>Fehlt ein Einzelschlüssel, reicht oft der Tausch eines Zylinders. Bei einem verlorenen Gruppen- oder Generalhauptschlüssel prüfen wir mit dir '
              'anhand des Schließplans, welche Zylinder betroffen sind, und tauschen gezielt statt pauschal.</p>'},
  '4838414': {'editor': '<p>Schnell wieder sicher, ohne mehr auszugeben als nötig. Häufen sich Verluste, zeigen wir dir, ab wann sich elektronische Zylinder rechnen.</p>'},
  'bb8c516': {'title': 'Erweitern, warten, kombinieren'},
  '6414a37': {'editor': '<p>Neue Räume, ein Anbau, ein zweiter Standort: Weil die Anlage auf dem Schließplan aufbaut, wächst sie mit. Wir warten Zylinder, ersetzen '
              'verschlissene Teile und kombinieren mechanische Türen bei Bedarf mit <a href="/zutrittssystem/">elektronischen Zylindern</a> für stark genutzte Eingänge.</p>'},
  'f5080c1': {'editor': '<p>Mechanische Zylinder von EVVA, auf Wunsch kombiniert mit elektronischen Komponenten von EVVA, SimonsVoss, Keyota, Keyrent oder NUKI.</p>'},
  '3ac3e9e': {'editor': '<p>Eine Anlage, die mit deinem Betrieb wächst, und ein Ansprechpartner für alles, was danach kommt.</p>'},
  'd70fb3d': {'_title': 'Mechanisch oder elektronisch', '_element_id': 'vergleich'},
  'c869af6': {'_title': 'Mechanisch oder elektronisch', 'title': 'Mechanisch oder elektronisch? Die ehrliche Antwort hängt von deinem Betrieb ab.'},
  '8b353e8': {'title': 'Mechanisch passt, wenn du wenige Türen, ein festes Team und seltene Wechsel hast. Die Anlage braucht keinen Strom und keine Software und hält bei guter Pflege viele Jahre.'},
  '6519b8c': {'title': 'Elektronisch rechnet sich, wenn viele Menschen kommen und gehen: Schichtbetrieb, Dienstleister, Mieterwechsel. Ein verlorener Transponder ist dann mit einem Klick gesperrt.'},
  '05ac70c': {'editor': '<p>Oft ist beides die beste Lösung: mechanische Zylinder für Nebenräume, elektronische für Eingang, Lager und Serverraum. Wir rechnen dir die '
              'Varianten durch und sagen dir offen, welche sich lohnt. Mehr dazu im <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.</p>'},
  'f1a5d3e': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'cfa4bb1': {'_title': 'Leistungen', 'title': 'Unsere Leistungen für mechanische Schließanlagen'},
  '4967d0c': {'title': 'Beratung und Planung: Wir nehmen jede Tür auf, klären mit dir, wer wo Zugang braucht, und projektieren die Anlage passend zu Gebäude und Budget.'},
  '99ee72d': {'title': 'Schließplan erstellen: General-, Gruppen- und Einzelschlüssel, sauber dokumentiert und vor der Bestellung mit dir abgestimmt.'},
  '8754a23': {'editor': '<p>Montage von EVVA-Zylindern mit Sicherungskarte: Wir bauen ein, prüfen jede Tür und übergeben dir Schlüssel, Karte und Schließplan.</p>'},
  '51f3331': {'title': 'Mechanische Schließanlagen <br><span style="font-weight: 700; ">in ganz Norddeutschland</span>'},
  '5c65e03': {'editor': '<p>Unser Firmensitz liegt in Bad Bevensen im Landkreis Uelzen. Von hier aus planen und montieren wir mechanische Schließanlagen in '
              '<a href="/lueneburg/">Lüneburg</a>, <a href="/uelzen/">Uelzen</a>, <a href="/celle/">Celle</a>, <a href="/winsen-luhe/">Winsen (Luhe)</a>, '
              'im Wendland und im ganzen Raum zwischen Hamburg und Hannover. Alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.</p>'
              '<p>Für die Bestandsaufnahme kommen wir zu dir, damit der Schließplan zu deinem Gebäude passt.</p>' + NAP},
  '7983242': {'title': 'Häufige Fragen zu <b>mechanischen Schließanlagen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zu <br><b>mechanischen Schließanlagen</b>'},
 },
 'ablauf': {
  'Erstgespräch': '<p>Ein kurzes Telefonat: Wie viele Türen, wie viele Menschen, wie oft wechseln sie? Du bekommst sofort eine ehrliche Einschätzung, ob mechanisch, elektronisch oder kombiniert am besten passt.</p>',
  'Termin vor Ort': '<p>Wir kommen zu dir, nehmen jede Tür auf, messen die Zylinder und klären, wer wo Zugang braucht. Den Kostenrahmen nennen wir dir noch vor Ort.</p>',
  'Planung deines Systems': '<p>Du erhältst den Schließplan und ein Angebot, das zu deinem Budget passt. Erst wenn du den Plan freigibst, wird die Anlage bei EVVA gefertigt.</p>',
  'Umsetzung': '<p>Wir tauschen die Zylinder Tür für Tür, bei kleineren Objekten meist an einem Tag, und dein Betrieb läuft weiter. Jede Tür wird nach dem Einbau geprüft.</p>',
  'Übergabe & Betreuung': '<p>Du bekommst Schlüssel, Sicherungskarte und den dokumentierten Schließplan. Für Nachschlüssel, Erweiterung und Wartung bleiben wir dein Ansprechpartner.</p>',
 },
 'faq': FAQ,
 'schema': {"@context": "https://schema.org", "@graph": [ORG, {
    "@type": "Service", "@id": URL + "#leistung", "name": "Mechanische Schließanlagen für Unternehmen",
    "serviceType": "Mechanische Schließanlage", "url": URL,
    "description": "Beratung, Planung, Projektierung, Montage und Wartung mechanischer Schließanlagen von EVVA mit Sicherungskarte; Schließplan, Nachschlüssel und Austausch bei Schlüsselverlust.",
    "provider": {"@id": BASE + "/#organization"}, "brand": {"@type": "Brand", "name": "EVVA"},
    "areaServed": [{"@type": "City", "name": o} for o in ORTE_NORD] + [{"@type": "State", "name": "Niedersachsen"}],
    "audience": {"@type": "BusinessAudience", "name": "Unternehmen, Praxen, Hausverwaltungen und Vereine"},
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Leistungen mechanische Schließanlagen", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
        ["Beratung und Planung", "Schließplan erstellen", "Montage EVVA-Zylinder", "Nachschlüssel gegen Sicherungskarte", "Austausch bei Schlüsselverlust", "Wartung und Erweiterung"]]}}]},
}
# Zweite Leistungsreihe: Reihe 985957a klonen und hinter die erste setzen; danach eine dritte Reihe für die Zielgruppen
SPEC['clone'] = [
 ('f1a5d3e', None, 'f1a5d3e', {
   'f1a5d3e': {'_title': 'Zielgruppen'},
   'cfa4bb1': {'_title': 'Zielgruppen', 'title': 'Für wen sich eine mechanische Schließanlage lohnt'},
   '4967d0c': {'title': 'Handwerk, Produktion und Landwirtschaft: Werkstatt, Halle, Büro und Lager in einer Anlage, robust und ganz ohne Strom und Software.'},
   '99ee72d': {'title': 'Praxen, Kanzleien und kleine Büros: wenige Türen, feste Teams, und trotzdem kommen nur Berechtigte in Akten- und Medikamentenräume.'},
   '8754a23': {'editor': '<p>Hausverwaltungen und Vereine: ein Schlüssel für Haustür, Keller und Wohnung, geschützt vor Kopien. Mehr dazu für '
               '<a href="/schliessanlage-hausverwaltung/">Hausverwaltungen und Mehrfamilienhäuser</a>.</p>'},
 }), ('985957a', '58762b2', '985957a', {
   '4967d0c': {'title': 'Nachschlüssel bestellen: Gegen Vorlage der Sicherungskarte bestellen wir Schlüssel nach, passend zum Schließplan.'},
   '99ee72d': {'title': 'Austausch bei Verlust: Wir tauschen genau die Zylinder, die der verlorene Schlüssel öffnet, und aktualisieren den Schließplan.'},
   '8754a23': {'editor': '<p>Wartung und Erweiterung: neue Türen, neue Bereiche, verschlissene Zylinder. Auf Wunsch mit elektronischen Komponenten an stark genutzten Türen.</p>'},
 }),
]
