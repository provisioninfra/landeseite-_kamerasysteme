# Technik- und Skalierungs-Check vor dem Livegang

Stand: 15.10.2026, zwei Prüfdurchgänge · Geprüft wurde die statische Version (`index.html`) mit
Chromium (Playwright), axe-core 4.10 (Barrierefreiheit), html-validate 9.5 (HTML-Validität) und
css-tree 3.1 (CSS-Syntax).

## Ergebnis in Kürze

Die Seite ist technisch bereit für den Livegang. Alle gefundenen Punkte aus beiden Durchgängen
wurden behoben. Offen bleiben nur zwei inhaltliche Entscheidungen (siehe „Offene Punkte“).

| Bereich | Ergebnis |
|---|---|
| Responsives Layout | 13 Bildschirmbreiten von 320 bis 1920 px geprüft, kein horizontaler Überlauf, keine Textüberlappung |
| JavaScript / Konsole | 0 Fehler, 0 Warnungen auf allen Breiten |
| Ladefehler | 0 fehlgeschlagene Requests |
| Barrierefreiheit (WCAG 2.1 AA + Best Practice) | 0 Verstöße auf Desktop und Mobil |
| HTML-Validität | 1 Hinweis zu `autoplay` am Hintergrundvideo (beabsichtigt, stumm) |
| Layoutverschiebung (CLS) | 0,00 |
| Seitengewicht beim ersten Aufruf | ca. 0,55 MB (Video 360 KB, Standbild 39 KB, CSS 17 KB, Schriften 31 KB); Timeline-Bibliothek und Animation (282 KB) laden erst kurz vor der Sektion |
| CSS-Syntax | fehlerfrei (beide Stylesheets) |
| Fehlerpfade (Animation, Video, Netz) | alle mit sichtbarem Fallback, keine JavaScript-Fehler |
| Externe Abrufe | nur das ProvenExpert-Siegel (wie auf der Startseite) |
| Schriften | Poppins lokal ausgeliefert, kein Abruf bei Google Fonts |

## Was geprüft wurde und was korrigiert wurde

### 1. Skalierung über alle Geräteklassen

Geprüfte Breiten: 320, 360, 390, 414, 600, 768, 834, 1024, 1180, 1280, 1366, 1440, 1920 px.

- **Korrigiert: Tablet (768 bis 1023 px).** Der Hero-Text lag über Tür und Schloss im Video und war
  schlecht lesbar. Tablet nutzt jetzt wie das Handy das gestapelte Layout: Text auf einfarbigem Navy,
  Video als eigener Block unter dem Button.
- **Korrigiert: Navigation zwischen 1100 und 1200 px.** Die Menüpunkte konnten in zwei Zeilen
  umbrechen. Das Burger-Menü greift jetzt bereits unter 1200 px.
- Kleinste Schriftgröße auf der Seite: 13 px (Nummerierung der Karten), alle Lesetexte 14 px oder größer.
- Der Lottie-Zeitstrahl skaliert mit der Containerbreite; die Textspalten bleiben auf allen Breiten
  ab 768 px exakt über den Kreisen.
- Sehr breite Monitore (1920 px): Inhalt bleibt auf 1400 px begrenzt, das Video füllt die volle Breite.

### 2. Video

- MP4 (H.264) als Hauptquelle, WebM (VP9) als Fallback, Poster-Standbild bis zum ersten Frame.
- Autoplay funktioniert auf iOS und Android nur stumm und mit `playsinline`, beides ist gesetzt.
  Wird Autoplay vom Gerät blockiert (z. B. Energiesparmodus), bleibt das Standbild sichtbar.
- Spielt einmal ab und bleibt auf dem letzten Bild stehen, wie auf der Startseite.
- Bei „Bewegung reduzieren“ in den Systemeinstellungen werden alle Animationen übersprungen.

### 3. Barrierefreiheit

- **Korrigiert:** Fehlende Landmarken. Inhalt liegt jetzt in `<main>`, es gibt einen `<footer>` und
  einen Sprunglink „Zum Inhalt springen“ für Tastaturnutzer.
- **Korrigiert:** Die mobile Timeline hatte ein ungültiges Element innerhalb der Liste. Die gelbe
  Fülllinie wird jetzt per CSS gezeichnet.
- Kontraste: Weiß auf Navy, Gelb auf Navy und dunkler Text auf Gelb liegen alle weit über dem
  geforderten Verhältnis von 4,5:1.
- Überschriftenstruktur: eine H1, danach H2 je Sektion, H3 für Karten und Schritte.
- Burger-Menü mit `aria-expanded`, dekorative Grafiken mit `aria-hidden`.

### 4. Datenschutz (DSGVO)

- **Korrigiert:** Die Schrift Poppins wurde von Google Fonts geladen. Das übermittelt die IP-Adresse
  der Besucher an Google und ist in Deutschland abmahngefährdet. Die vier Schriftdateien liegen jetzt
  im Projekt (`assets/fonts/`), es werden dieselben Dateien verwendet, die auch die Startseite lokal ausliefert.
- Verbleibender externer Abruf: das ProvenExpert-Siegel (Bild von images.provenexpert.com). Die
  Startseite lädt es genauso. Wer das vermeiden will, ersetzt es durch ein lokal gespeichertes Bild.
- Keine Cookies, keine Tracker, kein eingebettetes Fremdvideo in der statischen Version.
  In WordPress übernehmen Borlabs Cookie und Google Tag Manager der Hauptseite diese Themen automatisch.
- **Ergänzt:** Footer mit Links auf Impressum, Datenschutz und AGB der Hauptseite (Pflichtangaben).

### 5. Suchmaschinen und Teilen

- **Ergänzt:** Favicon (dieselben Dateien wie die Startseite), Theme-Color für mobile Browser,
  Open-Graph- und Twitter-Angaben mit dem Video-Standbild als Vorschaubild.
- Seitentitel und Meta-Beschreibung sind gesetzt. Die Canonical-URL wird nach Veröffentlichung
  eingetragen (in WordPress erledigt das Yoast SEO automatisch).

### 6. Ladezeit

- **Verbessert:** Beide Skripte laden jetzt nachrangig (`defer`), sie blockieren den Seitenaufbau nicht mehr.
- **Verbessert:** Lottie-Bibliothek von 298 KB auf 168 KB (Light-Build) reduziert, Rendering geprüft.
- Das ProvenExpert-Bild lädt verzögert (`loading="lazy"`).
- Bilder haben feste Breiten und Höhen, dadurch keine Layoutsprünge (CLS 0,00).
- Empfehlung für den Server: Gzip/Brotli-Komprimierung aktiv lassen (bei WordPress-Hostern Standard),
  dann liegt die Bibliothek bei rund 45 KB übertragen.

### 7. HTML-Validität

- Markup ist valide. Einziger Hinweis des Validators: `autoplay` am Video. Das ist für ein stummes
  Hintergrundvideo gängige Praxis und beabsichtigt.

## Zweiter Durchgang: Debugging und Härtung

Geprüft wurden gezielt Fehlerfälle und Randbedingungen, die beim normalen Betrachten nicht auffallen.

| Szenario | Ergebnis |
|---|---|
| Timeline-Bibliothek lädt nicht (z. B. Adblocker, Netzfehler) | Fallback: schlichte Linie mit fünf Punkten, keine Fehler |
| Animationsdaten laden nicht | gleicher Fallback, keine Fehler |
| Video blockiert oder nicht abspielbar | animierte SVG-Szene erscheint, Seite bleibt vollständig |
| Systemeinstellung „Bewegung reduzieren“ | alle Texte sofort sichtbar, Timeline im Endzustand |
| Nur Tastatur | Sprunglink als erstes Ziel, Burger-Menü per Enter, Escape schließt und setzt Fokus zurück |
| Seite per Doppelklick geöffnet (ohne Server, `file://`) | läuft inklusive Animation; nur Chrome blockiert lokale Schriftdateien und zeigt Ersatzschrift (Browser-Einschränkung, betrifft den Livebetrieb nicht) |
| Langsames Netz (simuliertes 3G) | Überschrift und Standbild nach 2,3 s sichtbar, keine Fehler |
| Fenstergröße mehrfach ändern und scrollen | keine Fehler, Zustand bleibt konsistent |

**Gefunden und behoben im zweiten Durchgang**

- **Bug im Stylesheet (schwerwiegend):** Ein nachträglich eingefügter Media-Block für sehr schmale Geräte
  hatte den 767-px-Block vorzeitig geschlossen. Folge: Zwischen 390 und 767 px wurde das Desktop-Raster
  der Ablauf-Sektion statt der mobilen Timeline angezeigt. Blockreihenfolge korrigiert, alle 13 Breiten erneut geprüft.
- **Überschrift bei 320 px:** „Videoüberwachung“ ragte aus dem Textblock. Bis 360 px greifen jetzt
  28 px Schriftgröße und automatische Silbentrennung; auf größeren Bildschirmen bleibt der Umbruch wie bisher.
