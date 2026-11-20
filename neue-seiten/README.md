# Neue Seiten (Welle 1, ab 20.11.2026)

Neue Seiten für provision-infra.de nach dem Vorschlag `../SEO-VORSCHLAG-SEITENARCHITEKTUR-2026-11.md`. Alle Seiten entstehen aus
einem frischen Elementor-Export der Uelzen-Seite (#4605) als Designvorlage: Kopf, Hero, Karten, Kundenstimmen, Ablauf,
Gründer, FAQ, Partner und Footer bleiben im Design der bestehenden Seiten, nur Texte, Abschnitte, FAQ, Schema und Menü
werden ersetzt. Die Startseite wird laut Kunde nicht verändert (nur Technik erlaubt).

| Seite | Datei | WordPress-ID | Fokus-Suchbegriff |
|---|---|---|---|
| /mechanische-schliessanlagen/ | `mechanische_schliessanlagen.py` | 5364 | mechanische Schließanlage |
| /standorte/ | `standorte.py` | 5368 | Schließanlagen Norddeutschland |
| /schliesssysteme/ | `schliesssysteme.py` | 5375 | Schließsysteme |
| /schliessanlage-hausverwaltung/ | `schliessanlage_hausverwaltung.py` | 5379 | Schließanlage Mehrfamilienhaus |
| /ratgeber/ | `ratgeber.py` | 5383 | Ratgeber Schließanlagen |
| /ratgeber/videoueberwachung-firmengelaende/ | `ratgeber_videoueberwachung_firmengelaende.py` | 5387 | Videoüberwachung Firmengelände |
| /ratgeber/schluessel-verloren-unternehmen/ | `ratgeber_schluessel_verloren.py` | 5391 | Schlüssel verloren Firma |
| /ratgeber/elektronischen-schliesszylinder-nachruesten/ | `ratgeber_zylinder_nachruesten.py` | 5395 | elektronischen Schließzylinder nachrüsten |

Menüs: „Menü Leistungsseiten“ (ID 20, Slug `menue-leistungsseiten`, Kopf) und „Menü Leistungsseiten Footer“ (ID 21).

Angaben des Kunden (20.11.2026): mechanisch EVVA; Leistungen Beratung, Planung, Projektierung, Schließplan, Nachschlüssel,
Austausch bei Verlust, Wartung und Erweiterung; elektronisch EVVA AirKey, EVVA Xesar, SimonsVoss (System 3060, AX,
MobileKey, FORTLOX), Keyota, Keyrent, NUKI; Autor der Ratgeber Jannes Heino Baumann; keine Preise und Referenzen
(neutral formuliert).

## Bauen

```bash
python3 -I bau.py <export-4605.json> mechanische_schliessanlagen.py <ausgabe.json>   # erzeugt auch <ausgabe>-texte.md
```

`bau.py` bricht ab bei doppelten Element-IDs oder Ankern und zu langen SEO-Werten und listet Reste aus der Vorlage
(Uelzen-Bezüge). Speichern: `werkzeuge/neue_seite.mjs` (Entwurf anlegen), `werkzeuge/save.mjs` (Elementor),
`werkzeuge/yoast2.mjs` (SEO-Werte), Prüfung mit `werkzeuge/vorschau.mjs`. Zugangsdaten nie im Repo.

Texte zum Gegenlesen: `texte/`.

## Stand 20.11.2026

- 17:3x UTC: alle acht Seiten nach Freigabe des Kunden veröffentlicht, öffentlich geprüft (HTTP 200, Canonical,
  `index, follow`, eine H1, strukturierte Daten: Service bzw. Article mit Autor, FAQPage, ItemList) und in der
  Yoast-Sitemap enthalten.
- Menü „Menü Kamerasysteme (Header)“ (17): unter „Mehr“ ergänzt um Mechanische Schließanlagen, Schließsysteme im
  Vergleich, Standorte, Ratgeber. „Secandary Menu“ (15, Zutrittssystem): Standorte und Ratgeber ergänzt.
  Menü „Main“ (6) bleibt unverändert, weil die Startseite es nutzt. Menüs der Ortsseiten (18, 19) unverändert:
  ihre Fußnavigation nutzt dasselbe Menü, ein Untermenü würde dort aufklappen.
- Footer-Block auf allen Seiten außer der Startseite (Kundenvorgabe): „Leistungen“ (a1f0072) um Mechanische
  Schließanlagen, Schließsysteme und Ratgeber ergänzt, „Standorte“ (a1f0073) um „Alle Standorte“
  (`werkzeuge/footer_transform.mjs`, je Seite frischer Export und ein Speichervorgang).
- 18:00–18:10 UTC: alle acht URLs in der Search Console (Property `https://provision-infra.de/`) über die URL-Prüfung
  zur Indexierung beantragt; Bestätigung „Indexierung wurde beantragt“ je URL per Screenshot geprüft. Hinweis: Die
  Adresse `/search-console/inspect?...&id=<URL>` liefert inzwischen 404; die Prüfung geht über das Suchfeld oben.
