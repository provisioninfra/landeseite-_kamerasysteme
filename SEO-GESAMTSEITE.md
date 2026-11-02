# SEO-Audit und Maßnahmenplan für die gesamte Website (Stand 02.11.2026)

Erhoben am 02.11.2026 auf provision-infra.de: alle 23 veröffentlichten Seiten per Abruf geprüft (Titel, Beschreibung,
Robots-Angaben, Überschriften, Strukturdaten, Bilder, interne Links), dazu robots.txt, Sitemap, Weiterleitungen,
Google-Suggest zu Schließanlagen-Begriffen und Lighthouse-Messungen (Handy). Rohdaten liegen nicht im Repo.

## 1. Ist-Zustand in Kürze

| Seite | Titel (Zeichen) | Wörter | Eingehende interne Links | Auffälligkeiten |
|---|---|---|---|---|
| Startseite `/` | 59 | 2.446 | von Karriere, Zutrittssystem, Kameraseite | H1 ohne „Schließanlage“, kein Link auf /zutrittssystem/ und die Stadtseiten, keine klickbare Telefonnummer |
| `/zutrittssystem/` | 62 | 940 | nur von Karriere | Thema überschneidet sich mit der Startseite, 40 Bilder ohne Alt-Text, doppelte H2, wenig Text |
| `/kamerasysteme/` | 60 | 1.908 | von Startseite, Karriere | in Ordnung; Überschriften-Dubletten durch Desktop/Handy-Varianten |
| `/lueneburg/` | 60 | 1.966 | keine (nur Sitemap) | verwaist, verlinkt selbst keine andere Seite, 29 % Textüberschneidung mit Uelzen |
| `/uelzen/` | 58 | 2.259 | keine (nur Sitemap) | verwaist, verlinkt selbst keine andere Seite |
| `/karriere/` | 50 | 1.691 | von allen Hauptseiten | in Ordnung (JobPosting-Schema, FAQ) |

Technisch sauber: http→https und www→ohne www leiten um (301), Schrägstrich-Varianten leiten um, 404 liefert 404,
HSTS gesetzt, robots.txt offen, Sitemap mit genau den sechs indexierbaren Seiten, alle Hilfsseiten (Kontakt, Termin,
Danke, AGB, Impressum, Datenschutz, Testseiten) stehen auf noindex. Yoast-Grundeinstellungen passen.

## 2. Maßnahmen nach Priorität

### A. Sofort (Risiko oder Quick Win, je unter einer Stunde)

1. **Bewertungs-Schema „Product“ entfernen.** Auf jeder Seite (auch den noindex-Seiten) steckt ein JSON-LD vom Typ
   `Product` mit Namen „ProVision Infra“, 5,0 Sternen und 126 Bewertungen. Das ist das ProvenExpert-Siegel. Google
   erlaubt Sterne-Snippets nicht für ein Unternehmen, das sich als Produkt ausgibt, und wertet das als irreführende
   Strukturdaten; mögliche Folge ist eine manuelle Maßnahme gegen die ganze Domain. Lösung: im ProvenExpert-Konto das
   Siegel ohne „Rich Snippets“ einbinden (oder das Schema im Widget-Code abschalten). Die sichtbaren Sterne bleiben.
2. **BugHerd aus dem Live-Betrieb nehmen.** Das Feedback-Skript lädt auf allen Seiten für alle Besucher, kostet
   Ladezeit und hat auf einer Live-Seite nichts verloren. Nur einbinden, solange aktiv getestet wird.
3. **Interne Verlinkung schließen.** Die Startseite verlinkt /zutrittssystem/ nicht, niemand verlinkt /lueneburg/ und
   /uelzen/, und die Stadtseiten führen nirgendwohin. Konkret: Footer-Zeile „Leistungen“ um „Zutrittssystem“ ergänzen,
   neue Footer-Zeile „Einsatzgebiet: Lüneburg | Uelzen | Hamburg | Hannover“ (Stadtseiten verlinkt), auf den Stadtseiten
   im Text auf die Leistungsseiten verlinken, auf der Kameraseite im Standort-Abschnitt auf die Stadtseiten.
4. **Klickbare Telefonnummer** (`tel:`) in Kopfzeile oder Footer von Startseite, Zutrittssystem- und Kameraseite. Für
   lokale Suchen und für Besucher am Handy ist der Anruf der kürzeste Weg; Karriere und Stadtseiten haben sie schon.
