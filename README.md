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
- `SEO-GESAMTSEITE.md` – SEO-Audit und priorisierter Maßnahmenplan für alle Seiten der Website (02.11.2026)
- `SEO-CHECK-2026-11.md` – ausführlicher SEO-Check mit Ziel „Platz 1 in Norddeutschland“: Antworten des Kunden, Befund (Technik,
  Inhalt, Verlinkung, lokale Signale, Autorität), Maßnahmenplan in drei Stufen, offene Zulieferungen (17.11.2026)
- `TRACKING-CHECK.md` – Prüfung der Meta-Pixel-Events im Tag Manager gegen die Formular-Logik, mit Korrekturanleitung (02.11.2026)
- `tools/siegel_handy.py` – schwebendes ProvenExpert-Siegel auch auf dem Handy zeigen (Ausblendung entfernen)
- `tools/schlachthof_seite.py` – Unterseite „Videoüberwachung für Schlachthöfe“ (`/videoueberwachung-schlachthoefe/`, ID 4870) aus der
  Kamera-Seite als Vorlage: Texte je Element-ID, FAQ, Strukturdaten (07.11.2026); Rechtsgrundlage und Quellen in `recherche/`
- `elementor/seo/seite-schlachthoefe.json` – Yoast-Angaben der Schlachthof-Seite
- Umlaut-Adressen `/videoüberwachung-schlachthöfe` (und gemischte Schreibweisen) führen über drei noindex-Weiterleitungsseiten
  (IDs 4891, 4893, 4894) auf die Schlachthof-Seite; Einzelheiten in `TECHNIK-CHECK.md` (07.11.2026)
- Umlaut-Adressen der Ortsseiten `/lüneburg/`, `/bienenbüttel/`, `/lüchow/` führen über drei weitere noindex-Weiterleitungsseiten
  (IDs 4986, 4987, 4988) auf `/lueneburg/`, `/bienenbuettel/`, `/luechow/` (08.11.2026)
- `tools/bilder_tausch.py` – sechs große Hintergrund-PNGs gegen verkleinerte Versionen tauschen (alle Seiten, 17.11.2026)
- `tools/video_tausch.py` – schwere Hero-Hintergrundvideos (bis 15 MB) gegen kompakte Fassungen tauschen (3316, 4313, 4870; 17.11.2026)
- `tools/bilder_glatt.py`, `tools/hintergrund_runde3.py` – Nachbesserung zu `bilder_tausch.py` (17./18.11.2026): Leuchtflächen aus
  den unberührten Originalen geglättet (141 statt 14 Alphastufen), weitere quantisierte Bilder aus den Imagify-Sicherungen als
  hochwertiges WebP, weiche Ausblendung abgeschnittener Overlays per Element-CSS, Footer-Block auf 1400 px zentriert
- `tools/text_link.py` – eine vorhandene Textstelle in einem Elementor-Textwidget verlinken, ohne den Text zu ändern
- `tools/footer_start_angleichen.py`, `tools/zutritt_hero_handy.py` – Footer-Block ausrichten und barrierefrei machen; Zutritt-Hero: kein Desktop-Video im Handy-Hochformat (18.11.2026)
- `tools/footer_menue.py` – Footer-Menüzeile wie in der Kopfzeile (Gruppenstruktur) auf Ortsseiten und neuen Seiten; ergänzt auf den 13 Ortsseiten-Kopien das fehlende Steuerungs-Widget „Handy-Darstellung“ (20.11.2026)
- `tools/kopfmenue.py` – einheitliches Kopfmenü auf allen Seiten (20.11.2026): Zielmenü, einheitliches Handy-CSS und Maße im Nav-Widget der Pillen-Kopfzeile setzen; Pillen-Kopfzeile auf der Karriere-Seite einfügen (Menüs selbst werden per REST gepflegt, siehe TECHNIK-CHECK)
- `tools/zutritt_griff_beschriftung.py` – Zutrittssystem, Block „Zusätzlich bekommst du“: Element-CSS (Kennung `pv-griff`), mit dem die fünf Beschriftungen zwischen 768 und 1511 px den mit der Breite skalierenden Lottie-Kästchen folgen; ab 1512 px unverändert (18.11.2026)
- `tools/zutritt_footer_zeile.py` – Footer-Zeile der Zutrittssystem-Seite (Bewertung + Social-Icons, fest 1400 px) ab Elementor-Breakpoint „Laptop“ (≤ 1440 px) 100 % breit, damit sie auf Tablets und Handys quer nicht seitlich abgeschnitten wird (18.11.2026)
- `tools/footer_block.py` – Footer je Seite: Zeile „Leistungen“/„Standorte“ mit Links zu allen Seiten und Firmendaten unter dem
  Copyright (17.11.2026)
- `tools/kamera_wording.py` – Kamera-Seite (ID 4313): Wording „Kamera- & Videosicherheitssysteme“ in H1, Unterzeile und
  Leistungsüberschrift; Modus `seo`: Strukturdaten und Seitentitel „Kamera- & Videosicherheit“ für den Google-Eintrag (17.11.2026)
- `tools/agb_seite.py`, `inhalte/agb-2026-01.txt` – AGB-Seite (ID 782): Wortlaut des Kunden als Textdatei, Werkzeug baut daraus
  Vorspann, Inhaltsverzeichnis, Abschnitte (h2), Ziffern (h3), Absätze und das Muster-Widerrufsformular ins Text-Widget (15.11.2026)
- `tools/hero_text.py` – Hero der Startseite (ID 31), der Kamera-Seite (4313) und der 15 Ortsseiten (4496, 4605, 4735–4783):
  mehr Abstand unter der Überschrift am Handy, zweiter Absatz gekürzt und fett; Absatztexte je Seiten-ID in `TEXTE` (07./08.11.2026)
- `tools/karriere_hero.py` – Karriere-Seite (HTML-Widget): dasselbe im Hero per exakten Ersetzungen im Widget-HTML (07.11.2026)
- `tools/handy_darstellung.py`, `tools/handy_patch.py` – Handy-Darstellung (Hoch- und Querformat) nach der Rückmeldung mit
  sechs Punkten vom 02.11.2026: CSS je Seite aus einer ID-Tabelle, als Widget „Steuerung Handy-Darstellung“ eingesetzt
- `tools/lueneburg_wiederherstellen.py` – Lüneburg-Seite nach Überschneidung mit der Parallelsitzung wiederhergestellt (02.11.2026)
- `tools/lottie_webp.py`, `tools/ladeverhalten.py`, `tools/unsichtbar_patch.py` – unsichtbare Ladezeit- und
  Strukturdaten-Änderungen für alle Seiten (02.11.2026), Zuordnung der neuen Lottie-Dateien in `elementor/lottie-uploads-2026-11-02.json`
- `elementor/sicherung-2026-11-02/` – Exporte der sechs indexierbaren Seiten vor diesen Änderungen
- `elementor/seo/` – Yoast-Angaben für Startseite (31) und Zutrittssystem-Seite (3316)
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
