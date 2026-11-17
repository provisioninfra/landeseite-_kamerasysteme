# SEO-Check provision-infra.de (17.11.2026): Ziel Platz 1 in Norddeutschland

## 1. Ziel und Rahmen (Antworten des Kunden)

| Frage | Antwort |
|---|---|
| Suchbegriffe | Schließanlagen / digitale Schließsysteme (Startseite), Video- und Kameraüberwachung (`/kamerasysteme/`) |
| Region | ganz Norddeutschland (Niedersachsen, Hamburg, Bremen, Schleswig-Holstein, Mecklenburg-Vorpommern) |
| Google Unternehmensprofil | vorhanden, verifiziert, gepflegt |
| Search Console / Analytics | Zugriff freigegeben; die automatische Anmeldung aus dieser Umgebung scheitert an einer Captcha-Abfrage von Google, Daten müssen exportiert werden |
| Backlinks | Hersteller-Partnerseiten sowie Presse, Vereine und Kunden möglich |
| Wettbewerber | selbst ermitteln; Suchmaschinen (Bing, Qwant) liefern aus dieser Umgebung keine brauchbaren Ergebnisse, Google selbst ist nicht abfragbar |
| Inhalte | Kunde liefert Stoff, Texte entstehen hier |
| Spielraum | Texte nur minimal, Wording, Aufbau, Reihenfolge, Animationen und Formatierungen bleiben; Menü, Verlinkung, neue Seiten und Technik frei |

Geprüft wurden alle 23 Seiten der Sitemap (Quelltext, Überschriften, Titel, Beschreibungen, Strukturdaten, interne
Links, Textähnlichkeit der Ortsseiten), die Server-Technik (Weiterleitungen, Header, Caching, Komprimierung) und das
Ladeverhalten von drei Schlüsselseiten im Chromium-Browser (Handy-Emulation ohne Netzdrosselung). Die
PageSpeed-Schnittstelle von Google war wegen erschöpften Tageskontingents nicht nutzbar.

## 2. Kurzurteil

Nein, die Seite ist nicht perfekt optimiert, aber die Basis ist solide. Technik (HTTPS, Weiterleitungen, Sitemap,
Canonicals, noindex für Kontakt- und Terminseiten), Titel und Beschreibungen, Überschriftenstruktur, FAQ und
Strukturdaten sind auf dem Stand, den die meisten regionalen Wettbewerber nicht haben. Für Platz 1 in ganz
Norddeutschland fehlen vier Dinge, in dieser Reihenfolge:

1. **Reichweite:** Die Website belegt mit 15 Ortsseiten nur den Umkreis von Bad Bevensen. Für Hamburg, Bremen,
   Hannover, Kiel, Lübeck, Rostock, Oldenburg, Osnabrück oder Braunschweig gibt es keine Inhalte, und die
   vorhandenen Ortsseiten teilen 69 bis 76 Prozent ihrer Sätze untereinander (Vorlagentext). Google wertet solche
   Serien schnell als Doorway-Seiten ab; die Serie darf so nicht auf 50 Städte verlängert werden.
2. **Ladezeit:** 3 bis 4 MB je Seite, 110 Anfragen, 37 CSS- und 38 JS-Dateien, Hintergrundbilder als PNG bis 700 KB,
   Hero-Video 0,8 MB am Handy, BugHerd-Skript und Facebook-Pixel auf jeder Seite. Gemessen ohne Netzdrosselung:
   LCP 3,0 bis 3,5 s mobil (Startseite 3,5 s, Kamera-Seite 3,0 s). Mit echtem Mobilfunk liegen die Core Web Vitals
   damit sehr wahrscheinlich im roten Bereich. Das kostet Rankings direkt.
3. **Autorität:** Backlinks und Erwähnungen sind nicht nachweisbar (keine Treffer in der Web-Recherche, der
   Links-Bericht der Search Console fehlt). Ohne Links von Herstellern, Verbänden, Presse und Verzeichnissen gewinnt
   bei überregionalen Begriffen immer die Seite mit mehr Autorität.
4. **Lokale Signale auf den Hauptseiten:** Startseite, Zutrittssystem- und Kamera-Seite zeigen weder Adresse noch
   Telefonnummer; nur zwei Seiten betten eine Karte ein; im Yoast-Schema fehlt die Organisation (Website-Repräsentation
   nicht gesetzt); auf 19 Seiten steht ein Product-Schema mit Eigenbewertung aus dem ProvenExpert-Siegel, das Google
   als irreführende Strukturdaten werten kann.

