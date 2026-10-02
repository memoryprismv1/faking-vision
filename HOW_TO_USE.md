# How to Use Faking Vision

**v0.24 update:** temporal analysis now separates Static Change Propensity (SCP), Current Change Propensity (CCP), Evidence Yield (EY), and change-generator relationships; explicit task objectives may alter sampling priority but remain separate from source evidence.

This guide is a quick route into the repository. The **FV Working
Process Specification is authoritative**. This guide does not replace
it.

## FV artifact output

FV operations produce actual artifacts, not merely prose responses.

- `fv analyse` creates the structured FV packet as files and packages the packet as a ZIP for delivery. The ZIP is the primary deliverable; human-readable analysis is supplementary.
- `fv validate` produces a validation report artifact and does not silently repair the packet.
- `fv compile` produces the compiled renderer specification and/or reconstruction artifact available to the environment.
- `fv audit` produces an independent audit artifact.

When file creation and packaging are available, do not substitute a textual dump of the packet for the packet ZIP. Do not simulate file creation by printing what the files would contain.

## FV command map

The textarea commands are operational boundaries, not claims that a standalone FV CLI exists.

| Command | Use it for | Main result |
|---|---|---|
| `fv analyse` | Analyse a raw image, video, CCTV sequence, LiDAR-camera sequence, scientific sequence, animation, or other visual source. | Source-grounded FV analysis packet. |
| `fv investigate` | Pursue a specified object, event, relationship, correspondence, or question across one or more observations/media. | Investigation record/report and, where appropriate, packet updates. |
| `fv assemble` | Put partial or overlapping observations together into a larger spatial/visual representation: LiDAR scans, telescope fields, aerial/satellite imagery, microscopy tiles, overlapping photographs, etc. | Registered/assembled representation with provenance and unresolved registration issues preserved. |
| `fv merge` | Reconcile independently produced FV packets and compare packet-scoped object declarations. | Merged packet/object inventory with provenance preserved and identity normalization only where supported. |
| `fv create` | Deliberately construct a new FV packet from established FV information or an explicit specification. | Requested packet type, including a reconstruction packet where applicable. |
| `fv resolve` | Resolve an open dispute or competing interpretation. | Reconciled packet or explicitly still-unresolved packet, with resolution history preserved. |
| `fv validate` | Check packet structure, evidence, consistency, disputes, and readiness. | Validation report; no silent repair. |
| `fv compile` | Convert a **resolved and validated** packet into renderer instructions and, where supported, reconstruct. | Compiled renderer specification and/or reconstruction artifact. |
| `fv audit` | Independently test the reconstruction against the packet and source where available. | Independent audit report. |

### The important distinctions

**Assemble is not merge.**

`assemble` combines partial observations that cover portions of a larger visual/spatial view. It may require registration, overlap handling, coordinate alignment, or spatial stitching. It does not automatically establish that similarly appearing objects across the inputs are one persistent object.

`merge` combines already-produced FV knowledge. It compares packet-scoped declarations, source evidence, temporal continuity, properties, relationships, and preserved visual evidence before establishing normalized persistent identity.

**Create is not analyse.**

`analyse` derives a packet from a source through the FV observation procedure. `create` constructs a packet from information that has already been established or explicitly specified. Existing packet-creation workflows, including packets derived from supplied literature, remain subject to evidence/uncertainty rules and must not turn external knowledge into visual evidence.

**Compile is not resolve.**

If a packet contains an open dispute, failed reconciliation, or failed validation, compilation stops and the packet returns to the appropriate earlier operation. The compiler must never solve an unresolved visual question by inventing an answer.

### Command chaining

A typical reconstruction path is:

`analyse / investigate / assemble / merge / create → resolve → validate → compile → audit`

Some jobs can skip operations that are not needed. `resolve` is required when a dispute or unresolved issue blocks the requested downstream operation. `validate` is the final packet gate before `compile`.

