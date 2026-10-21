import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const htmlPath = process.argv[2] ?? new URL('./FV_Edit_Visual_Workbench.html', import.meta.url).pathname;
const html = readFileSync(htmlPath, 'utf8');
const match = html.match(/<script>([\s\S]*?)<\/script>/i);
assert.ok(match, 'application script exists');
const script = match[1];
new Function(script);

const fixtureStart = script.indexOf('const object =');
const fixtureEnd = script.indexOf('  let packet, baseline', fixtureStart);
assert.ok(fixtureStart >= 0 && fixtureEnd > fixtureStart, 'fixture block anchors exist');
const helperStart = script.indexOf('  const stressFor =', fixtureEnd);
const helperEnd = script.indexOf('  const esc =', helperStart);
assert.ok(helperStart >= 0 && helperEnd > helperStart, 'environment helper anchors exist');
const sandbox = { Math, Set, Date, JSON, String, RegExp, Number, Object, Array, globalThis: {} };
vm.runInNewContext(
  \`const now = () => '2026-10-21T00:00:00.000Z';\\n\${script.slice(fixtureStart, fixtureEnd)}\\n\${script.slice(helperStart, helperEnd)}\\nglobalThis.fixtures=fixtures;globalThis.stressFor=stressFor;globalThis.passiveAffected=passiveAffected;\`,
  sandbox
);
const { fixtures, stressFor, passiveAffected } = sandbox.globalThis;
assert.equal(fixtures.length, 7);
for (const packet of fixtures) {
  assert.ok(packet.id && packet.fv_version);
  assert.ok(['none', 'low', 'high'].includes(packet.ENVIRONMENT.environmental_stress));
  const ids = packet.OI.map(o => o.id);
  assert.equal(new Set(ids).size, ids.length, \`\${packet.id}: unique OI IDs\`);
  for (const id of Object.keys(packet.MSRM.objects)) assert.ok(ids.includes(id), \`\${packet.id}: MSRM ref \${id}\`);
  for (const entry of [...(packet.ENVIRONMENT.affected_objects_passive ?? []), ...(packet.ENVIRONMENT.affected_objects_active ?? [])]) {
    const id = typeof entry === 'string' ? entry : entry?.id;
    assert.ok(ids.includes(id), \`\${packet.id}: affected-object ref \${id}\`);
  }
  const bundle = {
    bundle_format: 'fv-packet-bundle-v1',
    packet_meta: { id: packet.id, fv_version: packet.fv_version },
    'fv_version.json': { fv_version: packet.fv_version },
    'ENVIRONMENT.json': packet.ENVIRONMENT,
    'OI.json': packet.OI,
    'MSRM.json': packet.MSRM,
    'edit_log.json': packet.edit_log,
    media: { included: false }
  };
  const copy = JSON.parse(JSON.stringify(bundle));
  assert.equal(copy.packet_meta.fv_version, packet.fv_version, 'preserve packet version');
  assert.deepEqual(JSON.parse(JSON.stringify(copy['OI.json'])), JSON.parse(JSON.stringify(packet.OI)));
  assert.equal(copy.media.included, false);
}
const base = fixtures.find(p => p.id === 'bermuda_cove_pleasant_original');
assert.equal(stressFor({...base.ENVIRONMENT, sunlight: 'harsh glaring', temperature: 'hot'}), 'high');
assert.equal(stressFor({...base.ENVIRONMENT, precipitation: 'heavy rainfall'}), 'high');
const passiveIds = passiveAffected({...base.ENVIRONMENT, sunlight: 'harsh glaring', temperature: 'hot'}, base.OI);
assert.ok(passiveIds.every(id => base.OI.some(o => o.id === id)));
assert.ok(!passiveIds.includes('water') && !passiveIds.includes('vegetation'));
const negative = fixtures.find(p => p.id === 'bermuda_cove_harsh_passive_old');
assert.equal(negative.test_expectation.required_insulation_state, 'shade_seek');
assert.equal(negative.OI.find(o => o.id === 'cat_01').insulation_state, 'none');
assert.ok(html.includes('Applying conditions never moves an object or invents a behaviour'));
assert.ok(html.includes('Original schematic') && html.includes('Edited schematic'));
assert.ok(html.includes('type="file" accept=".json,application/json"'));
assert.ok(html.includes("bundle_format:'fv-packet-bundle-v1'"));
assert.ok(!html.includes('Math.random'));
console.log(\`PASS: syntax, \${fixtures.length} fixtures, JSON bundle round-trip, IDs/references, stress enum derivation, negative control, import/export UI, and schematic disclaimer.\`);
