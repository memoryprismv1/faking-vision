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
| `fv investigate` | TIR investigation workspace and evidence-supported packet commitment | No dedicated TIR schema confirmed in this review | TIR is procedurally defined. Preserve its provisional status and evidence links; do not claim schema validation unless a schema is supplied. |
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
- Treat question-directed analysis of supplied media as part of `fv investigate`; TD temporal queryability remains a packet capability and acceptance requirement, not a separate command.
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

A parity check confirms that the same 12 command forms are represented in the command reference, skill, and how-to command maps. The extra `fv audit batch` item remains explicitly marked as a non-native/proposed skill interface. Question-directed analysis of supplied media is included in `fv investigate`; there is no separate `fv query` command.

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


## Follow-up: rebuild target-version ambiguity

The canonical specification header states that the document has a v0.24 base with later normative additions, including v0.26 and v0.27, but does not declare a separately consolidated release number. The rebuild command's default-target wording could otherwise tempt an agent to treat the latest labelled addition as the consolidated target.

The skill and command reference now explicitly prohibit that inference. If no target is supplied and no single authoritative target label is designated, the agent must report the target as unresolved and request a version decision or mark migration blocked. This preserves the existing version-designation decision rather than silently deciding it during documentation cleanup.


## Correction: implicit-current rebuild target

A subsequent cross-file consistency check found that the previous follow-up's instruction to block or defer rebuild when no consolidated release label exists was stricter than the normative v0.27 rebuild text. That text explicitly says that, when `--to` is omitted, the current authoritative FV specification is the target.

The skill, command reference, and how-to guide now follow that rule: use the current authoritative Working Process Specification itself as the target, and describe it in the migration report as a v0.24 base with later normative additions (including v0.26 and v0.27), without inventing a consolidated release number. The missing consolidated label remains an open versioning/documentation decision, but does not by itself block migration to the current authoritative specification.

This correction supersedes the earlier sentence in this audit's "rebuild target-version ambiguity" follow-up that directed the agent to request a version decision or mark migration blocked solely because no consolidated release label was assigned.


## Follow-up: distinguish object promotion from packet commitment

A terminology collision remained between Making Vision's **promotion** (allocation of additional processing effort) and older FV wording such as "packet promotion" or "promote conclusions into TD" (committing evidence-supported information to authoritative packet records).

The current Working Process Specification, active skill, command reference, and how-to guide now distinguish these operations:

- **Candidate/object promotion:** selective allocation for additional inspection or analysis. It changes processing priority, not evidential certainty or packet status.
- **Packet commitment:** recording a source-supported conclusion in authoritative packet structures such as OI or TD. It requires evidence and is not implied by noticing or promoting a candidate.

Renamed the specification's Pass 5 heading to "packet commitment", added the distinction at that boundary, and updated agent-facing and operator-facing language. At that point, remaining uses of "promote" referred to selective processing or historical change-log wording, rather than packet commitment. A subsequent terminology pass tightened this further: candidate strengthening/rejection is now described as an outcome of inspection, and temporal tracking as an allocation of tracking effort. Reserve "promotion" for allocating additional processing attention; do not use it as a synonym for candidate verification, evidential strengthening, tracking status, or packet commitment.


## Verification: historical specification material was relocated, not discarded

The active `SKILL.md` is substantially shorter than the original `main` version because the embedded v0.24 specification extraction was separated from the agent-facing operating instructions. This was checked rather than assumed:

- Original `main` skill: 1,590 lines.
- Working-branch skill: 622 lines.
- Working-branch `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md`: 1,043 lines.
- The historical file's extracted specification body matches the corresponding v0.24 body formerly embedded in `main`'s skill through 98,484 characters; the remaining difference is the old skill's appended canonical-specification material, now represented by the current standalone Working Process Specification and agent-facing instructions.

The detailed historical v0.24 dispute lifecycle, typed identifiers, viewpoint rules, and other historical material remain available in the dedicated historical file. The current specification remains the operating authority. The line-count reduction is therefore a relocation/separation, not evidence that the research and historical specification were deleted.


The how-to image-analysis pipeline and the skill's per-frame procedure were also updated to make the sequence operationally visible: candidate generation → selective promotion for additional processing where warranted → candidate verification/alternative search → evidence-grounded packet commitment. Promotion remains selective and does not itself establish an object identity or packet fact.


## Follow-up: tighten selective-allocation terminology and section structure

A further contextual review found two remaining clarity issues:

- The operation-to-artifact matrix described investigation as supporting "promotion into authoritative packet records". This was corrected to **evidence-supported packet commitment**.
- The specification's component-driven candidature subsection heading appeared after the material it governed. The heading was moved before the subsection content.

The specification now reserves **promotion** for allocating additional processing attention. Candidate verification describes what inspection establishes (strengthened, weakened, rejected, or unresolved); temporal tracking is described as allocating tracking effort; packet records receive source-supported conclusions through packet commitment. The skill's per-frame procedure and the how-to image-analysis path make the sequence explicit: candidate generation → selective promotion where warranted → component/relationship verification and alternative search → classification/identity decisions where supported → packet commitment.

No examples were changed. No tests were run and no merge was performed.


## Follow-up: v0.25 edit-interface provenance and version-history gap

Reviewed merged PR #1 ("Document image packet editing and environmental participation") and its v0.25 design addition. The original agent interaction forms are:

- `fv edit` — list available objects;
- `fv edit <object-name/object-id> --list` — list the selected object's properties;
- `fv edit <object-name/object-id> <property-id>` — identify a direct property edit, with generic value-assignment syntax left unspecified.

