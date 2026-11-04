const { test, expect } = require('@playwright/test');
const fs = require('node:fs/promises');
const path = require('node:path');

const APP = '/PACKETS/tools/FV_Media_Object_Editor_MVP.html';
const PACKET = [{ id: 'cat_01', type: 'cat', description: 'test cat', properties: { colour: 'orange' } }];

async function makeVideo(page) {
  return page.evaluate(async () => {
    const canvas = document.createElement('canvas');
    canvas.width = 320;
    canvas.height = 180;
    const ctx = canvas.getContext('2d');
    const stream = canvas.captureStream(12);
    const mime = MediaRecorder.isTypeSupported('video/webm;codecs=vp8') ? 'video/webm;codecs=vp8' : 'video/webm';
    const recorder = new MediaRecorder(stream, { mimeType: mime });
    const chunks = [];
    recorder.addEventListener('dataavailable', event => {
      if (event.data.size) chunks.push(event.data);
    });
    const stopped = new Promise(resolve => recorder.addEventListener('stop', resolve, { once: true }));
    recorder.start();
    for (let i = 0; i < 12; i++) {
      ctx.fillStyle = `hsl(${i * 28} 75% 48%)`;
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(i * 20, 35, 35, 35);
      await new Promise(resolve => setTimeout(resolve, 85));
    }
    recorder.stop();
    await stopped;
    stream.getTracks().forEach(track => track.stop());
    const blob = new Blob(chunks, { type: mime });
    const bytes = new Uint8Array(await blob.arrayBuffer());
    let binary = '';
    for (const byte of bytes) binary += String.fromCharCode(byte);
    return btoa(binary);
  });
}

async function loadEditor(page, videoBytes) {
  await page.goto(APP);
  await page.locator('#videoFile').setInputFiles({
    name: 'synthetic-test.webm',
    mimeType: 'video/webm',
    buffer: Buffer.from(videoBytes, 'base64')
  });
  await expect(page.locator('#status')).toContainText('Video ready (320×180');
}

async function loadPacket(page) {
  await page.locator('#packetFile').setInputFiles({
    name: 'OI.json',
    mimeType: 'application/json',
    buffer: Buffer.from(JSON.stringify(PACKET))
  });
  await expect(page.locator('#status')).toContainText('Packet loaded: OI.json');
  await expect(page.locator('#object')).toBeEnabled();
  await expect(page.locator('#object')).toHaveValue('cat_01');
}

async function drawTriangle(page) {
  const canvas = page.locator('#view');
  await canvas.click({ position: { x: 80, y: 55 } });
  await canvas.click({ position: { x: 190, y: 65 } });
  await canvas.click({ position: { x: 130, y: 145 } });
}

async function saveDownload(page, selector, testInfo) {
  const pending = page.waitForEvent('download');
  await page.locator(selector).click();
  const download = await pending;
  const target = path.join(testInfo.outputDir, download.suggestedFilename());
  await download.saveAs(target);
  return { download, target };
}

test('loads real video and packet, edits only the selected object, saves keyframes and exports packet JSON', async ({ page }, testInfo) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  await loadPacket(page);

  await page.locator('#property').fill('appearance');
  await page.locator('#value').fill('orange tabby');
  await page.locator('#apply').click();
  await expect(page.locator('#status')).toContainText('Updated 1 matching record(s) for cat_01');

  await drawTriangle(page);
  await page.locator('#key').click();
  await expect(page.locator('#keyList')).toContainText('3 points');

  await page.locator('#clear').click();
  await page.locator('#source').evaluate(v => new Promise(resolve => {
    v.addEventListener('seeked', resolve, { once: true });
    v.currentTime = v.duration / 2;
  }));
  await drawTriangle(page);
  await page.locator('#key').click();
  await expect(page.locator('#keyList')).toContainText('3 points');
  expect(await page.locator('#keyList div').count()).toBe(2);

  const { target } = await saveDownload(page, '#savePacket', testInfo);
  const out = JSON.parse(await fs.readFile(target, 'utf8'));
  expect(out.format).toBe('fv-media-edit-mvp-v2');
  expect(out.packet.OI).toHaveLength(1);
  expect(out.packet.OI[0].id).toBe('cat_01');
  expect(out.packet.OI[0].properties.appearance).toBe('orange tabby');
  expect(out.packet.viewpoint).toHaveLength(1);
  expect(out.packet.viewpoint[0].role).toBe('render_preset');
  expect(out.packet.viewpoint[0].initial_state.status).toBe('unknown');
  expect(out.packet.viewpoint[0].pose.position.z).toBe(5);
  expect(out.packet.viewpoint[0].pose.framing.aspect_ratio).toBeCloseTo(16/9, 3);
  expect(out.edit_log.map(e => e.type)).toContain('viewpoint_edit');
  expect(out.media_edits.object_id).toBe('cat_01');
  expect(out.media_edits.mask_keyframes).toHaveLength(2);
  expect(out.edit_log.map(e => e.type)).toContain('property_edit');
  expect(out.edit_log.filter(e => e.type === 'mask_keyframe')).toHaveLength(2);
  expect(out.limitations).toContain('Mask polygons are manually authored; tracking is not automatic.');
});

