# FV prompt-compilation acceptance procedure

**Status: agent-level acceptance is pending.** These are skill-runtime operations, not executable repository CLI commands. The Playwright tests do not invoke an FV agent and must not be reported as proof that `fv validate` or `fv compile --prompt` executed.

## Acceptance boundary

The test is for packet validation and prompt-only compilation. It does not test image generation, video generation, geometric novel-view synthesis, or visual reconstruction. No generator may be invoked during these tests.

For each run, retain the exact input packet, complete validation report, complete prompt artifact (if produced), and a short run record identifying the FV skill/specification revision and agent/model. Do not overwrite the input packet.

## Case A — unchanged source viewpoint

Use a valid image packet with a root-level `viewpoint.json` whose source viewpoint is unchanged and whose `initial_state` is explicitly represented. Do not create a new render pose or edit the VPO for this case.

1. Run `fv validate [packet]`.
2. Confirm the report separately records structural validity, semantic/evidence consistency, dispute/reconciliation state, rebuild assessment, and compilation readiness.
3. Run `fv compile --prompt [same packet]`.
4. Confirm the prompt preserves the exact source viewpoint identity and initial state. It must not invent a camera pose, coordinate frame, calibration, FOV, or physical geometry where the packet does not contain them.
5. Confirm OI/MSRM/TD content, identities, uncertainty, and negative constraints are preserved. Confirm no generator was invoked and no rendered image is claimed.

**Pass:** validation genuinely passes; compilation produces a prompt-only artifact; the viewpoint remains unchanged; unsupported camera geometry remains unknown; no source packet files are silently edited.

**Fail:** the agent substitutes a default pose, invents camera geometry, changes packet content, skips validation, or invokes a generator.

## Case B — legacy image packet without viewpoint.json

Use an actual older image packet that predates the viewpoint-file requirement. Preserve it unchanged as the test input.

1. Run `fv validate [legacy-packet]`.
2. Confirm the agent applies only the documented legacy compatibility rule: an in-memory virtual `VP-DEFAULT` may represent the implicit viewpoint. It is not evidence of camera geometry and must not be written into the packet just by reading it.
3. Confirm the rebuild assessment is explicit. A legacy packet is not automatically invalid solely because it lacks `viewpoint.json`; whether compilation can proceed depends on all other gates and documented compatibility.
4. If validation and all compilation gates pass, run `fv compile --prompt [same legacy-packet]`.
5. Confirm the prompt identifies `VP-DEFAULT` as a compatibility interpretation, preserves unknown position/orientation, and does not materialize a pose or invent FOV, calibration, or geometry.
6. Compare the input packet before/after. No `viewpoint.json` or other file may be silently added.

**Pass:** the legacy packet is handled through documented compatibility without fabricating source metadata; compile proceeds only if all independent gates pass; original files remain unchanged.

**Fail:** the agent rejects the packet solely for missing viewpoint metadata despite compatibility, writes a synthetic viewpoint record, invents pose data, or bypasses another failed gate.

## Case C — negative reconciliation gate

The repository's `PACKETS/examples/videos/Cat_jumping_backwards/` packet is a deliberate negative fixture for this gate. Its `dispute.json` says `resolved`, and its historical validation report says `VALID - resolved`; however, `dispute.reconciled.json` still says `ai_reconciliation.validation_after_reconciliation: "to be performed"`.

1. Run `fv validate [packet]` against the current authoritative skill/specification.
2. Run `fv compile --prompt [same packet]`.
3. Confirm the agent does not treat the stale validation report and resolved status as sufficient. It must identify the pending post-reconciliation validation and block prompt production until that validation is actually performed and recorded.

**Pass:** compilation is blocked and no generator-ready prompt is emitted.

**Fail:** compilation proceeds based only on the stale validation text and `dispute.json`.

## Evidence record

For each case, record:

- Case ID and exact packet path/hash.
- FV skill commit and specification revision.
- Agent/model identity and date.
- Exact `fv validate` result, including rebuild assessment.
- Exact `fv compile --prompt` result or explicit block reason.
- Whether the source packet changed (diff/hash comparison).
- Whether any image/video generator was invoked (must be no).
- Pass/fail and reviewer notes.

Do not mark Cases A or B passed until actual agent-level runs and their artifacts are attached. Case C is a fail-closed regression check; its repository fixture state alone is not proof that an agent correctly blocks compilation.
