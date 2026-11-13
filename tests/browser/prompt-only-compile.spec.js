const { test, expect } = require('@playwright/test');
const fs = require('node:fs/promises');
const path = require('node:path');

const ROOT = path.resolve(__dirname, '../..');
const PACKET = path.join(ROOT, 'examples/videos/Cat_jumping_backwards');
const FIXTURE = path.join(ROOT, 'tests/fixtures/prompt-only-cat');
const readJson = async file => JSON.parse(await fs.readFile(file, 'utf8'));

// Contract-fixture check only. The repository defines fv compile as an
// agent/skill interaction; it does not contain an executable prompt compiler.
// This test checks a representative golden prompt, not compiler execution.
test('prompt-only golden fixture preserves packet facts and selected render VPO', async () => {
  const [oi, msrm, td, vpo, prompt] = await Promise.all([
    readJson(path.join(PACKET, 'OI.json')),
    readJson(path.join(PACKET, 'MSRM.json')),
    readJson(path.join(PACKET, 'TD.json')),
    readJson(path.join(FIXTURE, 'viewpoint.json')),
    fs.readFile(path.join(FIXTURE, 'COMPILED_PROMPT.txt'), 'utf8')
  ]);
  expect(oi.entities).toHaveLength(1);
  expect(prompt).toContain(oi.entities[0].canonical_id);
  expect(prompt).toContain(oi.entities[0].label);
  for (const scene of msrm.scenes) expect(prompt).toContain(scene.scene_id);
  expect(prompt).toContain(td.timeline[1].changes[0].temporal_scaling.toString());
  expect(vpo).toHaveLength(1);
  const v = vpo[0];
  expect(v.id).toBe('VP-TEST-0001');
  expect(v.role).toBe('render_preset');
  expect(v.is_default).toBe(true);
  expect(v.initial_state.status).toBe('unknown');
  expect(prompt).toContain(v.id);
  expect(prompt).toContain(v.coordinate_frame.id);
  expect(prompt).toContain('x=' + v.pose.position.x);
  expect(prompt).toContain('y=' + v.pose.position.y);
  expect(prompt).toContain('z=' + v.pose.position.z);
  expect(prompt).toContain('Yaw: ' + v.pose.orientation.yaw + ' degrees');
  expect(prompt).toContain('Pitch: ' + v.pose.orientation.pitch + ' degrees');
  expect(prompt).toContain('Roll: ' + v.pose.orientation.roll + ' degrees');
  expect(prompt).toContain(v.pose.orientation.rotation_order);
  expect(prompt).toContain(v.pose.projection);
  expect(prompt).toContain(String(v.pose.field_of_view_degrees));
  expect(prompt).toContain('Source viewpoint initial_state');
  expect(prompt).toContain('declared default render viewpoint');
  for (const required of ['unresolved','No second cat','No additional people','No second cat, people, or props','No invented floor','APPROXIMATE / UNSUPPORTED','Do not invoke a generator','complete output of prompt-only compilation']) {
    expect(prompt).toContain(required);
  }
});

// Regression: a stale validation report and dispute.json status=resolved do
// not override an incomplete reconciliation record. fv compile must fail
// closed until post-reconciliation validation has actually been completed.
test('legacy Cat packet is not compilation-ready while reconciliation validation is pending', async () => {
  const [gate, reconciled, validation] = await Promise.all([
    readJson(path.join(PACKET, 'dispute.json')),
    readJson(path.join(PACKET, 'dispute.reconciled.json')),
    readJson(path.join(PACKET, 'VALIDATION_REPORT_POST_RESOLVE.txt'))
  ]);
  expect(gate.status).toBe('resolved');
  expect(reconciled.status).toBe('resolved');
  expect(reconciled.ai_reconciliation.validation_after_reconciliation).toBe('to be performed');
  expect(validation.overall_status).toContain('PARTIAL');
  expect(validation.checks.find(item => item.check === 'snapshot_structure').status).toBe('FAIL');
  expect(validation.checks.find(item => item.check === 'persistent_investigation_record').status).toBe('NOT PRESENT');
  expect(validation.checks.find(item => item.check === 'source_media_inspection').status).toBe('NOT PERFORMED');
  expect(validation.rendering_gate).toContain('permitted compilation with uncertainty preserved');
  expect(validation.rendering_gate).toContain('not a claim of visual verification');
  // Human permission to render with uncertainty does not replace the pending
  // post-reconciliation validation. The agent-level compile gate must block
  // until that validation is completed; this fixture is not a compile pass.
});
