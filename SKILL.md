---
name: faking-vision
description: Operate Faking Vision (FV) for image and video analysis, visual investigation, spatial assembly, FV packet construction and merge, dispute resolution, reconstruction, packet validation, prompt compilation, temporal investigation, independent reconstruction audit, and the textarea command interface for FV work. Use this skill whenever the user asks to analyse an image/video with FV, create or inspect an FV packet, reconstruct from an FV packet, or audit a reconstruction. The canonical FV Working Process Specification at `SPECIFICATION/FV_Working_Process_Specification.md` is authoritative; do not substitute general computer-vision assumptions for FV procedures.
---

# Faking Vision Agent Skill

## Mandatory Making Vision prerequisite and candidate/promotion gates

Before performing any visual analysis, investigation, assembly, merge, reconstruction, or audit, obtain and read the current canonical Making Vision material:

https://www.memoryprism.com/readings/making-vision-v2

Making Vision V2 retains the central V1 architecture and clarifies several distinctions that matter to FV, especially current sensory information versus persistent knowledge, candidate versus object, promotion versus attention, and learning versus storage. If the V2 material cannot be accessed or read, state that limitation and do not perform visual analysis, investigation, assembly, merge, reconstruction, or audit until the prerequisite is completed. Documentation-only work may continue; do not claim the prerequisite was completed.

Apply the Making Vision processing architecture:

current sensory input → economical/background processing → candidate or perturbation → selective promotion for additional processing → deeper processing → action and/or persistence.

This is an allocation architecture, not a rigid serial vision algorithm. Persistent knowledge, spatial structure, expectations, task relevance, uncertainty, learned relevance, environmental statistics, current needs, physiological/internal state, energy, risk, and anticipated consequences can affect what receives additional processing. Keep those allocation influences distinct from evidence about what is externally present in the source.

Treat Making Vision as a working architectural synthesis, not an established published biological theory. Do not present constructs such as promotion, maplet/local inset, or the unified selective-allocation architecture as established neural mechanisms. When making scientific claims, distinguish independent evidence for component mechanisms from Making Vision's synthesis and testable predictions. Learning (a change in future processing) is not identical to persistence/storage (information retained over time); do not infer one from the other without evidence.

**Promotion is not recognition, identification, object confirmation, or persistence.** Promotion means that a candidate, state, region, or event warrants additional processing. A perturbation or candidate is only a possible allocation trigger; not every noticed change or candidate is promoted. Promotion can precede stable classification, naming, complete identification, or storage. A promoted candidate may remain ambiguous, be rejected after investigation, or be useful for action without being named.

**Keep processing allocation separate from packet commitment.** Do not count every detected region as an object, assign persistent identity, or establish correspondence merely because something was noticed or promoted. Commit an entity, identity, or correspondence to authoritative packet records only when the source evidence supports that decision. Preserve candidates, alternatives, rejected hypotheses, and unresolved identity where appropriate. Promotion itself does not license adding unsupported semantic detail.

Do not discard directly supported visual structure merely because object identity is unknown. Boundaries, free space, relative position, movement, obstacles, and other source-supported structure can be useful before stable object recognition. Record what the source supports and keep semantic uncertainty explicit.

## Viewpoint packet requirement (current specification)

Apply the current authoritative Working Process Specification for viewpoint metadata:
- Image: record viewpoint initialisation in root-level `viewpoint.json`.
- Video: record initialisation in `viewpoint.json` and supported viewpoint transitions over time in TD.
- Do not require same-scene multi-image comparisons, cross-view object matching, shared-scene hypotheses, or correspondence ledgers merely to record viewpoint metadata.
- A continuous observer/camera retains its viewpoint ID while moving; a distinct observer/viewpoint receives a distinct ID when supported by evidence.
- Preserve unknown position/orientation; do not invent coordinates or camera geometry.

This current rule supersedes older v0.24 wording preserved in `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md` that places initial viewpoint state in TD or expands viewpoint metadata into a cross-view visual-field experiment.

# FV textarea command interface

The chat textarea is the FV command line. FV commands are always prefixed
with `fv`.

The command is the user's explicit instruction for which FV operation to
perform. Do not interpret an unprefixed ordinary sentence as an FV command
unless the user clearly asks for FV work.

## Commands

### `fv analyse`

Analyse the attached or otherwise identified raw visual source using the
complete FV procedure.

