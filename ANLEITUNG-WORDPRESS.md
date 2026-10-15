# Anleitung: Die Kamera-Landingpage als Unterseite auf provision-infra.de veröffentlichen

Diese Anleitung ist für Menschen ohne Technik-Vorkenntnisse geschrieben. Du brauchst nur
deinen WordPress-Zugang (Administrator) und etwa 30 bis 45 Minuten. Es wird nichts an der
bestehenden Startseite verändert. Die neue Seite bleibt so lange unsichtbar, bis du sie
ganz am Ende bewusst veröffentlichst.

---

## Was du brauchst

1. **Zugang zum WordPress-Backend:** `https://www.provision-infra.de/wp-admin`
2. **Zwei Dateien aus diesem Projekt** (am besten vorher auf den Computer herunterladen):
   - `assets/video/hero.mp4` – das Hintergrundvideo
   - `elementor/landingpage-kamerasysteme.json` – die fertige Seitenvorlage
3. **Elementor Pro** muss aktiv sein. Das ist auf provision-infra.de bereits der Fall.

Die Dateien findest du auf GitHub unter
`https://github.com/provisioninfra/landeseite-_kamerasysteme` (Branch `claude/bold-darwin-ckgllr`).
Zum Herunterladen einer einzelnen Datei: Datei anklicken → oben rechts auf das Download-Symbol
(Pfeil nach unten) klicken. Beim Video erscheint eventuell „View raw“, das ebenfalls anklicken.

---

## Schritt 1: Sicherung anlegen (5 Minuten)

Auch wenn nichts schiefgehen sollte: Eine Sicherung kostet nichts und beruhigt.

1. Im Backend links auf **Werkzeuge → Daten exportieren** klicken.
2. **Alle Inhalte** auswählen → **Export-Datei herunterladen**. Die Datei auf dem Computer behalten.
3. Falls ein Backup-Plugin installiert ist (zum Beispiel UpdraftPlus, WP Vivid oder das Hosting-Backup),
   dort zusätzlich auf **Jetzt sichern** klicken.

---

## Schritt 2: Das Video in die Mediathek hochladen (5 Minuten)

1. Links im Menü auf **Medien → Datei hinzufügen** klicken.
2. Die Datei `hero.mp4` in das Feld ziehen oder über **Dateien auswählen** hochladen.
3. Nach dem Upload auf das Video klicken. Rechts erscheint das Feld **Datei-URL**.
4. Diese URL **kopieren** und zum Beispiel in eine Notiz einfügen. Sie sieht ungefähr so aus:
   `https://provision-infra.de/wp-content/uploads/2026/10/hero.mp4`

Falls das Hochladen mit einer Fehlermeldung wie „überschreitet die maximale Upload-Größe“ abbricht:
Das Video ist nur rund 0,4 MB groß, das sollte nicht passieren. Falls doch, bitte beim Hoster
nachfragen oder mir Bescheid geben.

---

## Schritt 3: Die Vorlage importieren (5 Minuten)

1. Links im Menü auf **Vorlagen** (Menüpunkt von Elementor) → **Gespeicherte Vorlagen** klicken.
2. Falls dort schon eine ältere Version von **„Landingpage Kamera- & Videoüberwachung“** liegt:
   mit der Maus darüberfahren → **In den Papierkorb**. Sonst gibt es später zwei gleichnamige Einträge.
3. Oben auf den Button **Vorlagen importieren** klicken.
4. **Datei auswählen** → `landingpage-kamerasysteme.json` → **Jetzt importieren**.
5. In der Liste erscheint jetzt der Eintrag **„Landingpage Kamera- & Videoüberwachung“**.

Das Design (Farben, Schriften, Rahmen, Abstände) ist fest in den einzelnen Elementen der Vorlage
hinterlegt. Es kommt also in jedem Fall mit, egal wie du die Nachfrage in Schritt 4 beantwortest.

Wenn beim Import eine Fehlermeldung erscheint: Den genauen Text der Meldung abfotografieren oder
kopieren und mir schicken. Dann passe ich die Datei an.

---

## Schritt 4: Die neue Unterseite anlegen (10 Minuten)

1. Links im Menü auf **Seiten → Erstellen** klicken.
2. Als Titel oben **„Kamera- & Videoüberwachung“** eintragen.
3. Auf den blauen Button **Mit Elementor bearbeiten** klicken. Der Elementor-Editor öffnet sich.
4. In der Mitte der leeren Seite siehst du ein **graues Ordner-Symbol** („Vorlage hinzufügen“).
   Darauf klicken.
