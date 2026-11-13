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
  // Legacy packet import must not silently materialize a render VPO.
  await expect(page.locator('#viewpoint')).toBeDisabled();
  await expect(page.locator('#cameraPin')).toBeHidden();
  // Explicit user action instantiates the canonical VPO_DEFAULT template.
  await page.locator('#newViewpoint').click();
  await expect(page.locator('#viewpoint')).toBeEnabled();
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
  const viewpointSchema = JSON.parse(await fs.readFile(path.resolve(__dirname, '../../SPECIFICATION/FV_Viewpoint_Schema.json'), 'utf8'));
  expect(viewpointSchema.items.properties.pose.additionalProperties).toBe(false);
  expect(viewpointSchema.items.properties.metadata.additionalProperties).toBe(true);
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



test('draggable camera icon edits VPO, logs before/after and exports the changed viewpoint', async ({ page }, testInfo) => {
  const video = await makeVideo(page);
  await loadEditor(page, video);
  await loadPacket(page);
  await expect(page.locator('#cameraPin')).toBeVisible();
  const before = await page.locator('#cameraPin').boundingBox();
  await page.locator('#cameraPin').hover();
  await page.mouse.down();
  await page.mouse.move(before.x + before.width / 2 + 45, before.y + before.height / 2 + 20);
  await page.mouse.up();
  await expect(page.locator('#log')).toContainText('Updated VPO');
  const { target } = await saveDownload(page, '#savePacket', testInfo);
  const out = JSON.parse(await fs.readFile(target, 'utf8'));
  expect(out.packet.viewpoint[0].pose.position.x).not.toBe(0);
  expect(out.edit_log.some(e => e.type === 'viewpoint_edit' && e.before && e.after)).toBeTruthy();
  expect(out.limitations.some(s => s.includes('does not reconstruct missing 3D geometry') && s.includes('new physical camera position'))).toBeTruthy();
});


test('loads a still image, drags the camera overlay, logs and exports the image viewpoint', async ({ page }, testInfo) => {
  await page.goto(APP);
  const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jXioAAAAASUVORK5CYII=', 'base64');
  await page.locator('#imageFile').setInputFiles({ name: 'viewpoint-source.png', mimeType: 'image/png', buffer: png });
  await expect(page.locator('#status')).toContainText('Still image loaded.');
  await loadPacket(page);
  await expect(page.locator('#cameraPin')).toBeVisible();
  const before = await page.locator('#cameraPin').boundingBox();
  await page.locator('#cameraPin').hover();
  await page.mouse.down();
  await page.mouse.move(before.x + before.width / 2 + 22, before.y + before.height / 2 + 12, { steps: 6 });
  await page.mouse.up();
  await expect(page.locator('#log')).toContainText('Updated VPO');
  await page.locator('#camYaw').fill('18');
  await page.locator('#camPitch').fill('9');
  await page.locator('#renderPerspective').click();
  await expect(page.locator('#perspectiveOutput')).toBeVisible();
  await expect(page.locator('#log')).toContainText('Generated planar perspective approximation');
  const pngDownload = page.waitForEvent('download');
  await page.locator('#downloadPerspective').click();
  expect((await pngDownload).suggestedFilename()).toBe('fv-perspective-approximation.png');
  const { target } = await saveDownload(page, '#savePacket', testInfo);
  const out = JSON.parse(await fs.readFile(target, 'utf8'));
  expect(out.packet.viewpoint[0].metadata.editor_image_anchor.x).not.toBe(0.5);
  expect(out.packet.viewpoint[0].metadata.planar_image_render.method).toBe('planar_affine_projection');
  expect(out.packet.viewpoint[0].metadata.planar_image_render.limitation).toContain('No hidden-surface reconstruction');
  expect(out.edit_log.some(e => e.type === 'viewpoint_edit')).toBeTruthy();
  expect(out.edit_log.some(e => e.type === 'perspective_image_render')).toBeTruthy();
});

test('integrates a real Wikimedia CCTV clip with canonical_id packet entities', async ({ page }, testInfo) => {
  test.skip(!process.env.FV_REAL_MEDIA_PATH, 'CI supplies a short VP9/WebM excerpt from the documented source clip');
  test.setTimeout(120000);
  const videoBytes = await fs.readFile(process.env.FV_REAL_MEDIA_PATH);
  const packetPath = path.resolve(__dirname, '../../examples/videos/CCTV_Snapshot_TD_Reconstruction_Experiment/PKT-CCTV-001/OI.json');
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