Ehrlich dazu: „Platz 1 in ganz Norddeutschland“ für Gattungsbegriffe wie „Schließanlage“ oder „Videoüberwachung
Unternehmen“ ist ein Projekt über viele Monate gegen Hersteller, Portale und Großanbieter. Realistisch und messbar
ist: zuerst Platz 1 in den Landkreisen Uelzen und Lüneburg (Karte und organisch), dann je Metropole mit eigenen,
echten Inhalten, dann überregionale Fachbegriffe über Ratgeber.

## 3. Befund im Detail

### 3.1 Technik

| Punkt | Befund | Bewertung |
|---|---|---|
| HTTPS, HSTS, www → ohne www, http → https, Schrägstrich | alles 301, HSTS mit preload | gut |
| robots.txt, Sitemap | offen, Sitemap mit 23 Seiten, Kontakt/Termin/Danke korrekt noindex und nicht in der Sitemap | gut |
| Canonical, og:image, viewport, lang=de | auf allen Seiten korrekt | gut |
| Komprimierung, Caching | Brotli, WP Rocket (x-cacheable YES), TTFB aus dem Cache 0,46 bis 0,70 s | ausreichend |
| Seitengewicht mobil | Startseite 3,6 MB / 111 Anfragen, Kamera 3,2 MB / 115, Lüneburg 3,9 MB / 114; Desktop-Startseite 8,2 MB (Lotties 3,5 MB, Video 1,9 MB) | schlecht |
| Größte Brocken | `Untitled-design-1.png` 2239×2409 px 696 KB, `Ellipse-3.png` 448 KB, `Ellipse-4.png` 236 KB, `2.png`/`1.png` je 217 KB (alle PNG als CSS-Hintergrund, nicht lazy), Hero-Video Handy 798 KB, Facebook-Pixel 204 KB, Lottie-Bibliothek 66 KB | schlecht |
| Dateien | 37 CSS- und 38 JS-Dateien, 71 KB Inline-CSS, HTML 594 KB | schlecht (Zusammenfassen/Minifizieren in WP Rocket nicht aktiv) |
| Drittanbieter | BugHerd (2 Anfragen, Feedback-Werkzeug, gehört nicht auf die Live-Seite), Google Tag Manager, Facebook-Pixel (lädt in der Messung vor jeder Einwilligung), ProvenExpert | BugHerd entfernen, Einwilligung prüfen |
| Bilder | Startseite 47 Bilder, nur 8 WebP, 41 lazy; dekorative SVG-Platzhalter ohne Alt (7 je Seite, unkritisch) | mittel |
| Ladeverhalten gemessen | LCP mobil: Start 3,46 s, Kamera 3,0 s, Lüneburg 1,98 s; CLS 0; lange Tasks 130 bis 320 ms | gelb bis rot |

### 3.2 Inhalt und On-Page

- Titel 50 bis 60 Zeichen, Beschreibungen 144 bis 160 Zeichen, keine Dubletten; Impressum, Datenschutz und AGB ohne
  Beschreibung (unkritisch).
- Genau eine H1 je Seite, 13 bis 19 H2 auf den Leistungsseiten, FAQ-Akkordeons mit FAQPage-Schema überall.
- Keyword-Belegung:
  - Startseite: „Schließanlage“ im Titel und in 3 H2, aber nicht in der H1 („… digitales Schließsystem“); kein
    Ortsbezug in Titel oder H1 (Lüneburg 4×, Uelzen 2×, Norddeutschland 3× im Text). Für „Schließanlage Lüneburg“
    rankt deshalb eher die Ortsseite, für „Schließanlage Norddeutschland“ niemand.
  - `/zutrittssystem/`: Titel und H1 nennen „Elektronische Schließanlage“, das Wort „Zutrittskontrolle“ fehlt ganz,
    „Zutrittssystem“ nur 2× im Text; Adresse und Begriff passen nicht zusammen.
  - `/kamerasysteme/`: Kamera, Videoüberwachung, Videosicherheit, Unternehmen in Titel, H1, H2 und Textanfang;
    Ortsbezug nur Hamburg/Hannover in einer H2.
  - Ortsseiten Lüneburg/Uelzen: Schließanlage, Videoüberwachung und Ort in Titel, H1, 7 H2 und Textanfang; gut.
- Wortzahlen (ohne Kopf und Fuß): Start 2.767, Kamera 2.232, Zutritt 1.262, Ortsseiten 2.286 bis 2.582,
  Schlachthof 2.473.
- Ortsseiten: Anteil der Sätze, die wortgleich auch auf anderen Ortsseiten stehen: 69 bis 76 Prozent (ähnlichste
  Paare 39 bis 40 Prozent gemeinsame Sätze).

