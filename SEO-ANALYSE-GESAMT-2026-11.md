# SEO-Analyse provision-infra.de – alle Seiten und Unterseiten (Stand 17.11.2026)

Ziel laut Auftrag: ProVision Infra soll bei Google der relevanteste Anbieter für Schließanlagen, Zutrittskontrolle und
Videoüberwachung werden und in Lüneburg, Winsen (Luhe), Uelzen, Dannenberg, Celle, Hitzacker, Bleckede, Munster sowie
im gesamten Gebiet dazwischen und darüber hinaus ganz oben ranken.

Dieser Bericht ist eine reine Analyse mit Empfehlungen. An WordPress wurde nichts verändert.

## 0. Das Wichtigste in Kürze

**Stärken (bereits vorhanden):**

- Technische Basis sauber: HTTPS, www- und http-Varianten leiten per 301 um, Yoast-Sitemap mit 23 URLs, robots.txt offen,
  Canonicals korrekt, alle Inhaltsseiten `index, follow`, Funnel-Seiten `noindex`.
- Alle 23 indexierbaren Seiten haben individuelle Titel (55–63 Zeichen), Descriptions (144–160 Zeichen) und genau eine H1.
- 15 lokale Landingpages mit je 2.000–2.300 Wörtern, FAQ-Schema und LocalBusiness-Daten (Lüneburg, Uelzen, Bad Bevensen,
  Celle, Winsen, Dannenberg, Hitzacker, Bleckede, Gifhorn, Lüchow, Wittingen, Ebstorf, Bienenbüttel, Wieren, Bad Bodenteich).
- Sehr starke Bewertungsbasis: 105 Google-Rezensionen (5,0) über zwei Google-Einträge plus ProvenExpert 4,99 (31 Bewertungen).
- Der Wettbewerb in der Zielregion hat fast keine spezialisierten Seiten zu „Schließanlage/Zutrittskontrolle + Stadt“; dort
  ranken Schlüsseldienste, Elektrobetriebe und Branchenverzeichnisse.

**Die größten Bremsen (nach Wirkung sortiert):**

