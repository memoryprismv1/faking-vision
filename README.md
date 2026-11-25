# Faking Vision (FV)

**Faking Vision (FV) is a way to leverage AI capabilities on media.** It turns media into structured information that AI systems can use to do substantially more than describe, caption, or generate images and video.

Its central output is an **AI-usable object database**, carried in portable FV packets: structured records of entities, components, observable properties, spatial and temporal relationships, events, viewpoints, evidence, uncertainty and provenance. The records can be investigated, queried through AI, compared across sources, assembled, merged, transformed and passed to other AI capabilities as working information.

The point is not simply to understand a piece of media. It is to make the information inside media available for further work. Once objects, relationships and events have been extracted into a structured representation, an AI agent can reason over that representation, connect it to other sources, answer questions, detect patterns, build timelines, support decisions, or use it as input to other tools and workflows.

> **Media in → structured object knowledge → many kinds of AI work out.**

Faking Vision is inspired by ideas explored in biological vision, but it is not limited to imitating human seeing. It is about giving AI a richer, persistent and reusable working representation of the world depicted or measured by media. Generative images and video are among the possible outputs and test environments—not the purpose or boundary of FV.

## From media to an AI object database

A caption is an answer for a reader. An FV packet is structured working material for AI systems.

FV extracts and organises what the source supports: objects and their components, properties, boundaries, positions, relationships, state changes, movement, events, viewpoints, evidence and uncertainty. It preserves identities and links across time or sources only when the evidence supports them. It also preserves what is unknown, disputed, off-screen or outside the available coverage.

That changes the kind of work an AI can do. Instead of repeatedly starting from raw media—or relying on a fluent paragraph that has thrown away most of the detail—an agent can work against a structured body of media-derived knowledge. It can ask questions of it, investigate particular entities, compare observations, follow relationships, build timelines, reconcile records, or pass relevant parts to another capability.

The packet is portable. It can be used by different AI agents and tools without requiring each one to rediscover the source from scratch. It is not a claim that FV already runs a database server, provides unrestricted SQL, or implements every downstream application. The object database is the structured knowledge resource represented by FV packets; agents and other tools can operate on that resource.

FV separates observation, interpretation, investigation and packet commitment. A plausible object is not automatically an established entity. A question can direct attention towards a part of the media, but it cannot supply the answer. If the evidence is insufficient, the uncertainty or dispute remains visible.

## What this makes possible

The same underlying object records can support very different jobs. These are examples of applications and compositions enabled by the FV approach, not claims that every application is already implemented as a turnkey feature.

- **Searchable media archives:** find every appearance of an object, event, configuration or visual condition across large collections without manually watching every file.
- **Cross-camera and cross-source investigation:** follow supported object continuity, compare observations, reconcile independent packets and expose gaps or conflicting accounts.
- **Operational intelligence:** turn warehouse, factory, construction-site, transport or retail media into records of assets, movement, occupancy, equipment states, process steps and exceptions.
- **Ecology and field research:** organise observations of organisms, behaviour, habitat conditions and change across cameras, locations and time.
- **Science and remote observation:** work with telescope imagery, scans, maps and other sensor-derived material as structured observations rather than isolated pictures.
- **Historical and cultural research:** compare objects, structures, scenes and changes across archival photographs, documents and recordings.
- **Forensic and journalistic work:** build evidence-linked timelines, compare accounts against recorded events, and keep observations distinct from hypotheses.
- **Accessibility and navigation:** derive structured descriptions of spaces, obstacles, routes, objects and changing conditions for other systems to use.
- **AI orchestration:** give specialist agents a shared object-and-event representation so one agent can investigate, another can compare, another can model consequences, and another can produce a report or visualisation.
- **Simulation and reconstruction:** use the structured representation as input to renderers, simulators, digital-twin workflows or generative systems, then compare their outputs with the source-grounded records.

The more interesting applications often combine several of these: for example, an archive can become searchable, its events can be placed on timelines, recurring patterns can be detected, and the resulting evidence can feed a separate planning or research agent.

The same reach creates responsibility. Media-derived records can be wrong, incomplete or sensitive. Keep source provenance, uncertainty, access controls and purpose limitations attached to the data. Do not turn an appearance match into a real-world identity claim, or treat a detected pattern as proof of intent or wrongdoing.

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

## Reconstruction is one downstream operation

Reconstruction is one way to consume the object database: another system can render or simulate the represented scene from an FV packet. It is also a useful test of whether the packet contains enough information, but it is only one of many possible downstream operations.

The packet is the reconstruction source of truth. A renderer may need the information translated into its own syntax, but that translation must not add semantic content. A reconstruction should not introduce entities, components or relationships that the packet never established, nor omit material information that the packet did establish.

The resulting media can be independently audited against the packet. A failed reconstruction or audit is useful diagnostic information: it may expose missing analysis, an ambiguous packet, a renderer limitation or an output deviation. It is not a reason to rewrite the source evidence to fit the generated result.

FV also specifies downstream editing of packet content, including environmental and viewpoint changes, with an edit record. These are controlled operations on an analysed representation, not a general-purpose image/video editing suite. An intended one-variable change must still be checked; it must not be assumed that nothing else changed.

**Generative media is one consumer of FV's structured media knowledge. The larger purpose is to make that knowledge useful across many AI tasks and systems.**

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
- It is not limited to image/video generation, editing, captioning or visual analysis as an end in itself.

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
