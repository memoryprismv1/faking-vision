# FV operation implementation status

Date: 2026-11-11
Repository baseline: `main`
Working branch: `work/fv-docs-skill-cleanup-20261111`

## Status vocabulary

- **Specified:** the current Working Process Specification and/or agent skill defines the operation and its boundaries.
- **Tool-supported (limited):** repository code implements a bounded part of the operation. This does not imply a general FV runtime or authoritative semantic validation.
- **Experimentally represented:** packet examples, prototypes, or workflows show an intended shape or bounded behavior. They are not proof of a general implementation.
- **Agent acceptance pending:** the operation is specified for an FV-capable agent, but the documented acceptance procedure has not yet been passed with retained agent-run evidence.

The `fv` textarea commands are agent-level operation requests, not standalone shell commands or an installed FV CLI.

## Operation matrix

| Operation | Specification status | Repository implementation/evidence | Boundary / current status |
|---|---|---|---|
| `fv analyse` | Specified | Packet structures, schemas, and example analysis artifacts exist. | No general-purpose analysis executable or automatic visual-analysis engine identified on `main`. Example correctness is deferred to the examples phase. |
| `fv investigate` | Specified | TIR and adaptive temporal-investigation procedures are defined; investigation artifacts exist in examples. | No separate investigation runtime identified. Agent-level execution is not established by the presence of TIR files. |
| `fv assemble` | Specified | Assembly procedure and example packets exist. Separate dataset/assembly workflows exist on divergent branches. | No general-purpose assembly engine identified on current `main`. Divergent workflows are not integrated by this documentation pass. |
| `fv merge` | Specified | Merge rules and example merged packets exist. | No general-purpose packet-merge engine identified on current `main`. Similarity or matching IDs alone are not identity proof. |
| `fv create` | Specified | Packet creation rules and packet schemas exist. | No dedicated packet-generation executable identified. This remains an agent-level operation. |
| `fv rebuild` / `fv upgrade` | Normative v0.27 workflow specified | Command, migration boundaries, report requirements, and post-migration validation are documented. | No packet-migration implementation or agent-level acceptance evidence identified. |
| `fv edit` | Specified | Two client-side browser prototypes exist: the schematic Visual Workbench and the Media Object Editor MVP. | Limited editing prototypes, not a general FV packet editor, authoritative validator, or full reconstruction workbench. Their version selectors/defaults remain v0.25/v0.26-era; neither implements the v0.27 rebuild workflow. |
| `fv edit viewpoint` | Specified; VPO schema and `VPO_DEFAULT` template exist | Browser UI supports VPO creation/editing, import/export, and edit logs. Browser tests cover camera/VPO behavior. | The Visual Workbench text console currently parses viewpoint `set position` and `set orientation` only. The broader command forms are not all implemented in that console. Explicit `VPO_DEFAULT` creation is a UI action, not a defined textarea subcommand. |
| `fv resolve` | Human-resolution and AI-reconciliation lifecycle specified | Dispute records and lifecycle examples exist. | No general-purpose automatic dispute resolver identified. Human decisions must not be fabricated by an agent. |
| `fv validate` | Structural, semantic, evidence, dispute, and rebuild-assessment requirements specified | Limited editor-level checks exist; JSON schemas and schema-validation tests exist for provenance/audit artifacts. | The browser workbench's `fv validate` is an editor-level structural/reference check, not the authoritative full FV semantic validator. Agent-level acceptance remains unverified. |
| `fv compile` | Renderer-neutral compilation and `--prompt` mode specified | Compiled specifications/prompts and an agent-level acceptance procedure exist. | No general renderer adapter or generator integration established. Prompt-compilation agent acceptance is explicitly pending. |
| `fv audit` | Independent packet-to-packet audit and JSON report schema specified | Audit report schema and report contract exist. | No general automated media auditor identified. The batch utility below does not perform audits. |
| `fv audit batch` | Proposed as an agent-level interface; explicitly not a native skill-runtime command | `TOOLS/fv_audit_batch.py`, aggregate schema, nine unit tests, and GitHub Actions workflow exist. | Implemented offline utility validates and aggregates existing reports; it does not re-audit media or rewrite source reports. |

## Browser editor implementations

### FV Edit Visual Workbench

Files:
- `PACKETS/tools/FV_Edit_Visual_Workbench.html`
- `PACKETS/tools/README_FV_Edit_Visual_Workbench.md`
- `PACKETS/tools/fv-editor-smoke-test.mjs`

