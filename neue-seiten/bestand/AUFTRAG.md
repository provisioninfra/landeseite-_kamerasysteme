# Auftrag: Werbetexter-Durchgang für bestehende Seiten (nur Textdateien, NICHT speichern)

Eingabe: bestand/<datei>-alt.json = {"<element-id>|<feldpfad>": "<text oder HTML>"} in Seitenreihenfolge.
Ausgabe: bestand/<datei>-neu.json mit GENAU denselben Schlüsseln; unveränderte Felder mit identischem Wert übernehmen.

Regeln des Kunden (hart):
- keine Gedankenstriche (– — und kein " - " als Strich), kein „nicht nur … sondern auch“, keine Kontrastschablonen („X statt Y“, „kein X, sondern Y“, „X und nicht Y“)
- keine auffälligen Dreiergruppen (Aufzählungen mit drei Gliedern, drei parallele Sätze), keine vagen Autoritäten („Experten sagen“)
- wie ein erfahrener menschlicher Fachredakteur und Profi-Werbetexter: konkrete Alltagsszenen, Nutzen vor Technik, Überschriften mit Hook, wechselnde Satzlängen und Satzanfänge, aktive Verben, keine Floskeln. Du-Ansprache wie auf der Startseite (Ton: scratchpad/wp/welle2/start-texte.txt).
Nicht ändern: Kundenstimmen (Felder von testimonial-/Bewertungs-Widgets mit Namen, z. B. 177c18bd, 6308d31b, 7639481c, 426f36df, 25a6e0bf, 46ac736, 2b91cf92), Footer-Listen a1f0072/a1f0073/1f95880, Kontaktdaten/NAP, Zahlen-Zähler (prefix/suffix), Button-Texte nur bei echtem Mehrwert.
Technik:
- HTML-Auszeichnung (span-Stile, br, strong, a href) erhalten; Links und Ziel-URLs unverändert.
- Länge je Feld ungefähr halten (±20 %), Überschriften und Kartentexte eher kürzer, sonst bricht das Layout.
- SEO: Ortsname bzw. Fokusbegriff (Schließanlagen <Ort>, Videoüberwachung <Ort>, Zutrittssystem, Kamera…) in H1, H2 und erstem Absatz behalten.
- Nichts erfinden: keine neuen Zahlen, Preise, Kunden, Referenzen, Fristen oder Ortsfakten. Ortsbezug nur mit Dingen, die schon im Text stehen oder allgemein bekannt und unstrittig sind (Lage, Nachbarorte, Landkreis). Jede Ortsseite soll sich eigenständig lesen und nicht wie ein Duplikat mit ausgetauschtem Ortsnamen.
Prüfen:
  python3 -I /home/user/landeseite-_kamerasysteme/neue-seiten/werkzeuge/texte_bestand.py anwenden footer/page-<ID>-vorher.json bestand/<datei>-alt.json bestand/<datei>-neu.json /tmp/claude-0/-home-user/8101c591-dd55-5971-91e8-f9b3f727dc4d/scratchpad/wp/bestand/<datei>-test.json
  python3 -I /home/user/landeseite-_kamerasysteme/neue-seiten/textpruefung.py bestand/<datei>-test.json 2b91cf92,7cfc047c,177c18bd,6308d31b,426f36df,25a6e0bf,46ac736
(alle Pfade relativ zu /tmp/claude-0/-home-user/8101c591-dd55-5971-91e8-f9b3f727dc4d/scratchpad/wp). Treffer beheben, außer reinen Herstellerlisten, Ortslisten, Pflichtangaben und Kundenzitaten.
Nichts in WordPress speichern, nichts committen, keine Netzwerkzugriffe auf provision-infra.de. Andere Dateien als die eigenen -neu.json / -test.json nicht anfassen.
Bericht kurz auf Deutsch: je Seite die 3 wichtigsten Änderungen (alt → neu), Restbefunde mit Begründung, fachlich neue Aussagen zum Gegenlesen.
