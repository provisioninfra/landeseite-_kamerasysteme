# Anleitung: Die Kamera-Landingpage in WordPress fertigstellen und veröffentlichen

Diese Anleitung ist für Menschen ohne Technik-Vorkenntnisse geschrieben. Die Seite liegt fertig
aufgebaut in deinem WordPress und ist inzwischen unter `https://www.provision-infra.de/kamerasysteme/`
veröffentlicht. Es bleibt: Produktbilder einsetzen, Texte prüfen, Suchmaschinen-Angaben eintragen.

---

## Wo die Seite liegt

1. Im Backend `https://www.provision-infra.de/wp-admin` anmelden.
2. Links auf **Seiten → Alle Seiten** klicken. Oben den Filter **Entwürfe** wählen.
3. Die Seite heißt **„Kamera- & Videoüberwachung“**. Die spätere Adresse lautet
   `https://www.provision-infra.de/kamera-videoueberwachung/`.

Die Seite ist aus den Original-Bausteinen deiner Startseite aufgebaut. Header, Hero, Slider,
Icon-Zeilen, Kundenstimmen, Ablauf-Timeline, Gründer, Partner, Standort, FAQ und Footer sind
dieselben Elementor-Elemente wie auf der Startseite, nur mit Kamera-Texten, dem neuen Video und
Platzhaltern für deine Produktbilder.

---

## Schritt 1: Vorschau ansehen (2 Minuten)

1. In der Seitenliste mit der Maus über die Seite fahren → **Vorschau** klicken.
2. Die Seite öffnet sich so, wie Besucher sie später sehen. Für andere ist sie noch unsichtbar.
3. Am Handy prüfen: Den Vorschau-Link kopieren und am Handy öffnen. Dafür musst du am Handy im
   WordPress-Backend eingeloggt sein, sonst wird die Vorschau nicht angezeigt.

Auf dem Handy liegt das Video als eigener Block unter dem Button, der Text steht auf einfarbigem
Hintergrund. Auf dem Desktop läuft das Video (4K-Fassung) hinter dem Text einmal ab und bleibt auf dem
letzten Bild stehen. Scrollst du weg und wieder zurück, startet es erneut.

---

## Schritt 2: Produktbilder prüfen (2 Minuten)

Der Abschnitt **„Technik, die wir verbauen“** zeigt fünf freigestellte TP-Link-VIGI-Kameras aus deinen Fotos
(Mediathek: `kamera-1.png` bis `kamera-5.png`, 1600 × 1200 Pixel mit transparentem Hintergrund). Die sechs
alten Platzhalter `kamera-produktbild-1.jpg` bis `-6.jpg` werden nicht mehr benutzt und können in der
Mediathek gelöscht werden.

So tauschst oder ergänzt du Bilder:

1. Seite öffnen → **Mit Elementor bearbeiten**.
2. Zum Slider scrollen und auf das Bild klicken, das du tauschen willst.
3. Links im Bedienfeld unter **Bild** auf das Bild klicken → **Bild wählen** → eigenes Foto hochladen
   oder aus der Mediathek wählen → **Medien auswählen**.
4. Weitere Kamera: Im **Struktur-Fenster** (Symbol mit den Ebenen) einen Slide markieren → Rechtsklick →
   **Duplizieren**, dann das Bild tauschen. Weniger Kameras: Slide markieren → Rechtsklick → **Löschen**.
5. Neue Bilder am besten freigestellt als PNG im Querformat 4:3 (1600 × 900 bis 1600 × 1200 Pixel), damit
   sie zu den vorhandenen passen.
6. Unten links auf **Aktualisieren** klicken.

---

## Schritt 3: Texte prüfen und anpassen (10 Minuten)

Jeder Text ist ein eigenes Elementor-Element. Im Editor auf einen Text klicken, links im Bedienfeld
schreiben, fertig. Diese Stellen lohnen einen Blick:

- **Hero:** Überschrift und Einleitung. In der Überschrift steht nach „Gebäude“ ein `<br>` (fester
  Zeilenumbruch), damit „mit Kamera- & Videoüberwachung“ auf jedem Bildschirm in der zweiten Zeile beginnt.
  Beim Ändern des Textes das `<br>` stehen lassen. Die Schriftgröße steht unter **Stil → Typografie → Größe**;
  für Tablet und Handy ist dort eine Formel wie `min(28px, 7vw - 2px)` hinterlegt. Die erste Zahl ist die
  größte erlaubte Größe, der Rest hält die Zeilen bei schmalen Bildschirmen zusammen. Wer es größer möchte,
  erhöht nur die erste Zahl.