5. Im Fenster oben auf den Reiter **Meine Vorlagen** wechseln.
6. Bei **„Landingpage Kamera- & Videoüberwachung“** auf **Einfügen** klicken.
   Falls gefragt wird, ob die Einstellungen der Vorlage übernommen werden sollen: **Ja** anklicken.
   Damit kommen Seitenlayout „Volle Breite“ und der dunkle Seitenhintergrund gleich mit.
7. Die Seite ist jetzt vollständig aufgebaut und sieht bereits so aus wie die Vorschau aus dem
   Projekt. Unten links auf **Aktualisieren** bzw. **Als Entwurf speichern** klicken (der kleine
   Pfeil neben dem grünen Button zeigt die Option).
8. Wenn Texte zwar da sind, aber noch nicht im Design erscheinen: Im Backend unter
   **Elementor → Werkzeuge → CSS regenerieren** klicken und die Seite neu laden.

---

## Schritt 5: Das Video einsetzen (5 Minuten)

Die Vorlage weiß noch nicht, wo dein Video liegt. Das trägst du jetzt an zwei Stellen ein.

**Stelle 1: Hintergrund des Hero-Bereichs (Desktop)**

1. Ganz oben im Hero-Bereich (dort, wo die große Überschrift steht) mit der Maus an den
   **Rand des Bereichs** fahren, bis ein **blauer Rahmen** mit einem kleinen Griff-Symbol erscheint.
   Auf dieses Griff-Symbol klicken. Links öffnet sich das Bedienfeld des Containers.
2. Oben im Bedienfeld auf den Reiter **Stil** klicken.
3. Unter **Hintergrund** ist der Typ **Video** bereits gewählt. Im Feld **Video-Link** steht ein
   Platzhalter (`…/uploads/hero.mp4`). Diesen durch die URL aus Schritt 2 ersetzen.
4. Darunter bleibt **Einmal abspielen** eingeschaltet. Das sorgt dafür, dass das Video wie auf der
   Startseite einmal durchläuft und dann stehen bleibt.

**Stelle 2: Video-Block unter dem Button (Tablet und Handy)**

1. Im Editor oben links auf das **Monitor-Symbol** (Responsive-Modus) klicken und **Mobil** wählen.
2. Nun erscheint unter dem gelben Button ein **Video-Widget**. Darauf klicken.
3. Links unter **Video → Quelle** steht **Selbst gehostet**. Das Feld **URL** ist noch leer.
   Hier die URL aus Schritt 2 eintragen (oder über **Medien auswählen** das Video aus der Mediathek wählen).
4. Wieder auf **Desktop** zurückschalten.

Unten links auf **Aktualisieren** klicken.

---

## Schritt 6: Seitenlayout prüfen (2 Minuten)

Damit die Seite den gleichen Kopfbereich (Logo und Menü) und Fußbereich wie die Startseite bekommt:

1. Unten links im Editor auf das **Zahnrad-Symbol** (Seiteneinstellungen) klicken.
2. Bei **Seitenlayout** muss **Elementor Volle Breite** stehen. Falls nicht, auswählen.
3. **Aktualisieren** klicken.

Hinweis: Die Vorlage enthält keinen eigenen Kopfbereich. Logo und Menü kommen automatisch von deiner
Website. Das ist gewollt, damit alles einheitlich bleibt.

---

## Schritt 7: Vorschau ansehen und Texte anpassen (10 Minuten)

1. Unten links auf das **Augen-Symbol** → **Vorschau** klicken. Die Seite öffnet sich in einem neuen
   Tab, so wie Besucher sie sehen würden. Sie ist für andere noch nicht erreichbar.
2. Am Handy prüfen: Den Vorschau-Link kopieren und auf dem Handy öffnen. Dafür musst du am Handy
   im WordPress-Backend eingeloggt sein, sonst wird die Vorschau nicht angezeigt.
3. **Texte ändern:** Im Editor einfach auf einen Text klicken und links im Bedienfeld im Feld
   **Titel** (bei Überschriften) oder im Texteditor (bei Fließtext) schreiben. Jede Änderung ist
   sofort in der Vorschau sichtbar.
4. **Button-Ziel ändern:** Auf den gelben Button klicken → links bei **Link** die Adresse anpassen.
   Aktuell führt er auf `https://provision-infra.de/kontakt`.
5. Nach jeder Änderung unten links **Aktualisieren** klicken.

Zwei Texte im Abschnitt „Ablauf der Zusammenarbeit“ stammen unverändert von der Startseite und
sprechen vom Schließsystem („Türen und Zutrittspunkte“, „Zutrittskonzept“). Prüfe, ob du sie für
die Kamera-Seite anpassen möchtest.

---

## Schritt 8: Adresse (URL) der Seite festlegen (2 Minuten)

1. Im Backend unter **Seiten → Alle Seiten** die neue Seite anklicken (nicht „Mit Elementor
   bearbeiten“, sondern den normalen Bearbeiten-Link).