5. **Search-Console-Property auf alle sechs Seiten anwenden:** nach den Änderungen für jede Seite „Indexierung
   beantragen“ und unter „Verbesserungen“ prüfen, ob das Product-Schema verschwindet.

### B. Diese Woche (Struktur und Inhalt der Hauptseiten)

6. **Startseite und Zutrittssystem-Seite voneinander abgrenzen.** Beide zielen auf „Schließanlage und Zutrittssystem“
   (Titel: „Schließanlagen & digitale Zutrittssysteme“ gegen „Elektronische Schließanlage & Zutrittssystem“). Google
   muss sich dann für eine entscheiden, meist zum Nachteil beider. Vorschlag für die Rollenverteilung:
   - Startseite: Marke plus Kernleistung „digitale Schließanlage für Unternehmen“. H1 angleichen, zum Beispiel
     „Digitale Schließanlage für dein Unternehmen: geplant, installiert, betreut“.
   - /zutrittssystem/: das Leistungspaket „Zutrittsmanagement mit Rundum-Service“ mit den drei Paketen (Essential,
     Professional, Enterprise). Titel etwa „Zutrittskontrolle als Service: 3 Pakete | ProVision Infra“, H1 passend,
     Text von 940 auf 1.500 bis 2.000 Wörter ausbauen (Leistungsumfang je Paket, Ablauf, Preise oder Preislogik, FAQ).
7. **Suchabsicht „Kosten“ bedienen.** Google-Suggest zeigt bei fast jedem Schließanlagen-Begriff die Ergänzung
   „kosten“ (digitale Schließanlage kosten, elektronische Schließanlage mit chip kosten, transponder schließanlage
   kosten, schließanlage kosten schlüssel verloren). Ein eigener Abschnitt oder eine Ratgeber-Seite „Was kostet eine
   digitale Schließanlage?“ mit Preisrahmen je Türanzahl und Technik (Zylinder, Transponder, App), Montage und
   laufenden Kosten holt diese Anfragen ab. Ohne Zahlen bleibt die Seite wirkungslos; Spannen reichen.
8. **Stadtseiten einzigartig machen.** Lüneburg und Uelzen teilen 29 % ihres Textes. Je Seite drei bis fünf lokale
   Belege: Referenzen oder Branchen aus der Stadt, Anfahrtszeit ab Bad Bevensen, Ansprechpartner, Gewerbegebiete,
   lokale Kundenstimme. Weitere Stadtseiten nur dort, wo echte Nachfrage ist: Google-Suggest kennt „schließanlage
   hamburg“, „zutrittskontrolle hamburg“, „videoüberwachung lüneburg“ und „sicherheitstechnik lüneburg“, aber keine
   Kombination mit Uelzen oder Bad Bevensen. Hamburg und Hannover lohnen sich als nächste Seiten, aber nur mit
   eigenem Inhalt; zehn Kopien derselben Seite wären eine „Doorway“-Falle.
9. **Überschriften bereinigen.** Desktop- und Handy-Varianten derselben Überschrift stehen zweimal als H2 im Code
   (Gründer-Abschnitt, FAQ-Titel), auf der Startseite folgen H6 direkt auf H2. Die ausgeblendete Variante als
   „div“ setzen (Elementor: HTML-Tag der Überschrift) oder eine Überschrift mit responsivem Umbruch verwenden.
10. **Alt-Texte** der inhaltlichen Bilder nachtragen, vor allem auf /zutrittssystem/ (Produktfotos, Pakete). Icons
    und Linien dürfen leer bleiben.

### C. Dieser Monat (Sichtbarkeit aufbauen)

11. **Google-Unternehmensprofil** für Bad Bevensen vollständig pflegen: Kategorien (Sicherheitsdienst, Schlüsseldienst,
    Alarmanlagenanbieter), Leistungen mit Beschreibung, Einsatzgebiet, Fotos aus Projekten, wöchentliche Beiträge,
    aktiv um Google-Bewertungen bitten (bisher liegen die 126 Bewertungen bei ProvenExpert, Google zeigt sie nicht).
    Profil-Link in `sameAs` der LocalBusiness-Strukturdaten aufnehmen.
12. **Einträge und Links aus der Region und der Branche:** IHK Lüneburg-Wolfsburg, Handwerkskammer, Gelbe Seiten,
    11880, Das Örtliche, Partnerverzeichnisse der verbauten Hersteller (zum Beispiel Fachpartner-Suchen von
    SimonsVoss, ABUS, Winkhaus, je nachdem, was verbaut wird), Wirtschaftsförderung Landkreis Uelzen, lokale Presse zu
    Projekten. Jeder Eintrag mit identischem Namen, Adresse und Telefonnummer wie im Impressum.
