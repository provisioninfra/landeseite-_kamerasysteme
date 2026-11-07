// Straffung der SEO-Ergänzungen (Kundenwunsch: kürzere Texte), Suchbegriffe bleiben.
export default function transform(elements, { walk, log }) {
  let n = 0;
  const byId = {}; elements.forEach(top => walk(top, e => { byId[e.id] = e; }));
  const set = (id, key, fn) => { const e = byId[id]; if (!e) { log('fehlt ' + id); return; } const alt = e.settings[key]; const neu = fn(alt); if (neu !== alt) { e.settings[key] = neu; n++; log(`${id}.${key} gekürzt`); } else log(`${id}.${key} unverändert`); };
  set('47ef5fe', 'editor', v => v.replace('Die Kamerapflicht gilt in ganz Deutschland für Schlachtbetriebe ab 1.000 Großvieheinheiten', 'Betroffen sind bundesweit Schlachtbetriebe ab 1.000 Großvieheinheiten'));
  set('3efeb2a', 'editor', v => v.replace('ProVision Infra setzt § 4d TierSchG technisch um – Videoüberwachung (Kameraüberwachung) entlang des gesamten Schlachtprozesses', 'ProVision Infra setzt § 4d TierSchG technisch um: Kameraüberwachung entlang des gesamten Schlachtprozesses'));
  set('4413783', 'editor', v => v.replace(' Grundlage ist der Gesetzesbeschluss des Bundestages vom 5. November 2026 (<a href="https://dserver.bundestag.de/btd/21/089/2108974.pdf" target="_blank" rel="noopener">Drucksache 21/8974</a>).', ' Quelle: <a href="https://dserver.bundestag.de/btd/21/089/2108974.pdf" target="_blank" rel="noopener">Bundestag, Drucksache 21/8974</a>.'));
  const KURZ = {
    'Gilt die Kamerapflicht auch für kleine Schlachthöfe, Metzgereien und Hofschlachtungen?': '<p>Nein. Die Pflicht nach § 4d Tierschutzgesetz greift ab 1.000 Großvieheinheiten Säugetiere oder 150.000 Stück Geflügel oder Kaninchen im Jahr; kleinere Schlachtbetriebe, Metzgereien und mobile Schlachtungen sind ausgenommen. Bei konkreten Anhaltspunkten für Verstöße kann die Behörde Kameras auch dort anordnen.</p>',
    'Muss der Betriebsrat der Videoüberwachung im Schlachthof zustimmen?': '<p>Ja. Kameras, die Beschäftigte erfassen, sind nach § 87 Absatz 1 Nummer 6 Betriebsverfassungsgesetz mitbestimmungspflichtig, auch bei gesetzlicher Pflicht. Üblich ist eine Betriebsvereinbarung zu Zweck, Standorten, Speicherfrist, Zugriff und dem Verbot der Leistungskontrolle; Kameraplan und Technikbeschreibung liefern wir dafür mit.</p>',
    'Wie viel Speicherplatz braucht ein Schlachthof für 30 Schlachttage?': '<p>Richtwert: Eine Full-HD-Kamera mit H.265 erzeugt 1 bis 3 GB pro Stunde, bei zehn Stunden Schlachtung also 300 bis 900 GB je Kamera für 30 Schlachttage. Wir dimensionieren den Rekorder mit Reserve und richten die automatische Löschung ein.</p>',
    'Welche Kameras eignen sich für Nassbereiche, Kälte und Reinigung im Schlachthof?': '<p>Wetterfeste Bullet- und Dome-Kameras mit Schutzart IP67, in Nassbereichen mit Hochdruckreinigung zusätzlich im Schutzgehäuse, montiert gegen Beschlagen und Verschmutzen. Lichtstarke Sensoren und Weißlicht-LEDs halten Betäubung und Entblutungsschnitt auch bei wenig Licht erkennbar.</p>',
    'Was ändert sich gegenüber der freiwilligen Videoüberwachung in Niedersachsen?': '<p>Seit 2019 empfehlen Land und Verbände in Niedersachsen Kameras freiwillig, mit Datenschutz-Leitfaden des Landwirtschaftsministeriums. Neu ist die bundesweite Pflicht mit festen Vorgaben zu Bereichen, Zeitstempel, 30 Schlachttagen Speicherung, Behördenabruf und Bußgeldern; bestehende Anlagen lassen sich meist erweitern.</p>',
  };
  const acc = Object.values(byId).find(e => e.widgetType === 'eael-adv-accordion');
  if (acc) for (const t of acc.settings.eael_adv_accordion_tab) { const k = KURZ[t.eael_adv_accordion_tab_title]; if (k && t.eael_adv_accordion_tab_content !== k) { t.eael_adv_accordion_tab_content = k; n++; } }
  log('FAQ-Antworten gekürzt: ' + Object.keys(KURZ).length);
  return n;
}
