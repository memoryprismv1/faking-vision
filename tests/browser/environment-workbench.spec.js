const { test, expect } = require('@playwright/test');
const fs = require('node:fs/promises');
const os = require('node:os');
const path = require('node:path');

const APP = '/TOOLS/FV_Edit_Visual_Workbench.html';

async function exportBundle(page, testInfo) {
  const downloadPromise = page.waitForEvent('download');
  await page.locator('#exportBtn').click();
  const download = await downloadPromise;
  const file = path.join(testInfo.outputDir, download.suggestedFilename());
  await download.saveAs(file);
  return JSON.parse(await fs.readFile(file, 'utf8'));
}

async function loadFixture(page, label) {
  await page.goto(APP);
  await page.getByRole('button', { name: new RegExp(label) }).click();
}

test('environment-only edit preserves spatial records and appends an edit log', async ({ page }, testInfo) => {
  await loadFixture(page, 'Bermuda Cove · baseline');
  const before = await exportBundle(page, testInfo);
  const originalPosition = before['MSRM.json'].objects.cat_01;
  await page.locator('#wind').selectOption('strong windy');
  await page.locator('#applyEnv').click();
  const after = await exportBundle(page, testInfo);

  expect(after['MSRM.json'].objects.cat_01).toEqual(originalPosition);
  expect(after['OI.json'].find(o => o.id === 'cat_01').behavior_after).toBe('loafing on wall');
  expect(after['edit_log.json']).toHaveLength(before['edit_log.json'].length + 1);
  expect(after['edit_log.json'].at(-1).edit_base).toBe('collection');
  expect(after['edit_log.json'].at(-1).msrm_change).toContain('none');
  expect(after['ENVIRONMENT.json'].affected_objects_active).toEqual([]);
});

test('applying an unrelated environmental edit does not erase an existing authored active response', async ({ page }, testInfo) => {
  await loadFixture(page, 'Bermuda Cove · active shade response');
  const before = await exportBundle(page, testInfo);
  expect(before['ENVIRONMENT.json'].affected_objects_active.map(x => x.id)).toContain('cat_01');

  // Wind changes; the already-authored shade response remains relevant to harsh sun.
  await page.locator('#wind').selectOption('moderate');
  await page.locator('#applyEnv').click();
  const after = await exportBundle(page, testInfo);

  expect(after['ENVIRONMENT.json'].affected_objects_active.map(x => x.id)).toContain('cat_01');
  expect(after['OI.json'].find(o => o.id === 'cat_01').insulation_state).toBe('shade_seek');
  expect(after['MSRM.json'].objects.cat_01).toEqual(before['MSRM.json'].objects.cat_01);
});

test('explicit negative test expectation is reported as FAIL', async ({ page }) => {
  await loadFixture(page, 'Bermuda Cove · negative passive test');
  await page.locator('#validateBtn').click();
  await expect(page.locator('#validationBadge')).toHaveText('FAIL');
  await expect(page.locator('#validationMessages')).toContainText('explicit test expectation not met for cat_01');
});

test('legacy packet retains its version mapping through export', async ({ page }, testInfo) => {
  await loadFixture(page, 'Windy Day · baseline with wind response');
  const bundle = await exportBundle(page, testInfo);
  expect(bundle['fv_version.json'].fv_version).toBe('0.25');
  expect(bundle.packet_meta.fv_version).toBe('0.25');
  await expect(page.locator('#specVersion')).toHaveValue('0.25');
});

test('malformed duplicate-ID import is rejected without replacing the loaded packet', async ({ page }) => {
  await loadFixture(page, 'Bermuda Cove · baseline');
  const beforeTitle = await page.locator('#editedTitle').textContent();
  const invalid = {
    packet_meta: { id: 'invalid_duplicate' },
    'fv_version.json': { fv_version: '0.26' },
    'ENVIRONMENT.json': { environmental_stress: 'none' },
    'OI.json': [{ id: 'dup' }, { id: 'dup' }],
    'MSRM.json': { objects: {} },
    'edit_log.json': []
  };
  page.once('dialog', dialog => dialog.accept());
  await page.locator('#importInput').setInputFiles({
    name: 'duplicate-ids.json',
    mimeType: 'application/json',
    buffer: Buffer.from(JSON.stringify(invalid))
  });
  await expect(page.locator('#console')).toContainText('OI contains duplicate object IDs');
  await expect(page.locator('#editedTitle')).toHaveText(beforeTitle);
});

test('exported packet bundle re-imports and preserves packet records', async ({ page }, testInfo) => {
  await loadFixture(page, 'Wall Cat · active shelter response');
  const first = await exportBundle(page, testInfo);
  const file = path.join(os.tmpdir(), 'fv-roundtrip.json');
  await fs.writeFile(file, JSON.stringify(first));
  await page.reload();
  await page.locator('#importInput').setInputFiles(file);
  await expect(page.locator('#console')).toContainText('imported fv-roundtrip.json');
  const second = await exportBundle(page, testInfo);

  for (const key of ['fv_version.json', 'ENVIRONMENT.json', 'OI.json', 'MSRM.json', 'edit_log.json']) {
    expect(second[key]).toEqual(first[key]);
  }
  expect(second.media.included).toBe(false);
});