## 1. Analyse an image with FV

Give the AI the source image together with:

the FV Working Process Specification contained in the FV skill (or the repository copy of `FV_Working_Process_Specification.docx`)

The image-analysis path is:

`source → observation → candidate generation → entity/component/appearance resolution → packet promotion → packet construction → validation → export`

### Component candidature

When an object is ambiguous, do not wait for whole-object recognition.

Use:

`component → candidate set → search for discriminating components/relationships → verify/reject`

A component is evidence, not identity. Preserve multiple evidence-supported candidates when necessary. Record what additional component or relationship was sought, what was observed, and why a candidate was strengthened, weakened, rejected, or left unresolved. Do not let later recognition rewrite the earlier evidence path.

For cross-media identity, keep TIR ambiguous until correspondence is supported:

- record the component report used for the correspondence hypothesis;
- label component quality as **high, weak, or transient**;
- use wording such as **“Initial investigation suggests same object based on [component-report]”**;
- if correspondence remains unresolved, record the competing candidates and what discriminating component/relationship should be searched for;
- if the said object is the same object across multiple investigated media, search for expected/discriminating components and relationships;
- do not treat an unobserved expected component as negative evidence when the view is occluded, cropped, blurred, too small, or otherwise uninformative;
- promote correspondence to persistent identity only when source evidence supports it.

The resulting FV packet uses:

-   **OI** --- Object Inventory: what entities/instances exist and which
    properties/components matter.
-   **MSRM** --- Map Spatial Relationship Manager: where entities are
    and how they are spatially related.
-   **PC** --- optional project-wide constants/canonical object database
    capability.

Keep observation, interpretation, and packet commitment distinct.
Observe visible structure before semantic naming where identity is
uncertain. Do not promote something into the closed reconstruction
inventory merely because it is plausible or typical.

Every material packet assertion must remain traceable to source evidence
or be explicitly represented as inference/uncertainty.

## 2. Analyse a video with FV

Give the AI the source video together with:

the FV Working Process Specification contained in the FV skill (or the repository copy of `FV_Working_Process_Specification.docx`)

The video path uses:

-   **OI**
-   **MSRM**
-   **TD** --- Temporal Data
-   **PC** --- optional where applicable

**TD is mandatory for a video reconstruction target.** TD owns the video
observation records; do not create a separate `observation.json` or
`observations.json` unless a future FV specification explicitly defines
one.

Video analysis should:

1.  Establish scenes/intervals and temporal structure.
2.  Use **Adaptive Temporal Decomposition (ATD)** rather than treating a
    fixed sampling rate as the fundamental temporal model.
3.  Acquire additional temporal evidence where observable structure,
    identity continuity, spatial relationships, state changes, or
    uncertainty justify it.
4.  Track persistent identities across observations.
5.  Distinguish movement from duplication.
6.  Distinguish occlusion and off-screen absence from deletion.
7.  Record entry/exit and state/behaviour changes.
8.  Promote evidence-supported temporal statements into **TD**.
9.  Preserve richer provisional investigation in **TIR** when needed.

### Audio-assisted temporal analysis

When audio is intentionally included:

1. Generate the timestamped transcript early, before the initial temporary TIR/TD investigation.
2. Keep the transcript as a provisional variable; it is not source truth.
3. Use transcript segments as additional cues for adaptive sampling.
4. Test the transcript against the source audio and the independently observed visual evidence.
5. Track transcription fidelity, cross-modal visual support, unresolved content, and timing/context mismatch cumulatively.
6. Do not discard the transcript channel because of a small number of apparent errors.
7. If a transcript claim identifies a potential gap, sample the relevant time/interval even if the claim is not yet visually supported, then update TIR.
8. Promote only source-supported results into TD.
9. If commentary does not match the current scene, preserve the discrepancy rather than assuming it is false, satirical, fabricated, or intentionally misleading.

### TIR versus TD

