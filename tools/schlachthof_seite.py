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
    "e429076": ("Der Bundestag hat am 5. November 2026 die Kamerapflicht für Schlachthöfe beschlossen: Sie gilt ab "
                "1. Januar 2027, mit einer Übergangsfrist von einem Jahr für die Umsetzung. <br>\n<br>\n"
                f"{B}ProVision Infra plant und installiert Videoüberwachung nach § 4d Tierschutzgesetz: alle Pflichtbereiche "
                "im Bild, 30 Schlachttage Speicherung, Abruf für die Behörde und Datenschutz für dein Team – in "
                "Norddeutschland und bundesweit.</span>"),
    "e54550b": "Ab 1. Januar 2027 gilt die Kamerapflicht für größere Schlachthöfe – mit einer Übergangsfrist von einem Jahr.",
    "c407c9d": "Was § 4d Tierschutzgesetz von deinem Schlachthof verlangt",
    "b31eb2f": "… alle tierschutzrelevanten Schritte im Bild sind,",
    "f35e156": "… Datum und Uhrzeit immer mitlaufen,",
    "f477c9d": "… 30 Schlachttage gespeichert werden,",
    "7865073": "… jeder Abruf der Behörde protokolliert wird,",
    "044ceb5": "… deine Beschäftigten geschützt bleiben,",
    "d673c65": "Videoüberwachung für Schlachthöfe von ProVision Infra: gesetzeskonform, dokumentiert, abnahmefertig",
    "139e9f8": "Jede Kamera planen wir entlang deines Schlachtprozesses: von der Entladung bis zu den ersten Schlachtarbeiten, ohne toten Winkel.",
    "144a30a": "Aufzeichnung, Zeitstempel und Abruf sind eingerichtet, bevor wir vom Hof fahren. Die Behörde kann ab dem ersten Schlachttag zugreifen.",
    "51f3331": "Videoüberwachung für Schlachthöfe in Niedersachsen, Norddeutschland und bundesweit",
    "7983242": "Häufige Fragen zur Videoüberwachung in Schlachthöfen",
    "45eaf1f": "Häufige Fragen zur Videoüberwachung in Schlachthöfen",
    # „Stell dir mal vor“, Handy-Variante: zwei Karten sind Überschrift-Widgets
    "a191679": "Bei einem Vorwurf zeigst du in Minuten, was wirklich passiert ist.",
    "f4441f3": "Die Abnahme durch das Veterinäramt läuft durch, weil Bildausschnitte und Dateiformat vorher geprüft sind.",
}