test('invalid environmental stress enum is rejected without replacing the packet', async ({ page }) => {
  await loadFixture(page, 'Bermuda Cove · baseline');
  const beforeTitle = await page.locator('#editedTitle').textContent();
  const invalid = {
    packet_meta: { id: 'invalid_stress' },
    'fv_version.json': { fv_version: '0.26' },
    'ENVIRONMENT.json': { environmental_stress: 'extreme' },
    'OI.json': [{ id: 'cat_01' }],
    'MSRM.json': { objects: { cat_01: { x: 1, y: 2 } } },
    'edit_log.json': []
  };
  page.once('dialog', dialog => dialog.accept());
  await page.locator('#importInput').setInputFiles({
    name: 'invalid-stress.json',
    mimeType: 'application/json',
    buffer: Buffer.from(JSON.stringify(invalid))
  });
  await expect(page.locator('#console')).toContainText('environmental_stress must be exactly none, low, or high');
  await expect(page.locator('#editedTitle')).toHaveText(beforeTitle);
});

test('missing required packet records and malformed MSRM map are rejected', async ({ page }) => {
  await loadFixture(page, 'Bermuda Cove · baseline');
  const beforeTitle = await page.locator('#editedTitle').textContent();
  const cases = [
    {
      name: 'missing-oi.json',
      data: {
        'ENVIRONMENT.json': { environmental_stress: 'none' },
        'MSRM.json': { objects: {} },
        'edit_log.json': []
      },
      message: 'Expected ENVIRONMENT object, OI array, MSRM.objects map'
    },
    {
      name: 'array-msrm.json',
      data: {
        'ENVIRONMENT.json': { environmental_stress: 'none' },
        'OI.json': [{ id: 'cat_01' }],
        'MSRM.json': { objects: [] },
        'edit_log.json': []
      },
      message: 'Expected ENVIRONMENT object, OI array, MSRM.objects map'
    }
  ];
  for (const item of cases) {
    page.once('dialog', dialog => dialog.accept());
    await page.locator('#importInput').setInputFiles({
      name: item.name,
      mimeType: 'application/json',
      buffer: Buffer.from(JSON.stringify(item.data))
    });
    await expect(page.locator('#console')).toContainText(item.message);
    await expect(page.locator('#editedTitle')).toHaveText(beforeTitle);
  }
});


test('environment edit writes only resolvable passive affected-object references', async ({ page }, testInfo) => {
  await loadFixture(page, 'Windy Day · baseline with wind response');
  await page.locator('#applyEnv').click();
  const bundle = await exportBundle(page, testInfo);
  const ids = new Set(bundle['OI.json'].map(o => o.id));
  for (const id of bundle['ENVIRONMENT.json'].affected_objects_passive) {
    expect(ids.has(typeof id === 'string' ? id : id.id)).toBe(true);
  }
  expect(bundle['ENVIRONMENT.json'].affected_objects_active.map(x => typeof x === 'string' ? x : x.id)).toContain('person_01');
});


test('environment edit appends to, rather than replaces, the prior edit history', async ({ page }, testInfo) => {
  await loadFixture(page, 'Wall Cat · active shelter response');
  const before = await exportBundle(page, testInfo);
  await page.locator('#applyEnv').click();
  const after = await exportBundle(page, testInfo);
  expect(after['edit_log.json'].slice(0, before['edit_log.json'].length)).toEqual(before['edit_log.json']);
  expect(after['edit_log.json']).toHaveLength(before['edit_log.json'].length + 1);
});


test('canonical_id packet imports, edits, exports and re-imports without adding legacy IDs', async ({ page }, testInfo) => {
  const canonicalId = 'PKT-CANONICAL-001-OBJ-001';
  const input = {
    bundle_format: 'fv-packet-bundle-v1',
    packet_meta: { id: 'canonical_packet', fv_version: '0.26' },
    'fv_version.json': { fv_version: '0.26' },
    'ENVIRONMENT.json': { environmental_stress: 'none', affected_objects_passive: [], affected_objects_active: [] },
    'OI.json': [{ canonical_id: canonicalId, category: 'vehicle', description: 'source description', properties: { appearance: 'silver sedan' } }],
    'MSRM.json': { reference: 'relative-only', objects: { [canonicalId]: { x: 41, y: 62 } } },
    'edit_log.json': []
  };
  await page.goto(APP);
  await page.locator('#importInput').setInputFiles({
    name: 'canonical-packet.json',
    mimeType: 'application/json',
    buffer: Buffer.from(JSON.stringify(input))
  });
  await expect(page.locator('#console')).toContainText('imported canonical-packet.json; 1 objects');
  await expect(page.locator('#objectList')).toContainText(canonicalId);
  await page.locator('[data-field="description"]').fill('edited through canonical identifier');
  await page.locator('#saveObject').click();
  const first = await exportBundle(page, testInfo);
  const firstRecord = first['OI.json'][0];
  expect(firstRecord.canonical_id).toBe(canonicalId);
  expect(firstRecord.id).toBeUndefined();
  expect(firstRecord.description).toBe('edited through canonical identifier');
  expect(first['MSRM.json'].objects[canonicalId]).toEqual({ x: 41, y: 62 });
  expect(first['edit_log.json'].at(-1).target).toBe(canonicalId);

  const file = path.join(testInfo.outputDir, 'canonical-roundtrip.json');
  await fs.writeFile(file, JSON.stringify(first));
  await page.reload();
  await page.locator('#importInput').setInputFiles(file);
  const second = await exportBundle(page, testInfo);
  expect(second['OI.json']).toEqual(first['OI.json']);
  expect(second['MSRM.json']).toEqual(first['MSRM.json']);
  expect(second['edit_log.json']).toEqual(first['edit_log.json']);
});