**TIR (Temporal Investigation Record)** is the persistent investigative
workspace. It may contain observations, measurements, hypotheses,
competing interpretations, sampling decisions, rejected hypotheses, and
unresolved questions.

**TD (Temporal Data)** is the authoritative temporal record committed to
the FV packet.

TIR is not a weaker version of TD. It records the investigation from
which evidence-supported temporal statements are derived. Provisional
reasoning may be revised as new evidence is acquired; only supported
statements are promoted into TD.

### ATD

A frame is source evidence at a particular instant. An observation
interval is the basic temporal representation unit.

ATD recursively increases temporal resolution only where the current
representation cannot adequately account for the source. Do not assume
that an interval midpoint is an event boundary merely because it was
sampled there.

Activity magnitude and interval width are separate controls: a highly
active region does not by itself determine the temporal precision
required.


### Change Propensity and propagation

Use **Static Change Propensity (SCP)** as the baseline attention prior for an
object. Use **Current Change Propensity (CCP)** for its present change-priority
state. CCP may change as observations, interactions, and propagation occur;
SCP does not automatically change.

Record **`change_generator_obj_ids`** when source evidence supports which
object(s) generated or transmitted a perturbation. An affected object may
become a subsequent generator. Do not invent an unobserved causal chain.

Use **Evidence Yield (EY)** as a temporal evidence record rather than a scalar:

```text
EY = {
    current: <current evidence/state>,
    frameid: <source frame>,
    previous: [<earlier evidence records>]
}
```

EY describes what evidence an object or region is producing now in relation
to its previous observations. CP/CCP directs attention; EY records evidence;
generator IDs record supported propagation relationships.

**Incongruity** is an expectation/observation mismatch, such as low expected
change followed by meaningful EY. It is a reason to investigate further, not
an object identity or explanation.

If an experiment supplies an explicit **task objective**, it may change
sampling priority (for example, tracking a specified thing across multiple
videos). The objective is an external instruction, not source evidence. It
specifies what to investigate, not what happened.


## 3. Investigate a visual question with FV

Use `fv investigate` when the task is not simply to describe or packetize a source, but to answer a specified visual question.

Examples:

- track a specified object across multiple videos;
- investigate whether two observed objects correspond;
- determine when a relationship changed;
- investigate an appearance/disappearance or ambiguous event;
- inspect multiple media for evidence relevant to one target.

The investigation workspace is **TIR**. Keep hypotheses, competing interpretations, rejected hypotheses, sampling decisions, and unresolved questions there. Promote only evidence-supported conclusions into the authoritative packet records.

A task objective can change where the system spends attention. It cannot supply missing identity, event, motivation, or temporal facts.

`fv investigate` should return the evidence path, relevant source observations, correspondence/component evidence, supported conclusions, and unresolved issues. If the investigation changes the packet, the affected packet must still pass the normal validation lifecycle.

## 4. Assemble partial or overlapping observations

Use `fv assemble` when multiple observations are pieces of a larger visual or spatial view.

Typical inputs include:

- overlapping LiDAR scans;
- telescope fields of view;
- satellite or aerial image tiles;
- microscopy tiles;
- overlapping photographs;
- other partial observations that must be registered into a larger representation.

The assembly process may establish geometric registration, overlap, coordinate alignment, and source correspondence needed to place the observations together. Preserve source provenance and unresolved registration conflicts.

Do not silently convert assembly correspondence into global object identity. If the assembled material requires object reconciliation across packets, use `fv merge`.

## 5. Merge independently produced FV packets

Use `fv merge` when separate FV packets need to be reconciled.

Before normalizing identity, compare:

- source and packet provenance;
- temporal continuity;
- visible structural properties and components;
- spatial relationships;
- preserved snapshots;
- other evidence relevant to the correspondence.

Packet-scoped IDs remain intact during this process. A normalized persistent identity is established only after the evidence supports equivalence.

## 6. Create a new FV packet deliberately

