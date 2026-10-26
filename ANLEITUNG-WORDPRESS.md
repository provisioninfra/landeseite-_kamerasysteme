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

- **Hero:** Überschrift und Einleitung. In der Überschrift steht nach „Unternehmen“ ein `<br>` (fester
  Zeilenumbruch), damit „mit Kamera- & Videoüberwachung“ auf jedem Bildschirm in der zweiten Zeile beginnt.
  Beim Ändern des Textes das `<br>` stehen lassen. Die Schriftgröße steht unter **Stil → Typografie → Größe**;
  für Tablet und Handy ist dort eine Formel wie `min(28px, 5.9vw - 2px)` hinterlegt. Die erste Zahl ist die
  größte erlaubte Größe, der Rest hält die Zeilen bei schmalen Bildschirmen zusammen. Wer es größer möchte,
  erhöht nur die erste Zahl.
- **Logo-Rahmen und drei Punkte** (direkt unter dem Hero, wie auf der Startseite): links der gelb umrandete Rahmen
  mit dem Logo, das auf die Startseite verlinkt (Bild-Element, Link unter **Inhalt → Link**; Datei kamera-logo-provision-infra-1032.png, eine hochgerechnete Version des Header-Logos; die Breite steht im Element unter **Erweitert → Eigenes CSS**), rechts drei Zeilen mit
  Icon und Text (Ausgangslage, Folgen, Lösung). Jede Zeile ist ein eigenes Textelement.
- **Was ohne Kameras auf deinem Gelände passiert?** Am Computer zweispaltig wie der Startseiten-Abschnitt „Warum immer
  mehr KMUs …“: links Überschrift und Einleitung (bleiben beim Scrollen stehen, bis die Karten rechts zu Ende sind),
  rechts fünf Karten mit X-Symbol (Rahmen, beim Überfahren mit der Maus gelb). Jede Karte: Situation („… wenn“),
  Verlauf und eine fette Box mit der Folge; die letzte Karte zusätzlich mit einer Hinweiszeile (Glühbirne).
  Karte anklicken, dann die Textelemente darin einzeln bearbeiten. Auf Tablet und Handy stehen Text und Karten
  untereinander, am Handy mit dem Glas-Logo oben wie auf der Startseite (Bild der Startseite, Mediathek-ID 516).
- **So arbeiten wir:** drei schwebende Kästen mit Haken (wie „ProVision Infra installiert dir genau das …“ auf der
  Startseite). Überschrift und die drei Texte sind einzelne Elemente.
- **Stell dir mal vor …:** acht Kästen um die schwenkende Kamera. Am Computer und Tablet stehen die Kästen links und
  rechts der Kamera; der erste Kasten leuchtet, beim Überfahren leuchtet der jeweilige Kasten und eine gelbe Linie
  läuft zur Kamera (Element „Leuchtlinie zur Kamera“, bitte nicht löschen). Am Handy stehen die acht Kästen
  untereinander, darunter die Kamera. Texte und Icons gibt es deshalb zweimal (Abschnitt „Computer/Tablet“ und
  Abschnitt „Handy“), Änderungen bitte an beiden Stellen. Die Kamera ist eine Lottie-Animation aus Produktbild 3
  (Mediathek: kamera-schwenk-scharf.json); sie schwenkt, schwebt leicht, die rote LED blinkt. Der gelbe Lichtschein um die
  Kamera ist ein CSS-Schatten des Elements (Erweitert → Eigenes CSS).
- **Und genau das wird möglich mit ProVision Infra:** Überschriften und Textkasten links, rechts die Szene der
  Startseite (Flur mit Tür) als Hintergrundbild, die Person darauf als dunkle Kapuzen-Silhouette (Einbrecher).
  Das Hintergrundbild wechselst du unter **Stil → Hintergrund** (Computer und Handy haben je ein eigenes Bild:
  kamera-szene-einbrecher-4800.webp und kamera-szene-einbrecher-mobil-2552.webp).
- **Icons:** Alle Icon-Kacheln sind dunkel mit gelbem Symbol (wie auf der Startseite). Die fünf Kamera-Icons liegen als
  SVG in der Mediathek (kamera-icon-…-dunkel.svg); ein Icon tauschst du im Icon-Element unter **Inhalt → Icon → SVG
  hochladen**.
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

Reihenfolge der Seite: Hero, Logo-Rahmen mit drei Punkten, Was ohne Kameras passiert, Kundenstimmen, Stell dir mal vor,
Und genau das wird möglich, So arbeiten wir, Ablauf der Zusammenarbeit, Gründer, Technik (Produktslider), Standort mit
Erstgespräch, FAQ, Partner, Footer. Kundenstimmen, Gründer, Standort und Partner sind unverändert von der Startseite
übernommen.

---

## Schritt 4: Menü oben (nichts zu tun)

