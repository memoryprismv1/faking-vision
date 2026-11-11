FAKING VISION

Working Process Specification — Rewritten (v0.24)

**Document status:** The base text is v0.24 and the document includes later normative additions, including v0.26 and v0.27. Those additions retain their own historical labels; this note does not declare a separately consolidated release number.

Ground-up operational specification for image/video analysis, FV investigation, assembly, packet merge, packet generation, reconstruction, prompt compilation, and evidence-grade evaluation.

Acceptance test: Give this document, an image or video, and no prior FV knowledge to an unfamiliar AI instance. It must be able to analyse the source and produce a valid FV packet. Conversely, given this document and a valid FV packet, it must be able to produce or attempt a reconstruction without inventing semantic content.

This document is deliberately written as an operator specification. It contains procedures, decision rules, schemas, examples, validation gates, and failure classes. It is not a single algorithm.

# 1. Purpose and acceptance criterion

Faking Vision (FV) converts visual observations into a portable structured information packet and tests whether a reconstruction system can hydrate that packet without silently substituting its own learned world model.

The packet is the reconstruction source of truth. The reconstruction system is not being asked to produce the most plausible version of what it sees. It is being asked to reproduce the information supplied by FV.

## 1.1 The unfamiliar-AI acceptance test

The specification is considered operational only if an AI instance that has never participated in FV can execute the following tasks from the document alone.

| **Test** | **Input** | **Required output** | **Pass condition** |
| --- | --- | --- | --- |
| A — Image analysis | This specification + image | FV packet + observation record | AI can produce the packet without undocumented FV instructions. |
| B — Video analysis | This specification + video | FV packet including temporal structure | AI can establish scene structure, identities, changes, and uncertainty without being taught the missing procedure. |
| C — Reconstruction | This specification + FV packet + generator | Image/video reconstruction attempt | AI uses packet as source of truth and does not add semantic content. |
| D — Traceability | Source + generated packet | Evidence map | Each material packet assertion can be traced to source evidence or explicitly marked inference/uncertainty. |
| E — Packet audit | Packet alone | Validation report | AI can identify structural contradictions, missing required fields, and inventory problems. |

## 1.2 What failure means

If the unfamiliar AI must ask what FV means by 'analyse the frame', what counts as an entity, how to build OI/MSRM/TD, how to represent uncertainty, or how to export the packet, the specification has failed operationally. A schema without a generation procedure is not sufficient.

FV packet generation produces a structured packet as files conforming to the packet schema. A prose description of packet contents does not satisfy packet generation when the operating environment supports file creation.

When the operating environment supports file creation and packaging, the packet must be created as its required files and packaged as a ZIP for delivery. The ZIP is the primary deliverable; human-readable explanation is supplementary.

The same artifact principle applies to downstream FV operations: validation produces a validation report artifact; compilation produces the compiled renderer specification and/or reconstruction artifact available to the environment; and independent audit produces an audit artifact. A chat response describing what those artifacts would contain is not a substitute for creating them.

# 2. Core rules

1. Observe before naming. Record visible structure before committing to semantic identity where identity is uncertain.

1. Do not convert plausibility into evidence. A thing that would normally be present in a scene is not therefore present in the source.

1. Separate observation, interpretation, and packet commitment.

1. Every declared reconstruction entity must have a source basis or an explicitly declared test instruction.

1. A packet is closed after inventory lock. Reconstruction may not create new semantic entities to make the scene more plausible.

1. Appearance is not automatically an entity. Texture, shading, reflection, highlight, shadow, fold, grain, and similar visual phenomena remain appearance unless separately represented as useful semantic structure.

1. Movement is not duplication. A persistent identity changing location, pose, orientation, or behaviour remains the same identity unless evidence supports another instance.

1. Off-screen is not deleted. Scene membership and visibility are distinct from identity existence.

1. Uncertainty must survive the pipeline. An unresolved observation cannot silently become a definite packet fact.

1. Evaluation claims require evidence. A suspected failure without a frame/time/location remains unresolved.

1. Renderer limitations are not packet facts. If a renderer cannot express a constraint, record that limitation instead of rewriting the packet.

1. The packet-to-prompt transformation is itself auditable. A compiler may translate syntax, but may not add world knowledge.

# 3. Operating model: five distinct layers

| **Layer** | **Question** | **Allowed operation** |
| --- | --- | --- |
| Source | What is visually present/changeable? | Acquire and inspect the source. |
| Observation record | What did the analyst actually observe? | Record visible structure, evidence, uncertainty, and candidates. |
| FV packet | What information is authorized for reconstruction? | Resolve entities/relationships/temporal structure and lock inventory. |
| Compiled renderer specification | How is the packet expressed to a particular generator? | Translate syntax while preserving packet semantics. |
| Generated result + audit | Did the renderer reproduce the packet? | Inspect output and classify deviations with evidence. |

Never use a later layer to retroactively rewrite an earlier layer. A generated image cannot become evidence about what was in the original source.

## 3.1 FV operation model and command interface

The FV command interface names distinct operations. The commands are an operator interface, not a claim that a standalone FV executable or CLI has been implemented.

`fv analyse` — analyse a raw visual source and produce a source-grounded FV analysis packet. For video, TD is mandatory for a video reconstruction target.

`fv investigate` — pursue a specified object, event, relationship, correspondence, or question across one or more observations or media. Use TIR as the investigative workspace; commit only supported conclusions to authoritative packet records.

`fv assemble` — integrate partial, viewpoint-dependent visual/spatial representations of a larger place or field into a more cohesive spatial representation. This includes overlapping media outputs from a generator, including outputs produced as an observer or sensor changes position or direction. Typical test material includes LiDAR scans, telescope fields, aerial/satellite imagery, microscopy tiles, and overlapping photographs. Preserve the local-view/source relationships, provenance, and unresolved registration conflicts.

Assembly is not object-identity merge. Assembly may establish the spatial correspondence required to place local representations together, but it must not silently normalize object identity across inputs.

### Biological grounding: viewpoint-oriented spatial integration

FV's `assemble` operation is grounded in the biological model described by [Making Vision V2](https://www.memoryprism.com/readings/making-vision-v2): vision is viewpoint-oriented. An organism does not acquire a complete place from one all-encompassing view. As it looks in different directions and moves through positions and spaces, it acquires multiple local, viewpoint-dependent representations of portions of the same environment.

In this account, a **maplet** is a local spatial representation associated with a particular viewpoint. It is not simply a cropped photograph: it carries local spatial information related to the observer's position and the spatial structure available to the organism. Use *maplet* descriptively for this local representation; do not assume a particular neural implementation from the term alone.

Several maplets can cover overlapping portions of the same place while differing in viewpoint, direction, visible extent, scale, resolution, occlusion, and available detail. Their overlap and shared spatial structure provide evidence for relating them. Integration relates these local representations and assembles them into a more cohesive spatial map that is not limited to any one viewpoint.

FV applies this principle to media generators and their outputs. An input image, scan, exposure, tile, or other media piece can be treated as a partial representation of a larger field. The task is not merely to join file edges or blend pixels. It is to establish how the partial representations relate spatially and how they fit into the larger field. The assembled result may be an image, point cloud, surface, map, or another representation appropriate to the media; it need not be a photomosaic.

A same-generator, same-acquisition-pass collection of overlapping outputs is a useful controlled assembly case. It is not the biological limit of the idea: viewpoint changes and movement can produce successive local representations of the same place from different directions and positions. The acquisition context must be recorded rather than assumed.

#### Assembly procedure

1. **Establish the local representations.** Identify each source piece or observation, its generator and acquisition context where known, and the local field it represents. Treat each as a source-grounded local view/maplet, not as an interchangeable tile.
2. **Establish viewpoint and reference information.** Record the supported viewpoint, pose/orientation, coordinate frame, calibration, scale/resolution, acquisition order/time, coverage, and source limitations. Unknown values remain unknown.
3. **Inspect overlap and correspondence.** Determine which areas or structures are shared between local views, which are visible from only one view, and where there are gaps. Use only correspondences supported by source evidence or justified calibration. Geometric tie points may support placement without becoming persistent object identities.
4. **Register the local views.** Estimate or apply transformations into a common spatial reference using a method appropriate to the generator and media. Record the method, inputs, assumptions, residuals, and conflicts. Do not force a registration when evidence is insufficient.
5. **Integrate into a cohesive representation.** Combine the registered views in a form appropriate to the data. Preserve which local views contribute to each region and retain their viewpoint-specific evidence.
6. **Retain uncertainty and limits.** Preserve occlusions, uncovered areas, weak correspondences, registration conflicts, differing resolutions, and other limitations. Do not fill unseen regions or hide disagreement merely to make the result look continuous.

The assembled representation must remain traceable to its contributing local views. Preserve source media unchanged, along with each view's provenance, viewpoint/reference information, coverage, transformations, and registration diagnostics. Overlap is evidence for relating representations; it is not permission to average away meaningful differences or erase the original views.

#### Assembly is not cross-dataset comparison

Separate datasets that cover the same visual field—for example, historical and current observations—are distinct observations, not automatically pieces of one acquisition. The planned companion comparison workflow retains independent source packets, inspects whether they cover the same field, establishes a justified common reference, and derives a comparison/difference result linked to both. Apparent differences require inspection for registration error, viewpoint, scale, resolution, illumination, season, sensor characteristics, processing differences, and unequal coverage. A pixel or point difference is not automatically a real-world change. This is a distinct capability to develop and test; do not substitute ordinary within-pass assembly for it.

#### Assembly is not object-identity merge

Assembly determines how local spatial representations fit together. It may establish that two regions or features occupy corresponding positions for registration, but it does not establish that similarly appearing entities are the same persistent object. Identity reconciliation remains a separate `fv merge` operation and must follow its evidence and uncertainty rules.


`fv merge` — reconcile independently produced FV packets. Compare packet-scoped object declarations using source evidence, temporal continuity, properties, relationships, and preserved visual evidence before establishing normalized persistent identity. Preserve packet provenance throughout.

`fv create` — deliberately construct a new FV packet from established FV information or an explicit specification. This includes a reconstruction packet where applicable. Creation must not manufacture unsupported visual facts or convert external knowledge into visual evidence.

`fv rebuild [packet] [--to <FV-version>]` — migrate an existing packet to the current authoritative Working Process Specification, or to the explicit target supplied with `--to`. Preserve the source packet, create a separate rebuilt copy unless replacement is explicitly requested, record the migration, and validate the rebuilt copy. Rebuild is not content editing, source re-analysis, dispute resolution, or compilation.

`fv edit` — make an intentional, evidence-grounded change to existing packet content. For image-packet interaction, `fv edit` with no arguments lists available objects; `fv edit <object-name/object-id> --list` lists the selected object's properties; and `fv edit <object-name/object-id> <property-id>` identifies a direct property edit. The general value-assignment syntax is not standardized; do not invent it. Require an unambiguous target and applicable property, and preserve successful edits with before/after information and provenance. `fv edit viewpoint` is a defined subcommand with its own viewpoint/VPO operations and constraints.

`fv resolve` — resolve packet disputes, ambiguities, correspondence conflicts, or competing interpretations. Where human intervention is required, follow the existing human-resolution → AI-reconciliation → packet-validation lifecycle. An open dispute remains a rendering gate.

`fv validate` — validate packet structure, evidence traceability, consistency, inventory closure, and dispute/reconciliation state. Validation does not silently repair the packet.

`fv compile` — compile a resolved and validated packet into a renderer-specific reconstruction specification and, where supported, perform reconstruction. Compilation is prohibited when the packet is invalid, reconciliation is incomplete, or dispute.json is open or invalid.

`fv audit` — independently compare the original/expected FV packet with a separate FV packet produced by analysing the generated media. The generated-media packet must be created from the media independently, without using the expected packet as evidence for what is visible. The generated media remains available as audit evidence. Audit does not rewrite either packet. It produces a downloadable JSON audit report when file creation is available. See `SPECIFICATION/FV_Provenance_And_Audit.md` for provenance and report schemas.

### 3.1.1 Assemble versus merge

`assemble` combines partial observations that are pieces of a larger visual/spatial view. `merge` reconciles already-produced FV knowledge and may normalize persistent object identity when evidence supports equivalence. The two operations must not be silently substituted for one another.

### 3.1.2 Create versus analyse

`analyse` derives information from a raw source through the FV observation procedure. `create` constructs a packet from information that has already been established or explicitly specified. Existing packet-generation procedures remain authoritative; `create` must preserve evidence, inference, uncertainty, and provenance boundaries.

### 3.1.3 Reconstruction command gate

The normal downstream path is: `analyse / investigate / assemble / merge / create → (resolve if required) → validate → compile → audit`. Not every job requires every operation. `compile` is a hard fidelity gate and never performs dispute resolution or packet repair. If the packet is not resolved and validated, return it to the appropriate earlier operation.

# 4. Source intake

## 4.1 Image intake

Before semantic analysis, record:

- source_id and file identity

- pixel dimensions and aspect ratio if available

- orientation/rotation

- visible image boundaries

- obvious cropping or framing limits

- quality limitations: blur, compression, low resolution, occlusion, glare, darkness, overexposure, etc.

- whether the source is a single image or a frame extracted from video

## 4.2 Video intake

Record:

- source_id

