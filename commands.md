# FV command reference

This document describes the Faking Vision (FV) commands, their inputs, outputs, and operating boundaries.

**These are AI-agent textarea commands, not a standalone command-line program.** Issue them in the conversation or interface where the FV agent skill is available. The command selects the FV operation; ordinary language can supply the task, target, constraints, and attached files. Examples below illustrate requests and should not be read as a promise that every command has a rigid positional-argument parser.

The authoritative rules are in [the FV Working Process Specification](SPECIFICATION/FV_Working_Process_Specification.md). The [agent skill](SKILL.md) supplies the agent-facing procedure. This reference is an index to those procedures, not a replacement for them.

## Command map

| Command | Use it for | Main result |
|---|---|---|
| `fv analyse` | Analyse a raw image or video source | FV analysis packet |
| `fv investigate` | Investigate an object, event, relationship, correspondence, or question in supplied media, including what happened and when | Evidence-grounded findings, relevant timing, investigation record and supported packet updates |
| `fv assemble` | Integrate partial or overlapping observations into a larger spatial/visual representation | Registered or assembled representation |
| `fv merge` | Reconcile independently produced FV packets | Merged packet or object inventory |
| `fv create` | Construct a packet from established FV information or an explicit specification | Newly created FV packet |
| `fv rebuild` / `fv upgrade` | Migrate an existing packet to a target FV specification version | Rebuilt packet and migration report |
| `fv edit` | Make an intentional change to packet content | Edited packet state and edit record |
| `fv edit viewpoint` | List/inspect source viewpoints and render VPOs; edit render-preset pose/state | Updated render VPO state and edit record |
| `fv resolve` | Address a dispute or competing interpretation | Reconciled or explicitly unresolved packet state |
| `fv validate` | Check a packet | Validation report |
| `fv compile` | Compile a resolved and validated packet for reconstruction | Renderer specification and, where supported, reconstruction |
| `fv audit` | Independently compare a reconstruction with the expected packet | JSON audit report |

## General command rules

- Prefix an FV instruction with `fv`. Do not treat an ordinary sentence as an FV command unless the user clearly requests FV work.
- A command may be followed by natural-language objectives or constraints. These can change the task's focus or sampling priority; they do not become source evidence.
- Keep operations separate. Do not silently combine analysis, investigation, editing, migration, dispute resolution, validation, compilation, and audit.
- FV work products are files when the operation calls for an artifact. A chat summary is supplementary, not a substitute for the packet, report, or reconstruction specification.
- Do not claim that an artifact was created if the environment could not create it. Identify missing inputs instead of inventing them.
- The command interface does not imply that a standalone FV executable, shell command, or local CLI has been implemented.

---

## `fv analyse`

**Purpose:** Analyse an attached or otherwise identified raw visual source using the complete FV procedure.

**Input:** An image, video, CCTV segment, LiDAR-camera sequence, or other visual media source. Supply or attach the source media.

**Output:**
- For an image: the complete FV packet as actual packet files, packaged as a ZIP. The ZIP is the primary deliverable.
- For a video: a packet containing OI (Object Inventory), MSRM (Map Spatial Relationship Manager), and TD (Temporal Data). TD is authoritative for the temporal record. Package the video packet as a ZIP when file packaging is available; the ZIP is the primary deliverable.
- For every newly generated packet: root-level `packet_provenance.json`, validated against `SPECIFICATION/FV_Packet_Provenance_Schema.json`.
- For every newly generated image/video packet: root-level `viewpoint.json` with source-supported initialisation. For video, record supported viewpoint transitions in TD. Preserve unknown position/orientation; do not invent camera geometry.
- For video frames actually captured/retained as evidence, perform the applicable FV image-analysis procedure; sampling does not replace analysis of a selected frame.
- When audio is intentionally included: preserve the source audio and timestamped `transcript.json` together under packet-level `audio/`; create the transcript before initial TIR/TD investigation. Treat it as a provisional sampling cue, assess transcription fidelity separately from cross-modal support and timing/context mismatch, and commit claims to TD only when source evidence supports them.

The media record may include optional attribution, organization, and contributor information when supplied or reliably available. Do not infer missing people, roles, organizations, contact details, timestamps, licences, or rights claims. Omit unavailable optional add-ons; do not retrofit legacy packets with guessed information.

**Boundary:** Analyse is general source analysis and packet creation. Use `fv investigate` when the user wants a finding about a specified object, event, relationship, correspondence, or question in supplied media. No separate `fv query` command is defined; question-directed media analysis belongs to `fv investigate`.

**Example:**