### 3.3 Struktur und Verlinkung

- Die Ortsseiten sind nur untereinander verlinkt (12 bis 14 eingehende Links je Seite, alle von anderen Ortsseiten);
  Startseite, Menü und Footer verlinken keine einzige Ortsseite.
- `/videoueberwachung-schlachthoefe/` hat null interne Links (nur Sitemap); `/karriere/` vier.
- Hauptmenü: „Schließanlagen“, „Videoüberwachung“, „So arbeiten wir“, „Über uns“, „FAQ“, „Mehr“; keine Standorte.

### 3.4 Lokale Signale

- LocalBusiness (Locksmith) auf 19 Seiten, Karte nur auf Kamera- und Schlachthof-Seite, Adresse und Telefon im
  Text der Ortsseiten, aber nicht auf Startseite, Zutrittssystem- und Kamera-Seite und nicht im Footer.
- Yoast: Organisation/Person nicht im Schema der Startseite, also Website-Repräsentation (Firma, Logo,
  Social-Profile) nicht gesetzt.
- Bewertungen: 5,0 bei Google (Zähler auf der Seite), 136 bei ProvenExpert; für das lokale Ranking zählen Google-
  Bewertungen, die Anzahl ist nicht bekannt.
- Product-Schema mit Eigenbewertung (ProvenExpert-Shortcode) auf 19 Seiten im Quelltext; das Ladeverhalten-Skript
  entfernt es nur im Browser, Google liest den Quelltext.

### 3.5 Autorität und Wettbewerb

- Web-Recherche (US-Index) findet keine Erwähnung von „ProVision Infra“ außerhalb der eigenen Seite; Backlinks sind
  erst mit dem Links-Bericht der Search Console belastbar.
- Wettbewerber aus der Recherche für Videoüberwachung im Norden: Graef-Gruppe (Hannover/Hamburg, Dahua),
  Yagemi (Hannover), Weberprotect (Niedersachsen), DEKOM (Hamburg), Schlegel Sicherheitstechnik (Bremen); für
  Schließanlagen dominieren Hersteller (ABUS, SimonsVoss, EVVA, dormakaba) und Portale (Vergleich.org, Heinze,
  Baunetz). Regionale Betriebe im Raum Lüneburg/Uelzen konnten aus dieser Umgebung nicht ermittelt werden.
- Laut Google-Suggest (Parallelsitzung, 16./17.11.) wird gesucht: „videoüberwachung unternehmen“, „… firma“,
  „… firmengelände“, „videoüberwachung lüneburg“; „videosicherheit“ hat keine Vervollständigung.

## 4. Maßnahmenplan (innerhalb des Spielraums: Texte minimal, Aufbau bleibt)

### Stufe A: sofort, ohne Eingriff in Wording oder Aufbau

| Nr. | Maßnahme | Wirkung | Aufwand |
|---|---|---|---|
| A1 | Product-Schema (ProvenExpert-Eigenbewertung) serverseitig entfernen (Shortcode-Code oder Filter), Siegel bleibt sichtbar | schützt vor Abwertung der Strukturdaten | klein |
| A2 | Yoast: Website-Repräsentation „Organisation“ mit Logo und Social-Profilen; Breadcrumbs prüfen | Organisation im Knowledge Graph, saubere Schema-Verknüpfung | klein |
| A3 | Footer-Vorlage: Adresse, Telefon, E-Mail, Öffnungszeiten, Linkblock „Standorte“ (15 Ortsseiten) und „Leistungen“ (Zutritt, Kamera, Schlachthöfe) | lokale Signale auf jeder Seite, alle Seiten erreichbar | klein |
| A4 | Hauptmenü „Mehr“: Unterpunkte „Standorte“ und „Schlachthöfe“ (Freigabe für Menüänderung nötig) | Crawling und Gewichtung der Ortsseiten | klein |
| A5 | Interne Links in bestehenden Regions-Absätzen: Kamera ↔ Schlachthof, Kamera ↔ Zutritt, Ortsseiten → Leistungsseiten (je ein Link, kein neuer Text) | Verteilung der Linkkraft | klein |
| A6 | BugHerd entfernen; Facebook-Pixel/GTM erst nach Einwilligung laden (Borlabs-Zuordnung prüfen) | Ladezeit, Rechtssicherheit | klein |
| A7 | Hintergrund-PNGs (5 Dateien, 1,8 MB) als WebP in Zielgröße, Hero-Video Handy auf 720 px und ≤ 400 KB, Poster-Bild, Video-Preload „none“ | LCP −1 s und mehr | mittel |
| A8 | WP Rocket: CSS/JS zusammenfassen und minifizieren, „JavaScript verzögert ausführen“ für Pixel, GTM, ProvenExpert, Lottie; LCP-Bild mit fetchpriority; nicht genutzte CSS entfernen testen | Anfragen von 110 auf unter 50, LCP unter 2,5 s | mittel |
| A9 | Startseite: Titel „Digitale Schließanlage für Unternehmen in Norddeutschland | ProVision Infra“ (nur SEO-Feld, kein Seitentext); Zutrittssystem-Seite: Titel um „Zutrittskontrolle“ ergänzen | Ortsbezug und passender Begriff ohne Textänderung | klein |