These forms remain in the how-to guide and are now also stated in the current operation model, command reference, and active skill. They are agent interaction conventions, not evidence of a standalone CLI. The Visual Workbench prototype has its own limited value-entry syntax; that does not standardize the general FV command language.

The merged v0.25 design also described an environment record, edit-base distinctions, and a proposed version-marker file. The current v0.26 normative addition refines environmental response representation and edit-log fields; v0.27 explicitly keeps version-marker filename/schema unspecified and separates migration (`fv rebuild`) from content editing. The Visual Workbench's `edit_base` field remains part of its constrained MVP interchange format, not a general FV packet schema.

The current Working Process Specification's v0.26 heading says it builds on v0.25, but no standalone v0.25 section remains. This is now treated as a documentation-status clarification rather than a missing normative section: the core image-edit interaction forms are present in the current command model, while the early environmental/edit-log/version-marker proposals were refined or superseded by v0.26 and v0.27. No separate v0.25 normative block will be reconstructed from the early proposal.


The canonical operation model and downstream path now include `fv rebuild` / `fv upgrade` as an optional migration stage before dispute resolution, validation, and compilation. This aligns the specification's operation sequence with the skill, command reference, and how-to guide. Rebuild remains conditional and does not replace content editing or dispute resolution.


The authoritative v0.27 rebuild rule now carries the same target-label clarification: when the current Working Process Specification is the default target, the report describes its v0.24 base and later normative additions and records that the consolidated release label is unassigned. The agent must not invent a version number or treat v0.27 alone as the consolidated version.


## Follow-up: research foundations integration check

The branch contains `docs/FV_RESEARCH_FOUNDATIONS.md`, a research-to-design reference covering change detection/visual sampling, border ownership and figure-ground organisation, component/shape cues, shadows, biological motion, scale calibration, and sensory-regime change as a separately labelled working hypothesis. It distinguishes empirical findings, theories/models, FV design translations, and hypotheses, and explicitly states what the research does not establish.

The active skill and how-to guide both require the research reference alongside Making Vision V2 before visual operations; the README links it. The source hierarchy is explicit: the research document motivates and bounds FV design choices but does not override the Working Process Specification. Selected recent and comparative references were checked against their publication records; the 2026 shape-cue study and the 2025-online/2026-issue visual-sampling study are correctly dated and their DOI/title details match. No new biological-mechanism claim was added.


The active skill and how-to guide now state the failure model directly: the target is a coherent but wrong scene model, not merely a wrong object label. The failure list includes missed/merged entities, lost components, boundary errors, overlooked low-salience changes, appearance/identity confusion, uncalibrated scale inference, and plausible interpretations silently converted into observations. The operational consequence is explicit: fluency and naming are not evidence of coverage; preserve structure, alternatives, uncertainty, temporal evidence, calibration, and observation/inference/packet-commitment boundaries.


## Examples phase — dispute-gate normalization (2026-11-12)

The example corpus contains 15 packet-level `dispute.json` files. A branch-wide structural pass confirmed that all 15 now use canonical aggregate `status` values (`none`, `open`, or `resolved`) and that every individual dispute record has a `resolution_status` field. The three CCTV Snapshot TD packets were normalized where they used custom aggregate values (`deferred_nonblocking_for_this_chunk`, `open_active_investigations`, and `open_active_temporal_investigations`) or stored per-dispute state under a generic `status` field.

The Making Vision chunk-level attention decision is now kept separate from dispute resolution. `operational_disposition: DEFERRED` means the question need not receive current chunk-local attention; it does not mean the underlying dispute is resolved. Deferred items retain `resolution_status: OPEN`, so the canonical aggregate status remains `open` and the rendering/compilation gate remains blocked. No new aggregate dispute status was added to the specification.

This is a structural/contract normalization of example records and documentation. It does not certify semantic completeness, source coverage, cross-chunk identity, or reconstruction readiness for these examples.

The three CCTV Snapshot TD packets are also explicitly marked as legacy v0.24 records without current root-level `viewpoint.json` and `packet_provenance.json`. The packet READMEs now preserve those omissions as unknowns and prohibit synthesizing camera geometry or source provenance. This is a compatibility/documentation boundary, not a migration or validation claim.

The legacy `Cat_jumping_backwards` example is also clarified as a negative gate fixture: `dispute.json` says `resolved`, but `dispute.reconciled.json` still records `validation_after_reconciliation: to be performed`. The post-resolution report now records this canonical gate inconsistency as FAIL and keeps rendering/compilation BLOCKED. Human permission to compile metadata-only output does not bypass required post-reconciliation validation. The packet itself was not rewritten, preserving the acceptance fixture.


## Examples phase — explicit no-dispute and legacy packet boundaries (2026-11-12)

The five legacy image examples and three authored video-target folders now declare `DISPUTES: NONE` in their packet READMEs. Their missing current root-level viewpoint/provenance records are explicitly documented; no source-camera geometry or provenance is synthesized. The `blue_chairs` Case B fixture is now dispute-clear, so the expected compile block is specifically the absence of a render VPO, not an ambiguous dispute state.

The seven environmental edit-pair folders now each have a packet-level README. Six declare `DISPUTES: NONE`; the rainy Wall Cat edit declares `DISPUTES: OPEN` and remains blocked pending source-image review. These folders remain metadata-only because source binaries and licence/source-page evidence are withheld; their legacy `source_provenance.json` is not a substitute for the current packet-provenance schema, and no root-level viewpoint record is present.
