#!/usr/bin/env python3
"""Unterseite „Videoüberwachung für Schlachthöfe“ (07.11.2026) aus der Kamera-Seite (ID 4313) als Vorlage.

Rechtsgrundlage (recherchiert am 07.11.2026): Fünftes Gesetz zur Änderung des Tierschutzgesetzes, Regierungsentwurf
BT-Drs. 21/6809 (Kabinett 29.04.2026), Beschlussempfehlung des Agrarausschusses BT-Drs. 21/8974 (04.11.2026),
vom Bundestag am 05.11.2026 beschlossen; neuer § 4d TierSchG; Inkrafttreten 01.01.2027 mit einjähriger Übergangsfrist
(§ 4d anzuwenden ab 01.01.2028, § 21 Abs. 1 TierSchG n. F.). Niedersachsen: Vereinbarung vom 12.02.2019 und Datenschutz-Leitfaden
(Stand Juni 2020). Quellen in `recherche/schlachthoefe-quellen.md`.

Vorgehen: Export der Kamera-Seite laden, Texte je Element-ID ersetzen (IDs bleiben, wie bei den Stadtseiten),
FAQ und Strukturdaten neu erzeugen, Handy-Darstellungs-Widget ergänzen, Seitentitel setzen.
Aufruf: python3 -I tools/schlachthof_seite.py export-4313.json ziel.json
"""
import copy, hashlib, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import handy_darstellung, ladeverhalten

SLUG = "videoueberwachung-schlachthoefe"
URL = f"https://provision-infra.de/{SLUG}/"
TITEL = "Videoüberwachung Schlachthöfe"
B = '<span style="font-weight: 700;">'

# --- Überschriften (heading: title) ---
HEADINGS = {
    "9dcea29": f"{B}Videoüberwachung für Schlachthöfe</span> nach dem neuen Tierschutzgesetz",
    "e429076": ("Am 5. November 2026 hat der Bundestag die Kamerapflicht für Schlachthöfe beschlossen: gültig ab "
                "1. Januar 2027, ein Jahr Übergangsfrist. <br>\n<br>\n"
                f"{B}ProVision Infra plant und installiert Videoüberwachung nach § 4d Tierschutzgesetz: Pflichtbereiche im "
                "Bild, 30 Schlachttage Speicherung, Behördenabruf, Datenschutz fürs Team. Norddeutschland und bundesweit.</span>"),
    "e54550b": "Ab 1. Januar 2027 gilt die Kamerapflicht – mit einem Jahr Übergangsfrist.",
    "c407c9d": "Was § 4d Tierschutzgesetz von deinem Schlachthof verlangt",
    "b31eb2f": "… alle tierschutzrelevanten Schritte im Bild sind,",
    "f35e156": "… Datum und Uhrzeit immer mitlaufen,",
    "f477c9d": "… 30 Schlachttage gespeichert werden,",
    "7865073": "… jeder Abruf der Behörde protokolliert wird,",
    "044ceb5": "… deine Beschäftigten geschützt bleiben,",
    "d673c65": "Videoüberwachung für Schlachthöfe: gesetzeskonform, dokumentiert, abnahmefertig",
    "139e9f8": "Jede Kamera planen wir entlang des Schlachtprozesses, von der Entladung bis zu den ersten Schlachtarbeiten.",
    "144a30a": "Aufzeichnung, Zeitstempel und Behördenabruf sind eingerichtet, bevor wir vom Hof fahren.",
    "51f3331": "Videoüberwachung für Schlachthöfe in Niedersachsen, Norddeutschland und bundesweit",
    "7983242": "Häufige Fragen zur Videoüberwachung in Schlachthöfen",
    "45eaf1f": "Häufige Fragen zur Videoüberwachung in Schlachthöfen",
    # „Stell dir mal vor“, Handy-Variante: zwei Karten sind Überschrift-Widgets
    "a191679": "Bei einem Vorwurf zeigst du in Minuten, was wirklich war.",
    "f4441f3": "Die Abnahme läuft durch: Bildausschnitte und Format sind vorher geprüft.",
}