- **Unser Anspruch:** Glas-Box unter dem Hero.
- **Fünf Unterschiede:** Am Computer zweispaltig wie der Startseiten-Abschnitt „Warum immer mehr KMUs …“: links
  Überschrift und Einleitung (bleiben beim Scrollen stehen, bis die Karten rechts zu Ende sind), rechts fünf Karten
  (Rahmen, beim Überfahren mit der Maus gelb) mit Überschrift, kurzem Text und einer fetten Box mit dem
  Schmerzpunkt. Karte anklicken, dann die drei Textelemente darin einzeln bearbeiten. Auf Tablet und Handy stehen
  Text und Karten untereinander, am Handy mit dem Glas-Logo oben wie auf der Startseite. Das Glas-Logo im
  Hintergrund ist das Bild der Startseite (Mediathek-ID 516).
- **Erstgespräch-Button** unter den Karten: nur der Button, ohne Text davor. Alle Buttons der Seite öffnen
  die eigene Kontaktseite /kontakt-kamerasysteme/ (wie die Startseite /kontakt öffnet).
- **Kontaktseite:** eigene Seite „Kontakt Kamerasysteme“ (ID 4371, /kontakt-kamerasysteme/), Kopie der Seite
  /kontakt, wie diese ohne Suchmaschinen-Indexierung. Darauf das Gravity-Forms-Formular „Anfrageformular
  Kamerasysteme“ (ID 4), eine Kopie von
  „Anfrageformular (1)“ mit den Feldern Name, Bereich, Mitarbeitende, Anzahl Gebäude (1, 2, 3, >3), E-Mail,
  Telefon. Felder und Texte änderst du unter **Formulare → Anfrageformular Kamerasysteme**. Die beiden
  bestehenden Formulare sind unverändert. Einträge des neuen Formulars findest du unter **Formulare →
  Einträge** (Formular auswählen). Das Schritt-für-Schritt-Design (eine Frage pro Schritt, Button „Weiter“)
  steuert der Eintrag **Landeseiten Forms → Kontakt Kamerasysteme**; dort lassen sich Farben, Schriftgrößen und
  Button-Texte ändern.
- **Terminbuchung:** Nach dem Absenden landet der Besucher auf /termin-kamerasysteme/ (bei Privat oder bis 50
  Mitarbeitenden auf /termin-gebucht-kamerasysteme/). Beide Seiten zeigen den Calendly-Termintyp „Telefonisches
  Erstgespräch Kamerasysteme“. Nach der Buchung leitet Calendly wie beim Schließsysteme-Termin auf /danke/ weiter
  (in Calendly unter dem Termintyp → Weitere Optionen → Bestätigungsseite hinterlegt). Den Termintyp selbst (Dauer,
  Fragen, Erinnerungen, Weiterleitung) pflegst du in Calendly. Die Seiten „Termin“ und „Termin Gebucht“ der
  Startseite bleiben beim Schließsysteme-Termin.
- **Ablauf der Zusammenarbeit:** Die fünf Schritte gibt es zweimal, einmal für Desktop (Texte über
  und unter dem Zeitstrahl) und einmal für das Handy (Timeline-Element). Änderungen bitte an beiden Stellen.
- **FAQ:** Auf das Akkordeon klicken → links unter **Inhalt** die Fragen aufklappen und bearbeiten.
  Die Antwort zur Rechtslage ist allgemein gehalten. Wenn du einen Datenschutz-Berater hast, lass sie gegenlesen.

Die Kundenstimmen, der Gründer-Abschnitt, die Partner und der Standort sind unverändert von der
Startseite übernommen.

---

## Schritt 4: Menü oben (2 Minuten, optional)

Die Kopfleiste zeigt das Menü deiner Website. Die Einträge springen zu den Abschnitten der Seite:
„Mit digitalen Schlüsseln Kosten sparen“ führt zur Glas-Box, die anderen drei zu Ablauf, Gründer und FAQ.

Nur der erste Eintrag passt vom Wortlaut nicht zur Kamera-Seite. Wenn er geändert werden soll, muss
unter **Design → Menüs** ein eigenes Menü für diese Seite angelegt werden. Das verändert die Startseite
nicht, braucht aber einen zweiten Schritt im Header der Seite. Sag Bescheid, dann übernehme ich das.

---

## Link-Vorschau (WhatsApp, LinkedIn, Facebook)