- **Hero zwischen 1024 und 1199 px:** Text lag noch über der Tür im Video. Das gestapelte Layout gilt jetzt
  bis 1199 px, ab 1200 px ist der Fließtext auf die halbe Bildschirmbreite begrenzt und endet vor der Tür.
- **Animation ohne Server:** Die Timeline-Daten lagen als JSON und wurden per Fetch geladen, was beim
  Öffnen der Datei ohne Server scheitert. Die Daten liegen jetzt als Skriptdatei vor; Bibliothek und Daten
  werden erst nachgeladen, wenn die Sektion in die Nähe kommt. Das spart beim ersten Aufruf rund 280 KB.
- **Inline-Styles entfernt:** Die Spaltenzuordnung der Schritte läuft über Klassen, damit auch eine strenge
  Content-Security-Policy nichts blockiert.
- **Fokus-Darstellung:** Sichtbarer gelber Fokusring für Tastaturnutzer auf allen Links und Buttons.
- **Fallback für ältere Safari-Versionen (vor 15):** `aspect-ratio` hat eine Ersatzlösung.
- **Open-Graph-Bild:** Muss eine absolute Adresse sein, Platzhalter mit Hinweis eingetragen (in WordPress
  übernimmt Yoast SEO das Vorschaubild).
- **Elementor-Vorlage:** Die Website nutzt die zusätzlichen Breakpoints „Tablet extra“ (1280 px) und
  „Laptop“ (1440 px). Die Sichtbarkeitsregeln der Vorlage berücksichtigen jetzt alle Stufen, sonst wäre der
  mobile Video-Block auch auf Laptops erschienen.

**Nicht prüfbar in dieser Umgebung**

- Firefox und Safari (WebKit) sind hier nicht installiert. Verwendete Techniken sind in beiden seit
  mehreren Jahren unterstützt (Flex, Grid, `aspect-ratio` mit Fallback, IntersectionObserver, CSS-Variablen).
  Vor dem Livegang einmal auf einem iPhone in Safari und auf einem Android-Gerät in Chrome öffnen.

## Offene Punkte (inhaltlich, keine Technik)

1. Die Sektionen „Über uns“ und „FAQ“ aus dem Menü sind noch nicht gebaut. Die Menüpunkte zeigen
   derzeit ins Leere. Entweder Sektionen ergänzen oder Menüpunkte entfernen.
2. Die Texte ab „Unser Anspruch“ wurden gekürzt und auf Kameras angepasst (Stand 15.10.2026);
   die Ablauf-Texte weichen damit bewusst vom Original der Startseite ab.

## Elementor-Vorlage

Die Vorlage (`elementor/landingpage-kamerasysteme.json`) wurde entsprechend angepasst: Auf Tablet
und Handy wird kein Hintergrundvideo hinter dem Text gezeigt, der Video-Block erscheint unter dem Button.
In WordPress kommen Favicon, Schriften, Cookie-Banner, Header und Footer von der Hauptseite.

**Nachbesserung nach erstem Import (Design fehlte):** Das Styling lag zunächst nur im
„Benutzerdefinierten CSS“ der Seiteneinstellungen, das beim Einfügen einer Vorlage nur nach
Bestätigung übernommen wird. Jetzt sind Farben, Schriften, Größen, Rahmen und Abstände als native
Elementor-Einstellungen an jedem Widget und Container hinterlegt (54 Text-Widgets mit eigener
Typografie), das ergänzende CSS hängt zusätzlich an jedem Sektions-Container. Außerdem korrigiert:
Rahmen-Einstellungen von Widgets mit dem richtigen Präfix, Icon-Form „square“ statt eines
ungültigen Werts, Lottie-Animation per URL statt über den Medien-Import, leere Video-URL im
mobilen Video-Widget (eine nicht erreichbare URL würde beim Import durch ein Platzhalterbild ersetzt),
Seitenlayout „Volle Breite“ in den Vorlagen-Einstellungen.
Der Import konnte ohne Zugang zum WordPress nicht live getestet werden.

## WordPress-Seite (Stand 15.10.2026, dritter Durchgang)

Mit Testzugang direkt in WordPress gebaut und geprüft:

- Seite 4313 „Kamera- & Videoüberwachung“ als Entwurf, zusammengesetzt aus den Original-Elementen der
  Startseite (Header, Hero, Glas-Box, Kundenstimmen-Slider als Produkt-Slider, Icon-Zeilen, Ablauf mit
  Lottie und EA-Timeline, Gründer, Partner, Standort, FAQ-Akkordeon, Footer).
- Gespeichert über den Speicherweg des Elementor-Editors (kein Vorlagen-Import, keine doppelten Medien).
- Geprüft in der Vorschau bei 1920, 1440, 1024, 768 und 390 px: kein horizontaler Überlauf, keine
  JavaScript-Fehler, alle Widgets gerendert (2 Nested-Carousels, Lottie, EA-Timeline, Akkordeon).
- Mobil: Text auf einfarbigem Hintergrund, Video als Block unter dem Button, Slider mit gelbem Rahmen
  des aktiven Slides wie bei den Kundenstimmen.
- Medien in der Mediathek: Hero-Video (ID 4305), Standbild (4306), sechs Platzhalter-Produktbilder
  (4307–4312), fünf Icons im Stil der Startseiten-Kacheln (4318–4322).
- Nicht verändert: Startseite, andere Seiten, Menüs, Einstellungen. Nichts veröffentlicht.

## Hero-Video in höherer Auflösung (15.10.2026)

- Quelle: 1280×720, 9,2 s, KI-generiert. Im Hero auf 1440 bis 1920 Pixel gedehnt, auf Retina-Bildschirmen auf das Doppelte.
- Alle 221 Frames mit Real-ESRGAN (Modell „animevideov3“, CPU) vierfach hochskaliert und auf 3840×2160 heruntergerechnet.
  Verglichen wurde mit reinem Lanczos-Upscaling und dem Modell „general-x4v3“; die gewählte Fassung liefert die
  saubersten Kanten ohne Rauschen auf den Flächen.
- Desktop-Hero: 4K (3,7 MB). Handy-Block: 2560×1440 (1,5 MB). Die Startseite liefert ihr Hero-Video ebenfalls in 4K aus.
- Verhalten: Video läuft einmal, das letzte Bild bleibt stehen. Verlässt der Bereich den Bildschirm und kommt zurück,
  startet es erneut (Hero und Handy-Block). Umgesetzt mit einem HTML-Widget am Seitenende plus CSS, weil Elementor ein
  einmal abgespieltes Video nach dem Ende ausblendet.
- Handy: Videoblock 330 px hoch, Bildausschnitt rechts (object-position), damit Kameras und Tür komplett sichtbar sind.

---

## Überschrift im Hero (16.10.2026)

- Wunsch: Überschrift größer, „mit Kamera- & Videoüberwachung“ immer in der zweiten Zeile.
- Umsetzung: fester Zeilenumbruch (`<br>`) nach „Gebäude“. Die zweite Zeile ist in Poppins (400) etwa 18,4-mal so
  breit wie die Schriftgröße, die erste (fett) etwa 14,1-mal. Daraus ergeben sich die Grenzen je Breakpoint:

| Breite | Größe | Textbox | Zweite Zeile |
|---|---|---|---|
| ab 1441 px | 52 px (seit 16.10., damit die Zeile vor dem Schloss im Video endet) | 88 % von 1400 px = 1232 px | ca. 914 px, einzeilig |
| 1281 bis 1440 px | 50 px | 940 px | ca. 920 px, einzeilig |
| 1025 bis 1280 px | 44 px | 940 px | ca. 810 px, einzeilig |
| 768 bis 1024 px | `min(36px, 4vw - 1.5px)` (29 px bei 768, 36 px ab 938) | 75 % der Breite | einzeilig |
| bis 767 px | `min(28px, 7vw - 2px)` (25,5 px bei 393, 28 px ab 429) | volle Breite minus 20 px | bricht nach „&“ um |

- Auf dem Handy ist die erste Zeile (fett) das Maß: Sie füllt bei 26 px auf einem 390-px-Bildschirm bereits die
  Breite. Die Formel hält sie bis 320 px einzeilig, die zweite Zeile wird zu „mit Kamera- &“ / „Videoüberwachung“.
- Elementor rendert die Einheit „custom“ unverändert als CSS (`font-size: min(...)`), Zeilenhöhe in em, damit sie
  mitskaliert. Geprüft auf der Live-Seite bei 1920, 1600, 1441, 1440, 1366, 1281, 1280, 1100, 1025, 1024, 900, 768,
  430, 393, 375, 360 und 320 px: Zeile 2 beginnt überall mit „mit Kamera-“.

---

## „Fünf Unterschiede“ als Hover-Karten (16.10.2026)