Use `fv create` when the required packet is being constructed from already established FV information or an explicit specification rather than directly analysing a raw source.

The command may be used to create a reconstruction packet or other explicitly supported packet type. It must not manufacture visual facts. Any supplied inference, external knowledge, or test instruction must remain distinguishable from source-derived evidence.

## 7. Create FV packets from existing literature

When a published image or video is the source material, treat the
published material as the source and apply the normal FV analysis
process.

Keep the literature/source identity and the evidence supporting packet
assertions traceable. Do not add scene content because it is typical of
the source category or supplied by outside knowledge.

The resulting packet can then be used independently as a reconstruction
representation.

## 8. Packet closure, identity, and uncertainty

The packet is the reconstruction source of truth.

Once the object/component inventory is locked, reconstruction may not
create new semantic entities to make the result more plausible.

Core distinctions must survive the pipeline:

-   appearance is not automatically an entity;
-   movement is not duplication;
-   off-screen is not deleted;
-   scene membership and identity existence are distinct;
-   unresolved information must not silently become certain;
-   object and background inventories remain distinct.

For video, persistent identity is maintained across scenes and temporal
observations unless evidence supports a genuinely different instance.

When multiple packet-scoped declarations are later merged, do not assume
local IDs are globally identical. Compare declarations, preserve packet
provenance, test continuity and visual evidence, and only then establish
a normalized persistent identity.

**PC as an object database is an experimental capability, not a
validated claim.** Packet-scoped PC IDs use the form
`<packet_id>-<object_id>` before merge.

## 9. Render an image from an FV packet

Give the renderer/generator:

-   the valid FV packet;
-   the FV Working Process Specification;
-   any renderer-specific operational information required by that
    generator.

The process is:

`packet → verify packet → compile into a lossless renderer specification → apply renderer-specific syntax → validate compilation → generate → independently audit`

The compiler may translate syntax for the chosen renderer, but may not
add semantic content, world knowledge, props, motivations, genre
conventions, or other undeclared scene information.

The packet's closed object/component inventory remains authoritative.

A renderer's capabilities and limitations are renderer facts, not FV
packet facts.

## 10. Render a video from an FV packet

Use a valid video packet containing **OI + MSRM + TD** (and **PC** only
where applicable).

The process is:

`packet → verify identities/occupancy/temporal structure → compile → apply renderer-specific syntax → validate compilation → generate → independently audit`

Preserve persistent identities and temporal relationships. Do not create
duplicate identities merely because movement, scene transitions,
occlusion, or rendering difficulty makes reconstruction harder.

Temporal information that is not encoded in TD must not be invented
during reconstruction or temporal querying.

If a temporal question cannot be answered from the recorded TD at its
actual precision, report insufficient temporal information rather than
infer the missing timing from OI, MSRM, scene category, or world
knowledge.

## 11. Prompt compilation is a separate fidelity boundary

The packet-to-prompt/compiler step must be auditable.

A lossless compilation preserves:

-   identity;
-   object/background separation;
-   scene membership;
-   spatial relationships;
-   temporal ordering and transitions;
-   state changes;
-   uncertainty.

Do not use compilation as an opportunity to improve prose by adding
semantic detail.

Compiler deviations should be treated separately from packet errors.
Useful failure classes include:

-   **PC-S** --- semantic addition
-   **PC-D** --- semantic deletion
-   **PC-T** --- temporal alteration
-   **PC-I** --- identity alteration
-   **PC-C** --- contradiction
-   **PC-B** --- background expansion
-   **PC-U** --- uncertainty collapse

## 12. Independently audit the reconstruction

Do not use the generator's explanation as evidence of what its output
contains.

Audit the generated result against the FV packet for:

-   object count and identity continuity;
-   component inventory;
-   scene occupancy;
-   spatial relationships;
-   temporal sequence and state changes;
-   behaviour;
-   style;
-   unsupported semantic additions;
-   unsupported background expansion.

