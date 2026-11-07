// SEO-Änderungen für Seite 4870 (/videoueberwachung-schlachthoefe/). Gibt die Zahl der Änderungen zurück.
export default function transform(elements, { walk, log }) {
  let n = 0;
  const byId = {}; elements.forEach(top => walk(top, e => { byId[e.id] = e; }));
  const set = (id, key, fn) => { const e = byId[id]; if (!e) { log('fehlt ' + id); return; } const alt = e.settings[key]; const neu = fn(alt); if (neu !== alt) { e.settings[key] = neu; n++; log(`${id}.${key} geändert`); } else log(`${id}.${key} unverändert (Muster nicht gefunden?)`); };

  // H1: Paragraf nennen
  set('9dcea29', 'title', v => v.replace('nach dem neuen Tierschutzgesetz', 'nach § 4d Tierschutzgesetz'));
  // Einleitung: Deutschland, Schlachtbetriebe
  set('47ef5fe', 'editor', v => v.replace('Betroffen sind Betriebe ab 1.000 Großvieheinheiten', 'Die Kamerapflicht gilt in ganz Deutschland für Schlachtbetriebe ab 1.000 Großvieheinheiten'));
  // Umsetzung: TierSchG-Kürzel und Kameraüberwachung als Suchbegriff
  set('3efeb2a', 'editor', v => v.replace('ProVision Infra setzt § 4d technisch um: Kameras entlang des gesamten Schlachtprozesses', 'ProVision Infra setzt § 4d TierSchG technisch um – Videoüberwachung (Kameraüberwachung) entlang des gesamten Schlachtprozesses'));
  // Rechtsgrundlage mit Quelle (Bundestag)
  set('4413783', 'editor', v => v.includes('Drucksache 21/8974') ? v : v.replace(/<\/p>\s*$/, ' Grundlage ist der Gesetzesbeschluss des Bundestages vom 5. November 2026 (<a href="https://dserver.bundestag.de/btd/21/089/2108974.pdf" target="_blank" rel="noopener">Drucksache 21/8974</a>).</p>'));
  // Standort: deutschlandweit + NAP-Block mit Telefon und E-Mail
  set('5c65e03', 'editor', v => {
    if (v.includes('tel:+4958214049040')) return v;
    let w = v.replace('Anlagen setzen wir bundesweit um', 'Anlagen setzen wir bundesweit um, von Schleswig-Holstein bis Bayern');
    return w + '<p><strong>ProVision Infra GmbH</strong><br>Klein Hesebecker Straße 11, 29549 Bad Bevensen<br>Telefon: <a href="tel:+4958214049040">05821 4049040</a><br>E-Mail: <a href="mailto:info@provision-infra.de">info@provision-infra.de</a><br>Mo–Do 9–18 Uhr, Fr 9–14 Uhr</p>';
  });

  // FAQ: fünf Fragen ergänzen
  const NEU = [
    ['Gilt die Kamerapflicht auch für kleine Schlachthöfe, Metzgereien und Hofschlachtungen?',
     '<p>Nein, nicht automatisch. Die Pflicht nach § 4d Tierschutzgesetz greift ab 1.000 Großvieheinheiten Säugetiere oder 150.000 Stück Geflügel oder Kaninchen im Jahr. Kleinere Schlachtbetriebe, Metzgereien mit eigener Schlachtung und mobile Schlachtungen sind ausgenommen. Die Behörde kann die Videoüberwachung dort aber bei konkreten Anhaltspunkten für Verstöße anordnen. Viele kleinere Betriebe rüsten freiwillig aus, um Vorwürfe schnell entkräften zu können und ihre Abnehmer abzusichern.</p>'],
    ['Muss der Betriebsrat der Videoüberwachung im Schlachthof zustimmen?',
     '<p>Ja. Kameras, die Beschäftigte erfassen, sind eine technische Einrichtung zur Überwachung im Sinne von § 87 Absatz 1 Nummer 6 Betriebsverfassungsgesetz und damit mitbestimmungspflichtig, auch wenn das Tierschutzgesetz die Aufzeichnung vorschreibt. Üblich ist eine Betriebsvereinbarung, die Zweck, Kamerastandorte, Speicherfrist, Zugriffsrechte und das Verbot der Leistungskontrolle festhält. Kameraplan und technische Beschreibung liefern wir als Grundlage dafür mit.</p>'],
    ['Wie viel Speicherplatz braucht ein Schlachthof für 30 Schlachttage?',
     '<p>Als Richtwert: Eine Full-HD-Kamera mit H.265-Kompression erzeugt je nach Bildrate und Bewegung etwa 1 bis 3 GB pro Stunde. Bei einer Zehn-Stunden-Schicht sind das 10 bis 30 GB pro Kamera und Schlachttag, für 30 Schlachttage also 300 bis 900 GB je Kamera, zuzüglich der Entladung vom Vortag. Wir dimensionieren Rekorder und Festplatten mit Reserve, legen die Aufnahmen je Kamera getrennt ab und richten die automatische Löschung nach Ablauf der Frist ein.</p>'],
    ['Welche Kameras eignen sich für Nassbereiche, Kälte und Reinigung im Schlachthof?',
     '<p>Im Schlachtbereich müssen Kameras Spritzwasser, Reinigungsmittel, Dampf und Temperaturwechsel aushalten. Wir setzen wetterfeste Bullet- und Dome-Kameras mit Schutzart IP67 ein, in Nassbereichen mit Hochdruckreinigung zusätzlich in Schutzgehäusen, und montieren so, dass Linsen nicht beschlagen oder verschmutzen. Lichtstarke Sensoren und Weißlicht-LEDs halten Betäubung und Entblutungsschnitt auch bei schlechtem Licht erkennbar.</p>'],
    ['Was ändert sich gegenüber der freiwilligen Videoüberwachung in Niedersachsen?',
     '<p>In Niedersachsen empfehlen Land und Verbände seit 2019 Kameras in Schlachthöfen auf freiwilliger Basis, begleitet von einem Datenschutz-Leitfaden des Landwirtschaftsministeriums. Neu ist die bundesweite Pflicht mit festen Vorgaben: definierte Bereiche von der Entladung bis zu den ersten Schlachtarbeiten, Zeitstempel im Bild, 30 Schlachttage Speicherung, arbeitstäglicher Abruf durch die Behörde und Bußgelder bei Verstößen. Bestehende freiwillige Anlagen lassen sich meist erweitern, statt sie zu ersetzen.</p>'],
  ];
  const acc = Object.values(byId).find(e => e.widgetType === 'eael-adv-accordion');
  if (acc) {
    const tabs = acc.settings.eael_adv_accordion_tab; const tmpl = tabs[0];
    const have = new Set(tabs.map(t => t.eael_adv_accordion_tab_title));
    const used = new Set(tabs.map(t => t._id));
    const newId = () => { let i; do { i = Math.random().toString(16).slice(2, 9); } while (used.has(i) || i.length < 7); used.add(i); return i; };
    for (const [q, a] of NEU) if (!have.has(q)) { tabs.push({ ...JSON.parse(JSON.stringify(tmpl)), _id: newId(), eael_adv_accordion_tab_title: q, eael_adv_accordion_tab_content: a }); n++; }
    log('FAQ jetzt ' + tabs.length + ' Einträge');
  } else log('FAQ-Widget fehlt');

  // Schema: Service-Beschreibung und Rechtsgrundlage
  const sd = byId['dca37dc'];
  if (sd && sd.settings.html.includes('ld+json')) {
    const m = sd.settings.html.match(/<script[^>]*>([\s\S]*?)<\/script>/); const j = JSON.parse(m[1]);
    const svc = j['@graph'].find(x => x['@type'] === 'Service');
    if (svc) {
      svc.name = 'Videoüberwachung für Schlachthöfe nach § 4d Tierschutzgesetz (Kamerapflicht)';
      svc.serviceType = 'Videoüberwachung für Schlachthöfe';
      svc.description = 'Planung, Installation und Abnahmebegleitung der gesetzlich vorgeschriebenen Videoüberwachung in Schlachthöfen nach § 4d Tierschutzgesetz: Kameras von der Entladung bis zu den ersten Schlachtarbeiten, Zeitstempel im Bild, Speicherung der letzten 30 Schlachttage, arbeitstäglicher Behördenabruf, Datenschutzunterlagen für Betriebsrat und Veterinäramt. Bundesweit.';
      svc.about = { '@type': 'Legislation', name: '§ 4d Tierschutzgesetz (TierSchG), Videoüberwachung in Schlachtbetrieben', legislationIdentifier: '§ 4d TierSchG', url: 'https://dserver.bundestag.de/btd/21/089/2108974.pdf', legislationJurisdiction: { '@type': 'Country', name: 'Deutschland' } };
      sd.settings.html = '<script type="application/ld+json">' + JSON.stringify(j) + '</script>'; n++; log('Schema aktualisiert');
    }
  }
  return n;
}
