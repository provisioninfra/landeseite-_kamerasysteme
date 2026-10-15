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

## Später in WordPress einbinden (Optionen)

1. Seite in Elementor nachbauen (Hero-Container mit Video-Hintergrund, Einstellungen wie Startseite).
2. Als eigene Unterseite per HTML-Widget/Custom-HTML einfügen.
3. Als statische Seite in einem Unterordner oder auf einer Subdomain (z. B. kamera.provision-infra.de) hosten.