- duration

- frame rate if available

- frame dimensions

- audio presence if relevant

- obvious cuts/tableau changes

- quality limitations

- whether the source contains continuous motion, hard cuts, fades, or mixed transitions

The analyst must not assume that every frame needs identical semantic analysis. Sampling is an analysis strategy, not permission to ignore meaningful changes.

## 4.3 Source integrity

If metadata or source quality prevents a reliable conclusion, preserve the limitation. Do not manufacture precision.

# 5. Image analysis procedure

## 5.1 Pass 1 — visual inventory without semantic commitment

Inspect the whole image. Identify visually bounded or otherwise separable regions and structures.

- Locate major boundaries, silhouettes, contours, surfaces, and spatial regions.

- Note repeated shapes or structures.

- Note partially visible structures and occlusions.

- Record obvious motion only if the source itself contains motion cues; a still image does not establish temporal change.

- Do not immediately assign familiar object names where the evidence is ambiguous.

## 5.2 Pass 2 — candidate generation

For each potentially meaningful structure, create a candidate record.

| **Field** | **Meaning** |
| --- | --- |
| candidate_id | Temporary identifier before entity resolution. |
| visual_evidence | What is actually visible: shape, boundary, attachment, texture, relative position, etc. |
| extent | Approximate image region if useful. |
| relationships | Observed spatial relationships to other candidates/regions. |
| semantic_hypothesis | Possible interpretation, if useful. |
| confidence | High / medium / low. |
| ambiguity | What alternative interpretations remain. |
| evidence_location | Image region or coordinate reference. |

Example: if a fruit is initially observed only as a small red rounded form, the evidence may support strawberry, raspberry, or another candidate rather than a single identity. Surface structures, aggregate-unit structure, a leafy calyx, or other diagnostic components can then be searched for to distinguish candidates. The fruit name is not evidence until the visible component bundle supports it.

For video, component emergence, disappearance, movement, or interaction may trigger adaptive sampling or behaviour-triggered component tracking when the component materially changes candidature, identity, relationship, or uncertainty. Record the candidature trajectory in TIR; commit only source-supported conclusions to TD.

Do not use later whole-object recognition to retroactively rewrite the earlier candidature record. The investigation must preserve the forward evidence path that existed when each candidate was considered.

## 5.2.1 Component-driven candidature and verification

Candidate verification is component- and relationship-based. Allocate additional processing to a candidate when its salience, uncertainty, task relevance, anomaly, or explanatory potential warrants closer inspection. The resulting inspection may strengthen, weaken, reject, or leave the candidate unresolved; the allocation decision itself does not establish its identity or evidential status. A candidate should be weakened or rejected when expected diagnostic evidence is contradicted, or when a required component should have been visible in the inspected view but is not observed. Mere absence from an uninformative or occluded view is not rejection.

Search should be targeted by the candidate set. Once a component creates candidature, ask what additional source evidence would distinguish the candidates, then inspect for that evidence. Do not search only for confirming evidence for the first candidate; where feasible, include evidence that could discriminate between or falsify the alternatives.

- the evidence supporting the allocation decision and any resulting strengthening, weakening, or rejection;

- whether the candidate was strengthened, weakened, rejected, or remains unresolved;

- which of those expected components/relationships were searched for and what was actually observed;

- the additional components or spatial/structural relationships expected to distinguish the candidates;

- the candidate set supported by that component and current context;

- the observed component and its source location;

For each component-driven candidature, record at minimum:

A component is evidence, not an identity. A single component may support several candidates. Candidate generation must preserve the alternatives actually supported by the observed component and context; it must not collapse immediately to the most familiar object.

When an object identity is uncertain, a visible component may be used to generate a bounded set of object candidates. Do not require whole-object recognition before candidature. The operational direction is: component → candidate set → targeted search for expected components/relationships → candidate verification or rejection.

## 5.3 Pass 3 — entity/component/appearance decision

Classify each candidate using the following decision order.

1. Is it merely a visual appearance phenomenon of an already represented entity? If yes, keep it as appearance unless a separately useful semantic representation is required.

1. Is it a separately useful part of an entity that must be represented to reconstruct the supplied information? If yes, classify as a component.

1. Is it a distinct semantic entity? If yes, classify as an object/instance candidate.

1. If the distinction cannot be established, retain the candidate as unresolved rather than forcing a category.

## 5.4 Pass 4 — identity resolution

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

Do not commit a correspondence hypothesis as a persistent identity until the available evidence supports that resolution. If continuity cannot be established, retain separate candidates or unresolved identity as appropriate.

Record the evidence used for the identity decision.

## 5.5 Pass 5 — packet commitment

Only after observation and candidate resolution should information be committed to the reconstruction packet. This is distinct from candidate/object promotion, which allocates additional processing effort and does not itself establish a packet fact.

Recognition is not a prerequisite for packet construction. A novel object may first be represented structurally and remain unnamed. Naming can be added later when supported.

5.6 Image/video packet decision gate

Before packet construction, classify the reconstruction target. For an image, build OI + MSRM, with optional PC. For a video, build OI + MSRM + TD, with optional PC. TD is not optional for a video. If a source is called a video but no meaningful temporal-difference record can be established, do not fabricate TD; classify the reconstruction target as an image or, only when explicitly defined by the experiment, as a set of independent images.

# 6. Video analysis procedure

## 6.1 Establish temporal structure and the temporal diff baseline

Start by identifying meaningful temporal units. A temporal unit may be a continuous scene, tableau, shot, or other interval in which the relevant visual organization remains coherent.

1. Inspect the video globally for major scene/tableau boundaries.

1. Create a scene/interval list with start and end times or frame ranges.

1. Within each interval, identify stable entities, components, spatial relationships, and states. These establish the baseline against which TD records subsequent differences.

1. Inspect transitions separately.

1. Inspect intervals around every meaningful appearance, disappearance, movement, or state change.

### 6.1.1 Audio transcript as a provisional temporal cue

If a transcript claim identifies a potential gap in the current TIR/TD representation, use its temporal location as an adaptive sampling target, subject to the current transcript assessment and timing/context information. Acquire the additional source observation and update TIR. Commit a resulting statement to TD only when the retained source evidence supports it. If the relationship between the audio commentary and the visual scene remains unresolved, preserve the uncertainty rather than deciding that the commentary is false, satirical, or otherwise untrustworthy without evidence.

A small number of transcript errors or apparent mismatches does not by itself invalidate the transcript as a useful sampling signal. The investigation should record the discrepancy, continue testing the channel, and use transcript claims as candidate sampling cues while their support is being established.

The temporary TIR must independently assess the transcript against the source audio and the visual source evidence. Track the audio/transcript channel cumulatively rather than using a binary keep/discard decision. At minimum distinguish: transcription fidelity (whether the transcript accurately represents the audio); visual/cross-modal support (whether a narrated claim corresponds to visual evidence); unresolved or ambiguous content; and timing/context mismatch where audio-supported commentary does not correspond scene-by-scene with the current visual interval.

Use the transcript during temporal investigation as an additional cue for adaptive sampling. A transcript segment may identify a time or interval that deserves visual inspection, including an event, action, relationship, or other claim that was not captured by the initial temporal observations. The claim does not need to be visually supported yet; identifying a potential gap is itself a reason to acquire the relevant source observation.

When audio is intentionally included, generate a timestamped transcript before the initial temporary TIR/TD temporal investigation. The transcript is a provisional analytical variable, not a source-of-truth record and not a substitute for listening to the source audio.

## 6.2 Temporal sampling

Sampling density must be adaptive. Begin with a lazy/coarse temporal scan. When temporal-difference (TD) evidence appears within an interval, increase sampling density locally and recursively inspect the affected subinterval. When the perturbation subsides, sampling may relax again. The sampling rate is therefore driven by observed perturbation, not imposed uniformly across the video.

### 6.2.1 Selected-frame FV image analysis

Every source frame that FV actually captures or retains as an evidence observation must undergo the default FV image-analysis procedure. Temporal sampling determines which source frames are acquired as evidence; it does not replace image analysis of those frames with mere frame retention.

For each selected frame, perform the applicable image-analysis passes: visual inventory, candidate generation, entity/component/appearance decision, identity assessment where temporal context permits, and evidence assessment and packet commitment as warranted. The resulting frame-level analysis must be available to TIR and may update OI, MSRM, TD, uncertainty, disputes, or other packet records where justified.

A selected frame is therefore both source evidence and an FV image-analysis observation. A packet must not treat a captured frame as semantically unanalysed merely because the temporal sampler selected it. Conversely, frames that were never selected need not receive the same full FV image-analysis treatment.

The temporal sampler answers **which observations are worth acquiring**. FV image analysis answers **what is present in each acquired observation**. These are distinct operations and neither substitutes for the other.

## 6.3 Track candidate identities and temporal lineages

For every candidate that may persist, maintain a temporal ledger.

### 6.3.1 Behaviour-triggered component tracking

Do not track every declared component merely because it exists. Component tracking is triggered by component behaviour when that behaviour creates enough perturbation or uncertainty to matter to the FV representation.

A component may remain an inventory/property detail while behaviourally irrelevant. Allocate temporal tracking effort to it only when its change, movement, interaction, deformation, state transition, or other behaviour materially affects the scene representation, an object state, a relationship, an action, reconstruction fidelity, or an unresolved temporal question.

Examples: a visible wheel does not automatically require wheel tracking; wheel rotation that materially explains vehicle behaviour may require local tracking. A person's hand does not automatically become a tracked component; a hand reaching for, contacting, or manipulating another object may make the hand's behaviour information-bearing. A decorative button that changes without affecting represented structure need not be tracked.

Component tracking is therefore **perturbation-triggered, not inventory-triggered**. The tracking decision and its evidence should be recorded in TIR, and any resulting component state/change should be committed to TD only when supported by the retained observations.

| **Field** | **Required content** |
| --- | --- |
| canonical_id | Stable identity used across the packet. |
| candidate lineage | Observation records associated with the identity. |
| scene membership | Scenes/intervals in which it is visible. |
| visibility state | Visible, occluded, off-screen, or unresolved. |
| entry/exit | Observed entry into or exit from the visible field. |
| state changes | Pose, orientation, location, behaviour, appearance, or other declared changes. |
| continuity evidence | Evidence connecting appearances. |
| duplication flag | Raised when one identity appears to have multiple simultaneous instances. |

## 6.4 Distinguish four temporal events

| **Event** | **Meaning** | **Default interpretation** |
| --- | --- | --- |
| Movement | Same identity changes location. | Update MSRM/TD; do not duplicate. |
| Occlusion | Same identity is temporarily hidden. | Identity persists. |
| Off-screen absence | Identity is not visible in the current framing/scene. | Identity persists unless source establishes otherwise. |
| New instance | Evidence supports a distinct additional identity. | Create a separate identity. |

## 6.5 Temporal conflict handling

If two observations appear incompatible, do not solve the conflict by spawning an extra object. First test whether the conflict is explained by movement, occlusion, camera/framing change, scene change, or uncertainty. Only explicit source evidence permits multiple instances.

# 7. Observation record and evidence discipline

The observation record is the bridge between raw source and packet. It must preserve what was seen and why a packet assertion was made.

| **Field** | **Example** |
| --- | --- |
| observation_id | OBS-014a2b3c4d |
| source_id | SRC-01b2c3d4e5 |
| time/frame | 00:12.4 / frame 298 |
| region | upper-left; approximate coordinates |
| visual description | elongated bounded form attached to candidate A |
| candidate_id | CAND-07c8d9e0f1 |
| interpretation | possible branch |
| confidence | medium |
| alternatives | shadow / branch |
| packet disposition | unresolved; not committed as object |
| evidence reference | frame 298 crop / image region |

The analyst must be able to answer: 'What in the source caused this packet field to exist?' If the answer is only 'because that is what the scene normally contains,' the field is not source-grounded.

# 8. Packet architecture

The FV packet separates object/instance information, spatial organization, temporal change, and optional project constants.

8.0 Packet architecture at a glance: OI answers WHAT EXISTS; MSRM manages WHERE/HOW ENTITIES ARE SPATIALLY RELATED; TD records WHAT CHANGED AND WHEN; PC contains genuine project-wide constants.

## 8.1 OI — Object Inventory

OI is the authoritative inventory of what entities/instances exist in the reconstruction target. It records the identities and the properties/components that matter for reconstruction.

- canonical identity

- instance identity where required

- category/name when supported

- properties

- declared components

- anomalies

- current state

- behaviour where relevant

- expression/facing/direction where relevant

- uncertainty

## 8.2 MSRM — Map Spatial Relationship Manager

MSRM is the authoritative spatial mapping and relationship-management layer. It records where entities are and how they relate spatially, at the precision actually supported by the source.

- scene membership

- relative position

- left/right/front/back/above/below relationships where supported

- distance or scale relationships when useful

- object-to-object relationships

- orientation and placement

- camera/frame relationships when they are part of the reconstruction target

## 8.3 TD — Temporal Data

TD is the authoritative temporal change layer. TD is operationally a diff log: it records what changed between temporal observations, when it changed, and which persistent identity the change belongs to. TD is mandatory for video. A video without TD is not a valid video reconstruction target; it must be treated/rendered as an image unless the experiment explicitly defines the source as independent images.

