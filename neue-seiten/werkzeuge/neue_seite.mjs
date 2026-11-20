// Legt eine Seite als Entwurf an (falls Slug noch nicht existiert) und gibt die ID aus. env: STATE, TITLE, SLUG
import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
const S = process.env.STATE;
const b = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: S });
const page = await ctx.newPage();
await page.goto('https://provision-infra.de/wp-admin/edit.php?post_type=page', { waitUntil: 'domcontentloaded' });
const nonce = await page.evaluate(() => window.wpApiSettings.nonce);
const api = (method, path, body) => page.evaluate(async ({ method, path, body, nonce }) => {
  const r = await fetch('/wp-json' + path, { method, headers: { 'X-WP-Nonce': nonce, 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined });
  return { status: r.status, json: await r.json().catch(() => null) };
}, { method, path, body, nonce });
const ex = await api('GET', `/wp/v2/pages?slug=${encodeURIComponent(process.env.SLUG)}&status=draft,publish,pending,private&_fields=id,status,slug`);
if (ex.json && ex.json.length) { console.log('ID', ex.json[0].id, 'vorhanden', ex.json[0].status); }
else {
  const r = await api('POST', '/wp/v2/pages', { title: process.env.TITLE, slug: process.env.SLUG, status: 'draft', ...(process.env.PARENT ? { parent: Number(process.env.PARENT) } : {}) });
  console.log('ID', r.json && r.json.id, 'neu', r.status, r.json && r.json.slug);
}
await ctx.storageState({ path: S }); await b.close();
