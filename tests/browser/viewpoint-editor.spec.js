const { test, expect } = require('@playwright/test');
const fs = require('node:fs/promises');
const path = require('node:path');

test('FV Edit camera drag changes VPO, logs it, exports and reloads it', async ({ page }, testInfo) => {
  await page.goto('/PACKETS/tools/FV_Edit_Visual_Workbench.html');
  await expect(page.locator('#cameraMarker')).toBeVisible();
  const before = await page.locator('#cameraMarker').boundingBox();
  await page.locator('#cameraMarker').hover();
  await page.mouse.down();
  await page.mouse.move(before.x + before.width / 2 + 55, before.y + before.height / 2 + 24, { steps: 6 });
  await page.mouse.up();
  await expect(page.locator('#viewX')).not.toHaveValue('0');
  const { target } = await (async () => {
    const pending = page.waitForEvent('download');
    await page.locator('#exportBtn').click();
    const download = await pending;
    const target = path.join(testInfo.outputDir, download.suggestedFilename());
    await download.saveAs(target);
    return { target };
  })();
  const bundle = JSON.parse(await fs.readFile(target, 'utf8'));
  expect(bundle.viewpoint[0].pose.position.x).not.toBe(0);
  expect(bundle['edit_log.json'].some(e => String(e.target).startsWith('VP-'))).toBeTruthy();
  await page.locator('#importInput').setInputFiles({ name: 'roundtrip.json', mimeType: 'application/json', buffer: await fs.readFile(target) });
  await expect(page.locator('#viewX')).not.toHaveValue('0');
});

test('FV Edit viewpoint command updates pose and records before/after', async ({ page }) => {
  await page.goto('/PACKETS/tools/FV_Edit_Visual_Workbench.html');
  const viewpointId = await page.locator('#cameraMarker').getAttribute('data-viewpoint-id');
  await page.locator('#command').fill(`fv edit viewpoint set ${viewpointId} position 2 1 5`);
  await page.locator('#runCommand').click();
  await expect(page.locator('#viewX')).toHaveValue('2');
  await expect(page.locator('#history')).toContainText(viewpointId);
});

test('FV Edit schematic explicitly does not claim to render a new camera image', async ({ page }) => {
  await page.goto('/PACKETS/tools/FV_Edit_Visual_Workbench.html');
  await expect(page.locator('.banner')).toContainText('SCHEMATIC ONLY');
  await expect(page.locator('.banner')).toContainText('not an original/edited image rendering');
});