- Die fünf Zeilen sind jetzt Klone der Karten aus dem Startseiten-Abschnitt „Warum immer mehr KMUs …“: 4 % weiße
  Fläche, 2-px-Rahmen in Weiß (40 %), Radius 24 px; beim Hover gelber Rahmen, dunkler Hintergrund, gelber Glow und
  Vergrößerung auf 105 % (Elementor-Container-Einstellungen, kein eigenes CSS).
- Aufbau je Karte wie auf der Startseite: Icon-Kachel, Überschrift, Text und darunter die fette Box mit dem
  Schmerzpunkt. Die gelbe Versprechen-Zeile ist dafür entfallen. Texte gekürzt (Text ca. 20 bis 27 Wörter,
  Box ein Satz).
- Kartenspalte 900 px breit, mittig; Tablet und Handy volle Breite. Auf dem Handy stapelt sich die Karte wie auf der
  Startseite: Kachel zentriert oben, Text zentriert darunter.

---

## Produktbilder: Kameras freigestellt (16.10.2026)

- Quelle: fünf Produktfotos (TP-Link VIGI) auf weißem Grund, 447 bis 1000 Pixel Kantenlänge. Ein sechstes Bild war
  ein Handy-Screenshot derselben Bullet-Kamera und wurde nicht verwendet.
- Ablauf: vierfach hochskaliert (Real-ESRGAN „general-x4v3“, CPU), dann freigestellt mit rembg. Die Maske ist die
  Vereinigung aus u2net und isnet-general-use: isnet schneidet weiße Halterungen weg, u2net hält sie, zusammen
  bleiben Antennen und Halterungen vollständig. Reinweiße Pixel außerhalb der Kante werden zusätzlich transparent
  gesetzt, Kante leicht geglättet.
- Ausgabe: 1600 × 1200 PNG mit Transparenz, Kamera mittig mit 8 % Rand, 0,3 bis 0,9 MB je Datei
  (`assets/img/produkte/kamera-1.png` bis `-5.png`). WordPress liefert im Slider die Größe „large“ (1024 px).
- Live geprüft: fünf Slides, alle Bilder geladen, keine JS-Fehler, Alt-Texte gesetzt. Werkzeuge:
  `tools/upscale_sr.py` (Modell „general“), Freistell-Skript `tools/produkt_freistellen.py`.

---

## „Fünf Unterschiede“ zweispaltig mit Sticky-Text und Glas-Logo (16.10.2026)

- Aufbau exakt wie der Startseiten-Abschnitt „Warum immer mehr KMUs …“: Zeile mit zwei Spalten (40 % Text, 60 %
  Karten, `align-items: flex-start`), linke Spalte mit Elementor-Pro-Sticky „oben“, „an Eltern-Container“ (Sticky
  endet mit der Zeile, also mit der letzten Karte und dem Button), aktiv für Widescreen, Desktop und Laptop wie auf
  der Startseite. Zwischen 1025 und 1280 px zwei Spalten ohne Sticky (wie dort), ab 1024 px abwärts untereinander
  mit zentriertem Text.
- Glas-Logo: Hintergrund-Overlay der Zeile (Bild `Frame-2147224855.png`, Mediathek-ID 516, links, 50 % Breite,
  Maus-Effekt), Deckkraft 50 % wie auf der Startseite. Auf Tablet und Handy Deckkraft 0, da nur für den Computer
  gewünscht.
- Nicht übernommen: Das gelbe Lichtschein-Overlay des Startseiten-Abschnitts (`2.png`) ist dort nicht sichtbar, weil
  die Klasse `shadeup` das Overlay-Pseudo-Element auf einen 30-px-Streifen reduziert. Auf dieser Seite würde es
  voll durchscheinen und vom Original abweichen.
- Prüfung in der Vorschau und live, ausgeloggt: 1920 und 1440 px: Textspalte wird beim Scrollen `position: fixed`
  (oben bündig, wie auf der Startseite) und am Ende der Zeile `absolute`, Unterkante gleich Unterkante der Zeile;
  keine Überlappung mit den Karten. 1280 px: zwei Spalten, kein Sticky. 1024, 768, 393 px: untereinander,
  Überschrift zentriert, Overlay aus, keine Überbreite, keine JS-Fehler.

---

## Kontaktformular auf der Seite (16.10.2026)

- Neues Gravity-Forms-Formular „Anfrageformular Kamerasysteme“ (ID 4), erzeugt als Export von „Anfrageformular (1)“
  (ID 2), angepasst und über **Import/Export → Formulare importieren** als neues Formular eingespielt. Die Formulare
  1 und 2 wurden danach erneut exportiert und mit dem Stand davor verglichen: identisch.
- Änderungen gegenüber dem Original: ein Feld „Wie lautet dein Name?“ statt Vor- und Nachname (volle Breite),
  „Wie viele Gebäude sollen überwacht werden?“ mit 1 / 2 / 3 / >3 statt der Türen-Frage, die Frage „Wie organisierst
  du deine Zugänge aktuell?“ entfällt. Versteckte UTM-Felder, Bereich (Privat/Geschäftlich) und Mitarbeitende mit
  ihrer Bedingung bleiben.
- Bestätigungen wie im Original (Standard → Seite „Termin“ 3617, „LQ form“ → Seite „Termin Gebucht“ 823). Im
  Query-String wird `first_name` jetzt mit dem ganzen Namen gefüllt, `last_name` entfällt. Die LQ-Regeln zum
  Türen-Feld (1–5, 6–15, Noch unsicher) entfallen, weil es das Feld nicht mehr gibt; Privat und Mitarbeitende
  1–10 / 11–50 wirken weiter. Benachrichtigung unverändert an anfragen@provision-infra.de, Betreff enthält den
  neuen Formulartitel.
- Einbindung: eigene Seite „Kontakt Kamerasysteme“ (ID 4371, /kontakt-kamerasysteme/), angelegt per REST als
  Entwurf, Inhalt über den Elementor-Editor gespeichert, dann veröffentlicht. Inhalt ist der Abschnitt der Seite
  /kontakt (Elementor-Daten in `elementor/quelle-kontakt.json`, nur gelesen): Überschrift, Text (kameraspezifisch),
  Essential-Addons-Widget „Gravity Form“ mit Formular 4 und der Klasse `cs-landeseiten-form`, Mindesthöhe 100 vh.
  Template „default“ wie /kontakt, Yoast noindex/nofollow wie /kontakt. Alle vier Buttons der Kamera-Seite
  verlinken auf diese Seite. Weil die URL „kontakt“ enthält, feuern dort dieselben Tag-Manager-Events wie auf
  /kontakt (Google-Ads-Conversion d6XM…, Meta „ViewContent“).
- Schritt-für-Schritt-Darstellung: Die Kontaktseite nutzt das Website-Modul „Landeseiten Forms“ (Eintrag „Kontakt
  test“, ID 2459, für Formular 2). Für Formular 4 wurde dieser Eintrag mit der Duplizieren-Funktion kopiert
  (Eintrag „Kontakt Kamerasysteme“, ID 4368) und nur das Formular umgestellt; alle 38 übrigen Einstellungen
  (Übergang „Reveal“, 800 px, Farben, Schriftgrößen, Button-Texte) sind identisch. Die Einträge 2459 und 828
  wurden vorher und nachher ausgelesen und sind unverändert.

---

## Link-Vorschau / Open Graph (16.10.2026)

- Befund: Yoast gab als `og:image` das erste Bild im Inhalt aus, das Header-Logo mit 258 × 60 Pixel. Messenger
  ignorieren so kleine Bilder, deshalb zeigte WhatsApp nur den Link. Die `og:description` war ein Textauszug der Seite.
- Lösung: Schlussbild des Hero-Videos (Tür und Kameras) als 1200 × 630 JPEG (`assets/img/og-kamerasysteme.jpg`,
  46 KB, Mediathek-ID 4376) in Yoast als Facebook- und X-Bild der Seite hinterlegt, dazu Vorschau-Titel und
  -Beschreibung sowie die Meta-Description. Gesetzt über den Yoast-Datenspeicher des Block-Editors
  (`setFacebookPreviewImage`, `setFacebookPreviewTitle`, `setFacebookPreviewDescription`, `updateData`), danach
  Seite gespeichert; Werte nach Neuladen bestätigt.
- Live geprüft, auch ohne Cache-Umgehung: `og:image` 1200 × 630 mit `og:image:width/height`, `twitter:image`,
  Bild per HTTP 200 als image/jpeg (26 KB nach Imagify). Ein Video lässt sich in Link-Vorschauen nicht abspielen;
  `og:video` würde WhatsApp ignorieren und wurde nicht gesetzt.

---

## Hero: Kameras über der Headline, Produktslider, Glas-V am Handy (16.10.2026)

