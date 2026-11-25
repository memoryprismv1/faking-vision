# Faking Vision (FV)

**Faking Vision is a visual analyser.** It turns images and video into structured, source-grounded information that can be inspected, questioned, compared, validated and reused.

Its central output is not a generated image, a caption, or a prompt. It is an **FV packet**: a collection of files that records what the source supports about the scene, its entities, components, spatial relationships, temporal changes, uncertainties and evidence.

FV is built around a simple question:

> Can an AI account for what is actually present in visual media, show where its claims came from, and preserve what it does not know?

Reconstruction and generative-media workflows are downstream uses of that analysis. They are useful tests of whether the packet contains enough information, but they are not the product's centre of gravity. FV is not an Adobe-like media editor or a generative-media suite.

## Why analyse rather than caption?

A caption can sound convincing while leaving the important questions unanswered:

- Which entities are actually visible?
- What are their boundaries, components and observable properties?
- Where are they in relation to one another?
- What changes over time, and when?
- Is an apparent change a new object, a change of state, movement, or a change in visibility?
- Which claims are directly supported by the source, which are interpretations, and which remain uncertain?
- What did the camera not see?

A fluent description can omit objects, merge identities, invent plausible details, mistake appearance for structure, or turn an uncertain interpretation into a fact. FV is intended to make those gaps visible.

It separates observation, interpretation, investigation and packet commitment. A plausible object is not automatically an established entity. A question can direct attention towards a part of the media, but it cannot supply the answer. If the evidence is insufficient, the uncertainty or dispute remains visible.

## The FV packet

An FV packet is the structured analysis result. It is a folder of files, normally delivered as a ZIP when file creation and packaging are available. Prose explaining the result is supplementary; it is not a substitute for the packet.

The packet records the information authorised for downstream use, together with its evidence and limitations. Core records include:

- **OI — Object Inventory:** committed entities, stable IDs, observable appearance and components. Unresolved candidates do not become committed objects merely because one interpretation seems likely.
- **MSRM — Map Spatial Relationship Manager:** supported spatial placement and relationships between entities. Relationships should not be replaced with invented coordinates or precision the source cannot provide.
- **TD — Temporal Data:** the temporal record for video, including intervals, events, state changes, movement, identity continuity and coverage limitations.
- **TIR — Temporal Investigation Record:** the investigative workspace for hypotheses, competing and rejected interpretations, sampling decisions, evidence paths and unresolved questions.
- **ENVIRONMENT — Environment:** recorded environmental conditions and their supported effects, including the distinction between environmental stress levels and what those conditions do or do not change.
- **viewpoint — Viewpoint:** what the camera observed and from where, including the limits of its field of view. Unknown camera position or orientation stays unknown.
- **packet_provenance — Provenance:** source and packet history, including available source identifiers, hashes, authorship and timestamps. Missing provenance is not to be invented.
- **dispute — Disputes:** open questions, competing interpretations and what evidence or decision would resolve them.

The exact required files and fields depend on the source and the authoritative specification. The list above is an orientation, not a substitute schema.

A packet distinguishes what is committed from what is still under investigation. Unresolved candidates and disputes remain outside the committed inventory until the evidence supports a decision. The packet is intended to be portable and checkable: material claims should be traceable to source evidence or explicitly retained as inference, uncertainty or unresolved work.

## What FV analyses

### Images

For a still image, FV builds a structured account of the frame: entities, visible components, appearance, boundaries, spatial relationships, viewpoint, evidence and uncertainty. It should preserve useful visual structure even when the identity of something cannot yet be established.

### Video and CCTV

Video analysis adds time. FV's specified temporal approach uses **Adaptive Temporal Decomposition**: it looks for meaningful change and allocates closer inspection where the evidence indicates that more detail is needed, rather than assuming every moment deserves the same sampling density.

The temporal record can represent:

- appearances, disappearances and reappearances;
- movement, interaction and state changes;
- identity continuity, including cases where continuity is uncertain;
- event timing and intervals;
- camera coverage gaps and periods where absence cannot safely be claimed.

This is particularly relevant to long CCTV recordings: much of a recording may be uneventful, while a short interval matters greatly. The aim is to make the relevant events investigable without losing the evidence and coverage limits around them.

For sequential or chunked media, the specified workflow can analyse individual chunks and then reconcile them into a larger packet or object inventory. Persistent identity across chunks must be tested; similar appearance or a convenient matching ID is not proof that two observations show the same object.

### Investigation

`fv investigate` directs analysis towards a question, object, event or relationship in supplied media. For example:

- What did this person, animal or vehicle do, and when?
- Does this object appear anywhere in the supplied footage?
- Did a delivery person appear during the period the camera actually covered?
- What changed in this interval?

The question changes attention and sampling priority, not the evidence rules. Findings should include relevant timing and source support. An absence claim is justified only when the available coverage is sufficient; otherwise the result must remain inconclusive or qualified.

### Audio in video

FV's specified audio procedure treats transcription as a provisional source of investigative cues, not as automatic visual fact. Transcription fidelity is assessed separately from visual support, timing and context. Audio can direct attention to a moment; a claim enters the authoritative visual/temporal record only when the relevant source evidence supports it.

### Multiple views and independent packets

FV distinguishes two operations that are easy to confuse:

- **Assemble** integrates partial or overlapping observations into a larger spatial/visual representation, preserving viewpoint, coverage, overlap, gaps and uncertain correspondences.
- **Merge** reconciles independently produced FV packets, testing identity and preserving packet provenance rather than silently combining similar-looking entities.

These operations are not simply image stitching or matching IDs.

## FV operations

FV uses distinct operations because analysing, investigating, assembling, merging, editing, resolving and validating are different jobs.

| Operation | Purpose |
|---|---|
| `fv analyse` | Analyse a raw image or video source and create an FV packet |
| `fv investigate` | Investigate an object, event, relationship or question in supplied media |
| `fv assemble` | Integrate partial or overlapping visual/spatial observations |
| `fv merge` | Reconcile independently produced FV packets |
| `fv create` | Construct a packet from established information or an explicit specification |
| `fv rebuild` / `fv upgrade` | Migrate an existing packet to the current authoritative specification or an explicit target |
| `fv edit` | Make an intentional, recorded change to packet content |
| `fv resolve` | Handle disputes, ambiguities and competing interpretations through the required lifecycle |
| `fv validate` | Assess packet structure, evidence, disputes and readiness |
| `fv compile` | Translate a resolved, validated packet into a renderer-specific reconstruction specification |
| `fv audit` | Independently compare a reconstruction with the packet it was meant to represent |

The operations are deliberately not interchangeable. Validation reports readiness; it does not silently repair a packet. Compilation translates the packet; it does not resolve disputes or add world knowledge. Audit checks the result; a generator's own explanation is not evidence that its output is correct.

## Reconstruction is a test, not the product

A useful test of an analysis packet is whether another system can reconstruct the represented scene from the packet alone without quietly filling gaps with its own assumptions.

The packet is the reconstruction source of truth. A renderer may need the information translated into its own syntax, but that translation must not add semantic content. A reconstruction should not introduce entities, components or relationships that the packet never established, nor omit material information that the packet did establish.

The resulting media can be independently audited against the packet. A failed reconstruction or audit is useful diagnostic information: it may expose missing analysis, an ambiguous packet, a renderer limitation or an output deviation. It is not a reason to rewrite the source evidence to fit the generated result.

FV also specifies downstream editing of packet content, including environmental and viewpoint changes, with an edit record. These are controlled operations on an analysed representation, not a general-purpose image/video editing suite. An intended one-variable change must still be checked; it must not be assumed that nothing else changed.

**Generative media is therefore a downstream consumer and test environment for FV analysis—not the definition of Faking Vision.**

## Making Vision and Faking Vision

Faking Vision grew out of an exploration of how biological vision works and how selected aspects of that processing architecture might be made operational in AI.

**Making Vision** is the foundational architectural synthesis.