```text
fv analyse [attached image or video]
```

## `fv investigate`

**Purpose:** Investigate a specified object, event, relationship, correspondence, or question in supplied media or across multiple observations/media. The user may simply name an object in the media, or ask a question about it. Investigate the target itself and report source-supported findings, including what it did and when where relevant.

**Input:** The target or question and the relevant source media/observations. The question directs attention and sampling; it does not dictate the answer.

**Output:** A direct, evidence-grounded finding with relevant timestamps or intervals where applicable, plus a persistent TIR (Temporal Investigation Record) when the investigation produces a result that needs to be retained. Preserve hypotheses, competing and rejected interpretations, sampling decisions, evidence paths, and unresolved questions. A chat answer should identify material coverage gaps or uncertainty; it must not require the user to inspect TD files to obtain the finding. Commit only source-supported conclusions to authoritative packet records.

For video, use temporal observations and adaptive sampling as needed to locate relevant actions/events and their timing. Report absence only when the available media coverage is adequate to support it; otherwise report that the result is inconclusive or coverage is incomplete. A task objective can alter attention or sampling priority. It cannot supply missing identity, event, motivation, or temporal facts.

When audio is included, assess transcription fidelity separately from visual/cross-modal support, ambiguity, and timing/context mismatch in TIR. Transcript segments may guide adaptive sampling before visual confirmation, but claims enter TD only when supported by acquired source observations.

**Example:**

```text
fv investigate this person across these CCTV clips
fv investigate the kitten in this video
fv investigate what the kitten did in this video and when
fv investigate whether a white dog appears anywhere in this image
fv investigate whether a delivery person appeared during the covered CCTV period
```

## `fv assemble`

**Purpose:** Integrate partial, viewpoint-dependent spatial representations into a larger, more cohesive representation.

**Input:** Source pieces or local representations that cover portions of a larger view or place. Examples include overlapping LiDAR scans, telescope fields, aerial imagery, microscopy tiles, and overlapping photographs. Treat each as a local view/maplet associated with its supported viewpoint and spatial information, not as an interchangeable image crop or file tile. Maplets may differ in viewpoint, direction, coverage, scale, resolution, occlusion, and detail.

**Procedure and output:**
1. Identify each source piece, its generator, and acquisition context where known.
2. Establish supported viewpoint/reference information, coverage, scale or resolution, calibration, pose or orientation, time/order, and limitations. Keep unknown values unknown.
3. Inspect overlap, gaps, occlusions, and shared structures. Use only supported or justified correspondences.
4. Register the local representations into a common reference using a suitable method for that media type. Retain transformations, assumptions, residuals, and conflicts.
5. Integrate the pieces while preserving which source views contribute to each region.
6. Preserve unobserved areas, weak correspondences, viewpoint-specific evidence, and unresolved conflicts.

**Boundary:** Assembly integrates local spatial representations into a cohesive map/view; it is not merely joining file edges or blending pixels. Separate historical/current datasets covering the same field are independent observations, not automatically pieces of one acquisition; comparison is a distinct companion workflow, not an established assembly result. Geometric correspondence does not establish persistent object identity. It is also not `fv merge`.

**Example:**

```text
fv assemble these LiDAR scans
```

## `fv merge`

**Purpose:** Reconcile independently produced FV packets or packet-scoped object inventories.

**Input:** Two or more FV packets.

**Procedure and output:** Compare source evidence, temporal continuity, structural properties, relationships, and preserved visual evidence before establishing normalized persistent identity. Produce the merged packet or object inventory while preserving packet-scoped IDs and provenance.

Do not assume equal local IDs mean equal objects. Do not merge objects merely because they share a category or generic components.

**Boundary:** Merge combines already-produced FV knowledge. It does not register partial observations into a larger map; that is `fv assemble`.

**Example:**

```text
fv merge these two adjacent CCTV packets
```

## `fv create`

**Purpose:** Deliberately construct a new FV packet from established FV information or an explicit specification.

**Input:** Established information, an explicit packet specification, or a suitable existing packet from which the requested new packet is to be constructed.

**Output:** The requested packet as actual packet files when file creation is available. A reconstruction packet is one possible use.

**Boundary:** Create constructs a packet; it is not raw-source analysis. It must not manufacture visual facts or turn external knowledge into visual evidence.

**Example:**

```text
fv create a reconstruction packet from this resolved packet
```

## `fv rebuild` (alias: `fv upgrade`)

**Purpose:** Migrate an existing FV packet to the current authoritative specification version or to a version explicitly supplied with `--to`.

**Syntax:**

