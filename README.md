# Landingpage: Kamera- & Videoüberwachung – ProVision Infra

Statische Unterseite (HTML/CSS/JS) im Look der Liveseite www.provision-infra.de.
Unabhängig vom WordPress/Elementor-System der Hauptseite und von anderen Projekten.

## Lokal ansehen

```bash
python3 -m http.server 8080
# dann http://localhost:8080 im Browser öffnen
```

## Struktur

- `index.html` – Seite (aktuell: Header + Hero, weitere Sektionen folgen)
- `assets/css/style.css` – Styles (Farben/Schrift wie Liveseite: Navy #010d30, Gelb #fbc91b, Poppins)
- `assets/js/main.js` – Hero-Video-Steuerung, mobile Navigation, Scroll-Animationen der Ablauf-Sektion
- `assets/js/lottie.min.js` – lottie-web 5.12.2 (Timeline-Animation)
- `assets/js/ablauf-timeline.json` – Lottie-Timeline der Startseite (Ablauf der Zusammenarbeit)
- `assets/video/hero.mp4` – Hero-Hintergrundvideo (siehe `assets/video/README.md`)
- `assets/img/` – Logo, Google-Icon

## Hero-Animation

Wie auf der Liveseite: Hintergrundvideo, autoplay, stumm, einmalig, bleibt auf dem letzten Bild stehen.
Falls das Video nicht geladen werden kann, läuft eine animierte SVG-Szene (Kamera schwenkt, Status Rot → Grün).

## In WordPress / Elementor einbinden

Im Ordner `elementor/` liegt eine importierbare Elementor-Vorlage, in der jeder Text ein eigenes
Elementor-Widget ist (Überschrift, Texteditor, Button) und sich nach dem Import direkt im Editor
bearbeiten lässt.

- `elementor/landingpage-kamerasysteme.json` – die Vorlage (Hero, Kernbotschaft, fünf Unterschiede, Ablauf)
- `elementor/custom.css` – das Styling, liegt in der Vorlage bereits im „Benutzerdefinierten CSS“ der Seite
- `tools/build_elementor_template.py` – erzeugt die JSON-Datei neu (`python3 tools/build_elementor_template.py`)

### Import, Schritt für Schritt

1. `assets/video/hero.mp4` in die WordPress-Mediathek hochladen und die URL kopieren.
2. WordPress-Backend → Vorlagen (Elementor) → Gespeicherte Vorlagen → „Vorlagen importieren“ → die JSON-Datei hochladen.
3. Neue Seite anlegen → „Mit Elementor bearbeiten“ → Ordner-Symbol „Vorlage hinzufügen“ → Reiter „Meine Vorlagen“ → „Landingpage Kamera- & Videoüberwachung“ einfügen.
4. Hero-Container anklicken → Stil → Hintergrund → Video-Link: die Mediathek-URL aus Schritt 1 eintragen.
   Ebenso im Video-Widget unter dem Button (nur mobil sichtbar) die gleiche URL eintragen.
5. Seitenlayout auf „Elementor Volle Breite“ bzw. „Elementor Canvas“ stellen, je nachdem, ob Header und Footer
   der Website erscheinen sollen. Mit „Volle Breite“ kommt der Header der Startseite automatisch mit.

Hinweise:
- Das Lottie-Widget der Ablauf-Sektion verweist auf die bereits in der Mediathek vorhandene Animation der Startseite.
- Die Ablauf-Sektion lässt sich alternativ auch direkt auf der Startseite im Elementor kopieren (Rechtsklick → Kopieren)
  und auf der neuen Seite einfügen, dann ist auch die mobile Timeline exakt das Original.
- Benutzerdefiniertes CSS pro Seite ist eine Elementor-Pro-Funktion (auf provision-infra.de vorhanden).