For an image, create the complete FV packet as actual packet files and
package the packet as a ZIP. The ZIP is the primary deliverable.

For a video, establish temporal structure and create the complete packet as
actual packet files containing OI + MSRM + TD, with TD authoritative for the
temporal record.


For every source frame actually captured or retained as an evidence
observation, perform the applicable FV image-analysis procedure: visual
inventory, candidate generation, entity/component/appearance decision,
identity assessment where temporal context permits, and evidence/packet
promotion where warranted. Sampling selects which frames to acquire; it
does not replace analysis of a selected frame.

When audio is intentionally included in a video packet:
- Preserve the source audio file together with the video identity and
  relevant time alignment under the packet-level `audio/` directory.
- Generate a timestamped `transcript.json` before the initial TIR/TD
  temporal investigation. The transcript is provisional analysis, not
  source-of-truth evidence and not a substitute for the audio file.
- Assess transcription fidelity separately from visual/cross-modal support,
  unresolved content, and timing/context mismatch. A narrated claim may
  refer to an earlier, later, off-screen, or different scene state.
- Use transcript segments as candidate cues for adaptive sampling, including
  to locate possible gaps in TIR/TD before visual confirmation. Update TIR
  with acquired observations; promote claims into TD only when source
  evidence supports them.
- Preserve uncertainty and discrepancies. Do not infer that commentary is
  false, satirical, or untrustworthy merely because it does not match the
  current visual interval. Do not invent unclear words or speaker attribution.

For every newly generated packet, also create the root-level
`packet_provenance.json` and validate it against
`SPECIFICATION/FV_Packet_Provenance_Schema.json`.

The `media` object may also contain these **optional add-ons** when the
relevant information is supplied or reliably available:
- `attribution`: an object for attribution to the original source/creator;
  leave its internal properties open and preserve only supplied information.
- `organizations`: an array of organization objects.
- `contributions`: an array of contributor objects with `username`, `email`,
  `organization`, `timestamp`, and `role`. The role is the contributor's
  role in relation to the current media, not their general job title.
  Optional contributor identifiers/type/notes may be included when known.

These three add-ons are not required fields. Omit any of them when the
information is unavailable; their absence does not affect packet validity or
packet generation. Do not infer missing people, organizations, roles, contact
details, or timestamps. Use null for unavailable values within a contribution
record that is otherwise being recorded. These records describe attribution
and contributions only; licence and rights metadata are not part of the
current implementation. Do not retrofit legacy packets with guessed data.

`fv analyse` is source analysis. Do not use it as a substitute for a
question-driven investigation when the task is to pursue a specified object,
event, relationship, or correspondence across observations.

### `fv investigate`

Investigate a specified object, event, relationship, correspondence, or
question across one or more visual observations or media.

Use TIR as the investigative workspace. Preserve hypotheses, competing
interpretations, rejected hypotheses, sampling decisions, evidence paths,
and unresolved questions there. Promote only source-supported conclusions
into authoritative packet records.

A task objective may alter attention or sampling priority, but it is not
source evidence and cannot supply missing identity, event, motivation, or
temporal facts.

When the investigation includes audio, assess the source audio and transcript
cumulatively in TIR. Keep transcription fidelity distinct from visual
cross-modal support, ambiguity, and timing/context mismatch. Transcript
claims may direct adaptive sampling before visual support is established, but
must not be promoted directly into TD without supporting source observations.

Example:

`fv investigate this person across these CCTV clips`

### `fv assemble`

**Biological grounding — viewpoint-oriented maplet integration**

FV's assembly model follows the biological account of viewpoint-oriented
vision. A moving observer looks in different directions and occupies
different positions/spaces. It therefore acquires multiple local,
viewpoint-dependent representations (maplets) of portions of the same
place. Overlap and shared spatial structure let those maplets be related
and integrated into a more cohesive spatial map that is not limited to
any single viewpoint.

Treat a maplet as a local spatial representation associated with a
particular view/viewpoint, not merely as an arbitrary image crop or file
tile. Its extent, detail, orientation, scale, occlusion, and relation to
the observer/reference frame may differ from other maplets. The task of
`fv assemble` is to establish how these partial representations fit
together and integrate them while retaining their source and viewpoint
relationships.

This is the conceptual grounding, not a claim that maplets are discrete
neural modules or that all generators encode viewpoints in the same way.
Adapt the representation and registration method to the media generator;
do not impose image-specific assumptions on LiDAR, telescope data, or
other media.

