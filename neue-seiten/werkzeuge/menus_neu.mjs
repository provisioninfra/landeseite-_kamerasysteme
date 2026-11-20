// Legt Menüs per REST an (falls nicht vorhanden) und füllt sie. env: STATE, DEF (JSON: [{name, slug, items:[{title,url,children:[...]}]}])
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const S = process.env.STATE, DEF = JSON.parse(fs.readFileSync(process.env.DEF, 'utf8'));
const b = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: S });
const page = await ctx.newPage();
await page.goto('https://provision-infra.de/wp-admin/edit.php?post_type=page', { waitUntil: 'domcontentloaded' });
const nonce = await page.evaluate(() => window.wpApiSettings.nonce);
const api = (method, path, body) => page.evaluate(async ({ method, path, body, nonce }) => {
  const r = await fetch('/wp-json' + path, { method, headers: { 'X-WP-Nonce': nonce, 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
  return { status: r.status, json: await r.json().catch(() => null) };
}, { method, path, body, nonce });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const call = async (m, p, body) => { for (let t = 0; t < 6; t++) { await sleep(t ? 30000 : 4000); const r = await api(m, p, body); if (r.status !== 429) return r; console.log('429, warte'); } };
const menus = (await call('GET', '/wp/v2/menus?per_page=100&_fields=id,name,slug')).json;
for (const m of DEF) {
  let menu = menus.find(x => x.slug === m.slug);
  if (!menu) { const r = await call('POST', '/wp/v2/menus', { name: m.name, slug: m.slug }); console.log('menü angelegt', m.slug, r.status, r.json && r.json.id); menu = r.json; }
  const have = (await call('GET', `/wp/v2/menu-items?menus=${menu.id}&per_page=100&_fields=id,title,url,parent,menu_order`)).json || [];
  let order = 0;
  const add = async (it, parent) => {
    order++;
    let ex = have.find(h => h.url === it.url && h.title.rendered === it.title && h.parent === parent);
    if (!ex) { const r = await call('POST', '/wp/v2/menu-items', { title: it.title, url: it.url, type: 'custom', object: 'custom', menus: menu.id, parent, menu_order: order, status: 'publish' }); console.log('  item', it.title, r.status, r.json && r.json.id); ex = r.json; }
    else console.log('  vorhanden', it.title);
    for (const c of it.children || []) await add(c, ex.id);
  };
  for (const it of m.items) await add(it, 0);
  const fin = (await call('GET', `/wp/v2/menu-items?menus=${menu.id}&per_page=100&_fields=id,title,url,parent,menu_order`)).json;
  console.log(m.slug, 'id', menu.id, JSON.stringify(fin.map(h => [h.menu_order, h.parent, h.title.rendered, h.url])));
}
await ctx.storageState({ path: S }); await b.close();
