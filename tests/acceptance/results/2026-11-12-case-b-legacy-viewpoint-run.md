# Case B — legacy viewpoint compatibility acceptance

Date: 2026-11-12  
Branch: `work/fv-docs-skill-cleanup-20261111`  
Execution: agent-level FV skill operation; no standalone CLI.

## Input

`examples/images/blue_chairs/`

- Legacy image packet with OI/MSRM and source image.
- Packet README now explicitly declares `DISPUTES: NONE`.
- No root-level `viewpoint.json` or `packet_provenance.json` exists.
- No source camera pose, orientation or calibration is recorded.

## Operation and result

- **Legacy read compatibility: PASS.** The implicit `VP-DEFAULT` compatibility identity may represent the legacy source viewpoint at read time only.
- **No invented geometry: PASS.** No camera pose or calibration was inferred or written.
- **No synthetic viewpoint file: PASS.** The packet remained unchanged; no `viewpoint.json` was created.
- **Render-VPO gate: BLOCKED as expected.** `VP-DEFAULT` is not a render VPO. No separate render VPO is available or selected, so prompt compilation was not attempted.
- **Dispute gate: CLEAR.** The explicit `DISPUTES: NONE` declaration means the compatibility test is not confounded by a missing dispute-state declaration.
- Generator invoked: No.

## Acceptance

**PASS for Case B.** The legacy source viewpoint is read compatibly without fabricating source-camera geometry. Compilation is correctly withheld because a render VPO is absent. This is a bounded agent-level compatibility test, not evidence of a standalone FV CLI.
