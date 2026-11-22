"""Gemeinsame Bausteine aller neuen Seiten (Kontaktblock, Organisation im Schema, Wortlisten)."""
BASE = 'https://provision-infra.de'
NAP = ('<p><strong>ProVision Infra GmbH</strong><br>Klein Hesebecker Straße 11, 29549 Bad Bevensen<br>'
       'Telefon: <a href="tel:+4958214049040">05821 4049040</a><br>'
       'E-Mail: <a href="mailto:info@provision-infra.de">info@provision-infra.de</a><br>Montag bis Donnerstag 9 bis 18 Uhr, Freitag 9 bis 14 Uhr</p>')
ORTE_NORD = ['Lüneburg', 'Uelzen', 'Bad Bevensen', 'Celle', 'Winsen (Luhe)', 'Dannenberg (Elbe)', 'Hitzacker (Elbe)', 'Bleckede',
             'Lüchow (Wendland)', 'Gifhorn', 'Wittingen', 'Ebstorf', 'Bienenbüttel', 'Wieren', 'Bad Bodenteich', 'Munster', 'Soltau',
             'Hamburg', 'Hannover']
ORG = {
    "@type": "LocalBusiness", "@id": BASE + "/#organization", "name": "ProVision Infra GmbH", "url": BASE + "/",
    "logo": BASE + "/wp-content/uploads/2026/10/kamera-logo-provision-infra-1032.png",
    "image": BASE + "/wp-content/uploads/2026/11/header-foto-1305-q92.webp",
    "telephone": "+49 5821 4049040", "email": "info@provision-infra.de", "priceRange": "$$",
    "address": {"@type": "PostalAddress", "streetAddress": "Klein Hesebecker Straße 11", "postalCode": "29549",
                "addressLocality": "Bad Bevensen", "addressRegion": "Niedersachsen", "addressCountry": "DE"},
    "geo": {"@type": "GeoCoordinates", "latitude": 53.0779485, "longitude": 10.5903962},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"], "opens": "09:00", "closes": "18:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "09:00", "closes": "14:00"}],
    "areaServed": [{"@type": "City", "name": o} for o in ORTE_NORD] + [{"@type": "State", "name": "Niedersachsen"}],
    "sameAs": ["https://www.instagram.com/provision_infra_gmbh/", "https://www.facebook.com/share/1CWs2rohMt/",
               "https://www.linkedin.com/company/provision-infra-gmbh-i-g/"]}
# Wörter der Uelzen-Vorlage, die auf überregionalen Seiten nicht stehen bleiben dürfen
VERBOTEN = ['Uelzen', 'Uelzener', 'Veerßen', 'Oldenstadt', 'Holdenstedt', 'B4', 'Suderburg', 'Rosche', 'Himbergen', 'Altenmedingen']

# Reihenfolge der Hauptabschnitte nach dem Vorbild der Startseite (fehlende IDs werden übersprungen)
ORDER = ['192a273', '0f0c707', 'd135e80', '67b8213', '34dc7fa', '7cfc047c', 'd7f768f', '00fec0c', 'af8c629', '1a6dd74',
         'd70fb3d', '25be186', 'f1a5d3e', '7cf6d53', '916606a', 'a3437e1', '713bf22', 'b3e009b', 'a4e4757', 'bec6cfd',
         '88956c0', '55b8573', 'b0720cd', '9fafb57']

# Gründertext ohne Gedankenstriche und ohne Aufzählungsketten, mit Namen
GRUENDER = {
 'e04b70a': {'editor': '<p>Jannes Heino Baumann kommt aus der Praxis. Gelernt hat er Elektriker, später kam die Ausbildung zum IT-Systemkaufmann dazu. '
             'Danach fuhr er als Berufsfeuerwehrmann in Hamburg Einsätze, und auch im militärischen Sicherheitsumfeld hat er gearbeitet.</p>'
             '<p>Bei der Feuerwehr öffnet man verschlossene Türen, wenn jede Minute zählt. Aus diesem Handwerk wurde sein erstes eigenes Unternehmen: ein Schlüsseldienst.</p>'},
 'a1d3e7d': {'editor': '<p>Dort sah er jeden Tag, wie Betriebe mit ihren Schlüsseln umgehen. Sie gehen von Hand zu Hand. Hin und wieder lässt jemand heimlich einen nachmachen. '
             'Teuer wird das an dem Tag, an dem einer fehlt.</p>'
             '<p>Immer mehr Kunden fragten ihn deshalb nach einer digitalen Lösung. Sie wollten auf einen Blick sehen, wer in welchen Raum darf. Übergabetermine und Nachschlüssel wollten sie sich sparen.</p>'},
}