Classify deviations rather than simply asking whether the output "looks
right."

Useful failure classes include:

-   **INV-O** --- object invention
-   **INV-C** --- component invention
-   **ID-S** --- identity split
-   **ID-M** --- identity merge
-   **SP-D** --- spatial deviation
-   **TM-D** --- temporal deviation
-   **BH-D** --- behaviour deviation
-   **ST-D** --- style deviation
-   **DET-U** --- unsupported detail
-   **UNC** --- evaluator uncertainty

Generated imagery is not source evidence unless supported by the FV
packet. Every reconstruction should be independently FV-audited.

## 13. Evidence-grade disputes

A suspected failure is not automatically a confirmed failure.

A material dispute should preserve the relevant source/evidence location
or snapshot, affected record, classification, confidence/resolution
state, and other required dispute fields.

`dispute.json` is the packet-level rendering gate:

-   `none` --- no open dispute blocks rendering;
-   `open` --- rendering is blocked;
-   `resolved` --- rendering may proceed after the required
    human-resolution, AI-reprocessing, and validation lifecycle.

Resolved disputes preserve `dispute.reconciled.json` and the human
resolution separately.

Human resolution does not directly repair the packet. The affected
analysis/packet records must be reprocessed and validated before the
dispute can be cleared.

## 14. Three distinct correctness questions

Keep these separate:

1.  **Source-analysis fidelity** --- was the source analysed correctly?
2.  **Packet fidelity** --- was that analysis converted into the
    intended packet without semantic drift?
3.  **Compilation fidelity** --- was the packet converted into renderer
    instructions without semantic drift?
4.  **Render fidelity** --- did the generator reproduce the packet?
5.  **Evaluation fidelity** --- is the failure claim itself supported by
    evidence?

A failed reconstruction does not automatically mean the packet was
wrong. A correct packet and correct compilation can still produce a
failed reconstruction.

## 15. "I haven't been taught to create an image/video from a packet."

The FV specification already defines the reconstruction task and
packet-to-renderer compilation boundary.

The distinction is:

-   **FV specifies what must be reconstructed.**
-   **The compiler translates that representation into renderer-specific
    syntax.**
-   **The renderer's capabilities and limitations are renderer facts,
    not FV packet facts.**

FV does not require a particular rendering technology. A renderer may
need operational instructions, but those instructions do not authorize
rewriting the FV packet to fit the renderer.

If an AI can analyse the source and create the packet but refuses
reconstruction because it has not been taught a particular generator's
controls, that is a renderer/tool-use limitation, not a missing semantic
definition in FV.

If a renderer cannot work directly from a packet, it may be given a
compiled prompt, but the compilation must remain lossless with respect
to packet semantics.

## Minimal paths

**Source → packet**

`image + FV specification → FV packet`

`video + FV specification → FV packet (OI + MSRM + TD)`

**Packet → image**

`FV image packet → verify → lossless renderer compilation → image reconstruction → independent audit`

**Packet → video**

`FV video packet → verify identity/occupancy/temporal structure → lossless renderer compilation → video reconstruction → independent audit`


### Change log — v0.22

- Added SCP/CCP separation for temporal attention.
- Added change-generator IDs and propagation tracking.
- Added structured EY with current/frameid/previous history.
- Added operational incongruity.
- Added explicit task-objective handling as a separate sampling-priority input.


### Change log — v0.23

- Added component-driven candidature and verification.
- Added targeted search for discriminating components and relationships.
- Clarified preservation of candidate alternatives and forward evidence paths.
- Added the fruit confusion-set pattern for component-based differentiation.

### Change log — v0.24

- Added ambiguous TIR correspondence/identity handling across multiple investigated media.
- Added component-quality labels: high, weak, and transient.
- Added provisional correspondence wording and discriminating-component search for identity resolution.
- Clarified that an unobserved expected component is not negative evidence when the view is uninformative or occluded.