```text
fv rebuild [packet] [--to <FV-version>]
fv upgrade [packet] [--to <FV-version>]
```

If no target version is supplied, use the current authoritative Working Process Specification itself as the target, as the normative rebuild rule directs. Its header describes a v0.24 base with later normative additions, including v0.26 and v0.27, but does not assign a consolidated release number. Record this target description in the migration report without inventing a release label or treating v0.27 alone as the consolidated version. The consolidated release label remains an open versioning decision; its absence does not by itself block migration to the current authoritative specification. `fv upgrade` is an alias for the same operation, not a separate workflow.

**Input:** An existing FV packet and, optionally, the target FV version.

**Procedure and output:**
- Preserve the supplied packet as the migration source. Work on a separate rebuilt copy unless the user explicitly requests an in-place replacement.
- Inspect packet files, version markers, provenance, schemas, edit history, disputes, and validation reports.
- Treat an unversioned packet as legacy; do not guess its exact authoring version.
- Map the source structure to the target specification. Distinguish mechanical transformations from compatibility handling and changes requiring source re-analysis, human input, or `fv edit`.
- Preserve identities, evidence references, scene membership, temporal order, uncertainty, negative constraints, disputes, and original provenance.
- Do not invent observations, object properties, camera geometry, coordinate frames, environmental conditions, object responses, timestamps, rights claims, or human resolutions to satisfy a newer schema.
- Produce a migration report and run target-version `fv validate` on the rebuilt copy. Report structural validation, FV semantic validation, dispute/reconciliation readiness, and independent visual audit separately.

**Outcomes:**
- **UPGRADED — VALIDATED:** migration and target-version validation passed. Compilation readiness remains a separate decision.
- **UPGRADED — REVIEW REQUIRED:** structural migration completed, but evidence, semantic, dispute, or human-review requirements remain.
- **BLOCKED:** safe migration requires missing source material, a specification decision, or human input.

**Boundary:** Rebuild is version migration, not content editing, source re-analysis, dispute resolution, or compilation. It must preserve the historical version claim rather than make legacy content appear to have been authored under the target version.

**Example:**

```text
fv rebuild [legacy-packet.zip]
```

## `fv edit`

**Purpose:** Make an intentional, evidence-grounded change to existing packet content.

**Input:** The packet and the intended change, such as an object property, viewpoint, or environmental condition edit.

**Image-packet interaction forms:**

```text
fv edit
fv edit <object-name/object-id> --list
fv edit <object-name/object-id> <property-id>
```

With no arguments, list available objects. With `--list`, list the selected object's properties. The property form identifies a direct edit target; the general syntax for supplying a new value is not standardized. Do not invent value-assignment syntax. These are agent interaction conventions, not evidence of a standalone CLI.

**Output:** The edited packet state, with successful changes and their provenance recorded in the packet's edit log. Failed or unresolved operations must not be recorded as successful. Preserve before/after information. For viewpoint edits, preserve source `initial_state`, validate the render VPO against `FV_Viewpoint_Schema.json`, and leave OI/MSRM scene content unchanged.

The target must be sufficiently unambiguous. Do not guess between objects or properties.

**Boundary:** Edit changes packet content; it does not perform specification-version migration. Use `fv rebuild` or `fv upgrade` for migration. The general value-assignment syntax for every object/property edit is not fully standardized; do not invent unsupported syntax.

### Viewpoint editing

The `fv edit viewpoint` subcommand has defined forms:

| Operation | Syntax | Purpose |
|---|---|---|
| List | `fv edit viewpoint list` | List source viewpoints and reusable render presets |
| Show | `fv edit viewpoint show <VP-ID>` | Show a viewpoint definition |
| Set position | `fv edit viewpoint set <VP-ID> position x y z` | Set camera position in the declared world frame |
| Set orientation | `fv edit viewpoint set <VP-ID> orientation yaw pitch roll` | Set intrinsic Y-X-Z camera rotation in degrees |
| Set projection | `fv edit viewpoint set <VP-ID> projection perspective|orthographic` | Set projection type |
| Set field of view | `fv edit viewpoint set <VP-ID> fov degrees` | Set perspective field of view |
| Set target | `fv edit viewpoint set <VP-ID> target x y z` | Set look-at target |
| Save preset | `fv edit viewpoint save <VP-ID> as <name>` | Save a named reusable preset or derived version |
| Set default | `fv edit viewpoint default <VP-ID>` | Set the packet's default render viewpoint |
| Reset | `fv edit viewpoint reset <VP-ID>` | Restore the selected preset's saved state |