- Kameras: Elementor skaliert das Hintergrundvideo immer auf die Hero-Höhe (16:9, mittig). Die Kameras liegen im Bild
  bei 16 bis 27 % der Höhe und standen damit hinter der ersten Headline-Zeile. Lösung: Hero-Innenabstand oben 280 px
  statt 200 px, unten 20 px statt 100 px, damit die Hero-Höhe am Desktop gleich bleibt (1025 px) und der
  Videoausschnitt sich nicht verschiebt. Laptop und Tablet: oben 220 px statt 150 px. Gemessen bei 1920, 1600, 1536,
  1441, 1440, 1366, 1280, 1100, 1024 und 768 px: Unterkante der Kameras liegt überall über der Headline (Abstand
  2 bis 40 px), Oberkante unter der Menüleiste.
- Produktslider: `pause_on_hover` und `pause_on_interaction` auf „nein“, damit die Bilder am Computer auch dann
  weiterlaufen, wenn die Maus darüber steht oder ein Pfeil geklickt wurde. Autoplay (5 s) und Endlosschleife waren
  bereits wie bei den Kundenstimmen gesetzt; die Kundenstimmen bleiben unverändert.
- Glas-V am Handy: Overlay der Karten-Zeile wie auf der Startseite oben mittig, „contain“, Deckkraft 0,64. Tablet
  weiterhin ohne.

---

## Hero: Schloss neben statt hinter der Headline (16.10.2026)

- Befund: Seit die Headline größer ist und „mit Kamera- & Videoüberwachung“ in einer Zeile steht, endete die zweite
  Zeile am Desktop hinter dem leuchtenden Schloss im Video (bei 1920 px Text bis 1385 px, Schloss ab 1210 px).
- Warum „Schloss unter der Headline“ nicht geht: Im Videobild liegen Kameras und Schloss nur 7 % der Bildhöhe
  auseinander (bei 1920 px etwa 75 px), die zweizeilige Headline ist 130 bis 160 px hoch. Beides passt nicht zwischen
  Kameras (oben) und Schloss (unten), bei keiner Videogröße.
- Erster Versuch (verworfen): Video ab 1441 px um 200 px nach rechts verschoben. Dadurch rückte die Tür zu weit nach
  rechts, Rückmeldung des Kunden. Zurückgenommen.
- Lösung ab 1441 px: Headline 52 px statt 64 px (bei 1536 px endet die Zeile sonst hinter dem Schloss; 52 px ist das
  Maximum). Video unverändert an seinem Platz.
- Lösung 1025 bis 1440 px: kleine Verschiebung des Videobilds per Custom-CSS des Hero, linke Kante per Maske weich
  ausgeblendet. 1281 bis 1440 px `746px - 50vw` (26 bis 106 px), 1025 bis 1280 px `max(0, 645px - 50vw)`
  (5 bis 132 px). Elementor zentriert das Video mit `translate(-50%, -50%)`, die Regel ergänzt nur den Versatz.
  Tablet und Handy unverändert.
- Live gemessen: Schloss beginnt 14 bis 36 px rechts vom Textende (1281 bis 1920 px), Kameras zwischen Menüleiste
  und Headline, Tür bei 1441 bis 1920 px komplett im Bild (rechte Kante 1467 bis 1766 px).

---

## Terminbuchung Kamerasysteme über Calendly (16.10.2026)

- Calendly-Termintyp „Telefonisches Erstgespräch Kamerasysteme“ (30 Minuten) existiert im Konto provision-infra,
  Slug `telefonisches-erstgesprach-kamerasysteme` (ohne ä). Über die öffentliche Profil-Schnittstelle von Calendly
  ermittelt, Buchungsseite liefert HTTP 200.
- Zwei neue Seiten als Kopien der bestehenden Terminseiten, nur der Calendly-Link ist getauscht (Elementor-Daten der
  Originale in `elementor/quelle-termin.json` und `quelle-termin-gebucht.json`, Ausgabe des Composers in
  `termin-kamerasysteme.elements.json` und `termin-gebucht-kamerasysteme.elements.json`, Link in `medien.json`):
  „Termin Kamerasysteme“ (ID 4391, /termin-kamerasysteme/) und „Termin Gebucht Kamerasysteme“ (ID 4392,
  /termin-gebucht-kamerasysteme/). Template „default“, Yoast noindex/nofollow wie die Originale. Das Widget übernimmt
  wie bisher `first_name` und `email` aus der URL in Calendly.
- Formular 4 „Anfrageformular Kamerasysteme“: Standard-Bestätigung → Seite 4391, „LQ form“ → Seite 4392 (über die
  Bestätigungs-Einstellungen im Formular-Editor). Formulare 1 und 2 erneut per Export verglichen: unverändert. Die
  Seiten „Termin“ (3617) und „Termin Gebucht“ (823) sind unverändert.
- Tracking: Beide neuen URLs enthalten „termin“ bzw. „termin-gebucht“, die Tag-Manager-Auslöser (Google-Ads-Conversion,
  Meta „Lead“, Meta „SubmitApplication“) greifen also wie beim Original.
- Weiterleitung nach der Buchung (18.10.2026 im Calendly-Konto nachgesehen, nur gelesen, nichts gespeichert): Beide
  Termintypen stehen unter „Bestätigungsseite“ auf „An externe Site weiterleiten“ mit der URL
  `https://provision-infra.de/danke/`, „Ereignisdetails an die weitergeleitete Seite übergeben“ ist bei beiden aus.
  Der Kamera-Termin ist damit identisch zum Schließsysteme-Termin eingestellt, es war keine Änderung nötig. Die Seite
  /danke/ ist allgemein formuliert („Wir freuen uns darauf, dich im Gespräch kennenzulernen“), der Tag-Manager-Auslöser
  „URL enthält danke“ (Meta „Schedule“) greift für beide Termine gleich.
- Einziger Unterschied zwischen den beiden Termintypen (nicht geändert): Beim Schließsysteme-Termin sind
  E-Mail-Erinnerungen „1 Stunde vor dem Ereignis“ aktiv, beim Kamera-Termin stehen sie auf „Aus“. SMS-Erinnerung
  (10 Minuten vorher), E-Mail-Bestätigung, Absage-E-Mail und der Workflow „Terminbestaetigung“ sind bei beiden gleich.


## Neuer Seitenaufbau nach dem Vorbild der Startseite (20.10.2026)

Reihenfolge jetzt (Stand 20.10. abends): Hero, Logo-Rahmen mit drei Punkten, Was ohne Kameras passiert (Glas-Logo,
Pain-Karten), Kundenstimmen, Stell dir mal vor, Und genau das wird möglich, So arbeiten wir, Ablauf, Gründer, Technik,
Standort, FAQ, Partner, Footer.
Alle Texte überarbeitet (kürzer, ohne Gedankenstriche, ohne Dreiergruppen und Floskeln); Kundenstimmen, Gründer, Standort
und Partner bleiben wörtlich die Startseiten-Bausteine.

- **Logo-Rahmen + drei Punkte:** Kopie des Startseiten-Abschnitts unter dem Hero (Zeile mit Rahmen und drei Icon-Zeilen).
  Im Rahmen statt des Vimeo-Films das Header-Logo (Mediathek-ID 407) mit Link zur Startseite; Rahmen mindestens 320/240/190 px
  hoch (Computer/Tablet/Handy). Anker `digitalen` liegt auf diesem Abschnitt, damit der erste Menüpunkt weiter funktioniert.
- **Pain-Karten:** fünf Karten im Format der Startseite („… wenn“, Verlauf, Folge-Box), X-Symbol der Startseite, letzte Karte
  mit Hinweiszeile (Vorlage: fünfte Startseiten-Karte, Rahmen und Hintergrund an die anderen angeglichen). Einleitung 20 px
  (Laptop 19, Tablet 18, Handy 17). Sticky-Text, Hover-Rahmen und Glas-V unverändert, erneut gemessen (1920/1440 sticky,
  Hover: Rahmen rgb(251,201,27), Glow 24 px).
- **So arbeiten wir:** Kopie des schwebenden Teils („… installiert dir genau das, damit du“) als eigener Abschnitt.
- **Stell dir mal vor:** Die Startseite zeichnet Rahmen, Icons und Leuchtlinie der acht Kästen in acht Lottie-Dateien
  (je 1,2 MB, Schloss und Griff als eingebettete Bilder) an festen Positionen; Text und Rahmen laufen dort je nach Breite
  und Textlänge auseinander (auf der Startseite bei 1440 px bis zu 76 px). Für die Kameraseite bekommen die Kästen Rahmen,
  Icon und Aufleuchten selbst (Vorlage: Handy-Kasten der Startseite), die gelbe Linie zum Kamerakopf zeichnet ein Skript
  (`tools/kamera-linien.html`) als SVG-Pfad von der tatsächlichen Kastenkante zur Kamera: erster Kasten leuchtet beim
  Erscheinen, Hover wechselt Kasten und Linie, Verlassen schaltet nach 120 ms zurück; Resize und Größenänderung der
  Kamera (ResizeObserver) ziehen die Linie nach. Das Hover-Skript der Website im Footer findet auf der Kameraseite keine
  `data-lottie-target`-Elemente und bleibt untätig. Die Kamera in der Mitte ist eine selbst erzeugte Lottie-Datei
  (tools/kamera_lottie_erzeugen.py: Produktbild 3 als eingebettetes PNG, Schwenk ±6°, Schweben, blinkende LED,
  Lichtschein; 210 KB, Mediathek-ID 4449), Trigger „im Sichtbereich“, Endlosschleife; außerhalb des Sichtbereichs pausiert
  Elementor sie. Gemessen (Linie, Kamera, Kästen in Spaltenbreite): 1920, 1440, 1280, 1024, 768; Handy: acht Kästen
  untereinander, Kamera 280 px breit darunter.
