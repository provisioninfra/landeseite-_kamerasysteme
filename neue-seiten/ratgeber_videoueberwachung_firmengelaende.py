import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz

URL = BASE + '/ratgeber/videoueberwachung-firmengelaende/'
TITEL = 'Videoüberwachung auf dem Firmengelände: Was ist erlaubt?'
BESCHR = 'Darf ich mein Firmengelände per Kamera überwachen? Rechtsgrundlage, Hinweisschild, Speicherdauer, Mitarbeitende und Betriebsrat: der Leitfaden.'
KARTEN = [
 ('Die Rechtsgrundlage: berechtigtes Interesse',
  p('Für Unternehmen ist in aller Regel Art. 6 Abs. 1 lit. f DSGVO die Grundlage: Du darfst filmen, wenn du ein berechtigtes Interesse hast, die Kamera dafür erforderlich ist '
    'und die Interessen der gefilmten Personen nicht überwiegen. Berechtigt sind zum Beispiel der Schutz vor Einbruch, Diebstahl und Vandalismus oder die Aufklärung von Straftaten. '
    'Am stärksten ist deine Position, wenn es bereits Vorfälle gab und du sie belegen kannst.'),
  kurz('Zweck festlegen, Erforderlichkeit prüfen, Abwägung schriftlich festhalten.')),
 ('Was du filmen darfst und was nicht',
  p('Erlaubt sind in der Regel dein eigenes Gelände, Zufahrten, Tore, Laderampen, Lagerflächen und Eingänge. Öffentlicher Gehweg, Straße und Nachbargrundstück gehören nicht ins Bild; '
    'wo sie sich nicht ganz vermeiden lassen, werden sie geschwärzt. Tabu sind Toiletten, Umkleiden, Pausen- und Sozialräume. Tonaufnahmen sind grundsätzlich unzulässig.'),
  kurz('Eigene Flächen ja, fremde Flächen und Rückzugsräume nein, Ton nie.')),
 ('Das Hinweisschild ist Pflicht',
  p('Bevor jemand den überwachten Bereich betritt, muss er die Kamera erkennen können. Auf das Schild gehören das Kamerasymbol, wer verantwortlich ist und wie man ihn erreicht, '
    'der Zweck, die Rechtsgrundlage, die Speicherdauer und ein Hinweis, wo die vollständigen Datenschutzinformationen zu finden sind. '
    'Die Datenschutzaufsichtsbehörden stellen dafür Muster bereit.'),
  kurz('Sichtbar vor dem Kamerabereich, mit Verantwortlichem, Zweck und Speicherdauer.')),
 ('Wie lange du Aufnahmen speichern darfst',
  p('So kurz wie möglich. Die Aufsichtsbehörden halten in der Regel 48 bis 72 Stunden für ausreichend, um einen Vorfall zu bemerken. Danach werden die Aufnahmen automatisch überschrieben. '
    'Gibt es einen konkreten Vorfall, sicherst du den betroffenen Ausschnitt für Polizei und Versicherung; der Rest wird wie gewohnt gelöscht.'),
  kurz('Automatisch löschen nach wenigen Tagen, nur Vorfälle gezielt sichern.')),
 ('Mitarbeitende richtig einbinden',
  p('Kameras dürfen Beschäftigte nicht dauerhaft bei der Arbeit überwachen. Wenn Arbeitsplätze zwangsläufig ins Bild geraten, müssen die Mitarbeitenden vorher informiert werden, '
    'und die Kamera darf nicht zur Leistungs- oder Verhaltenskontrolle genutzt werden. Verdeckte Aufnahmen sind nur in eng begrenzten Ausnahmefällen bei einem konkreten Verdacht einer Straftat denkbar '
    'und sollten vorher rechtlich geprüft werden.'),
  kurz('Offen informieren, Arbeitsplätze möglichst aussparen, keine Leistungskontrolle.')),
 ('Der Betriebsrat hat ein Mitbestimmungsrecht',
  p('Gibt es einen Betriebsrat, muss er der Einführung zustimmen, denn Kameras sind technische Einrichtungen, die zur Überwachung von Beschäftigten geeignet sind (§ 87 Abs. 1 Nr. 6 BetrVG). '
    'Am besten regelt eine Betriebsvereinbarung Zweck, Kamerastandorte, Speicherdauer und wer Aufnahmen ansehen darf.'),
  kurz('Ohne Zustimmung des Betriebsrats keine Kameras.')),
 ('Dokumentation: Verzeichnis und Folgenabschätzung',
  p('Die Videoüberwachung gehört in dein Verzeichnis der Verarbeitungstätigkeiten. Überwachst du systematisch und in großem Umfang öffentlich zugängliche Bereiche, ist zusätzlich eine '
    'Datenschutz-Folgenabschätzung nötig. Lege außerdem fest, wer Zugriff auf die Aufnahmen hat, und halte das schriftlich fest. Deinen Datenschutzbeauftragten, falls vorhanden, beziehst du früh ein.'),
  kurz('Schriftlich festhalten, wer was warum filmt und wer zugreifen darf.')),
 ('Technik, die Datenschutz leichter macht',
  p('Gute Planung löst viele Fragen schon bei der Montage: enge Bildausschnitte, Privatzonen, die Gehweg oder Nachbarfenster automatisch schwärzen, Aufzeichnung lokal auf einem Rekorder '
    'statt in einer fremden Cloud, Zugriff nur mit eigenem Passwort und automatische Löschung nach der festgelegten Frist. So planen wir unsere '
    '<a href="/kamerasysteme/">Videoüberwachung für Unternehmen</a>.'),
  kurz('Datenschutz beginnt beim Kamerawinkel, nicht erst beim Formular.')),
]
FAQ = [
 ('Darf ich mein Firmengelände per Kamera überwachen?',
  p('Ja, wenn du ein berechtigtes Interesse hast, etwa Schutz vor Einbruch oder Diebstahl, die Kamera dafür erforderlich ist und die Rechte der Gefilmten nicht überwiegen. Dazu kommen Hinweisschild, kurze Speicherdauer und klare Grenzen beim Bildausschnitt.')),
 ('Brauche ich ein Hinweisschild für die Videoüberwachung?',
  p('Ja. Das Schild muss vor dem überwachten Bereich sichtbar sein und mindestens den Verantwortlichen mit Kontakt, den Zweck, die Rechtsgrundlage, die Speicherdauer und einen Hinweis auf die vollständigen Datenschutzinformationen enthalten.')),
 ('Wie lange darf ich Videoaufnahmen speichern?',
  p('So kurz wie möglich. Die Aufsichtsbehörden halten in der Regel 48 bis 72 Stunden für ausreichend. Aufnahmen eines konkreten Vorfalls darfst du zur Beweissicherung länger aufbewahren.')),
 ('Muss ich meine Mitarbeitenden über Kameras informieren?',
  p('Ja. Mitarbeitende müssen vor Inbetriebnahme informiert werden. Eine dauerhafte Überwachung am Arbeitsplatz oder eine Leistungskontrolle per Kamera ist nicht zulässig.')),
 ('Muss der Betriebsrat der Videoüberwachung zustimmen?',
  p('Ja. Nach § 87 Abs. 1 Nr. 6 BetrVG hat der Betriebsrat ein Mitbestimmungsrecht bei technischen Einrichtungen, die zur Überwachung von Beschäftigten geeignet sind. Üblich ist eine Betriebsvereinbarung.')),
 ('Darf die Kamera den Gehweg oder das Nachbargrundstück zeigen?',
  p('Nein, soweit es sich vermeiden lässt. Moderne Kameras können solche Bereiche per Privatzone dauerhaft schwärzen. Das planen wir bei der Montage gleich mit ein.')),
 ('Sind Kamera-Attrappen erlaubt?',
  p('Auch Attrappen können Menschen unter Überwachungsdruck setzen und deshalb Ärger mit Nachbarn oder Beschäftigten auslösen. Datenschutzrechtlich verarbeiten sie zwar keine Daten, Schutz bieten sie im Ernstfall aber auch nicht.')),
 ('Ersetzt dieser Ratgeber eine Rechtsberatung?',
  p('Nein. Er gibt dir einen Überblick über die üblichen Anforderungen, Stand November 2026. Für deinen Einzelfall wende dich an deinen Datenschutzbeauftragten, einen Anwalt oder die zuständige Aufsichtsbehörde.')),
]
SPEC = {
 'slug': 'videoueberwachung-firmengelaende', 'parent_slug': 'ratgeber', 'title': 'Videoüberwachung auf dem Firmengelände',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Videoüberwachung Firmengelände: Was ist erlaubt? (DSGVO)',
         'description': BESCHR, 'focuskw': 'Videoüberwachung Firmengelände', 'bctitle': 'Videoüberwachung Firmengelände', 'robots_noindex': '0'},
 'remove': REMOVE,
 'karten': KARTEN,
 'set': {
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Videoüberwachung auf dem Firmengelände:</span><br>Was ist erlaubt?'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Einbruch im Lager, Diebstahl an der Rampe, Graffiti am Tor: Viele Betriebe wollen ihr Gelände mit Kameras schützen und fragen sich, was sie dabei rechtlich beachten müssen. '
              'Dieser Leitfaden erklärt die Regeln verständlich, vom Hinweisschild bis zum Betriebsrat.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Ja, Videoüberwachung ist erlaubt, aber nur mit klaren Regeln.'},
  '7df04ae': {'editor': p('Du darfst dein Firmengelände filmen, wenn du ein berechtigtes Interesse hast, die Kamera nur deine eigenen Flächen zeigt, ein Hinweisschild vorher darauf aufmerksam macht '
              'und die Aufnahmen nach wenigen Tagen gelöscht werden. Mitarbeitende werden informiert, ein Betriebsrat muss zustimmen.')},
  'd38dec5': {'editor': p('Dieser Ratgeber gibt dir einen Überblick über die üblichen Anforderungen und ersetzt keine Rechtsberatung. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Acht Punkte, die du vor der ersten Kamera <span style="font-weight: 700; ">klären solltest</span>'},
  '43e5085': {'editor': p('Von der Rechtsgrundlage bis zur Technik: Wenn diese acht Punkte geklärt sind, ist deine Videoüberwachung auf einem soliden Fundament.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste vor der Installation'},
  '8b353e8': {'title': 'Zweck und Abwägung schriftlich festgehalten, Vorfälle der Vergangenheit dokumentiert.'},
  '6519b8c': {'title': 'Kamerawinkel und Privatzonen geplant, Hinweisschilder bestellt, Ton deaktiviert.'},
  '05ac70c': {'editor': p('Speicherdauer festgelegt, Mitarbeitende informiert, Betriebsrat beteiligt, Verzeichnis der Verarbeitungstätigkeiten ergänzt.')},
  'f1a5d3e': {'_title': 'Passend dazu', '_element_id': 'weiterlesen'},
  'cfa4bb1': {'_title': 'Passend dazu', 'title': 'Passend dazu'},
  '4967d0c': {'title': '<a href="/kamerasysteme/" style="color: #FBC91B;">Videoüberwachung für Unternehmen</a>: wie wir Kameras planen, montieren und datenschutzgerecht einrichten.'},
  '99ee72d': {'title': '<a href="/videoueberwachung-schlachthoefe/" style="color: #FBC91B;">Videoüberwachung für Schlachthöfe</a>: was die neue Kamerapflicht nach § 4d TierSchG verlangt.'},
  '8754a23': {'editor': p('<a href="/ratgeber/schluessel-verloren-unternehmen/">Schlüssel im Unternehmen verloren</a>: wer haftet und was jetzt zu tun ist.')},
  '51f3331': {'title': 'Kameras, die erlaubt sind <br><span style="font-weight: 700; ">und im Ernstfall helfen</span>'},
  '5c65e03': {'editor': p('Wir planen Videoüberwachung so, dass sie rechtlich sauber ist und trotzdem Bilder liefert, mit denen Polizei und Versicherung arbeiten können: mit Begehung, Kamerawinkeln, '
              'Privatzonen, Hinweisschildern und lokaler Aufzeichnung. Im Einsatz sind wir in ganz Norddeutschland, alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zur <b>Videoüberwachung im Unternehmen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zur <br><b>Videoüberwachung im Unternehmen</b>'},
 },
 'faq': FAQ,
 'schema': artikel_schema(URL, TITEL, BESCHR),
}