# Presse-Kasten: Klon des Kastens „Videoüberwachung aus einer Hand“ (b3e009b) mit neuen IDs, hinter dem Zitat bec6cfd
PRESSE_LINKS = {
 'interview': 'https://arbeitgebermagazin.de/provision-infra-gruender-im-interview-zutrittskontrolle-ist-keine-hausmeisterarbeit',
 'unternehmerjournal': 'https://www.unternehmerjournal.de/erfahrungen-mit-provision-infra-wie-dieser-anbieter-fuer-schliessanlagen-seinen-kunden-bares-geld-spart/',
 'gewinnermagazin': 'https://gewinnermagazin.de/erfahrungen-mit-provision-infra-wie-unternehmen-mit-einer-digitalen-schliessanlage-fuenfstellige-kosten-vermeiden/',
}
def _ext(url): return {'url': url, 'is_external': 'on', 'nofollow': '', 'custom_attributes': ''}
PRESSE = ('b3e009b', 'bec6cfd', {
  'b3e009b': {'_title': 'Presse', '_element_id': 'presse'},
  '30deaeb': {'title': 'ProVision Infra in der Presse'},
  '018167f': {'editor': '<p>Im Interview mit dem <a href="' + PRESSE_LINKS['interview'] + '" target="_blank" rel="noopener">Arbeitgebermagazin</a> erklärt Gründer Jannes Heino Baumann, '
              'warum Zutrittskontrolle Chefsache ist. Wie unsere Kunden mit einer digitalen Schließanlage teure Schlüsselverluste vermeiden, haben das '
              '<a href="' + PRESSE_LINKS['unternehmerjournal'] + '" target="_blank" rel="noopener">Unternehmerjournal</a> und das '
              '<a href="' + PRESSE_LINKS['gewinnermagazin'] + '" target="_blank" rel="noopener">GEWINNERmagazin</a> aufgeschrieben.</p>'},
  'c9c0f01': {'text': 'Zum Interview', 'link': _ext(PRESSE_LINKS['interview'])},
 }, True)

def video_kasten(text):
    """Kasten „Videoüberwachung aus einer Hand“ (b3e009b) hinter dem CTA 713bf22."""
    return ('b3e009b', '713bf22', {'018167f': {'editor': '<p>' + text + '</p>'}})

def cta(titel, text, nach='a3437e1'):
    """Abschluss-Aufruf der Startseite (713bf22) hinter dem Ablauf a3437e1 bzw. einem anderen Abschnitt."""
    return ('713bf22', nach, {'cba15a6': {'title': titel}, '4e4df2b': {'editor': '<p>' + text + '</p>'}})

STELL_D = ['0a26d69', '592b9e8', '16319c7', 'e6004c2', '7f574bc', '172d8ab', '3d7b08d', 'dd3436a']
STELL_M = ['196a01d', '95203a8', 'b640c54', 'b7ef4bd', '8f999b2', 'ba5311c', 'c325747', '13ec65b']
def stell_dir_vor(texte, nach='d7f768f'):
    """„Stell dir mal vor …“: Überschrift 00fec0c, Türgriff-Komposition (af8c629, Computer) und Handy-Variante (1a6dd74). texte: 8 Sätze."""
    assert len(texte) == 8
    d, m = {}, {}
    for i, t in enumerate(texte):
        key_d = 'title' if STELL_D[i] in ('7f574bc', '3d7b08d') else 'editor'
        key_m = 'title' if STELL_M[i] in ('8f999b2', 'c325747') else 'editor'
        d[STELL_D[i]] = {key_d: t if key_d == 'title' else '<p>' + t + '</p>'}
        m[STELL_M[i]] = {key_m: t if key_m == 'title' else '<p>' + t + '</p>'}
    # Reihenfolge der Einfügung: 00fec0c hinter nach, af8c629 hinter 00fec0c, 1a6dd74 hinter af8c629
    return [('00fec0c', nach, {}), ('af8c629', '00fec0c', d), ('1a6dd74', 'af8c629', m)]

VORTEIL_PAARE = [  # (Überschrift Computer, Überschrift Handy, Text Computer, Text Handy, Text ist Überschrift-Widget)
 ('2555e77', '53df6ca', '1612902', '32646b1', False), ('81a0a3c', '86545bf', '785bb33', '387ed5d', False),
 ('4bb5f6f', '0187c11', '6c90f27', '3473792', False), ('b362dc2', '629de19', 'e24ac9d', '312cf79', False),
 ('b36cabe', '3c50e91', 'e060d48', '878d455', True), ('a72840a', '4b04469', '7ef2742', '1e230d2', False),
 ('f359da5', 'ff9a5e8', 'b5100a8', '9acd9ed', False), ('af8e9bc', '5811b59', '4b62b72', 'f7136e5', False),
 ('cb7293a', 'c4e5d54', '4b64e18', 'f97a0a2', True)]
