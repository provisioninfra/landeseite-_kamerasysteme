# Regeln für Arbeiten an provision-infra.de (WordPress)

Gilt für jede Claude-Sitzung, die mit dem WordPress-Zugang des Kunden arbeitet. Zugangsdaten stehen nicht in
diesem Repo; der Kunde gibt sie im Chat. Sie gehören nie in Dateien, Commits, Logs, Screenshots oder Chat-Ausgaben.

## Nur lesen, nicht ändern

- Alle bestehenden Live-Seiten: Startseite (ID 31), /kontakt (42), /termin (3617), /termin-gebucht (823),
  /danke (34), /danke-seite (2465), Entwürfe des Kunden (z. B. 4033) sowie die Kamera-Seiten /kamerasysteme (4313),
  /kontakt-kamerasysteme (4371), /termin-kamerasysteme (4391), /termin-gebucht-kamerasysteme (4392).
- Menüs, Plugins, Theme-, Elementor-, Yoast-, WP-Rocket-Einstellungen, Benutzer.
- Gravity-Forms-Formulare 1, 2 und 4; Einträge unter „Landeseiten Forms“ (2459, 828, 4368).
- Mediathek-Dateien anderer Seiten (nicht löschen, nicht ersetzen).
- Die Startseite ist Design-Vorlage: Bausteine auslesen (WordPress-Export `export.php?download=true&content=page`,
  Feld `_elementor_data`), nie bearbeiten.

## Erlaubt

- Neue Seiten anlegen (zuerst Entwurf, per Vorschau prüfen, dann veröffentlichen), eigene Medien hochladen.
- Kopien bestehender Formulare: Gravity Forms → Import/Export → exportieren, anpassen, als neues Formular importieren.
  „Landeseiten Forms“: Duplizieren-Link nutzen und nur die Kopie umstellen.
- Keine Test-Einträge in Formulare absenden (erzeugt Einträge und E-Mails), außer der Kunde bittet darum.

## Bewährte Technik

- Prüfen der Live-Seite mit `?nowprocket=1` (WP-Rocket-Cache umgehen); Cookie-Banner mit
  „Nur essenzielle Cookies akzeptieren“ schließen.
- Seite anlegen: REST `POST /wp-json/wp/v2/pages` mit Cookie-Login und `X-WP-Nonce` (aus `window.wpApiSettings.nonce`
  einer Admin-Seite), Status `draft`.
- Elementor-Inhalt speichern: Editor der eigenen Seite öffnen (`post.php?post=ID&action=elementor`) und
  `elementorCommon.ajax.addRequest('save_builder', { data: { status, elements, settings } })` aufrufen.
  Vorlagen-Import verliert das Design.
- Medien: REST `POST /wp-json/wp/v2/media` (multipart).
- Yoast: im Block-Editor der eigenen Seite über `wp.data.dispatch('yoast-seo/editor')` (`setNoIndex`, `setNoFollow`,
  `setFacebookPreviewImage`, `setFacebookPreviewTitle`, `setFacebookPreviewDescription`, `updateData`), danach
  `wp.data.dispatch('core/editor').savePost()`.
- Headless Chromium spielt kein H.264 ab; Hintergrundvideos per Standbild simulieren.
- Details: ANLEITUNG-WORDPRESS.md, TECHNIK-CHECK.md, tools/build_from_homepage.py.