# --- Fließtexte (text-editor: editor, HTML) ---
TEXTE = {
    "47ef5fe": ("<p>Betroffen sind Betriebe ab 1.000 Großvieheinheiten Säugetiere oder 150.000 Stück Geflügel oder Kaninchen "
                "im Jahr – rund 90 Prozent aller Schlachttiere. Kleinere Betriebe kann die Behörde bei konkreten "
                "Anhaltspunkten verpflichten.</p>"),
    "3efeb2a": ("<p>ProVision Infra setzt § 4d technisch um: Kameras entlang des gesamten Schlachtprozesses, Zeitstempel im "
                "Bild, 30 Schlachttage Speicherung mit automatischer Löschung und ein Abruf, der bei der Abnahme "
                "standhält.</p>"),
    "c5f5120": "<p>Fünf Vorgaben für die einjährige Übergangsfrist. Dein Schlachthof ist auf der sicheren Seite, wenn …</p>",
    "59a04cb": ("<p>Von der Entladung über Warten, Zutrieb, Betäubung und Entblutung bis zu den ersten Schlachtarbeiten. "
                "Tiere und Personen müssen erkennbar sein.</p>"),
    "c05fed2": ("<p>Kameras offen sichtbar. Was nur mit unangemessenem Aufwand einsehbar wäre, klärt die Behörde bei der "
                "Abnahme.</p>"),
    "ca72bdb": ("<p>Bei der Wiedergabe ständig lesbar. Dateien je Kamera getrennt, mit Standort, sortiert nach Datum und "
                "Uhrzeit.</p>"),
    "9d1d8c1": "<p>Vom Bundestag auf Anregung des Bundesrates ergänzt. Fehlt die Sortierung, beanstandet das die Behörde.</p>",
    "24f8396": ("<p>Die letzten 30 Tage mit Schlachtungen plus die Entladung vom Vortag. Die Behörde ruft arbeitstäglich in "
                "einem üblichen Dateiformat ab.</p>"),
    "7227d67": "<p>Danach wird automatisch gelöscht. Löschen von Hand oder Aufheben auf Vorrat gibt es nicht.</p>",
    "4838414": ("<p>Verwendete Daten, Tag und Uhrzeit, Dienststelle und abgerufene Aufnahmen – nur für die "
                "Datenschutzkontrolle.</p>"),
    "19193be": ("<p>Protokolle werden sechs Monate nach der Speicherfrist automatisch gelöscht. Aufnahmen und Protokolle sind "
                "gegen Missbrauch zu schützen.</p>"),
    "6f77810": ("<p>DSGVO und BDSG gelten: so wenig Arbeitszeit im Bild wie möglich, Kameras erkennbar gekennzeichnet, keine "
                "Leistungskontrolle auf dieser Grundlage.</p>"),
    "3ac3e9e": ("<p>Datenschutz-Folgenabschätzung prüfen, Datenschutzbeauftragten und Betriebsrat früh einbinden – Kameras "
                "sind mitbestimmungspflichtig.</p>"),
    "4413783": ("<p>Wer Aufnahmen nicht, unvollständig oder zu spät bereitstellt, handelt ordnungswidrig (§ 18 "
                "Tierschutzgesetz). Die Behörde kann Anordnungen bis zur Untersagung treffen.</p>"),
    # „Stell dir mal vor“ – Computer-Variante (716d34c) und Handy-Variante (57840b0), gleiche Reihenfolge
    "d912454": "<p>Die Behörde ruft ab – alles liegt sortiert nach Kamera, Datum und Uhrzeit bereit.</p>",
    "ee35cf1": "<p>Jede Betäubung und jeder Entblutungsschnitt im Bild, mit Zeitstempel.</p>",
    "a71645f": "<p>Nach 30 Schlachttagen löscht das System von selbst.</p>",
    "832bc11": "<p>Dein Tierschutzbeauftragter sieht alle Abläufe gleichzeitig.</p>",
    "eb73aa0": "<p>Bei einem Vorwurf zeigst du in Minuten, was wirklich war.</p>",
    "57a4afd": "<p>Dein Team weiß, wo gefilmt wird – und dass niemand Leistung kontrolliert.</p>",
    "c0fa617": "<p>Die Abnahme läuft durch: Bildausschnitte und Format sind vorher geprüft.</p>",
    "b795beb": "<p>Fällt eine Kamera aus, meldet sich das System sofort.</p>",
    "98ff3a7": "<p>Die Behörde ruft ab – alles liegt sortiert nach Kamera, Datum und Uhrzeit bereit.</p>",
    "ddf231e": "<p>Jede Betäubung und jeder Entblutungsschnitt im Bild, mit Zeitstempel.</p>",
    "6c14f0d": "<p>Nach 30 Schlachttagen löscht das System von selbst.</p>",
    "e923bf2": "<p>Dein Tierschutzbeauftragter sieht alle Abläufe gleichzeitig.</p>",
    "b15163f": "<p>Dein Team weiß, wo gefilmt wird – und dass niemand Leistung kontrolliert.</p>",
    "3846da1": "<p>Fällt eine Kamera aus, meldet sich das System sofort.</p>",
    "2db6205": ("<p>Wir planen und installieren Videoüberwachung nach § 4d Tierschutzgesetz: Kameras an jedem Prozessschritt, "
                "Zeitstempel im Bild, 30 Schlachttage Speicherung, automatische Löschung, Abruf fürs Veterinäramt. Dazu alle "
                "Unterlagen für Behörde, Datenschutzbeauftragten und Betriebsrat.</p>"),
    "887ada7": ("<p>Übergeben wird erst nach Prüfung von Bildausschnitten, Speicherfrist und Löschung – schriftlich, als "
                "Unterlage für Veterinäramt, Datenschutz und Betriebsrat.</p>"),
    "20734e0": "<p>Kurzes Telefonat: Tierarten, Schlachttage, Bereiche. Du erfährst, ob und ab wann die Pflicht dich trifft.</p>",
    "8595654": ("<p>Wir gehen den Weg der Tiere ab, von der Rampe bis zur Entblutung, und legen fest, welche Kamera welchen "
                "Schritt zeigt. Den Kostenrahmen nennen wir vor Ort.</p>"),
    "2f2676e": ("<p>Konzept mit Kamerastandorten je Prozessschritt, Speicher- und Abrufkonzept nach § 4d und ein Angebot. "
                "Dann entscheidest du.</p>"),
    "933e53d": ("<p>Wir montieren die Kameras und richten Aufzeichnung, Zeitstempel, Speicherfrist und Behördenabruf ein. Du "
                "konfigurierst nichts selbst.</p>"),
    "d11be39": ("<p>Wir prüfen jeden Bildausschnitt gegen die Pflichtliste und halten das schriftlich fest – deine Unterlage "
                "für die Abnahme. Danach bleiben wir erreichbar.</p>"),
    "8080300": ("<p>Wir verbauen TP-Link VIGI: wetterfeste Bullet- und Dome-Kameras (IP67), lichtstark für Betäubungs- und "
                "Entblutebereiche, mit Datum und Uhrzeit im Bild. Dazu ein Rekorder mit Speicher für 30 Schlachttage je "
                "Kamera und Export in gängigen Dateiformaten für die Behörde.</p>"),
    "5c65e03": ("<p>Wir sitzen in Bad Bevensen bei Lüneburg, in Niedersachsen – dem Land, das Kameras in Schlachthöfen seit "
                "2019 mit einer freiwilligen Vereinbarung und einem Datenschutz-Leitfaden vorangebracht hat. Zwischen "
                "Hamburg, Bremen, Hannover und dem Oldenburger Münsterland sind wir vor Ort, Anlagen setzen wir bundesweit "
                "um.</p><p>Beratung, Begehung und Umsetzung finden bei dir im Betrieb statt. Auch Kameras fürs Gelände oder "
                "digitale Zutrittskontrolle? Mehr zu "
                "<a href=\"https://provision-infra.de/kamerasysteme/\">Videoüberwachung für Unternehmen</a> und "
                "<a href=\"https://provision-infra.de/\">digitalen Schließanlagen</a>.</p>"),
}