def vorteile(paare, nach='f1a5d3e'):
    """„Das heißt für dich:“ (7cf6d53 Computer, 916606a Handy). paare: 9 × (Überschrift mit Doppelpunkt, Text)."""
    assert len(paare) == 9
    d, m = {}, {}
    for (hd, hm, td, tm, th), (h, t) in zip(VORTEIL_PAARE, paare):
        d[hd] = {'title': h}; m[hm] = {'title': h}
        d[td] = {'title': t} if th else {'editor': '<p>' + t + '</p>'}
        m[tm] = {'title': t} if th else {'editor': '<p>' + t + '</p>'}
    return [('7cf6d53', nach, d), ('916606a', '7cf6d53', m)]

def analyse(intro, fragen, schluss, nach='d70fb3d'):
    """Abschnitt „Wer braucht wann Zugang?“ (25be186): Einleitung, drei Fragen mit Symbol, Schlusssatz."""
    a, b, c = fragen
    return ('25be186', nach, {'5eb986c': {'editor': '<p>' + intro + '</p>'}, '38a8d1e': {'title': a}, '12b578c': {'title': b},
                              '8b4bb3b': {'title': c}, '280fbda': {'editor': '<p>' + schluss + '</p>'}})

# Slider „Technik, die wir verbauen“: Klon des Kundenstimmen-Karussells (7cfc047c / 2b91cf92) mit Produktkarten.
# Medien-IDs und URLs stehen in technik-medien.json (nach dem Upload erzeugt).
TECHNIK = [
 ('evva-4ks-mechanischer-zylinder', 'EVVA 4KS',
  'Bewährter mechanischer Zylinder für Schließanlagen mit Schließplan. Nachschlüssel gibt es nur gegen Sicherungskarte.',
  'EVVA 4KS mechanischer Schließzylinder im Schnitt mit Schlüssel'),
 ('evva-akura-44-mechanischer-zylinder', 'EVVA AKURA 44',
  'Die neuere mechanische Generation von EVVA, ebenfalls mit geschütztem Schlüsselprofil.',
  'EVVA AKURA 44 mechanischer Schließzylinder im Schnitt mit Schlüssel'),
 ('evva-elektronischer-knaufzylinder', 'Elektronischer Zylinder von EVVA',
  'Passt in die vorhandene Tür und öffnet mit Transponder oder Smartphone.',
  'Elektronischer Knaufzylinder von EVVA in Messing'),
 ('evva-xesar-komponenten', 'EVVA Xesar',
  'Beschläge und Zylinder aus einem System, verwaltet in einer gemeinsamen Software.',
  'EVVA Xesar Beschläge, Wandleser und elektronischer Zylinder'),
 ('evva-wandleser-steuereinheit', 'EVVA Wandleser mit Steuereinheit',
  'Steuert Tore und elektrische Türöffner. Die Steuereinheit sitzt geschützt auf der Innenseite.',
  'EVVA Wandleser und offene Steuereinheit'),
 ('simonsvoss-digitalzylinder-ax', 'SimonsVoss Digitalzylinder AX',
  'Wird kabellos montiert und öffnet per Transponder oder Smartphone.',
  'SimonsVoss Digitalzylinder AX'),
 ('simonsvoss-smarthandle-ax-tuer', 'SimonsVoss SmartHandle AX',
  'Der elektronische Beschlag ersetzt den alten Türdrücker, ganz ohne Kabel.',
  'SimonsVoss SmartHandle AX an einer Holztür'),
 ('simonsvoss-smarthandle-ax-langschild', 'SimonsVoss SmartHandle mit Langschild',
  'Dieselbe Idee in der Ausführung mit langem Schild, passend für viele Bürotüren.',
  'SimonsVoss SmartHandle mit Langschild'),
 ('keyota-knaufzylinder', 'Keyota Smart-Zylinder',
  'Öffnet per App. Die Bridge funkt über Mobilfunk und braucht kein WLAN vor Ort.',
  'Keyota elektronischer Knaufzylinder'),
 ('evva-certified-partner', 'Zertifizierter EVVA Partner',
  'Für elektronische Schließsysteme von EVVA sind wir offiziell zertifiziert.',
  'EVVA Certified Partner für elektronische Schließsysteme'),
]
def technik(nach='1a6dd74'):
    import json, os
    med = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'technik-medien.json'), encoding='utf-8'))
    return {'nach': nach, 'titel': 'Technik, <span style="font-weight: 700; ">die wir verbauen</span>',
            'karten': [(med[n]['id'], med[n]['url'], name, text, alt) for n, name, text, alt in TECHNIK]}
