# Sicherung der sechs indexierbaren Seiten vom 02.11.2026

Exporte aus dem Elementor-Editor (Elemente, Seiteneinstellungen, Titel, Status) unmittelbar vor den unsichtbaren
SEO-/Ladezeit-Änderungen (siehe TECHNIK-CHECK.md, Abschnitt „Unsichtbare Änderungen auf allen Seiten“). Enthalten die
Bearbeitungen vom 29.10.2026, die nicht aus diesem Repo stammen.

| Datei | Seite |
|---|---|
| seite-31.json | Startseite |
| seite-3316.json | /zutrittssystem/ |
| seite-4313.json | /kamerasysteme/ |
| seite-4496.json | /lueneburg/ |
| seite-4605.json | /uelzen/ |
| seite-4408.json | /karriere/ (unverändert gelassen) |

Wiederherstellen: Datei mit `PAGE_ID`, `FILE` und `SAVE_STATUS=publish` über den Speicherweg des Elementor-Editors
speichern (Skript `save_page.mjs` aus der Sitzung, Ablauf in TECHNIK-CHECK.md). Die veränderten Fassungen entstehen
daraus mit `python3 -I tools/unsichtbar_patch.py sicherung.json ziel.json lottie-uploads.json`.
