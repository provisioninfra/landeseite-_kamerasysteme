# Technik- und Skalierungs-Check vor dem Livegang

Stand: 15.10.2026 · Geprüft wurde die statische Version (`index.html`) mit Chromium (Playwright),
axe-core 4.10 (Barrierefreiheit) und html-validate 9.5 (HTML-Validität).

## Ergebnis in Kürze

Die Seite ist technisch bereit für den Livegang. Alle gefundenen Punkte wurden behoben.
Offen bleiben nur zwei inhaltliche Entscheidungen (siehe „Offene Punkte“).

| Bereich | Ergebnis |
|---|---|
| Responsives Layout | 13 Bildschirmbreiten von 320 bis 1920 px geprüft, kein horizontaler Überlauf, keine Textüberlappung |
| JavaScript / Konsole | 0 Fehler, 0 Warnungen auf allen Breiten |
| Ladefehler | 0 fehlgeschlagene Requests |
| Barrierefreiheit (WCAG 2.1 AA + Best Practice) | 0 Verstöße auf Desktop und Mobil |
| HTML-Validität | 1 Hinweis zu `autoplay` am Hintergrundvideo (beabsichtigt, stumm) |
| Layoutverschiebung (CLS) | 0,00 |
| Seitengewicht beim ersten Aufruf | ca. 1,0 MB (Video 360 KB, Timeline-Bibliothek 168 KB, Animation 114 KB) |
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

## Offene Punkte (inhaltlich, keine Technik)

1. Zwei Texte in „Ablauf der Zusammenarbeit“ stammen unverändert von der Startseite und sprechen vom
   Schließsystem („Türen und Zutrittspunkte“, „Zutrittskonzept“). Für die Kamera-Seite anpassen?
2. Die Sektionen „Über uns“ und „FAQ“ aus dem Menü sind noch nicht gebaut. Die Menüpunkte zeigen
   derzeit ins Leere. Entweder Sektionen ergänzen oder Menüpunkte entfernen.

## Elementor-Vorlage

Die Vorlage (`elementor/landingpage-kamerasysteme.json`) wurde entsprechend angepasst: Auf Tablet
und Handy wird kein Hintergrundvideo hinter dem Text gezeigt, der Video-Block erscheint unter dem Button.
In WordPress kommen Favicon, Schriften, Cookie-Banner, Header und Footer von der Hauptseite.
Der Import konnte ohne Zugang zum WordPress nicht live getestet werden.
