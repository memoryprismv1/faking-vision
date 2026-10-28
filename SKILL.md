---
name: faking-vision
description: Operate Faking Vision (FV) for image and video analysis, visual investigation, spatial assembly, FV packet construction and merge, dispute resolution, reconstruction, packet validation, prompt compilation, temporal investigation, independent reconstruction audit, and the textarea command interface for FV work. Use this skill whenever the user asks to analyse an image/video with FV, create or inspect an FV packet, reconstruct from an FV packet, or audit a reconstruction. The canonical FV Working Process Specification at `SPECIFICATION/FV_Working_Process_Specification.md` is authoritative; do not substitute general computer-vision assumptions for FV procedures.
---

# Faking Vision Agent Skill

## Mandatory Making Vision prerequisite and promotion gate

Before performing any visual analysis, investigation, assembly, merge, reconstruction, or audit, obtain and read the canonical Making Vision material:
https://www.memoryprism.com/readings/making-vision

Do not begin visual analysis on the assumption that this skill alone, general computer-vision knowledge, or a remembered summary substitutes for reading the canonical material. If the material cannot be accessed or read, state that limitation and do not claim the prerequisite was completed.

Apply the Making Vision processing order: current sensory field/input and directly supported structure → candidate generation → candidate allocation and promotion → deeper processing. Keep candidate generation, promotion, recognition, identification, and object state distinct. Internal state and expectations may influence promotion but must not be misrepresented as external visual evidence.

**Object promotion is a required gate before object counting or identity assignment.** Do not count every detected region as an object, assign identities, or build persistent correspondence from unpromoted candidates. Promote candidates only when supported by the available visual evidence; preserve uncertain, rejected, and unresolved candidates rather than forcing a count or identity. Promotion does not license adding unsupported semantic detail.



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

Example:

`fv investigate this person across these CCTV clips`

### `fv assemble`

Assemble partial or overlapping observations into a larger spatial or visual
representation.

Use this for inputs such as overlapping LiDAR scans, telescope fields of
view, aerial/satellite imagery, microscopy tiles, or overlapping
photographs. Establish registration, overlap, coordinate alignment, and
source correspondence as supported by the evidence.

Preserve source provenance and unresolved registration conflicts.

`fv assemble` does not silently establish global object identity. If
independently produced FV packets also need identity reconciliation, use
`fv merge`.

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

### `fv validate`

Validate the identified FV packet against the v0.24 packet rules.

Validation is not reconstruction and is not an independent reconstruction
audit.

Report structural problems, missing required fields, contradictions,
inventory problems, unresolved disputes, and reconciliation state as
applicable.

Do not silently repair the packet. If repair is required, identify what must
be reprocessed or changed.

Example:

`fv validate`

### `fv compile`

Compile a **resolved and validated** FV packet into a reconstruction
specification and perform the reconstruction when the required
renderer/generator is available.

Compilation is a fidelity boundary. It may translate packet content into
renderer-specific syntax but may not add semantic content, world knowledge,
props, motivations, genre conventions, or other undeclared information.

Before compilation, verify the packet validation result and the current
`dispute.json` rendering gate. If the packet is invalid, reconciliation is
incomplete, or `dispute.json` is open, missing, malformed, or inconsistent,
stop and return the packet to the appropriate earlier operation.

Compilation never resolves disputes.

If the available environment cannot perform the actual rendering, produce
the lossless compiled renderer specification rather than pretending that
rendering occurred.

Examples:

`fv compile`

`fv compile this packet as a video`

### `fv audit`

Independently audit a generated reconstruction against its FV packet and,
where available, the source.

Do not use the generator's explanation as evidence.

Classify observed deviations using the FV audit framework, including
inventory, identity, spatial, temporal, behaviour, style, unsupported-detail,
and evaluator-uncertainty classes.

`fv audit` is an evaluation operation. It does not rewrite the packet merely
because the reconstruction differs from it.

Example:

`fv audit`

## Command interpretation rules

- `fv analyse` means raw source → FV analysis/packet.
- `fv investigate` means specified visual question/object/event → investigative evidence path.
- `fv assemble` means partial/overlapping observations → registered/assembled representation.
- `fv merge` means independent FV packets → reconciled packet/object inventory with provenance preserved.
- `fv create` means established information/specification → newly constructed FV packet.
- `fv resolve` means open dispute/ambiguity → reconciled or still-unresolved packet.
- `fv validate` means packet → validation report.
- `fv compile` means resolved + validated packet → lossless renderer specification and, where supported, reconstruction.
- `fv audit` means reconstruction → independent FV evaluation against the packet/source.
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
- `fv audit` MUST create the independent audit report/artifact when file
  creation is available.
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

This skill contains the complete v0.24 FV operating material and the textarea command/output contract. Use it directly; the user should not need to supply the FV specification separately. The three source documents are preserved verbatim in `references/` for provenance.

The source hierarchy is: `SPECIFICATION/FV_Working_Process_Specification.md` is the single authoritative FV specification. This skill is the operational interface and must not introduce rules that conflict with or are absent from the specification.

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

## Complete authoritative source

The following is the complete extracted text of the v0.24 Working Process Specification.

---

