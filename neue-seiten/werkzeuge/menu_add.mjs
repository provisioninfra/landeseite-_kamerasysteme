// Fügt einem bestehenden Menü Einträge hinzu (idempotent nach URL+Parent). env: STATE, MENU, PARENT, ITEMS (JSON [[titel,url,order],...]), MOVE (JSON [[id,order],...])
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const S = process.env.STATE, MENU = Number(process.env.MENU), PARENT = Number(process.env.PARENT || 0);
const ITEMS = JSON.parse(process.env.ITEMS || '[]'), MOVE = JSON.parse(process.env.MOVE || '[]');
const b = await chromium.launch(); const ctx = await b.newContext({ storageState: S }); const page = await ctx.newPage();
await page.goto('https://provision-infra.de/wp-admin/edit.php?post_type=page', { waitUntil: 'domcontentloaded' });
const nonce = await page.evaluate(() => window.wpApiSettings.nonce);
const api = (method, path, body) => page.evaluate(async ({ method, path, body, nonce }) => { const r = await fetch('/wp-json' + path, { method, headers: { 'X-WP-Nonce': nonce, 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined }); return { status: r.status, json: await r.json().catch(() => null) }; }, { method, path, body, nonce });
const sleep = ms => new Promise(r => setTimeout(r, ms));
const call = async (m, p, body) => { for (let t = 0; t < 6; t++) { await sleep(t ? 30000 : 5000); const r = await api(m, p, body); if (r.status !== 429) return r; } };
const have = (await call('GET', `/wp/v2/menu-items?menus=${MENU}&per_page=100&_fields=id,url,parent`)).json;
for (const [title, url, order] of ITEMS) {
  if (have.some(h => h.url === url && h.parent === PARENT)) { console.log('vorhanden', title); continue; }
  const r = await call('POST', '/wp/v2/menu-items', { title, url, type: 'custom', object: 'custom', menus: MENU, parent: PARENT, menu_order: order, status: 'publish' });
  console.log('neu', title, r.status);
}
for (const [id, order] of MOVE) { const r = await call('POST', `/wp/v2/menu-items/${id}`, { menu_order: order }); console.log('verschoben', id, order, r.status); }
const fin = (await call('GET', `/wp/v2/menu-items?menus=${MENU}&per_page=100&_fields=id,title,url,parent,menu_order`)).json;
console.log(JSON.stringify(fin.sort((a, b) => a.menu_order - b.menu_order).map(h => [h.menu_order, h.parent, h.title.rendered])));
await ctx.storageState({ path: S }); await b.close();