Every viewpoint edit must validate against `SPECIFICATION/FV_Viewpoint_Schema.json`, preserve the source `initial_state`, record before/after values and provenance in the edit log, and leave OI/MSRM scene content unchanged. List/show may inspect source viewpoint records and render VPOs; set/save/default/reset operations modify an editable render VPO or active render pose only. Do not treat a source-only viewpoint record as an editable render VPO. A 2D source image alone does not provide arbitrary 3D geometry; report unsupported or approximate renders rather than claiming exact camera movement.

`VPO_DEFAULT` may be instantiated only through an explicit packet-creation or editor action. The current textarea command list does not define an instantiation subcommand or syntax. Do not invent one; use an explicitly available editor action or request clarification. The current Visual Workbench text console parses only viewpoint `set position` and `set orientation`; use the broader browser UI controls for other supported VPO fields rather than claiming the console implements every listed form.

**Schema/command coverage boundary:** `FV_Viewpoint_Schema.json` also defines projection-specific `orthographic_scale`, framing (`aspect_ratio`, `fit`, optional center/notes), coordinate-frame metadata, and optional tolerances. The command table does not yet define standard edit syntax for all of these fields. Do not infer that `set projection orthographic` alone creates a valid orthographic pose; the required `orthographic_scale`, coordinate frame, and framing must also be present. Until command syntax is explicitly specified, use a schema-valid editor action or request clarification.


**Example:**

```text
fv edit viewpoint set VP-AB12CD34 position 2 1 4
```

## `fv resolve`

**Purpose:** Resolve an FV dispute, ambiguity, correspondence conflict, or competing interpretation.

**Input:** The relevant dispute, ambiguity, or competing interpretation, together with any required human resolution information and cited evidence.

**Procedure and output:** Preserve the original automated observation, uncertainty, evidence references, and dispute history. Where human intervention is required, the human supplies resolution information but does not declare the packet reconciled. The AI then reads `dispute.json`, inspects cited source evidence and snapshots, reviews the human changes, and reconciles the packet. At minimum, update OI and PC where justified; update other packet records only where a justified dependency is established. Preserve provenance and distinguish later human additions from the AI's original observations.

After reconciliation, validate the affected packet records. If every dispute is resolved and validation passes, move the detailed `dispute.json` to `dispute.reconciled.json` and create a new small `dispute.json` with aggregate status `resolved`. If any dispute remains unresolved or validation fails, keep the detailed `dispute.json` in place with aggregate status `open`. The packet and resolution history must preserve whether the issue was resolved or remains unresolved.

**Boundary:** An open or invalid dispute remains a reconstruction gate. Do not merely change a status field to make compilation possible.

**Example:**

```text
fv resolve dispute D-014
```

## `fv validate`

**Purpose:** Check an FV packet against the applicable authoritative FV specification.

**Input:** The packet to validate.

**Checks and output:** Produce a validation report covering applicable structural problems, missing required fields, contradictions, inventory problems, evidence consistency, unresolved disputes, and reconciliation state. Also assess whether the packet may need migration to the current FV specification version.

When audio is included, verify that the audio file and `transcript.json` are present, source-aligned, and mutually traceable; check that TIR preserves the provisional transcript assessment and material discrepancies. Audio and visual evidence remain separate evidence streams.

The rebuild assessment must use one of these outcomes and explain the reason, affected records/rules, and next step:

- **REBUILD NOT INDICATED**
- **REBUILD MAY BE NEEDED**
- **REBUILD RECOMMENDED**
- **REBUILD REQUIRED**
- **ASSESSMENT INDETERMINATE**

**Boundary:** Validation checks; it does not silently repair the packet, rebuild it, rewrite version claims, or resolve disputes. Identify what must be reprocessed or changed.

**Example:**

```text
fv validate [packet]
```

## `fv compile`

**Purpose:** Compile a resolved and validated FV packet into a reconstruction specification and, when the required renderer/generator is available, perform the reconstruction.

**Input:** A packet that has passed the applicable validation, reconciliation, and dispute gates.

**Default output:** A lossless renderer specification and/or the reconstruction artifact available to the environment.

