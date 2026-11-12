# FV prompt-compilation acceptance procedure

**Status: PARTIAL — agent-level cases exercised 2026-11-12.** Case B (legacy viewpoint compatibility) and Case C (negative reconciliation gate) passed their defined checks. Case A demonstrated default-render-VPO selection and prompt-only output, but remains partial because the full validation gate—including a separately recorded rebuild assessment and full semantic/evidence/dispute readiness—was not executed. These are skill-runtime operations, not executable repository CLI commands. Playwright tests do not invoke an FV agent and must not be reported as proof that `fv validate` or `fv compile --prompt` executed.

## Acceptance boundary

The test covers packet validation and prompt-only compilation, not image/video generation or visual reconstruction. No generator may be invoked.

For each run, retain the exact input packet, validation report, prompt artifact (if produced), and run record identifying the FV skill/specification revision and agent/model. Do not overwrite the input packet.

## Case A — default render viewpoint, unchanged

Use a valid image packet with a root-level `viewpoint.json` containing a source viewpoint record whose `initial_state` is preserved as supported by evidence, plus a separately defined render VPO with `role: render_preset` (or `source_and_render`), a complete pose and coordinate frame, and `is_default: true`.

The default VPO may be a declared standard/test render pose. It is not a claim that the source camera occupied that pose. Do not edit it during this case.

1. Run `fv validate [packet]`. Confirm structural validity, semantic/evidence consistency, dispute/reconciliation state, rebuild assessment, and compilation readiness separately. Confirm the VPO schema and unique-default rule are checked.
2. Run `fv compile --prompt [same packet]` without an explicit VPO selection.
3. Confirm the compiler selects the record marked `is_default: true`, not merely the first array entry. The prompt must include that VPO's ID, coordinate convention, position, Y-X-Z orientation, projection, FOV/scale, framing, and target when present.
4. Confirm source `initial_state` remains separately represented and is not replaced by the default render pose.
5. Confirm OI/MSRM/TD, identities, uncertainty, and negative constraints are preserved. No generator is invoked and no rendered image is claimed.

**Pass:** validation passes; default VPO is selected and fully represented; source initialisation remains distinct; input packet is unchanged.

**Fail:** compiler ignores `is_default`, chooses an arbitrary/first VPO, confuses source initialisation with render pose, invents/alters pose data, skips validation, or invokes a generator.

## Case B — legacy image packet without viewpoint.json

Use an actual older image packet that predates the viewpoint-file requirement. Preserve it unchanged.

1. Run `fv validate [legacy-packet]`.
2. Confirm documented compatibility: virtual `VP-DEFAULT` may represent the implicit source viewpoint in memory. It is not a render VPO and carries no inferred camera geometry.
3. Confirm the rebuild assessment is explicit. Missing `viewpoint.json` alone does not automatically invalidate a legacy packet.
4. Run `fv compile --prompt [same legacy-packet]` only if all independent gates pass and a render VPO is otherwise available/explicitly selected. Do not silently convert `VP-DEFAULT` into a render pose.
5. Confirm unknown source position/orientation remains unknown. Compare input before/after; no `viewpoint.json` may be silently written.

**Pass:** legacy source compatibility is honoured without fabricating a render VPO or source geometry; compilation proceeds only when a render viewpoint and all other gates are satisfied; original files remain unchanged.

**Fail:** missing metadata alone causes rejection despite compatibility, `VP-DEFAULT` is treated as a render pose, a synthetic viewpoint is written, or another failed gate is bypassed.

## Case C — negative reconciliation gate

The repository's `PACKETS/examples/videos/Cat_jumping_backwards/` packet is a negative fixture. Its `dispute.json` says `resolved`, and its historical validation report says `VALID - resolved`; however, `dispute.reconciled.json` still says `ai_reconciliation.validation_after_reconciliation: "to be performed"`.

1. Run `fv validate [packet]` against the current authoritative skill/specification.
2. Run `fv compile --prompt [same packet]`.
3. Confirm the agent identifies pending post-reconciliation validation and blocks prompt production until validation is actually performed and recorded.

**Pass:** compilation is blocked and no generator-ready prompt is emitted.

**Fail:** compilation proceeds based only on stale validation text and `dispute.json`.

## Evidence record

For each case, record case ID and packet hash; FV skill/specification revision; agent/model and date; exact validation and compile result; whether source files changed; whether any generator was invoked (must be no); and pass/fail with reviewer notes.

## Recorded agent-level results (2026-11-12)

- **Case A — PARTIAL:** the Wikimedia image packet selected its separately declared `is_default: true` render VPO and emitted a prompt-only compile artifact. Source viewpoint initialisation remained unknown and distinct. The run's 28/28 local checks were structural/consistency checks, not a full JSON Schema or semantic `fv validate` run. Rebuild assessment and full validation dimensions remain outstanding.
- **Case B — PASS (compatibility gate):** the legacy `blue_chairs` image packet was read without adding `viewpoint.json`; virtual `VP-DEFAULT` was not treated as a render VPO and no camera geometry was inferred. Compilation was correctly not attempted because no render VPO was available.
- **Case C — PASS (negative gate):** prompt production was blocked because post-reconciliation validation remained pending; no generator was invoked and the input packet was unchanged.

Evidence records:
- [Wikimedia media rerun](results/2026-11-12-wikimedia-media-agent-run.md)
- [Case C negative-gate run](results/2026-11-12-case-c-agent-run.md)

The full Wikimedia rerun packet archive (`FV_Wikimedia_Test_2026-11-12-redone.zip`) is retained locally, not committed to the repository. The repository run record documents its hashes, method, outputs, and limitations. Overall acceptance remains **PARTIAL** until Case A's full validation gate is exercised and its evidence is retained. Case C's fixture state alone is not proof that an agent correctly blocks compilation; the separate Case C run record is the evidence for that agent-level result.