FAQ = [
    ("Welche Schlachthöfe müssen Videoaufzeichnungen machen?",
     "Alle Schlachteinrichtungen für warmblütige Tiere, die einen Tierschutzbeauftragten brauchen: ab 1.000 "
     "Großvieheinheiten Säugetiere im Jahr (etwa 1.000 Rinder oder rund 5.000 Mastschweine) oder ab 150.000 Stück "
     "Geflügel oder Kaninchen. Das sind rund 232 Betriebe mit etwa 90 Prozent aller Schlachttiere. Kleinere Betriebe "
     "kann die Behörde bei konkreten Anhaltspunkten für Verstöße ebenfalls verpflichten."),
    ("Ab wann gilt die Kamerapflicht?",
     "Das Gesetz gilt ab dem 1. Januar 2027, mit einer Übergangsfrist von einem Jahr: Spätestens ab dem 1. Januar 2028 "
     "müssen die Aufzeichnungen laufen und abrufbar sein. Bundesrat und Verkündung standen am 7. November 2026 noch "
     "aus. Wer früh 2027 plant, hat Zeit für Abnahme, Betriebsrat und Datenschutzbeauftragten."),
    ("Welche Bereiche müssen gefilmt werden?",
     "Alle tierschutzrelevanten Schritte, soweit vorhanden: Entladen, Warten und Zutrieb bis zur Betäubung, die "
     "Betäubung, das Aufhängen, der Entblutungsschnitt, die Entblutung und die ersten weiteren Schlachtarbeiten wie "
     "Brühen oder Zurichten. Zerlegung, Verpackung, Büros und Pausenräume gehören nicht dazu."),
    ("Wie lange müssen die Aufnahmen gespeichert werden?",
     "Für die letzten 30 Tage mit Schlachtungen, plus die Entladung vom Vortag. Danach wird automatisch gelöscht, die "
     "Abrufprotokolle sechs Monate später. Den Speicherbedarf rechnen wir aus Kamerazahl, Auflösung und "
     "Schlachtzeiten aus."),
    ("Wer hat Zugriff auf die Aufnahmen?",
     "Die zuständige Behörde, meist das Veterinäramt: arbeitstäglicher Abruf in einem üblichen Dateiformat, je Kamera "
     "mit Standort. Sie sichtet stichprobenartig und anlassbezogen, löscht nach der Sichtung und verarbeitet nur bei "
     "Anhaltspunkten weiter. Für andere Zwecke braucht der Betrieb eine eigene Rechtsgrundlage nach der DSGVO."),
    ("Was gilt für den Datenschutz der Beschäftigten?",
     "DSGVO und Bundesdatenschutzgesetz gelten. Kameras müssen erkennbar sein, der gefilmte Anteil der Arbeitszeit so "
     "gering wie möglich, Leistungskontrolle ist unzulässig. Dazu Hinweisschilder, Verarbeitungsverzeichnis, Prüfung "
     "einer Datenschutz-Folgenabschätzung und Mitbestimmung des Betriebsrats. Tonaufnahmen bleiben aus."),
    ("Welche technischen Anforderungen gelten für die Kameras?",
     "Das Gesetz verlangt offen sichtbare Kameras, die Tiere und Personen geeignet erfassen, Datum und Uhrzeit lesbar "
     "im Bild, ein übliches Dateiformat und die Bereitstellung je Kamera, sortiert nach Datum und Uhrzeit. Details "
     "kann das Bundesministerium per Verordnung festlegen; die steht noch aus. Wir planen mit ausreichender Auflösung "
     "und Beleuchtung, wasserdichten Gehäusen, Notstrom und Ausfallmeldung."),
    ("Was passiert, wenn keine Aufzeichnung vorliegt?",
     "Wer Aufnahmen nicht, unvollständig oder zu spät bereitstellt, handelt ordnungswidrig nach § 18 Tierschutzgesetz. "
     "Die Behörde kann Anordnungen bis zur Untersagung treffen. Unsere Anlagen melden Kamera- und Speicherausfälle "
     "automatisch."),
    ("Was kostet die Umsetzung?",
     "Das hängt von Prozessschritten, Hallen, Kamerazahl, Verkabelung und Speicher für 30 Schlachttage ab. Einen "
     "ersten Rahmen bekommst du im Erstgespräch, einen verbindlichen Preis nach der Begehung."),
    ("Können vorhandene Kameras weiter genutzt werden?",
     "Ja, wenn sie die Pflichtbereiche erfassen, Datum und Uhrzeit zeigen und der Rekorder je Kamera in einem üblichen "
     "Dateiformat exportiert. Viele niedersächsische Betriebe haben seit 2019 Kameras; wir prüfen den Bestand und "
     "bieten nur an, was fehlt."),
    ("Wie läuft die Abnahme durch die Behörde?",
     "Nach der ersten Installation und nach erheblichen Änderungen prüft die Behörde, ob alle Pflichtbereiche erfasst "
     "sind und das Dateiformat nutzbar ist. Dafür liefern wir Kameraplan und Testabruf; auf Wunsch begleiten wir den "
     "Termin."),
    ("In welcher Region installiert ProVision Infra Videoüberwachung für Schlachthöfe?",
     "Sitz ist Bad Bevensen bei Lüneburg. Vor Ort sind wir vor allem in Niedersachsen, Hamburg, Bremen und "
     "Schleswig-Holstein; Anlagen setzen wir bundesweit um."),
]