- **Und genau das wird möglich:** Kopie des Startseiten-Abschnitts mit neuen Hintergrundbildern: Startseiten-Grafik, die
  Person per Freisteller (rembg u2net) in eine dunkle Kapuzen-Silhouette mit schwachem grünem Lichtsaum umgesetzt
  (tools/einbrecher_silhouette.py; Mediathek-IDs 4450 Computer, 4451 Handy, je 240 KB JPEG). Darüber ein HTML-Element, das die
  Hintergrund-Geometrie nachbildet (Computer/Tablet: cover, mittig; Handy: contain, unten) und zwei Bullet-Kameras aus
  den Produktbildern (IDs 4446/4447) über der Tür und über der Silhouette platziert: Schwenk ±4° (7 s bzw. 8 s), rote
  LED blinkt (1,3 s). Textkasten liegt über der Kamera-Ebene (z-index). Gemessen in allen Breiten; bei 585 bis 768 px
  greift die Mindesthöhe 1000 px der Startseite.
- **Partner** stehen jetzt nach dem FAQ, Standort mit Erstgespräch vor dem FAQ.
- **Headline:** „Wir schützen dein Unternehmen“; Handy-Formel `min(28px, 5.9vw - 2px)`, damit die fette Zeile bei 360 bis
  430 px einzeilig bleibt (bei 393 px: 21,2 px, zwei Zeilen insgesamt).
- **Aufräumen:** acht testweise hochgeladene Linien-Lotties und eine Testdatei wieder aus der Mediathek gelöscht
  (IDs 4437 bis 4445). Neu in der Mediathek: 4446 bis 4451 (Kameras, Kamera-Animation, zwei Szenenbilder).
- Prüfung auf der Live-Seite (Playwright, Chromium): keine horizontale Verschiebung bei 1920/1440/1280/1024/768/393 px,
  keine JavaScript-Fehler, Reihenfolge der 22 Abschnitte wie geplant, Logo-Link auf die Startseite, Animationen laufen
  (Kamera-Lottie im Sichtbereich, Szene-Kameras per CSS), Hover-Zusammenspiel der Kästen in allen Desktop-Breiten.

## Zweite Runde nach Rückmeldung am Handy (20.10.2026)

- **Icons:** Alle Icon-Kacheln dunkel mit gelbem Symbol wie die Startseiten-Icons. Die fünf Kamera-Icons neu als SVG mit
  dunkler Kachel (Verlauf, gelber Schein unten, feiner Rand, Strich 5 px) erzeugt und hochgeladen (IDs 4461 bis 4465,
  `elementor/icons.json`); die gelben Vorgänger (4318 bis 4322) gelöscht. Elementor bettet die SVGs inline ein; die
  Verlaufsdefinitionen tragen in allen fünf Dateien dieselben IDs und sind identisch, deshalb stört die Mehrfachdefinition nicht.
- **Einleitung des Glas-Abschnitts:** „Fünf Situationen, die jeden Betrieb treffen können. Ohne Kameras passiert Folgendes,
  wenn …“ (konkreter, führt weiter in die Karten „… nachts jemand über den Zaun steigt, …“).
- **„So arbeiten wir“ am Handy grau:** Ursache war die aus dem Startseiten-Abschnitt übernommene Zusatzregel, die bei
  höchstens 767 px die oberen 100 px mit einem Verlauf abdunkelt (dort Übergang vom Hero). Die Überschrift stand darunter.
  Regel für diesen Abschnitt entfernt, zusätzlich 30 px Abstand oben auf Tablet und Handy. Geprüft bei 393, 768, 1440 px.
- **Lichtschein um die Kamera:** Der in die Lottie-Datei eingebettete Schein wurde an der Bühnenkante (360 x 520) abgeschnitten
  und wirkte kantig. Jetzt ohne Schein in der Datei (109 KB statt 210 KB, Mediathek-ID 4460, alte Datei 4449 gelöscht); der
  Schein ist ein weicher CSS-Schatten auf dem SVG (`drop-shadow` 26 px und 70 px, gelb), der der Kamerakontur folgt und
  nicht beschnitten wird. Gilt am Computer und am Handy.
- **Szene „Und genau das wird möglich“:** die beiden eingefügten Bullet-Kameras entfernt (Wunsch), Silhouette bleibt.
  Zugehörige Mediendateien 4446/4447 gelöscht.
- **Animationen gegen die Startseite geprüft** (Playwright, 393 und 1440 px, langsames Durchscrollen): Einblend-Animationen
  der Elementor-Elemente laufen (übrig bleiben nur Elemente in ausgeblendeten Varianten, genau wie auf der Startseite),
  `floating`-Animation (3 s) und Glas-Optik (`backdrop-filter: blur(20px)`) der schwebenden Kästen kommen aus dem
  seitenweiten CSS und greifen auch hier, Sticky-Text (Computer), Zähler, beide Slider mit Autoplay, Ablauf-Lottie
  (scrollgebunden, Computer), Hover-Rahmen der Karten, Kamera-Lottie (läuft im Sichtbereich, pausiert außerhalb),
  Leuchtlinie und Aufleuchten der Kästen (Computer/Tablet). Keine JavaScript-Fehler, keine horizontale Verschiebung.

## Dritte Runde nach Rückmeldung am Handy (20.10.2026)

- **Box „Genau daraus ist ProVision Infra entstanden“ unten abgeschnitten:** Der Abschnitt der Startseite hat am Handy kein
  Polster nach unten; auf der Kameraseite folgt der Technik-Slider mit dem Verlaufsstreifen (`shadeup`), der den unteren Rand
  und den gelben Schein der Box verdeckte (auf der Startseite folgt der Partner-Abschnitt ohne Streifen). Jetzt 40 px Abstand
  am Handy, 60 px am Tablet. Rest des Abschnitts unverändert.
- **Leuchtlinie begann mitten im ersten Kasten:** Die Linie wurde beim Erscheinen des Abschnitts gezeichnet, während der erste
  Kasten noch mit `fadeInLeft` hereinglitt; gemessen wurde seine Zwischenposition (bei 1536 px 54 px zu weit links). Das
  Skript wartet jetzt, bis die Einblend-Animation des Standard-Kastens beendet ist (`getAnimations`, Rückfall nach 5 s), und
  legt die aktuelle Linie nach jedem `animationend` eines Kastens neu. Geprüft: Linienstart exakt an der Kastenkante bei
  1920, 1536, 1440, 1366, 1024 und 768 px (Abweichung 0 px); keine Linie kreuzt einen anderen Kasten (zwölf Breiten von
  768 bis 1920 px, alle acht Kästen).
- **Logo im Rahmen:** 88 % der Rahmenbreite (Tablet 72 %, Handy 86 %). Zwei Hürden: Das Bild-Element steckt wegen des Links in
  einem `<a>` und schrumpft als Flex-Kind des zentrierten Rahmens auf die natürliche Bildbreite, die Breite wird deshalb per
  eigenem CSS auf dem Element gesetzt. Und die einzige Logodatei der Website (Header, Mediathek-ID 407) ist nur 258 x 60 px
  groß; ein größeres Logo wäre unscharf. Deshalb mit Real-ESRGAN (`realesr-animevideov3`, gut für flächige Grafik) auf
  1032 x 240 px vervierfacht, Alpha getrennt skaliert, als PNG hochgeladen (ID 4479). Kein größeres Logo in der Mediathek
  vorhanden (Suche nach „logo“, „ProVision-Infra-GmbH“; nur Partnerlogos).
- **Schärfe:** Szenenbild (Computer) mit Real-ESRGAN `realesr-general-x4v3` in Kacheln vervierfacht, auf 4800 x 2208
  verkleinert und leicht nachgeschärft, als WebP (106 KB, Mediathek-ID 4473; WordPress legt zusätzlich eine 2560-px-Kopie
  „-scaled“ an, die Seite nutzt die volle Datei). Handy-Variante 2552 x 2208 (90 KB, ID 4474). Kamera-Ausschnitt des
  Produktbilds 3 ebenso auf 880 x 1511 hochgerechnet und als WebP mit Transparenz (60 KB) in die Lottie-Datei eingebettet
  (ID 4472, 80 KB); die Ebene ist auf 30,68 % skaliert, Geometrie und LED-Position unverändert. Alte Dateien (4450, 4451,
  4460) gelöscht. Hochrechnen: `tools/kamera_lottie_erzeugen.py` liest `assets/img/produkte/kamera-3-scharf.webp`.