Die Kopfleiste ist die der Startseite, zeigt auf der Kamera-Seite aber ein eigenes Menü: unter **Design → Menüs**
heißt es „Menü Kamerasysteme (Header)“ (seit 24.10.2026). Der Name beginnt absichtlich mit „Menü“, damit es in der
alphabetischen Liste hinter „Main“ steht; Hintergrund siehe `TECHNIK-CHECK.md` („Fehlendes Footer-Menü“). Die vier Einträge springen zu Abschnitten der Kamera-Seite:

- „Durch Videoüberwachung teure Schäden verhindern“ → Abschnitt „Und genau das wird möglich mit ProVision Infra“
- „So arbeiten wir zusammen“ → Abschnitt „So arbeiten wir“ (direkt darunter der Ablauf)
- „Über uns“ → „Der Gründer von ProVision Infra“
- „FAQ“ → die häufigen Fragen

Das Menü „Main“ der Startseite ist unverändert. Einträge ändern: **Design → Menüs**, oben „Menü Kamerasysteme (Header)“
auswählen, Text oder Link anpassen, „Menü speichern“. Die Links beginnen mit `/kamerasysteme/#…`, damit sie auch
von anderen Seiten aus funktionieren.

---

## Link-Vorschau (WhatsApp, LinkedIn, Facebook)

Die Seite hat in Yoast ein eigenes Vorschaubild (Schlussbild des Hero-Videos, 1200 × 630 Pixel, Mediathek
`kamera-vorschau-1200x630-1.jpg`), einen Vorschau-Titel („Wir schützen dein Unternehmen mit Kamera- &
Videoüberwachung“) und als Beschreibung die Meta-Beschreibung aus Schritt 5. Ändern: Seite bearbeiten → Yoast-Box → Reiter **Social** → Bild,
Titel, Beschreibung. WhatsApp merkt sich eine Vorschau pro Link; nach Änderungen hilft ein Zusatz wie
`?v=2` am Link, bis WhatsApp die neue Vorschau lädt. Ein Video kann in keiner Link-Vorschau laufen, nur ein Bild.

---

## Schritt 5: Suchmaschinen-Angaben prüfen (2 Minuten)

Die Angaben sind bereits eingetragen (Stand 20.10.2026, Werte in `elementor/seo.json`). Falls sie einmal
verloren gehen: unter **Seiten → Alle Seiten** die Seite normal bearbeiten (nicht mit Elementor) und im
**Yoast SEO**-Kasten unterhalb des Inhalts eintragen:

- **Fokus-Keyphrase:** `Videoüberwachung für Unternehmen`
- **SEO-Titel:** `Videoüberwachung für Unternehmen | ProVision Infra`
- **Meta-Beschreibung:** `Videoüberwachung für Unternehmen im Raum Hamburg und Hannover. ProVision Infra plant und installiert dein Kamerasystem, mit Alarm aufs Handy.`
- Reiter **Social**: Bild `kamera-vorschau-1200x630-1.jpg`, Titel `Wir schützen dein Unternehmen mit Kamera- & Videoüberwachung`,
  Beschreibung wie die Meta-Beschreibung (Facebook und X/Twitter).
- Reiter **Erweitert**: „Cornerstone-Inhalt“ ist eingeschaltet, „Erlaube Suchmaschinen, diese Seite anzuzeigen“ steht auf Ja.

Dann **Aktualisieren** klicken. Was sonst noch für Suchmaschinen eingebaut ist (Überschriften, Strukturdaten,
FAQ-Daten), steht in `TECHNIK-CHECK.md` unter „SEO-Optimierung“ und braucht keine Pflege von Hand.

### Google Search Console (erledigt am 26.10.2026)

Im Google-Konto hey@provision-infra.de gibt es jetzt die Property `https://provision-infra.de/`. Google hat die
Inhaberschaft automatisch über den Tag Manager bestätigt (der Container auf der Website muss dafür bleiben). Die Sitemap
`sitemap_index.xml` ist eingereicht und erfolgreich gelesen, die Kameraseite ist laut URL-Prüfung „auf Google“ und
indexiert, Produkt-, Rezensions- und Navigationspfad-Daten werden als gültig erkannt. Eine erneute Indexierung nach den
SEO-Änderungen ist beantragt.

Nach größeren Änderungen an der Seite: [search.google.com/search-console](https://search.google.com/search-console)
öffnen, oben `https://provision-infra.de/kamerasysteme/` in die Suchleiste eingeben, **Indexierung beantragen** klicken.

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

## Zwei Handgriffe für dich (je eine Minute)

1. **Spam-Schutz des Formulars:** Formulare → „Anfrageformular Kamerasysteme“ → Einstellungen → Formulareinstellungen →
   „Anti-Spam-Honeypot“ einschalten → speichern. Das Feld ist unsichtbar, Besucher merken nichts. Ich durfte diese Einstellung
   nicht selbst ändern.
2. **Testbenutzer löschen:** Benutzer → „claude-test“ → Löschen, Inhalte deinem eigenen Benutzer zuordnen.

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
