// Ergänzt den Footer-Block: Leistungen (a1f0072) um Mechanische Schließanlagen, Schließsysteme, Ratgeber; Standorte (a1f0073) um „Alle Standorte“.
const L = (text, url, id) => ({ text, selected_icon: { value: '', library: '' }, _id: id, link: { url, is_external: '', nofollow: '', custom_attributes: '' } });
export default async function (elements, { walk, log }) {
  let n = 0;
  elements.forEach(top => walk(top, e => {
    const list = e.settings && e.settings.icon_list;
    if (!Array.isArray(list)) return;
    const urls = list.map(i => i.link && i.link.url);
    if (e.id === 'a1f0072') {
      const add = (after, item) => { if (urls.includes(item.link.url)) return; const i = list.findIndex(x => x.link && x.link.url === after); list.splice(i >= 0 ? i + 1 : list.length, 0, item); urls.push(item.link.url); n++; };
      add('/zutrittssystem/', L('Mechanische Schließanlagen', '/mechanische-schliessanlagen/', '0a1f1a1'));
      add('/mechanische-schliessanlagen/', L('Schließsysteme', '/schliesssysteme/', '0a1f1a2'));
      add('/videoueberwachung-schlachthoefe/', L('Ratgeber', '/ratgeber/', '0a1f1a3'));
      log('a1f0072 jetzt: ' + list.map(i => i.text).join(', '));
    }
    if (e.id === 'a1f0073' && !urls.includes('/standorte/')) { list.push(L('Alle Standorte', '/standorte/', '0a1f1b1')); n++; log('a1f0073 + Alle Standorte'); }
  }));
  return n;
}