FAKING VISION
Working Process Specification — Rewritten (v0.24)
Ground-up operational specification for image/video analysis, FV packet generation, reconstruction, prompt compilation, and evidence-grade evaluation.
Acceptance test: Give this document, an image or video, and no prior FV knowledge to an unfamiliar AI instance. It must be able to analyse the source and produce a valid FV packet. Conversely, given this document and a valid FV packet, it must be able to produce or attempt a reconstruction without inventing semantic content.
This document is deliberately written as an operator specification. It contains procedures, decision rules, schemas, examples, validation gates, and failure classes. It is not a single algorithm.
1. Purpose and acceptance criterion
Faking Vision (FV) converts visual observations into a portable structured information packet and tests whether a reconstruction system can hydrate that packet without silently substituting its own learned world model.
The packet is the reconstruction source of truth. The reconstruction system is not being asked to produce the most plausible version of what it sees. It is being asked to reproduce the information supplied by FV.
1.1 The unfamiliar-AI acceptance test
The specification is considered operational only if an AI instance that has never participated in FV can execute the following tasks from the document alone.
1.2 What failure means
If the unfamiliar AI must ask what FV means by 'analyse the frame', what counts as an entity, how to build OI/MSRM/TD, how to represent uncertainty, or how to export the packet, the specification has failed operationally. A schema without a generation procedure is not sufficient.
2. Core rules
Observe before naming. Record visible structure before committing to semantic identity where identity is uncertain.
Do not convert plausibility into evidence. A thing that would normally be present in a scene is not therefore present in the source.
Separate observation, interpretation, and packet commitment.
Every declared reconstruction entity must have a source basis or an explicitly declared test instruction.
A packet is closed after inventory lock. Reconstruction may not create new semantic entities to make the scene more plausible.
Appearance is not automatically an entity. Texture, shading, reflection, highlight, shadow, fold, grain, and similar visual phenomena remain appearance unless separately represented as useful semantic structure.
Movement is not duplication. A persistent identity changing location, pose, orientation, or behaviour remains the same identity unless evidence supports another instance.
Off-screen is not deleted. Scene membership and visibility are distinct from identity existence.
Uncertainty must survive the pipeline. An unresolved observation cannot silently become a definite packet fact.
Evaluation claims require evidence. A suspected failure without a frame/time/location remains unresolved.
Renderer limitations are not packet facts. If a renderer cannot express a constraint, record that limitation instead of rewriting the packet.
The packet-to-prompt transformation is itself auditable. A compiler may translate syntax, but may not add world knowledge.
3.1 FV operation model and command interface
`fv analyse`, `fv investigate`, `fv assemble`, `fv merge`, `fv create`, `fv resolve`, `fv validate`, `fv compile`, and `fv audit` are distinct FV operations. The normal downstream path is analyse/investigate/assemble/merge/create → resolve → validate → compile → audit. Assemble combines partial or overlapping observations into a larger spatial/visual representation; merge reconciles independently produced FV packets and may normalize persistent identity only when evidence supports equivalence. Create constructs a packet from established information or an explicit specification. Compile requires a resolved and validated packet and never resolves disputes or repairs packets.
3. Operating model: five distinct layers
Never use a later layer to retroactively rewrite an earlier layer. A generated image cannot become evidence about what was in the original source.
4. Source intake
4.1 Image intake
Before semantic analysis, record:
source_id and file identity
pixel dimensions and aspect ratio if available
orientation/rotation
visible image boundaries
obvious cropping or framing limits
quality limitations: blur, compression, low resolution, occlusion, glare, darkness, overexposure, etc.
whether the source is a single image or a frame extracted from video
4.2 Video intake
Record:
source_id
duration
frame rate if available
frame dimensions
audio presence if relevant
obvious cuts/tableau changes
quality limitations
whether the source contains continuous motion, hard cuts, fades, or mixed transitions
The analyst must not assume that every frame needs identical semantic analysis. Sampling is an analysis strategy, not permission to ignore meaningful changes.
4.3 Source integrity
If metadata or source quality prevents a reliable conclusion, preserve the limitation. Do not manufacture precision.
5. Image analysis procedure
5.1 Pass 1 — visual inventory without semantic commitment
Inspect the whole image. Identify visually bounded or otherwise separable regions and structures.
Locate major boundaries, silhouettes, contours, surfaces, and spatial regions.
Note repeated shapes or structures.
Note partially visible structures and occlusions.
Record obvious motion only if the source itself contains motion cues; a still image does not establish temporal change.
Do not immediately assign familiar object names where the evidence is ambiguous.
5.2 Pass 2 — candidate generation
For each potentially meaningful structure, create a candidate record.
Example: if a fruit is initially observed only as a small red rounded form, the evidence may support strawberry, raspberry, or another candidate rather than a single identity. Surface structures, aggregate-unit structure, a leafy calyx, or other diagnostic components can then be searched for to distinguish candidates. The fruit name is not evidence until the visible component bundle supports it.
For video, component emergence, disappearance, movement, or interaction may trigger adaptive sampling or behaviour-triggered component tracking when the component materially changes candidature, identity, relationship, or uncertainty. Record the candidature trajectory in TIR; promote only source-supported conclusions into TD.
Do not use later whole-object recognition to retroactively rewrite the earlier candidature record. The investigation must preserve the forward evidence path that existed when each candidate was considered.
Candidate verification is component- and relationship-based. A candidate may be promoted when the observed bundle of components and relationships is sufficiently diagnostic for the task. A candidate should be weakened or rejected when expected diagnostic evidence is contradicted, or when a required component should have been visible in the inspected view but is not observed. Mere absence from an uninformative or occluded view is not rejection.
Search should be targeted by the candidate set. Once a component creates candidature, ask what additional source evidence would distinguish the candidates, then inspect for that evidence. Do not search only for confirming evidence for the first candidate; where feasible, include evidence that could discriminate between or falsify the alternatives.
the evidence supporting the promotion or rejection decision.
whether the candidate was strengthened, weakened, rejected, or remains unresolved;
which of those expected components/relationships were searched for and what was actually observed;
the additional components or spatial/structural relationships expected to distinguish the candidates;
the candidate set supported by that component and current context;
the observed component and its source location;
For each component-driven candidature, record at minimum:
A component is evidence, not an identity. A single component may support several candidates. Candidate generation must preserve the alternatives actually supported by the observed component and context; it must not collapse immediately to the most familiar object.
When an object identity is uncertain, a visible component may be used to generate a bounded set of object candidates. Do not require whole-object recognition before candidature. The operational direction is: component → candidate set → targeted search for expected components/relationships → candidate verification or rejection.
5.2.1 Component-driven candidature and verification
5.3 Pass 3 — entity/component/appearance decision
Classify each candidate using the following decision order.
Is it merely a visual appearance phenomenon of an already represented entity? If yes, keep it as appearance unless a separately useful semantic representation is required.
Is it a separately useful part of an entity that must be represented to reconstruct the supplied information? If yes, classify as a component.
Is it a distinct semantic entity? If yes, classify as an object/instance candidate.
If the distinction cannot be established, retain the candidate as unresolved rather than forcing a category.
5.4 Pass 4 — identity resolution
Determine whether multiple observations refer to the same instance or different instances.
Identity resolution begins as a correspondence investigation, not an immediate identity commitment.
Use visible structural continuity and source evidence. Where observations occur across multiple investigated media, maintain a provisional correspondence hypothesis until the evidence supports a stronger identity statement.
For each correspondence investigation, record:
• the observed components supporting the correspondence;
• the quality of each component as identity/correspondence evidence: high, weak, or transient;
• the candidate correspondence(s) supported by the current evidence;
• additional discriminating components or relationships that could distinguish the candidates;
• which expected or discriminating components/relationships were searched for;
• what was actually observed;
• whether the correspondence was strengthened, weakened, rejected, or remains unresolved;
• the evidence supporting that status.
Component quality must be interpreted in context. A high-quality component is relatively distinctive and sufficiently stable to contribute strongly to correspondence; a weak component is observable but common, non-distinctive, or insufficient on its own; a transient component may be useful but depends on temporary pose, expression, clothing, illumination, viewpoint, or other changing state.
Do not merge merely because two candidates belong to the same category or share generic components. Do not split merely because appearance changes.
Do not treat an unobserved expected component as negative evidence unless the inspected view should have exposed it. Occlusion, crop, blur, scale, viewpoint, and other source limitations may make an expected component unobservable.
Useful TIR wording includes:
• “Initial investigation suggests same object based on [component report].”
• “Correspondence remains unresolved; current evidence includes [component report].”
• “If the said object is the same object across multiple investigated media, search for [expected/discriminating component or relationship].”
Do not promote a correspondence hypothesis to a committed persistent identity until the available evidence supports that resolution. If continuity cannot be established, retain separate candidates or unresolved identity as appropriate.
Record the evidence used for the identity decision.
5.5 Pass 5 — packet promotion
Only after observation and candidate resolution should information be promoted into the reconstruction packet.
Recognition is not a prerequisite for packet construction. A novel object may first be represented structurally and remain unnamed. Naming can be added later when supported.
5.6 Image/video packet decision gate
Before packet construction, classify the reconstruction target. For an image, build OI + MSRM, with optional PC. For a video, build OI + MSRM + TD, with optional PC. TD is not optional for a video. If a source is called a video but no meaningful temporal-difference record can be established, do not fabricate TD; classify the reconstruction target as an image or, only when explicitly defined by the experiment, as a set of independent images.
6. Video analysis procedure
6.1 Establish temporal structure and the temporal diff baseline
Start by identifying meaningful temporal units. A temporal unit may be a continuous scene, tableau, shot, or other interval in which the relevant visual organization remains coherent.
Inspect the video globally for major scene/tableau boundaries.
Create a scene/interval list with start and end times or frame ranges.
Within each interval, identify stable entities, components, spatial relationships, and states. These establish the baseline against which TD records subsequent differences.
Inspect transitions separately.
Inspect intervals around every meaningful appearance, disappearance, movement, or state change.
If a transcript claim identifies a potential gap in the current TIR/TD representation, use its temporal location as an adaptive sampling target, subject to the current transcript assessment and timing/context information. Acquire the additional source observation and update TIR. Promote a resulting statement into TD only when the retained source evidence supports it. If the relationship between the audio commentary and the visual scene remains unresolved, preserve the uncertainty rather than deciding that the commentary is false, satirical, or otherwise untrustworthy without evidence.
A small number of transcript errors or apparent mismatches does not by itself invalidate the transcript as a useful sampling signal. The investigation should record the discrepancy, continue testing the channel, and use transcript claims as candidate sampling cues while their support is being established.
The temporary TIR must independently assess the transcript against the source audio and the visual source evidence. Track the audio/transcript channel cumulatively rather than using a binary keep/discard decision. At minimum distinguish: transcription fidelity (whether the transcript accurately represents the audio); visual/cross-modal support (whether a narrated claim corresponds to visual evidence); unresolved or ambiguous content; and timing/context mismatch where audio-supported commentary does not correspond scene-by-scene with the current visual interval.
Use the transcript during temporal investigation as an additional cue for adaptive sampling. A transcript segment may identify a time or interval that deserves visual inspection, including an event, action, relationship, or other claim that was not captured by the initial temporal observations. The claim does not need to be visually supported yet; identifying a potential gap is itself a reason to acquire the relevant source observation.
When audio is intentionally included, generate a timestamped transcript before the initial temporary TIR/TD temporal investigation. The transcript is a provisional analytical variable, not a source-of-truth record and not a substitute for listening to the source audio.
6.1.1 Audio transcript as a provisional temporal cue
6.2 Temporal sampling
Sampling density must be adaptive. Begin with a lazy/coarse temporal scan. When temporal-difference (TD) evidence appears within an interval, increase sampling density locally and recursively inspect the affected subinterval. When the perturbation subsides, sampling may relax again. The sampling rate is therefore driven by observed perturbation, not imposed uniformly across the video.
6.2.1 Selected-frame FV image analysis
Every source frame that FV actually captures or retains as an evidence observation must undergo the default FV image-analysis procedure. Temporal sampling determines which source frames are acquired as evidence; it does not replace image analysis of those frames with mere frame retention.
For each selected frame, perform the applicable image-analysis passes: visual inventory, candidate generation, entity/component/appearance decision, identity assessment where temporal context permits, and packet/evidence promotion as warranted. The resulting frame-level analysis must be available to TIR and may update OI, MSRM, TD, uncertainty, disputes, or other packet records where justified.
A selected frame is therefore both source evidence and an FV image-analysis observation. A packet must not treat a captured frame as semantically unanalysed merely because the temporal sampler selected it. Conversely, frames that were never selected need not receive the same full FV image-analysis treatment.
The temporal sampler answers **which observations are worth acquiring**. FV image analysis answers **what is present in each acquired observation**. These are distinct operations and neither substitutes for the other.
6.3 Track candidate identities and temporal lineages
For every candidate that may persist, maintain a temporal ledger.
6.3.1 Behaviour-triggered component tracking
Do not track every declared component merely because it exists. Component tracking is triggered by component behaviour when that behaviour creates enough perturbation or uncertainty to matter to the FV representation.
A component may remain an inventory/property detail while behaviourally irrelevant. Promote it to a temporal tracking target only when its change, movement, interaction, deformation, state transition, or other behaviour materially affects the scene representation, an object state, a relationship, an action, reconstruction fidelity, or an unresolved temporal question.
Examples: a visible wheel does not automatically require wheel tracking; wheel rotation that materially explains vehicle behaviour may require local tracking. A person's hand does not automatically become a tracked component; a hand reaching for, contacting, or manipulating another object may make the hand's behaviour information-bearing. A decorative button that changes without affecting represented structure need not be tracked.
Component tracking is therefore **perturbation-triggered, not inventory-triggered**. The tracking decision and its evidence should be recorded in TIR, and any promoted component state/change should enter TD only when supported by the retained observations.
6.4 Distinguish four temporal events
6.5 Temporal conflict handling
If two observations appear incompatible, do not solve the conflict by spawning an extra object. First test whether the conflict is explained by movement, occlusion, camera/framing change, scene change, or uncertainty. Only explicit source evidence permits multiple instances.
7. Observation record and evidence discipline
The observation record is the bridge between raw source and packet. It must preserve what was seen and why a packet assertion was made.
The analyst must be able to answer: 'What in the source caused this packet field to exist?' If the answer is only 'because that is what the scene normally contains,' the field is not source-grounded.
8. Packet architecture
The FV packet separates object/instance information, spatial organization, temporal change, and optional project constants.
8.0 Packet architecture at a glance: OI answers WHAT EXISTS; MSRM manages WHERE/HOW ENTITIES ARE SPATIALLY RELATED; TD records WHAT CHANGED AND WHEN; PC contains genuine project-wide constants.
8.1 OI — Object Inventory
OI is the authoritative inventory of what entities/instances exist in the reconstruction target. It records the identities and the properties/components that matter for reconstruction.
canonical identity
instance identity where required
category/name when supported
properties
declared components
anomalies
current state
behaviour where relevant
expression/facing/direction where relevant
uncertainty
8.2 MSRM — Map Spatial Relationship Manager
MSRM is the authoritative spatial mapping and relationship-management layer. It records where entities are and how they relate spatially, at the precision actually supported by the source.
scene membership
relative position
left/right/front/back/above/below relationships where supported
distance or scale relationships when useful
object-to-object relationships
orientation and placement
camera/frame relationships when they are part of the reconstruction target
8.3 TD — Temporal Data
TD is the authoritative temporal change layer. TD is operationally a diff log: it records what changed between temporal observations, when it changed, and which persistent identity the change belongs to. TD is mandatory for video. A video without TD is not a valid video reconstruction target; it must be treated/rendered as an image unless the experiment explicitly defines the source as independent images.
For video, observation records are records within TD, not a required separate packet file. TD may contain the temporal baseline observations and the differences derived from them. Do not create an observation.json or observations.json file unless a future FV specification explicitly defines one.
scene/interval order
start/end times or frame ranges
entry/exit
movement
state changes
appearance/disappearance
off-screen status
persistence
transitions
8.3.1 TD makes the packet temporally queryable
TD is not merely video metadata and is not simply a description of the whole video. Because it records state transitions and other temporal differences, questions can be answered from the packet without reconstructing the video. For example: when did a traffic light turn green; did a pedestrian begin crossing before or after the light changed; how long elapsed between two state changes; which event happened first; did two changes overlap; or what changed between two specified times? Such answers are recoverable only to the temporal precision actually recorded in TD.
Example TD diff: 00:14.2→00:14.6, traffic_light_01.color = yellow→green. A query 'When did the light turn green?' can therefore return approximately 00:14.6. If TD does not contain the relevant transition or sufficient timing evidence, the correct answer is that the packet does not contain enough temporal information; OI, MSRM, or general world knowledge must not be used to invent the missing time.
8.4 PC — project constants
Using PC as an object database is an architectural capability to be tested, not a claim that the methodology has already been validated. Continuous same-camera footage split into temporally adjacent files is the intended experimental material for testing object reuse, packet merge, and object-database normalisation.
8.4.3 Object database status
The snapshot property is an additive property of an existing PC object declaration. Adding it must not change the existing PC structure, field organization, or semantics. If no visual evidence is available or needed, the property may be absent.
A PC object may include a snapshot property containing references to preserved visual evidence for that canonical object. Snapshot references provide visual grounding for inspection, comparison, merge, and later normalisation; they do not replace the canonical PC declaration and do not turn snapshots into canonical definitions.
8.4.2 Snapshot property for PC objects
An object declared in PC remains in the existing PC object/declaration structure. Do not reorganize PC, introduce a separate object-database container, or move existing PC information merely to support this use. Object-database capability is additive.
PC may also serve as the project’s canonical object database when a project declares reusable visual objects as genuine project-wide constants. This is a functional use of the existing PC structure, not a new packet layer or a replacement for PC.
8.4.1 PC as a canonical object database
8.5 Disputes — packet-level human-intervention and rendering-gate layer
Disputes is a packet-level structured JSON layer that records cases in which automated visual analysis, identity resolution, spatial/temporal resolution, or reconstruction audit cannot be trusted to resolve an item adequately. It is not an interpretation layer and it does not silently convert an unresolved observation into a corrected fact. The current actionable dispute state is stored in dispute.json.
A dispute record should identify at minimum: dispute_id; issue; source_id; affected layer/record or region; snapshot_ids; original observation or attempted resolution; resolution_status; resolved_by; resolution_remark; human_action_required; and relevant timestamps. The record may also contain AI reconciliation state and packet records affected after reconciliation.
dispute.json is the current rendering gate. Its aggregate status is: none when no dispute exists; open when one or more disputes remain unresolved; resolved when all recorded disputes have completed human intervention, AI reconciliation, and packet validation. Rendering is prohibited while the status is open or invalid. Rendering may proceed only when status is none or resolved.
### 8.5.1 Human resolution and packet reconciliation
A human resolves the disputed question and may add or correct object information and other relevant packet detail. The human does not directly declare the packet reconciled. The original automated observation and uncertainty must remain traceable.
The packet is returned to the AI. The AI reads dispute.json, inspects the cited source evidence and referenced snapshots, reviews the human-supplied changes, and performs packet reconciliation. At minimum, the AI updates OI and PC as justified by the human resolution and supporting evidence, preserves provenance, and determines whether every recorded dispute has been resolved. Other packet fields may be updated only where the reconciliation establishes a justified dependency.
The human additions are later resolution information. They must not be represented as evidence that the AI originally knew the answer.
### 8.5.2 Dispute reconciliation states
A — All disputes resolved. If all disputes are resolved and the reconciled packet passes validation, rename/move the existing dispute.json to dispute.reconciled.json. Then create a new, small dispute.json containing only the current aggregate resolved state needed by the rendering gate. The archived dispute.reconciled.json retains the detailed dispute history and resolution material; the new dispute.json is deliberately cheap to open.
B — One or more disputes remain unresolved. Keep the existing dispute.json in place and change only its aggregate status to open. Do not rebuild or rewrite the full dispute record merely to update the current state. The unresolved dispute details remain in the existing file.
This separation keeps the current rendering decision cheap to inspect even when a long investigation has accumulated a large dispute history.
When all disputes have been reconciled, the new dispute.json may be only:
{
  "status": "resolved"
}
The detailed records remain in dispute.reconciled.json.
### 8.5.3 Mandatory AI reconciliation and rendering gate
After human intervention, rendering remains blocked until AI reconciliation and packet validation are complete. The AI must not merely change a status field to resolved. If reconciliation cannot reliably resolve every dispute or validation fails, retain dispute.json with aggregate status open.
### 8.5.4 Current dispute file versus reconciliation history
dispute.json is the current actionable/rendering-gate state. dispute.reconciled.json is the archived detailed record of a completed reconciliation. A long investigation must not require opening a large historical dispute file merely to determine whether rendering is currently permitted.
The reconciliation lifecycle is: AI analysis → dispute.json = open → rendering blocked → human reviews source/evidence and adds or corrects packet information → packet returned to AI → AI reads dispute.json + human changes + source/evidence → OI / PC updated as justified → packet validation → dispute.json moved to dispute.reconciled.json → new small dispute.json = resolved → rendering permitted.
When audio is included, packet validation must verify that the audio file and transcript are present, source-aligned, and mutually traceable, and that the temporal investigation records the provisional transcript assessment and any material discrepancies.
AUDIO_COMPANION.txt may continue to provide human-readable audio notes, but it does not replace the audio file or transcript.json when a transcript is intentionally included.
Audio and visual evidence are separate evidence streams. A transcript may inform OI, TD, disputes, or other packet fields, but those fields must remain traceable to the audio segment or visual evidence that supports them. When audio and visual evidence disagree, preserve the conflict and use the existing uncertainty/dispute process rather than silently privileging one stream.
The packet must preserve the relationship between the audio file and the source video, including source identity and relevant time alignment. transcript.json should contain timestamped transcript segments and, where supported, speaker/voice attribution and transcription uncertainty. Do not invent words that are not supported by the audio. If speech is unclear, preserve the uncertainty rather than silently normalising it.
audio/
    source.<original-extension>
    transcript.json