For video, observation records are records within TD, not a required separate packet file. TD may contain the temporal baseline observations and the differences derived from them. Do not create an observation.json or observations.json file unless a future FV specification explicitly defines one.

TD also owns viewpoint-conditioned temporal observations. Each observation/interval should reference its active `viewpoint_id` where known. The initial viewpoint state is recorded in `viewpoint.json`; TD records supported viewpoint transitions over time, not as OI entities. See section 10.1B. The viewpoint identity persists while the same observer/camera moves; distinct viewpoints are separately identified. A viewpoint switch is a temporal event, not an object-inventory event.

- scene/interval order

- start/end times or frame ranges

- entry/exit

- movement

- state changes

- appearance/disappearance

- off-screen status

- persistence

- transitions

8.3.1 TD makes the packet temporally queryable

TD is not merely video metadata and is not simply a description of the whole video. Because it records state transitions and other temporal differences, questions can be answered from the packet without reconstructing the video. For example: when did a traffic light turn green; did a pedestrian begin crossing before or after the light changed; how long elapsed between two state changes; which event happened first; did two changes overlap; or what changed between two specified times? Such answers are recoverable only to the temporal precision actually recorded in TD.

Example TD diff: 00:14.2→00:14.6, traffic_light_01.color = yellow→green. A query 'When did the light turn green?' can therefore return approximately 00:14.6. If TD does not contain the relevant transition or sufficient timing evidence, the correct answer is that the packet does not contain enough temporal information; OI, MSRM, or general world knowledge must not be used to invent the missing time.

## 8.4 PC — project constants

Using PC as an object database is an architectural capability to be tested, not a claim that the methodology has already been validated. Continuous same-camera footage split into temporally adjacent files is the intended experimental material for testing object reuse, packet merge, and object-database normalisation.

### 8.4.1 PC as a canonical object database

PC may also serve as the project’s canonical object database when a project declares reusable visual objects as genuine project-wide constants. This is a functional use of the existing PC structure, not a new packet layer or a replacement for PC.

### 8.4.2 Snapshot property for PC objects

An object declared in PC remains in the existing PC object/declaration structure. Do not reorganize PC, introduce a separate object-database container, or move existing PC information merely to support this use. Object-database capability is additive.

### 8.4.3 Object database status

The snapshot property is an additive property of an existing PC object declaration. Adding it must not change the existing PC structure, field organization, or semantics. If no visual evidence is available or needed, the property may be absent.

A PC object may include a snapshot property containing references to preserved visual evidence for that canonical object. Snapshot references provide visual grounding for inspection, comparison, merge, and later normalisation; they do not replace the canonical PC declaration and do not turn snapshots into canonical definitions.

## 8.5 Disputes — packet-level human-intervention and rendering-gate layer

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

## 8.6 Audio evidence and transcript

When audio is included, packet validation must verify that the audio file and transcript are present, source-aligned, and mutually traceable, and that the temporal investigation records the provisional transcript assessment and any material discrepancies.

AUDIO_COMPANION.txt may continue to provide human-readable audio notes, but it does not replace the audio file or transcript.json when a transcript is intentionally included.

Audio and visual evidence are separate evidence streams. A transcript may inform OI, TD, disputes, or other packet fields, but those fields must remain traceable to the audio segment or visual evidence that supports them. When audio and visual evidence disagree, preserve the conflict and use the existing uncertainty/dispute process rather than silently privileging one stream.

The packet must preserve the relationship between the audio file and the source video, including source identity and relevant time alignment. transcript.json should contain timestamped transcript segments and, where supported, speaker/voice attribution and transcription uncertainty. Do not invent words that are not supported by the audio. If speech is unclear, preserve the uncertainty rather than silently normalising it.

Use an optional packet-level audio/ directory:

```text
audio/
    source.<original-extension>
    transcript.json
```

If the provisional transcript identifies a temporal location or claim not adequately represented in the current TIR/TD, use it to trigger additional sampling at the relevant location, even when the claim has not yet been visually supported. Update TIR with the new evidence and commit the result to TD only when the source supports it.

A commentary segment may be accurate while referring to an earlier, later, off-screen, or otherwise different scene state. Scene-by-scene visual disagreement must therefore be recorded as a timing/context discrepancy unless the source evidence establishes that the commentary is false. Do not infer satire, fabrication, or speaker intent merely from a mismatch.

The temporal investigation must test the transcript against the source audio and the visual evidence. TIR should maintain cumulative assessment of at least two distinct properties: transcription fidelity (whether the transcript represents the audio accurately) and cross-modal support (whether narrated claims correspond to visual evidence), alongside unresolved/ambiguous content and timing/context mismatches. This assessment is not a binary transcript-valid/invalid gate: isolated transcription or interpretation errors do not by themselves invalidate an otherwise useful audio channel.

Generate the transcript before the initial temporary temporal investigation and retain it as a provisional analysis variable. It may be used to guide adaptive temporal sampling, including by identifying potential gaps before those claims are independently verified, but it must not be committed directly to TD merely because the transcript contains a claim.

When audio is intentionally included in a video packet, preserve the audio file and its transcript together as source-derived evidence. The transcript is an interpretation/extraction of the audio; it is not a substitute for the audio evidence.

## 8.7 Snapshots — preserved visual evidence

Snapshots are preserved source-derived visual evidence selected for inspection, verification, transition analysis, ambiguity, dispute resolution, or audit. The term is media-neutral and replaces source-specific language such as saved_frames.

The packet snapshot location uses lowercase `snapshot`. Its permitted structure is: `snapshot/manifest.json` (optional), `snapshot/verification/`, `snapshot/objs/`, and `snapshot/disputes/`. These are the only permitted subfolders under `snapshot/`. No nested folders may be created inside any of these folders without explicit authorization. No other snapshot subfolders may be created.

Object snapshots may include a preserved source crop and a separate highlighted analytical crop showing the object boundary or region used for analysis. A highlight is an analytical aid and must never replace or masquerade as the preserved source evidence.

The snapshot manifest, when used, belongs directly in `snapshot/manifest.json`; it is not a packet-root manifest. A manifest is not required merely because snapshots exist.

PC may hold project-wide constants that genuinely apply across scenes, including reusable visual object declarations. PC is also the existing FV structure that may serve as the project canonical object database; this does not create a new object-database layer.

A packet_id is a first-class packet identifier. It must be stable within the merge set and must be carried wherever packet provenance is required.

When a PC file is created for a packet before packet merge, each object ID must remain packet-scoped and traceable: <packet_id>-<object_id>. Do not assign a merged/global canonical object ID before the merge operation. Packet-scoped IDs preserve provenance and allow later identity matching and object-database normalisation.

The purpose of PC object declarations is to prevent repeated object instantiation across scenes or temporal observations when the evidence supports persistent identity. OI records which declared objects are present and their scene-specific state; TD records changes to those persistent identities through time.

# 9. Packet generation procedure

Assign a stable packet_id before packet contents are generated. Use that packet_id consistently in packet metadata and in packet-scoped object IDs.

For every newly generated packet, create the additive root-level `packet_provenance.json` using `FV_Packet_Provenance_Schema.json`. Record the packet-generating agent separately from the system that generated the source media. Unknown values remain null/unknown; do not infer them. Existing packets without this file remain valid under the backward-compatibility rule in section 10.1.

The `media` object in `packet_provenance.json` may also contain three independent **optional add-ons**, when the relevant information is supplied or reliably available:

- `attribution`: an object for attribution to the original source/creator. Its internal properties are deliberately left open for now; preserve supplied attribution information without inventing or normalizing fields.
- `organizations`: an array of organization objects associated with the current media. Each organization has a `name` and may have an `organization_id`.
- `contributions`: an array of contributor objects. Record `username`, `email`, `organization`, `timestamp`, and `role`. The role is the contributor's role in relation to the current media, not their general job title. Optional `contributor_id`, `contributor_type`, and `notes` may be included when known. A contribution's organization refers to `organization_id` when available, otherwise to the exact organization name.

These add-ons are not required. Omit any or all of them when the information is unavailable; omission does not affect packet validity or packet generation. Do not infer a person, organization, role, contact detail, or timestamp. Use null for unavailable values within a contribution record that is otherwise being recorded. These fields record attribution and contributions; they do not establish licence, permission, copyright ownership, or other rights. Licence and rights metadata are outside the current implementation scope.

## 9.1 Build the initial inventory

Filesystem discipline: folder structure is part of the operator interface. Do not create folders for organizational convenience. Before creating any folder not explicitly permitted by this specification, ask the operator for permission. No nested folder may be created inside `snapshot/verification/`, `snapshot/objs/`, or `snapshot/disputes/` without explicit permission. Extra folder depth is not a semantic layer and must not be introduced merely to separate artifact types.

1. Create one candidate record for each potentially meaningful semantic structure.

1. Resolve candidate identity where evidence permits.

1. Assign stable packet-scoped IDs. When a PC object declaration is created before packet merge, use the packet ID plus local object ID (for example, PKT-CCTV-001-OBJ-003). Do not prematurely assign a merged/global identity; that is established by packet merge and normalisation.

1. Separate object identities from component identities.

1. Record unresolved candidates explicitly.

## 9.2 Build OI

1. Create an OI entry for every object/instance committed to the packet.

1. Add only properties supported by source evidence or explicitly authorized project instructions.

1. Add declared components only when separately useful to reconstruction.

1. Record current state and behaviour only where visually supported.

1. Preserve uncertainty.

## 9.3 Build MSRM

1. For each scene/interval, enumerate relevant identities.

1. Record spatial positions and relationships at supported precision.

1. Do not invent exact coordinates when the source supports only relative placement.

1. Keep object inventory separate from background description.

1. Record scene-specific placements without creating new identities.

## 9.4 Build TD — the temporal diff log

1. Create ordered scene/interval records.

1. Record every meaningful change.

1. Link each change to an existing canonical identity where continuity is supported.

1. Mark off-screen/occluded states explicitly.

1. Do not encode uncertainty as a definite temporal event.

## 9.5 Lock inventory

Before export, freeze the semantic inventory. After inventory lock:

- No new object identity may be introduced by the renderer.

- No new component identity may be introduced by the renderer.

- A background description does not authorize arbitrary semantic additions.

- Uncertainty remains uncertainty.

- Missing information may be simplified or omitted; it may not be silently filled with model knowledge.

# 10. Packet schema and minimal example

## 10.1 Minimal file set

FV_PACKET/
  README.txt
  packet_provenance.json # required for newly generated packets; optional for legacy packets; records packet/media generator provenance
  PC.json                # optional generally; used when project-wide constants/object declarations are needed
  OI.json                # object/instance information
  viewpoint.json         # observer/viewpoint identities; required for newly generated packets
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

`packet_provenance.json` is an additive packet-level metadata file. It is mandatory for newly generated packets but may be absent from existing/legacy packets. Its absence MUST NOT invalidate a legacy packet; downstream operations must report provenance as unknown or legacy-missing. Do not retrofit old packets with guessed values. See `FV_Packet_Provenance_Schema.json`.

FV_PACKET/
  README.txt
  PC.json                # optional generally; used when project-wide constants/object declarations are needed
  OI.json                # object/instance information
  viewpoint.json         # observer/viewpoint identities; required for newly generated packets
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

## 10.1A Typed generated identifiers

Every identifier newly generated by FV MUST carry an explicit type prefix and an opaque autogenerated hash suffix:

`<TYPE>-<autogeneratedhash>`

Examples include `OBJ-<autogeneratedhash>`, `VP-<autogeneratedhash>`, `OBS-<autogeneratedhash>`, `CAND-<autogeneratedhash>`, `SCN-<autogeneratedhash>`, `SRC-<autogeneratedhash>`, `DSP-<autogeneratedhash>`, `SNAP-<autogeneratedhash>`, `AUD-<autogeneratedhash>`, `FAIL-<autogeneratedhash>`, `PKT-<autogeneratedhash>`, `EVT-<autogeneratedhash>`, `EDIT-<autogeneratedhash>`, `MEDIA-<autogeneratedhash>`, `FRM-<autogeneratedhash>`, `REG-<autogeneratedhash>`, `COMP-<autogeneratedhash>`, `REL-<autogeneratedhash>`, `RUN-<autogeneratedhash>`, `TIR-<autogeneratedhash>`, and `ENV-<autogeneratedhash>`. These are type examples, not a closed list. The type prefix MUST identify the kind of entity or record being identified; do not use an untyped generic identifier where an identifier is required.

The hash suffix is an automatically generated, opaque, collision-resistant token. It MUST NOT encode semantic guesses or be derived from visual appearance, object category, location, identity claims, or other source content. The exact hash-generation algorithm is an implementation detail, but implementations MUST preserve uniqueness within the relevant packet/merge scope and preserve an ID once assigned. Do not regenerate IDs on re-analysis, export, or packet update.

For packet-scoped object identities created before merge, retain packet provenance using `<packet_id>-OBJ-<autogeneratedhash>` (for example, `PKT-<autogeneratedhash>-OBJ-<autogeneratedhash>`). A later merge may establish a normalized persistent object ID only through the existing evidence-based merge procedure. Do not silently rewrite source packet IDs.

