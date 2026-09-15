# How to Use Faking Vision

This guide is a quick route into the repository. The **FV Working
Process Specification is authoritative**. This guide does not replace
it.

## 1. Analyse an image with FV

Give the AI the source image together with:

`SPECIFICATION/FV_Working_Process_Specification_v0.19.docx`

The image-analysis path is:

`source → observation → candidate generation → entity/component/appearance resolution → packet promotion → packet construction → validation → export`

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

`SPECIFICATION/FV_Working_Process_Specification_v0.19.docx`

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

## 3. Create FV packets from existing literature

When a published image or video is the source material, treat the
published material as the source and apply the normal FV analysis
process.

Keep the literature/source identity and the evidence supporting packet
assertions traceable. Do not add scene content because it is typical of
the source category or supplied by outside knowledge.

The resulting packet can then be used independently as a reconstruction
representation.

## 4. Packet closure, identity, and uncertainty

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

## 5. Render an image from an FV packet

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

## 6. Render a video from an FV packet

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

## 7. Prompt compilation is a separate fidelity boundary

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

## 8. Independently audit the reconstruction

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

## 9. Evidence-grade disputes

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

## 10. Three distinct correctness questions

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

## 11. "I haven't been taught to create an image/video from a packet."

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