test('refuses fewer than three polygon points and does not invent keyframes', async ({ page }) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  await page.locator('#key').click();
  await expect(page.locator('#status')).toHaveText('Draw at least three polygon points first.');
  await page.locator('#view').click({ position: { x: 80, y: 55 } });
  await page.locator('#view').click({ position: { x: 190, y: 65 } });
  await page.locator('#key').click();
  await expect(page.locator('#status')).toHaveText('Draw at least three polygon points first.');
  await expect(page.locator('#keyList')).toHaveText('No shape keyframes yet.');
});

test('malformed packet JSON does not discard a previously loaded object selection', async ({ page }) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  await loadPacket(page);
  await page.locator('#packetFile').setInputFiles({
    name: 'broken.json',
    mimeType: 'application/json',
    buffer: Buffer.from('{ this is not valid JSON')
  });
  await expect(page.locator('#status')).toContainText('Could not parse JSON');
  await expect(page.locator('#object')).toBeEnabled();
  await expect(page.locator('#object')).toHaveValue('cat_01');
});

test('exports a WebM render after a saved mask keyframe', async ({ page }, testInfo) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  await drawTriangle(page);
  await page.locator('#key').click();
  await page.locator('#source').evaluate(v => new Promise(resolve => {
    v.addEventListener('seeked', resolve, { once: true });
    v.currentTime = v.duration / 2;
  }));

  const { target, download } = await saveDownload(page, '#export', testInfo);
  expect(download.suggestedFilename()).toBe('fv-edited-video.webm');
  const bytes = await fs.readFile(target);
  expect(bytes.length).toBeGreaterThan(1000);
  expect([...bytes.subarray(0, 4)]).toEqual([0x1a, 0x45, 0xdf, 0xa3]);
  await expect(page.locator('#status')).toContainText('Video export complete');
});


test('integrates a real Wikimedia CCTV clip with canonical_id packet entities', async ({ page }, testInfo) => {
  test.skip(!process.env.FV_REAL_MEDIA_PATH, 'CI supplies a short VP9/WebM excerpt from the documented source clip');
  test.setTimeout(120000);
  const videoBytes = await fs.readFile(process.env.FV_REAL_MEDIA_PATH);
  const packetPath = path.resolve(__dirname, '../../PACKETS/examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/OI.json');
  const packetBytes = await fs.readFile(packetPath);
  const objectId = 'PKT-CCTV-001-OBJ-046';

  await page.goto(APP);
  await page.locator('#videoFile').setInputFiles({
    name: 'cctv-part1-real-source-excerpt.webm',
    mimeType: 'video/webm',
    buffer: videoBytes
  });
  await expect(page.locator('#status')).toContainText('Video ready (');
  await page.locator('#packetFile').setInputFiles({
    name: 'OI.json',
    mimeType: 'application/json',
    buffer: packetBytes
  });
  await expect(page.locator('#object')).toBeEnabled();
  await page.locator('#object').selectOption(objectId);
  await expect(page.locator('#object')).toHaveValue(objectId);

  await page.locator('#property').fill('editor_test');
  await page.locator('#value').fill('canonical_id edit verified on real CCTV media');
  await page.locator('#apply').click();
  await expect(page.locator('#status')).toContainText('Updated 1 matching record(s) for ' + objectId);

  await drawTriangle(page);
  await page.locator('#key').click();
  await expect(page.locator('#keyList')).toContainText('3 points');

  const { target: packetTarget } = await saveDownload(page, '#savePacket', testInfo);
  const exported = JSON.parse(await fs.readFile(packetTarget, 'utf8'));
  const entity = exported.packet.entities.find(item => item.canonical_id === objectId);
  expect(entity.properties.editor_test).toBe('canonical_id edit verified on real CCTV media');
  expect(exported.packet.entities.find(item => item.canonical_id !== objectId && item.properties?.editor_test))
    .toBeUndefined();
  expect(exported.media_edits.object_id).toBe(objectId);
  expect(exported.edit_log.map(edit => edit.type)).toContain('property_edit');
  expect(exported.edit_log.filter(edit => edit.type === 'mask_keyframe')).toHaveLength(1);

  const { target: videoTarget, download } = await saveDownload(page, '#export', testInfo);
  expect(download.suggestedFilename()).toBe('fv-edited-video.webm');
  const rendered = await fs.readFile(videoTarget);
  expect(rendered.length).toBeGreaterThan(1000);
  expect([...rendered.subarray(0, 4)]).toEqual([0x1a, 0x45, 0xdf, 0xa3]);
  await expect(page.locator('#status')).toContainText('Video export complete');
});


