import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const S = process.env.STATE, PAGE_ID = process.env.PAGE_ID, STATUS = process.env.POST_STATUS || 'draft';
const data = JSON.parse(fs.readFileSync(process.env.DATA, 'utf8'));
const settings = { ...data.settings, post_status: STATUS };
const b = await chromium.launch({ args: ['--disable-blink-features=AutomationControlled'] });
const ctx = await b.newContext({ storageState: S, viewport: { width: 1400, height: 1000 } });
const page = await ctx.newPage();
page.on('dialog', d => d.dismiss().catch(() => {}));
await page.goto(`https://provision-infra.de/wp-admin/post.php?post=${PAGE_ID}&action=elementor`, { waitUntil: 'domcontentloaded', timeout: 120000 });
await page.waitForFunction(() => window.elementorCommon && window.elementorCommon.ajax && window.elementor && window.elementor.documents, null, { timeout: 120000 });
await page.waitForTimeout(5000);
let res;
for (let t = 0; t < 6; t++) {
  if (t) await page.waitForTimeout(30000);
  res = await page.evaluate(({ elements, settings, status }) => new Promise(resolve => {
    elementorCommon.ajax.addRequest('save_builder', {
      data: { status, elements, settings },
      success: r => resolve({ ok: true, r: JSON.stringify(r).slice(0, 400) }),
      error: e => resolve({ ok: false, status: e && e.status, e: JSON.stringify(e).slice(0, 200) }),
    });
  }), { elements: data.elements, settings, status: STATUS });
  console.log('Versuch', t + 1, JSON.stringify(res));
  if (res.ok) break;
}
await ctx.storageState({ path: S });
await b.close();
