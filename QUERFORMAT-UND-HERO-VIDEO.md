# Handy-Querformat und Hero-Video auf allen Landingpages (02.11.2026)

Rückmeldung des Kunden (iPhone, Querformat und Hochformat):

1. Im Querformat (956 × 440 CSS-Pixel) verdecken Grafiken Texte, der linke Text einer Sektion „läuft beim Scrollen nicht mit“.
2. Auf allen Seiten startet das Hero-Video hin und wieder nicht, stattdessen ist ein Abspiel-Symbol zu sehen.
   Gewünscht: Video läuft immer, beim Herunter- und wieder Hochscrollen erneut, aber jeweils nur einmal.

## Befund

Geprüft wurden Startseite, /zutrittssystem/, /kamerasysteme/, /karriere/, /lueneburg/ und /uelzen/ mit Playwright in sechs
Ansichten (iPhone hoch 440 × 956 und quer 956 × 440, iPad hoch 820 × 1180 und quer 1180 × 820, Desktop 1440 × 900 und
1920 × 1080). Alle Scans scrollen die Seite in Schritten durch und prüfen, welche Elemente unter dem festen
ProvenExpert-Siegel liegen (`document.elementsFromPoint`), ob Elemente seitlich überstehen, welche Elemente fest oder
sticky sind, und wie sich die `<video>`-Elemente verhalten.

### Querformat am Handy

- Das Querformat eines iPhones liegt mit 956 px Breite in Elementors Breakpoint „Tablet Hochformat“ (bis 1024 px). Der
  Breakpoint „Mobil Querformat“ (bis 880 px) ist in den Elementor-Einstellungen nicht aktiv. Die Seite zeigt im
  Querformat also das Tablet-Layout, aber mit nur 440 px Höhe.
- Das **feste ProvenExpert-Siegel** (`#pe-badge-fixed`, HTML-Widget am Seitenende jeder Landingpage, 110 px breit, unten
  rechts) deckt in dieser Höhe laufend Text ab: auf der Startseite an 18 Scrollpositionen, auf /uelzen/ an 19, auf
  /kamerasysteme/ an 18, auf /zutrittssystem/ an 9. Im Hochformat ist das Siegel per Elementor-Einstellung
  („hide_mobile“) ohnehin ausgeblendet. Das ist der Hauptbefund hinter „Grafiken passen nicht“ (Bilder 1 und 2 des Kunden).
- Das **Cookie-Symbol von Borlabs** (96 × 96 px, fest unten links) überdeckt im Querformat ebenfalls Text, z. B. die
  Zwischenüberschrift „(… und stattdessen mit Zutritt per App …)“.
- Die **Sticky-Textspalte** der Kachel-Sektion ist nur für Laptop, Desktop und Breitbild aktiviert (`sticky_on`), im
  Tablet-Breakpoint also aus. Elementor-Motion-Effects gibt es auf der Startseite nicht. Die Tür-Sektion „Und genau das
  wird möglich“ (`c567c71`) ist 950 px hoch mit Hintergrundbild `cover`; der Textblock steht oben links und scrollt in
  Chromium normal mit. Ein Festhängen des Textes ließ sich ohne iPhone nicht nachstellen; ein WebKit-Test war hier nicht
  möglich. Beobachtung: Vor und nach dem Textblock bleibt in 440 px Höhe jeweils fast ein ganzer Bildschirm nur Tür.
- Seitliches Überstehen gibt es nur bei den Karussells (Kundenstimmen, Technik), die absichtlich 140 vw breit sind; keine
  horizontale Scrollbar (`scrollWidth` = Viewport) in allen Ansichten.
- iPad und Desktop: Das Siegel überdeckt auch dort gelegentlich den rechten Spaltenrand (iPad hoch 8, iPad quer 12,
  Desktop 8, 1920 px 5 Positionen). Das ist das bestehende Design und wurde nicht verändert.

### Hero-Video

- Hero der Startseite (und der daraus geklonten Seiten /lueneburg/ und /uelzen/): Elementor-Hintergrundvideo, am Computer
  im Hero-Container (`0f0c707`, Ausschnitt 0–3,5 s), am Handy als eigener Block (`d135e80`, Ausschnitt 1–3,5 s), jeweils
  „einmal abspielen“. Elementor setzt die Videoquelle per JavaScript (`src="…mp4#t=1,3.5"`) und verlässt sich auf das
  `autoplay`-Attribut; einen Neustart beim Zurückscrollen gibt es in Elementor für eigene Videos nicht. Nach dem Ende
  blendet Elementor das Video aus (`hide()`), sichtbar bleibt dann das Ersatzbild – auf der Startseite ein einfarbig
  grünes Bild (`back-empt.png`).