The workbench is a client-only schematic editor. It provides seven fixtures, environment/object editing, edit logs, JSON bundle import/export, editor-level checks, and a camera/VPO metadata affordance. Its version selector covers v0.25 and v0.26-proposed, not v0.27. Its scene view uses CSS shapes and markers; it is not a source-image renderer. The documented Node smoke test checks syntax, fixtures, IDs/references, bundle round-tripping, stress derivation, negative controls, and UI affordances. It is not the authoritative FV validator or browser end-to-end test.

Its command console currently handles:
- `fv edit viewpoint set <VP-ID> position x y z`
- `fv edit viewpoint set <VP-ID> orientation yaw pitch roll`
- selected general `fv edit` property forms
- editor-level `fv validate`

It does not parse every agent-level viewpoint command listed in `SKILL.md` and `commands.md`.

### FV Media Object Editor MVP

Files:
- `PACKETS/tools/FV_Media_Object_Editor_MVP.html`
- `PACKETS/tools/README_FV_Media_Object_Editor_MVP.md`

The MVP loads user-supplied video or still images, supports manual polygon mask keyframes, interpolates compatible polygons, applies a pixel tint, exports WebM, edits selected packet properties, and edits/exports VPO records. Its import defaults to v0.26 when version metadata is absent and does not implement v0.27 migration. Its still-image perspective output is a planar affine approximation; it does not reconstruct hidden surfaces, depth, parallax, or occlusion. It is not an authoritative FV packet writer or semantic validator. VPO creation is an explicit UI action.

## Automated test inventory

| Test group | Count | What it covers | What it does not prove |
|---|---:|---|---|
| Playwright viewpoint editor | 4 | VPO edits, command-console position update, schematic disclaimer, explicit VPO_DEFAULT instantiation | Full agent-level viewpoint command support or physical 3D rendering |
| Playwright environment workbench | 11 | Environment edits, negative expectation, IDs/references, legacy version preservation, import/export | Authoritative FV semantic validation of arbitrary packets |
| Playwright media object editor | 7 | Video/image editing, masks, property edits, VPO metadata, WebM export, real CCTV integration case | Automatic segmentation/tracking or semantic reconstruction |
| Python audit-batch tests | 9 | Aggregation, duplicate handling, unit profiles, schema output, invalid-report diagnostics, provenance roles | Independent visual/media auditing |
| Python provenance-schema tests | 5 | Optional add-ons and provenance schema constraints | Full packet semantic validation |
| Agent prompt-compilation acceptance | Pending | Default VPO selection, legacy viewpoint compatibility, negative reconciliation gate | No pass may be claimed until actual agent runs and artifacts are retained |

There are 22 Playwright tests and 14 Python unit tests in the inspected files. Test definitions are present; this document does not claim that they were executed or passed during this audit.

## GitHub Actions workflows

- `.github/workflows/fv-environment-workbench-browser.yml`: Playwright Chromium workflow, triggered by relevant pull-request paths or manual dispatch. It prepares a short real CCTV excerpt for the integration test and uploads test results.
- `.github/workflows/fv-audit-batch.yml`: Python schema/unit-test workflow, triggered by pushes to `feature/fv-audit-batch`, relevant pull-request paths, or manual dispatch.

No manual workflow dispatch was performed during this audit. Available commit-run lookup did not provide a complete repository-wide workflow history; CI status is therefore **unverified**, not passed or failed.

## Artifact contract cross-reference

The machine-readable schema and operation-output coverage is audited separately in
`docs/FV_ARTIFACT_CONTRACT_AUDIT_2026-11-11.md`. In particular, the presence
of provenance, viewpoint, and audit schemas does not mean that the full packet,
validation report, TIR, dispute, compile output, or rebuild report has a
dedicated JSON Schema. The viewpoint schema also supports more VPO fields than
the current command syntax exposes.

## Documentation implications

1. Keep the distinction between agent-level commands and repository tools explicit.
2. Do not describe editor-level checks as authoritative `fv validate`.
3. Do not describe the batch processor as `fv audit`; it only validates/aggregates existing audit reports.
4. Do not claim the browser command console supports every viewpoint command form.
5. Treat question-directed analysis of supplied media as part of `fv investigate`; TD temporal queryability remains a packet capability and acceptance requirement, not a separate user-facing command.
6. Example packet review and cleanup is tracked separately from the operation implementation matrix; the subsequent example audit and current evidence status are recorded in `PACKETS/examples/README.md` and `PACKETS/META_EXAMPLES_CATALOG.md`.