Die Seite hat in Yoast ein eigenes Vorschaubild (Schlussbild des Hero-Videos, 1200 × 630 Pixel, Mediathek
`kamera-vorschau-1200x630-1.jpg`), einen Vorschau-Titel („Wir schützen dein Gebäude mit Kamera- &
Videoüberwachung“) und eine Beschreibung. Ändern: Seite bearbeiten → Yoast-Box → Reiter **Social** → Bild,
Titel, Beschreibung. WhatsApp merkt sich eine Vorschau pro Link; nach Änderungen hilft ein Zusatz wie
`?v=2` am Link, bis WhatsApp die neue Vorschau lädt. Ein Video kann in keiner Link-Vorschau laufen, nur ein Bild.

---

## Schritt 5: Suchmaschinen-Angaben eintragen (3 Minuten)

1. Unter **Seiten → Alle Seiten** die Seite normal bearbeiten (nicht mit Elementor).
2. Unterhalb des Inhalts im **Yoast SEO**-Kasten:
   - **SEO-Titel:** `Kamera- & Videoüberwachung – ProVision Infra`
   - **Meta-Beschreibung:** `ProVision Infra plant & installiert deine Kamera- und Videoüberwachung – damit dein Gebäude rund um die Uhr geschützt ist.`
   - Reiter **Social**: als Facebook-Bild das Standbild aus der Mediathek wählen
     (Datei `kamera-hero-standbild.jpg`).
3. **Aktualisieren** klicken.

---

## Schritt 6: Veröffentlichen (1 Minute)

1. Seite öffnen → **Mit Elementor bearbeiten**.
2. Unten links auf den grünen Button **Veröffentlichen** klicken.
3. Die Seite ist jetzt unter `https://www.provision-infra.de/kamera-videoueberwachung/` erreichbar.
4. Anschließend oben in der Admin-Leiste **WP Rocket → Cache leeren** klicken, damit die Seite
   überall aktuell ausgeliefert wird.

---

## Schritt 7: Verlinken, damit Besucher die Seite finden (5 Minuten)

Eine Unterseite ohne Link findet niemand. Möglichkeiten:

- **Button auf der Startseite:** Im Elementor der Startseite an passender Stelle einen Button einfügen,
  Link `/kamera-videoueberwachung/`.
- **Menü:** Unter **Design → Menüs** die Seite dem Menü hinzufügen.
- **Google Search Console** (falls eingerichtet): Die Adresse unter „URL-Prüfung“ eintragen und
  **Indexierung beantragen**.

---

## Nach der Veröffentlichung: Kurzer Check

- Seite im **privaten Browserfenster** öffnen: Wird alles angezeigt, läuft das Video?
- **Am Handy** öffnen: Liegt das Video unter dem Button? Lässt sich der Slider wischen?
- **Buttons klicken:** Alle führen auf die Kontaktseite.
- **Testbenutzer löschen:** Unter **Benutzer** den Benutzer `technik@provision-infra.de` entfernen.

---

## Falls die Seite einmal verloren geht

Im Projekt liegt die Seite als Elementor-Vorlage: `elementor/landingpage-kamerasysteme.json`.
Import über **Vorlagen → Gespeicherte Vorlagen → Vorlagen importieren**, dann auf einer neuen Seite
über **Vorlage hinzufügen → Meine Vorlagen** einfügen. Hinweis: Beim Vorlagen-Import legt Elementor
Kopien der verwendeten Bilder in der Mediathek an. Die Datei lässt sich mit
`python3 tools/build_from_homepage.py` jederzeit neu erzeugen.

---

## Wenn etwas nicht klappt

| Problem | Lösung |
|---|---|
| Vorschau zeigt nicht die neue Seite | Browser-Cache leeren oder privates Fenster. Zusätzlich **WP Rocket → Cache leeren**. |
| Video läuft am Desktop nicht | Hero-Container anklicken → Stil → Hintergrund → Video-Link prüfen (`kamera-hero-video.mp4`). |
| Ein Produktbild ist verzerrt | Foto im Querformat 4:3 verwenden oder im Bild-Element unter Stil → Breite anpassen. |
| Timeline im Ablauf fehlt | Lottie-Element anklicken → Quelle prüfen. Es verweist auf die Animationsdatei der Startseite. |
| Slider lässt sich nicht wischen | Nach dem Speichern die Seite neu laden. Im Editor selbst ist der Slider nicht wischbar. |

Bei allem anderen: Screenshot und kurze Beschreibung reichen, dann kümmere ich mich darum.