Use an optional packet-level audio/ directory:
If the provisional transcript identifies a temporal location or claim not adequately represented in the current TIR/TD, use it to trigger additional sampling at the relevant location, even when the claim has not yet been visually supported. Update TIR with the new evidence and promote the result into TD only when the source supports it.
A commentary segment may be accurate while referring to an earlier, later, off-screen, or otherwise different scene state. Scene-by-scene visual disagreement must therefore be recorded as a timing/context discrepancy unless the source evidence establishes that the commentary is false. Do not infer satire, fabrication, or speaker intent merely from a mismatch.
The temporal investigation must test the transcript against the source audio and the visual evidence. TIR should maintain cumulative assessment of at least two distinct properties: transcription fidelity (whether the transcript represents the audio accurately) and cross-modal support (whether narrated claims correspond to visual evidence), alongside unresolved/ambiguous content and timing/context mismatches. This assessment is not a binary transcript-valid/invalid gate: isolated transcription or interpretation errors do not by themselves invalidate an otherwise useful audio channel.
Generate the transcript before the initial temporary temporal investigation and retain it as a provisional analysis variable. It may be used to guide adaptive temporal sampling, including by identifying potential gaps before those claims are independently verified, but it must not be promoted directly into TD merely because the transcript contains a claim.
When audio is intentionally included in a video packet, preserve the audio file and its transcript together as source-derived evidence. The transcript is an interpretation/extraction of the audio; it is not a substitute for the audio evidence.
8.6 Audio evidence and transcript
8.6 Snapshots — preserved visual evidence
Snapshots are preserved source-derived visual evidence selected for inspection, verification, transition analysis, ambiguity, dispute resolution, or audit. The term is media-neutral and replaces source-specific language such as saved_frames.
The packet snapshot location uses lowercase `snapshot`. Its permitted structure is: `snapshot/manifest.json` (optional), `snapshot/verification/`, `snapshot/objs/`, and `snapshot/disputes/`. These are the only permitted subfolders under `snapshot/`. No nested folders may be created inside any of these folders without explicit authorization. No other snapshot subfolders may be created.
Object snapshots may include a preserved source crop and a separate highlighted analytical crop showing the object boundary or region used for analysis. A highlight is an analytical aid and must never replace or masquerade as the preserved source evidence.
The snapshot manifest, when used, belongs directly in `snapshot/manifest.json`; it is not a packet-root manifest. A manifest is not required merely because snapshots exist.
PC may hold project-wide constants that genuinely apply across scenes, including reusable visual object declarations. PC is also the existing FV structure that may serve as the project canonical object database; this does not create a new object-database layer.
A packet_id is a first-class packet identifier. It must be stable within the merge set and must be carried wherever packet provenance is required.
When a PC file is created for a packet before packet merge, each object ID must remain packet-scoped and traceable: <packet_id>-<object_id>. Do not assign a merged/global canonical object ID before the merge operation. Packet-scoped IDs preserve provenance and allow later identity matching and object-database normalisation.
The purpose of PC object declarations is to prevent repeated object instantiation across scenes or temporal observations when the evidence supports persistent identity. OI records which declared objects are present and their scene-specific state; TD records changes to those persistent identities through time.
9. Packet generation procedure
Assign a stable packet_id before packet contents are generated. Use that packet_id consistently in packet metadata and in packet-scoped object IDs.
9.1 Build the initial inventory
Filesystem discipline: folder structure is part of the operator interface. Do not create folders for organizational convenience. Before creating any folder not explicitly permitted by this specification, ask the operator for permission. No nested folder may be created inside `snapshot/verification/`, `snapshot/objs/`, or `snapshot/disputes/` without explicit permission. Extra folder depth is not a semantic layer and must not be introduced merely to separate artifact types.
Create one candidate record for each potentially meaningful semantic structure.
Resolve candidate identity where evidence permits.
Assign stable packet-scoped IDs. When a PC object declaration is created before packet merge, use the packet ID plus local object ID (for example, PKT-CCTV-001-OBJ-003). Do not prematurely assign a merged/global identity; that is established by packet merge and normalisation.
Separate object identities from component identities.
Record unresolved candidates explicitly.
9.2 Build OI
Create an OI entry for every promoted object/instance.
Add only properties supported by source evidence or explicitly authorized project instructions.
Add declared components only when separately useful to reconstruction.
Record current state and behaviour only where visually supported.
Preserve uncertainty.
9.3 Build MSRM
For each scene/interval, enumerate relevant identities.
Record spatial positions and relationships at supported precision.
Do not invent exact coordinates when the source supports only relative placement.
Keep object inventory separate from background description.
Record scene-specific placements without creating new identities.
9.4 Build TD — the temporal diff log
Create ordered scene/interval records.
Record every meaningful change.
Link each change to an existing canonical identity where continuity is supported.
Mark off-screen/occluded states explicitly.
Do not encode uncertainty as a definite temporal event.
9.5 Lock inventory
Before export, freeze the semantic inventory. After inventory lock:
No new object identity may be introduced by the renderer.
No new component identity may be introduced by the renderer.
A background description does not authorize arbitrary semantic additions.
Uncertainty remains uncertainty.
Missing information may be simplified or omitted; it may not be silently filled with model knowledge.
10. Packet schema and minimal example
10.1 Minimal file set
FV_PACKET/
  README.txt
  PC.json                # optional generally; used when project-wide constants/object declarations are needed
  OI.json                # object/instance information
  MSRM.json              # spatial organization
  TD.json                # temporal data; required for video; owns video observation records
  dispute.json           # required packet-level dispute state and rendering gate
  dispute.reconciled.json # preserved resolution record when a dispute is resolved
  snapshot/              # preserved visual evidence, when needed
    manifest.json        # optional; only here, never at packet root
    verification/        # permitted snapshot subfolder
    objs/                # permitted snapshot subfolder for object evidence
    disputes/            # permitted snapshot subfolder for dispute evidence
  AUDIO_COMPANION.txt    # optional; only when audio is intentionally included
