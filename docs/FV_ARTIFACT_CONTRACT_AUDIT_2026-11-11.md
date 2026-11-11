# FV Artifact Contract Audit

Date: 2026-11-11
Baseline: `main`
Working branch: `work/fv-docs-skill-cleanup-20261111`

## Purpose and scope

This audit compares the operation-level artifact requirements in the current Working Process Specification, active skill, command reference, and how-to guide against the machine-readable JSON schemas found in the repository.

This is a contract-coverage review, not a claim that every FV packet layer must have a separate JSON Schema. The specification deliberately defines some packet layers procedurally. Where no dedicated schema was found in the inspected schema references/searches, this report says so rather than inventing one.

## Schema inventory confirmed on the working branch

| Schema | Root shape | Required contract | Used by |
|---|---|---|---|
| `FV_Packet_Provenance_Schema.json` | Object; `additionalProperties: false` | `schema_version`, `packet_id`, `fv_spec_version`, `packet_generator`, `media` | Newly generated packet provenance |
| `FV_Viewpoint_Schema.json` | Array of viewpoint records; at least one item | Each record: `id`, `observer`, `initial_state` | Root-level `viewpoint.json` |
| `FV_Audit_Report_Schema.json` | Object; `additionalProperties: false` | `schema_version`, `audit_id`, `created_at`, `auditor`, `inputs`, `comparison`, `metrics`, `deviations`, `limitations` | `FV_AUDIT_REPORT.json` |
| `FV_Audit_Batch_Report_Schema.json` | Object; `additionalProperties: false` | `schema_version`, `report_type`, source/valid/invalid/duplicate counts, `source_audits`, `profiles`, `deviations`, invalid/duplicate detail arrays, `limitations` | Offline batch aggregation output |

### Provenance schema observations

- The root schema rejects undeclared root properties.
- Packet-generator and media-generator agent records use the same required identity fields, including `generated_at` and `identity_source`; unavailable values are represented as null/unknown where allowed.
- `media` requires media ID, media type, SHA-256 slot, media-generator slot, and embedded-provenance array. Several values may be null when unavailable.
- `attribution`, `organizations`, and `contributions` are optional independent add-ons. The attribution object is deliberately open; organization and contribution entries have narrower contracts.
- Legacy packets may omit the entire provenance file under the stated compatibility rule. Newly generated packets may not omit it.

### Viewpoint schema observations

- The root is a JSON array, not an object wrapper.
- Every record requires `id`, `observer`, and `initial_state`.
- `initial_state.status` is mandatory and distinguishes `known`, `partially_known`, and `unknown`.
- A render pose requires position, orientation, projection, and framing. Orientation requires intrinsic Euler representation, yaw/pitch/roll, degrees, and Y-X-Z rotation order.
- The coordinate frame requires an ID, right-handedness, +Y up axis, and units.
- Perspective FOV and orthographic scale are distinct projection fields. Framing requires aspect ratio and fit.
- The schema permits optional tolerance fields and metadata. It does not itself enforce cross-record uniqueness of IDs or the “at most one default” rule described in prose; those require semantic validation beyond the basic JSON Schema constraints.

### Audit schema observations

- The audit report requires packet-to-packet comparison and explicit packet references with provenance status.
- Each metric requires a code, numerator, denominator, uncertainty count, rate (nullable), and unit definition.
- Deviation records require a taxonomy code, status, description, confidence, and evidence references. The schema allows timestamp/frame, location, packet references, and notes as optional fields.
- The report requires a limitations array. The top-level provenance snapshot is optional.
- The schema's allowed metric codes and deviation classes are finite enums. Producers must use those codes rather than invent near-synonyms.

### Batch schema observations

- The batch report is a separate aggregate artifact, not the output schema for an individual `fv audit`.
- The batch schema is used by the offline aggregation utility. It must not be presented as an independent visual audit schema or as proof that media were re-audited.

## Operation-to-artifact coverage

