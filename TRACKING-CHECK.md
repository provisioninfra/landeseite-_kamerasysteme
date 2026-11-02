# Tracking-Check Meta-Pixel (02.11.2026)

Geprüft: veröffentlichter Google-Tag-Manager-Container GTM-KV75JXFB (Version 11, öffentliche Datei gtm.js), alle
Gravity-Forms-Definitionen (Export) und die Zielseiten. Meta-Pixel-ID in allen Tags: 1882223199102262 (korrekt).

## Soll (Vorgabe)

| Formular | Fall | Event |
|---|---|---|
| Schließsysteme | privat, oder geschäftlich bis 5 Türen (LQ) | Lead |
| Schließsysteme | geschäftlich über 5 Türen (HQ) | SubmitApplication („Bewerbung einreichen“) |
| Kamerasysteme | privat (LQ) | Contact |
| Kamerasysteme | geschäftlich (HQ) | CompleteRegistration |

Die Einstufung passiert in Gravity Forms über die Bestätigungsseite:
- Formular 2 „Anfrageformular (1)“ (Seite /kontakt/): HQ → /termin-gebucht/, LQ → /termin/
- Formular 4 „Anfrageformular Kamerasysteme“ (/kontakt-kamerasysteme/): HQ → /termin-gebucht-kamerasysteme/, LQ → /termin-kamerasysteme/
- Formular 6 „Schließ- & Kamerasysteme“ (/kontakt-kombiniert/): geschäftlich → /termin-gebucht/, privat → /termin/
- Formular 5 „Funnel Auswahl“ (/anfrage-auswahl/) verteilt nur auf die Kontaktseiten.

## Ist (Container Version 11)

Alle Meta-Tags feuern beim Seitenaufruf (gtm.js), ausgelöst allein durch „Seiten-URL enthält …“:

| Tag | Event | Trigger (URL enthält) | Feuert tatsächlich auf |
|---|---|---|---|
| 17 | PageView | alle Seiten | alle Seiten |
| 19 | ViewContent | „kontakt“ | /kontakt/, /kontakt-kamerasysteme/, /kontakt-kombiniert/ |
| 21 | Lead | „termin“ | /termin/, /termin-gebucht/, /termin-kamerasysteme/, /termin-gebucht-kamerasysteme/ |
| 23 | Schedule | „danke“ | /danke/, /danke-seite/ |
| 26 | SubmitApplication | „termin-gebucht“ | /termin-gebucht/ und /termin-gebucht-kamerasysteme/ |

Tags für Contact und CompleteRegistration existieren nicht.

## Abweichungen vom Soll

1. **Lead feuert auf allen vier Terminseiten**, also auch bei HQ-Leads (zusätzlich zu SubmitApplication) und bei beiden
   Kamera-Fällen. Jeder HQ-Lead zählt damit doppelt, jede Kamera-Anfrage als Schließsystem-Lead.
2. **SubmitApplication feuert auch auf /termin-gebucht-kamerasysteme/** (Kamera HQ) statt CompleteRegistration.
3. **Contact und CompleteRegistration fehlen** komplett; Kamera-Anfragen lösen keines der gewünschten Events aus.
4. Nebenbefunde: Der Google-Ads-Conversion-Tag 14 feuert ebenfalls auf allen „termin“-Seiten (gleiche Doppelzählung);
   Meta-Pixel und Google-Ads-Tags laden ohne Cookie-Einwilligung (Borlabs kennt nur „facebook“ als Inhaltsblocker für
   Einbettungen, kein Tag-Manager-Service, kein Consent Mode); die Rechtsfrage sollte der Datenschutzbeauftragte
   prüfen. In Gravity Forms gilt bei Formular 2 „privat ab 16 Türen“ und bei Formular 6 „geschäftlich“ ohne
   Türenregel als HQ; das ist Absicht laut Kunde, weicht aber vom Wortlaut der Vorgabe ab.

## Korrektur im Tag Manager (fünf Minuten, Arbeitsbereich → Version veröffentlichen)

Trigger neu anlegen, Typ „Seitenaufruf“, Bedingung **Page Path ist gleich** (nicht „enthält“):

| Trigger | Page Path |
|---|---|
| Termin LQ Schließ | /termin/ |
| Termin HQ Schließ | /termin-gebucht/ |
| Termin LQ Kamera | /termin-kamerasysteme/ |
| Termin HQ Kamera | /termin-gebucht-kamerasysteme/ |

Tags:
1. Tag „Lead“ (21): alten Trigger („termin“ enthält) entfernen, Trigger „Termin LQ Schließ“ zuweisen.
2. Tag „SubmitApplication“ (26): alten Trigger entfernen, Trigger „Termin HQ Schließ“ zuweisen.
3. Tag „Lead“ duplizieren → Name „Meta Contact“, Standardereignis **Contact**, Trigger „Termin LQ Kamera“.
4. Tag „Lead“ duplizieren → Name „Meta CompleteRegistration“, Standardereignis **CompleteRegistration**, Trigger
   „Termin HQ Kamera“.
5. Optional gleich mitziehen: Google-Ads-Tag 14 ebenfalls auf die vier exakten Pfade (oder je Fall eigene
   Conversion-Aktionen) statt „enthält termin“.
6. Vorschau prüfen: /termin/ → nur Lead; /termin-gebucht/ → nur SubmitApplication; /termin-kamerasysteme/ → nur Contact;
   /termin-gebucht-kamerasysteme/ → nur CompleteRegistration; dann veröffentlichen und im Meta Events Manager
   (Test-Events) gegenprüfen.

Gravity Forms braucht keine Änderung, die Zielseiten bleiben die Quelle der Qualität. Wer Seitenaufrufe ohne
Formular (direktes Öffnen von /termin/) ausschließen will, hängt an die Bestätigungen zusätzlich einen Parameter an
(z. B. `&f=1`) und ergänzt in jedem Trigger „Query lead = 1“; das war nicht Teil der Vorgabe.
