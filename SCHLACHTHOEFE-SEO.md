# SEO-Optimierung: /videoueberwachung-schlachthoefe/ (Seite 4870)

Stand: 07.11.2026 · Auftrag: vollständige SEO-Optimierung und Indexierung in der Google Search Console.
Die Seite wurde am 07.11.2026 von der Parallelsitzung „Neue Unterseite mit Videoüberwachung“ aus der Kamera-Seite (4313)
aufgebaut; dieser Durchgang baut darauf auf. Abgestimmt per `send_message`, Speicherungen aus frischem Editor-Export.

## 1. Ausgangslage (Audit vor der Änderung)

| Prüfpunkt | Befund |
| --- | --- |
| Titel | 65 Zeichen (zu lang): „Videoüberwachung im Schlachthof (§ 4d TierSchG) \| ProVision Infra“ |
| Description | 192 Zeichen (zu lang) |
| H1 | „Videoüberwachung für Schlachthöfe nach dem neuen Tierschutzgesetz“ |
| Inhalt | ca. 1.900 Wörter, 12 FAQ, fünf Pflichtpunkte nach § 4d, Ablauf, Technik, Standort; fachlich bereits sehr gut |
| Schema | LocalBusiness + Service (eigenes Widget), FAQPage (EA-Akkordeon), Yoast WebPage/Breadcrumb, ProvenExpert Product |
| OG-Bild | Logo (258 × 60 px) statt eines Vorschaubilds |
| NAP | kein Telefon-/E-Mail-Link auf der Seite |
| Suchbegriffe | „Kameraüberwachung“ 0×, „Schlachtbetrieb“ 0×, „Deutschland“ 0×, „TierSchG“ 0× |
| Indexierung | in `page-sitemap.xml`, `index, follow`, Canonical korrekt; zusätzlich Seite 4891 mit Umlaut-Slug (noindex, „Weiterleitung“) in der Sitemap |

## 2. Rechtslage (geprüft, Quellen)

- Bundestag, 05.11.2026: Gesetz zur Änderung des Tierschutzgesetzes und des Tierhaltungskennzeichnungsgesetzes,
  Entwurf Drucksache 21/6809 in der Fassung der Beschlussempfehlung Drucksache 21/8974 (Text des neuen § 4d dort,
  Abs. 3 und 4): Aufzeichnung von Entladung, Wartezeit bis Betäubung, Betäubung, Aufhängen, Entblutungsschnitt,
  Entblutung, ersten Schlachtarbeiten; Datum und Uhrzeit ständig lesbar; Speicherung der letzten 30 Schlachttage plus
  Entladung; arbeitstäglicher Abruf durch die Behörde in einem üblichen Dateiformat, je Kamera mit Standort;
  Anwendung ab dem Tag des Inkrafttretens im Folgejahr (ein Jahr Übergang).
  Quelle: https://dserver.bundestag.de/btd/21/089/2108974.pdf
- heise online, 05.11.2026: Inkrafttreten 1. Januar 2027, einjährige Übergangsfrist, Schwellen 1.000 Großvieheinheiten
  bzw. 150.000 Stück Geflügel/Kaninchen pro Jahr, 232 von über 4.500 Betrieben (über 90 % der Schlachtungen),
  Anordnung bei kleineren Betrieben in Verdachtsfällen.
  Quelle: https://www.heise.de/news/Tierschutz-Nur-grosse-Schlachthoefe-von-Videopflicht-betroffen-11513964.html
- Bundesrat und Verkündung standen am 07.11.2026 noch aus; die Seite sagt das in FAQ 2.

Die bestehenden Seitentexte stimmen mit diesen Quellen überein; geändert wurden nur Formulierungen für Suchbegriffe
und Ergänzungen (siehe 4).

## 3. Keyword-Set

Google Suggest (Deutschland, 07.11.2026): Vervollständigungen gibt es für „videoüberwachung schlachthof“,
„videoüberwachung schlachthöfe“ (+ „… in schlachthöfen petition“), „kameraüberwachung schlachthof“, „schlachthof
kamera“, „tierschutzgesetz videoüberwachung“, „schlachthof überwachung“. Keine Vervollständigungen für
„kamerapflicht schlachthof“, „§ 4d tierschutzgesetz“, „… pflicht/gesetz/kosten/datenschutz“ – die Nachfrage entsteht
mit dem Gesetz gerade erst, die Presse nutzt „Kamerapflicht“ und „Videopflicht“.

| Priorität | Suchbegriff | Einsatz |
| --- | --- | --- |
| 1 | Videoüberwachung Schlachthof / Schlachthöfe | Titel, H1, URL, Hero, H2 „Videoüberwachung für Schlachthöfe: gesetzeskonform …“, FAQ, Service-Schema |
| 1 | Kamerapflicht Schlachthof (ab 2027) | Titel, Description, Hero-H2, Einleitung, FAQ 1 neu |
| 1 | § 4d Tierschutzgesetz / TierSchG | Titel, H1, Einleitung, Pflichtpunkte, Schema `about` (Legislation) |
| 2 | Kameraüberwachung Schlachthof | Einleitung (neu) |
| 2 | Tierschutzgesetz Videoüberwachung, Videoaufzeichnung Schlachthof | H2, FAQ |
| 2 | Schlachtbetrieb, Veterinäramt, Betriebsrat, DSGVO, 30 Schlachttage | Fließtext, FAQ |
| 3 | Niedersachsen, bundesweit/deutschlandweit | Standort-H2, Standort-Text, FAQ Niedersachsen (neu), Schema areaServed Deutschland |