- **Dateigröße:** `Main-Banner-Video-6.mp4` (Handy) 15,4 MB und `Main-Banner-Video-new-2.mp4` (Desktop) 13,8 MB für je
  4,2 Sekunden (2880 × 2880 bzw. 3840 × 2160, 26–29 Mbit/s). Zum Vergleich Kamera-Seite: 0,5 MB (Handy) und 3,7 MB (4K).
  Dazu kommt: Das jeweils unsichtbare Video (Desktop-Hero am Handy, Handy-Block am Computer) wurde trotzdem geladen,
  am Handy also 29 MB. Auf Mobilfunk erscheint deshalb sekundenlang nur das Standbild.
- **Abspiel-Symbol:** Das Symbol in der Bildschirmaufnahme des Kunden ist die Anzeige von iOS Safari für ein Video, das
  das Gerät nicht automatisch startet. In der Aufnahme ist die Batterieanzeige gelb, also der Stromsparmodus aktiv; in
  diesem Modus startet iOS keine Videos von selbst, erst nach einer Berührung. Das erklärt das „hin und wieder“. Eine
  Website kann das nicht umgehen, sie kann das Video aber bei der ersten Berührung (Tippen oder Scrollen) starten.

## Änderungen

### 1. Steuer-Snippet als HTML-Widget am Seitenende (CSS + JavaScript)

Datei: `tools/seitenweit-querformat-hero-video.html`. Elementor Pro „Custom Code“ steht auf der Seite nicht zur Verfügung
(kein Menüpunkt), deshalb liegt das Snippet wie die bisherige Videosteuerung der Kamera-Seite als eigener Container mit
HTML-Widget am Ende jeder Landingpage (Container „Querformat + Hero-Video (Steuerung)“, ohne Abstände, Höhe 0).

CSS, nur für `(orientation: landscape) and (max-height: 520px)`, also Handys im Querformat:

- `#pe-badge-fixed` ausblenden (das Siegel bleibt im Hero und im Footer sichtbar, im Hochformat war es schon ausgeblendet),
- Cookie-Symbol `.brlbs-cmpnt-widget` auf 62 % verkleinern (Ankerpunkt unten links).

JavaScript für alle Elementor-Hintergrundvideos (`video.elementor-background-video-hosted`), außer auf der Kamera-Seite
(4313), die ihre eigene Steuerung behält:

- Unsichtbare Videos nicht laden: Ist der Video-Container ausgeblendet, werden vor Elementors Initialisierung `autoplay`
  entfernt und `preload="none"` gesetzt. Wird der Block durch Drehen oder Größenänderung sichtbar, lädt und startet das Video.
- Einmal abspielen, letztes Bild stehen lassen: Endzeit des Ausschnitts wird selbst überwacht (Browser wenden
  `#t=start,ende` nur beim ersten Durchlauf an), Elementors Ausblenden nach `ended` wird zurückgenommen.
- Verlässt der Hero-Bereich den Bildschirm und kommt zurück (IntersectionObserver), springt das Video auf die Startzeit
  und läuft genau einmal erneut.
- Hat das Gerät den automatischen Start unterbunden (Stromsparmodus), startet das Video bei der ersten Berührung
  (`touchend`, `click`, `keydown`), sofern es noch nicht durchgelaufen ist.

Getestet gegen die Live-Seite /uelzen/ in Chromium (Snippet vor `</body>` eingefügt, Seite unverändert): Hochformat lädt
nur noch das Handy-Video (vorher beide), Querformat blendet das Siegel aus und verkleinert das Cookie-Symbol, Neustart
nach Zurückscrollen in allen drei Ansichten, Desktop lädt das Handy-Video nicht mehr.

### 2. Kleine Hero-Videos für Startseite, /lueneburg/ und /uelzen/

Mit ffmpeg aus den Originalen neu kodiert (H.264 High, ohne Tonspur, `-movflags +faststart`), Qualität gegen das Original
gemessen (SSIM, 1,0 = identisch):

| Datei (Mediathek) | Auflösung | Größe | SSIM | ersetzt |
| --- | --- | --- | --- | --- |
| `startseite-hero-tuer-desktop-2160.mp4` (ID 4690) | 3840 × 2160, CRF 22 | 1,9 MB | 0,996 | `Main-Banner-Video-new-2.mp4` (13,8 MB) |
| `startseite-hero-tuer-handy-1440.mp4` (ID 4687) | 1440 × 1440, CRF 21 | 0,8 MB | 0,993 | `Main-Banner-Video-6.mp4` (15,4 MB) |

```bash
ffmpeg -i Main-Banner-Video-new-2.mp4 -an -c:v libx264 -profile:v high -level 5.1 -pix_fmt yuv420p -crf 22 -preset slow -movflags +faststart startseite-hero-tuer-desktop-2160.mp4
ffmpeg -i Main-Banner-Video-6.mp4 -an -vf scale=1440:1440 -c:v libx264 -profile:v high -pix_fmt yuv420p -crf 21 -preset slow -movflags +faststart startseite-hero-tuer-handy-1440.mp4
```