dispute.json is a packet-level flat file, not an OI or MSRM subfile. If no dispute exists, the packet may declare DISPUTES: NONE in its manifest/README instead of carrying an empty dispute file. If any dispute requires human intervention, the dispute file and its evidence references must be present.
FV_PACKET/
  README.txt
  PC.json                # optional generally; used when project-wide constants/object declarations are needed
  OI.json                # object/instance information
  MSRM.json              # spatial organization
  TD.json                # temporal data; required for video; owns video observation records
  dispute.json           # packet-level dispute state and rendering gate
  dispute.reconciled.json # preserved resolution record when a dispute is resolved
  snapshot/              # preserved visual evidence, when needed
    manifest.json        # optional; only here, never at packet root
    verification/        # permitted snapshot subfolder
    objs/                # permitted snapshot subfolder for object evidence
    disputes/            # permitted snapshot subfolder for dispute evidence
  AUDIO_COMPANION.txt    # optional; only when audio is intentionally included
10.2 Minimal OI example
{
  "entities": [
    {
      "canonical_id": "A1",
      "category": "figure",
      "properties": {
        "appearance": "dark coat",
        "orientation": "facing right"
      },
      "components": [],
      "uncertainty": []
    },
    {
      "canonical_id": "C1",
      "category": "capsule",
      "properties": {
        "appearance": "small enclosed vehicle"
      },
      "components": [],
      "uncertainty": []
    }
  ]
}
10.3 Minimal MSRM example
{
  "scenes": [
    {
      "scene_id": "S01",
      "entities": [
        {"id": "A1", "position": "left of center"},
        {"id": "C1", "position": "right of A1"}
      ]
    }
  ]
}
10.4 Minimal TD example
{
  "timeline": [
    {
      "scene_id": "S01",
      "start": 0,
      "end": 9,
      "visible": ["A1", "C1"],
      "off_screen": []
    },
    {
      "scene_id": "S02",
      "start": 9,
      "end": 18,
      "visible": ["A1"],
      "off_screen": ["C1"],
      "changes": [{"id": "A1", "change": "moved"}]
    }
  ]
}
The examples are illustrative schema patterns, not a requirement that every project use these exact property names or coordinate systems. The essential requirement is that the information categories and identity relationships remain explicit and auditable.
11. Backgrounds versus objects
FV must distinguish a background as a visual setting from the semantic object inventory.
This distinction prevents the evaluator from incorrectly classifying every background pixel as an invented object while still testing whether a generator expands a sparse background into a conventional world.
12. Uncertainty and unresolved states
Uncertainty is an explicit state, not a temporary inconvenience to be erased.
An unresolved observation may remain in the observation record without becoming a closed-inventory entity. Evaluators must not turn unresolved source observations into reconstruction failures.
If the unresolved condition materially prevents reliable packet construction, identity resolution, spatial/temporal resolution, or audit, create a packet-level dispute record. The dispute does not replace the unresolved observation; it makes the need for human intervention explicit and traceable.
13. Reconstruction procedure
13.1 Renderer-neutral reconstruction
The reconstruction system receives the locked packet. Its job is to express the packet visually, not to infer a richer world.
Before loading the packet for reconstruction, validate dispute.json as a hard rendering gate. If it is missing, malformed, open, or inconsistent with the packet, stop reconstruction. Continue only when its aggregate status is none or resolved and ordinary packet validation passes.
Load packet and verify schema.
Verify that OI, MSRM, and TD are internally consistent.
Load optional PC constants.
Establish the closed object/component inventory.
For video, establish persistent identity ledger before rendering scene sequence.
Render each scene according to its local membership and spatial instructions.
Apply temporal changes from TD.
Keep off-screen identities persistent rather than deleting/recreating them.
Do not add unspecified semantic objects/components.
Preserve uncertainty where the packet contains uncertainty.
13.2 Missing information
When the packet does not specify a detail necessary to make pixels coherent, the renderer may choose a visually coherent realization that does not create a new semantic entity. This is an appearance-generation allowance, not permission to expand the inventory.
13.3 Renderer limitations
If a renderer cannot reliably execute a packet constraint, record the limitation as an engineering observation. Do not alter the packet to make the renderer appear compliant.
14. Packet-to-renderer prompt compilation
A renderer may require natural-language or other generator-native instructions. That translation is a separate experimental layer.
FV PACKET → LOSSLESS COMPILED SPECIFICATION → RENDERER-SPECIFIC ADAPTER → GENERATOR
14.1 Compiler rules
Preserve all packet identities.
Preserve object/background separation.
Preserve scene membership.
State off-screen persistence explicitly for persistent identities.
Preserve temporal ordering, transitions, and declared state changes.
Do not add adjectives, props, motivations, world-building details, or genre conventions merely to make the prompt sound natural.
Check positive and negative instructions for contradictions before generation.
Keep renderer-specific instructions distinguishable from packet facts.
Keep renderer capability limitations separate from source/packet information.
14.2 Recommended compiled structure
GLOBAL STYLE / PROJECT CONSTANTS
GLOBAL IDENTITY LEDGER
CLOSED OBJECT INVENTORY
CLOSED BACKGROUND INVENTORY
GLOBAL TEMPORAL RULES

SCENE S01
  BACKGROUND
  PRESENT ENTITIES
  OFF-SCREEN / ABSENT ENTITIES
  POSITIONS / RELATIONSHIPS
  ACTION / STATE
  CAMERA / FRAMING
  TRANSITION
  LOCAL ENTITY CLOSURE

SCENE S02
  ...