### Stufe B: 2 bis 8 Wochen, neue Seiten (Stoff vom Kunden)

| Nr. | Maßnahme | Hinweis |
|---|---|---|
| B1 | Regionalseiten je Metropole und Bundesland (Hamburg, Bremen, Hannover, Kiel/Schleswig-Holstein, Rostock/MV, Braunschweig/Wolfsburg, Oldenburg/Osnabrück) mit echten Inhalten: Projekte, Branchen vor Ort, Anfahrt und Servicezeiten, Ansprechpartner, Partner; keine Kopie der Ortsseiten-Vorlage | Grundlage für „ganz Norddeutschland“ |
| B2 | Bestehende 15 Ortsseiten entdoppeln: je Seite 30 bis 40 Prozent eigener Text (Projekt, Branche, Anfahrt), sonst Zusammenlegen auf Landkreis-Seiten erwägen | Doorway-Risiko senken |
| B3 | Ratgeber (ein Beitrag je zwei Wochen): „Elektronische Schließanlage: Kosten und Ablauf“, „Zutrittskontrolle und Betriebsrat“, „Videoüberwachung auf dem Firmengelände: was die DSGVO erlaubt“, „Schließanlage verloren: was jetzt“, „Kamerapflicht Schlachthof“ (vorhanden), „Schließsystem mieten oder kaufen“ | holt die überregionalen Suchen |
| B4 | Projektberichte mit Ortsnamen und Fotos (Freigabe der Kunden), verlinkt von Orts- und Leistungsseiten | lokale Relevanz, Vertrauen |
| B5 | Leistungsseite „Schlüsselnotdienst Baumann“ nur, wenn das Geschäft gewollt ist (eigenes Profil, eigener Begriff) | optional |

### Stufe C: laufend, Autorität

| Nr. | Maßnahme |
|---|---|
| C1 | Hersteller-Partnereinträge mit Link: EVVA (AirKey/Xesar-Partner), SimonsVoss, Nuki Pro, TP-Link VIGI, dormakaba, weitere |
| C2 | Verzeichnisse mit einheitlichen Firmendaten (NAP): Handwerkskammer, IHK, Gelbe Seiten, 11880, Das Örtliche, Cylex, Wer liefert was, Kununu, Bing Places, Apple Business Connect |
| C3 | Presse und Region: Landeszeitung Lüneburg, Allgemeine Zeitung Uelzen, Wirtschaftsförderung, Vereine und Sponsoring mit Link |
| C4 | Google-Bewertungen systematisch nach jedem Projekt (Link oder QR-Karte), Ziel 50+ Bewertungen mit Ortsnennung im Text |
| C5 | Monatlich: Search Console (Suchanfragen, Seiten, Links), Positionen für 20 Kernbegriffe je Region |

## 5. Offene Punkte, die nur der Kunde liefern kann

1. Search Console: Export „Leistung“ der letzten 3 Monate (Suchanfragen und Seiten als CSV) sowie Screenshots von
   „Seitenindexierung“ und „Links“; die automatische Anmeldung aus dieser Umgebung endet in einer Captcha-Abfrage.
2. Bildschirmfotos der Google-Ergebnisse vom eigenen Handy für „Schließanlagen Lüneburg“, „elektronische
   Schließanlage Uelzen“, „Videoüberwachung Unternehmen Hamburg“ (so erkenne ich die echten regionalen Wettbewerber).
3. Google Unternehmensprofil: Anzahl Bewertungen, Hauptkategorie und Zusatzkategorien, Einzugsgebiet, ob
   Leistungen und Produkte gepflegt sind.
4. Liste der Hersteller, bei denen ProVision zertifizierter Partner ist (für C1).
5. Drei bis fünf Projekte mit Freigabe für Projektberichte (Ort, Branche, Fotos), dazu Presse- und Vereinskontakte.
6. Freigaben: BugHerd entfernen; WP-Rocket-Einstellungen ändern; Product-Schema entfernen; Menü und Footer anpassen.