**Operationally:**

1. Identify each source piece/local representation, its generator and
   acquisition context where known.
2. Establish the supported viewpoint/reference information, coverage,
   scale/resolution, calibration, pose/orientation, order/time, and
   limitations. Unknown values remain unknown.
3. Inspect overlap, gaps, occlusions, and shared structures. Use only
   source-supported or justified correspondences.
4. Register local representations into a common reference using an
   appropriate domain-specific method. Record transformations,
   assumptions, residuals, and conflicts.
5. Integrate them into a larger cohesive representation appropriate to
   the media, while retaining which source views contribute to each
   region.
6. Preserve unobserved areas, weak correspondences, viewpoint-specific
   evidence, and unresolved conflicts. Do not invent missing content or
   conceal disagreement to make the result look seamless.

A same-generator, same-acquisition-pass set of overlapping outputs is a
useful controlled assembly test. It is not the biological limit of the
operation: viewpoint changes and movement can produce successive
maplets of the same place across different directions and positions.
Record the actual acquisition relationship; do not assume it.

Keep original source media unchanged. Preserve provenance, viewpoint
and reference information, coverage, transformations, and registration
diagnostics. Geometric correspondence needed to place maplets does not
establish persistent object identity.

**Do not confuse assembly with comparison or merge:**

- Separate datasets covering the same field (for example, historical
  and current observations) are independent observations, not pieces
  of one acquisition. Retain separate source packets and derive a
  linked comparison/difference result only after inspecting and
  registering them. A measured difference is not automatically a
  real-world change; inspect registration, viewpoint, scale,
  resolution, illumination, season, sensor, processing, and coverage
  differences.
- `fv assemble` integrates local spatial representations into a
  larger map/view.
- `fv merge` reconciles independently produced FV knowledge and may
  normalize persistent object identity only when evidence supports it.

See the authoritative Working Process Specification, section
**Biological grounding: viewpoint-oriented spatial integration**, for
the full rationale and procedure. The separate historical/current
same-field comparison workflow is a planned companion capability; do
not describe it as already implemented or validated.

Example:

`fv assemble these LiDAR scans`

### `fv merge`

Merge independently produced FV packets or packet-scoped object inventories.

Compare source evidence, temporal continuity, structural properties,
relationships, and preserved visual evidence before establishing normalized
persistent identity. Preserve packet-scoped IDs and provenance throughout
the merge.

Do not assume that equal local IDs mean equal objects. Do not merge merely
because candidates share a category or generic components.

Example:

`fv merge these two adjacent CCTV packets`

### `fv create`

Deliberately create a new FV packet from established FV information or an
explicit specification.

Use this when the requested packet is being constructed rather than derived
directly from a raw source. A reconstruction packet is an example. Existing
packet-generation procedures, including packets derived from supplied
literature or other non-visual material where explicitly supported, remain
subject to FV evidence and uncertainty rules.

`fv create` must not manufacture visual facts or turn external knowledge
into visual evidence.

Example:

`fv create a reconstruction packet from this resolved packet`

### `fv rebuild` (alias: `fv upgrade`)

Upgrade an existing FV packet to the current authoritative specification version, or to the version explicitly supplied with `--to`.

`fv rebuild [packet] [--to <FV-version>]`

This is a version-migration operation, not a content-editing operation.

- Preserve the supplied packet as the migration source and work on a separate rebuilt copy unless the user explicitly requests in-place replacement.
- Inspect packet files, version markers, provenance, schemas, edit history, disputes, and validation reports. An unversioned packet is legacy; do not guess its exact authoring version.
- Map the source structure to the target specification and distinguish mechanical transformations from compatibility handling and changes requiring re-analysis, human input, or `fv edit`.
- Preserve identities, evidence references, scene membership, temporal order, uncertainty, negative constraints, disputes, and original provenance.
- Never invent missing observations, object properties, camera geometry, coordinate frames, environmental conditions, object responses, timestamps, rights claims, or human resolutions to satisfy a newer schema.
- Preserve the historical version claim. Record the new target mapping as a migration event; do not pretend the packet was originally authored under the target version.
- Produce a rebuild report listing the source and target versions, inspected files, transformations, compatibility handling, unresolved items, required follow-up, and post-rebuild validation.
- Run target-version `fv validate` on the rebuilt copy. Report structural validation, FV semantic validation, dispute/reconciliation readiness, and independent visual audit separately.
- Do not resolve disputes or bypass compilation gates. A structurally upgraded packet may still require evidence work, human review, or `fv resolve`.