The type prefix is determined by the record being identified, not by the JSON property name. Examples: object/instance = `OBJ-`; viewpoint = `VP-`; candidate = `CAND-`; observation = `OBS-`; scene = `SCN-`; source = `SRC-`; dispute = `DSP-`; snapshot = `SNAP-`; audit = `AUD-`; failure/deviation = `FAIL-`; packet = `PKT-`; event = `EVT-`; edit = `EDIT-`; media = `MEDIA-`; frame = `FRM-`; region = `REG-`; component = `COMP-`; relationship = `REL-`; run = `RUN-`; temporal investigation record = `TIR-`; environment = `ENV-`. Implementations MUST define an explicit type prefix for any additional identifier class rather than generating untyped IDs.

**Compatibility:** existing packets and externally supplied source identifiers retain their original IDs and provenance. Do not bulk-rename legacy packet contents merely to satisfy this convention. Treat legacy IDs as legacy; all newly generated IDs use the typed format. The reserved literal `VP-DEFAULT` is the sole documented viewpoint-ID exception and is used only by the legacy compatibility rule in section 17.3. It is not a generated ID.

## 10.1B Viewpoint records

A packet MUST contain a root-level `viewpoint.json` for newly generated image and video packets. It is a JSON array of viewpoint records. Each record identifies one distinct observer/viewpoint identity and MUST contain its viewpoint initialisation. An image normally has one viewpoint record. A video has one record for each distinct observer/viewpoint identity represented in the source; multiple camera feeds or observer perspectives require separate records. Viewpoint IDs MUST be unique within the packet. Do not create extra records merely because the same observer moves or changes orientation.

Each record MUST contain:
- `id`: stable typed viewpoint ID in the form `VP-<autogeneratedhash>`;
- `observer.type`: generic observer kind, such as `camera`, `human`, `robot`, `drone`, `telescope`, or `unknown`;
- `initial_state`: the viewpoint initialisation for this image or video.
- optional `role`, `name`, `is_default`, `coordinate_frame`, and `pose` fields for reusable viewpoint objects (VPOs), as defined by `FV_Viewpoint_Schema.json`.

The `initial_state` records where/how the observer's view is initially situated, to the extent supported by the source. It MUST contain `status` (`known`, `partially_known`, or `unknown`). It MAY contain qualitative or source-supported `position`, `orientation`, and `description`, plus `basis` explaining the evidence/source for the entry. Use ordinary descriptive values; do not imply a calibrated coordinate system. If the spatial position or orientation cannot be established, state that it is unknown rather than omitting the initialisation or guessing. Pixel crop, image dimensions, and apparent perspective alone do not establish physical observer coordinates.

Optional observer description and source-supported sensor/device metadata may be included. The viewpoint identifies the observer/perspective, not an object in OI and not the visual field itself. Do not infer a calibrated camera, physical location, orientation, field-of-view geometry, or coordinate system.

For a still image, `viewpoint.json` is the required home for the initial viewpoint state. No TD file is required solely to express that initialisation.

### Reusable viewpoint objects (VPO)

A VPO is an editable, portable camera instruction. It is not merely a description of where an existing source image was captured. Preserve these as separate concepts:

- `initial_state`: source-supported description of the observer used for the original observation;
- `pose`: explicit camera pose to be used when rendering or requesting a new view;
- `role`: whether the record describes a source viewpoint, a render preset, or both.

A VPO pose MUST use an explicitly declared coordinate frame. FV's canonical default frame is right-handed, +X right, +Y up, +Z toward the viewer, with camera-local forward along -Z. Position units MUST be declared. Orientation uses intrinsic Euler rotations in Y-X-Z order, in degrees: yaw about world +Y, then pitch about the rotated camera +X, then roll about the rotated camera +Z. Positive angles follow the right-hand rule. The complete convention MUST accompany the numeric values; bare yaw/pitch/roll numbers are not portable.

A perspective pose uses `field_of_view_degrees`; an orthographic pose uses `orthographic_scale`. Framing includes aspect ratio and fit behaviour. Only fields applicable to the selected projection should be supplied. A look-at target may be supplied; when present it is a target constraint, not a substitute for the stored pose convention.

`VPO_DEFAULT` is FV's canonical default render-viewpoint object template, defined in `SPECIFICATION/VPO_DEFAULT.json` and constrained by `SPECIFICATION/FV_Viewpoint_Schema.json`. It is a reusable render preset, not a source-camera observation and not an ID. When explicitly instantiated as a packet record, it receives a newly generated `VP-<autogeneratedhash>` ID. Its default pose and coordinate convention are the documented template values; they do not describe the source camera.

A newly constructed packet/editor fixture may instantiate `VPO_DEFAULT` as its declared default render VPO. An imported packet that lacks a viewpoint record MUST NOT silently receive `VPO_DEFAULT`; the operator may explicitly create/instantiate it. An analysed source image MUST NOT be assigned an invented physical source pose merely to satisfy a default. Preserve `initial_state.status: unknown` where the source pose is unknown. At most one record may have `is_default: true`. Legacy packets without VPO fields remain readable through the separate virtual `VP-DEFAULT` compatibility behaviour; that identity is never a render VPO.

A viewpoint edit changes the active/render pose and its edit history. It MUST NOT alter OI inventory or MSRM object placement. The source viewpoint record remains available for provenance. The editor and `fv edit viewpoint` MUST use the same schema, defaults, coordinate conventions, validation and edit operations.

An AI renderer consumes the VPO as a constraint, not as inspiration. It MUST preserve the supplied scene inventory and apply the specified camera pose. Where the scene representation does not contain sufficient geometry to realise the requested pose, the renderer/editor MUST report the limitation or mark the result approximate; it MUST NOT silently invent geometry and claim an exact viewpoint match.


For video, the initial state is recorded in `viewpoint.json`, and TD records supported viewpoint transitions over time. TD observation/interval records MUST reference the active viewpoint using `viewpoint_id` whenever known. TD MUST record supported changes to that viewpoint, including position/orientation changes, camera movement, zoom/reframing, and camera/viewpoint switches as distinguishable events. A continuous observer/camera that moves retains its viewpoint ID. A switch to a distinct observer/viewpoint uses its own ID and TD records when it becomes active. A scene cut alone does not prove a new physical camera; create a distinct viewpoint record only when the source supports a distinct perspective/observer identity. If identity or transition is unresolved, preserve uncertainty rather than inventing a camera count or movement.

A viewpoint transition is a change in the observer's spatial position, orientation, or view framing over time. Record only the kind and extent of change supported by the source, with the time/frame interval using the existing TD conventions. Do not infer physical coordinates from image-plane movement or apparent perspective changes. Viewpoint movement is not object movement and MUST NOT create or modify OI identities merely because the frame changes.

### Legacy viewpoint compatibility (separate from VPO_DEFAULT)

A legacy packet without `viewpoint.json` remains readable. At read time, supply the virtual reserved ID `VP-DEFAULT` to represent only the implicit source viewpoint of the supplied image/video. This compatibility identity is not a viewpoint record, not a VPO, and not a render preset. It carries no inferred position, orientation, calibration, FOV, coordinate frame, geometry, or camera movement. It MUST NOT be written back into the legacy packet merely by reading it. Legacy TD may reference `VP-DEFAULT` in an in-memory compatibility view, but do not alter the original packet or invent temporal viewpoint events.

`VP-DEFAULT` MUST NOT be converted into, substituted for, or used to instantiate `VPO_DEFAULT`. If no render VPO exists and none is explicitly selected, report that no render viewpoint is selected; do not fabricate one. `VPO_DEFAULT` may be instantiated only by an explicit packet-creation or editor action.

Validate newly generated `viewpoint.json` against `SPECIFICATION/FV_Viewpoint_Schema.json`. No separate observations file is introduced; video observation and viewpoint-transition records remain within TD.

## 10.2 Minimal OI example

{
  "entities": [
    {
      "canonical_id": "OBJ-a1b2c3d4",
      "category": "figure",
      "properties": {
        "appearance": "dark coat",
        "orientation": "facing right"
      },
      "components": [],
      "uncertainty": []
    },
    {
      "canonical_id": "OBJ-c1d2e3f4",
      "category": "capsule",
      "properties": {
        "appearance": "small enclosed vehicle"
      },
      "components": [],
      "uncertainty": []
    }
  ]
}

## 10.3 Minimal MSRM example

{
  "scenes": [
    {
      "scene_id": "SCN-01a2b3c4",
      "entities": [
        {"id": "OBJ-a1b2c3d4", "position": "left of center"},
        {"id": "OBJ-c1d2e3f4", "position": "right of A1"}
      ]
    }
  ]
}

## 10.4 Minimal TD example

{
  "timeline": [
    {
      "scene_id": "SCN-01a2b3c4",
      "start": 0,
      "end": 9,
      "visible": ["OBJ-a1b2c3d4", "OBJ-c1d2e3f4"],
      "off_screen": []
    },
    {
      "scene_id": "SCN-02b3c4d5",
      "start": 9,
      "end": 18,
      "visible": ["OBJ-a1b2c3d4"],
      "off_screen": ["OBJ-c1d2e3f4"],
      "changes": [{"id": "OBJ-a1b2c3d4", "change": "moved"}]
    }
  ]
}

The examples are illustrative schema patterns, not a requirement that every project use these exact property names or coordinate systems. The essential requirement is that the information categories and identity relationships remain explicit and auditable.

# 11. Backgrounds versus objects

FV must distinguish a background as a visual setting from the semantic object inventory.

| **Case** | **Correct treatment** |
| --- | --- |
| Painted lunar landscape is declared as background | Background content may be reconstructed within the declared description. |
| A rock is separately declared as an object | Rock is part of the closed object inventory. |
| Background says 'cratered ground' | Crater appearance is not automatically a new object inventory entry. |
| Background category implies typical props not stated | Those props are not authorized merely by category knowledge. |
| A background contains a separately important semantic component explicitly declared | Represent it as specified. |

This distinction prevents the evaluator from incorrectly classifying every background pixel as an invented object while still testing whether a generator expands a sparse background into a conventional world.

# 12. Uncertainty and unresolved states

Uncertainty is an explicit state, not a temporary inconvenience to be erased.

| **State** | **Use** |
| --- | --- |
| Confirmed | Evidence is sufficient for the packet claim. |
| Probable | Evidence strongly favors the claim but does not justify treating it as certain. |
| Unresolved | More evidence or inspection is required. |
| Rejected | A candidate interpretation was tested and not supported. |

An unresolved observation may remain in the observation record without becoming a closed-inventory entity. Evaluators must not turn unresolved source observations into reconstruction failures.

If the unresolved condition materially prevents reliable packet construction, identity resolution, spatial/temporal resolution, or audit, create a packet-level dispute record. The dispute does not replace the unresolved observation; it makes the need for human intervention explicit and traceable.

# 13. Reconstruction procedure

## 13.1 Renderer-neutral reconstruction

The reconstruction system receives the locked packet. Its job is to express the packet visually, not to infer a richer world.

Before loading the packet for reconstruction, validate dispute.json as a hard rendering gate. If it is missing, malformed, open, or inconsistent with the packet, stop reconstruction. Continue only when its aggregate status is none or resolved and ordinary packet validation passes.

1. Load packet and verify schema.

1. Verify that OI, MSRM, and TD are internally consistent.

1. Load optional PC constants.

1. Establish the closed object/component inventory.

1. For video, establish persistent identity ledger before rendering scene sequence.

1. Render each scene according to its local membership and spatial instructions.

1. Apply temporal changes from TD.

1. Keep off-screen identities persistent rather than deleting/recreating them.

1. Do not add unspecified semantic objects/components.

1. Preserve uncertainty where the packet contains uncertainty.

## 13.2 Missing information

When the packet does not specify a detail necessary to make pixels coherent, the renderer may choose a visually coherent realization that does not create a new semantic entity. This is an appearance-generation allowance, not permission to expand the inventory.

## 13.3 Renderer limitations

If a renderer cannot reliably execute a packet constraint, record the limitation as an engineering observation. Do not alter the packet to make the renderer appear compliant.

# 14. Packet-to-renderer prompt compilation

A renderer may require natural-language or other generator-native instructions. That translation is a separate experimental layer.

FV PACKET → LOSSLESS COMPILED SPECIFICATION → RENDERER-SPECIFIC ADAPTER → GENERATOR

## 14.1 Compiler rules

1. Preserve all packet identities.

1. Preserve object/background separation.

1. Preserve scene membership.

1. State off-screen persistence explicitly for persistent identities.

1. Preserve temporal ordering, transitions, and declared state changes.

1. Do not add adjectives, props, motivations, world-building details, or genre conventions merely to make the prompt sound natural.

1. Check positive and negative instructions for contradictions before generation.

1. Keep renderer-specific instructions distinguishable from packet facts.

1. Keep renderer capability limitations separate from source/packet information.

## 14.2 Recommended compiled structure

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

## 14.3 Prompt compilation failure classes

| **Code** | **Failure** |
| --- | --- |
| PC-S | Semantic addition. |
| PC-D | Semantic deletion. |
| PC-T | Temporal alteration. |
| PC-I | Identity alteration. |
| PC-C | Contradictory instructions. |
| PC-B | Background expansion. |
| PC-U | Uncertainty collapse. |

# 15. Reconstruction evaluation

## 15.1 Independent packet-to-packet audit

The audit inputs are:

1. The original/expected FV packet: the reconstruction source of truth.
2. The generated image/video.
3. A separate FV packet produced by independently analysing the generated media. This generated-media packet must not use the expected packet as evidence for what is visible in the media.

Compare the expected packet with the generated-media packet. Keep the generated media available for inspecting and locating deviations. Do not use the reconstruction generator's explanation as evidence.

Keep three identities distinct:
- media generator: the system that produced the image/video;
- generated-media packet generator: the agent that independently analysed that media;
- auditor: the agent that compares the two packets and produces the audit.

Use `packet_provenance.json` when available. Missing provenance in legacy packets is unknown, not a reason to reject the packet or invent an identity.

The evaluator must independently check:

1. Object count and identity continuity.
1. Component inventory.
1. Scene occupancy.
1. Spatial relationships.
1. Temporal sequence and state changes.
1. Declared behaviour/action.
1. Style/appearance constraints.
1. Unsupported semantic additions.
1. Background expansion.
1. Every nontrivial deviation with evidence references to the media and relevant packet records.

The audit does not rewrite either packet.

## 15.2 Scene occupancy accounting

| **Scene** | **Identity** | **Expected** | **Observed** | **Status** |
| --- | --- | --- | --- | --- |
| S01 | A1 | 1 | 1 | PASS |
| S01 | A2 | 1 | 1 | PASS |
| S02 | C1 | 1 | 2 | FAIL — possible identity split |
| S03 | K1 | 0 | 1 | FAIL — unsupported object if independently semantic |

Never force an ambiguous candidate into an existing identity simply to make counts close.

# 16. Failure taxonomy

| **Code** | **Class** | **Definition** |
| --- | --- | --- |
| INV-O | Object invention | New semantic object absent from packet. |
| INV-C | Component invention | New separately represented component absent from packet. |
| ID-S | Identity split | One packet identity rendered as multiple simultaneous instances. |
| ID-M | Identity merge | Two declared identities collapse into one visual instance. |
| SP-D | Spatial deviation | Declared relationship/location is not preserved. |
| TM-D | Temporal deviation | Declared sequence, timing, persistence, or state change is not preserved. |
| BH-D | Behaviour deviation | Declared behaviour/action is not preserved. |
| ST-D | Style deviation | Declared visual style/appearance constraint is materially violated. |
| DET-U | Unsupported detail | Generated detail cannot be cleanly treated as declared appearance and is being treated semantically. |
| UNC | Evaluator uncertainty | Evidence is insufficient for definitive classification. |

# 17. Evidence-grade failure reporting

Disputes are not limited to renderer failures. A dispute may be raised whenever the AI cannot reliably determine the correct visual representation. The minimum dispute linkage should include dispute_id, source/evidence reference, affected OI/MSRM/TD record where applicable, problem description, attempted resolution, status, and human_action_required.

For generated or re-rendered images, preserve the disputed output and the relevant source snapshot(s) when the AI cannot reliably read, compare, or explain an object or visual structure. The strange result is evidence of the dispute, not permission to invent a correction.

| **Required field** | **What to record** |
| --- | --- |
| failure_id | Unique audit identifier. |
| timestamp/frame | Exact video time or frame range. |
| location | Image region or approximate coordinates. |
| observed entity | What is visibly present. |
| packet mapping | Declared identity or 'none'. |
| evidence | Frame, crop, screenshot, or frame range. |
| classification | Failure code and rationale. |
| confidence | High / medium / low. |
| resolution | Confirmed / unresolved / rejected. |

Do not classify an evaluator's uncertain observation as a formal failure until supporting evidence is located.

## 17.1 Downloadable JSON audit report

When file creation is available, every `fv audit` MUST create a downloadable JSON report named `FV_AUDIT_REPORT.json`. The JSON report is the primary audit artifact; a human-readable chat summary is supplementary. Validate the report against `SPECIFICATION/FV_Audit_Report_Schema.json`.

The report MUST identify the expected packet, generated-media packet, generated media, auditor, available packet/media provenance, audit specification version, and comparison method. It MUST preserve individual deviation records and evidence references. It MUST include category-specific numerators, denominators, uncertainty counts, rate percentages, and the unit definition used for each denominator.

Calculate each rate as 100 × confirmed deviation units / assessable units. If the denominator is zero, report a null rate, not zero. Uncertain units remain separate; they are not silently counted as passes or failures. Do not combine unlike deviation classes into one overall score. Comparable rates require stable unit definitions and visible denominators.

See `SPECIFICATION/FV_Provenance_And_Audit.md` for the complete report contract.

## 17.2 Batch aggregation reference utility

A reference offline processor is provided at `TOOLS/fv_audit_batch.py`. It validates and aggregates existing audit JSON reports; it does not re-audit media, rewrite source reports, or provide a native skill-runtime command. The proposed `fv audit batch [audit-report.json ...]` interface remains experimental until the skill runtime can invoke the utility with attached files.

The processor detects identical and conflicting duplicate audit IDs, retains invalid-report diagnostics, separates profiles by role, agent/model identity, FV audit specification and report schema versions, metric code, unit definition, and scope, and pools numerators and denominators before recalculating rates. Zero denominators yield null rates. See `SPECIFICATION/FV_Provenance_And_Audit.md` for invocation and boundaries; run `python -m unittest discover -s TOOLS -p 'test_*.py' -v` for the reference tests.

## 17.3 Viewpoint initialisation and transition

FV records the observer's viewpoint as packet metadata. This is not a requirement to recognise a scene, compare different images, match objects across viewpoints, reconstruct camera geometry, or reconcile multiple views into a shared scene.

- **Image:** record the initial viewpoint in `viewpoint.json`.
- **Video:** record the initial viewpoint in `viewpoint.json`, then record supported viewpoint transitions over time in TD.
- **Distinct observers/viewpoints:** assign separate viewpoint identities when the source supports them. Movement or reorientation by the same observer does not create a new identity.

The initialisation states where/how the view is situated at the beginning, at the precision supported by the source. A transition states how that viewpoint changes during the video. Position, orientation, camera movement, zoom/reframing, and viewpoint switches are distinguishable where evidence permits. Unknowns remain explicitly unknown. Do not invent coordinates, calibration, or camera geometry.

This metadata requirement does not require a matched set of images or a fixed scene. The viewpoint identity and initial state are defined in section 10.1B; temporal transitions are recorded in TD. The visual field, object inventory, and per-object visibility remain separate FV concerns and are not expanded by this requirement.

# 18. Model-knowledge containment test

FV should actively test whether a renderer imports knowledge about what a scene category normally contains.

1. Create a deliberately sparse packet.

1. Choose a category that strongly predicts common but undeclared objects.

1. Render it.

1. Audit every semantic addition separately.

1. Repeat with a richer packet.

1. Compare whether omitted structure is systematically filled by the renderer.

The relevant mechanism is model-knowledge expansion of the supplied representation, not merely generic 'hallucination'.

# 19. Temporal identity stress test

1. Declare one persistent identity.

1. Place it at A in scene 1.

1. Place the same identity at B in scene 2.

1. Place the same identity at C in scene 3.

1. Make the environment visually rich enough that previous locations remain tempting.

1. Score movement, disappearance/reappearance, duplication, and identity continuity separately.

This test isolates whether a renderer treats sequential spatial requirements as movement of one identity or as permission to spawn additional instances.

19.1 Temporal queryability check

For every video packet, test whether TD supports at least the following classes of query at its recorded precision: (a) state-transition time; (b) event ordering; (c) elapsed interval between changes; (d) temporal overlap; (e) entry/exit timing; and (f) changes within a specified time window. A failure to answer must be reported as missing/insufficient TD, not repaired from world knowledge or from assumptions about the source.

# 20. Complete image-analysis checklist

☐ Source metadata and limitations recorded.

☐ Whole image inspected before local interpretation.

☐ Boundaries/regions/contours identified.

☐ Candidate structures recorded.

☐ Observation separated from semantic hypothesis.

☐ Components separated from appearance phenomena.

☐ Object/instance candidates identified.

☐ Identity decisions supported by evidence.

☐ Uncertain candidates retained as unresolved where necessary.

☐ OI built from entities committed to the packet only.

☐ MSRM built from observed spatial relationships.

☐ Inventory locked before reconstruction.

☐ Packet internally validated.

☐ Packet exported with README and required files.

# 21. Complete video-analysis checklist

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

# 22. Complete reconstruction checklist

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

# 23. Packet integrity checklist

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

# 24. Practical operator template

## 24.1 Image job

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

## 24.2 Video job

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

# 25. End-to-end procedure

1. Receive image/video and establish source identity.

1. Record source limitations.

1. Inspect the source before semantic commitment.

1. Create observation records and evidence locations.

1. Generate candidates from visible structure.

1. Resolve object/component/appearance status.

1. Resolve identities while preserving uncertainty.

1. For video, establish scenes/intervals and temporal continuity.

1. Build OI.

1. Build MSRM.

1. Build TD for video.

1. Add PC only for genuine project-wide constants.

1. Cross-check packet references.

1. Lock the closed inventory.

1. Export the packet.

1. If reconstructing, compile the packet into a lossless renderer specification.

1. Apply renderer-specific syntax without adding semantic content.

1. Validate compiled specification against packet.

1. Generate reconstruction.

1. Independently audit the generated result.

1. Attach evidence to every nontrivial failure claim.

1. Classify deviations.

1. Keep renderer limitations separate from packet errors.

# 26. Worked miniature example: sparse image

Suppose the source image shows a person, a rectangular box, and a dark irregular patch on the floor. The patch resembles a bag but its boundaries are ambiguous.

1. Record person and box as candidates with visible evidence.

1. Record the dark patch as an unresolved candidate; do not call it a bag merely because bags are common near people.

1. If the patch cannot be established as a semantic object, it does not enter the closed object inventory.

1. Represent the person and box in OI and their relative positions in MSRM.

1. Record the unresolved patch in the observation/audit record.

1. Lock inventory with person + box only.

1. A renderer may reproduce a dark floor appearance if needed for visual coherence, but it may not introduce a semantic bag.

# 27. Worked miniature example: persistent video identity

Suppose one figure appears in scene S01 on the left, disappears during a hard cut, and appears in S02 on the right.

1. Create one candidate lineage from S01 and S02 if continuity is supported by the declared test/source.

1. Assign one canonical identity, e.g. A1.

1. Record S01 membership and left position in MSRM.

1. Record S02 membership and right position in MSRM.

1. Record the scene transition and continued identity in TD.

1. Do not create A2 merely because A1 occupies a different position.

1. If continuity cannot be established, mark the identity relationship unresolved rather than inventing certainty.

27.1 Worked miniature example: temporal query from TD

Suppose a video contains a traffic light. OI declares traffic_light_01. MSRM records its location relative to the road and other entities. TD records: 00:14.2→00:14.6, traffic_light_01.color = yellow→green. A packet query asking 'When did the traffic light turn green?' is answered from TD as approximately 00:14.6. A query asking whether a pedestrian began crossing before or after the change can be answered by comparing the pedestrian's corresponding TD event with the light transition. If the packet contains no such transition, the answer remains unknown.

# 28. What this specification does not assume

- It does not require bounding boxes.

- It does not require ControlNet.

- It does not require masks, reference-image conditioning, compositing, latent object slots, or deterministic layout controls.

- It does not assume that every visual representation is a photograph-like stored image.

- It does not assume that object names must precede structural representation.

- It does not assume that a generator's explanation is evidence of what its output contains.

Specific engineering interventions may be tested later when a failure mechanism has been characterized.

# 29. Distinguishing three kinds of correctness

| **Question** | **What is being tested?** |
| --- | --- |
| Was the source analysed correctly? | Source-analysis fidelity. |
| Was the analysis converted into the intended packet without semantic drift? | Packet fidelity. |
| Was the packet converted into the generator instruction without semantic drift? | Compilation fidelity. |
| Did the generator reproduce the packet? | Render fidelity. |
| Was the failure claim itself supported by evidence? | Evaluation fidelity. |

These must not be collapsed. A generator failure may actually be a packet error or a prompt-compilation error. Conversely, a correct packet and correct compiled prompt can still produce a failed reconstruction.

# 30. Final acceptance test

## 30.1 Packet merge identity test

When multiple packets describe temporally adjacent material from the same source/world, merge must compare packet-scoped object declarations rather than assuming local IDs are globally identical. The merge process must preserve source packet provenance, test continuity and visual evidence, and only then establish a normalised persistent object identity.

The specification passes only when an unfamiliar AI can use it as an executable process rather than merely as a description of FV.

1. Give the AI one image and this document. Ask for a complete FV packet.

1. Inspect whether it knows what to observe, what to record, how to resolve candidates, how to construct OI/MSRM, and how to validate the result.

1. Give the AI one video and this document. Ask for a complete packet including TD and persistent identities.

1. Inspect whether it can distinguish movement, occlusion, off-screen absence, and new instances.

1. Give the AI a valid packet and this document. Ask it to compile and reconstruct.

1. Inspect whether the compilation preserves packet semantics and whether the renderer is prevented from importing undeclared world knowledge.

1. Ask the AI to justify every material packet assertion with source evidence.

1. Any undocumented step that the AI must be taught separately is a specification gap.

## 30.2 Additional acceptance test: temporal queryability