SEO = {
    "title": "Videoüberwachung im Schlachthof (§ 4d TierSchG) | ProVision Infra",
    "description": ("Kamerapflicht für Schlachthöfe ab 2027 mit einjähriger Übergangsfrist: Videoüberwachung nach § 4d "
                    "Tierschutzgesetz, geplant und installiert von ProVision Infra. Norddeutschland und bundesweit."),
    "focus_keyphrase": "Videoüberwachung Schlachthof",
    "og_title": "Videoüberwachung für Schlachthöfe nach § 4d Tierschutzgesetz | ProVision Infra",
    "cornerstone": False,
}

def walk(els):
    for e in els:
        yield e
        yield from walk(e.get("elements", []))

def schema(vorhanden_html):
    """Strukturdaten: Organisation aus der Vorlage übernehmen, Service neu (FAQ-Schema liefert das Akkordeon)."""
    start = vorhanden_html.find("{"); ende = vorhanden_html.rfind("}") + 1
    g = json.loads(vorhanden_html[start:ende])
    org = next(x for x in g["@graph"] if x["@type"] == "LocalBusiness")
    service = {
        "@type": "Service", "@id": URL + "#leistung", "name": "Videoüberwachung für Schlachthöfe nach § 4d Tierschutzgesetz",
        "serviceType": "Videoüberwachung", "url": URL,
        "image": "https://provision-infra.de/wp-content/uploads/2026/10/kamera-vorschau-1200x630-1.jpg",
        "description": SEO["description"], "provider": {"@id": "https://provision-infra.de/#organization"},
        "areaServed": [{"@type": "State", "name": "Niedersachsen"}, {"@type": "State", "name": "Hamburg"},
                       {"@type": "State", "name": "Bremen"}, {"@type": "State", "name": "Schleswig-Holstein"},
                       {"@type": "State", "name": "Mecklenburg-Vorpommern"}, {"@type": "Country", "name": "Deutschland"}],
        "audience": {"@type": "BusinessAudience", "name": "Schlachtbetriebe und Fleischwirtschaft"},
    }
    # Kein eigenes FAQPage: das Essential-Addons-Akkordeon gibt bereits ein FAQ-Schema mit allen Einträgen aus
    # („EA FAQ Schema“); ein zweiter Block wäre eine Dublette.
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [org, service]}, ensure_ascii=False) + "</script>"

