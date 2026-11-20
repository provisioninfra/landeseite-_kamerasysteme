import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, ORG, BASE, VERBOTEN, ORTE_NORD, ORDER, GRUENDER, PRESSE, video_kasten, cta, analyse, stell_dir_vor, vorteile

URL = BASE + '/mechanische-schliessanlagen/'
def p(t): return '<p>' + t + '</p>'
FAQ = [
 ('Was kostet eine mechanische Schließanlage?',
  p('Den Preis bestimmen vor allem die Zahl der Türen und Schlüssel. Auch der Schutzgrad des Profils spielt mit hinein. Eine kleine Anlage für ein Büro kostet deutlich weniger '
    'als eine für Halle und Verwaltung mit Außentoren. Nach der Begehung bekommst du den Kostenrahmen schriftlich, ohne versteckte Posten.')),
 ('Was unterscheidet Generalhauptschlüssel, Gruppenschlüssel und Einzelschlüssel?',
  p('Mit dem Generalhauptschlüssel öffnest du jede Tür der Anlage. Ein Gruppenschlüssel ist auf einen Bereich begrenzt, etwa auf die Werkstatt. '
    'Der Einzelschlüssel passt nur zu einer Tür. Haupteingang und Tor lassen sich so einrichten, dass jeder Schlüssel sie öffnet. Welche Ebenen du brauchst, halten wir im Schließplan fest.')),
 ('Wozu brauche ich eine Sicherungskarte?',
  p('Sie ist dein Eigentumsnachweis. Nachschlüssel und Zylinder werden nur gegen Vorlage der Karte gefertigt. So weißt du jederzeit, wie viele Schlüssel existieren. '
    'Bewahre die Karte getrennt von den Schlüsseln auf.')),
 ('Was passiert, wenn ein Schlüssel der Schließanlage verloren geht?',
  p('Entscheidend ist, welcher Schlüssel fehlt. Bei einem Einzelschlüssel genügt meist ein neuer Zylinder. Fehlt ein Gruppen- oder Generalhauptschlüssel, '
    'ermitteln wir anhand des Schließplans die betroffenen Türen und tauschen gezielt. Kommt so etwas häufiger vor, zeigen wir dir, ab wann sich '
    '<a href="/zutrittssystem/">elektronische Zylinder</a> rechnen.')),
 ('Wer haftet, wenn ein Mitarbeiter einen Schlüssel verliert?',
  p('Das hängt vom Einzelfall ab, unter anderem vom Arbeitsvertrag und davon, wie der Verlust passiert ist. Verbindlich klären das deine Versicherung oder ein Anwalt. '
    'Technisch hilft ein sauber dokumentierter Schließplan, weil er den Austausch und damit den Schaden klein hält. Mehr dazu im Ratgeber '
    '<a href="/ratgeber/schluessel-verloren-unternehmen/">Schlüssel im Unternehmen verloren</a>.')),
 ('Kann ich meine mechanische Schließanlage später erweitern?',
  p('Ja. Neue Türen oder ein Anbau lassen sich jederzeit aufnehmen, weil jede Anlage auf ihrem Schließplan aufbaut. Wir bestellen die passenden Zylinder und tragen die Änderung nach.')),
 ('Lässt sich eine mechanische Anlage mit elektronischen Zylindern kombinieren?',
  p('Ja, für viele Betriebe ist genau das die wirtschaftlichste Lösung. Stark genutzte Türen bekommen elektronische Zylinder, Nebenräume bleiben mechanisch. '
    'Einen Überblick gibt der <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.')),
 ('Wie lange dauert der Einbau einer mechanischen Schließanlage?',
  p('Sobald du den Schließplan freigibst, fertigt der Hersteller die Anlage. Der Einbau dauert bei kleineren Objekten meist einen Tag. '
    'Größere Gebäude bauen wir abschnittsweise um, damit dein Betrieb weiterläuft. Den Zeitplan findest du im Angebot.')),
 ('Welche Hersteller verbaut ProVision Infra?',
  p('Mechanische Schließanlagen bauen wir mit EVVA. Für elektronische Komponenten setzen wir auf EVVA, SimonsVoss, Keyota, Keyrent und NUKI. '
    'Welches System zu deinem Gebäude passt, entscheiden wir nach der Begehung.')),
 ('Übernehmt ihr Wartung und Service für bestehende Anlagen?',
  p('Ja. Wir warten Zylinder und ersetzen verschlissene Teile. Nachschlüssel bestellen wir gegen Vorlage der Sicherungskarte. Bei neuen Anlagen beraten wir herstellerneutral und übernehmen auf Wunsch die gesamte Projektierung.')),
]
SPEC = {
 'slug': 'mechanische-schliessanlagen', 'title': 'Mechanische Schließanlagen',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '>Uelzen<', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Mechanische Schließanlage für Unternehmen | ProVision Infra',
         'description': 'Mechanische Schließanlagen von EVVA mit Sicherungskarte für Betriebe in Norddeutschland: Beratung, Schließplan, Montage, Nachschlüssel und Service.',
         'focuskw': 'mechanische Schließanlage', 'bctitle': 'Mechanische Schließanlagen', 'robots_noindex': '0'},
 'remove': ['a3564b7', '7dfd9f6', 'aed8a2d', 'f9348eb'],
 'order': ORDER,
 'handy_css': True,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Mechanische Schließanlagen</span><br>für Unternehmen in Norddeutschland'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Zwölf Schlüssel sind im Umlauf, und keiner weiß genau, wer welchen hat. Der Generalschlüssel? Ist mit einem ehemaligen Mitarbeiter gegangen. '
              'Spätestens jetzt zeigt sich, ob eine Schließanlage geplant wurde oder einfach gewachsen ist.<br><br>'
              '<span style="font-weight: 700;">ProVision Infra plant und betreut mechanische Schließanlagen von EVVA mit Sicherungskarte. Mit einem sauberen Schließplan weißt du jederzeit, wer welche Tür öffnet. '
              'Und fehlt später ein Schlüssel, rufst du genau eine Nummer an: unsere.</span>'},
  '34dc7fa': {'_title': 'Einleitung + Film'},
  'd05eab3': {'_title': 'Einleitung Überschrift', 'title': 'Eine Schließanlage ist nur so sicher wie ihr Schließplan.'},
  '7df04ae': {'editor': p('In einer mechanischen Schließanlage regelt ein einziges System, wer welche Tür öffnen darf. Die Geschäftsführung kommt überall hinein, die Reinigungsfirma nur in die Sozialräume. '
              'Trotzdem trägt jeder nur einen Schlüssel am Bund. Damit das über Jahre so bleibt, braucht es einen durchdachten Schließplan und ein Profil, das sich nicht einfach kopieren lässt.')},
  'd38dec5': {'editor': p('Genau hier setzen wir an. Gemeinsam mit dir projektieren wir die Anlage und bauen anschließend EVVA-Zylinder mit Sicherungskarte ein. '
              'Nachschlüssel und spätere Erweiterungen bekommst du ebenfalls von uns. Alle Arbeiten erledigt unser eigenes Team, Subunternehmer setzen wir nicht ein.')},
  'd7f768f': {'_title': 'Aufbau mechanische Schließanlage'},
  '74b6d54': {'_title': 'Aufbau Überschrift', 'title': 'So funktioniert eine mechanische Schließanlage: <span style="font-weight: 700; ">vom Schließplan bis zum Nachschlüssel</span>'},
  '43e5085': {'editor': p('Ob deine Anlage nach Jahren noch stimmt, entscheiden fünf Bausteine. Fehlt einer davon, weiß irgendwann niemand mehr, welcher Schlüssel welche Tür öffnet.')},
  '8cc96a4': {'title': 'Der Schließplan'},
  '71be80d': {'editor': p('Das Herz jeder Anlage ist eine Übersicht aller Türen und aller Schlüssel. Sie legt fest, wer wo hineinkommt, und wird vor der Bestellung mit dir abgestimmt. '
              'Jede spätere Erweiterung baut darauf auf.')},
  '59a04cb': {'editor': p('Den Schließplan bekommst du schriftlich. Auch wir dokumentieren ihn, damit jede Nachbestellung genau passt.')},
  '5e90e79': {'title': 'Hauptschlüssel, Gruppen- und Einzelschlüssel'},
  '88e4e41': {'editor': p('Ein Generalhauptschlüssel öffnet alle Türen, ein Gruppenschlüssel nur einen Bereich wie die Werkstatt. Mit dem Einzelschlüssel kommst du durch genau eine Tür. '
              'Den Haupteingang können trotzdem alle öffnen, sodass jeder mit einem einzigen Schlüssel auskommt.')},
  'ca72bdb': {'editor': p('Die Verantwortung ist klar geregelt, und niemand muss mehr raten, wer wo hineinkommt.')},
  'b452400': {'title': 'Sicherungskarte und Kopierschutz'},
  '6773460': {'editor': p('Bei EVVA-Anlagen mit Sicherungskarte entstehen Nachschlüssel nur gegen Vorlage der Karte. Das Profil ist geschützt und lässt sich an keiner gewöhnlichen Kopiermaschine nachmachen.')},
  '24f8396': {'editor': p('So behältst du die Kontrolle über die Zahl der Schlüssel. Legst du uns die Karte vor, bestellen wir Nachschlüssel für dich.')},
  '5860b09': {'title': 'Austausch bei Schlüsselverlust'},
  'dc25036': {'editor': p('Fehlt ein Einzelschlüssel, reicht oft ein neuer Zylinder. Bei einem verlorenen Gruppen- oder Generalhauptschlüssel prüfen wir mit dir im Schließplan, '
              'welche Türen betroffen sind. Getauscht wird dann gezielt an diesen Stellen.')},
  '4838414': {'editor': p('Deine Türen sind schnell wieder sicher, und du zahlst nur für die Zylinder, die es wirklich braucht. Häufen sich Verluste, rechnen wir dir den Umstieg auf elektronische Zylinder vor.')},
  'bb8c516': {'title': 'Erweitern, warten, kombinieren'},
  '6414a37': {'editor': p('Kommen neue Räume oder ein zweiter Standort hinzu, wächst die Anlage über den Schließplan mit. Verschlissene Zylinder ersetzen wir bei der Wartung. '
              'Stark genutzte Eingänge kombinieren wir auf Wunsch mit <a href="/zutrittssystem/">elektronischen Zylindern</a>.')},
  'f5080c1': {'editor': p('Mechanisch arbeiten wir mit EVVA. Für elektronische Ergänzungen kommen unter anderem SimonsVoss und NUKI in Frage.')},
  '3ac3e9e': {'editor': p('Deine Anlage wächst mit, und bei jeder Frage erreichst du denselben Ansprechpartner.')},
  'd70fb3d': {'_title': 'Mechanisch oder elektronisch', '_element_id': 'vergleich'},
  'c869af6': {'_title': 'Mechanisch oder elektronisch', 'title': 'Mechanisch oder elektronisch? Die Antwort hängt von deinem Betrieb ab.'},
  '8b353e8': {'title': 'Mechanisch lohnt sich bei wenigen Türen und einem festen Team. Die Anlage kommt ohne Strom und Software aus und hält bei guter Pflege viele Jahre.'},
  '6519b8c': {'title': 'Elektronisch rechnet sich, sobald viele Menschen kommen und gehen, etwa im Schichtbetrieb. Ein verlorener Transponder ist dann mit einem Klick gesperrt.'},
  '05ac70c': {'editor': p('Häufig ist die Mischung am wirtschaftlichsten: mechanische Zylinder in Nebenräumen, elektronische am Eingang. Wir rechnen dir die Varianten durch und sagen dir offen, '
              'welche sich lohnt. Mehr dazu im <a href="/schliesssysteme/">Vergleich der Schließsysteme</a>.')},
  'f1a5d3e': {'_title': 'Leistungen', '_element_id': 'leistungen'},
  'cfa4bb1': {'_title': 'Leistungen', 'title': 'Unsere Leistungen für mechanische Schließanlagen'},
  '4967d0c': {'title': 'Beratung und Planung: Wir nehmen jede Tür auf und klären mit dir die Zugänge. Daraus entsteht eine Anlage, die zu Gebäude und Budget passt.'},
  '99ee72d': {'title': 'Schließplan: Wir legen die Schlüsselebenen fest und dokumentieren sie. Bestellt wird erst, wenn du jede Zeile abgesegnet hast.'},
  '8754a23': {'editor': p('Montage: Wir bauen die EVVA-Zylinder ein und prüfen jede einzelne Tür, bevor wir dir die Anlage übergeben.')},
  '51f3331': {'title': 'Mechanische Schließanlagen <br><span style="font-weight: 700; ">in ganz Norddeutschland</span>'},
  '5c65e03': {'editor': p('Unser Firmensitz liegt in Bad Bevensen im Landkreis Uelzen. Von dort aus planen und montieren wir Schließanlagen in '
              '<a href="/lueneburg/">Lüneburg</a>, <a href="/uelzen/">Uelzen</a>, <a href="/celle/">Celle</a>, <a href="/winsen-luhe/">Winsen (Luhe)</a> '
              'und im Wendland. Auch zwischen Hamburg und Hannover sind wir regelmäßig unterwegs. Alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') +
              p('Für die Bestandsaufnahme kommen wir zu dir, damit der Schließplan wirklich zu deinem Gebäude passt.') + NAP},
  '7983242': {'title': 'Häufige Fragen zu <b>mechanischen Schließanlagen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zu <br><b>mechanischen Schließanlagen</b>'},
 },
 'graft': stell_dir_vor([
    'Ein Mitarbeiter verliert seinen Schlüssel, und du weißt sofort, welche Türen betroffen sind.',
    'Heimlich nachmachen lässt sich kein Schlüssel, weil das Profil geschützt ist.',
    'Die Reinigungsfirma kommt in die Sozialräume. Das Lager bleibt für sie zu.',
    'Fällt der Strom aus, schließt trotzdem jede Tür wie gewohnt.',
    'Neue Kollegen bekommen am ersten Tag genau den Schlüssel, den sie brauchen.',
    'An deinem Bund hängt ein einziger Schlüssel für alle Türen, die du öffnen darfst.',
    'Der Schließplan liegt dir schriftlich vor, und jede Erweiterung baut darauf auf.',
    'Kommt ein zweiter Standort dazu, wächst die Anlage einfach mit.']) + [
   analyse('Bevor wir einen einzigen Zylinder bestellen, schauen wir uns an, wie dein Betrieb heute mit Schlüsseln arbeitet:',
           ('Wer braucht welche Türen?', 'Wie oft wechseln die Nutzer?', 'Welche Räume sind besonders kritisch?'),
           'Aus den Antworten entsteht ein Schließplan, der zu deinem Alltag passt.'),
  ] + vorteile([
    ('Klare Ordnung:', 'Der Schließplan legt fest, wer welche Tür öffnet. Das Rätselraten hat ein Ende.'),
    ('Schutz vor Kopien:', 'Nachschlüssel gibt es bei EVVA nur gegen Vorlage der Sicherungskarte.'),
    ('Unabhängig vom Strom:', 'Zylinder und Schlüssel arbeiten ohne Batterie und ohne Software.'),
    ('Ein Schlüssel am Bund:', 'Jede Person trägt genau einen Schlüssel für ihre Türen.'),
    ('Für Handwerk und Landwirtschaft:', 'Werkstatt und Lager hängen an einer robusten Anlage, die viele Jahre hält.'),
    ('Für Praxen und kleine Büros:', 'Das Team ist überschaubar, und in Akten- oder Medikamentenräume kommen trotzdem nur Berechtigte.'),
    ('Für Hausverwaltungen und Vereine:', 'Ein Schlüssel öffnet Haustür und Wohnung. Mehr dazu auf der Seite für <a href="/schliessanlage-hausverwaltung/">Hausverwaltungen</a>.'),
    ('Planbare Kosten bei Verlust:', 'Getauscht werden nur die Zylinder, die der verlorene Schlüssel öffnet.'),
    ('Offen für später:', 'Stark genutzte Eingänge lassen sich jederzeit elektronisch nachrüsten.'),
  ]) + [
   cta('So kommst du zu deiner mechanischen Schließanlage',
       'Ob mechanisch reicht oder eine Kombination besser passt, klären wir im Erstgespräch. Danach weißt du, was deine Anlage kostet und wie lange der Umbau dauert.'),
   video_kasten('Kameras ergänzen eine Schließanlage dort, wo Schlüssel allein nicht reichen, zum Beispiel an Toren und Laderampen. Wir planen beides zusammen und installieren Kamerasysteme mit Alarm aufs Handy.'),
   PRESSE,
 ],
 'ablauf': {
  'Erstgespräch': p('Ein kurzes Telefonat genügt für den Anfang. Wir fragen nach Türen und Nutzern und sagen dir ehrlich, ob eine mechanische Anlage reicht oder eine Kombination besser passt.'),
  'Termin vor Ort': p('Vor Ort nehmen wir jede Tür auf und messen die Zylinder aus. Den Kostenrahmen erfährst du noch beim Termin.'),
  'Planung deines Systems': p('Du erhältst den Schließplan und ein Angebot, das zu deinem Budget passt. Gefertigt wird die Anlage bei EVVA erst, wenn du den Plan freigegeben hast.'),
  'Umsetzung': p('Wir tauschen die Zylinder Tür für Tür, bei kleineren Objekten meist an einem Tag. Dein Betrieb läuft dabei weiter, und jede Tür wird nach dem Einbau geprüft.'),
  'Übergabe & Betreuung': p('Zum Schluss bekommst du die Schlüssel samt Sicherungskarte und den dokumentierten Schließplan. Auch danach sind wir für Nachschlüssel und Wartung erreichbar.'),
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
SPEC['clone'] = [
 ('985957a', '58762b2', '985957a', {
   '4967d0c': {'title': 'Nachschlüssel: Gegen Vorlage der Sicherungskarte bestellen wir neue Schlüssel, passend zum Schließplan.'},
   '99ee72d': {'title': 'Schlüsselverlust: Wir tauschen genau die Zylinder, die der verlorene Schlüssel öffnet, und aktualisieren den Plan.'},
   '8754a23': {'editor': p('Wartung und Erweiterung: Wir nehmen neue Türen auf und ersetzen verschlissene Zylinder. Stark genutzte Eingänge rüsten wir auf Wunsch elektronisch nach.')},
 }),
]