Outcomes:
- **UPGRADED — VALIDATED:** migration and target-version validation passed; compilation readiness remains a separate decision.
- **UPGRADED — REVIEW REQUIRED:** structural migration completed, but evidence, semantic, dispute, or human-review requirements remain.
- **BLOCKED:** safe migration requires missing source material, a specification decision, or human input.

Use compatibility behaviour only where the target specification defines it. `VPO_DEFAULT` is the canonical render-preset template in `SPECIFICATION/VPO_DEFAULT.json`; instantiate it only for new packet construction or an explicit editor/user action, assigning a generated `VP-<autogeneratedhash>` record ID. Do not silently add it when importing a packet that lacks viewpoint records. The legacy virtual `VP-DEFAULT` is a separate read-time-only source-viewpoint compatibility identity, not a VPO or render preset; it carries no camera geometry and must never be materialized as pose data. Missing environment data alone does not invalidate a legacy packet. Do not invent a version-marker filename/schema while that format remains unspecified; record the target mapping in the rebuild report and flag the gap.

`fv upgrade` is an alias for this same operation, not a separate workflow.

Example:

`fv rebuild [legacy-packet.zip]`

### `fv resolve`

Resolve an FV dispute, ambiguity, correspondence conflict, or competing
interpretation.

Use the existing dispute lifecycle. Where human intervention is required,
the human supplies the resolution information; the AI then reconciles the
packet against the cited evidence and human changes, preserves provenance,
and validates the affected records.

An open or invalid dispute remains a reconstruction gate. Do not merely
change a status field to make compilation possible.

Example:

`fv resolve dispute D-014`

### `fv edit`

Make an intentional, evidence-grounded change to existing packet content. Use the relevant edit operation for object properties, viewpoints, or environmental conditions. Record successful changes and their provenance in the packet's edit log; do not record failed or unresolved operations as successful.

`fv edit` does not perform specification-version migration. Use `fv rebuild` (or its alias `fv upgrade`) to bring a legacy packet into alignment with a newer FV standard. Rebuilding does not replace intentional content edits.

### `fv edit viewpoint`

List and inspect source viewpoint records and reusable render VPOs. The `set`, `save`, `default`, and `reset` operations modify the active/render pose or render-preset state only; preserve source `initial_state` as provenance. Do not treat a source-only viewpoint as an editable render VPO.

Supported operations:
- `fv edit viewpoint list` — list source viewpoints and reusable render presets.
- `fv edit viewpoint show <VP-ID>` — show the full viewpoint definition.
- `fv edit viewpoint set <VP-ID> position x y z` — set camera position in the declared world frame.
- `fv edit viewpoint set <VP-ID> orientation yaw pitch roll` — set intrinsic Y-X-Z camera rotation in degrees.
- `fv edit viewpoint set <VP-ID> projection perspective|orthographic` — set projection.
- `fv edit viewpoint set <VP-ID> fov degrees` — set perspective field of view.
- `fv edit viewpoint set <VP-ID> target x y z` — set the look-at target.
- `fv edit viewpoint save <VP-ID> as <name>` — save a named reusable preset/derived version.
- `fv edit viewpoint default <VP-ID>` — set the packet's default render viewpoint.
- `fv edit viewpoint reset <VP-ID>` — restore the selected preset's saved state.

Every edit must validate against `SPECIFICATION/FV_Viewpoint_Schema.json`, preserve the source `initial_state`, record before/after values and provenance in the edit log, and leave OI/MSRM scene content unchanged. The command and browser editor must produce equivalent packet state. A 2D source image alone does not provide arbitrary 3D geometry; report unsupported or approximate renders instead of claiming exact camera movement.

`VPO_DEFAULT` may be instantiated only through an explicit packet-creation or editor action. The current textarea command list does not define an instantiation subcommand or syntax. Do not invent one; use an explicitly available editor action or request clarification. If interacting with the current Visual Workbench text console, use only its implemented viewpoint `set position` and `set orientation` forms; other VPO fields are exposed through browser UI controls, not that console.

Example:

`fv edit viewpoint set VP-AB12CD34 position 2 1 4`

### `fv validate`

Validate the identified FV packet against the current authoritative Working Process Specification and the packet's declared version/compatibility rules.

