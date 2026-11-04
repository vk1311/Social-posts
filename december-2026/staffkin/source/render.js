const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const dir = '/home/claude/gen/html';
  const out = process.argv[2];
  fs.mkdirSync(out, { recursive: true });
  const list = JSON.parse(fs.readFileSync(path.join(dir, 'list.json')));
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  for (const s of list) {
    await page.goto('file://' + path.join(dir, s + '.html'));
    await page.evaluate(() => document.fonts.ready);
    // flag overflow: any element extending below the footer line
    const over = await page.evaluate(() => {
      const lim = 1350 - 140; let bad = [];
      document.querySelectorAll('.wrap *').forEach(e => { const r = e.getBoundingClientRect(); if (r.bottom > lim && r.height) bad.push(e.className || e.tagName); });
      return bad.slice(0, 3);
    });
    if (over.length) console.log('OVERFLOW', s, over.join(','));
    await page.screenshot({ path: path.join(out, s + '.png') });
  }
  await browser.close();
  console.log('done', list.length);
})();
