import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const S = process.env.STATE, PAGE_ID = process.env.PAGE_ID;
const seo = JSON.parse(fs.readFileSync(process.env.DATA, 'utf8')).seo;
const b = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: S, viewport: { width: 1400, height: 1000 } });
const page = await ctx.newPage();
page.on('dialog', d => d.accept().catch(() => {}));
await page.goto(`https://provision-infra.de/wp-admin/post.php?post=${PAGE_ID}&action=edit`, { waitUntil: 'domcontentloaded', timeout: 120000 });
await page.waitForFunction(() => window.wp && wp.data && wp.data.select('yoast-seo/editor') && wp.data.select('core/editor').getCurrentPostId(), null, { timeout: 120000 });
await page.waitForTimeout(6000);
const r = await page.evaluate(async (seo) => {
  const y = wp.data.dispatch('yoast-seo/editor');
  y.updateData({ title: seo.title, description: seo.description });
  y.setFocusKeyword(seo.focuskw); y.setBreadcrumbsTitle(seo.bctitle); y.setNoIndex(seo.robots_noindex);
  y.setFacebookPreviewTitle(seo.title); y.setFacebookPreviewDescription(seo.description);
  if (y.setFacebookPreviewImage && seo.og_image) y.setFacebookPreviewImage({ url: seo.og_image, id: seo.og_image_id || 398 });
  await new Promise(r => setTimeout(r, 6000));
  // Klassische Metabox-Felder (werden mit dem Beitrag gespeichert) prüfen und notfalls direkt setzen
  const want = { 'yoast_wpseo_title': seo.title, 'yoast_wpseo_metadesc': seo.description, 'yoast_wpseo_focuskw': seo.focuskw,
                 'yoast_wpseo_bctitle': seo.bctitle, 'yoast_wpseo_meta-robots-noindex': seo.robots_noindex,
                 'yoast_wpseo_opengraph-title': seo.title, 'yoast_wpseo_opengraph-description': seo.description };
  if (seo.og_image) { want['yoast_wpseo_opengraph-image'] = seo.og_image; if (seo.og_image_id) want['yoast_wpseo_opengraph-image-id'] = String(seo.og_image_id); }
  const before = {}, missing = [];
  for (const [id, v] of Object.entries(want)) {
    const el = document.getElementById(id); before[id] = el ? el.value : '(kein Feld)';
    if (el && el.value !== v) { el.value = v; el.dispatchEvent(new Event('change', { bubbles: true })); }
    if (!el) missing.push(id);
  }
  const hasMetaBoxes = !!(wp.data.select('core/edit-post') && wp.data.select('core/edit-post').hasMetaBoxes && wp.data.select('core/edit-post').hasMetaBoxes());
  await wp.data.dispatch('core/editor').savePost();
  for (let i = 0; i < 40; i++) { await new Promise(r => setTimeout(r, 500)); const s = wp.data.select('core/editor'), e = wp.data.select('core/edit-post');
    if (!s.isSavingPost() && !(e && e.isSavingMetaBoxes && e.isSavingMetaBoxes())) break; }
  await new Promise(r => setTimeout(r, 2000));
  const after = {}; for (const id of Object.keys(want)) { const el = document.getElementById(id); after[id] = el ? el.value : '(kein Feld)'; }
  return { hasMetaBoxes, missing, before, after };
}, seo);
console.log(JSON.stringify(r, null, 1));
await page.waitForTimeout(3000);
await ctx.storageState({ path: S }); await b.close();
