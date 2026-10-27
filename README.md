# Landingpage: Kamera- & Videoüberwachung – ProVision Infra

Statische Unterseite (HTML/CSS/JS) im Look der Liveseite www.provision-infra.de.
Unabhängig vom WordPress/Elementor-System der Hauptseite und von anderen Projekten.

## Lokal ansehen

Die Datei `index.html` lässt sich per Doppelklick öffnen. Chrome zeigt dann wegen einer
Browser-Einschränkung die Ersatzschrift statt Poppins; mit einem lokalen Server stimmt alles:

```bash
python3 -m http.server 8080
# dann http://localhost:8080 im Browser öffnen
```

## Struktur

- `index.html` – Seite (Header, Hero, Logo-Rahmen mit drei Punkten, Was ohne Kameras passiert, So arbeiten wir, Stell dir mal vor, Und genau das wird möglich, Ablauf der Zusammenarbeit, Footer)
- `assets/css/style.css` – Styles (Farben/Schrift wie Liveseite: Navy #010d30, Gelb #fbc91b, Poppins)
- `assets/js/main.js` – Hero-Video-Steuerung, mobile Navigation, Scroll-Animationen der Ablauf-Sektion
- `assets/js/lottie_light.min.js` – lottie-web 5.12.2, Light-Build (Timeline-Animation)
- `assets/js/ablauf-timeline.js` – Lottie-Timeline der Startseite (Ablauf der Zusammenarbeit), wird bei Bedarf nachgeladen
- `assets/video/hero.mp4` – Hero-Hintergrundvideo (siehe `assets/video/README.md`)
- `assets/img/` – Logo, Google-Icon, Favicons
- `assets/fonts/` – Poppins (lokal ausgeliefert, kein Abruf bei Google)

## Hero-Animation

Wie auf der Liveseite: Hintergrundvideo, autoplay, stumm, einmalig, bleibt auf dem letzten Bild stehen.
Falls das Video nicht geladen werden kann, läuft eine animierte SVG-Szene (Kamera schwenkt, Status Rot → Grün).

## Dokumente

- `ANLEITUNG-WORDPRESS.md` – Schritt-für-Schritt-Anleitung für Laien: Seite als Unterseite auf provision-infra.de veröffentlichen
- `TECHNIK-CHECK.md` – Ergebnis des Technik- und Skalierungs-Checks vor dem Livegang
- `SEO-KEYWORDS.md` – Keyword-Karte (Google-Suggest-Auswertung, Zuordnung zur Seite, offene Hebel außerhalb der Seite)

## WordPress: die eigentliche Seite

Die Landingpage ist in WordPress veröffentlicht („Kamera- & Videoüberwachung“, Seiten-ID 4313,
`/kamerasysteme/`). Sie wurde aus den Original-Bausteinen der Startseite zusammengesetzt und über den
Speicherweg des Elementor-Editors gespeichert. Alle Texte sind native Elementor-Elemente.

- `tools/build_from_homepage.py` – baut die Seite aus den Startseiten-Bausteinen zusammen
- `tools/kamera-linien.html` – Skript und Stil für die Leuchtlinie und das Aufleuchten der Kästen in „Stell dir mal vor“
- `elementor/quelle-startseite.json` – Elementor-Daten der Startseite (per WordPress-Export gelesen, nur Quelle)
- `elementor/medien.json`, `elementor/icons.json` – IDs/URLs der hochgeladenen Kamera-Medien und Icons
- `elementor/seo.json` – SEO-Titel, Meta-Beschreibung, Fokus-Keyphrase und Vorschau-Titel der Seite (vom Composer geschrieben, in Yoast eingetragen)
- `elementor/geo.json` – Geokoordinaten des Firmensitzes für die LocalBusiness-Strukturdaten
- `elementor/kamera-seite.elements.json` – Elemente + Seiteneinstellungen (Stand, der in WordPress gespeichert ist)
- `elementor/landingpage-kamerasysteme.json` – dieselbe Seite als importierbare Elementor-Vorlage (Sicherung)
- `tools/menue_handy.py` – Kopfleisten-Menü: CSS und Skript, damit „Mehr“ nur am Bildschirm aufklappt und das Handy-Menü
  flach ist (von beiden Build-Skripten genutzt)
- `tools/startseite_link.py` – Startseite: Teaser „Videoüberwachung aus einer Hand“, Footer-Zeile „Leistungen“, feste
  Footer-Menüs und flaches Handy-Menü (liest die Sicherung, schreibt `elementor/startseite-mit-link.elements.json`)
- `elementor/startseite-sicherung-2026-10-26.json` – Sicherung der Startseite vor dieser Änderung (Elementor-Export, 23 Abschnitte)
- `elementor/startseite-mit-link.elements.json` – Startseite mit Teaser und Footer-Zeile (Stand, der in WordPress gespeichert ist)

Neu erzeugen: `python3 tools/build_from_homepage.py` (Kamera-Seite), `python3 tools/startseite_link.py` (Startseite). Die Schritte bis zur Veröffentlichung stehen in
`ANLEITUNG-WORDPRESS.md`.

## Statische Version (index.html)

Die statische HTML-Version ist eine eigenständige Vorschau mit gleichem Inhalt, aber eigenem Code.
Maßgeblich für die Veröffentlichung ist die WordPress-Seite.