FINAL CLOSED-WORLD ASSERTION
14.3 Prompt compilation failure classes
15. Reconstruction evaluation
15.1 Independent audit
The evaluator must inspect the generated image/video independently of the generator's explanation.
Check object count and identity continuity.
Check component inventory.
Check scene occupancy.
Check spatial relationships.
Check temporal sequence and state changes.
Check declared behaviour/action.
Check style/appearance constraints.
Check unsupported semantic additions.
Check whether background expansion has occurred.
Record every nontrivial deviation with evidence.
15.2 Scene occupancy accounting
Never force an ambiguous candidate into an existing identity simply to make counts close.
16. Failure taxonomy
17. Evidence-grade failure reporting
Disputes are not limited to renderer failures. A dispute may be raised whenever the AI cannot reliably determine the correct visual representation. The minimum dispute linkage should include dispute_id, source/evidence reference, affected OI/MSRM/TD record where applicable, problem description, attempted resolution, status, and human_action_required.
For generated or re-rendered images, preserve the disputed output and the relevant source snapshot(s) when the AI cannot reliably read, compare, or explain an object or visual structure. The strange result is evidence of the dispute, not permission to invent a correction.
Do not promote an evaluator's uncertain observation into a formal failure until supporting evidence is located.
18. Model-knowledge containment test
FV should actively test whether a renderer imports knowledge about what a scene category normally contains.
Create a deliberately sparse packet.
Choose a category that strongly predicts common but undeclared objects.
Render it.
Audit every semantic addition separately.
Repeat with a richer packet.
Compare whether omitted structure is systematically filled by the renderer.
The relevant mechanism is model-knowledge expansion of the supplied representation, not merely generic 'hallucination'.
19. Temporal identity stress test
Declare one persistent identity.
Place it at A in scene 1.
Place the same identity at B in scene 2.
Place the same identity at C in scene 3.
Make the environment visually rich enough that previous locations remain tempting.
Score movement, disappearance/reappearance, duplication, and identity continuity separately.
This test isolates whether a renderer treats sequential spatial requirements as movement of one identity or as permission to spawn additional instances.
19.1 Temporal queryability check
For every video packet, test whether TD supports at least the following classes of query at its recorded precision: (a) state-transition time; (b) event ordering; (c) elapsed interval between changes; (d) temporal overlap; (e) entry/exit timing; and (f) changes within a specified time window. A failure to answer must be reported as missing/insufficient TD, not repaired from world knowledge or from assumptions about the source.
20. Complete image-analysis checklist
☐ Source metadata and limitations recorded.
☐ Whole image inspected before local interpretation.
☐ Boundaries/regions/contours identified.
☐ Candidate structures recorded.
☐ Observation separated from semantic hypothesis.
☐ Components separated from appearance phenomena.
☐ Object/instance candidates identified.
☐ Identity decisions supported by evidence.
☐ Uncertain candidates retained as unresolved where necessary.
☐ OI built from promoted entities only.
☐ MSRM built from observed spatial relationships.
☐ Inventory locked before reconstruction.
☐ Packet internally validated.
☐ Packet exported with README and required files.
21. Complete video-analysis checklist
☐ Source metadata and limitations recorded.
☐ Scene/interval boundaries identified.
☐ Sampling concentrated around meaningful changes.
☐ Candidates tracked across time.
☐ Persistent identities assigned with continuity evidence.
☐ Movement distinguished from duplication.
☐ Occlusion distinguished from deletion.
☐ Off-screen persistence represented.
☐ Entry/exit recorded.
☐ State and behaviour changes recorded.
☐ OI/MSRM/TD cross-checked.
☐ Temporal ordering validated.
☐ Inventory locked.
☐ Uncertainty preserved.
☐ Packet exported and independently audited.
22. Complete reconstruction checklist
☐ Packet schema verified.
☐ Closed object/component inventory established.
☐ Persistent identity ledger loaded.
☐ Scene occupancy loaded.
☐ Background inventory kept separate.
☐ Temporal rules loaded.
☐ No semantic additions used to solve rendering difficulty.
☐ Off-screen identities remain persistent.
☐ Movement does not create duplicates.
☐ Generated result independently audited.
23. Packet integrity checklist
☐ Dispute status is explicit in dispute.json: none, open, or resolved; rendering is allowed only for none or resolved.
☐ Every dispute references valid source/evidence locations or snapshots.
☐ Every dispute requiring human intervention is marked human_action_required.
☐ Dispute records preserve unresolved state rather than silently converting it to certainty.
☐ Snapshot references resolve to preserved evidence where retention is required.
☐ dispute.json aggregate status matches the individual dispute records.
☐ AI reprocessing is complete and validation passed before dispute.json may become resolved.
☐ Resolved disputes have dispute.reconciled.json preserved.
☐ Human resolution is preserved separately from AI reprocessing.
☐ Open disputes block rendering.
☐ Every dispute has issue, source/affected record, snapshot_ids, resolution_status, resolved_by, and resolution_remark fields.
☐ Every OI identity is uniquely identifiable.
☐ Every OI component belongs to a declared identity.
☐ Every MSRM reference points to a valid identity/background.
☐ Every TD identity points to a valid persistent identity.
☐ No scene references an undeclared identity.
☐ Video packets contain TD; packets without TD are not treated as video reconstruction targets.
☐ No identity has contradictory simultaneous states without explicit uncertainty.
☐ Object and background inventories remain distinct.
☐ Uncertainty fields are not silently converted to certainty.
☐ Required files are present.
☐ If audio is included, the source audio file and transcript.json are present and mutually traceable.
☐ README records source, packet purpose, version/format, and known limitations.
24. Practical operator template
24.1 Image job
INPUT
  Source image:
  Source ID:

OBSERVATION
  Global visual structure:
  Candidate list:
  Evidence locations:
  Uncertainties:

ENTITY RESOLUTION
  Object/instance IDs:
  Component IDs:
  Appearance-only features:
  Unresolved candidates:

PACKET
  OI:
  MSRM:
  PC (if applicable):

VALIDATION
  Inventory closed?:
  Packet internally consistent?:
  Evidence trace complete?:

OUTPUT
  FV packet:
  README:
  Audit record:
  Disputes: packet-level dispute.json if required
  Snapshots: preserved evidence, including verification/ where required
24.2 Video job
INPUT
  Source video:
  Source ID:
  Duration:
  FPS:
  Dimensions:

TEMPORAL ANALYSIS
  Scene/interval list:
  Key frames:
  Candidate identities:
  Continuity evidence:
  Entry/exit:
  Occlusion/off-screen:
  State changes:

PACKET
  OI:
  MSRM:
  TD:
  PC (if applicable):

VALIDATION
  Identity ledger closed?:
  Scene occupancy closed?:
  Temporal order consistent?:
  Uncertainty preserved?:

OUTPUT
  FV packet:
  Evidence record:
  Audit record:
25. End-to-end procedure
Receive image/video and establish source identity.
Record source limitations.
Inspect the source before semantic commitment.
Create observation records and evidence locations.
Generate candidates from visible structure.
Resolve object/component/appearance status.
Resolve identities while preserving uncertainty.
For video, establish scenes/intervals and temporal continuity.
Build OI.
Build MSRM.
Build TD for video.
Add PC only for genuine project-wide constants.
Cross-check packet references.
Lock the closed inventory.
Export the packet.
If reconstructing, compile the packet into a lossless renderer specification.
Apply renderer-specific syntax without adding semantic content.
Validate compiled specification against packet.
Generate reconstruction.
Independently audit the generated result.
Attach evidence to every nontrivial failure claim.
Classify deviations.
Keep renderer limitations separate from packet errors.
26. Worked miniature example: sparse image
Suppose the source image shows a person, a rectangular box, and a dark irregular patch on the floor. The patch resembles a bag but its boundaries are ambiguous.
Record person and box as candidates with visible evidence.
Record the dark patch as an unresolved candidate; do not call it a bag merely because bags are common near people.
If the patch cannot be established as a semantic object, it does not enter the closed object inventory.
Represent the person and box in OI and their relative positions in MSRM.
Record the unresolved patch in the observation/audit record.
Lock inventory with person + box only.
A renderer may reproduce a dark floor appearance if needed for visual coherence, but it may not introduce a semantic bag.
27. Worked miniature example: persistent video identity
Suppose one figure appears in scene S01 on the left, disappears during a hard cut, and appears in S02 on the right.
Create one candidate lineage from S01 and S02 if continuity is supported by the declared test/source.
Assign one canonical identity, e.g. A1.
Record S01 membership and left position in MSRM.
Record S02 membership and right position in MSRM.
Record the scene transition and continued identity in TD.
Do not create A2 merely because A1 occupies a different position.
If continuity cannot be established, mark the identity relationship unresolved rather than inventing certainty.
27.1 Worked miniature example: temporal query from TD
Suppose a video contains a traffic light. OI declares traffic_light_01. MSRM records its location relative to the road and other entities. TD records: 00:14.2→00:14.6, traffic_light_01.color = yellow→green. A packet query asking 'When did the traffic light turn green?' is answered from TD as approximately 00:14.6. A query asking whether a pedestrian began crossing before or after the change can be answered by comparing the pedestrian's corresponding TD event with the light transition. If the packet contains no such transition, the answer remains unknown.
28. What this specification does not assume
It does not require bounding boxes.
It does not require ControlNet.
It does not require masks, reference-image conditioning, compositing, latent object slots, or deterministic layout controls.
It does not assume that every visual representation is a photograph-like stored image.
It does not assume that object names must precede structural representation.
It does not assume that a generator's explanation is evidence of what its output contains.
Specific engineering interventions may be tested later when a failure mechanism has been characterized.
29. Distinguishing three kinds of correctness
These must not be collapsed. A generator failure may actually be a packet error or a prompt-compilation error. Conversely, a correct packet and correct compiled prompt can still produce a failed reconstruction.
30. Final acceptance test
29.1 Packet merge identity test
When multiple packets describe temporally adjacent material from the same source/world, merge must compare packet-scoped object declarations rather than assuming local IDs are globally identical. The merge process must preserve source packet provenance, test continuity and visual evidence, and only then establish a normalised persistent object identity.
The specification passes only when an unfamiliar AI can use it as an executable process rather than merely as a description of FV.
Give the AI one image and this document. Ask for a complete FV packet.
Inspect whether it knows what to observe, what to record, how to resolve candidates, how to construct OI/MSRM, and how to validate the result.
Give the AI one video and this document. Ask for a complete packet including TD and persistent identities.
Inspect whether it can distinguish movement, occlusion, off-screen absence, and new instances.
Give the AI a valid packet and this document. Ask it to compile and reconstruct.
Inspect whether the compilation preserves packet semantics and whether the renderer is prevented from importing undeclared world knowledge.
Ask the AI to justify every material packet assertion with source evidence.
Any undocumented step that the AI must be taught separately is a specification gap.
30.1 Additional acceptance test: temporal queryability
Give an unfamiliar AI a valid video packet and ask temporal questions whose answers are explicitly encoded in TD, such as 'When did the light turn green?' The AI must retrieve the answer from TD rather than infer it from OI, MSRM, the scene category, or external world knowledge. Then ask a question whose answer is not encoded. The AI must report insufficient temporal information rather than fabricate an answer.
31. Working principle
Faking Vision is not trying to make a renderer produce a plausible world. It is trying to determine whether a renderer can produce the supplied world without quietly replacing the supplied representation with its own.
Ground-up operational specification. Further changes should be made by testing this document against unfamiliar AI instances, not by adding sections merely because a later conversation exposed a missing paragraph.
32. Adaptive Temporal Decomposition (ATD)
FV video analysis must not use a predetermined sampling rate as its fundamental temporal model. Temporal resolution is determined by the evidence required to represent the visual sequence adequately.
Adaptive Temporal Decomposition (ATD) recursively subdivides a temporal interval when the current representation cannot adequately account for what occurs within that interval. The process continues only where additional temporal resolution is justified by observable structure, identity continuity, spatial relationships, state changes, or uncertainty.
32.1 Frame versus temporal interval
A frame is source evidence at a particular instant.
An observation interval is the basic temporal representation unit.
A temporal leaf is an interval that can currently be represented without material loss of relevant evidence.
An unresolved interval is subdivided for further observation.
TD records the resulting ordered temporal structure, transitions, state changes, and uncertainty.
32.2 Recursive temporal procedure
Establish the temporal extent of the source and identify obvious hard scene/tableau boundaries.
Create an initial interval covering each coherent temporal region.
Observe interval endpoints and interior evidence sufficient to test whether one FV state can represent the interval.
Compare structured state rather than relying on global pixel difference alone.
If the interval is adequately represented, retain it as a temporal leaf.
If it is unresolved, subdivide it into ordered subintervals and repeat the test.
Preserve the source frames needed to inspect unresolved intervals and important transitions.
32.3 Interval-resolution test
An interval is unresolved when the available evidence cannot safely be represented as one temporally consistent FV state. The test considers:
visual difference that materially changes the represented scene;
object or boundary difference, including appearance, disappearance, splitting, merging, or altered boundaries;
persistence and identity continuity;
spatial relationship changes such as contact, separation, occlusion, ordering, containment, or relative movement;
observable state, behaviour, facing, direction, expression, or component-state changes;
uncertainty about whether a material change occurred or which identity/relationship is involved.
Large pixel change is not required for subdivision, and small pixel change is not sufficient to declare an interval stable. A local event can require finer temporal resolution even when most of the frame is unchanged.
32.4 No fixed-rate shortcut
Statements such as 'sample every N frames' or 'sample every X seconds' may be used for an engineering pre-pass or comparison experiment, but they are not the FV temporal model. An implementation that merely subdivides every interval to a predetermined minimum duration is also not considered evidence-driven ATD.
32.5 Entity continuity during ATD
Temporal subdivision must not itself create or destroy identity. Provisional entities should be associated across neighboring intervals using multiple observable cues where available:
position and bounding geometry;
motion and co-motion consistency;
shape, area, and appearance continuity;
boundary continuity;
pairwise spatial relationships;
occlusion and reappearance evidence.
If continuity cannot be established, preserve the ambiguity. Do not manufacture a new identity merely because an interval boundary was introduced.
32.6 Temporal relationship evidence
Changes in relationships are first-class temporal evidence. Examples include near→farther, separate→contact, beside→separated, visible→occluded, following/co-moving→independent motion, and outside→inside. MSRM remains responsible for spatial relationships; TD records how those relationships change through time.
32.7 Temporal maplet
A retained temporal leaf may be represented as a bounded temporal maplet: a time range linked to the relevant OI/MSRM state, transition evidence, and uncertainty. This is a representation concept, not a replacement for OI, MSRM, or TD.
32.8 Temporal evidence retention
Where temporal evidence cannot be resolved confidently, retain the relevant source frames as snapshots and create a packet-level dispute when human intervention is required. Snapshot retention does not itself imply that every frame is archived.
Retain evidence around state transitions.
Retain evidence around identity ambiguity and occlusion.
Retain evidence around important relationship changes.
Retain evidence where later observations promote or refine an object/component.
Do not retain every frame simply because a fixed-rate policy selected it.
32.9 Updated video-analysis checklist
☐ Temporal resolution was determined from evidence rather than a fixed sampling rate.
☐ Candidate intervals were recursively subdivided only where the current representation was unresolved.
☐ Interval stability was tested using structured visual state, not global pixel difference alone.
☐ Object continuity and relationship continuity were considered.
☐ Movement, occlusion, off-screen absence, and new instances remain distinct.
☐ Temporal boundaries do not create new identities.
☐ TD records the resulting temporal order and changes at the precision actually supported.
☐ Important transition/ambiguity evidence was retained.
32.10 Perturbation-driven adaptive sampling
ATD should allocate temporal observation effort according to the observed rate and concentration of visual perturbation. The default mode is a lazy scan. A temporal-difference cluster detected within a coarse interval is a trigger to increase local sampling density. The affected interval is subdivided and sampled more frequently; if perturbation persists or becomes denser, subdivision may continue. When perturbation falls below the criterion for further attention, the sampler may return to the coarser rate.
The initial video division is an engineering search structure, not a fixed temporal resolution. A merge-sort-like strategy may be used: divide the source into length-dependent chunks, inspect representative points and boundaries, then recursively subdivide only chunks or subintervals containing evidence of unresolved temporal change.
Sampling effort should therefore behave approximately as: quiet interval → low observation density; emerging perturbation → increased density; sustained/high perturbation → higher density; perturbation subsides → reduced density. The exact rates are implementation parameters to be empirically calibrated, not FV constants.
If an explicit task objective is supplied by the experiment, it may alter sampling priority. The task objective is an external analysis instruction, not source evidence. It may specify what to track or investigate, but it must not supply identities, events, motivations, or missing temporal facts. Goal-directed sampling and evidence acquisition remain separate.
CP, EY, and change-generator identity serve different functions: SCP/CCP control where attention is directed; EY records what evidence is actually being produced; change_generator_obj_ids records the supported source relationship responsible for propagation. They must not be collapsed into one score.
Incongruity may be recorded when an initially low expected change state produces unexpectedly meaningful evidence. Operationally, this is an expectation/observation mismatch that warrants additional investigation; it is not an object identity and must not be used to manufacture one.
EY should describe what meaningful evidence the object or region is producing now relative to its prior observations. It may contain movement, boundary change, displacement, interaction, emergence, disappearance, or other source-grounded evidence. EY does not itself identify the cause.
EY = { current: <current evidence/state>, frameid: <source frame>, previous: [<earlier evidence records>] }
Evidence Yield (EY) is a temporal evidence record, not a scalar importance score. For an object or region, represent EY as a current observation linked to its source frame and a history of previous observations. Minimum conceptual structure:
When a change propagates through multiple objects, the directly affected object may become a subsequent change generator. Preserve the observed propagation chain where evidence supports it, for example: generator A → affected object B → subsequent generator B → affected object C. Do not invent a complete causal graph when only part of the chain is observable.
For propagation events, TIR should record change_generator_obj_ids: the persistent object IDs that source-grounded evidence identifies as generating or transmitting the current perturbation. The field identifies an evidence relationship; it is not inferred merely because an object has high CCP.
Current Change Propensity (CCP) is the present change-priority state after incorporating current observations, interactions, and propagation. CCP may rise or fall as the scene evolves. An object's CCP may change substantially while its SCP remains unchanged.
Static Change Propensity (SCP) is the baseline propensity assigned to an object from its observable or explicitly supplied characteristics before the current event develops. SCP is persistent during the analysis unless the experiment explicitly defines a recalibration procedure. A low SCP object is not discarded; lazy scanning remains responsible for the rest of the scene.
Adaptive temporal sampling may use Change Propensity (CP) as an attention-prior mechanism. CP is not a source fact and must not be treated as an importance score or as observed change. Its purpose is to provide a shortcut for deciding what to look at first when attention is limited.
32.10.1 Change Propensity, Current Change, and Change Generators
32.11 Temporal timestamps are index metadata
A source timestamp, frame number, or derived source-time coordinate is temporal index metadata attached to an observation or TD record. It is not itself a visual object and must not be promoted or repeatedly represented as scene content merely because its displayed value changes from frame to frame.
If the source contains a visually displayed CCTV timestamp, that timestamp is visual evidence and should be read from the relevant source frame or snapshot only when the question requires it. The machine temporal coordinate and the visually displayed timestamp are distinct fields.
35. Change log — v0.11
• Refined Adaptive Temporal Decomposition to explicitly support perturbation-driven adaptive sampling: lazy scanning by default, increased local sampling around TD clusters, recursive subdivision while perturbation persists, and relaxation when it subsides.
• Added a merge-sort-like chunking strategy as an implementation pattern for locating temporal perturbations efficiently without making fixed-rate sampling the FV model.
• Clarified that sampling density is a dynamic implementation parameter driven by observed perturbation rate/concentration and must be empirically calibrated.
• Clarified that frame numbers and source timestamps are temporal index metadata, not visual objects; displayed CCTV timestamps remain source visual evidence and are inspected only when needed.
33. Change log — v0.9
34. Change log — v0.10
• Added packet-level DISPUTES flat file for cases where automated analysis cannot reliably resolve what is present or how it should be represented and human intervention is required.
• Added SNAPSHOTS as the media-neutral name for preserved visual evidence, replacing saved_frames terminology.
• Added verification/ as a possible snapshot subfolder for evidence retained specifically to resolve uncertainty or disputes.
• Clarified that disputes may originate from OI, MSRM, TD, observation, source, or reconstruction/audit while remaining visible at packet level.
• Clarified that disputed visual evidence is preserved as-is and that human resolution must not silently rewrite the original automated observation.
Added Adaptive Temporal Decomposition (ATD) as the general FV temporal-analysis model.
Defined the observation interval as the basic temporal representation unit; frames remain source evidence.
Replaced fixed-rate temporal resolution as the conceptual basis of video analysis.
Defined recursive subdivision of unresolved intervals.
Added structured temporal tests for visual, object/boundary, persistence, relationship, state, and uncertainty changes.
Added entity-continuity requirements during temporal subdivision.
Made relationship changes first-class temporal evidence.
Defined the temporal maplet concept.
Clarified that merely subdividing to a predetermined minimum duration is not evidence-driven adaptation.
32.12 Moving-camera perturbation
A moving camera is itself a source of temporal perturbation. High temporal-difference density may arise from the camera sweeping past otherwise static world structure. FV must not automatically interpret this as object motion or as independent new entities. Transient visual structures that enter, traverse, and leave the field of view remain observations and may be information-bearing even when persistent identity is not established.
32.13 Perturbation-density compression
Adaptive temporal decomposition can compress a dense temporal-difference stream into a smaller set of evidence-bearing snapshots while retaining the temporal structure needed to locate materially relevant perturbations. Snapshot count alone is not the measure of success. Reconstruction experiments should compare source TD behavior, retained FV evidence, and reconstructed-output TD behavior.
32.14 Reconstruction as an experimental test
FV reconstruction experiments may intentionally use crude or ugly renderers. Aesthetic quality is not an acceptance criterion. The first question is whether the packet plus retained snapshots can regenerate the temporal and visual structure represented by FV. Generated intermediate imagery is not source evidence unless supported by the FV packet. Every generated reconstruction should be independently FV-audited.
32.15 Experimental material selection
FV experiments do not require prestigious, large, or specialized datasets. For exploratory work, prefer small, directly accessible material that permits rapid observation, modification, reconstruction, and failure analysis. Dataset prestige and scale are not FV requirements.
Change log — v0.12
• Added moving-camera perturbation as a general temporal consideration.
• Added perturbation-density compression as an experimental concept.
• Added deliberate ugly reconstruction as a valid experimental method.
• Added independent FV audit of reconstructed outputs.
• Added guidance to prefer small, directly accessible experimental material.
Change log — v0.13
Replaced the legacy DISPUTES.flat concept with structured dispute.json.
Made dispute.json a required packet-level rendering gate with aggregate status none, open, or resolved; rendering is permitted only for none or resolved.
Added structured dispute fields including issue, source/affected record, snapshot_ids, resolution_status, resolved_by, resolution_remark, human_action_required, timestamps, and AI reprocessing state.
Added dispute.reconciled.json as the preserved resolution record.
Added the required human-resolution → AI-reprocessing → packet-validation lifecycle.
Clarified that human resolution does not directly repair the packet; AI must reprocess the packet and update affected OI/MSRM/TD or observation records before the dispute can be cleared.
Added rendering-gate and packet-integrity checks for dispute state and reprocessing completion.
Change log — v0.14
Added PC as an optional canonical object-database use without changing the existing PC structure.
Added an additive snapshot property for PC object declarations to provide preserved visual grounding.
Clarified that object-database use, packet merge, and object-database normalisation remain experimental goals requiring continuous same-camera temporal material for validation.
Change log — v0.15
• Added filesystem discipline requiring operator permission before creating unlisted folders.
• Added support for highlighted analytical object snapshots while preserving the original source evidence separately.
• Defined the lowercase snapshot/ structure: optional manifest.json plus verification/, objs/, and disputes/, with no nested folders without explicit permission.
• Made packet_id a first-class provenance identifier.
• Required packet-scoped PC object IDs in the form <packet_id>-<object_id> before packet merge.
• Clarified PC as the existing canonical object-database structure and its role in preventing repeated object instantiation.
• Made TD the owner of video observation records; no separate observation.json/observations.json is required.
Information should be promoted from TIR into TD only when the evidence supports the corresponding official temporal statement. Provisional reasoning should remain distinguishable from committed packet facts.
TIR is therefore not a temporary or inferior version of TD. It is the record of the investigation from which the official TD record is derived. The AI may use TIR freely as an analytical workspace and may revise, extend, or contradict provisional entries as new evidence is acquired.
• TD.json is the official temporal record. It contains the evidence-grounded temporal information committed to the FV packet.
• TIR is the investigation record. It may contain rich observations, measurements, hypotheses, competing interpretations, intermediate conclusions, sampling decisions, rejected hypotheses, and unresolved questions.
TIR is distinct from TD.json:
TIR is the persistent investigation record used during temporal analysis. It replaces the implementation-oriented name TEMP_TD.
TIR — Temporal Investigation Record
17.18 Multi-pass temporal analysis and TIR
Adaptive Temporal Decomposition may use multiple analysis passes before deciding which observations to retain. The passes serve different purposes and must not be confused with a fixed sampling rate.
17.18.1 Initial global interval for long video
For a video longer than one minute, an implementation may use an initial global temporal interval of 4 seconds as an engineering starting point.
Let L = video duration; I = 4 seconds; and a = ceil(L / I), the number of global interval positions. The 4-second value is an implementation parameter, not an FV constant. It is a starting probe whose adequacy must be evaluated empirically.
17.18.2 Random reconnaissance pass
Before or alongside the normal global pass, the AI may perform an independent random reconnaissance pass. Set r = ceil(a / 2). Generate r unique random temporal positions across the video, subject to the experiment's sampling-coordinate rule.
In the current implementation, random reconnaissance positions are selected from odd-numbered temporal positions so that they are distinct from the even-position global sampling structure. Random positions must be non-duplicate and bounded by the actual video duration. If an adaptive candidate would otherwise reuse a random observation, select another unsampled coordinate.
Each random observation is analysed and its temporal evidence is accumulated in TIR. The random reconnaissance TD is an in-memory analysis resource during the run; it does not need to be exported as a separate file.
Random reconnaissance is not itself the final temporal representation. Its purpose is to provide an independent view of where temporal activity, object/action changes, transitions, or uncertainty may occur.
17.18.3 Normal global pass
Run the global temporal sequence using the current initial interval: 0, 4, 8, 12, 16, ... At each interval, compare the observations and update TIR. The global interval is therefore a default observation stride, not a claim that nothing meaningful occurred between its endpoints.
17.18.4 TIR is the active temporal analysis workspace
During video analysis, maintain a rich temporary temporal-data structure (TIR) that may contain substantially more information than the final TD packet schema.
TIR may contain, as applicable: temporal observations and source coordinates; global visual change; local/regional visual change; object appearance/disappearance; object movement; object action or apparent action; object pose, orientation, direction, or state change; object identity continuity and ambiguity; object-to-object relationship changes; contact, separation, following, containment, occlusion, and co-motion; camera movement, pan, tilt, zoom, and reframing; affected spatial regions; persistence and transition evidence; local activity baselines; hypotheses and intermediate conclusions; evidence supporting or contradicting a conclusion; uncertainty; reasons an interval does or does not require further observation; and relationships between observations from different passes.
TIR is an analytical scratchpad, not a restricted scalar TD score. The AI should use it to form meaningful temporal conclusions and to decide where additional evidence is useful.
The final TD record is a structured, evidence-grounded representation derived from the analysis. TIR may therefore be richer, messier, and more exploratory than exported TD.
17.18.5 TD dimensions for adaptive decisions
Adaptive decisions should consider multiple forms of temporal evidence rather than a single pixel-difference value: visual change; object/boundary change; object movement; object action; persistence/identity continuity; spatial relationship change; state change; camera/framing change; spatial concentration of change; and uncertainty or insufficient temporal evidence.
Object change and object action are temporal evidence even when whole-frame visual difference is modest. Conversely, large whole-frame change caused by camera motion must not automatically be treated as object-level activity.
Any externally supplied task objective and the sampling-priority consequences of that objective, kept separate from source evidence.
Incongruity records where observed evidence departs materially from the current expectation and triggers further investigation.
Evidence Yield (EY) records using current evidence, source frame ID, and previous evidence history.
Change-generator relationships, including change_generator_obj_ids and affected object IDs where supported.
Change Propensity records: static change propensity (SCP) and current change propensity (CCP), with their evidential basis or provisional status.
17.18.6 Global versus local TD
TIR should distinguish global temporal change from local/regional temporal change where the evidence permits. Global TD describes change distributed across much or all of the frame. Local TD describes change concentrated in one or more spatial regions.
A frame-wide perturbation may indicate camera movement, zoom, reframing, lighting change, or a genuinely global scene change. A concentrated perturbation may indicate object movement, action, appearance/disappearance, occlusion, or a local state/relationship change. This distinction is an analysis aid, not an automatic semantic classification.
17.18.7 Local baseline
Where useful, TIR should maintain a slowly updating local activity baseline for a region or temporal stretch. Adaptive significance should be judged relative to recent local behaviour when possible, rather than only against a single fixed global threshold.
A continuously busy region should not trigger unlimited subdivision merely because its absolute TD remains high. A sudden departure from that region's recent behaviour should receive greater attention. A local baseline is provisional evidence and must be updated as new observations arrive.
17.18.8 Adaptive insertion
When the current global interval contains unresolved or materially significant temporal evidence, insert an additional observation.
The default insertion point is the midpoint of the interval. Midpoint selection is intentional: the global temporal positions and the random reconnaissance positions use different coordinate parity in the current implementation, so midpoint insertion normally supplies an observation that has not already been sampled.
If an alternative insertion point is considered, first check whether that temporal coordinate has already been sampled. Never duplicate an existing observation merely because a different pass discovered the same coordinate. The midpoint is an evidence-acquisition convenience, not a claim that the true event boundary lies at the mathematical midpoint.
17.18.9 Meaningful adaptive conclusions
TIR should be used to make temporal conclusions before requesting further observations. Examples include: an object persists while changing location; a person/object begins or ends an action; camera movement explains frame-wide change; a localized change warrants object-level inspection; an object becomes occluded and later reappears; a relationship changes while participating objects remain present; a transition appears within an interval but its timing is unresolved; or an interval contains insufficient evidence to distinguish competing temporal explanations.
The answer to 'why sample here?' should therefore be a conclusion about the source evidence or unresolved temporal structure, not merely 'because the threshold was exceeded.'
17.18.10 Minimum-width investigation
An implementation may define a minimum temporal width for a specific hot interval when precise transition localization is required. Activity magnitude and interval width answer different questions: activity evidence determines whether an interval deserves deeper investigation; minimum width determines when the investigation has reached the desired temporal resolution.
A minimum width must not be applied uniformly to every interval. Quiet intervals remain on the global lazy scan. A hot interval may continue to be subdivided until its temporal width is sufficiently small for the question being analysed or the available source evidence reaches its limit.
17.18.11 Random reconnaissance refresh
The initial random reconnaissance pass is primarily a triage mechanism. It does not automatically need to be repeated after every adaptive subdivision. However, if a region becomes sufficiently complex or uncertain that the original reconnaissance evidence is no longer informative, a local reconnaissance pass may be performed and recorded in TIR.
17.18.12 Pass interaction
The passes are complementary: random reconnaissance provides independent temporal evidence; the 4-second global pass provides systematic coverage; adaptive investigation follows conclusions from TIR. No single pass is independently authoritative.
Change log — v0.17
Added a multi-pass temporal-analysis procedure combining an optional random reconnaissance pass, a long-video 4-second global starting interval, and evidence-driven adaptive insertion.
Defined TIR as a rich in-memory temporal-analysis scratchpad that may contain observations, object/action changes, relationships, camera changes, regions, uncertainty, hypotheses, and intermediate conclusions before final TD export.
Added object change and object action as explicit temporal evidence.
Added global-versus-local TD distinction to help separate camera/framing perturbation from concentrated object-level change.
Added a provisional local activity baseline for adaptive significance.
Clarified midpoint insertion and sampling-coordinate uniqueness.
Added optional minimum-width investigation for specifically hot intervals without turning minimum width into a global fixed-rate sampler.
Clarified that random reconnaissance is independent evidence/triage rather than the final temporal representation, and may be locally refreshed when initial evidence becomes stale.
Change log — v0.17
Renamed the temporal investigation workspace from TEMP_TD to TIR (Temporal Investigation Record).
Defined TIR as a persistent investigation record distinct from the official TD.json.
Clarified that TIR may retain rich, provisional, contradictory, exploratory, and rejected temporal reasoning while TD contains committed, evidence-grounded temporal information.
Clarified that TIR is the source/workspace for deriving the official TD record, not a temporary copy of TD.
• Clarified that transcript claims may identify potential gaps and trigger adaptive sampling before the claims are visually supported.
• Separated transcription fidelity from cross-modal visual support in cumulative audio/transcript assessment.
• Added explicit distinction between transcript errors, unresolved content, and commentary that is temporally/contextually displaced from the visual scene.
• Added cumulative transcript assessment so isolated transcription/interpretation errors do not automatically invalidate the audio channel.
• Defined the transcript as a sampling cue rather than a source-of-truth record.
• Defined transcript generation as an early provisional analysis step before the initial temporary TIR/TD temporal investigation.
Change log — v0.20
Change log — v0.19
• Replaced the previous dispute-resolved.json resolution model with the dispute reconciliation workflow.
• Defined dispute.json as the small current actionable/rendering-gate state when reconciliation is complete.
• Defined dispute.reconciled.json as the preserved detailed dispute/reconciliation history after all disputes are resolved.
• Clarified that unresolved disputes keep dispute.json in place and only its aggregate status is changed to open.
• Defined human intervention as packet enrichment/correction followed by AI reconciliation, with OI and PC updated from the returned packet and supporting evidence.
• Added optional packet-level audio evidence with the source audio file and timestamped transcript.json.
• Clarified that transcript text is an interpretation of audio and does not replace the audio source evidence.
Change log — v0.22
Added Change Propensity as a temporal-analysis attention prior, separating Static Change Propensity (SCP) from Current Change Propensity (CCP).
Added change_generator_obj_ids and explicit propagation relationships so current change can be traced from a source object through affected objects.
Defined Evidence Yield (EY) as a structured temporal evidence record with current, frameid, and previous history rather than a scalar score.
Added operational incongruity as an expectation/observation mismatch that can trigger further investigation.
Clarified that explicit task objectives may alter sampling priority but are external instructions, not source evidence.
Added the requirement to keep CP, EY, and change-generator relationships distinct.
Change log — v0.23
Added component-driven candidature and verification: component → candidate set → targeted search for expected components/relationships → verification or rejection.
Defined component candidature as an evidence-preserving alternative to immediate whole-object recognition.
Added required candidature/verification fields for observed components, candidate alternatives, discriminating components/relationships, search results, and promotion/rejection status.
Clarified that later whole-object recognition must not retroactively rewrite the earlier evidence path.
Connected component emergence and behaviour to adaptive temporal sampling and behaviour-triggered component tracking where the component materially affects identity, relationship, or uncertainty.
### Change log — v0.24
• Added ambiguous TIR correspondence/identity handling across multiple investigated media.
• Added component-quality labels: high, weak, and transient.
• Added provisional correspondence wording and discriminating-component search for identity resolution.
• Clarified that unobserved expected components are not negative evidence when the view is uninformative or occluded.