def bauen(basis):
    data = copy.deepcopy(basis)
    by = {e["id"]: e for e in walk(data["elements"])}
    fehlend = [i for i in list(HEADINGS) + list(TEXTE) if i not in by]
    assert not fehlend, f"IDs fehlen in der Vorlage: {fehlend}"
    for i, t in HEADINGS.items():
        assert by[i].get("widgetType") == "heading", (i, by[i].get("widgetType")); by[i]["settings"]["title"] = t
    for i, t in TEXTE.items():
        assert by[i].get("widgetType") == "text-editor", (i, by[i].get("widgetType")); by[i]["settings"]["editor"] = t
    # FAQ (Essential Addons Accordion): Struktur des ersten Eintrags übernehmen
    acc = by["ed852c3"]["settings"]; vorlage = acc["eael_adv_accordion_tab"][0]
    acc["eael_adv_accordion_tab"] = [dict(vorlage, _id=hashlib.md5(("faq-schlacht-" + q).encode()).hexdigest()[:7],
                                          eael_adv_accordion_tab_title=q, eael_adv_accordion_tab_content=f"<p>{a}</p>") for q, a in FAQ]
    # Strukturdaten
    by["dca37dc"]["settings"]["html"] = schema(by["dca37dc"]["settings"]["html"])
    # Ladeverhalten-Skript in der aktuellen Fassung aus dem Repo
    by["dc9ac90"]["settings"]["html"] = ladeverhalten.LADE_SCRIPT
    # Handy-Darstellung (gleiche Element-IDs wie die Kamera-Seite)
    steuerung = by["85d5f75"]
    if not any(w.get("settings", {}).get("_title") == "Steuerung Handy-Darstellung" for w in steuerung["elements"]):
        steuerung["elements"].append(handy_darstellung.style_widget(handy_darstellung.SEITEN[4313]))
    # Seitentitel
    data["settings"]["post_title"] = TITEL; data["title"] = TITEL; data["status"] = "publish"
    return data

if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data = bauen(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    pathlib.Path(dst).with_name("seo-schlachthoefe.json").write_text(json.dumps(SEO, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Seite gebaut:", dst, "| Überschriften", len(HEADINGS), "| Texte", len(TEXTE), "| FAQ", len(FAQ))