| Operation | Required/expected artifact in current specification | Dedicated schema found in this review? | Documentation status / gap |
|---|---|---|---|
| `fv analyse` | Packet files: OI, MSRM, and TD for video; root `viewpoint.json`; new-packet `packet_provenance.json`; source/evidence records as applicable | Viewpoint and provenance schemas; no general packet/OI/MSRM/TD schema confirmed in this review | The process specification remains the operational contract for OI/MSRM/TD. Do not imply that the two additive schemas validate the whole packet. |
| `fv investigate` | TIR investigation workspace and supported promotion into authoritative packet records | No dedicated TIR schema confirmed in this review | TIR is procedurally defined. Preserve its provisional status and evidence links; do not claim schema validation unless a schema is supplied. |
| `fv assemble` | Assembled spatial representation with local-view/source relationships, provenance, transforms, registration diagnostics and unresolved conflicts | No dedicated assembly-output schema confirmed in this review | Output is specified procedurally; no single machine-readable assembly artifact schema was confirmed. |
| `fv merge` | Reconciled packet knowledge and identity-normalisation evidence while retaining source packet identities/provenance | No dedicated merge-report schema confirmed in this review | Merge rules are specified, but this review found no dedicated merge-output schema. |
| `fv create` | Complete packet files and ZIP deliverable when file creation/packaging is available | Provenance and viewpoint schemas only | These schemas are additive components, not a complete packet schema. |
| `fv rebuild` / `fv upgrade` | Rebuilt packet copy, migration report, target-version validation | No dedicated rebuild-report schema confirmed in this review | Command documentation specifies outcomes and report content, but no machine-readable migration-report schema was found in the inspected references. |
| `fv edit` | Edited packet state and edit-log provenance | Viewpoint schema applies to viewpoint records; no general edit-log schema confirmed | The viewpoint schema does not validate edit history or all packet changes. |
| `fv resolve` | Dispute record, human resolution, AI reconciliation and validation history | No dedicated dispute schema confirmed in this review | Dispute lifecycle is specified in prose; do not imply JSON Schema validation. |
| `fv validate` | Validation report artifact and rebuild assessment | No dedicated validation-report schema confirmed in this review | The command requires a report artifact, but this review found no dedicated machine-readable report schema. |
| `fv compile` | Lossless renderer specification and/or reconstruction artifact; prompt-only mode produces prompt artifact | No dedicated compile-output schema confirmed in this review | Fidelity and gate requirements are specified, but output serialization remains renderer/environment dependent. |
| `fv audit` | `FV_AUDIT_REPORT.json` | Yes: `FV_Audit_Report_Schema.json` | Explicit schema-backed contract. |
| Batch aggregation utility | `FV_AUDIT_BATCH_REPORT.json` and readable summary | Yes: `FV_Audit_Batch_Report_Schema.json` | Offline reference utility only; not a native skill-runtime command. |

## Concrete command/schema mismatch: viewpoint editing

The command reference exposes these viewpoint forms: set position, orientation, projection, FOV, target; save; set default; reset.

The viewpoint schema also supports coordinate-frame declarations, orthographic scale, framing aspect ratio/fit/center/notes, and tolerances. The command table does not define standard syntax for editing all of those fields. In particular:

- Selecting `orthographic` without a valid `orthographic_scale`, coordinate frame, and framing does not produce a complete schema-valid pose.
- `fov` is the command shorthand for schema field `field_of_view_degrees`; the mapping should remain explicit in implementation.
- The command console prototype currently parses only viewpoint `set position` and `set orientation`, as documented in the implementation-status report.
- The schema itself does not enforce all semantic rules, including uniqueness of viewpoint IDs and at-most-one default. Those remain semantic validation requirements.

The command reference now states this coverage boundary. No unsupported syntax has been invented.

## Missing-schema register

The following are not asserted to be missing from FV as a whole; they are simply not covered by a dedicated schema confirmed in this review:

1. Complete packet / OI / MSRM / TD schemas.
2. TIR schema.
3. Dispute schema.
4. Validation-report schema.
5. Rebuild/migration-report schema.
6. Compile-output schema.
7. Audio transcript schema for `transcript.json`.
8. Assembly and merge report/output schemas.
9. General edit-log schema.

These are design decisions, not automatic requests to create nine new schemas. The process specification may intentionally rely on procedural rules for some artifacts. Any new schema should be justified by a concrete interoperability or validation need and should preserve existing packet compatibility.

## Next review actions

