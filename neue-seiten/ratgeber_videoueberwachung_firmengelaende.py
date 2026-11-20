import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gemeinsam import NAP, BASE, VERBOTEN
from gemeinsam_artikel import AUTOR_ZEILE, REMOVE, artikel_schema, p, kurz, ORDER, GRUENDER, PRESSE, video_kasten, cta, stell_dir_vor

URL = BASE + '/ratgeber/videoueberwachung-firmengelaende/'
TITEL = 'Videoüberwachung auf dem Firmengelände: Was ist erlaubt?'
BESCHR = 'Darf ich mein Firmengelände per Kamera überwachen? Rechtsgrundlage, Hinweisschild, Speicherdauer, Mitarbeitende und Betriebsrat: der Leitfaden.'
KARTEN = [
 ('Die Rechtsgrundlage: berechtigtes Interesse',
  p('Für private Unternehmen stützt sich Videoüberwachung in aller Regel auf Art. 6 Abs. 1 lit. f DSGVO. Du brauchst also einen berechtigten Zweck, etwa den Schutz vor Einbruch oder die Aufklärung von Diebstählen. '
    'Die Kamera muss für diesen Zweck erforderlich sein, und die Interessen der Gefilmten dürfen nicht überwiegen. '
    'Gab es bereits Vorfälle und kannst du sie belegen, steht deine Begründung auf festem Boden.'),
  kurz('Schreib Zweck und Abwägung auf, bevor die erste Kamera hängt.')),
 ('Was du filmen darfst und was nicht',
  p('Ins Bild gehört dein eigenes Gelände, zum Beispiel Zufahrt und Laderampe. Der öffentliche Gehweg bleibt draußen, das Nachbargrundstück ebenso. '
    'Ragen solche Flächen trotzdem in den Blickwinkel, werden sie geschwärzt. In Umkleiden und Toiletten haben Kameras nichts zu suchen, in Pausenräumen genauso wenig. '
    'Ton nimmst du grundsätzlich nicht auf.'),
  kurz('Gefilmt wird nur, was dir gehört. Der Ton bleibt aus.')),
 ('Das Hinweisschild ist Pflicht',
  p('Wer den überwachten Bereich betritt, muss die Kamera vorher erkennen können. Deshalb hängt das Schild gut sichtbar vor dem Kamerabereich. '
    'Darauf stehen neben dem Kamerasymbol der Verantwortliche mit Kontaktdaten und der Zweck der Überwachung. Ergänze Rechtsgrundlage und Speicherdauer '
    'und verweise auf die vollständigen Datenschutzinformationen. Ein Muster dafür stellt die Datenschutzkonferenz der Aufsichtsbehörden bereit.'),
  kurz('Das Schild muss man sehen, bevor man im Bild ist.')),
 ('Wie lange du Aufnahmen speichern darfst',
  p('So kurz wie möglich. Die Aufsichtsbehörden halten in der Regel 48 bis 72 Stunden für ausreichend, um einen Vorfall zu bemerken. Danach überschreibt der Rekorder die Aufnahmen automatisch. '
    'Ist tatsächlich etwas passiert, sicherst du den betroffenen Ausschnitt für Polizei und Versicherung. Alles andere wird wie gewohnt gelöscht.'),
  kurz('Gelöscht wird automatisch, gesichert wird nur der Vorfall.')),
 ('Mitarbeitende richtig einbinden',
  p('Eine Kamera darf Beschäftigte nicht dauerhaft bei der Arbeit beobachten. Lässt sich ein Arbeitsplatz im Bild nicht vermeiden, informierst du die Mitarbeitenden vor dem Start. '
    'Zur Leistungs- oder Verhaltenskontrolle darfst du die Aufnahmen nicht nutzen. Verdeckte Aufnahmen kommen nur in eng begrenzten Ausnahmefällen in Betracht, '
    'wenn ein konkreter Verdacht auf eine Straftat besteht. Einen solchen Schritt lässt du vorher rechtlich prüfen.'),
  kurz('Sag deinem Team offen, wo Kameras hängen, und spare Arbeitsplätze möglichst aus.')),
 ('Der Betriebsrat hat ein Mitbestimmungsrecht',
  p('Hat dein Betrieb einen Betriebsrat, muss er der Einführung zustimmen. Kameras sind technische Einrichtungen, die zur Überwachung von Beschäftigten geeignet sind (§ 87 Abs. 1 Nr. 6 BetrVG). '
    'Sinnvoll ist eine Betriebsvereinbarung. Sie hält fest, wo die Kameras hängen und wer die Aufnahmen ansehen darf.'),
  kurz('Erst stimmt der Betriebsrat zu, dann wird montiert.')),
 ('Dokumentation: Verzeichnis und Folgenabschätzung',
  p('Die Videoüberwachung gehört in dein Verzeichnis der Verarbeitungstätigkeiten. Filmst du systematisch und in großem Umfang öffentlich zugängliche Bereiche, brauchst du zusätzlich eine '
    'Datenschutz-Folgenabschätzung. Halte außerdem schriftlich fest, wer auf die Aufnahmen zugreifen darf. Hast du einen Datenschutzbeauftragten, hol ihn früh dazu.'),
  kurz('Was du filmst und wer es sehen darf, steht schwarz auf weiß in deinen Unterlagen.')),
 ('Technik, die Datenschutz leichter macht',
  p('Viele Datenschutzfragen beantwortet schon eine gut geplante Montage. Privatzonen schwärzen den Gehweg dauerhaft im Bild. Die Aufnahmen bleiben auf einem Rekorder in deinem Betrieb '
    'und verschwinden nach der festgelegten Frist von selbst. Genau so richten wir unsere <a href="/kamerasysteme/">Videoüberwachung für Unternehmen</a> ein.'),
  kurz('Datenschutz beginnt beim Kamerawinkel.')),
]
FAQ = [
 ('Darf ich mein Firmengelände per Kamera überwachen?',
  p('Ja, wenn du ein berechtigtes Interesse hast, etwa den Schutz vor Einbruch oder Diebstahl. Die Kamera muss dafür erforderlich sein, und die Rechte der Gefilmten dürfen nicht überwiegen. '
    'Außerdem brauchst du ein Hinweisschild und eine kurze Speicherdauer.')),
 ('Brauche ich ein Hinweisschild für die Videoüberwachung?',
  p('Ja. Das Schild muss sichtbar sein, bevor jemand den überwachten Bereich betritt. Es nennt den Verantwortlichen mit Kontaktdaten und den Zweck der Überwachung. '
    'Dazu kommen Rechtsgrundlage und Speicherdauer sowie ein Hinweis auf die vollständigen Datenschutzinformationen.')),
 ('Wie lange darf ich Videoaufnahmen speichern?',
  p('So kurz wie möglich. In der Regel halten die Aufsichtsbehörden 48 bis 72 Stunden für ausreichend. Aufnahmen eines konkreten Vorfalls darfst du zur Beweissicherung länger aufbewahren.')),
 ('Muss ich meine Mitarbeitenden über Kameras informieren?',
  p('Ja, und zwar bevor die Kameras in Betrieb gehen. Eine dauerhafte Überwachung am Arbeitsplatz ist unzulässig, eine Leistungskontrolle per Kamera ebenfalls.')),
 ('Muss der Betriebsrat der Videoüberwachung zustimmen?',
  p('Ja, sofern es einen gibt. Nach § 87 Abs. 1 Nr. 6 BetrVG bestimmt der Betriebsrat bei technischen Einrichtungen mit, die zur Überwachung von Beschäftigten geeignet sind. '
    'Geregelt wird das üblicherweise in einer Betriebsvereinbarung.')),
 ('Darf die Kamera den Gehweg oder das Nachbargrundstück zeigen?',
  p('Nein, soweit es sich vermeiden lässt. Moderne Kameras schwärzen solche Bereiche dauerhaft per Privatzone. Das richten wir bei der Montage gleich mit ein.')),
 ('Sind Kamera-Attrappen erlaubt?',
  p('Eine Attrappe verarbeitet keine Daten, datenschutzrechtlich ist sie deshalb unproblematisch. Sie kann aber Nachbarn oder Beschäftigte unter Überwachungsdruck setzen und so Streit auslösen. '
    'Im Ernstfall liefert sie außerdem kein einziges Bild.')),
 ('Ersetzt dieser Ratgeber eine Rechtsberatung?',
  p('Nein. Er gibt dir einen Überblick über die üblichen Anforderungen, Stand November 2026. Für deinen Einzelfall wendest du dich an deinen Datenschutzbeauftragten oder einen Anwalt.')),
]
SPEC = {
 'slug': 'videoueberwachung-firmengelaende', 'parent_slug': 'ratgeber', 'title': 'Videoüberwachung auf dem Firmengelände',
 'menu': 'menue-leistungsseiten', 'menu_footer': 'menue-leistungsseiten-footer',
 'verboten': VERBOTEN, 'erlaubt': ['im Landkreis Uelzen', '/uelzen/', '"name": "Uelzen"', 'Standorte:'],
 'seo': {'title': 'Videoüberwachung Firmengelände: Was ist erlaubt? (DSGVO)',
         'description': BESCHR, 'focuskw': 'Videoüberwachung Firmengelände', 'bctitle': 'Videoüberwachung Firmengelände', 'robots_noindex': '0'},
 'remove': REMOVE,
 'order': ORDER, 'handy_css': True,
 'graft': [cta('Kameras, die erlaubt sind und im Ernstfall helfen', 'Im Erstgespräch klären wir, welche Bereiche du überwachen darfst und wo die Kameras am meisten bringen.', nach='f1a5d3e'),
   video_kasten('Wir planen und installieren Kamerasysteme mit Alarm aufs Handy, von der Begehung bis zum Hinweisschild. Die Aufnahmen bleiben lokal in deinem Betrieb.'), PRESSE],
 'karten': KARTEN,
 'set': {
  **GRUENDER,
  '9dcea29': {'_title': 'H1', 'title': '<span style="font-weight: 700;">Videoüberwachung auf dem Firmengelände:</span><br>Was ist erlaubt?'},
  'e429076': {'_title': 'Hero-Text', 'title': 'Nachts wird das Lager aufgebrochen, am Morgen fehlen Werkzeug und Kabeltrommeln. Spätestens dann denken viele Betriebe über Videoüberwachung auf dem Firmengelände nach. '
              'Und sofort kommt die Frage, was rechtlich erlaubt ist. Dieser Leitfaden beantwortet sie Punkt für Punkt, vom Hinweisschild bis zum Betriebsrat.' + AUTOR_ZEILE},
  '34dc7fa': {'_title': 'Kurzfassung + Film'},
  'd05eab3': {'_title': 'Kurzfassung', 'title': 'Kurz gesagt: Ja, du darfst dein Firmengelände filmen, wenn du dich an klare Regeln hältst.'},
  '7df04ae': {'editor': p('Videoüberwachung auf dem Firmengelände ist erlaubt, wenn du ein berechtigtes Interesse hast, etwa den Schutz vor Einbruch. Die Kamera zeigt ausschließlich deine eigenen Flächen. '
              'Ein Hinweisschild macht vor dem Kamerabereich auf sie aufmerksam, und nach wenigen Tagen löschen sich die Aufnahmen. Deine Mitarbeitenden informierst du vorab; gibt es einen Betriebsrat, muss er zustimmen.')},
  'd38dec5': {'editor': p('Dieser Ratgeber gibt dir einen Überblick über die üblichen Anforderungen und ersetzt keine Rechtsberatung. Stand: November 2026.')},
  'd7f768f': {'_title': 'Artikel', '_element_id': 'artikel'},
  '74b6d54': {'_title': 'Artikel Überschrift', 'title': 'Acht Punkte, die du vor der ersten Kamera <span style="font-weight: 700; ">klären solltest</span>'},
  '43e5085': {'editor': p('Wer diese Punkte vor der Montage klärt, muss später nichts nachbessern, wenn die Aufsichtsbehörde oder der Betriebsrat nachfragt.')},
  'd70fb3d': {'_title': 'Checkliste', '_element_id': 'checkliste'},
  'c869af6': {'_title': 'Checkliste', 'title': 'Checkliste vor der Installation'},
  '8b353e8': {'title': 'Zweck und Abwägung sind aufgeschrieben, frühere Vorfälle belegt.'},
  '6519b8c': {'title': 'Kamerawinkel und Privatzonen sind geplant, die Hinweisschilder bestellt.'},
  '05ac70c': {'editor': p('Die Speicherdauer steht fest, und dein Team weiß Bescheid. Der Betriebsrat hat zugestimmt, falls es einen gibt, und die Kameras stehen im Verzeichnis der Verarbeitungstätigkeiten.')},
  'f1a5d3e': {'_title': 'Passend dazu', '_element_id': 'weiterlesen'},
  'cfa4bb1': {'_title': 'Passend dazu', 'title': 'Passend dazu'},
  '4967d0c': {'title': '<a href="/kamerasysteme/" style="color: #FBC91B;">Videoüberwachung für Unternehmen</a>: wie wir Kameras planen und datenschutzgerecht einrichten.'},
  '99ee72d': {'title': '<a href="/videoueberwachung-schlachthoefe/" style="color: #FBC91B;">Videoüberwachung für Schlachthöfe</a>: was die neue Kamerapflicht nach § 4d TierSchG verlangt.'},
  '8754a23': {'editor': p('<a href="/ratgeber/schluessel-verloren-unternehmen/">Schlüssel im Unternehmen verloren</a>: wer haftet und was jetzt zu tun ist.')},
  '51f3331': {'title': 'Kameras, die erlaubt sind <br><span style="font-weight: 700; ">und im Ernstfall helfen</span>'},
  '5c65e03': {'editor': p('Unsere Kameras filmen rechtlich sauber und liefern im Ernstfall trotzdem Bilder, mit denen Polizei und Versicherung arbeiten können. Dafür nehmen wir uns bei der Begehung Zeit und wählen jeden Kamerawinkel mit Bedacht. '
              'Wir sind in ganz Norddeutschland unterwegs; alle Orte findest du in der <a href="/standorte/">Übersicht unserer Standorte</a>.') + NAP},
  '7983242': {'title': 'Häufige Fragen zur <b>Videoüberwachung im Unternehmen</b>'},
  '45eaf1f': {'title': 'Häufige Fragen zur <br><b>Videoüberwachung im Unternehmen</b>'},
 },
 'faq': FAQ,
 'schema': artikel_schema(URL, TITEL, BESCHR),
}