**Compilation gates and restrictions:**
- Verify the packet validation result and the current `dispute.json` rendering gate.
- Stop if the packet is invalid, reconciliation is incomplete, or `dispute.json` is open, missing, malformed, or inconsistent.
- Do not resolve disputes or repair an invalid packet during compilation.
- Translate packet content into renderer-specific syntax without adding semantic content, world knowledge, props, motivations, genre conventions, or other undeclared information.
- Include the required rebuild assessment. If rebuild is **REBUILD REQUIRED**, stop and direct the operator to rebuild/upgrade, validate, and retry. If rebuild may be needed or recommended, continue only where the packet independently passes all compilation gates and the target specification permits its compatibility path; state that no rebuild occurred.
- If the assessment is **ASSESSMENT INDETERMINATE**, do not imply that the packet is current. Stop if the uncertainty affects a required compilation rule and identify the missing information; otherwise continue only with an explicit warning and the applicable compatibility boundary.
- If rendering is unavailable, produce the lossless compiled renderer specification rather than pretending a reconstruction occurred.

### Prompt-only mode

**Syntax:**

```text
fv compile --prompt [attached-packet.zip]
```

This mode produces only a compiled, generator-ready prompt/specification artifact. The packet ZIP is input, not an instruction to render.

Prompt-only mode applies the same validation, reconciliation, and dispute gates as ordinary compilation. Preserve packet identities, closed object and background inventories, scene membership, off-screen persistence, spatial relations, temporal order, transitions, uncertainty, negative constraints, and viewpoint information. State renderer limitations and missing geometry where relevant. Do not invoke an image/video generator or claim that an image was generated. The operation ends when the prompt artifact is produced.

**Examples:**

```text
fv compile
fv compile this packet as a video
fv compile --prompt [attached-packet.zip]
```

## `fv audit`

**Purpose:** Independently audit a reconstruction by comparing the expected/original FV packet with a separate FV packet produced by analysing the generated media.

**Input:** The expected FV packet, the independently generated-media FV packet, and the generated media where available.

**Procedure and output:**
- Analyse the generated media independently. Do not use the expected packet as evidence for what is visible in the generated media.
- Keep the media generator, generated-media packet generator/analyst, and auditor identities distinct. Use `packet_provenance.json` when present; legacy packets without it remain usable with unknown provenance.
- Do not use the reconstruction generator's explanation as evidence.
- Do not rewrite either packet during the audit. Keep the generated media available for inspecting and locating deviations.
- Classify deviations using the FV failure taxonomy, including inventory, identity, spatial, temporal, behaviour, style, unsupported-detail, and evaluator-uncertainty classes.
- Each material deviation must reference source-media evidence (frame/time/region/crop where applicable) and relevant expected/generated packet records where possible.
- Record category-specific numerator, denominator, uncertainty count, rate, and exact unit definition/scope. Calculate `100 * numerator / denominator`; use null for a zero denominator. Do not count uncertain units as passes or failures, or collapse unlike categories into one overall percentage.

When file creation is available, create `FV_AUDIT_REPORT.json` as the primary downloadable artifact and validate it against `SPECIFICATION/FV_Audit_Report_Schema.json`. A readable summary is supplementary.

**Example:**

```text
fv audit [expected-packet.zip] [generated-media-packet.zip] [generated-media]
```

### Batch audit is a separate utility

`fv audit batch` is **not** a native skill-runtime command. The repository includes the offline reference processor `TOOLS/fv_audit_batch.py`. It validates existing JSON audit reports and writes an aggregate JSON report plus a readable summary; it does not re-audit media or rewrite source reports. See `SPECIFICATION/FV_Provenance_And_Audit.md` for its use and limits.

---

## Typical command sequence

A common reconstruction path is:

```text
analyse / investigate / assemble / merge / create
                    ↓
          (optional rebuild/upgrade)
                    ↓
       (resolve if required)
                    ↓
                validate
                    ↓
                 compile
                    ↓
                  audit
```

Not every task requires every operation. Use only the operations needed for the task and the packet's state. An intentional `fv edit` may be needed when packet content must change; it is a separate operation, not a mandatory stage in every reconstruction path. Validate affected packet records before compilation.

In particular:

- **Assemble** combines partial or overlapping observations.
- **Merge** reconciles independently produced FV knowledge.
- **Create** constructs a packet from established information or a specification.
- **Rebuild/upgrade** migrates packet structure to a target FV version.
- **Edit** makes intentional content changes.
- **Resolve** is required when a dispute or ambiguity blocks downstream work.
- **Validate** is the packet check; it does not repair.
- **Compile** requires a resolved and validated packet and never performs resolution.
- **Audit** independently tests the reconstruction against the expected packet.

## Related documentation

- [How to use FV](HOW_TO_USE.md) — quick route through common tasks.
- [Agent skill](SKILL.md) — operational instructions for an FV-capable agent.
- [Working Process Specification](SPECIFICATION/FV_Working_Process_Specification.md) — authoritative process and rules.
- [Faking Vision README](README.md) — project introduction and overview.
