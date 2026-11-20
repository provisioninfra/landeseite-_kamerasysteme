// Vorschau eines Entwurfs (angemeldet) in mehreren Breiten: Screenshot, horizontaler Überlauf, Konsolenfehler. env: STATE, PAGE_ID, OUT
import { chromium, devices } from '/opt/node-tools/node_modules/playwright/index.mjs';
const S = process.env.STATE, ID = process.env.PAGE_ID, OUT = process.env.OUT;
const b = await chromium.launch();
for (const [name, opt] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['handy', devices['iPhone 13']]]) {
  const ctx = await b.newContext({ ...opt, storageState: S, locale: 'de-DE' });
  const page = await ctx.newPage(); const errs = [];
  page.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 140)); });
  await page.goto(`https://provision-infra.de/?page_id=${ID}&preview=true`, { waitUntil: 'load', timeout: 120000 });
  await page.waitForTimeout(3000);
  // langsam scrollen, damit Einblend-Animationen auslösen
  await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } window.scrollTo(0, 0); });
  await page.waitForTimeout(1500);
  const info = await page.evaluate(() => ({ breite: document.documentElement.scrollWidth, fenster: innerWidth, hoehe: document.body.scrollHeight,
    h1: [...document.querySelectorAll('h1')].map(h => h.innerText.trim()), menu: [...document.querySelectorAll('header nav a, .elementor-nav-menu a')].slice(0, 12).map(a => a.innerText.trim()).filter(Boolean),
    breitesElement: [...document.querySelectorAll('body *')].filter(e => e.getBoundingClientRect().right > innerWidth + 2 && getComputedStyle(e).position !== 'fixed').slice(0, 5).map(e => (e.className || e.tagName).toString().slice(0, 60)) }));
  console.log(name, JSON.stringify(info));
  if (errs.length) console.log('  konsole:', errs.slice(0, 5));
  await page.screenshot({ path: `${OUT}-${name}.png`, fullPage: true });
  await ctx.close();
}
await b.close();