Validation is not reconstruction and is not an independent reconstruction
audit.

Report structural problems, missing required fields, contradictions,
inventory problems, unresolved disputes, and reconciliation state as
applicable.

Do not silently repair the packet. If repair is required, identify what must
be reprocessed or changed.

When audio is included, also verify that the audio file and `transcript.json`
are present, source-aligned, and mutually traceable, and that TIR records the
provisional transcript assessment and material discrepancies. Keep audio
evidence and visual evidence as separate traceable streams.

Also assess whether the packet may require migration to the current FV specification version. Include an explicit rebuild assessment in the validation report: **REBUILD NOT INDICATED**, **REBUILD MAY BE NEEDED**, **REBUILD RECOMMENDED**, **REBUILD REQUIRED**, or **ASSESSMENT INDETERMINATE**. Give the reason, affected records/rules, and next step. A legacy packet may remain valid under documented compatibility rules while still receiving a rebuild warning. Do not rebuild, rewrite version claims, or materialize compatibility placeholders during validation.

Example:

`fv validate`

### `fv compile`

Compile a **resolved and validated** FV packet. By default, compile the packet
into a reconstruction specification and perform reconstruction when the
required renderer/generator is available.

Compilation is a fidelity boundary. It may translate packet content into
renderer-specific syntax but may not add semantic content, world knowledge,
props, motivations, genre conventions, or other undeclared information.

Before compilation, verify the packet validation result and the current
`dispute.json` rendering gate. If the packet is invalid, reconciliation is
incomplete, or `dispute.json` is open, missing, malformed, or inconsistent,
stop and return the packet to the appropriate earlier operation.

Compilation never resolves disputes.

Compilation must also report the packet's rebuild assessment, using the same five outcomes as `fv validate`. If rebuild is **MAY BE NEEDED** or **RECOMMENDED**, compilation may proceed only when the packet independently passes all compilation gates and the target specification explicitly permits its legacy compatibility path; warn that no rebuild occurred. If rebuild is **REQUIRED**, stop before producing renderer instructions or a prompt and direct the operator to `fv rebuild` / `fv upgrade`, then `fv validate`, then retry. If assessment is **INDETERMINATE**, do not imply that the packet is current; stop if the uncertainty affects a required compilation rule, otherwise state the warning and compatibility boundary. Compilation never runs rebuild automatically.

If the available environment cannot perform the actual rendering, produce
the lossless compiled renderer specification rather than pretending that
rendering occurred. This fallback applies to default compilation; prompt-only
mode below always stops after producing the prompt artifact.

#### Prompt-only output mode

`fv compile --prompt [attached-packet.zip]` requests **only a compiled prompt
artifact** from the supplied FV packet. The ZIP is the input packet, not an
instruction to render it.

In this mode:

- Apply the same validation, reconciliation, and `dispute.json` gates as
  ordinary compilation. Do not emit a generator-ready prompt for a packet
  that fails those gates.
- Produce a lossless, generator-ready prompt/specification artifact using the
  packet-to-renderer compilation rules below.
- Preserve packet identities, closed object and background inventories,
  scene membership, off-screen persistence, spatial relations, temporal order,
  transitions, uncertainty, and explicit negative constraints.