Give an unfamiliar AI a valid video packet and ask temporal questions whose answers are explicitly encoded in TD, such as 'When did the light turn green?' The AI must retrieve the answer from TD rather than infer it from OI, MSRM, the scene category, or external world knowledge. Then ask a question whose answer is not encoded. The AI must report insufficient temporal information rather than fabricate an answer.

## 30.3 Command-interface acceptance test

An unfamiliar AI should be able to interpret the FV command interface without undocumented instructions. Given a raw source, `fv analyse` must invoke the source-analysis procedure. Given a specified question over one or more observations, `fv investigate` must preserve an explicit investigative evidence path. Given partial or overlapping spatial observations, `fv assemble` must perform source-grounded registration/assembly without silently normalizing object identity. Given independent packets, `fv merge` must preserve packet provenance and test identity equivalence before normalization. Given established information, `fv create` must construct the requested packet without inventing visual facts. Given an open dispute, `fv resolve` must follow the required resolution lifecycle. `fv validate` must report readiness without silently repairing the packet. `fv compile` must refuse unresolved or invalid input. `fv audit` must independently evaluate the result.

# 31. Working principle

Faking Vision is not trying to make a renderer produce a plausible world. It is trying to determine whether a renderer can produce the supplied world without quietly replacing the supplied representation with its own.

Ground-up operational specification. Further changes should be made by testing this document against unfamiliar AI instances, not by adding sections merely because a later conversation exposed a missing paragraph.

# 32. Adaptive Temporal Decomposition (ATD)

FV video analysis must not use a predetermined sampling rate as its fundamental temporal model. Temporal resolution is determined by the evidence required to represent the visual sequence adequately.

Adaptive Temporal Decomposition (ATD) recursively subdivides a temporal interval when the current representation cannot adequately account for what occurs within that interval. The process continues only where additional temporal resolution is justified by observable structure, identity continuity, spatial relationships, state changes, or uncertainty.

## 32.1 Frame versus temporal interval

- A frame is source evidence at a particular instant.

- An observation interval is the basic temporal representation unit.

- A temporal leaf is an interval that can currently be represented without material loss of relevant evidence.

- An unresolved interval is subdivided for further observation.

- TD records the resulting ordered temporal structure, transitions, state changes, and uncertainty.

## 32.2 Recursive temporal procedure

1. Establish the temporal extent of the source and identify obvious hard scene/tableau boundaries.

1. Create an initial interval covering each coherent temporal region.

1. Observe interval endpoints and interior evidence sufficient to test whether one FV state can represent the interval.

1. Compare structured state rather than relying on global pixel difference alone.

1. If the interval is adequately represented, retain it as a temporal leaf.

1. If it is unresolved, subdivide it into ordered subintervals and repeat the test.

1. Preserve the source frames needed to inspect unresolved intervals and important transitions.

## 32.3 Interval-resolution test

An interval is unresolved when the available evidence cannot safely be represented as one temporally consistent FV state. The test considers:

- visual difference that materially changes the represented scene;

- object or boundary difference, including appearance, disappearance, splitting, merging, or altered boundaries;

- persistence and identity continuity;

- spatial relationship changes such as contact, separation, occlusion, ordering, containment, or relative movement;

- observable state, behaviour, facing, direction, expression, or component-state changes;

- uncertainty about whether a material change occurred or which identity/relationship is involved.

Large pixel change is not required for subdivision, and small pixel change is not sufficient to declare an interval stable. A local event can require finer temporal resolution even when most of the frame is unchanged.

## 32.4 No fixed-rate shortcut

Statements such as 'sample every N frames' or 'sample every X seconds' may be used for an engineering pre-pass or comparison experiment, but they are not the FV temporal model. An implementation that merely subdivides every interval to a predetermined minimum duration is also not considered evidence-driven ATD.

## 32.5 Entity continuity during ATD

Temporal subdivision must not itself create or destroy identity. Provisional entities should be associated across neighboring intervals using multiple observable cues where available:

- position and bounding geometry;

- motion and co-motion consistency;

- shape, area, and appearance continuity;

- boundary continuity;

- pairwise spatial relationships;

- occlusion and reappearance evidence.

If continuity cannot be established, preserve the ambiguity. Do not manufacture a new identity merely because an interval boundary was introduced.

## 32.6 Temporal relationship evidence

Changes in relationships are first-class temporal evidence. Examples include near→farther, separate→contact, beside→separated, visible→occluded, following/co-moving→independent motion, and outside→inside. MSRM remains responsible for spatial relationships; TD records how those relationships change through time.

## 32.7 Temporal maplet

A retained temporal leaf may be represented as a bounded temporal maplet: a time range linked to the relevant OI/MSRM state, transition evidence, and uncertainty. This is a representation concept, not a replacement for OI, MSRM, or TD.

## 32.8 Temporal evidence retention

Where temporal evidence cannot be resolved confidently, retain the relevant source frames as snapshots and create a packet-level dispute when human intervention is required. Snapshot retention does not itself imply that every frame is archived.

- Retain evidence around state transitions.

- Retain evidence around identity ambiguity and occlusion.

- Retain evidence around important relationship changes.

- Retain evidence where later observations support or refine an object/component.

- Do not retain every frame simply because a fixed-rate policy selected it.

## 32.9 Updated video-analysis checklist

- ☐ Temporal resolution was determined from evidence rather than a fixed sampling rate.

- ☐ Candidate intervals were recursively subdivided only where the current representation was unresolved.

- ☐ Interval stability was tested using structured visual state, not global pixel difference alone.

- ☐ Object continuity and relationship continuity were considered.

- ☐ Movement, occlusion, off-screen absence, and new instances remain distinct.

- ☐ Temporal boundaries do not create new identities.

- ☐ TD records the resulting temporal order and changes at the precision actually supported.

- ☐ Important transition/ambiguity evidence was retained.

## 32.10 Perturbation-driven adaptive sampling

ATD should allocate temporal observation effort according to the observed rate and concentration of visual perturbation. The default mode is a lazy scan. A temporal-difference cluster detected within a coarse interval is a trigger to increase local sampling density. The affected interval is subdivided and sampled more frequently; if perturbation persists or becomes denser, subdivision may continue. When perturbation falls below the criterion for further attention, the sampler may return to the coarser rate.

The initial video division is an engineering search structure, not a fixed temporal resolution. A merge-sort-like strategy may be used: divide the source into length-dependent chunks, inspect representative points and boundaries, then recursively subdivide only chunks or subintervals containing evidence of unresolved temporal change.

Sampling effort should therefore behave approximately as: quiet interval → low observation density; emerging perturbation → increased density; sustained/high perturbation → higher density; perturbation subsides → reduced density. The exact rates are implementation parameters to be empirically calibrated, not FV constants.

If an explicit task objective is supplied by the experiment, it may alter sampling priority. The task objective is an external analysis instruction, not source evidence. It may specify what to track or investigate, but it must not supply identities, events, motivations, or missing temporal facts. Goal-directed sampling and evidence acquisition remain separate.

### 32.10.1 Change Propensity, Current Change, and Change Generators

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



## 32.11 Temporal timestamps are index metadata

A source timestamp, frame number, or derived source-time coordinate is temporal index metadata attached to an observation or TD record. It is not itself a visual object and must not be committed or repeatedly represented as scene content merely because its displayed value changes from frame to frame.

If the source contains a visually displayed CCTV timestamp, that timestamp is visual evidence and should be read from the relevant source frame or snapshot only when the question requires it. The machine temporal coordinate and the visually displayed timestamp are distinct fields.

## Change log — v0.9

## Change log — v0.10

• Added packet-level DISPUTES flat file for cases where automated analysis cannot reliably resolve what is present or how it should be represented and human intervention is required.

• Added SNAPSHOTS as the media-neutral name for preserved visual evidence, replacing saved_frames terminology.

• Added verification/ as a possible snapshot subfolder for evidence retained specifically to resolve uncertainty or disputes.

• Clarified that disputes may originate from OI, MSRM, TD, observation, source, or reconstruction/audit while remaining visible at packet level.

• Clarified that disputed visual evidence is preserved as-is and that human resolution must not silently rewrite the original automated observation.

- Added Adaptive Temporal Decomposition (ATD) as the general FV temporal-analysis model.

- Defined the observation interval as the basic temporal representation unit; frames remain source evidence.

- Replaced fixed-rate temporal resolution as the conceptual basis of video analysis.

- Defined recursive subdivision of unresolved intervals.

- Added structured temporal tests for visual, object/boundary, persistence, relationship, state, and uncertainty changes.

- Added entity-continuity requirements during temporal subdivision.

- Made relationship changes first-class temporal evidence.

- Defined the temporal maplet concept.

- Clarified that merely subdividing to a predetermined minimum duration is not evidence-driven adaptation.

## 32.12 Moving-camera perturbation

A moving camera is itself a source of temporal perturbation. High temporal-difference density may arise from the camera sweeping past otherwise static world structure. FV must not automatically interpret this as object motion or as independent new entities. Transient visual structures that enter, traverse, and leave the field of view remain observations and may be information-bearing even when persistent identity is not established.

## 32.13 Perturbation-density compression

Adaptive temporal decomposition can compress a dense temporal-difference stream into a smaller set of evidence-bearing snapshots while retaining the temporal structure needed to locate materially relevant perturbations. Snapshot count alone is not the measure of success. Reconstruction experiments should compare source TD behavior, retained FV evidence, and reconstructed-output TD behavior.

## 32.14 Reconstruction as an experimental test

FV reconstruction experiments may intentionally use crude or ugly renderers. Aesthetic quality is not an acceptance criterion. The first question is whether the packet plus retained snapshots can regenerate the temporal and visual structure represented by FV. Generated intermediate imagery is not source evidence unless supported by the FV packet. Every generated reconstruction should be independently FV-audited.

## 32.15 Experimental material selection

FV experiments do not require prestigious, large, or specialized datasets. For exploratory work, prefer small, directly accessible material that permits rapid observation, modification, reconstruction, and failure analysis. Dataset prestige and scale are not FV requirements.

## Change log — v0.11

• Refined Adaptive Temporal Decomposition to explicitly support perturbation-driven adaptive sampling: lazy scanning by default, increased local sampling around TD clusters, recursive subdivision while perturbation persists, and relaxation when it subsides.

• Added a merge-sort-like chunking strategy as an implementation pattern for locating temporal perturbations efficiently without making fixed-rate sampling the FV model.

• Clarified that sampling density is a dynamic implementation parameter driven by observed perturbation rate/concentration and must be empirically calibrated.

• Clarified that frame numbers and source timestamps are temporal index metadata, not visual objects; displayed CCTV timestamps remain source visual evidence and are inspected only when needed.

## Change log — v0.12

• Added moving-camera perturbation as a general temporal consideration.

• Added perturbation-density compression as an experimental concept.

• Added deliberate ugly reconstruction as a valid experimental method.

• Added independent FV audit of reconstructed outputs.

• Added guidance to prefer small, directly accessible experimental material.

# Change log — v0.13

- Replaced the legacy DISPUTES.flat concept with structured dispute.json.

- Made dispute.json a required packet-level rendering gate with aggregate status none, open, or resolved; rendering is permitted only for none or resolved.

- Added structured dispute fields including issue, source/affected record, snapshot_ids, resolution_status, resolved_by, resolution_remark, human_action_required, timestamps, and AI reprocessing state.

- Added dispute.reconciled.json as the preserved resolution record.

- Added the required human-resolution → AI-reprocessing → packet-validation lifecycle.

- Clarified that human resolution does not directly repair the packet; AI must reprocess the packet and update affected OI/MSRM/TD or observation records before the dispute can be cleared.

- Added rendering-gate and packet-integrity checks for dispute state and reprocessing completion.

## Change log — v0.14

Added PC as an optional canonical object-database use without changing the existing PC structure.

Added an additive snapshot property for PC object declarations to provide preserved visual grounding.

Clarified that object-database use, packet merge, and object-database normalisation remain experimental goals requiring continuous same-camera temporal material for validation.

## Change log — v0.15

• Added filesystem discipline requiring operator permission before creating unlisted folders.

• Added support for highlighted analytical object snapshots while preserving the original source evidence separately.

• Defined the lowercase snapshot/ structure: optional manifest.json plus verification/, objs/, and disputes/, with no nested folders without explicit permission.

• Made packet_id a first-class provenance identifier.

• Required packet-scoped PC object IDs in the form <packet_id>-<object_id> before packet merge.

• Clarified PC as the existing canonical object-database structure and its role in preventing repeated object instantiation.

• Made TD the owner of video observation records; no separate observation.json/observations.json is required.

Information should be committed from TIR to TD only when the evidence supports the corresponding official temporal statement. Provisional reasoning should remain distinguishable from committed packet facts.

TIR is therefore not a temporary or inferior version of TD. It is the record of the investigation from which the official TD record is derived. The AI may use TIR freely as an analytical workspace and may revise, extend, or contradict provisional entries as new evidence is acquired.

• TD.json is the official temporal record. It contains the evidence-grounded temporal information committed to the FV packet.

• TIR is the investigation record. It may contain rich observations, measurements, hypotheses, competing interpretations, intermediate conclusions, sampling decisions, rejected hypotheses, and unresolved questions.

TIR is distinct from TD.json:

TIR is the persistent investigation record used during temporal analysis. It replaces the implementation-oriented name TEMP_TD.

## TIR — Temporal Investigation Record

## 17.18 Multi-pass temporal analysis and TIR

Adaptive Temporal Decomposition may use multiple analysis passes before deciding which observations to retain. The passes serve different purposes and must not be confused with a fixed sampling rate.

### 17.18.1 Initial global interval for long video

For a video longer than one minute, an implementation may use an initial global temporal interval of 4 seconds as an engineering starting point.

Let L = video duration; I = 4 seconds; and a = ceil(L / I), the number of global interval positions. The 4-second value is an implementation parameter, not an FV constant. It is a starting probe whose adequacy must be evaluated empirically.

### 17.18.2 Random reconnaissance pass

Before or alongside the normal global pass, the AI may perform an independent random reconnaissance pass. Set r = ceil(a / 2). Generate r unique random temporal positions across the video, subject to the experiment's sampling-coordinate rule.

In the current implementation, random reconnaissance positions are selected from odd-numbered temporal positions so that they are distinct from the even-position global sampling structure. Random positions must be non-duplicate and bounded by the actual video duration. If an adaptive candidate would otherwise reuse a random observation, select another unsampled coordinate.

Each random observation is analysed and its temporal evidence is accumulated in TIR. The random reconnaissance TD is an in-memory analysis resource during the run; it does not need to be exported as a separate file.

Random reconnaissance is not itself the final temporal representation. Its purpose is to provide an independent view of where temporal activity, object/action changes, transitions, or uncertainty may occur.

### 17.18.3 Normal global pass

Run the global temporal sequence using the current initial interval: 0, 4, 8, 12, 16, ... At each interval, compare the observations and update TIR. The global interval is therefore a default observation stride, not a claim that nothing meaningful occurred between its endpoints.

### 17.18.4 TIR is the active temporal analysis workspace

During video analysis, maintain a rich temporary temporal-data structure (TIR) that may contain substantially more information than the final TD packet schema.

TIR may contain, as applicable: temporal observations and source coordinates; global visual change; local/regional visual change; object appearance/disappearance; object movement; object action or apparent action; object pose, orientation, direction, or state change; object identity continuity and ambiguity; object-to-object relationship changes; contact, separation, following, containment, occlusion, and co-motion; camera movement, pan, tilt, zoom, and reframing; affected spatial regions; persistence and transition evidence; local activity baselines; hypotheses and intermediate conclusions; evidence supporting or contradicting a conclusion; uncertainty; reasons an interval does or does not require further observation; and relationships between observations from different passes.

TIR is an analytical scratchpad, not a restricted scalar TD score. The AI should use it to form meaningful temporal conclusions and to decide where additional evidence is useful.

The final TD record is a structured, evidence-grounded representation derived from the analysis. TIR may therefore be richer, messier, and more exploratory than exported TD.

### 17.18.5 TD dimensions for adaptive decisions

Adaptive decisions should consider multiple forms of temporal evidence rather than a single pixel-difference value: visual change; object/boundary change; object movement; object action; persistence/identity continuity; spatial relationship change; state change; camera/framing change; spatial concentration of change; and uncertainty or insufficient temporal evidence.

Object change and object action are temporal evidence even when whole-frame visual difference is modest. Conversely, large whole-frame change caused by camera motion must not automatically be treated as object-level activity.

- Any externally supplied task objective and the sampling-priority consequences of that objective, kept separate from source evidence.

- Incongruity records where observed evidence departs materially from the current expectation and triggers further investigation.

- Evidence Yield (EY) records using current evidence, source frame ID, and previous evidence history.

- Change-generator relationships, including change_generator_obj_ids and affected object IDs where supported.

- Change Propensity records: static change propensity (SCP) and current change propensity (CCP), with their evidential basis or provisional status.

### 17.18.6 Global versus local TD

TIR should distinguish global temporal change from local/regional temporal change where the evidence permits. Global TD describes change distributed across much or all of the frame. Local TD describes change concentrated in one or more spatial regions.

A frame-wide perturbation may indicate camera movement, zoom, reframing, lighting change, or a genuinely global scene change. A concentrated perturbation may indicate object movement, action, appearance/disappearance, occlusion, or a local state/relationship change. This distinction is an analysis aid, not an automatic semantic classification.

### 17.18.7 Local baseline

Where useful, TIR should maintain a slowly updating local activity baseline for a region or temporal stretch. Adaptive significance should be judged relative to recent local behaviour when possible, rather than only against a single fixed global threshold.

A continuously busy region should not trigger unlimited subdivision merely because its absolute TD remains high. A sudden departure from that region's recent behaviour should receive greater attention. A local baseline is provisional evidence and must be updated as new observations arrive.

### 17.18.8 Adaptive insertion

When the current global interval contains unresolved or materially significant temporal evidence, insert an additional observation.

The default insertion point is the midpoint of the interval. Midpoint selection is intentional: the global temporal positions and the random reconnaissance positions use different coordinate parity in the current implementation, so midpoint insertion normally supplies an observation that has not already been sampled.

If an alternative insertion point is considered, first check whether that temporal coordinate has already been sampled. Never duplicate an existing observation merely because a different pass discovered the same coordinate. The midpoint is an evidence-acquisition convenience, not a claim that the true event boundary lies at the mathematical midpoint.

### 17.18.9 Meaningful adaptive conclusions

TIR should be used to make temporal conclusions before requesting further observations. Examples include: an object persists while changing location; a person/object begins or ends an action; camera movement explains frame-wide change; a localized change warrants object-level inspection; an object becomes occluded and later reappears; a relationship changes while participating objects remain present; a transition appears within an interval but its timing is unresolved; or an interval contains insufficient evidence to distinguish competing temporal explanations.

The answer to 'why sample here?' should therefore be a conclusion about the source evidence or unresolved temporal structure, not merely 'because the threshold was exceeded.'

### 17.18.10 Minimum-width investigation

An implementation may define a minimum temporal width for a specific hot interval when precise transition localization is required. Activity magnitude and interval width answer different questions: activity evidence determines whether an interval deserves deeper investigation; minimum width determines when the investigation has reached the desired temporal resolution.

A minimum width must not be applied uniformly to every interval. Quiet intervals remain on the global lazy scan. A hot interval may continue to be subdivided until its temporal width is sufficiently small for the question being analysed or the available source evidence reaches its limit.

### 17.18.11 Random reconnaissance refresh

The initial random reconnaissance pass is primarily a triage mechanism. It does not automatically need to be repeated after every adaptive subdivision. However, if a region becomes sufficiently complex or uncertain that the original reconnaissance evidence is no longer informative, a local reconnaissance pass may be performed and recorded in TIR.

### 17.18.12 Pass interaction

The passes are complementary: random reconnaissance provides independent temporal evidence; the 4-second global pass provides systematic coverage; adaptive investigation follows conclusions from TIR. No single pass is independently authoritative.

## Change log — v0.17

- Added a multi-pass temporal-analysis procedure combining an optional random reconnaissance pass, a long-video 4-second global starting interval, and evidence-driven adaptive insertion.

- Defined TIR as a rich in-memory temporal-analysis scratchpad that may contain observations, object/action changes, relationships, camera changes, regions, uncertainty, hypotheses, and intermediate conclusions before final TD export.

- Added object change and object action as explicit temporal evidence.

- Added global-versus-local TD distinction to help separate camera/framing perturbation from concentrated object-level change.

- Added a provisional local activity baseline for adaptive significance.

- Clarified midpoint insertion and sampling-coordinate uniqueness.

- Added optional minimum-width investigation for specifically hot intervals without turning minimum width into a global fixed-rate sampler.

- Clarified that random reconnaissance is independent evidence/triage rather than the final temporal representation, and may be locally refreshed when initial evidence becomes stale.

## Change log — v0.17

- Renamed the temporal investigation workspace from TEMP_TD to TIR (Temporal Investigation Record).

- Defined TIR as a persistent investigation record distinct from the official TD.json.

- Clarified that TIR may retain rich, provisional, contradictory, exploratory, and rejected temporal reasoning while TD contains committed, evidence-grounded temporal information.

- Clarified that TIR is the source/workspace for deriving the official TD record, not a temporary copy of TD.

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

## Change log — v0.22

- Added Change Propensity as a temporal-analysis attention prior, separating Static Change Propensity (SCP) from Current Change Propensity (CCP).

- Added change_generator_obj_ids and explicit propagation relationships so current change can be traced from a source object through affected objects.

- Defined Evidence Yield (EY) as a structured temporal evidence record with current, frameid, and previous history rather than a scalar score.

- Added operational incongruity as an expectation/observation mismatch that can trigger further investigation.

- Clarified that explicit task objectives may alter sampling priority but are external instructions, not source evidence.

- Added the requirement to keep CP, EY, and change-generator relationships distinct.

## Change log — v0.23

- Added component-driven candidature and verification: component → candidate set → targeted search for expected components/relationships → verification or rejection.

- Defined component candidature as an evidence-preserving alternative to immediate whole-object recognition.

- Added required candidature/verification fields for observed components, candidate alternatives, discriminating components/relationships, search results, and promotion/rejection status.

- Clarified that later whole-object recognition must not retroactively rewrite the earlier evidence path.

- Connected component emergence and behaviour to adaptive temporal sampling and behaviour-triggered component tracking where the component materially affects identity, relationship, or uncertainty.

### Change log — v0.24

• Added ambiguous TIR correspondence/identity handling across multiple investigated media.

• Added component-quality labels: high, weak, and transient.

• Added provisional correspondence wording and discriminating-component search for identity resolution.

• Clarified that unobserved expected components are not negative evidence when the view is uninformative or occluded.

# v0.26 — Environmental participation and object response

**Status:** Normative addition to the FV Working Process Specification  
**Date:** 2026-10-21  
**Builds on:** v0.25 image packet editing and environmental participation  
**Tracking issue:** https://github.com/memoryprismv1/faking-vision/issues/4

## Purpose

Environmental edits can affect environmental state, object appearance, and object behaviour/location. These are distinct changes and must be represented and validated separately. This addition addresses the v0.25 limitation where appearance could change while spatial relations remained unchanged despite a test expecting an active response.

## Response classification

Classify an object's response **for the current edit**, not as a permanent type:

- **Passive response:** the represented change is to appearance or state, with no behaviour or spatial change asserted.
- **Active response:** the represented object changes behaviour and/or location in response to the changed environment. Update MSRM whenever position or spatial relation changes.

These categories describe the edit record, not an absolute ontology. Living objects do not universally move in high stress, and non-living objects are not universally immobile. Ground expectations in source evidence, explicit task/test requirements, the represented object's capabilities and constraints, and uncertainty. Do not invent an unobserved response simply because it seems typical.

## Environmental stress

In `ENVIRONMENT.json`, `environmental_stress` uses exactly one of `none`, `low`, or `high`. Explanations, provenance, and uncertainty belong in other fields. A free-form value such as `high - triggers shelter seeking` is invalid for this enum.

High stress triggers a check of relevant objects within the affected area. It does not by itself prove a particular behaviour or mandate movement.

## Record responsibilities and consistency

- **ENVIRONMENT.json:** environmental condition state and the defined stress value.
- **OI.json:** object state and supported before/after behaviour. Include applicable response/insulation state when known. Distinguish direct observation from inference; rationale is not source evidence.
- **MSRM.json:** current spatial state. If an edit changes position or spatial relation, record auditable before/after information. Do not fabricate a spatial change where none is asserted.
- **edit_log.json:** edit event, changed properties, affected IDs, response classification, provenance, outcome, and before/after references. Use `affected_objects_passive` as an array of IDs and `affected_objects_active` as an array of records keyed by `id` with supported before/after response and `msrm_changed`.

Use the same object IDs across OI, MSRM, and edit records. References must resolve or have an explicit schema-approved explanation for omission. Conflicting copies of edit classifications are not allowed.

## Validation and audit

1. A test may declare a specific expected response. If packet data or the rendered image contradicts that expectation, that test fails. The intentionally negative harsh-sun test is an example: it expects the cat remaining exposed to be flagged.
2. Where high stress makes a response worth investigating but source or test evidence does not determine the response, mark the result unresolved or request review; do not apply a universal rule that every living object must move.
3. If active movement or shelter-seeking is asserted, verify that OI, MSRM, the edit log, and the edited image agree. A log or generator explanation is not evidence that the object is actually sheltered.
4. For passive response, check the expected visible state change and ensure unsupported object movement or new entities are not invented.
5. Report JSON parsing, structural consistency, FV semantic validation, and independent visual audit separately. Passing one does not imply passing the others.

## Compatibility and provenance

Preserve v0.25 packet history and legacy version claims. When an older packet is updated, record its new mapping/edit event without implying that it was originally authored under v0.26. Missing environment data alone does not invalidate a legacy packet.

The supplied test bundle repeats assertions that source images were generated by the contributor and creator-owned, but the bundle does not establish those claims with source URLs or rights evidence. Do not publish the image binaries or describe them as rights-cleared until source and licence/permission evidence is available.

# v0.27 — Legacy packet rebuild and version upgrade

**Status:** Normative command/workflow addition  
**Purpose:** Bring an existing FV packet into structural and procedural alignment with a specified FV specification version without rewriting its historical evidence or provenance.

