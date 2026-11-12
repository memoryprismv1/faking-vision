# FV operation implementation status

Date: 2026-11-12
Repository baseline: `main`
Working branch: `work/fv-docs-skill-cleanup-20261111`

## Status vocabulary

- **Specified:** the current Working Process Specification and/or agent skill defines the operation and its boundaries.
- **Tool-supported (limited):** repository code implements a bounded part of the operation. This does not imply a general FV runtime or authoritative semantic validation.
- **Experimentally represented:** packet examples, prototypes, or workflows show an intended shape or bounded behavior. They are not proof of a general implementation.
- **Agent acceptance partial:** one or more defined agent-level acceptance cases have been exercised, but the complete acceptance gate or required evidence remains outstanding.

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
| `fv validate` | Structural, semantic, evidence, dispute, and rebuild-assessment requirements specified | Limited editor-level checks exist; JSON schemas and schema-validation tests exist for provenance/audit artifacts. | The browser workbench's `fv validate` is an editor-level structural/reference check, not the authoritative full FV semantic validator. Agent-level validation was exercised in the Wikimedia prompt-compilation run and the negative reconciliation-gate run; full semantic/evidence/dispute validation and a separately recorded rebuild assessment remain unverified. |
| `fv compile` | Renderer-neutral compilation and `--prompt` mode specified | Compiled specifications/prompts and an agent-level acceptance procedure exist. | No general renderer adapter or generator integration established. Agent-level prompt-only acceptance is partial: Case A demonstrated default-render-VPO selection and prompt output but did not complete the full validation gate; Case B legacy compatibility and Case C negative-gate enforcement passed their defined checks. |
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
| Playwright prompt-only fixture checks | 2 | Golden prompt content and legacy Cat-packet reconciliation gate fixture assertions | Execution of an agent-level compiler or proof that the agent enforces the compile gate |
| Python audit-batch tests | 9 | Aggregation, duplicate handling, unit profiles, schema output, invalid-report diagnostics, provenance roles | Independent visual/media auditing |
| Python provenance-schema tests | 5 | Optional add-ons and provenance schema constraints | Full packet semantic validation |
| Agent prompt-compilation acceptance | Partial: 3 defined cases exercised | Case A default VPO selection/prompt output; Case B legacy viewpoint compatibility; Case C negative reconciliation gate | Case A remains partial because full validation/rebuild assessment was not executed. Local structural checks are not full schema or semantic validation. See acceptance run records |

There are 24 Playwright tests across the four browser spec files (including two prompt-only fixture checks), and 14 Python unit tests in the inspected files. The two prompt-only tests are fixture/contract assertions; they do not execute the agent-level compiler or establish its acceptance. Test definitions are present; this document does not claim that they were executed or passed during this audit.

## Agent-level prompt-compilation acceptance (2026-11-12)

- **Case A — PARTIAL:** Wikimedia image packet default render VPO selected correctly and a prompt-only compile artifact was produced. Source viewpoint initialisation remained separately unknown. The run passed 28 local structural/consistency checks, but did not execute the full validation dimensions or a separately recorded rebuild assessment.
- **Case B — PASS (compatibility gate):** legacy `blue_chairs` packet remained unchanged; virtual `VP-DEFAULT` was treated only as a read-time source-viewpoint compatibility identity, not a render VPO. No camera geometry or synthetic `viewpoint.json` was added; compilation was not attempted without a render VPO.
- **Case C — PASS (negative gate):** prompt compilation was blocked because post-reconciliation validation remained pending. No generator was invoked and the packet was unchanged.
- The complete Wikimedia rerun packet archive is retained locally as `FV_Wikimedia_Test_2026-11-12-redone.zip`; its repository-side run record documents source hashes, method, artifacts and limitations. The archive itself is not committed.
- Overall prompt-compilation acceptance remains **PARTIAL** until Case A's full validation gate and evidence are completed.

Evidence:
- [Wikimedia media rerun](../tests/acceptance/results/2026-11-12-wikimedia-media-agent-run.md)
- [Case C negative-gate run](../tests/acceptance/results/2026-11-12-case-c-agent-run.md)
- [Acceptance procedure](../tests/acceptance/prompt-compilation-agent-acceptance.md)

## GitHub Actions workflows and observed CI evidence

- `.github/workflows/fv-environment-workbench-browser.yml`: Playwright Chromium workflow. It prepares a short real CCTV excerpt, lists discovered tests, runs the browser suite, and uploads test results.
- `.github/workflows/fv-audit-batch.yml`: Python schema/unit-test workflow. It installs dependencies, runs unittest discovery, and checks Python syntax.

Observed runs on this working branch:

| Suite | Run | Tested commit | Result | Evidence |
|---|---:|---|---|---|
| Python provenance/audit | 43191452973 | `3a97b2e13799101c78c66a4da89f8379f7d9f751` | **14 tests passed**; syntax check passed | [GitHub Actions](https://github.com/memoryprismv1/faking-vision/actions/runs/43191452973) |
| Playwright Chromium | 43196216581 | `c504e4e129a7ffff972e03d4cc47025d0cbf7ad0` | **24 tests passed**, including real Wikimedia CCTV integration | [GitHub Actions](https://github.com/memoryprismv1/faking-vision/actions/runs/43196216581) |
| Python provenance/audit | 43203495982 | `048eb1001cfc491315de4e82e7185ccf8baa8b7a` | **14 tests passed**; syntax check passed | [GitHub Actions](https://github.com/memoryprismv1/faking-vision/actions/runs/43203495982) |

These are successful suite runs on the listed commits, not one combined run on a single commit. The latest Python run verifies the Python suite at `048eb10`; the browser suite has not yet been rerun at that exact commit. The two prompt-only browser tests are fixture/contract checks and do not constitute agent-level `fv compile` acceptance.

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