[Making Vision V2 – Reading](https://www.memoryprism.com/readings/making-vision-v2)

Making Vision considers how current sensory information interacts with existing knowledge, spatial structure, expectations, internal state and selective allocation of processing. It is a working synthesis, not an established published biological theory and not a claim that FV reproduces the biological visual system.

Faking Vision takes selected ideas into an operational framework for analysing visual media. The repository's [FV research foundations](docs/FV_RESEARCH_FOUNDATIONS.md) map independent perceptual and AI research to FV procedures and distinguish empirical findings from design translations and open hypotheses.

## What FV does not claim

- It does not turn a plausible interpretation into source evidence.
- It does not invent identity, motive, timing, camera geometry or object properties that the source does not support.
- It does not silently resolve disputes or repair an invalid packet.
- It does not treat a task objective, transcript or generator output as proof of what the original media contains.
- It does not claim that every specified operation has a general-purpose software implementation.
- It does not claim to reproduce the biological visual system.
- It does not make a packet rights-cleared, privacy-cleared, museum-verified or true beyond its source. Source rights, provenance and reuse context require their own checks.
- It is not a generative-media product whose primary purpose is to create or edit images and video.

## How to use FV

FV commands are **AI-agent instructions**, not commands for a standalone shell program or an installed FV CLI. Issue them in a conversation or environment where the FV agent skill is available. Ordinary language supplies the task, target, constraints and attached media.

Examples:

```text
fv analyse this image
fv analyse this video, paying particular attention to the traffic light
fv investigate what the kitten did in this video and when
fv investigate whether a white dog appears anywhere in this image
fv investigate whether a delivery person appeared during the covered CCTV period
fv assemble these images into one landscape
fv analyse these three one-hour CCTV chunks and merge them into one object database
fv merge these two packets
fv validate this packet
```

For full command syntax, inputs, outputs, options and operating restrictions, see the [FV command reference](commands.md). The [How to Use FV guide](HOW_TO_USE.md) provides a practical route through common tasks.

The [FV Working Process Specification](SPECIFICATION/FV_Working_Process_Specification.md) is authoritative. The agent skill and supporting documentation provide operational access and guidance. When the current specification is unavailable, an agent must say so and request it; a historical snapshot is not a substitute.

## Specification and implementation status

The repository distinguishes what is specified from what has been implemented or demonstrated. An operation appearing in the command reference means its process is defined; it does not, by itself, mean a general-purpose engine or standalone executable exists.

The [operation implementation status](docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md) records the current evidence and limitations. In brief, FV's command interface is agent-level; repository tools and browser prototypes support bounded tasks, not a universal FV runtime or authoritative semantic validator for arbitrary packets. Some defined agent-level acceptance cases have been exercised, but those results must not be generalized beyond the cases tested.

The [FV versioning status](docs/FV_VERSIONING_STATUS.md) explains the current specification's version labels. The authoritative specification has a v0.24 base with later normative additions labelled v0.26 and v0.27; no consolidated release number is assigned.

## Repository documentation

- [FV command reference](commands.md)
- [How to Use FV](HOW_TO_USE.md)
- [Agent skill](SKILL.md)
- [Working Process Specification](SPECIFICATION/FV_Working_Process_Specification.md)
- [Historical v0.24 specification snapshot](SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md) — reference only
- [FV research foundations and operational evidence map](docs/FV_RESEARCH_FOUNDATIONS.md)
- [Operation implementation status](docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md)
- [Documentation audit and cleanup baseline](docs/FV_DOCUMENTATION_BASELINE_2026-11-11.md)
- [FV versioning status](docs/FV_VERSIONING_STATUS.md)
- [Artifact contract and schema coverage audit](docs/FV_ARTIFACT_CONTRACT_AUDIT_2026-11-11.md)
- [Packet format and provenance guide](docs/FV_PACKET_GUIDE.md)
- [Example packets and evidence index](examples/README.md)
- [Meta example contribution catalogue](docs/META_FV_EXAMPLES_CATALOG.md)
- Repository utilities and prototypes: `TOOLS/`

## Example corpus: privacy, rights and provenance

The example media corpus has undergone a visual privacy inventory and a basic embedded-metadata review. The findings and asset-level observations are recorded in the [example corpus visual privacy audit](tests/acceptance/results/2026-11-12-example-corpus-privacy-audit.md).

The reviewed inventory contains 305 images and 4 videos. The audit did not identify screenshots of a user's desktop, browser, application window, terminal or other personal system in the supplied corpus. It also records the context for CCTV demonstration material, the withdrawal of an earlier handwritten-name concern after reinspection, and a source-rights question concerning the Supercircuits CCTV material whose public-domain rationale was not independently established.

Three generated story MP4s contain AAC audio tracks that were not listened to or transcribed and are **not audio-cleared**. Source and licence records are uneven across legacy examples; several LiDAR, telescope and CCTV examples lack original raw inputs or reproducible acquisition/provenance records.

The corpus must therefore not be described as fully privacy-, rights- or provenance-cleared. The audit distinguishes visual findings, metadata checks, source licensing and unavailable evidence; one does not substitute for another. Consult the audit and each packet README before redistribution or claims that an example has been independently reproduced.

## License

This repository is licensed under **CC BY-NC 4.0**.

Non-commercial copying, sharing, study and adaptation are permitted with attribution under the license. Commercial use requires separate permission.

## Publication

[Faking Vision – Zenodo](https://zenodo.org/records/22672967)  
DOI: [10.5281/zenodo.22672967](https://doi.org/10.5281/zenodo.22672967)