1. **Interne Verlinkung und Navigation:** Das Hauptmenü besteht nur aus Sprungankern (#digitalen, #arbeiten, #Über, #FAQ) plus
   Karriere. Weder /kamerasysteme/ noch /zutrittssystem/ noch eine einzige Stadtseite ist aus Menü oder Startseiten-Text verlinkt.
   /lueneburg/ und /uelzen/ erhalten Links ausschließlich von den anderen Stadtseiten. /videoueberwachung-schlachthoefe/ ist
   praktisch verwaist (einziger Link: die eigene Umlaut-Weiterleitungsseite).
2. **Stadtseiten sind zu ~80 % Textbausteine:** Nur 10–15 % der Fünf-Wort-Folgen einer Stadtseite kommen auf keiner anderen
   Stadtseite vor (ohne den Ortsnamen gerechnet). H1, Titelmuster, Abschnittsfolge und FAQ sind bis auf den Ortsnamen identisch.
   Das ist das Muster, das Google als „Doorway Pages“ einstuft, und es verhindert, dass die Seiten in ihrer Stadt als die
   relevanteste Antwort gelten.
3. **Keine sichtbaren Kontaktdaten auf den drei Hauptseiten:** Startseite, /kamerasysteme/ und /zutrittssystem/ zeigen weder
   Telefonnummer, Adresse, E-Mail noch Öffnungszeiten im sichtbaren Text (nur im Schema-Code). Für Local SEO (NAP-Konsistenz),
   Vertrauen und Conversion ist das eine Lücke.
4. **Ladezeit mobil:** Lighthouse-Performance 48–64 von 100, LCP 3,4–16,4 s. Hauptursachen: PNG-Grafiken statt WebP
   (bis 960 KB Einsparung je Seite), zwei unkomprimierte Hero-Videos auf /zutrittssystem/ (6,2 + 3,7 MB), Google Tag Manager
   + Facebook-Pixel (530 KB, 640–790 ms Blockierzeit), render-blockierende CSS/JS, nicht entferntes BugHerd-Skript (Fehler in
   der Konsole), DOM mit 1.300–1.550 Elementen.
5. **Strukturierte Daten uneinheitlich und riskant:** Dasselbe `@id` `#organization` wird je Seite als `LocalBusiness`,
   `["LocalBusiness","Locksmith"]` oder `Organization` deklariert, mit unterschiedlichen `areaServed`, Logos und Geo-Daten.
   Das ProvenExpert-Widget liefert auf 7 Seiten ein `Product`-Schema „ProVision Infra“ mit AggregateRating 5,0/136 – das ist
   eine Eigenbewertung, die Googles Richtlinien für Bewertungs-Rich-Results verletzt (Risiko: manuelle Maßnahme „Spam durch
   strukturierte Daten“). Yoast hat keine Organisation hinterlegt (`publisher` leer); /karriere/ enthält doppelte
   WebSite-/WebPage-Knoten.
6. **Google-Unternehmensprofil mit zwei Einträgen** (81 und 24 Rezensionen). Wenn das ein Duplikat ist, splittet es Bewertungen
   und Rankingsignale; wenn es zwei Standorte sind, fehlt die Ausspielung auf der Website. Außerdem: Branchenbuch-Eintrag
   (ortsdienst.de) unter „Wachschutz/Personenschutz“ ohne Telefon und Website.
7. **Fehlende Themen mit nachweisbarer Nachfrage:** „Sicherheitstechnik <Stadt>“ (Lüneburg, Winsen, Uelzen, Celle, Gifhorn,
   Soltau) wird gesucht, die Website nutzt den Begriff kaum. „Alarmanlage Lüneburg/Celle“ wird gesucht, es gibt kein Angebot
   dazu. Munster hat keine Seite. Es gibt keinen Ratgeber-Bereich für Fragen wie „Schlüssel verloren Firma wer haftet“,
   „Videoüberwachung Firmengelände DSGVO Muster/Schild/Betriebsrat“, „digitale Schließanlage Kosten“, „Schließanlage austauschen
   Kosten“ – alles Suchanfragen, die Google in der Vervollständigung zeigt.

**Top-10-Maßnahmen** (Details und Reihenfolge in Kapitel 8):

| # | Maßnahme | Wirkung | Aufwand |
|---|---|---|---|
| 1 | Hauptmenü auf echte Seiten umbauen: Leistungen (Schließanlagen, Zutrittskontrolle, Videoüberwachung, Branche Schlachthöfe), Standorte (alle Stadtseiten), Über uns, Referenzen, Karriere, Kontakt | sehr hoch | gering |
| 2 | Footer auf allen Seiten mit NAP-Block (Firma, Adresse, Telefon als `tel:`-Link, E-Mail, Öffnungszeiten) und Standortliste | hoch | gering |
| 3 | Startseite: Abschnitt „Unsere Region“ mit Textlinks auf alle Stadtseiten; /kamerasysteme/ verlinkt die Schlachthof-Seite | hoch | gering |
| 4 | Google-Unternehmensprofil bereinigen (Duplikat prüfen/zusammenführen, Kategorien, Leistungen, Einzugsgebiet, Beiträge, Fotos) | sehr hoch | gering |
| 5 | Schema konsolidieren: eine LocalBusiness-Definition site-weit, ProvenExpert-Produkt-Schema abschalten, Yoast-Organisation setzen | mittel, senkt Risiko | gering |
| 6 | Stadtseiten individualisieren (Ziel: >40 % einzigartiger Text): lokale Referenzen, Anfahrt/Reaktionszeit, Branchenstruktur, eigene FAQ, Fotos; Munster-Seite ergänzen | sehr hoch | hoch |
| 7 | Performance: PNG → WebP, Hero-Videos /zutrittssystem/ auf ≤1 MB, BugHerd entfernen, GTM/Pixel verzögern, Render-Blocking beseitigen | mittel | mittel |
| 8 | Ratgeber-Bereich mit 8–12 Artikeln zu den gefundenen Fragen, intern auf Leistungs- und Stadtseiten verlinkt | hoch (mittelfristig) | hoch |
| 9 | Umlaut-URLs per 301 statt Meta-Refresh-Seite; Großschreibungs-Varianten per 301 | gering | gering |
| 10 | Off-Page: Branchenbuch-Einträge korrigieren/ergänzen, Hersteller-Partnerverzeichnisse (SimonsVoss, EVVA, TP-Link VIGI, Nuki), regionale Presse, Verbände; GitHub-Repos privat stellen | hoch (laufend) | mittel |

## 1. Datenbasis und Methode

- Crawl aller 23 Sitemap-URLs plus 10 bekannter Funnel-/Sonder-URLs am 16./17.11.2026 (HTML + Header, 22 s Abstand wegen
  Rate-Limit des Hosters). Auswertung: Status, Canonical, Robots, Titel, Description, Überschriften, Wortzahl, Bilder/Alt-Texte,
  interne und externe Links, Schema-Knoten, Ortsnennungen, Textähnlichkeit (Jaccard auf Fünf-Wort-Folgen).
- Weiterleitungs- und Header-Tests (http/https, www, Groß-/Kleinschreibung, Trailing Slash, Umlaut-URLs, 404, Feed, Suche,
  REST-API, Sitemap-Aliasse, Cache-Header).
- Lighthouse 12.8 (mobil, simulierte Drosselung) für Startseite, /lueneburg/, /kamerasysteme/, /zutrittssystem/, /celle/.
- Google-Suggest-Vervollständigungen (de/DE) für 96 Kombinationen Ort × Begriff, 30 informationelle Long-Tails, Markenbegriffe.
- Externe Signale: ProvenExpert-Profil, Branchenbuch ortsdienst.de, gefundene Backlinks (keyrent.de, gewinnermagazin.de,
  unternehmerjournal.de), Wettbewerber-Recherche je Stadt.
- Rohdaten im Ordner `seo-analyse/` dieses Repos.

**Nicht möglich in dieser Analyse:** Search-Console-Leistungsdaten (benötigt Login mit 2FA), echte Google-Rankings
(automatisierte SERP-Abfragen wurden vom System blockiert; DuckDuckGo/Bing lieferten keine verwertbaren Ergebnisse),
Chrome-UX-Felddaten (PageSpeed-API-Kontingent erschöpft), Backlink-Datenbank, Google-Unternehmensprofil-Statistiken.
Diese vier Quellen sollten vor der Umsetzung einmal gezogen werden (Kapitel 9).

## 2. Indexierung und Technik

| Prüfpunkt | Befund | Bewertung |
|---|---|---|
| robots.txt | `User-agent: *` / `Disallow:` (leer) + Sitemap-Verweis | gut |
| Sitemap | `sitemap_index.xml` → `page-sitemap.xml`, 23 URLs, lastmod 21× 13.11.2026; `/sitemap.xml` und `/wp-sitemap.xml` leiten um | gut |
| http → https, www → ohne www | 301 (zwei Hops bei `http://www.`: erst https://www, dann ohne www) | gut, ein Hop wäre sauberer |
| Trailing Slash, `/index.php`, `/?p=ID` | 301 auf die saubere URL | gut |
| Groß-/Kleinschreibung (`/Lueneburg/`) | 200, keine Weiterleitung (Canonical zeigt auf die Kleinschreibung) | kleines Duplikat-Risiko, 301 empfohlen |
| Umlaut-URLs (`/videoüberwachung-schlachthöfe/`) | eigene WordPress-Seiten (4891/4893/4894) mit `noindex, nofollow`, Meta-Refresh 0 s und JS `location.replace` | funktioniert, aber gibt keine Linkkraft weiter; serverseitige 301 empfohlen |
| 404-Verhalten | unbekannte URL → HTTP 404 mit Standard-Seite „Page not found“ (Hello Elementor, 26 Wörter, kein Menü-Inhalt) | 404-Seite gestalten (Suche, Links auf Leistungen/Standorte) |
| `/feed/`, `/?s=` | 200, Feed indexierbar, Suchergebnisse ohne noindex geprüft? (Yoast setzt für Suche standardmäßig noindex) | niedrig |
| REST-API `/wp-json/wp/v2/pages` | öffentlich (WordPress-Standard) | normal |
| Cache | Varnish HIT, `age` bis 3,6 Tage auf /lueneburg/; `cache-control: max-age=0` für Browser | Inhalte erscheinen für Google erst nach Cache-Leerung; nach Änderungen immer Cache leeren |
| HTML-Größe | 430–600 KB unkomprimiert je Landingpage (Elementor-Inline-CSS, Schema, Lottie); komprimiert 100–153 KB | hoch, siehe Performance |
| Sprache/hreflang | `lang="de"`, keine Alternativen | passt |
| Noindex-Seiten | /kontakt/, /termin/, /anfrage-auswahl/, /kontakt-kombiniert/, /kontakt-kamerasysteme/, /termin-kamerasysteme/, /danke/ und die drei Umlaut-Seiten | richtig; `nofollow` auf /kontakt/, /termin/ ist unnötig |

## 3. Seitenstruktur und interne Verlinkung

**Hauptmenü („Main“)**: „Mit digitalen Schlüsseln Kosten sparen“ (#digitalen), „So arbeiten wir zusammen“ (#arbeiten),
„Mehr“ → „Über uns“ (#Über), „FAQ“ (#FAQ), „Komm in unser Team“ (/karriere/). Das Menü enthält also **keine** Leistungsseite
und **keine** Standortseite. Google bewertet Seiten, die aus der Hauptnavigation verlinkt sind, als wichtiger; Nutzer finden
die Leistungen nur über den Footer.

**Footer**: /kamerasysteme/, /zutrittssystem/, /kontakt/, /karriere/, AGB, Datenschutz, Impressum, Facebook, LinkedIn,
ProvenExpert. Kein Standort, keine Adresse, keine Telefonnummer.

**Eingehende interne Links je Seite (ohne Sitemap):**

| Seite | eingehende Links | Quellen | Ankertexte |
|---|---|---|---|
| / | 25 | alle Seiten (Logo, Footer) | Logo (leer), „digitalen Schließanlagen“, „Zur Startseite“ |
| /zutrittssystem/ | 18 | Startseite, Karriere, alle Stadtseiten | „digitalen Zutrittssystem“, „Zutrittssystem“ |
| /kamerasysteme/ | 19 | Startseite, Karriere, Zutrittssystem, Stadtseiten | „Kamera- und Videoüberwachung für Unternehmen“ |
| /lueneburg/ | 14 | **nur** die 14 anderen Stadtseiten | „Lüneburg“ |
| /uelzen/ | 14 | **nur** die 14 anderen Stadtseiten | „Uelzen“ |
| 13 Stadtseiten | je 12 | **nur** die anderen Stadtseiten | Ortsname |
| /videoueberwachung-schlachthoefe/ | 1 | nur die eigene Umlaut-Weiterleitungsseite | „Videoüberwachung für Schlachthöfe“ |
| /karriere/ | 4 | Menü | „Komm in unser Team“ |

Folgen: Die Stadtseiten hängen als geschlossener Ring unter sich, ohne Zufluss von der Startseite oder den Leistungsseiten.
Die Schlachthof-Seite muss Google über die Sitemap finden und erhält keine interne Relevanz. Die Ankertexte der Stadtseiten
bestehen nur aus dem Ortsnamen; „Schließanlagen Lüneburg“ oder „Videoüberwachung Celle“ kommt als Linktext nirgends vor.

**Ausgehende Links der Startseite** auf nur 8 verschiedene interne Ziele (Karriere, Zutrittssystem, Kamerasysteme, Kontakt,
AGB, Datenschutz, Impressum, Startseite). Externe Links: Facebook, LinkedIn, ProvenExpert.

## 4. On-Page je Seite

| Seite | Titel (Zeichen) | Description | H1 | Wörter | Bilder ohne Alt | FAQ |
|---|---|---|---|---|---|---|
| / | Digitale Schließanlage für Unternehmen \| ProVision Infra (56) | 150 | Wir installieren in deinem Unternehmen ein digitales Schließsystem | 2.406 | 10/47 (Deko-Linien, SVG) | 10 |
| /zutrittssystem/ | Elektronische Schließanlage mit Service \| ProVision Infra (57) | 144 | Wir betreuen deine elektronische Schließanlage … | **913** | **16/29** (Icons 72×72) | 6 |
| /kamerasysteme/ | Kamera- & Videoüberwachung für Unternehmen \| ProVision Infra (60) | 155 | Wir schützen dein Unternehmen mit Kamera- & Videoüberwachung | 1.892 | 7/27 | 11 |
| /videoueberwachung-schlachthoefe/ | Videoüberwachung Schlachthof: Kamerapflicht § 4d TierSchG (57) | 160 | Videoüberwachung für Schlachthöfe nach § 4d Tierschutzgesetz | 2.053 | 7/27 | 17 |
| /lueneburg/ | Schließanlagen & Videoüberwachung Lüneburg \| ProVision Infra (60) | 158 | Mechanische & elektronische Schließanlagen sowie Videoüberwachung in Lüneburg | 1.920 | 7/26 | 10 |
| /uelzen/ | … Uelzen \| ProVision Infra (58) | 153 | … in Uelzen | 2.195 | 7/26 | 11 |
| 13 Stadtseiten | „Schließanlagen & Videoüberwachung <Stadt> \| ProVision Infra“ (55–60) | 146–158 | „Mechanische & elektronische Schließanlagen sowie Videoüberwachung in <Stadt>“ | 2.061–2.175 | 7/26 | 10 |
| /karriere/ | Karriere bei ProVision Infra: Jobs in Bad Bevensen (50) | 152 | Komm ins Team … | 1.663 | 0/7 | 8 |
| /impressum/, /datenschutz/, /agb/ | kurz, ohne Description | – | ja | 181 / 5.381 / 3.812 | – | – |

Beobachtungen:

- **Titel folgen einem Muster** „Leistung + Ort | Marke“. Das ist korrekt, aber auf 15 Stadtseiten identisch aufgebaut. Der
  Begriff „Sicherheitstechnik“, der laut Google-Suggest in Lüneburg, Winsen, Uelzen, Celle, Gifhorn und Soltau aktiv gesucht
  wird, fehlt in allen Titeln und H1.
- **/zutrittssystem/ ist die dünnste Leistungsseite** (913 Wörter) und trägt einen Service-Titel („… mit Service“), obwohl sie
  das Kernprodukt „elektronische Schließanlage“ abdeckt. Zwischen Startseite (digitale Schließanlage) und /zutrittssystem/
  (elektronische Schließanlage) gibt es keine klare Keyword-Trennung; beide zielen auf dasselbe Thema.
- **Startseite ohne Ort im Titel/H1.** „zwischen Hamburg und Hannover“ steht nur in der Description. Für die lokale Relevanz
  der wichtigsten Seite fehlt ein Bezug zu Region oder Firmensitz im sichtbaren Kopfbereich.
- **Alt-Texte:** Deko-Linien und Icons ohne Alt sind unkritisch, auf /zutrittssystem/ fehlen aber bei 16 von 29 Bildern Alt-
  Attribute, darunter die Paket-Icons. Leere `alt=""` für reine Dekoration wäre korrekt; fehlende Attribute sind ein
  Accessibility-Mangel.
- **Heading-Hierarchie:** Lighthouse meldet auf der Startseite „heading-order“ (Sprünge in der Überschriftenebene). Die
  doppelten H2 „Der Gründer von ProVision Infra“ und „Häufige Fragen …“ auf jeder Landingpage stammen aus Desktop-/Mobil-
  Varianten derselben Abschnitte.
- **Kontaktdaten sichtbar:** Stadtseiten, Karriere, Schlachthof-Seite: ja (Telefon als `tel:`-Link, Adresse, E-Mail,
  Öffnungszeiten). Startseite, /kamerasysteme/, /zutrittssystem/: **nein**.

## 5. Lokale Landingpages (15 Stadtseiten)

**Anteil seitenspezifischer Textbausteine** (Fünf-Wort-Folgen, die auf keiner anderen Stadtseite vorkommen):

| Seite | Wörter | einzigartig | davon ohne Ortsnamen |
|---|---|---|---|
| /uelzen/ | 2.273 | 25 % | 25 % |
| /lueneburg/ | 1.977 | 23 % | 15 % |
| /bad-bevensen/ | 2.234 | 21 % | 15 % |
| /winsen-luhe/ | 2.270 | 22 % | 14 % |
| /celle/ | 2.246 | 21 % | 12 % |
| /hitzacker/, /wieren/ | 2.149 / 2.211 | 20 % | 13 % |
| /bienenbuettel/, /ebstorf/, /gifhorn/, /luechow/ | ~2.190 | 19 % | 11–12 % |
| /bleckede/, /dannenberg/, /wittingen/, /bad-bodenteich/ | ~2.200 | 17–18 % | 10 % |

Was identisch ist: Titelmuster, H1-Muster, alle 18 H2 (nur Ortsname getauscht), Reihenfolge der Abschnitte, Kundenstimmen
(Studio Lüüd, Digitale Hanseaten, …), Gründer-Block, Ablauf, Partner-Logos, Hero-Video, FAQ-Fragen 1–2 und 4–10 (nur Ortsname
getauscht), das Standort-Linkverzeichnis.

Was lokal ist: Einleitungssatz mit Entfernung zum Firmensitz („Celle … rund 70 Kilometer nördlich“), ein Absatz
„ProVision Infra in <Stadt> und im Landkreis“, Branchenbeispiele mit Ortsbezug („Kanzleien, Praxen und Hausverwaltungen in
Celle“), die Description.

Bewertung: Die Seiten sind inhaltlich solide und besser als die meisten Wettbewerber in diesen Städten (die keine solchen
Seiten haben). Aber sie sind untereinander so ähnlich, dass Google sie als Varianten einer Vorlage erkennt. Aus Googles
Spam-Richtlinien („Doorways“: Seiten für mehrere Orte mit weitgehend gleichem Inhalt) folgt kein automatischer Ausschluss,
aber eine Kanibalisierung: Google wählt für Suchanfragen in der Region eine der 15 Seiten, nicht zwingend die passende, und
keine der Seiten gilt als die beste Antwort für ihre Stadt.

**Fehlende Orte** aus dem Auftrag: **Munster** (keine Seite). Weitere Orte mit nachweisbarer Nachfrage und ohne Seite:
Soltau („sicherheitstechnik soltau“), Buchholz in der Nordheide (steht im Schema `areaServed`), Hamburg („schließanlage
hamburg“, „zutrittskontrolle hamburg“, „videoüberwachung hamburg“, „sicherheitstechnik hamburg“ – die einzige Stadt mit
eigenständiger Nachfrage nach „Schließanlage + Ort“), Salzwedel (Branchenbuch-Eintrag vorhanden). Für Hamburg und Hannover
ist der Wettbewerb deutlich stärker (Klöppner, Büttner, BSS, Freihoff).

**Realistische Einordnung „ganz oben“:** Für „<Leistung> <Stadt>“ zeigt Google zuerst Anzeigen, dann das lokale 3er-Paket
aus Google-Unternehmensprofilen, dann organische Treffer. Das lokale Paket wird nach Entfernung zum Suchenden sortiert. Mit
Firmensitz Bad Bevensen ist das Paket in Uelzen, Bad Bevensen, Ebstorf, Bienenbüttel und Wieren erreichbar, in Lüneburg
(30 km) mit Glück, in Celle, Winsen, Gifhorn, Hamburg praktisch nicht – es sei denn, es gibt dort einen echten,
besetzten Standort (virtuelle Büros verbietet Google). Organisch ist Platz 1 für die Stadtseiten in allen genannten Orten
realistisch, weil kein Wettbewerber vergleichbar spezialisierte Seiten hat. Der Weg dahin führt über Kapitel 8.

## 6. Strukturierte Daten

| Seite(n) | Knoten | Problem |
|---|---|---|
| Startseite, /lueneburg/, /uelzen/, 13 Stadtseiten | `["LocalBusiness","Locksmith"]` `#organization`, `Service`, `FAQPage`, ProvenExpert-`Product` | Typ „Locksmith“ (Schlüsseldienst) passt nur, wenn Türöffnung/Notdienst angeboten wird |
| /kamerasysteme/, /videoueberwachung-schlachthoefe/ | `LocalBusiness` `#organization` (ohne Locksmith), `image` = Kamera-Logo statt Firmenbild, `hasMap` nur hier | gleiche `@id`, anderer Typ und andere Werte |
| /karriere/ | `Organization` `#organization`, `areaServed: "Norddeutschland"`, anderes Logo (ProVision-Infra-GmbH-blau), zusätzlich eigene `WebSite`-/`WebPage`-/`BreadcrumbList`-Knoten mit denselben `@id`s wie Yoast | Dubletten; Yoast-Knoten und manuelle Knoten konkurrieren |
| alle | Yoast `WebSite.publisher` leer, kein Yoast-Organisationsknoten | Yoast „Unternehmensdaten“ nicht gepflegt |
| 7 Seiten | ProvenExpert: `Product` „ProVision Infra“ mit `AggregateRating` 5/136 | Eigenbewertung als Produkt-Bewertung; verstößt gegen die Richtlinie für Bewertungs-Snippets („self-serving reviews“), Risiko einer manuellen Maßnahme |
| 7 Seiten | `FAQPage` mit 6–17 Fragen | technisch korrekt; seit 2023 zeigt Google FAQ-Rich-Results nur noch für Behörden-/Gesundheitsseiten – kein SERP-Vorteil, aber kein Schaden |
| /karriere/ | 4 × `JobPosting` (datePosted 18./24.10.2026, validThrough 31.01.2027, jobLocation, hiringOrganization) | gut; `validThrough` vor Ablauf verlängern, sonst Fehler in der Search Console |
| alle | `openingHoursSpecification` Mo–Do 9–18, Fr 9–14 | konsistent mit sichtbaren Angaben der Stadtseiten |

Empfehlung: **eine** zentrale Organisationsdefinition (Yoast „Organisation“ mit Name, Logo, Profilen; oder ein einziges
HTML-Widget im Footer-Template) mit `LocalBusiness` als Typ (`Locksmith` nur, wenn Notdienst angeboten wird), Geo, Telefon,
Öffnungszeiten, `sameAs`, `areaServed` als vollständige Liste. Auf den Seiten bleiben nur `Service`- und `FAQPage`-Knoten mit
`provider: {"@id": "…#organization"}`. ProvenExpert-Widget: Option „Rich Snippet / strukturierte Daten“ abschalten (das
Siegel selbst bleibt). Auf /karriere/ die duplizierten WebSite-/WebPage-Knoten entfernen.

## 7. Performance (Lighthouse mobil, 17.11.2026)

| Seite | Performance | LCP | TBT | CLS | Transfer | Requests | Barrierefreiheit | Best Practices | SEO |
|---|---|---|---|---|---|---|---|---|---|
| / | 52 | 5,0 s | 700 ms | 0 | 4,1 MB | 153 | 94 | 75 | 100 |
| /lueneburg/ | 64 | 3,4 s | 770 ms | 0,003 | 3,9 MB | 140 | 99 | 75 | 100 |
| /kamerasysteme/ | 54 | 6,4 s | 540 ms | 0,003 | 3,1 MB | 138 | 95 | 75 | 92* |
| /zutrittssystem/ | **48** | **16,4 s** | 810 ms | 0,003 | **13,1 MB** | 126 | 98 | 75 | 100 |
| /celle/ | 56 | 4,2 s | 760 ms | 0,002 | 3,9 MB | 140 | 99 | 75 | 100 |

\* robots.txt-Prüfung des Audits schlug einmalig fehl (vermutlich 429 des Hosters); robots.txt ist gültig.

Ursachen und Hebel:

- **Bilder:** `Untitled-design-1.png` 697 KB, `Ellipse-3.png` 449 KB, `Ellipse-4.png` 238 KB, `1.png`/`2.png` 217 KB –
  als WebP/AVIF 930–960 KB Einsparung je Seite. Die Ellipsen sind Deko-Verläufe und könnten CSS sein.
- **Videos:** /zutrittssystem/ lädt `Untitled-design.mp4` (6,2 MB) und `Untitled-design-1.mp4` (3,7 MB) – beide auf dem Handy.
  Die anderen Seiten wurden am 02.11. bereits auf 0,8/1,9 MB umgestellt; /zutrittssystem/ fehlt. /kamerasysteme/ und die
  Schlachthof-Seite nutzen `kamera-hero-video-4k.mp4` und `…-mobil-1080.mp4` (493 KB mobil; Desktop-4K-Datei prüfen).
- **Drittanbieter:** Google Tag Manager 322 KB (380–480 ms Blockierzeit) und Facebook-Pixel 207 KB (260–435 ms) laden vor der
  Einwilligung (im Audit ohne Klick im Cookie-Banner) – neben der Performance ein Datenschutz-Punkt zum Prüfen. BugHerd
  (77 KB) läuft ins Leere („Unauthenticated Error“ in der Konsole) und sollte entfernt werden (steht schon in TECHNIK-CHECK.md).
  ProvenExpert-Widget 29 KB + AWS 56 KB.
- **Render-blockierend:** jQuery, jquery-migrate, Font-Awesome `all.min.css`, Elementor-Widget-CSS, Post-CSS – 330–850 ms.
  WP Rocket: „CSS asynchron laden/Unused CSS entfernen“, „JS verzögert ausführen“ und „JS verzögern bis Interaktion“ für GTM,
  Facebook, ProvenExpert, Lottie prüfen (Hero-Video-Skript ausnehmen).
- **Ungenutztes JS** 300–340 KB (GTM, gtag, Facebook, Lottie); **Legacy-JS** 56 KB.
- **DOM** 1.266–1.555 Elemente; Elementor-Container mit Desktop-/Mobil-Duplikaten verdoppeln Inhalte.
- **Server:** TTFB 220 ms, Varnish-Cache aktiv – gut.
- **Barrierefreiheit:** `aria-allowed-role`, `aria-hidden-focus`, `heading-order` (Startseite), `skip-link` (/zutrittssystem/).

Ziel nach Umsetzung: Performance ≥ 80 mobil, LCP < 2,5 s, TBT < 200 ms. Core Web Vitals sind ein (kleiner) Rankingfaktor und
ein großer Conversion-Faktor auf dem Handy, wo die lokale Suche überwiegend stattfindet.

## 8. Keywords, Nachfrage und Wettbewerb

### 8.1 Was in der Region tatsächlich gesucht wird (Google-Suggest, 96 Kombinationen)

| Begriff | Orte mit Vervollständigung | Bedeutung für ProVision |
|---|---|---|
| Schlüsseldienst <Stadt> | alle 16 Orte, oft mit Zusätzen („kosten“, „notdienst“, Straßennamen) | B2C-Notdienst-Intention; nur relevant, falls Türöffnung/Notdienst für Firmenkunden angeboten wird. Dann eigene Seite „Schlüsselnotdienst für Gewerbe“. Sonst `Locksmith`-Schema entfernen |
| Sicherheitstechnik <Stadt> | Lüneburg, Winsen (Luhe), Uelzen, Celle, Gifhorn, Soltau, Hamburg | **Hauptchance**: Oberbegriff, den Kunden benutzen; auf der Website fast nicht vorhanden |
| Videoüberwachung <Stadt> | Lüneburg, Hamburg | bereits bedient (/lueneburg/, /kamerasysteme/); Titel-/H1-Platz für Lüneburg stärken |
| Alarmanlage <Stadt> | Lüneburg, Celle, Hamburg | kein Angebot auf der Website; entweder Einbruchmeldeanlagen (eigenes Angebot oder Partner) aufnehmen oder bewusst auslassen |
| Schließanlage <Stadt> | nur Hamburg | geringe lokale Nachfrage als Einzelbegriff; Nachfrage läuft über „Sicherheitstechnik“, „Schlüsseldienst“ und generische B2B-Begriffe |
| Zutrittskontrolle <Stadt> | nur Hamburg | wie oben |

Generische Begriffe mit Nachfrage (ohne Ort): „schließanlage unternehmen“, „zutrittskontrolle unternehmen“, „videoüberwachung
unternehmen (dsgvo, eingangsbereich)“, „digitale schließanlage (kosten, nutzungsdauer, simonsvoss, mehrfamilienhaus, test,
vergleich, abschreibung, abus)“, „elektronischer schließzylinder (nachrüsten, mit transponder, mit fingerabdruck, haustür,
testsieger)“, „schließanlage mieten“, „videoüberwachung schlachthof“.

Informationelle Fragen mit Nachfrage (Ratgeber-Potenzial): „schlüssel verloren firma wer haftet / haftpflicht“,
„schließanlage austauschen kosten / bei schlüsselverlust / mehrfamilienhaus“, „schließanlage mehrfamilienhaus schlüssel
verloren kosten / versicherung / generalschlüssel“, „videoüberwachung firmengelände erlaubt / dsgvo muster / mitarbeiter /
schild / betriebsrat / rechtsgrundlage“, „videoüberwachung lagerhalle erlaubt“, „videoüberwachung baustelle (kosten, mieten,
dsgvo, schild)“, „videoüberwachung stall erlaubt / schild“, „zutrittskontrolle kita“, „zutrittskontrolle fitnessstudio“,
„schließanlage sportverein“, „digitale schließanlage kostengruppe“, „zutrittskontrolle kostengruppe din 276“.

Markenbegriffe: „provision infra gmbh rezensionen“ wird vervollständigt – es gibt Markennachfrage; Rezensionen sind das
erste, was Suchende sehen wollen.

### 8.2 Wettbewerb je Stadt (Recherche-Schnappschuss)

- **Lüneburg:** Elbe Schlüsselzentrum, Rainer Schlüsseldienst, Heidenreich Elektrotechnik (eine Unterseite
  „Kommunikations- und Sicherheitstechnik“, ca. 300 Wörter, keine Stadtseiten, keine Bewertungen), Haus für Sicherheit
  (Alarm/Video), Branchenverzeichnisse (trustlocal, Gelbe Seiten, 11880).
- **Celle:** servtech GmbH, SicherheitsCelle, SiTech Klindtworth, Draht + Schutz – klassische Sicherheitstechniker mit
  Alarm/Video, keine Spezialisierung auf Schließanlagen für Unternehmen.
- **Uelzen, Winsen, Dannenberg, Hitzacker, Bleckede:** keine spezialisierten Anbieter mit eigener Online-Präsenz gefunden; die
  Freihoff Gruppe (ca. 300 Mitarbeitende) schreibt Techniker für Uelzen/Winsen aus, hat aber keine lokalen Seiten.
- **Munster:** Klaus Vorländer (Alarmanlagen, Verzeichniseintrag ohne Öffnungszeiten), Hekö in Soltau.
- **Regional (Niedersachsen):** Weberprotect (Content-Marketing-Blog zu Videoüberwachung mit Städtelisten).
- **Hamburg:** Klöppner Schließanlagen und Sicherheitstechnik, Büttner, BSS – etablierte Marken mit Bewertungen.

Fazit: In den acht genannten Orten gibt es keinen Wettbewerber, der Schließanlagen, Zutrittskontrolle und Videoüberwachung für
Unternehmen mit lokalen Inhalten anbietet. Die Rankings werden heute von Verzeichnissen und Schlüsseldiensten gehalten, die
sich mit gut verlinkten, wirklich lokalen Seiten plus starkem Unternehmensprofil überholen lassen.

### 8.3 Off-Page-Status

| Signal | Befund |
|---|---|
| Google-Unternehmensprofil | zwei Einträge laut ProvenExpert-Anbindung: 81 Rezensionen (5,0) und 24 Rezensionen (5,0). Namen/Kategorien konnten ohne Login nicht geprüft werden |
| ProvenExpert | 4,99/5 aus 31 Bewertungen (12 Monate), 100 % Empfehlung, neueste 03.11.2026; Adresse und zwei Telefonnummern (…4049040 / …4049049) |
| Branchenbücher | ortsdienst.de (Heidekreis/Munster und Salzwedel): Eintrag unter „Wachschutz/Personenschutz“, **ohne** Telefon und Website |
| Backlinks (gefunden) | keyrent.de: 2 Artikel, Follow-Links mit Anker „ProVision Infra GmbH“ auf `www.provision-infra.de` (301 → ohne www, Linkkraft bleibt); gewinnermagazin.de und unternehmerjournal.de (28.04.2026, als „Anzeige“ markiert, `rel="nofollow"`, Anker „unverbindliches Erstgespräch“); ProvenExpert-Profil; LinkedIn (`/company/provision-infra-gmbh-i-g/` – „i.G.“ im Slug), Facebook, Instagram |
| Marken-SERP | Bei der Suche nach „ProVision Infra“ erscheinen auch die öffentlichen GitHub-Repositories (`landeseite-_kamerasysteme`, `unterseite_Uelzen`) mit internen Arbeitsdokumenten (README: „unveröffentlichter Entwurf“). Das Lüneburg-Repo ist privat |
| Presse/Verbände/Hersteller | keine Erwähnungen in regionaler Presse (LZ, AZ, Cellesche Zeitung) oder Hersteller-Partnerverzeichnissen (SimonsVoss, EVVA, TP-Link VIGI, Nuki) gefunden |

## 9. Empfehlungen – priorisiert

### Phase 1 (sofort, 1–2 Wochen, überwiegend Konfiguration)

1. **Hauptmenü „Main“ umbauen** (WordPress → Design → Menüs; gilt für alle Seiten, die „Main“ nutzen):
   - Leistungen ▾: Digitale Schließanlagen (/), Elektronische Schließanlage & Zutrittskontrolle (/zutrittssystem/),
     Kamera- & Videoüberwachung (/kamerasysteme/), Videoüberwachung für Schlachthöfe (/videoueberwachung-schlachthoefe/)
   - Standorte ▾: Lüneburg, Uelzen, Celle, Winsen (Luhe), Bad Bevensen, Dannenberg, Hitzacker, Bleckede, Gifhorn, Lüchow,
     Wittingen, Ebstorf, Bienenbüttel, Wieren, Bad Bodenteich, (neu) Munster
   - Über uns, Referenzen (neu), Karriere, Kontakt
   - Die Sprunganker bleiben als Sekundärnavigation innerhalb der Seite (Sticky-Leiste oder Inhaltsverzeichnis).
   - Die Stadtseiten nutzen eigene Menüs („Menü Lüneburg“, „Menü Uelzen“): dort dieselben Punkte „Leistungen“ und „Standorte“ ergänzen.
2. **Footer-Template** (Elementor Theme Builder): NAP-Block „ProVision Infra GmbH · Klein Hesebecker Straße 11 · 29549 Bad
   Bevensen · Telefon als `tel:+4958214049040` · E-Mail · Mo–Do 9–18, Fr 9–14“ plus Spalte „Standorte“ mit allen Stadtseiten
   und Spalte „Leistungen“. Gleicher Block auf Startseite, /kamerasysteme/, /zutrittssystem/ sichtbar.
3. **Startseite:** Abschnitt „Schließanlagen und Videoüberwachung in deiner Region“ mit je einem Satz und Textlink pro Stadt
   (Ankertext „Schließanlagen & Videoüberwachung in Celle“ statt „Celle“). H1/Untertitel um die Region ergänzen („… zwischen
   Hamburg und Hannover“ oder „… im Raum Lüneburg, Uelzen und Celle“).
4. **/kamerasysteme/** verlinkt die Schlachthof-Seite (Abschnitt „Branchenlösungen“); die Schlachthof-Seite verlinkt zurück.
5. **Google-Unternehmensprofil:**
   - Beide Einträge im Business-Profil-Manager prüfen. Duplikat → zusammenführen lassen (Support „Duplikat melden“, Rezensionen
     werden in der Regel übernommen). Zwei echte Standorte → beide pflegen und auf der Website je eine Standortseite verlinken.
   - Hauptkategorie „Installateur für Sicherheitssysteme“ (engl. „Security system installer“) prüfen, Zusatzkategorien
     „Anbieter von Sicherheitssystemen“, ggf. „Schlüsseldienst“ nur bei Notdienst-Angebot. Exakte Kategorienamen im Profil-Manager
     verifizieren.
   - Leistungen anlegen (Mechanische Schließanlage, Elektronische Schließanlage, Zutrittskontrolle, Videoüberwachung,
     Wartung/Service), Einzugsgebiet mit allen 16 Orten, Website = Startseite, UTM-Parameter für Auswertung.
   - Wöchentlich 1 Beitrag (Projekt, Tipp, Rechtsänderung § 4d TierSchG), 20+ Fotos von echten Montagen, Fragen & Antworten
     vorbelegen, Bewertungslink in jede Abschlussmail.
6. **Strukturierte Daten konsolidieren** (Kapitel 6): Yoast → Suchmaschinen-Darstellung → „Organisation“ mit Logo und Profilen;
   zentrale LocalBusiness-Definition; ProvenExpert-Schema-Option aus; Dubletten auf /karriere/ entfernen; danach mit dem
   Rich-Results-Test prüfen.
7. **Weiterleitungen:** Umlaut-URLs als 301 (Yoast Premium „Weiterleitungen“ oder nginx-Regel des Hosters), danach die drei
   Weiterleitungsseiten löschen; `/Lueneburg/`-Varianten per Regel auf Kleinschreibung umleiten; `http://www.` direkt auf
   `https://` ohne www (ein Hop).
8. **GitHub-Repos** `landeseite-_kamerasysteme` und `unterseite_Uelzen` auf privat stellen (sie erscheinen in der Markensuche).
9. **LinkedIn-Slug** ohne „i-g“ beantragen; alle Profile (Facebook, Instagram, LinkedIn, ProvenExpert) mit identischem Namen,
   Adresse, Telefon und Website-Link.

### Phase 2 (4–8 Wochen, Inhalte)

10. **Stadtseiten individualisieren** – Ziel mindestens 40 % einzigartiger Text ohne Ortsnamen, Reihenfolge nach Auftrag:
    Lüneburg, Uelzen, Celle, Winsen, Dannenberg, Hitzacker, Bleckede, dann Munster (neu), dann die übrigen. Pro Seite:
    - eigener Einstieg mit der konkreten Situation vor Ort (Gewerbegebiete, typische Objekte, Branchenstruktur, z. B. Hafen/
      Elbe-Logistik in Bleckede, Tourismus/Hotels in Hitzacker und Bad Bevensen, Produktion/Zucker in Uelzen, Bundeswehr/
      Truppenübungsplatz in Munster, Hochschule/Verwaltung in Lüneburg, Residenzstadt/Behörden in Celle, Hamburg-Pendler/Logistik
      in Winsen),
    - 2–3 anonymisierte oder freigegebene **lokale Referenzen** mit Fotos (Objektart, Umfang, Lösung),
    - Anfahrt und Reaktionszeit („von Bad Bevensen in 35 Minuten in Lüneburg“), Servicefenster, Ansprechpartner,
    - 4–5 **eigene FAQ** je Stadt (z. B. Lüneburg: Denkmalschutz/Altstadt-Türen; Celle: Fachwerk; Hitzacker: Hochwasser/
      Ferienwohnungen; Munster: Zutritt für Vereine/Kasernenumfeld; Winsen: Logistikhallen),
    - Titel/H1 um „Sicherheitstechnik“ ergänzen, z. B. „Sicherheitstechnik in Lüneburg: Schließanlagen, Zutritt & Videoüberwachung“,
    - die vier Kleinst-Orte (Wieren, Bad Bodenteich, Bienenbüttel, Ebstorf) nach drei Monaten anhand der Search-Console-
      Impressionen prüfen: ohne Nachfrage zu einer Seite „Landkreis Uelzen“ zusammenführen (301).
11. **Neue Seiten:** Munster (Auftrag), Soltau (Nachfrage „sicherheitstechnik soltau“), optional Buchholz i. d. N.; mittelfristig
    Hamburg-Süd/Harburg und Hannover nur mit echten Referenzen dort.
12. **Leistungsseiten schärfen:**
    - /zutrittssystem/ auf 1.800+ Wörter ausbauen: Titel „Elektronische Schließanlage & Zutrittskontrolle für Unternehmen |
      ProVision Infra“; Keyword-Trennung zur Startseite (Startseite = Marke + „digitale Schließanlage für Unternehmen“,
      /zutrittssystem/ = „elektronische Schließanlage“, „Zutrittskontrolle“, Pakete/Service).
    - Neue Seite „Mechanische Schließanlagen“ (EVVA, Sicherungskarte, Schließplan) – heute nur auf Stadtseiten erwähnt.
    - Neue Hub-Seite „Sicherheitstechnik für Unternehmen“ als Klammer (Schließanlage + Zutritt + Video + Service) für den
      meistgesuchten Oberbegriff.
    - Seite „Referenzen/Projekte“ (E-E-A-T, lokale Beweise, intern auf Stadtseiten verlinkt) und „Über uns“ als eigene Seite
      (Team, Zertifikate/Herstellerschulungen, Versicherungen, Gründer).
    - Entscheidung „Alarmanlagen“: Nachfrage in Lüneburg/Celle vorhanden; falls als Angebot (eigen oder Partner) möglich,
      eigene Seite; sonst nicht bedienen.
    - Preisrahmen in den FAQ „Was kostet …“ (die häufigste Suchabsicht neben „erlaubt“), z. B. „ab … € je Tür inklusive Montage“.
13. **Ratgeber-Bereich** (/ratgeber/), 8–12 Artikel à 1.200–1.800 Wörter, jeweils mit Links auf Leistungs- und Stadtseiten:
    „Schlüssel verloren im Unternehmen: wer haftet, was kostet der Austausch der Schließanlage“, „Videoüberwachung auf dem
    Firmengelände: erlaubt? DSGVO-Muster, Hinweisschild, Betriebsrat“, „Digitale Schließanlage: Kosten, Nutzungsdauer,
    Abschreibung“, „Mechanisch, elektronisch oder digital – Vergleich für Betriebe“, „Schließanlage Mehrfamilienhaus: Schlüssel
    verloren – Ablauf für Hausverwaltungen“, „Videoüberwachung Lagerhalle/Baustelle/Stall: was erlaubt ist“, „Zutrittskontrolle
    für Kita, Praxis, Fitnessstudio, Sportverein“, „Kamerapflicht Schlachthöfe § 4d TierSchG – Checkliste“ (ergänzt die
    bestehende Seite), „Elektronischen Schließzylinder nachrüsten“.
14. **Performance-Paket:** PNG → WebP (Imagify/ShortPixel oder manuell), Ellipsen als CSS; /zutrittssystem/-Videos auf die
    kleinen Fassungen (≤ 1 MB mobil, ≤ 2 MB Desktop); BugHerd-Skript entfernen; WP Rocket „JS verzögern“ für GTM/Pixel/
    ProvenExpert/Lottie (Hero-Video-Snippet ausnehmen), „Unused CSS entfernen“ testen; jquery-migrate abschalten; Lottie nur
    im Viewport laden (Steuer-Container der Sitzung vom 02.11. prüfen); Consent-Verhalten von GTM/Facebook-Pixel prüfen.
15. **404-Seite** gestalten (Suche, Links zu Leistungen und Standorten, Telefon); **Impressum/Datenschutz/AGB** mit kurzer
    Description versehen (optional).

### Phase 3 (laufend, ab Monat 2)

16. **Citations (Branchenbücher):** ortsdienst.de korrigieren (Kategorie Sicherheitstechnik, Telefon, Website); Einträge mit
    identischen Daten bei Gelbe Seiten, Das Örtliche, 11880, GoYellow, Cylex, trustlocal, wlw (B2B), Yelp, Bing Places, Apple
    Business Connect, IHK Lüneburg-Wolfsburg, Handwerkskammer (falls Mitglied), Wirtschaftsförderung Landkreis Uelzen.
17. **Hersteller- und Partnerverzeichnisse:** SimonsVoss-Partnersuche, EVVA-Partner, TP-Link VIGI/Omada-Partner, Nuki Pro,
    Keyota/Keyrent-Partnerseiten (keyrent.de verlinkt bereits zweimal – ausbauen: Gastbeitrag, Case Study).
18. **Regionale PR und Links:** Fachbeitrag zur Kamerapflicht § 4d TierSchG in Landwirtschafts-/Fleischereiverbänden
    (Landvolk, Fleischerverband Niedersachsen), Pressemitteilung an LZ, AZ Uelzen, Cellesche Zeitung, Winsener Anzeiger,
    EJZ (Lüchow-Dannenberg), Böhme-Zeitung (Munster/Soltau); Sponsoring lokaler Vereine mit Link; Vorträge bei
    Unternehmerverbänden/Wirtschaftsjunioren.
19. **Bewertungen:** Google-Rezensionen weiter sammeln (Ziel: 150+ auf einem Eintrag), auf jede antworten, in den Antworten
    Ort und Leistung nennen („Danke für den Auftrag in Celle – Schließanlage mit 40 Türen“).
20. **Monitoring:** Search Console (Leistung je Stadtseite, Index-Abdeckung, Rich-Results-Fehler), Unternehmensprofil-
    Statistik, Rank-Tracking für 30 Kernbegriffe (Sicherheitstechnik/Schließanlage/Videoüberwachung × 8 Städte + generisch),
    quartalsweise Aktualisierung der Stadtseiten (neue Referenzen, Datum).

## 10. Keyword-Zuordnung (Soll)

| Seite | Fokus | Nebenbegriffe |
|---|---|---|
| / | digitale Schließanlage für Unternehmen, ProVision Infra | Schließsystem Unternehmen, Access Management as a Service, Region Hamburg–Hannover |
| /zutrittssystem/ | elektronische Schließanlage, Zutrittskontrolle Unternehmen | Zutrittssystem, Transponder, Service-Pakete, Wartung |
| neu: /mechanische-schliessanlagen/ | mechanische Schließanlage, Schließplan, Sicherungskarte | EVVA, Schließanlage austauschen, Schlüssel verloren Firma |
| neu: /sicherheitstechnik/ | Sicherheitstechnik für Unternehmen | Sicherheitstechnik Lüneburg/Uelzen/Celle (verlinkt Stadtseiten) |
| /kamerasysteme/ | Videoüberwachung Unternehmen, Kameraüberwachung Firma | DSGVO, Firmengelände, Lagerhalle, App |
| /videoueberwachung-schlachthoefe/ | Videoüberwachung Schlachthof, § 4d TierSchG | Kamerapflicht 2027, Speicherung 30 Tage |
| /lueneburg/ u. a. | Sicherheitstechnik <Stadt>, Schließanlagen <Stadt>, Videoüberwachung <Stadt> | Zutrittskontrolle <Stadt>, Firma in der Nähe |
| /ratgeber/… | je eine informationelle Frage | siehe Kapitel 8.1 |
| /karriere/ | Jobs Sicherheitstechnik Bad Bevensen / Uelzen | Servicetechniker, Quereinsteiger |

## 11. Reihenfolge und Erfolgsmessung

Woche 1–2: Menü, Footer, Startseiten-Region, Unternehmensprofil, Schema, Weiterleitungen, Repos privat (Phase 1).
Woche 3–8: Stadtseiten Lüneburg → Uelzen → Celle → Winsen → Dannenberg → Hitzacker → Bleckede → Munster (neu), /zutrittssystem/-
Ausbau, Performance-Paket, erste vier Ratgeber-Artikel.
Ab Monat 3: restliche Stadtseiten, Referenzseite, Citations, PR, monatliche Auswertung.

Messgrößen: Impressionen und Klicks je Stadtseite in der Search Console (Ziel: jede Zielstadt mit Impressionen für
„Sicherheitstechnik/Schließanlage/Videoüberwachung <Stadt>“ innerhalb von 8 Wochen, Top 3 innerhalb von 4–6 Monaten),
Anrufe/Formulare aus dem Unternehmensprofil, Lighthouse-Performance ≥ 80 mobil, Anzahl Google-Rezensionen, Anzahl verweisender
Domains. Platz 1 lässt sich nicht garantieren; die genannten Maßnahmen schließen aber jede gefundene Lücke zum Wettbewerb und
bauen in der Region einen Vorsprung auf, den heute niemand hat.

## Anhang

- `seo-analyse/seiten-metriken-2026-11-17.txt` – Kennzahlen aller 33 geprüften URLs, Dubletten-Matrix, Linkgraph, Schema je Seite
- `seo-analyse/lighthouse-mobil-2026-11-17.txt` – Lighthouse-Details (Chancen, größte Dateien, Drittanbieter, Audits)
- `seo-analyse/google-suggest-orte.txt`, `google-suggest-longtail.txt`, `google-suggest-marke.txt` – Vervollständigungen
- `SEO-KEYWORDS.md` – Keyword-Karte Kameraseite (26.10.2026), `SCHLACHTHOEFE-SEO.md`, `TECHNIK-CHECK.md`