Test | Input | Required output | Pass condition
A — Image analysis | This specification + image | FV packet + observation record | AI can produce the packet without undocumented FV instructions.
B — Video analysis | This specification + video | FV packet including temporal structure | AI can establish scene structure, identities, changes, and uncertainty without being taught the missing procedure.
C — Reconstruction | This specification + FV packet + generator | Image/video reconstruction attempt | AI uses packet as source of truth and does not add semantic content.
D — Traceability | Source + generated packet | Evidence map | Each material packet assertion can be traced to source evidence or explicitly marked inference/uncertainty.
E — Packet audit | Packet alone | Validation report | AI can identify structural contradictions, missing required fields, and inventory problems.


Layer | Question | Allowed operation
Source | What is visually present/changeable? | Acquire and inspect the source.
Observation record | What did the analyst actually observe? | Record visible structure, evidence, uncertainty, and candidates.
FV packet | What information is authorized for reconstruction? | Resolve entities/relationships/temporal structure and lock inventory.
Compiled renderer specification | How is the packet expressed to a particular generator? | Translate syntax while preserving packet semantics.
Generated result + audit | Did the renderer reproduce the packet? | Inspect output and classify deviations with evidence.


Field | Meaning
candidate_id | Temporary identifier before entity resolution.
visual_evidence | What is actually visible: shape, boundary, attachment, texture, relative position, etc.
extent | Approximate image region if useful.
relationships | Observed spatial relationships to other candidates/regions.
semantic_hypothesis | Possible interpretation, if useful.
confidence | High / medium / low.
ambiguity | What alternative interpretations remain.
evidence_location | Image region or coordinate reference.