# --- Fließtexte (text-editor: editor, HTML) ---
TEXTE = {
    "47ef5fe": ("<p>Betroffen sind Betriebe, die jährlich mindestens 1.000 Großvieheinheiten Säugetiere oder 150.000 Stück "
                "Geflügel oder Kaninchen schlachten – nach Angaben der Bundesregierung rund 90 Prozent aller Schlachttiere "
                "in Deutschland. Kleinere Betriebe kann die Behörde bei konkreten Anhaltspunkten ebenfalls zur Aufzeichnung "
                "verpflichten.</p>"),
    "3efeb2a": ("<p>ProVision Infra setzt die Vorgaben aus § 4d Tierschutzgesetz technisch um: Kameras entlang des gesamten "
                "Schlachtprozesses, Zeitstempel im Bild, 30 Schlachttage Speicherung mit automatischer Löschung und ein Abruf "
                "für die Behörde, der bei der Abnahme standhält.</p>"),
    "c5f5120": ("<p>Fünf Vorgaben, die jeder betroffene Betrieb innerhalb der einjährigen Übergangsfrist erfüllen muss. Dein "
                "Schlachthof ist auf der sicheren Seite, wenn …</p>"),
    "59a04cb": ("<p>von der Entladung über Warten und Zutrieb, Betäubung, Aufhängen und Entblutungsschnitt bis zu den ersten "
                "weiteren Schlachtarbeiten wie Brühen oder Zurichten. Tiere und die Personen, die mit ihnen umgehen, müssen "
                "erkennbar sein.</p>"),
    "c05fed2": ("<p>Die Kameras müssen offen sichtbar sein. Bereiche, die nur mit unangemessenem Aufwand einsehbar wären, "
                "prüft die Behörde bei der Abnahme der Anlage.</p>"),
    "ca72bdb": ("<p>Bei der Wiedergabe müssen Datum und Uhrzeit ständig gut lesbar im Bild stehen. Die Dateien sind je Kamera "
                "getrennt, mit eindeutiger Standortangabe und nach Datum und Uhrzeit sortiert bereitzustellen.</p>"),
    "9d1d8c1": ("<p>Diese Anforderung hat der Bundestag auf Anregung des Bundesrates ergänzt. Eine fehlende Sortierung kann "
                "die Behörde bei ihrer Kontrolle beanstanden.</p>"),
    "24f8396": ("<p>Aufzuheben sind die Aufzeichnungen der letzten 30 Tage, an denen geschlachtet wurde, plus die Entladung, "
                "wenn sie am Vortag stattfand. Die Behörde muss sie arbeitstäglich in einem üblichen Dateiformat abrufen "
                "können.</p>"),
    "7227d67": ("<p>Nach Ablauf der Frist müssen die Aufnahmen automatisch gelöscht werden. Löschen von Hand oder längeres "
                "Aufheben auf Vorrat ist nicht vorgesehen.</p>"),
    "4838414": ("<p>Für jeden Zugriff der Behörde sind die verwendeten Daten, Tag und Uhrzeit, die abrufende Dienststelle und "
                "die abgerufenen Aufnahmen zu protokollieren. Die Protokolle dienen allein der Datenschutzkontrolle.</p>"),
    "19193be": ("<p>Sechs Monate nach Ende der Speicherfrist werden auch die Protokolle automatisch gelöscht. Aufnahmen und "
                "Protokolle sind gegen zweckfremde Nutzung und Missbrauch zu schützen.</p>"),
    "6f77810": ("<p>Es gelten DSGVO und Bundesdatenschutzgesetz. Die Aufzeichnung darf keinen dauerhaften Überwachungsdruck "
                "erzeugen: so wenig Arbeitszeit im Bild wie möglich, Kameras durch Piktogramme und Hinweise erkennbar, keine "
                "Leistungskontrolle auf dieser Grundlage.</p>"),
    "3ac3e9e": ("<p>Prüfe früh, ob eine Datenschutz-Folgenabschätzung nötig ist, und beziehe Datenschutzbeauftragten und "
                "Betriebsrat ein: Kameras, die Beschäftigte erfassen, sind mitbestimmungspflichtig, sobald es einen "
                "Betriebsrat gibt.</p>"),
    "4413783": ("<p>Wer Aufzeichnungen nicht, nicht vollständig oder nicht rechtzeitig bereitstellt, handelt ordnungswidrig "
                "(§ 18 Tierschutzgesetz). Bei Verstößen kann die Behörde zusätzlich Anordnungen bis zur Untersagung "
                "treffen.</p>"),
    # „Stell dir mal vor“ – Computer-Variante (716d34c) und Handy-Variante (57840b0), gleiche Reihenfolge
    "d912454": "<p>Die Behörde ruft die Aufnahmen ab, und alles liegt sortiert nach Kamera, Datum und Uhrzeit bereit.</p>",
    "ee35cf1": "<p>Jede Betäubung und jeder Entblutungsschnitt sind im Bild, mit lesbarem Zeitstempel.</p>",
    "a71645f": "<p>Nach 30 Schlachttagen löscht das System automatisch, ohne dass jemand daran denken muss.</p>",
    "832bc11": "<p>Dein Tierschutzbeauftragter sieht Abläufe, die er sonst nie gleichzeitig im Blick hätte.</p>",
    "eb73aa0": "<p>Bei einem Vorwurf zeigst du in Minuten, was wirklich passiert ist.</p>",
    "57a4afd": "<p>Deine Beschäftigten wissen, wo gefilmt wird und wo nicht – und dass niemand ihre Leistung kontrolliert.</p>",
    "c0fa617": "<p>Die Abnahme durch das Veterinäramt läuft durch, weil Bildausschnitte und Dateiformat vorher geprüft sind.</p>",
    "b795beb": "<p>Fällt eine Kamera aus, meldet sich das System, bevor Aufzeichnungen fehlen.</p>",
    "98ff3a7": "<p>Die Behörde ruft die Aufnahmen ab, und alles liegt sortiert nach Kamera, Datum und Uhrzeit bereit.</p>",
    "ddf231e": "<p>Jede Betäubung und jeder Entblutungsschnitt sind im Bild, mit lesbarem Zeitstempel.</p>",
    "6c14f0d": "<p>Nach 30 Schlachttagen löscht das System automatisch, ohne dass jemand daran denken muss.</p>",
    "e923bf2": "<p>Dein Tierschutzbeauftragter sieht Abläufe, die er sonst nie gleichzeitig im Blick hätte.</p>",
    "b15163f": "<p>Deine Beschäftigten wissen, wo gefilmt wird und wo nicht – und dass niemand ihre Leistung kontrolliert.</p>",
    "3846da1": "<p>Fällt eine Kamera aus, meldet sich das System, bevor Aufzeichnungen fehlen.</p>",
    "2db6205": ("<p>Bei ProVision Infra planen und installieren wir Videoüberwachung für Schlachtbetriebe nach § 4d "
                "Tierschutzgesetz: Kameras an jedem Prozessschritt von der Rampe bis zu den ersten Schlachtarbeiten, "
                "Zeitstempel im Bild, Speicherung für 30 Schlachttage mit automatischer Löschung und ein Abruf, den das "
                "Veterinäramt ohne Rückfragen nutzen kann.</p><p>Dazu bekommst du die Unterlagen, die Behörde, "
                "Datenschutzbeauftragter und Betriebsrat sehen wollen: Kameraplan mit Bildausschnitten, Speicher- und "
                "Löschkonzept, Protokollierung der Abrufe und Hinweisschilder für deine Beschäftigten.</p>"),
    "887ada7": ("<p>Übergeben wird erst, wenn Bildausschnitte, Speicherfrist und Löschung geprüft sind. Das Ergebnis bekommst "
                "du schriftlich – als Unterlage für Veterinäramt, Datenschutzbeauftragten und Betriebsrat.</p>"),
    "20734e0": ("<p>Ein kurzes Telefonat: Welche Tierarten, wie viele Schlachttage, welche Bereiche? Du bekommst eine ehrliche "
                "Einschätzung, ob und ab wann die Pflicht deinen Betrieb trifft.</p>"),
    "8595654": ("<p>Wir gehen mit dir den Weg der Tiere ab, von der Rampe bis zur Entblutung, und legen fest, welche Kamera "
                "welchen Schritt zeigt. Den Kostenrahmen nennen wir dir noch vor Ort.</p>"),
    "2f2676e": ("<p>Du bekommst ein Konzept mit Kamerastandorten je Prozessschritt, ein Speicher- und Abrufkonzept nach § 4d "
                "und ein Angebot, das zu deinem Betrieb passt. Dann entscheidest du.</p>"),
    "933e53d": ("<p>Wir montieren die Kameras und richten Aufzeichnung, Zeitstempel, Speicherfrist und den Abruf für die "
                "Behörde ein. Du musst nichts selbst konfigurieren.</p>"),
    "d11be39": ("<p>Gemeinsam prüfen wir jeden Bildausschnitt gegen die Pflichtliste und halten das schriftlich fest – deine "
                "Unterlage für die Abnahme durch das Veterinäramt. Danach bleiben wir erreichbar.</p>"),
    "8080300": ("<p>Wir verbauen Überwachungskameras von TP-Link VIGI, für Schlachthöfe als wetterfeste Bullet- oder "
                "Dome-Kamera (IP67), lichtstark für Betäubungs- und Entblutebereiche, mit Datum und Uhrzeit im Bild. Dazu "
                "kommen ein Rekorder im Gebäude mit Speicher für 30 Schlachttage je Kamera und ein Export in gängigen "
                "Dateiformaten für den Abruf durch die Behörde. So wird aus einzelnen Kameras eine Videoüberwachung, die "
                "§ 4d Tierschutzgesetz erfüllt.</p>"),
    "5c65e03": ("<p>Wir sitzen in Bad Bevensen bei Lüneburg, mitten in Niedersachsen – dem Bundesland, das die "
                "Videoüberwachung in Schlachthöfen seit 2019 mit einer freiwilligen Vereinbarung und einem eigenen "
                "Datenschutz-Leitfaden vorangetrieben hat. Zwischen Hamburg, Bremen, Hannover und dem Oldenburger "
                "Münsterland sind wir vor Ort; darüber hinaus setzen wir Anlagen bundesweit um.</p>"
                "<p>Für Beratung, Begehung und Umsetzung kommen wir zu dir in den Betrieb. Du brauchst auch Kameras für "
                "Gelände und Gebäude oder eine digitale Zutrittskontrolle? Mehr zu "
                "<a href=\"https://provision-infra.de/kamerasysteme/\">Videoüberwachung für Unternehmen</a> und "
                "<a href=\"https://provision-infra.de/\">digitalen Schließanlagen</a>.</p>"),
}