2. Rechts in der Seitenleiste unter **Permalink** oder **URL** den Teil hinter dem Domainnamen
   anpassen, zum Beispiel auf `kamerasysteme`. Die Seite ist dann später unter
   `https://www.provision-infra.de/kamerasysteme/` erreichbar.
3. **Aktualisieren** klicken.

---

## Schritt 9: Suchmaschinen-Angaben eintragen (3 Minuten)

Auf der Website ist das Plugin **Yoast SEO** aktiv. Es sitzt unterhalb des Seiteninhalts
(normale Bearbeiten-Ansicht, nicht Elementor).

1. Bei **SEO-Titel** eintragen: `Kamera- & Videoüberwachung – ProVision Infra`
2. Bei **Meta-Beschreibung** eintragen:
   `ProVision Infra plant & installiert deine Kamera- und Videoüberwachung – damit dein Gebäude rund um die Uhr geschützt ist.`
3. Im Reiter **Social** bei **Facebook-Bild** ein Standbild aus dem Video hochladen
   (`assets/video/hero-poster.jpg` aus dem Projekt eignet sich dafür).
4. **Aktualisieren** klicken.

---

## Schritt 10: Veröffentlichen (1 Minute)

1. Seite öffnen → **Mit Elementor bearbeiten**.
2. Unten links auf den grünen Button **Veröffentlichen** klicken.
3. Die Seite ist jetzt live unter der Adresse aus Schritt 8.

---

## Schritt 11: Verlinken, damit Besucher die Seite finden (5 Minuten)

Eine Unterseite ohne Link findet niemand. Zwei einfache Wege:

**Im Menü der Website:**
1. **Design → Menüs** öffnen.
2. Links unter **Seiten** die neue Seite anhaken → **Zum Menü hinzufügen**.
3. Den neuen Eintrag per Drag-and-drop an die gewünschte Stelle ziehen → **Menü speichern**.

Hinweis: Das Menü auf der Startseite ist mit Elementor gebaut und zeigt Sprungmarken
(„Mit digitalen Schlüsseln Kosten sparen“ usw.). Wenn dort ein neuer Punkt erscheinen soll,
muss das Menü unter **Design → Menüs** bearbeitet werden, das im Elementor-Header verwendet wird.

**Als Button oder Link auf der Startseite:** Im Elementor der Startseite einen Button einfügen
und als Link die neue Adresse eintragen.

---

## Nach der Veröffentlichung: Kurzer Check

- Seite im **privaten Fenster** des Browsers öffnen (ohne Login): Wird alles angezeigt?
- **Am Handy** öffnen: Liegt das Video unter dem Button? Ist der Text gut lesbar?
- **Button klicken:** Landet man auf der Kontaktseite?
- **Google Search Console** (falls eingerichtet): Die neue URL unter „URL-Prüfung“ eintragen und
  **Indexierung beantragen**. Dann taucht die Seite schneller bei Google auf.

---

## Wenn etwas nicht klappt

| Problem | Lösung |
|---|---|
| Vorlage erscheint nicht unter „Meine Vorlagen“ | Seite im Browser neu laden. Falls weiterhin nicht: Import wiederholen. |
| Video läuft nicht | URL in beiden Stellen prüfen (Schritt 5). Die URL muss mit `.mp4` enden. |
| Design fehlt komplett (weißer Hintergrund, Standardschrift) | Es wurde noch die alte Vorlagen-Datei verwendet. Alte Vorlage unter Gespeicherte Vorlagen löschen, aktuelle `landingpage-kamerasysteme.json` importieren, Seite neu einfügen. |
| Texte sind da, Feinheiten fehlen (Icon-Kacheln, Timeline-Linie) | **Elementor → Werkzeuge → CSS regenerieren**, dann Seite neu laden. Falls weiterhin: beim Einfügen die Nachfrage mit **Ja** bestätigen. |
| Seitenhintergrund ist weiß statt dunkelblau | Zahnrad unten links → **Stil** → **Hintergrund** → Farbe `#010D30`. Oder beim Einfügen die Nachfrage mit **Ja** bestätigen. |
| Timeline-Animation im Ablauf fehlt | Das Lottie-Widget anklicken → Quelle **Externe URL** → Link prüfen. Er zeigt auf die Animationsdatei der Startseite in deiner Mediathek. |
| Seite sieht auf dem Handy seltsam aus | Browser-Cache leeren oder privates Fenster nutzen. Zusätzlich im Backend unter **Elementor → Werkzeuge → CSS regenerieren** klicken. |
| Logo und Menü fehlen oben | Schritt 6: Seitenlayout auf **Elementor Volle Breite** stellen. |

Bei allem anderen: Screenshot und kurze Beschreibung reichen, dann kümmere ich mich darum.