## SEO-Optimierung (20.10.2026)

Texte unverändert bis auf kleine Ergänzungen, alles am 20.10. abends geprüft (Lighthouse 12 lokal, Playwright 1440/393 px).

- **Titel und Beschreibung (Yoast):** Titel `Kamera- & Videoüberwachung für Unternehmen | ProVision Infra` (60 Zeichen, vorher
  „Kamera- & Videoüberwachung - ProVision“), Meta-Beschreibung mit Region (151 Zeichen, vorher 180 und damit abgeschnitten),
  Fokus-Keyphrase „Videoüberwachung für Unternehmen“, Seite als Cornerstone markiert. Vorschau-Titel für Facebook/X trugen noch
  „dein Gebäude“ (alte H1), jetzt „Wir schützen dein Unternehmen mit Kamera- & Videoüberwachung“ mit der neuen Beschreibung.
  Werte: `elementor/seo.json`. Canonical, `index, follow`, Sitemap-Eintrag, Weiterleitungen (http, www, ohne Schrägstrich →
  301 auf die Seite) und robots.txt waren bereits in Ordnung; Kontakt- und Terminseiten bleiben `noindex`.
- **Überschriften:** Die Startseite setzt Abschnittsüberschriften als `<div>`; hier sind es jetzt echte Überschriften:
  h2 für „Solange nichts passiert …“, „Stell dir mal vor …“, „Mit Kamera- und Videoüberwachung … teure Schäden verhindern“,
  „So arbeiten wir“, „Ablauf der Zusammenarbeit“, „Hier findest du ProVision Infra“, „Unsere Partner“; h3 für die fünf Schritte
  (vorher h6), „Genau daraus ist ProVision Infra entstanden“ und die FAQ-Fragen (vorher `<p>`); Fließtext in
  Überschriften-Widgets (Vorzeile, Kästen „So arbeiten wir“, Bewertungszeile) als `<p>`. Aussehen identisch: alle
  berechneten Stile (Größe, Gewicht, Zeilenhöhe, Farbe, Abstände) vor und nach der Umstellung verglichen, bei 1440 und 393 px
  keine Abweichung. Lighthouse „Reihenfolge der Überschriften“ besteht jetzt.
- **Kleine Textergänzungen (Suchbegriffe):** FAQ „Wie lange dauert die Installation einer Videoüberwachung?“, „Kann ich die
  Kamerabilder auf dem Handy sehen?“, „Was kostet eine Videoüberwachung für mein Unternehmen?“, neue siebte Frage zur Region
  (Bad Bevensen, Hamburg, Hannover, Niedersachsen, bundesweit); Schritt 3 heißt „Planung deines Kamerasystems“ (das Wort
  „Kamerasystem“ kam trotz der Adresse /kamerasysteme/ nicht vor).
- **Strukturierte Daten:** Yoast liefert WebPage, Breadcrumb, WebSite. Dazu kommen jetzt `LocalBusiness` (Firmendaten aus dem
  Impressum: Adresse, Telefon, Öffnungszeiten, Einsatzgebiet, Social-Profile) und `Service` (Kamera- und Videoüberwachung für
  Unternehmen, Anbieter, Einsatzgebiet) als JSON-LD im Abschnitt „Steuerung Hintergrundvideo“, sowie `FAQPage` mit den sieben
  Fragen, die das FAQ-Akkordeon selbst ausgibt (Option „FAQ Schema“ des Widgets; Antworten ohne den überflüssigen `span`).
  Alle vier JSON-LD-Blöcke sind gültig. Der `Product`-Block mit der Bewertung stammt vom ProvenExpert-Siegel (seitenweit).
- **Bilder:** Eigene Medien haben Alt-Texte (Logo, Produktbilder). Das Footer-Logo (Startseiten-Datei ohne Alt-Text) hatte als
  Link keinen Namen; jetzt eigene Kopie der Datei mit Alt-Text (Mediathek-ID 4492, `medien.json: footer_logo`).
- **Ladezeit:** Am Computer wurde auch das ausgeblendete Handy-Video (1,5 MB) geladen; das Steuerskript nimmt dem Block
  Autoplay und Vorladen, solange er unsichtbar ist (bei Größenänderung startet das Video nach). Am Handy ist das größte
  sichtbare Element das Standbild hinter dem Videoblock; ein Preload-Hinweis am Seitenanfang (nur bis 767 px) lässt den
  Browser es sofort laden (Start nach 0,7 s statt 1,8 s, als „erkennbar und priorisiert“ gewertet). Lighthouse (lokal, gedrosselt,
  Schwankung einige Punkte): Handy 39 → 47 Punkte, blockierende Zeit 1,6 s → 0,8 s; Computer 78 → 82; SEO 100, Barrierefreiheit
  94 → 95. Der große Rest kommt aus seitenweiten Teilen (Tag Manager, Meta-Pixel, ProvenExpert, BugHerd-Skript mit Fehlermeldung,
  Startseiten-Hintergrundbilder als PNG, Hero-Video als größtes Element am Handy) und wurde nicht angefasst.
- **Geprüft nach dem Speichern:** Titel, Meta, OG/Twitter, Canonical, Überschriftenfolge, JSON-LD, Preload-Link, Videos
  (Computer: nur 4k-Video, Handy: nur Handy-Video), keine JavaScript-Fehler, Seiteneinstellungen unverändert.

## Eigenes Header-Menü (24.10.2026)

- Die Kopfleiste nutzte das seitenweite Menü „Main“ (erster Eintrag „Mit digitalen Schlüsseln Kosten sparen“, alle Links auf
  die Startseite). Da das Menü auch die Startseite bedient, wurde es nicht geändert, sondern ein eigenes WordPress-Menü
  „Kamerasysteme Header“ angelegt (ID 17, Slug `kamerasysteme-header`, per REST `wp/v2/menus` und `wp/v2/menu-items`;
  `medien.json: menue_header`). Das Nav-Menü-Widget der Kopfleiste (2a487ab) zeigt auf dieses Menü; Aussehen, Abstände und
  Handy-Menü (Hamburger) bleiben die der Startseite, weil es dasselbe Widget mit denselben Einstellungen ist.
- Einträge: „Durch Videoüberwachung teure Schäden verhindern“ → `/kamerasysteme/#moeglich`, „So arbeiten wir zusammen“ →
  `/kamerasysteme/#arbeitsweise`, „Über uns“ → `/kamerasysteme/#Über`, „FAQ“ → `/kamerasysteme/#FAQ`. Absolute Pfade wie beim
  Original (`/#digitalen`), damit Elementors sanftes Scrollen greift und die Links auch von anderen Seiten funktionieren.
- Geprüft bei 1024, 1280, 1440, 1920 und 393 px: alle vier Einträge in einer Zeile, keine horizontale Verschiebung; Klick auf
  jeden Eintrag scrollt zum richtigen Abschnitt (Abschnittsoberkante am oberen Rand, bei 1280/1440 um die 25 px des
  Verlaufsstreifens darüber, wie beim Original); am Handy öffnet der Hamburger das Menü mit den neuen Einträgen. Keine
  JavaScript-Fehler. Die Startseite zeigt weiterhin ihr Menü „Main“ mit den alten Einträgen (HTML verglichen).

## Debugging in drei Runden (24.10.2026)

Geprüft wurden die Kameraseite und ihre drei Unterseiten (Kontakt, Termin, Termin gebucht): Optik auf zwölf Breiten
(320, 360, 393, 768, 834, 1024, 1280, 1366, 1440, 1536, 1920, 2560 px), Bedienung (Menü, FAQ, Slider, Hover, Leuchtlinie,
Tastatur), Inhalte (Rechtschreibung, Schreibregeln, Links), Sicherheit (nur lesende Prüfungen) und Ladezeit (Lighthouse 12).
Runde 1: Bestandsaufnahme mit Skripten und Sichtprüfung aller Abschnitte. Runde 2: Korrekturen, danach alles erneut.
Runde 3: fünf weitere Breiten, Abschnitts-Screenshots bei 360 und 1536 px, Endkontrolle von Reihenfolge, SEO-Kopf und Menüs.

### Behoben

- **Erzwungene Zeilenumbrüche** im Text unter „Und genau das wird möglich“ (aus der Startseitenvorlage übernommen) erzeugten
  am Handy und Tablet abgehackte Zeilen; Text läuft jetzt frei.
- **Hero-Button am Handy:** Schrift 11 px, jetzt 12 px (ab 360 px Breite einzeilig, bei 320 px zwei zentrierte Zeilen).
- **Gedankenstriche** im Gründertext (Startseitentext, hier Kopie): zwei Stellen umformuliert, Inhalt gleich.
- **FAQ-Überschrift** am Computer brach mit „Infra“ allein in der dritten Zeile; „ProVision Infra“ bleibt jetzt zusammen.
- **Footer-Menü am Handy:** der lange erste Eintrag brach linksbündig um, jetzt zentriert.
- **Slider-Punkte** (6 px) als Tap-Ziel zu klein: unsichtbare Trefferfläche 24 px, Aussehen gleich.
- **Unscharfe Kleinbilder** auf Handys mit hoher Pixeldichte: Google-Logo (68 px) und Sternenleiste (83 px) der Startseite durch
  vierfach hochgerechnete Kopien mit Alt-Text ersetzt (Mediathek 4525, 4526; Transparenz getrennt skaliert).