Die Originale bleiben in der Mediathek; geändert wurde nur die Video-URL in den Elementor-Einstellungen der Hero-Container
(Start-/Endzeit, Ersatzbild und alles andere unverändert). Die Videos der Zutrittssystem-Seite (6,4 MB und 3,8 MB) und der
Kamera-Seite wurden nicht angefasst.

### 3. Vorgehen je Seite

Für jede Seite wurden die gespeicherten Elementor-Daten im Editor gelesen (`elementor.config.initial_document`, Werte der
Seiteneinstellungen in `.settings.settings`), der Steuer-Container angehängt, bei den drei Tür-Video-Seiten die zwei
Video-URLs ersetzt und per `save_builder` mit dem bisherigen Status gespeichert. Danach wurde der sichtbare Text der
Live-Seite vor und nach der Änderung verglichen (identisch), die Elementanzahl geprüft und das Verhalten in Chromium
nachgestellt. Stand je Seite siehe Abschnitt „Ergebnis“.

Hinweise aus dem Durchlauf: Der Server drosselt schnelle Folgeaufrufe (HTTP 429), zwischen Editor-Aufrufen also 60 Sekunden
Pause, Speichern bei 429 nach 30 Sekunden wiederholen. Die Live-Seite /uelzen/ war seit dem Build vom 27.10. in WordPress
weiterbearbeitet worden (vierte Kundenstimme, Absatz mit Links auf /lueneburg/ und Startseite im Standort-Text) – deshalb
immer vom Live-Export ausgehen, nie vom Repo-Stand.

## Abstimmung mit der Parallelsitzung „Neue Unterseite mit Videoüberwachung“

Während dieser Arbeit speicherte eine zweite Claude-Sitzung (gleicher WordPress-Zugang, Branch `claude/bold-darwin-ckgllr`
dieses Repos) auf denselben Seiten einen eigenen Container „Steuerung Ladeverhalten“ (unsichtbare Lottie-/Video-Blöcke
nicht laden, ProvenExpert-„Product“-Schema aus dem DOM entfernen) und änderte das Siegel-Widget: Handy-Ausblendung
entfernt (Kundenwunsch, Siegel im Hochformat sichtbar) plus Querformat-Regel am Widget selbst. Ihr Speicherlauf um 09:56
überschrieb /lueneburg/ mit einem Export von 09:20 und damit meinen Container samt Videotausch. Nach gegenseitigen
Nachrichten (`send_message`) stellte die Sitzung Lüneburg um ca. 10:05 aus dem Uelzen-Export wieder her und speicherte
danach alle Seiten aus frischen Exporten. Regel seitdem: vor jedem Speichern frisch exportieren, Seite und Uhrzeit der
anderen Sitzung vorher nennen, Steuer-Container getrennt halten (ihre Titel beginnen mit „Steuerung“, meiner heißt
„Querformat + Hero-Video (Steuerung)“).

## Ergebnis (Stand 02.11.2026, 10:50 Uhr)

| Seite | Mein Container (CSS+JS) | Kleine Hero-Videos | Siegel Querformat aus | Container „Steuerung Ladeverhalten“ (Parallelsitzung) |
| --- | --- | --- | --- | --- |
| /uelzen/ (4605) | ja (09:44) | ja | ja (doppelt: mein CSS und Widget-Regel) | ja |
| /lueneburg/ (4496) | ja (09:49, nach Überschreiben um 10:05 wiederhergestellt) | ja | ja | ja |
| /zutrittssystem/ (3316) | ja (09:53) | nein (eigene Videos 6,4 / 3,8 MB, unverändert) | ja | ja |
| /kamerasysteme/ (4313) | nein (eigene Videosteuerung der Seite, JS des Snippets wäre dort inaktiv) | eigene kleine Videos | ja (Widget-Regel der Parallelsitzung) | ja |
| Startseite (31) | ja (10:48, aus frischem Export mit den Ständen der Parallelsitzung von 10:26) | ja | ja (doppelt) | ja |

Sichtbarer Text aller geänderten Seiten vor/nach identisch (Vergleich des gerenderten HTML), je Seite genau zwei neue
Elemente (Container + Widget).

## Nicht geändert, zur Entscheidung

- Siegel-Überlappung auf iPad und Desktop (rechter Spaltenrand): bestehendes Design.
- Videos der Zutrittssystem-Seite (6,4 MB / 3,8 MB) könnten genauso verkleinert werden.
- Startzeit 1 s des Handy-Videos, grünes Ersatzbild `back-empt.png` des Handy-Blocks.
- Sticky-Textspalte und Höhe der Tür-Sektion im Tablet-Layout, falls das „Nicht-Mitlaufen“ am iPhone weiter auftritt
  (dann bitte kurzes Video der Stelle schicken).
