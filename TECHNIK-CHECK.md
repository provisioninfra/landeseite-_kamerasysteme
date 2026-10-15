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