test('creates, edits, switches and exports reusable viewpoint presets without changing OI', async ({ page }, testInfo) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  await loadPacket(page);
  await expect(page.locator('#viewpoint')).toBeEnabled();
  await expect(page.locator('#viewpoint option')).toHaveCount(1);

  await page.locator('#camX').fill('2.5');
  await page.locator('#camY').fill('1.25');
  await page.locator('#camZ').fill('7');
  await page.locator('#camYaw').fill('30');
  await page.locator('#camPitch').fill('-10');
  await page.locator('#camRoll').fill('5');
  await page.locator('#camFov').fill('60');
  await page.locator('#camAspect').fill('1.5');
  await page.locator('#targetX').fill('0');
  await page.locator('#targetY').fill('1');
  await page.locator('#targetZ').fill('0');
  await page.locator('#saveViewpoint').click();
  await expect(page.locator('#status')).toContainText('VPO saved');

  await page.locator('#newViewpoint').click();
  await expect(page.locator('#viewpoint option')).toHaveCount(2);
  const newId = await page.locator('#viewpoint').inputValue();
  expect(newId).toMatch(/^VP-[A-F0-9]{12}$/);
  await page.locator('#camZ').fill('9');
  await page.locator('#saveViewpoint').click();
  await page.locator('#viewpoint').selectOption({ index: 0 });
  await expect(page.locator('#camZ')).toHaveValue('7');
  await page.locator('#viewpoint').selectOption(newId);
  await expect(page.locator('#camZ')).toHaveValue('9');

  const { target } = await saveDownload(page, '#savePacket', testInfo);
  const out = JSON.parse(await fs.readFile(target, 'utf8'));
  expect(out.format).toBe('fv-media-edit-mvp-v2');
  expect(out.packet.OI).toEqual(PACKET);
  expect(out.packet.viewpoint).toHaveLength(2);
  const first = out.packet.viewpoint[0];
  expect(first.pose.position).toEqual({ x: 2.5, y: 1.25, z: 7 });
  expect(first.pose.orientation).toMatchObject({
    representation: 'intrinsic_euler', yaw: 30, pitch: -10, roll: 5,
    unit: 'degrees', rotation_order: 'Y-X-Z'
  });
  expect(first.pose.projection).toBe('perspective');
  expect(first.pose.field_of_view_degrees).toBe(60);
  expect(first.pose.target).toEqual({ x: 0, y: 1, z: 0 });
  expect(first.pose.framing.aspect_ratio).toBe(1.5);
  expect(out.packet.viewpoint[1].pose.position.z).toBe(9);
  expect(out.packet.viewpoint.filter(v => v.is_default)).toHaveLength(1);
  expect(out.edit_log.filter(e => e.type === 'viewpoint_edit').length).toBeGreaterThanOrEqual(2);
});

test('loads an existing viewpoint.json record and preserves its source provenance', async ({ page }, testInfo) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  const packet = {
    OI: PACKET,
    viewpoint: [{
      id: 'VP-SOURCE0001',
      role: 'source',
      observer: { type: 'camera' },
      initial_state: { status: 'known', position: 'fixed tripod', orientation: 'level', basis: 'source metadata' }
    }]
  };
  await page.locator('#packetFile').setInputFiles({
    name: 'packet.json', mimeType: 'application/json', buffer: Buffer.from(JSON.stringify(packet))
  });
  await expect(page.locator('#viewpoint')).toBeEnabled();
  await expect(page.locator('#viewpoint')).toHaveValue('VP-SOURCE0001');
  await page.locator('#camX').fill('3');
  await page.locator('#saveViewpoint').click();
  const { target } = await saveDownload(page, '#savePacket', testInfo);
  const out = JSON.parse(await fs.readFile(target, 'utf8'));
  expect(out.packet.viewpoint[0].initial_state).toEqual(packet.viewpoint[0].initial_state);
  expect(out.packet.viewpoint[0].role).toBe('source_and_render');
  expect(out.packet.viewpoint[0].pose.position.x).toBe(3);
});