Field | Required content
canonical_id | Stable identity used across the packet.
candidate lineage | Observation records associated with the identity.
scene membership | Scenes/intervals in which it is visible.
visibility state | Visible, occluded, off-screen, or unresolved.
entry/exit | Observed entry into or exit from the visible field.
state changes | Pose, orientation, location, behaviour, appearance, or other declared changes.
continuity evidence | Evidence connecting appearances.
duplication flag | Raised when one identity appears to have multiple simultaneous instances.


Event | Meaning | Default interpretation
Movement | Same identity changes location. | Update MSRM/TD; do not duplicate.
Occlusion | Same identity is temporarily hidden. | Identity persists.
Off-screen absence | Identity is not visible in the current framing/scene. | Identity persists unless source establishes otherwise.
New instance | Evidence supports a distinct additional identity. | Create a separate identity.


Field | Example
observation_id | OBS_014
source_id | IMG_001 / VID_002
time/frame | 00:12.4 / frame 298
region | upper-left; approximate coordinates
visual description | elongated bounded form attached to candidate A
candidate_id | C07
interpretation | possible branch
confidence | medium
alternatives | shadow / branch
packet disposition | unresolved; not promoted as object
evidence reference | frame 298 crop / image region


Case | Correct treatment
Painted lunar landscape is declared as background | Background content may be reconstructed within the declared description.
A rock is separately declared as an object | Rock is part of the closed object inventory.
Background says 'cratered ground' | Crater appearance is not automatically a new object inventory entry.
Background category implies typical props not stated | Those props are not authorized merely by category knowledge.
A background contains a separately important semantic component explicitly declared | Represent it as specified.


State | Use
Confirmed | Evidence is sufficient for the packet claim.
Probable | Evidence strongly favors the claim but does not justify treating it as certain.
Unresolved | More evidence or inspection is required.
Rejected | A candidate interpretation was tested and not supported.


Code | Failure
PC-S | Semantic addition.
PC-D | Semantic deletion.
PC-T | Temporal alteration.
PC-I | Identity alteration.
PC-C | Contradictory instructions.
PC-B | Background expansion.
PC-U | Uncertainty collapse.


Scene | Identity | Expected | Observed | Status
S01 | A1 | 1 | 1 | PASS
S01 | A2 | 1 | 1 | PASS
S02 | C1 | 1 | 2 | FAIL — possible identity split
S03 | K1 | 0 | 1 | FAIL — unsupported object if independently semantic


Code | Class | Definition
INV-O | Object invention | New semantic object absent from packet.
INV-C | Component invention | New separately represented component absent from packet.
ID-S | Identity split | One packet identity rendered as multiple simultaneous instances.
ID-M | Identity merge | Two declared identities collapse into one visual instance.
SP-D | Spatial deviation | Declared relationship/location is not preserved.
TM-D | Temporal deviation | Declared sequence, timing, persistence, or state change is not preserved.
BH-D | Behaviour deviation | Declared behaviour/action is not preserved.
ST-D | Style deviation | Declared visual style/appearance constraint is materially violated.
DET-U | Unsupported detail | Generated detail cannot be cleanly treated as declared appearance and is being treated semantically.
UNC | Evaluator uncertainty | Evidence is insufficient for definitive classification.


Required field | What to record
failure_id | Unique audit identifier.
timestamp/frame | Exact video time or frame range.
location | Image region or approximate coordinates.
observed entity | What is visibly present.
packet mapping | Declared identity or 'none'.
evidence | Frame, crop, screenshot, or frame range.
classification | Failure code and rationale.
confidence | High / medium / low.
resolution | Confirmed / unresolved / rejected.


Question | What is being tested?
Was the source analysed correctly? | Source-analysis fidelity.
Was the analysis converted into the intended packet without semantic drift? | Packet fidelity.
Was the packet converted into the generator instruction without semantic drift? | Compilation fidelity.
Did the generator reproduce the packet? | Render fidelity.
Was the failure claim itself supported by evidence? | Evaluation fidelity.


---


## Canonical specification

The complete authoritative FV rules, including the agent-facing analysis
requirements and environmental participation rules, are maintained in
`SPECIFICATION/FV_Working_Process_Specification.md`.

This skill is the operational interface for applying those rules. It must not
be treated as a separate source of policy: if a procedure or rule appears to
conflict with the canonical specification, follow the canonical specification
and flag the discrepancy for correction. Do not invent additional FV
requirements that are not documented there.