FAQ = [
    ("Welche Schlachthöfe müssen Videoaufzeichnungen machen?",
     "Die Pflicht trifft Schlachteinrichtungen für warmblütige Tiere, die nach der EU-Verordnung 1099/2009 einen "
     "Tierschutzbeauftragten benennen müssen: ab 1.000 Großvieheinheiten Säugetiere im Jahr (das entspricht etwa 1.000 "
     "Rindern oder rund 5.000 Mastschweinen) oder ab 150.000 Stück Geflügel oder Kaninchen. Nach der Gesetzesbegründung "
     "sind das bundesweit rund 232 Betriebe, in denen etwa 90 Prozent aller Schlachttiere geschlachtet werden. Kleinere "
     "Betriebe sind ausgenommen, können aber von der Behörde zur Aufzeichnung verpflichtet werden, sobald konkrete "
     "Anhaltspunkte für Tierschutzverstöße vorliegen."),
    ("Ab wann gilt die Kamerapflicht?",
     "Der Bundestag hat das Gesetz am 5. November 2026 beschlossen. Es gilt ab dem 1. Januar 2027, mit einer Übergangsfrist "
     "von einem Jahr für die Einrichtung der Videoüberwachung: Spätestens ab dem 1. Januar 2028 müssen die Aufzeichnungen "
     "laufen und für die Behörde abrufbar sein. Die abschließende Beratung im Bundesrat und die Verkündung im "
     "Bundesgesetzblatt standen am 7. November 2026 noch aus. Wer früh im Jahr 2027 plant und installiert, hat Zeit für "
     "die Abnahme durch die Behörde und für die Einbindung von Betriebsrat und Datenschutzbeauftragtem."),
    ("Welche Bereiche müssen gefilmt werden?",
     "Alle tierschutzrelevanten Schritte, soweit sie im Betrieb vorkommen: das Entladen, die Zeit zwischen Entladung und "
     "Betäubung (Zutrieb, Ruhen und Warten), die Betäubung, das Aufhängen nach der Betäubung, das Setzen des "
     "Entblutungsschnitts, die Entblutung und die ersten weiteren Schlachtarbeiten wie Brühen oder Zurichten. Bei Tieren, "
     "die ohne Betäubung getötet werden, gelten entsprechende Schritte. Zerlegung, Verpackung, Büros und Pausenräume "
     "gehören nicht dazu und werden auch nicht gefilmt."),
    ("Wie lange müssen die Aufnahmen gespeichert werden?",
     "Für die letzten 30 Tage, an denen geschlachtet wurde, zuzüglich der Entladung, wenn sie nicht am Schlachttag "
     "stattfand. Danach müssen die Aufnahmen automatisch gelöscht werden. Die Protokolle über die Abrufe der Behörde "
     "werden sechs Monate nach Ablauf der Speicherfrist ebenfalls automatisch gelöscht. Wie viel Speicher dein Betrieb "
     "braucht, hängt von Kamerazahl, Auflösung und Schlachtzeiten ab; das rechnen wir im Konzept aus."),
    ("Wer hat Zugriff auf die Aufnahmen?",
     "Die zuständige Behörde, in der Regel das Veterinäramt. Der Betreiber stellt die Aufnahmen arbeitstäglich in einem "
     "üblichen Dateiformat zum Abruf bereit, je Kamera getrennt und mit Standortangabe. Die Behörde sichtet "
     "stichprobenartig und anlassbezogen, löscht nach der Sichtung und darf nur bei Anhaltspunkten für Verstöße weiter "
     "verarbeiten. Für den Betreiber selbst ist § 4d keine Grundlage für andere Zwecke; eine eigene Nutzung braucht eine "
     "eigene Rechtsgrundlage nach der DSGVO."),
    ("Was gilt für den Datenschutz der Beschäftigten?",
     "Es gelten DSGVO und Bundesdatenschutzgesetz. Die Kameras müssen für die Beschäftigten erkennbar sein, etwa durch "
     "Piktogramme und Kurzinformationen, der Anteil der gefilmten Arbeitszeit ist so gering wie möglich zu halten, und "
     "eine Verhaltens- oder Leistungskontrolle auf dieser Grundlage ist unzulässig. Dazu kommen Hinweisschilder, das "
     "Verzeichnis der Verarbeitungstätigkeiten, die Prüfung einer Datenschutz-Folgenabschätzung und die Mitbestimmung "
     "des Betriebsrats. Tonaufnahmen sind nicht erlaubt und bleiben abgeschaltet."),
    ("Welche technischen Anforderungen gelten für die Kameras?",
     "Das Gesetz verlangt offen sichtbare Kameras, die Tiere und die handelnden Personen in geeigneter Weise erfassen, "
     "Datum und Uhrzeit bei der Wiedergabe ständig gut lesbar, ein übliches Dateiformat und die Bereitstellung je Kamera "
     "mit Standort, sortiert nach Datum und Uhrzeit. Nähere technische Einzelheiten kann das Bundesministerium per "
     "Rechtsverordnung festlegen; die steht noch aus. Wir planen so, dass Betäubungswirkung und Umgang mit den Tieren "
     "auf den Aufnahmen beurteilbar sind: ausreichende Auflösung und Beleuchtung, wasserdichte Gehäuse, "
     "Notstromversorgung und eine Meldung, wenn eine Kamera ausfällt."),
    ("Was passiert, wenn keine Aufzeichnung vorliegt?",
     "Wer Aufzeichnungen nicht, nicht richtig, nicht vollständig oder nicht rechtzeitig zum Abruf bereitstellt, handelt "
     "ordnungswidrig nach § 18 Tierschutzgesetz. Die Behörde kann außerdem Anordnungen treffen, bei Tierschutzverstößen "
     "bis hin zur Untersagung. Ein technischer Ausfall sollte deshalb sofort auffallen und dokumentiert werden; unsere "
     "Anlagen melden Kamera- und Speicherausfälle automatisch."),
    ("Was kostet die Umsetzung?",
     "Das hängt von der Zahl der Prozessschritte und Hallen, der Kamerazahl, der Verkabelung und dem Speicher für 30 "
     "Schlachttage ab. Die Bundesregierung geht in ihrer Gesetzesbegründung von überschaubaren Kosten je Betrieb aus; in "
     "der Praxis entscheidet der Aufbau deines Betriebs. Einen ersten Rahmen bekommst du im Erstgespräch, einen "
     "verbindlichen Preis nach der Begehung."),
    ("Können vorhandene Kameras weiter genutzt werden?",
     "Ja, wenn sie die Pflichtbereiche geeignet erfassen, Datum und Uhrzeit im Bild zeigen und der Rekorder die "
     "Aufnahmen in einem üblichen Dateiformat je Kamera bereitstellen kann. Viele niedersächsische Betriebe haben seit der "
     "freiwilligen Vereinbarung von 2019 bereits Kameras; wir prüfen den Bestand bei der Begehung und bieten nur an, was "
     "fehlt."),
    ("Wie läuft die Abnahme durch die Behörde?",
     "Die Behörde kontrolliert nach der ersten Installation und nach erheblichen baulichen, technischen oder "
     "organisatorischen Änderungen, ob alle Pflichtbereiche geeignet erfasst sind und ob sie die bereitgestellten "
     "Aufnahmen im gelieferten Format tatsächlich nutzen kann. Dafür bekommst du von uns einen Kameraplan mit "
     "Bildausschnitten je Prozessschritt und einen Testabruf; auf Wunsch begleiten wir den Termin."),
    ("In welcher Region installiert ProVision Infra Videoüberwachung für Schlachthöfe?",
     "Unser Sitz ist Bad Bevensen bei Lüneburg. Wir sind vor allem in Niedersachsen, Hamburg, Bremen und "
     "Schleswig-Holstein unterwegs und setzen Anlagen für Schlachtbetriebe bundesweit um. Beratung und Begehung finden "
     "bei dir im Betrieb statt."),
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
    """Strukturdaten: Organisation aus der Vorlage übernehmen, Service und FAQ neu."""
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
    faq = {"@type": "FAQPage", "@id": URL + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [org, service, faq]}, ensure_ascii=False) + "</script>"

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
    data["settings"]["post_title"] = TITEL; data["title"] = TITEL; data["status"] = "draft"
    return data

if __name__ == "__main__":
    src, dst = sys.argv[1:3]
    data = bauen(json.loads(pathlib.Path(src).read_text(encoding="utf-8")))
    pathlib.Path(dst).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    pathlib.Path(dst).with_name("seo-schlachthoefe.json").write_text(json.dumps(SEO, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Seite gebaut:", dst, "| Überschriften", len(HEADINGS), "| Texte", len(TEXTE), "| FAQ", len(FAQ))