- Resolve the active render viewpoint from root-level `viewpoint.json` (or
  the packet's canonical viewpoint field). If no VPO is explicitly selected and exactly one record has `is_default: true`, select that default render VPO; do not select the first array entry arbitrarily. If no default is declared and no VPO is explicitly selected, report that no render viewpoint is selected rather than inventing one. A default render VPO is distinct from the source observer's `initial_state` and does not rewrite or imply source-camera geometry. The legacy virtual `VP-DEFAULT` compatibility identity represents only an implicit source viewpoint; it is not a substitute for a render VPO. Include the selected VPO ID, declared
  coordinate-frame ID/convention/units, camera position, intrinsic Y-X-Z
  yaw/pitch/roll in degrees, projection, FOV or orthographic scale, target when
  present, aspect ratio, and framing. Do not substitute source `initial_state`
  for the selected render `pose`.
- State explicitly whether the target renderer can honour the requested camera
  pose. If geometry/depth is insufficient for a physical viewpoint change from
  a 2D source, mark the view as approximate/unsupported and identify the
  missing information; never imply that prompt compilation itself generated
  the image.
- Keep packet facts distinct from renderer-specific syntax and capability
  limitations. Do not add undeclared semantic content to make the prompt sound
  natural.
- **Do not invoke an image or video generator, render, or claim that a
  reconstruction occurred.** The operation ends when the prompt artifact is
  produced.

The prompt-only mode changes the output requested from compilation; it does
not relax the compilation fidelity boundary or validation gates. It does not
change the default behaviour of `fv compile`.

If the available environment cannot create a file, return the complete prompt
artifact as output and state that it was not saved as a file. Do not invent an
artifact path.

Examples:

`fv compile`

`fv compile this packet as a video`

`fv compile --prompt [attached-packet.zip]`

### `fv audit`

Independently audit a reconstruction by comparing the original/expected FV
packet with a separate FV packet produced by analysing the generated media.
The generated-media analysis must inspect the media independently; do not use
the expected packet as evidence for what is visible in the generated media.

Keep three identities distinct: media generator, generated-media packet
generator (analyst), and auditor. Use `packet_provenance.json` when present;
legacy packets without it remain usable and have unknown provenance.

Do not use the reconstruction generator's explanation as evidence. Do not
rewrite either packet during audit.

Classify deviations using the FV failure taxonomy, including inventory,
identity, spatial, temporal, behaviour, style, unsupported-detail, and
evaluator-uncertainty classes. Record evidence references and category-specific
counts, denominators, uncertainty, and rates.

`fv audit` MUST create a downloadable `FV_AUDIT_REPORT.json` when file
creation is available. The JSON report is the primary artifact; a readable
summary is supplementary. Validate it against
`SPECIFICATION/FV_Audit_Report_Schema.json`.

Example:

`fv audit [expected-packet.zip] [generated-media-packet.zip] [generated-media]`

**Batch audit:** a reference offline processor is provided at
`TOOLS/fv_audit_batch.py`. It validates existing JSON reports and writes an
aggregate JSON report plus a readable summary; it does not re-audit media or
rewrite source reports. See `SPECIFICATION/FV_Provenance_And_Audit.md` for
installation, invocation, duplicate handling, profile boundaries, and tests.
The skill-level `fv audit batch` command remains a proposed interface until
the skill runtime can invoke the utility with attached files.

## Command interpretation rules

- `fv analyse` means raw source → FV analysis/packet.
- `fv investigate` means specified visual question/object/event → investigative evidence path.
- `fv assemble` means partial/overlapping observations → registered/assembled representation.
- `fv merge` means independent FV packets → reconciled packet/object inventory with provenance preserved.
- `fv create` means established information/specification → newly constructed FV packet.
- `fv rebuild` / `fv upgrade` means an existing packet → separate migrated copy, migration report, and target-version validation; it does not edit source content or resolve disputes.
- `fv edit` means an intentional packet-content change with before/after values and provenance.
- `fv edit viewpoint` means inspect source viewpoints/render VPOs or edit the render pose without rewriting source `initial_state`.
- `fv resolve` means open dispute/ambiguity → reconciled or still-unresolved packet.
- `fv validate` means packet → validation report.
- `fv compile` means resolved + validated packet → lossless renderer specification and, where supported, reconstruction.
- `fv audit` means expected FV packet + independently analysed generated-media packet → independent packet-to-packet evaluation and downloadable JSON audit report.
- `fv audit batch` is not a native skill-runtime command. The offline reference processor is `TOOLS/fv_audit_batch.py`; it validates and aggregates existing JSON reports when invoked with attached files. Do not claim the skill command itself is implemented.
- Keep these boundaries separate. Do not silently combine operations.
- A command may be followed by natural-language constraints or objectives;
  those modify the requested operation but do not change FV evidence rules.

## Artifact output contract

FV work products are files. The chat response is not the work product when
the requested FV operation calls for an artifact.

- `fv analyse` MUST create the packet files and, when file packaging is
  available, package them as a ZIP. Return the ZIP as the primary result.
- `fv investigate` MUST create the investigation artifact/report when the
  operation produces a persistent investigation result.
- `fv assemble` MUST create the assembled/registered representation and
  preserve the source provenance and unresolved registration information.
- `fv merge` MUST create the merged packet/object inventory with provenance
  and correspondence decisions preserved.
- `fv create` MUST create the requested FV packet as actual packet files when
  the environment supports file creation.
- `fv resolve` MUST preserve the dispute/resolution record and the
  reconciled packet state as artifacts when applicable.
- `fv validate` MUST create a validation report artifact when file creation
  is available.
- `fv compile` MUST create the compiled renderer specification and/or
  reconstruction artifact available to the environment.
- `fv audit` MUST create a downloadable JSON audit report when file
  creation is available; the JSON is primary and the human-readable summary is
  supplementary.

The offline `fv_audit_batch.py` utility produces a separate aggregate JSON
report and readable summary. It is not a native skill command and does not
re-audit media. Do not claim that `fv audit batch` is implemented.
- Human-readable chat summaries are supplementary.
- Never replace an artifact with a prose dump of the artifact's intended
  contents.
- Never pretend that a file was created when the environment could not
  create it; report the actual limitation.
- Use stable filenames. Do not append specification versions, dates,
  `final`, or similar suffixes unless the user explicitly requests a
  separate artifact. Version information belongs in document content,
  metadata, or version control.

- If the necessary source, packet, or reconstruction is not present, identify
  the missing input rather than inventing it.
- Do not invent filesystem paths, executable commands, repository layouts, or
  renderer capabilities merely because an FV command was entered.
- The textarea command interface is an agent interaction convention, not a
  claim that an FV executable or CLI has been implemented.
- Filenames should remain stable. Do not append FV specification versions,
  dates, `final`, or similar suffixes to filenames unless the user explicitly
  requests a separate artifact. Version information belongs in document
  content, metadata, or version control.

## Command chaining

Commands may be issued in separate turns. The normal downstream path is:

`fv analyse / fv investigate / fv assemble / fv merge / fv create`

then, when required:

`fv resolve`

then:

`fv validate`

then:

`fv compile`

then:

`fv audit`

Not every operation is required for every job. In particular:

- `assemble` is for putting partial or overlapping observations together;
- `merge` is for reconciling independently produced FV knowledge;
- `create` is for deliberately constructing a packet from established
  information or an explicit specification;
- `resolve` is required when a dispute or ambiguity blocks downstream work;
- `compile` requires a resolved, validated packet and never performs
  resolution or repair.

When the relevant packet or reconstruction already exists in the current
working context, do not make the user re-import the FV specification merely
to continue the chain.


## Operating rule

This skill contains the agent-facing operating instructions and textarea command/output contract. When used with the repository, read and apply `SPECIFICATION/FV_Working_Process_Specification.md`; the user should not need to supply that file separately. When the repository file is unavailable, state that the complete current specification cannot be consulted. Do not treat the embedded historical v0.24 snapshot as a substitute for the current specification. Packet provenance and JSON audit requirements are additionally defined in `SPECIFICATION/FV_Provenance_And_Audit.md` and their JSON schemas. The separately preserved historical v0.24 snapshot is reference material only and must not override current instructions.

The source hierarchy is: `SPECIFICATION/FV_Working_Process_Specification.md` is authoritative for FV packet structure, operations, evidence rules, and reconstruction gates. The canonical Making Vision material is the foundational perceptual source that this skill operationalizes; its required reading and the candidate-promotion gate are skill prerequisites, not replacements for FV packet rules. This skill may provide agent-facing procedures and guardrails grounded in Making Vision, but it must not contradict the Working Process Specification or silently redefine its packet requirements.

When operating FV:
- preserve FV terminology and distinctions;
- observe before naming;
- do not turn plausibility into evidence;
- keep observation, interpretation, and packet commitment distinct;
- preserve uncertainty;
- never invent semantic content to make a reconstruction more plausible;
- treat the packet as the reconstruction source of truth;
- independently audit generated results rather than trusting generator explanations;
- when the source material does not support a conclusion, preserve the uncertainty or dispute rather than filling the gap from world knowledge.

## Historical v0.24 specification snapshot — reference only

The historical v0.24 extraction is preserved in `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md` for provenance and historical comparison. It is not current operating authority. Apply the current `SPECIFICATION/FV_Working_Process_Specification.md` and active instructions above whenever wording differs.

## Canonical specification

The complete authoritative FV rules, including the agent-facing analysis
requirements and environmental participation rules, are maintained in
`SPECIFICATION/FV_Working_Process_Specification.md`.

This skill is the operational interface for applying those rules. It must not
be treated as a separate source of policy: if a procedure or rule appears to
conflict with the canonical specification, follow the canonical specification
and flag the discrepancy for correction. Do not invent additional FV
requirements that are not documented there.