## Command

`fv rebuild [packet] [--to <FV-version>]`

`fv upgrade` is an accepted alias for `fv rebuild`. If no target version is supplied, use the current authoritative FV specification version available to the agent. State the source and target versions in the rebuild report.

## Responsibilities and boundaries

- **Rebuild/upgrade is packet migration.** It maps an existing packet's structure and records to a target FV version.
- **Edit is intentional content change.** Use `fv edit` to change object properties, viewpoints, environmental conditions, or other packet content. Do not use `fv edit` as a substitute for version migration.
- **Validate checks; it does not repair.** Rebuild must run validation after migration, but validation remains a separate operation and its result must be reported independently.
- **Rebuild is not analyse or investigate.** It does not re-examine the source media or recover evidence that was never recorded. If source re-analysis is needed, identify it as a separate required operation.
- **Rebuild is not resolve.** It must not settle disputes, invent human decisions, or change an open dispute to resolved. Existing compilation gates remain in force.
- **Rebuild is not compile.** A rebuilt packet must pass the target version's validation and reconciliation gates before compilation.

## Validation and compilation rebuild assessment

Both `fv validate` and `fv compile` must assess whether the packet may need migration to the current/target FV specification version. They must return that assessment explicitly; they must not leave the user to infer it from individual schema warnings.

Use one of these outcomes in the validation report and compile result:

- **REBUILD NOT INDICATED:** the packet is mapped to the target version, or its legacy structure is fully covered by documented compatibility rules and no material migration gap was found.
- **REBUILD MAY BE NEEDED:** the packet is legacy, unversioned, or uses older structures, but the available evidence does not establish that a rebuild is necessary. State the reason and what inspection would settle it.
- **REBUILD RECOMMENDED:** a specific, safe migration opportunity or current-version gap has been identified. State the affected records/rules and the benefit of rebuilding.
- **REBUILD REQUIRED:** the packet cannot meet a required target-version rule through documented compatibility handling. Identify the blocking gap and direct the operator to `fv rebuild` / `fv upgrade`.
- **ASSESSMENT INDETERMINATE:** version or packet evidence is insufficient to decide. State what is missing; do not guess.

### `fv validate`

Validation must report the rebuild assessment alongside (not instead of) structural validity, FV semantic validity, evidence consistency, dispute/reconciliation state, and compilation readiness. A legacy packet may be valid under an explicitly documented compatibility rule while still receiving **REBUILD MAY BE NEEDED** or **REBUILD RECOMMENDED**. Do not fail validation solely because a packet is old or unversioned when compatibility permits it.

Validation never performs the rebuild. It must not silently rewrite packet files, update version claims, or materialize compatibility placeholders as source facts.

### `fv compile`

Compilation must inspect the validation report or perform the same rebuild assessment before compiling, and repeat the assessment in its result:

- If **REBUILD NOT INDICATED**, continue subject to all ordinary validation and dispute gates.
- If **REBUILD MAY BE NEEDED** or **REBUILD RECOMMENDED**, explicitly warn that migration may improve/currentize the packet. Compilation may continue only when the packet independently passes all compilation gates and the target specification explicitly permits its legacy compatibility path. State that compilation did not rebuild the packet.
- If **REBUILD REQUIRED**, stop before producing renderer instructions or a generator-ready prompt. Direct the operator to `fv rebuild` / `fv upgrade`, then `fv validate`, then retry compilation.
- If **ASSESSMENT INDETERMINATE**, do not imply that the packet is current. If the uncertainty affects a required compilation rule, stop and identify the information needed; otherwise continue only with an explicit warning and the applicable compatibility boundary.

Neither command runs `fv rebuild` automatically. A recommendation is a diagnostic, not permission to mutate the packet. Rebuild remains an explicit, separately requested operation.

## Required procedure

1. Preserve the supplied packet as the immutable migration source. Work on a separate rebuilt copy unless the user explicitly requests an in-place replacement.
2. Inventory packet files, declared version markers, schemas, provenance, edit history, disputes, and validation reports. If no version marker exists, identify the source as **legacy/unversioned**; do not guess its exact authoring version.
3. Determine which historical rules can be established from the packet and available specifications. Report when the original version or historical validity cannot be established.
4. Build a migration map from the source representation to the target version. Separate:
   - mechanical structural transformations;
   - compatibility representations explicitly permitted by the target specification;
   - changes requiring source re-analysis, human input, or an intentional `fv edit`.
5. Apply only transformations justified by the target specification. Preserve packet IDs, evidence references, identity, scene membership, temporal order, uncertainty, negative constraints, dispute history, and original provenance unless a target rule explicitly requires a traceable structural representation change.
6. Never invent observations, object properties, camera geometry, coordinate frames, environmental conditions, object responses, timestamps, rights claims, or human resolutions to satisfy a newer schema.
7. Preserve the original version claim. Record the target mapping as a new migration event; never relabel historical content as though it had originally been authored under the target version.
8. Produce a rebuild report that records source packet/version, target version, files inspected, transformations applied, compatibility handling, unresolved items, operations requiring re-analysis or human action, and post-rebuild validation results.
9. Run `fv validate` against the rebuilt copy using the target specification. Report structural validation, FV semantic validation, dispute/reconciliation readiness, and any independent visual audit separately. A successful structural migration does not imply that evidence gaps or open disputes have been resolved.

## Outcomes

Return one of these explicit outcomes:

- **UPGRADED — VALIDATED:** migration completed and target-version validation passed; compilation readiness is reported separately.
- **UPGRADED — REVIEW REQUIRED:** structural migration completed, but one or more evidence, semantic, dispute, or human-review requirements remain.
- **BLOCKED:** migration cannot safely proceed without missing source material, a specification decision, or human input.

A blocked or review-required packet must not be described as fully upgraded or compilation-ready.

## Compatibility and provenance

Apply compatibility behaviour only where the target specification explicitly defines it. For example, a legacy packet may remain readable through the documented virtual `VP-DEFAULT` interpretation; that compatibility interpretation does not establish physical camera geometry and must not be materialized as invented pose data. Missing environment data alone does not invalidate a legacy packet. Rebuild must not manufacture an `ENVIRONMENT.json` state or object response merely to make the packet resemble a newer example.

Use an established FV version-marker file and schema when one is defined. Until the version-marker filename/schema is standardized, do not invent one: preserve the source packet, state the target mapping in the rebuild report, and flag the marker-format gap rather than writing an undocumented version file.

The rebuild report is a migration record, not a replacement for source provenance, edit history, dispute history, or validation reports.

# 33. AI execution requirements and analysis heuristics

This section incorporates the agent-facing requirements formerly maintained in
`FV_Working_Process_Specification_AI_Agent_Additional_Guidance.md`. The present
Working Process Specification is the single authoritative source for FV rules.
Examples and heuristics below guide application of the preceding procedures;
they do not override source evidence, packet schemas, validation gates, or
explicit task requirements.

## 33.1 Evidence levels

Keep claims distinguishable by their evidential basis:

1. **Direct visual evidence:** structure, appearance, components, and states
   directly visible in the source.
2. **Relational evidence:** conclusions derived from visible relationships,
   including relative size, position, overlap, grouping, orientation, and
   occlusion.
3. **Calibrated inference:** conclusions supported by a reliable reference,
   known geometry, or other justified calibration.
4. **Knowledge-supported inference:** conclusions requiring stored knowledge
   about an object, species, environment, or typical behaviour.
5. **Unresolved or speculative:** claims for which the available evidence does
   not justify a unique answer.

Do not present a higher-level inference as direct observation. Preserve the
basis and uncertainty of each consequential claim. A fluent explanation does
not strengthen its evidence.

## 33.2 Object properties, actions, and scene construction

Analyse what an object visibly **is like** separately from what it **does**.
Properties may include shape, colour, texture, visible components, relative
size, and orientation. Actions or methods may include holding, resting,
leaning, containing, supporting, or interacting with another object. Record
an action only when the source supports the relevant relationship or state;
do not infer a complete temporal event from one still image.

Construct local scene structure before producing a scene-level narrative.
Include candidates, boundaries, major surfaces, spatial relationships,
overlap and occlusion, relative scale, repeated or unusual objects, and
foreground/background organisation. A candidate may remain structurally
represented while its identity is unresolved.

## 33.3 Object promotion and alternative passes

Object promotion means allocating additional inspection or analysis effort to
a candidate object or relationship. Promotion may be triggered by salience,
uncertainty, task relevance, anomaly, or the possibility that the candidate
explains other observed structure. Promotion changes processing priority; it
does not increase evidential certainty by itself.

For a difficult or ambiguous source, consider separate analytical passes:

- **Broad-scene pass:** establish major structures and relationships.
- **Candidate-focused pass:** inspect one uncertain or consequential candidate
  and the components or relationships that would distinguish alternatives.
- **Alternative-allocation pass:** redirect attention to a different candidate or
  relationship and test whether the scene interpretation changes.
- **Consistency pass:** check the resulting interpretations against the same
  source evidence and preserve unresolved alternatives.

Do not force the first plausible interpretation to become the final one.
Record meaningful alternatives and the evidence that supports or contradicts
them. Promotion must not cause unsupported entities or relationships to be
added to the packet.

## 33.4 Size anchoring and calibration

An image does not automatically establish absolute physical size. A familiar
object may serve as a size anchor only when its identity and relevant
dimensions are sufficiently reliable for the task. State the anchor and the
assumptions used. Distinguish relative size visible in the image from an
absolute measurement derived through calibration.

Do not manufacture measurements from a familiar-looking object when its
identity, dimensions, perspective, or distance are uncertain. If calibration
is not justified, report relative scale or leave absolute size unresolved.

## 33.5 Adversarial visual analysis

FV must test whether a plausible interpretation is being produced by
misleading attention or incomplete inspection, not merely whether it can
recognise a likely object.

- **Camouflage:** a target visually blends into the background and may be
  overlooked as scenery.
- **Sleight of hand:** attention is directed toward a distractor while another
  relevant object or event is missed.

These are different failure mechanisms. When a task or source suggests either,
inspect the background and low-salience regions as well as the promoted
foreground candidate. Do not presume a hidden target exists; record only
what the source supports. For adversarial tests, retain the distractor,
candidate, inspected region, and evidence supporting the detection or
non-detection outcome.

## 33.6 Insufficient views and active observation

An inadequate view is not a complete observation. Use a status such as
**object detected; identity unresolved** when that is what the evidence
supports. A wider view may establish context while a closer or alternate view
may expose diagnostic components; neither view should be treated as
automatically decisive.

When the operating environment permits acquiring another observation, use
the cycle:

**observe → construct → assess uncertainty → identify the useful next view →
acquire it → update the analysis.**

Request or acquire a better view when the unresolved question materially
affects the task and another observation could discriminate between
alternatives. If another view is unavailable, preserve the uncertainty rather
than fabricating a resolution. For embodied systems, camera or body movement
is an observation-acquisition action, not evidence about the scene until the
new view is observed.

## 33.7 Blind analysis and knowledge containment

Keep these sources separate during analysis:

- **Image evidence:** what can be seen directly.
- **Internal comparison:** what can be compared with other objects or
  references already present in the source.
- **External knowledge:** information supplied by model knowledge, databases,
  or external references.
- **Calibration:** what is established through a justified measurement or
  reference.
- **Uncertainty:** what remains unresolved after those sources are considered.

External knowledge can generate candidates or help interpret evidence, but it
must not be relabelled as something visibly observed. If a task requires blind
analysis, do not use external identity information to settle the result.
Preserve the distinction between source-grounded findings and knowledge-based
hypotheses.

## 33.8 Output structure for difficult or consequential images

When the task needs a human-readable analysis alongside the packet, organise
it so that evidence and inference are easy to audit. A suitable structure is:

1. Scene structure.
2. Objects and unresolved candidates.
3. Spatial and other observed relationships.
4. Calibration and size assumptions, if any.
5. Direct evidence with source locations.
6. Inferences, labelled by evidential basis.
7. Uncertainties and limitations.
8. Alternative readings considered.
9. The next observation that would most efficiently resolve a material
   uncertainty.

This explanation is supplementary. It does not replace the required packet,
evidence references, validation report, or other operation-specific artifact.

## 33.9 Generality and experimental discipline

The analysis and temporal rules apply across source types, including still
images, CCTV, driving and LiDAR-camera sequences, drone and archaeological
video, phone video, historical film, animation, and GIFs. Adapt the
observation method to the source without changing the evidence standard.

FV experiments may use deliberately simple or aesthetically poor
reconstructions when these make packet fidelity and failure easier to test.
Prefer small, directly accessible material that permits rapid observation,
modification, reconstruction, and failure analysis. Dataset size, prestige,
and visual polish are not substitutes for a clear, testable experiment.

Treat capabilities not yet demonstrated by controlled tests as experimental.
In particular, a robot's ability to request or acquire a better view is an
operational capability to test, not an assumption that every FV environment
can move a camera or embodied system.


## Supplementary provenance and audit-file processing

Packet provenance, independent packet-to-packet audit reports, and batch aggregation are specified in `FV_Provenance_And_Audit.md`. The batch reference utility and its tests are under `TOOLS/`. These additions do not alter the core packet records or claim that the FV skill command runtime itself is a standalone CLI.