- Decide whether validation and rebuild reports need stable machine-readable schemas or whether the existing procedural contract is sufficient.
- Decide whether the transcript structure needs a formal schema; current rules require timestamped segments and traceability but do not establish a dedicated JSON Schema in this review.
- Decide which additional VPO fields deserve standardized command syntax versus remaining editor-only schema fields.
- Do not add a generic packet schema until its relationship to the existing OI/MSRM/TD structures and legacy compatibility is explicitly settled.
- Keep `fv query` design separate from this artifact audit.
- Keep examples untouched until the final examples phase.


## Follow-up: operator-facing command/artifact alignment

Reviewed the command map and artifact-output sections in `commands.md`, `SKILL.md`, and `HOW_TO_USE.md`.

Corrections made on the working branch:

- Added explicit `fv rebuild` / `fv upgrade` interpretation and artifact requirements to the active skill: preserve the source packet, create a separate rebuilt copy and migration report, and validate the target copy. Keep migration, structural validation, FV semantic validation, dispute/reconciliation readiness, and independent visual audit as separate outcomes.
- Added explicit `fv edit` and `fv edit viewpoint` artifact requirements to the skill. Successful edits retain before/after information and provenance; viewpoint edits preserve source `initial_state`, validate the VPO schema, and do not alter OI/MSRM scene content.
- Expanded the how-to artifact summary to cover all operations in its command map rather than only analyse, validate, compile, and audit.
- Added the batch-audit boundary to the how-to: the offline utility aggregates existing reports and is not a native skill-runtime command.
- Clarified that video packets, like image packets, are packaged as ZIP deliverables when packaging is available.
- Kept the command-interface distinction explicit: these are agent textarea commands, not evidence that a standalone CLI exists.

A parity check confirms that the same 12 command forms are represented in the command reference, skill, and how-to command maps. The extra `fv audit batch` item remains explicitly marked as a non-native/proposed skill interface. `fv query` remains intentionally absent pending its separate design discussion.

This follow-up changes documentation coverage only. It does not add schemas, alter packet semantics, change examples, run tests, or merge the branch.

## Deferred consistency item for the examples phase

The command-reference resolve example uses `D-014` as a dispute identifier. The current specification's typed-identifier convention assigns dispute records the `DSP-` prefix (for example, `DSP-<autogeneratedhash>`). This appears to be an example-level inconsistency. It is deliberately not changed during this pass because examples are reserved for the final cleanup phase. Check all command examples against the typed-ID convention in that phase; do not silently reinterpret legacy IDs.


## Follow-up: operational procedure alignment

A further line-by-line review compared rebuild, dispute resolution, validation, compilation, and independent audit procedures in the canonical specification against the skill and command reference.

Corrections made:

- Expanded `fv resolve` to preserve the original automated observation and uncertainty, keep human resolution separate, inspect cited evidence/snapshots, update OI and PC only where justified, and validate affected records.
- Made the two dispute-file outcomes explicit: archive detailed history as `dispute.reconciled.json` and create a small resolved gate file only after every dispute is reconciled and validation passes; otherwise retain the detailed `dispute.json` with status open.
- Expanded `fv audit` evidence handling: retain generated media for inspection, cite source-media locations and packet records, define metric units/scopes, calculate rates from numerator/denominator, use null for zero denominators, and keep uncertainty separate from pass/fail counts.

The review confirmed that the skill's rebuild assessment and compile gates already cover the five canonical outcomes, including compatibility handling, required-rebuild stop, and indeterminate assessment. No change to those rules was needed.

No packet semantics or schemas were changed. Examples remain untouched; the previously recorded dispute-ID example discrepancy remains deferred. No tests were run and no merge was performed.


## Follow-up: foundational prerequisite in the how-to guide

The active skill already makes current Making Vision V2 a mandatory prerequisite for visual operations and distinguishes promotion from recognition, identity, and packet commitment. The how-to guide did not surface that prerequisite clearly. Added a concise section covering the required reading, the selective-allocation architecture, the distinction between promotion and packet commitment, preservation of supported structure under identity uncertainty, and the status of Making Vision as a working synthesis rather than an established neural theory.

This is a documentation alignment change; no visual operation was performed and no research claim was independently expanded in this pass.