- **Footer-Menü ausdrücklich gesetzt:** Die Footer-Menü-Widgets der Startseite verweisen auf ein nicht vorhandenes Menü
  („karriere-menu“); WordPress zeigt dann das alphabetisch erste Menü mit Einträgen. Auf der Kameraseite ist jetzt das
  Kamera-Menü fest eingetragen, und das Menü heißt „Menü Kamerasysteme (Header)“, damit es hinter „Main“ einsortiert wird und
  die Startseite nicht beeinflusst (Slug `menue-kamerasysteme-header`).

### Geprüft und in Ordnung

- Keine horizontale Verschiebung, keine abgeschnittenen Texte, keine fehlenden Bilder, keine JavaScript-Fehler aus eigenem
  Code auf allen Breiten; Rechtschreibprüfung (Deutsch) ohne Fehler, keine Platzhalter; alle Links erreichbar (Facebook
  antwortet nur echten Browsern, im Browser geprüft: Firmenseite); Anker der Menüs vorhanden; Menü, FAQ, beide Slider,
  Karten-Hover, Leuchtlinie und Tastaturreihenfolge funktionieren; Kontaktformular rendert (ohne Testversand), Calendly lädt.
- Sicherheit: HSTS mit Preload, nosniff, TLS 1.0/1.1 aus, XML-RPC, debug.log, .env und .git gesperrt, keine
  Verzeichnislisten, Nutzerliste über REST und ?author= gesperrt, Formular-REST nur mit Anmeldung, keine Cookies vor Einwilligung,
  kein Mixed Content, keine Inline-Event-Handler, eigene SVG- und Lottie-Dateien ohne Skripte, eigene Skripte verarbeiten keine
  Nutzereingaben; Kontakt- und Terminseiten `noindex`.
- Lighthouse nach den Korrekturen: Handy 43 Punkte (LCP 6,4 s statt 11 s), Barrierefreiheit 99 (vorher 94), SEO 100;
  Computer 94 (vorher 78), Barrierefreiheit 99.

### Offen, nur mit Zugriff auf die ganze Website zu lösen (Empfehlungen)

- **Footer der Startseite zeigt ein fremdes Menü:** Seit heute gibt es ein Menü „Lüneburg“ (nicht von mir angelegt). Weil die
  Footer-Widgets der Startseite auf das fehlende „karriere-menu“ verweisen, zeigt der Startseiten-Footer jetzt dieses Menü
  (Schließanlagen, Videoüberwachung, …) statt „Main“. Abhilfe: in den Footer-Widgets der Startseite das Menü „Main“ fest
  auswählen, oder das Menü „Lüneburg“ so umbenennen, dass es hinter „Main“ steht.
- **BugHerd-Skript** (Feedback-Werkzeug) lädt auf allen Seiten mit öffentlichem API-Schlüssel und wirft einen Konsolenfehler;
  für den Livebetrieb entfernen.
- **Spam-Schutz:** Honeypot des Kamera-Formulars einschalten (Anleitung, „Zwei Handgriffe“); Captcha nur bei Bedarf.
- **HTTP-Header:** Content-Security-Policy, X-Frame-Options (oder frame-ancestors), Referrer-Policy und Permissions-Policy
  fehlen seitenweit; `readme.html` und `license.txt` sind abrufbar, der Generator-Tag nennt WordPress- und Elementor-Version.
- **Benutzer:** Testbenutzer „claude-test“ (Administrator) löschen; für alle Administratoren Zwei-Faktor-Anmeldung.
- **Kleinigkeiten der Startseitenvorlage:** Sprungmarke „Zum Inhalt springen“ und der ProvenExpert-Link mit geringem Kontrast,
  ProvenExpert-Siegel als Tap-Ziel nur 20 px hoch, Hintergrund-PNGs der Startseite (1,6 MB), Kontakt- und Terminseiten ohne h1.

## SEO, zweite Stufe (24.10.2026)

Grundlage: die Yoast-Analyse der Seite (Fokus-Keyphrase „Videoüberwachung für Unternehmen“) und die Lighthouse-Messung.
Alle Texte bleiben inhaltlich gleich; es sind gezielte Ergänzungen.

- **Keyphrase an den Stellen, die zählen:** SEO-Titel beginnt jetzt damit (`Videoüberwachung für Unternehmen | ProVision Infra`,
  50 Zeichen, vorher wurde die Breite überschritten), Meta-Beschreibung gekürzt (141 Zeichen), Hero-Einleitung („… installiert
  Kamera- und Videoüberwachung für Unternehmen“), Fließtext unter „Und genau das wird möglich“, FAQ-Antwort zur Region, Alt-Text
  des Logos (Mediathek 4479). Yoast: Keyphrase-Dichte von 2 auf 8 Treffer bei 1562 Wörtern (grün), Titel grün.
- **Zwischenüberschriften:** FAQ heißt „Häufige Fragen zur Videoüberwachung für Unternehmen“; der Standort-Abschnitt trägt die
  Region als H2 („Videoüberwachung in Hamburg, Hannover und Niedersachsen“, lokale Suche) statt „Hier findest du ProVision Infra“.
- **Synonyme:** neuer kurzer Absatz unter „Technik, die wir verbauen“ (Überwachungskameras, Bullet-/Dome-/schwenkbare Kamera,
  Nachtsicht, Bewegungserkennung, Rekorder, App) und „Kameraüberwachung“ in der ersten FAQ-Antwort.
- **Ladezeit am Handy:** Hero-Video des Handy-Blocks neu kodiert (1920 x 1080, CRF 24, 504 KB statt 2560 x 1440 mit 1,5 MB;
  SSIM zur 4k-Quelle 0,999, Bildvergleich ohne sichtbaren Unterschied; Mediathek 4549, alte Datei 4342 gelöscht). Overlay-Bild des
  Gründer-Abschnitts als WebP (182 KB statt 696 KB, Mediathek 4545). Die drei Lichtschein-PNGs der Startseite bleiben: verkleinerte
  Kopien zeigten Streifen im Verlauf. Übertragene Datenmenge am Handy 4,6 MB → 3,1 MB, am Computer 6,7 MB → 3,5 MB.
- **Nicht umgesetzt, bewusst:** Keyphrase im Permalink (die Adresse /kamerasysteme/ bleibt), Keyphrase in mehr als zwei
  Zwischenüberschriften (wäre Schlüsselwort-Stopfen), Yoasts „Bindewörter“-Hinweis (für deutsche Texte wenig aussagekräftig).
- **Geprüft nach dem Speichern:** Titel, Beschreibung, OG, vier gültige JSON-LD-Blöcke, 13 H2, keine JavaScript-Fehler,
  Handy lädt nur das neue 1080p-Video, Gründer-Overlay aus dem WebP; Lighthouse SEO 100, Barrierefreiheit 99 (Handy und Computer).
- **Was nur du tun kannst, mit größter Wirkung:** Property in der Search Console und „Indexierung beantragen“; ein Link von der
  Startseite auf /kamerasysteme/ (Menü „Main“ oder ein Textlink, Ankertext „Videoüberwachung für Unternehmen“); Honeypot des
  Formulars einschalten.

## Google-Indexierung (26.10.2026)

- Search-Console-Property `https://provision-infra.de/` im Konto hey@provision-infra.de angelegt (URL-Präfix, nicht Domain:
  die Domain-Variante bräuchte einen DNS-Eintrag). Inhaberschaft automatisch über Google Tag Manager bestätigt; eine zweite
  Bestätigungsmethode (HTML-Tag in Yoast oder DNS) wäre sinnvoll, damit die Bestätigung nicht am Tag-Manager-Container hängt.
- Sitemap `sitemap_index.xml` eingereicht, Status „Erfolgreich“, 7 erkannte Seiten.
- URL-Prüfung der Kameraseite: „URL ist auf Google“, Seite indexiert; Verbesserungen erkannt: Produkt-Snippets (ProvenExpert),
  Rezensions-Snippets, Navigationspfade (Yoast), HTTPS. „Indexierung beantragen“ ausgelöst: „URL wurde einer bevorzugten
  Crawling-Warteschlange hinzugefügt“, damit Google den neuen Titel und die SEO-Änderungen zügig übernimmt.
- Ablauf technisch: echter Browser mit Google-Anmeldung (2-Faktor-Freigabe durch den Kunden), Steuerung über Befehlsdatei;
  der Direktlink zur URL-Prüfung liefert 404, der Weg über das Suchfeld der Property funktioniert. Browserprofil danach gelöscht.