13. **Hersteller- und Systemseiten.** Suggest zeigt starke Nachfrage zu Marken („digitale schließanlage simonsvoss“,
    „transponder schließanlage abus“, „elektronischer schließzylinder testsieger“). Eine Seite je verbautem System
    („SimonsVoss Schließanlage installieren lassen“ mit Vorteilen, Grenzen, Kosten, Referenz) zieht Besucher, die schon
    eine Technik im Kopf haben.
14. **Ratgeber-Reihe** (je 800 bis 1.500 Wörter, mit FAQ-Schema, untereinander und zu den Leistungsseiten verlinkt):
    „Schlüsselverlust in der Firma: was jetzt zu tun ist und was die Versicherung zahlt“, „Schließanlage nachrüsten:
    mechanisch zu digital in drei Schritten“, „Transponder, Chip oder App: welcher Zugang passt zu welchem Betrieb“,
    „Nutzungsdauer und Wartung digitaler Schließanlagen“, „Videoüberwachung auf dem Betriebsgelände: was erlaubt ist“
    (die Kameraseite liefert die FAQ-Basis). Das sind die Fragen, die Suggest zu den Kernbegriffen anzeigt.
15. **Referenzen-Seite** mit drei bis fünf echten Projekten (Branche, Türen, Technik, Ergebnis, Zitat). Einzigartiger
    Inhalt, Vertrauen und natürliche Verlinkung zu Leistungs- und Stadtseiten.

### D. Technik und Ladezeit (laufend)

16. **Ladezeit am Handy** ist die größte technische Schwäche (Messwerte in Abschnitt 3). Hebel in dieser Reihenfolge:
    BugHerd entfernen; WP Rocket „JavaScript verzögert ausführen“ für GTM, Meta-Pixel und ProvenExpert aktivieren;
    Hero-Bild je Seite vorladen (preload) und als WebP in Anzeigegröße ausliefern; Hintergrundvideos erst nach dem
    ersten Bild laden; Elementor „Verbesserte Asset-Ladung“ und „Optimierte DOM-Ausgabe“ einschalten; Anzahl der
    Elemente pro Seite reduzieren (die Startseite liefert 94 Bilder). Ziel: LCP unter 2,5 s, TBT unter 300 ms.
17. **Hosting prüfen.** Der Server beantwortet bereits wenige parallele Abrufe mit 429 und 502 und braucht für die
    gecachte Startseite über eine Sekunde bis zum ersten Byte. Ein CDN mit Cache am Rand (zum Beispiel Cloudflare)
    oder ein stärkerer Tarif verbessert Ladezeit und Stabilität für alle Seiten auf einmal.
18. **Weiterleitungskette** `http://www.…` → `https://www.…` → `https://…` auf einen Schritt kürzen (Serverkonfiguration).
19. **Strukturdaten vereinheitlichen.** Die LocalBusiness-Angaben sind auf allen Seiten konsistent (Name, Adresse,
    Telefon), nur die Karriere-Seite nutzt `#organization` statt `#organisation` als Kennung und damit eine zweite
    Entität. Eine Kennung für alle. Auf der Startseite fehlt der Service-Typ für Schließanlagen in der Breite, wie ihn
    die Stadtseiten haben.
20. **Kleinkram:** RSS-Feed-Link und xmlrpc.php im Kopf entfernen (kein Nutzen, xmlrpc ist ein Angriffsziel), IndexNow
    in Yoast einschalten (Bing, DuckDuckGo und KI-Suchen bekommen Änderungen sofort), Bing Webmaster Tools anlegen,
    GA4-Ziele für Formular und Calendly, damit sich Rankings an Anfragen messen lassen.

## 3. Lighthouse (Handy, simuliertes Mobilfunknetz)

| Seite | Leistung | SEO | Barrierefreiheit | LCP | CLS | Blockierzeit | Übertragung |
|---|---|---|---|---|---|---|---|
| Startseite | 44 | 100 | 98 | 4,5 s | 0,007 | 3.910 ms | 15,4 MB |
| /zutrittssystem/ | 47 | 100 | 98 | 3,8 s | 0,204 | 1.280 ms | 8,7 MB |
| /lueneburg/ | 60 | 92* | 99 | 4,1 s | 0,033 | 780 ms | 3,8 MB |
| /karriere/ | 61 | 92* | 100 | 4,3 s | 0,003 | 750 ms | 2,4 MB |
| /kamerasysteme/ (26.10.) | 43 | 100 | 99 | 7,8 s | 0,046 | 1.170 ms | – |