## 4. Umgesetzte Änderungen (07.11.2026, 18:22 UTC Elementor, 18:24 UTC Yoast)

Elementor-Daten (`tools/schlachthoefe_seo_transform.mjs`, angewandt auf den frischen Export):

- H1 `9dcea29`: „… nach § 4d Tierschutzgesetz“ (statt „nach dem neuen Tierschutzgesetz“).
- Einleitung `47ef5fe`: „Die Kamerapflicht gilt in ganz Deutschland für Schlachtbetriebe ab 1.000 Großvieheinheiten …“.
- Umsetzung `3efeb2a`: „§ 4d TierSchG … Videoüberwachung (Kameraüberwachung) entlang des gesamten Schlachtprozesses“.
- § 18-Absatz `4413783`: Quellenlink auf Drucksache 21/8974 (Bundestag, `rel="noopener"`).
- Standort `5c65e03`: „bundesweit um, von Schleswig-Holstein bis Bayern“ + NAP-Block mit `tel:`- und `mailto:`-Link.
- FAQ: 12 → 17 Fragen (kleine Betriebe/Metzgereien, Betriebsrat § 87 BetrVG, Speicherbedarf für 30 Schlachttage,
  Kameras für Nassbereiche, Unterschied zur freiwilligen Vereinbarung in Niedersachsen).
- Schema (Widget `dca37dc`): Service-Name mit „(Kamerapflicht)“, `serviceType` „Videoüberwachung für Schlachthöfe“,
  neue Beschreibung, `about` = Legislation „§ 4d Tierschutzgesetz“ mit Link auf die Drucksache.

Yoast (Block-Editor, Metabox-Felder geprüft):

| Feld | Wert |
| --- | --- |
| Titel (57) | `Videoüberwachung Schlachthof: Kamerapflicht § 4d TierSchG` |
| Description (160) | `Kamerapflicht für Schlachthöfe ab 2027: Videoüberwachung nach § 4d TierSchG mit Zeitstempel, 30 Tage Speicherung und Behördenabruf. ProVision Infra, bundesweit.` |
| Fokus-Keyphrase | `Videoüberwachung Schlachthof` |
| Breadcrumb-Titel | `Videoüberwachung Schlachthöfe` |
| OG-/Twitter-Bild | `kamera-vorschau-1200x630-1.jpg` (ID 4376, 1200 × 630) |
| Robots | index, follow |

Prüfung nach dem Speichern (gerendertes HTML vorher/nachher): Elementanzahl 346 = 346, Textdiff nur die genannten
Stellen, 2.178 Wörter, FAQPage mit 17 Fragen, Service-Schema gültig, Titel/Description/OG wie oben.

## 5. Search Console

(wird nach der Indexierungsanforderung ergänzt)

## 6. Ehrliche Einordnung „Platz 1 deutschlandweit“

Eine Platzierung kann niemand garantieren. Die Ausgangslage ist aber günstig: Die Suchnachfrage entsteht mit dem
Gesetz gerade erst, die Konkurrenz besteht bisher aus Nachrichtenartikeln, Behörden- und Verbandsseiten, kaum aus
Anbietern mit eigener Fachseite. Die Seite beantwortet die Fragen, die Schlachtbetriebe jetzt haben, mit Quelle.
Für den Spitzenplatz entscheiden die nächsten Monate außerhalb der Seite:

1. **Interne Links** von /kamerasysteme/ (Textlink „Videoüberwachung für Schlachthöfe“) und aus dem Header-Menü der
   Kamera-Seiten; die Seite ist bisher nur über die Sitemap erreichbar.
2. **Backlinks aus der Branche**: Fachpresse (fleischwirtschaft.de, topagrar, agrarheute), Fleischerverbände,
   Landesvereinigung der Ernährungswirtschaft Niedersachsen, IHK; Pressemitteilung „Kamerapflicht ab 2027: Was
   Schlachthöfe jetzt tun müssen“ mit Link auf die Seite.
3. **Inhalt ausbauen, sobald Verkündung und Verordnung vorliegen**: Datum im Bundesgesetzblatt, Text der
   Tierschutz-Schlachtverordnung zu Auflösung/Format, Checkliste als PDF (Linkmagnet), Referenzprojekt mit Fotos.
4. **Google Unternehmensprofil**: Leistung „Videoüberwachung für Schlachthöfe“, Beitrag mit Link.
5. **Zweitseite 4891** (Umlaut-Slug) durch eine 301-Weiterleitung ersetzen, damit keine zweite URL existiert.
6. **Search Console** nach 2–4 Wochen: Suchanfragen mit „Schlachthof“ prüfen und Titel/FAQ nachschärfen.