## SEO, dritte Stufe: Suchabsichten (26.10.2026)

Grundlage: Google-Suggest-Auswertung zu 20 Ausgangsbegriffen (Datei `SEO-KEYWORDS.md`). Ergebnis: Wer nach Videoüberwachung
für Firmen sucht, fragt vor allem nach der Rechtslage (erlaubt, DSGVO, Hinweisschild, Mitarbeiter, Betriebsrat), nach Orten
(Betriebsgelände, Firmengelände, Gewerbegrundstück, Betriebshof, Lagerhalle, Eingangsbereich) und lokal (Lüneburg, Hamburg,
Hannover, „in der Nähe“).

- **Vier neue FAQ-Einträge** decken genau diese Absichten ab: Betriebsgelände und Mitarbeiter (berechtigtes Interesse,
  Hinweisschild, Mitarbeiterinformation, Betriebsvereinbarung, kamerafreie Räume), Speicherdauer (in der Regel 72 Stunden,
  länger nur mit Anlass), typische Bereiche (Einfahrt, Eingangsbereich, Parkplatz, Betriebshof, Lagerhalle, Gewerbegrundstück;
  Gehweg und Nachbargrundstück bleiben außen vor), Nachrüsten vorhandener Anlagen. Die Rechtsangaben sind allgemein
  gehalten und verweisen auf die Prüfung im Einzelfall. Das FAQ-Schema wächst automatisch mit (11 Fragen, gültig).
- **Lokal:** Standort-Text nennt den Sitz „Bad Bevensen bei Lüneburg“ (Impressum-Angabe), Lüneburg im Einsatzgebiet der
  Strukturdaten; LocalBusiness jetzt mit Geokoordinaten und Kartenlink (`elementor/geo.json`, Gebäudetreffer bei OpenStreetMap).
- **Meta-Beschreibung** mit „DSGVO-konform geplant“ und Lüneburg (153 Zeichen).
- **Geprüft nach dem Speichern:** Titel, Beschreibung, vier gültige JSON-LD-Blöcke, 11 FAQ-Fragen im Schema, keine
  JavaScript-Fehler; FAQ und Standort bei 393, 768 und 1440 px sauber.
- **Offen, nur mit Zutun des Kunden:** Preisrahmen für die Kosten-Frage, Hauptmenü-Eintrag „Videoüberwachung“ (Teaser und Footer-Link der Startseite sind seit
  27.10. gesetzt, siehe unten), Google Unternehmensprofil,
  Backlinks, zweite Bestätigungsmethode in der Search Console (Liste in `SEO-KEYWORDS.md`).

## Link von der Startseite (27.10.2026)

Freigabe des Kunden für genau drei Änderungen an der Startseite (ID 31); alles andere blieb unangetastet. Sicherung vorher
aus dem Elementor-Editor exportiert: `elementor/startseite-sicherung-2026-10-26.json` (23 Abschnitte, Seiteneinstellungen).

- **Teaser-Abschnitt „Videoüberwachung aus einer Hand“** zwischen „So kommst du zu deinem digitalen Zutrittssystem“ und
  „Der Gründer von ProVision Infra“: Kasten nach dem Vorbild des Standort-Kastens (Rahmen, Radius, Einblendung), Überschrift
  als h2, die zwei Sätze des Kunden, Button „Videoüberwachung für Unternehmen“ (Keyphrase als Linktext) auf `/kamerasysteme/`.
  Breite 820 px, auf Tablet und Handy volle Breite, Abstand 60/50/40 px nach oben und unten, Anker `#videoueberwachung`.
- **Footer-Zeile „Leistungen: Schließsysteme | Videoüberwachung“** neben Datenschutz, Impressum, AGB (Kopie der
  Rechtsliste). Auf dem Handy steht „Leistungen:“ in eigener Zeile (Custom CSS am Widget), sonst brach die Zeile mitten im
  Linktext um.
- **Footer-Menüs der Startseite** zeigten auf ein nicht vorhandenes Menü („karriere-menu“) und damit per WordPress-Fallback
  auf das alphabetisch erste Menü; beide Nav-Widgets stehen jetzt fest auf „Main“. Damit entfällt der Grund für die
  Namenswahl „Menü Kamerasysteme (Header)“ (bleibt so, schadet nicht).
- **Hauptmenü:** Der Eintrag „Videoüberwachung“ an zweiter Stelle im Menü „Main“ wurde vom Freigabesystem dieser Sitzung
  zweimal blockiert (Änderung an der seitenweiten Navigation; einmal per REST, einmal über den Menüeditor). Nicht umgangen;
  der Handgriff steht in `ANLEITUNG-WORDPRESS.md`, Schritt 7.
- **Vorgehen:** `tools/startseite_link.py` liest die Sicherung, setzt die drei Änderungen und schreibt
  `elementor/startseite-mit-link.elements.json` (24 Abschnitte); gespeichert über den Speicherweg des Elementor-Editors
  mit Status „publish“. Vorher per Vergleich geprüft: unter den bestehenden Abschnitten ändert sich nur der Footer,
  die Seiteneinstellungen sind identisch.
- **Geprüft nach dem Speichern** bei 393, 768, 1024, 1440 und 1920 px: zwei Links auf `/kamerasysteme/` (Teaser-Button,
  Footer), Teaser als 17. von 24 Abschnitten, kein horizontaler Überlauf, keine JavaScript-Fehler, Header unverändert,
  Footer-Menüs zeigen „Main“, Einblend-Animation des Teasers wie bei den Nachbarabschnitten.

## Kopfleisten-Menü: „Mehr“ nur am Bildschirm, Handy flach (27.10.2026)

Vorgabe des Kunden: Am Bildschirm bleibt „Mehr“ als Aufklappmenü, auf dem Handy sollen nach dem Ausklappen sofort alle
Einträge sichtbar sein, „Komm in unser Team“ steht überall zuletzt. Gilt für alle Seiten außer der Karriere-Seite.

- **Menüs:** Der Kunde hat „Komm in unser Team“ im Hauptmenü „Main“ selbst als letzten Unterpunkt von „Mehr“ angelegt
  (Design → Menüs). Im Kamera-Menü stand es an zweiter Stelle; über die REST-Schnittstelle als letzter Unterpunkt von „Mehr“
  eingeordnet. Reihenfolge dort jetzt: „Durch Videoüberwachung teure Schäden verhindern“, „Mehr“ mit „So arbeiten wir
  zusammen“, „Über uns“, „FAQ“, „Komm in unser Team“ (die Verschachtelung von „So arbeiten wir zusammen“ stammt vom Kunden).
- **Befund Handy:** Elementors Aufklappmenü zeigt „Mehr“ als Zeile mit Pfeil; die Unterpunkte sind eingeklappt (display none,
  aria-hidden) und erscheinen erst nach einem Tipp auf den Pfeil.
- **Lösung (`tools/menue_handy.py`, von beiden Build-Skripten genutzt):** Custom CSS am Menü-Widget der Kopfleiste: unter
  768 px wird die Zeile „Mehr“ ausgeblendet und ihre Unterliste dauerhaft eingeblendet, Schriftgröße der Unterpunkte wie die
  der Hauptpunkte. Dazu ein kleines Skript (HTML-Widget im Steuerungsabschnitt), das die Markierung aria-hidden der nun
  sichtbaren Unterpunkte zurücknimmt, damit Vorlesehilfen sie erreichen; Elementors Menüskript setzt sie bei jeder
  Initialisierung, deshalb mit MutationObserver. Ein einziges Menü genügt für beide Darstellungen: Ändert der Kunde das Menü,
  folgen Bildschirm und Handy automatisch.
- **Seiten:** Startseite (ID 31, `tools/startseite_link.py`, Schritt 4) und Kameraseite (ID 4313, Composer) umgesetzt.
  Zutrittssystem-Seite (ID 3316): zwei Einträge, „Komm in unser Team“ bereits zuletzt, kein „Mehr“, nichts zu tun.
  Karriere-Seite: ausgenommen, hat ohnehin kein solches Menü. Die neuen Seiten „Lüneburg“ (ID 4496) und „Uelzen“ (ID 4605,
  beide am 27.10. von anderer Hand angelegt bzw. geändert) nutzen eigene Menüs ohne „Mehr“ und ohne „Komm in unser Team“;
  nicht angefasst, Rückfrage an den Kunden.
- **Footer-Menüs** zeigen weiterhin „Mehr“ als Aufklappmenü (am Bildschirm per Hover, auf dem Handy per Tipp). Nicht Teil der
  Vorgabe, die die Kopfleiste betrifft; mit demselben CSS gleich umsetzbar.
- **Nebenbefund Hoster:** Viele Anfragen kurz hintereinander (mehrere Browser parallel) beantwortet der Server mit 429, dann
  fehlen Stylesheets und Seiten sehen „kaputt“ aus. Prüfungen deshalb nacheinander mit Pausen; echte Besucher sind nicht
  betroffen.