\* Die 92 entsteht allein durch die Prüfung „robots.txt gültig“, die während der Messung an der Drosselung des Hosters
scheiterte; die Datei ist gültig (siehe Abschnitt 1). Zielwerte für gute Core Web Vitals: LCP unter 2,5 s, CLS unter
0,1, Blockierzeit unter 300 ms.

Ursachen laut Messung:

- **Startseite:** zwei Hero-Videos (2,7 MB und 2,3 MB) laden am Handy beide, dazu acht Lottie-Animationen der
  Desktop-Variante mit je knapp 0,9 MB (zusammen etwa 7 MB), obwohl sie am Handy nicht sichtbar sind. Google Tag
  Manager blockiert 675 ms, das Meta-Pixel 374 ms. Größtes sichtbares Element ist ein Textabsatz, der auf Schriftarten
  und Layout wartet.
- **Zutrittssystem:** sechs Lottie-Dateien (zusammen etwa 5 MB), ein Video (0,8 MB), ein 450-KB-PNG; der
  Layout-Sprung (CLS 0,20) kommt vom Hintergrundvideo-Container und einem fixierten Element, die nach dem Laden
  Platz verschieben.
- **Alle Seiten:** BugHerd, ProvenExpert und Tag Manager laden vor dem Inhalt.

Was die Messwerte am schnellsten verbessert: Lottie-Widgets nur auf Desktop laden („Responsive“ ausblenden reicht
nicht, die Datei lädt trotzdem) oder durch statische SVG/CSS ersetzen und im Widget „Lazy Load“ einschalten; das
Handy-Video wie auf der Kameraseite erst laden, wenn der Block sichtbar ist; Videos auf 1080p und unter 1 MB
komprimieren; Tag Manager und Pixel über WP Rocket verzögert starten; dem Hero-Container eine feste Mindesthöhe geben
(gegen den Layout-Sprung).

Zum Vergleich: die Kameraseite stand nach der Optimierung bei SEO 100, Barrierefreiheit 99, Leistung 43 (Handy) und
87 (Desktop). Die Werte der Leistung sind vor allem durch Drittskripte, Videos und die Elementor-Seitengröße begrenzt.

## 4. Suchbegriffe mit echter Nachfrage (Google-Suggest, Deutschland)

- Kaufnah: elektronische Schließanlage unternehmen, elektronisches Schließsystem gewerbe, zutrittssystem firma,
  zutrittskontrolle unternehmen, schließanlage hamburg, zutrittskontrolle hamburg, videoüberwachung lüneburg,
  sicherheitstechnik lüneburg.
- Kosten: digitale schließanlage kosten, elektronische schließanlage mit chip kosten, transponder schließanlage
  kosten, schließanlage kosten schlüssel verloren.
- Technik und Vergleich: elektronische schließanlage mit transponder / mit chip / mit schlüssel, elektronischer
  schließzylinder nachrüsten / testsieger / mit fingerabdruck, transponder schließanlage nachrüsten, digitale
  schließanlage vergleich / test / nutzungsdauer.
- Marken: digitale schließanlage simonsvoss, transponder schließanlage abus, elektronische schließanlage winkhaus.
- Problemfall: schlüsselverlust firma, schlüsselverlust firma versicherung.
- Ohne messbare Nachfrage: Kombinationen mit Uelzen und Bad Bevensen (Stadtseiten dort nur als lokale Landeseiten
  für das Unternehmensprofil und Empfehlungen sinnvoll, nicht als Ranking-Ziel).

## 5. Reihenfolge, wenn die Zeit knapp ist

1. Product-Schema abschalten, BugHerd entfernen, Footer-Links auf Zutrittssystem und Stadtseiten, Telefonnummer.
2. Startseite und Zutrittssystem-Seite abgrenzen, Kosten-Abschnitt schreiben.
3. Google-Unternehmensprofil pflegen und Bewertungen auf Google holen.
4. Ladezeit am Handy mit WP Rocket und Bildformaten verbessern.
5. Ratgeber, Hersteller- und Referenzseiten nach und nach ergänzen, jeweils in der Search Console beantragen.
