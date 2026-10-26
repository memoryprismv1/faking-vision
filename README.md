# Faking Vision

Faking Vision (FV) is an operational framework and agent skill for explicit, auditable visual investigation, analysis, reconstruction, and evaluation.

FV provides procedures for examining images and video through visible components, relationships, temporal evidence, candidate formation, correspondence, targeted verification, adaptive sampling, and explicit uncertainty. It is designed to keep observation, interpretation, and commitment separate so that visual reasoning can be inspected rather than hidden inside a model's learned assumptions.

**Publication record:** [Faking Vision on Zenodo](https://zenodo.org/records/22672967) · DOI: [10.5281/zenodo.22672967](https://doi.org/10.5281/zenodo.22672967) · **Working repository and agent skill:** [memoryprismv1/faking-vision](https://github.com/memoryprismv1/faking-vision)

## What FV does

FV supports a complete visual-investigation and reconstruction workflow:

* **Analyse** — examine a raw visual source and produce a structured FV packet.
* **Investigate** — pursue a specified object, event, relationship, correspondence, or question across observations.
* **Assemble** — register and combine partial or overlapping visual/spatial observations into a larger view or representation.
* **Merge** — reconcile independently produced FV packets and normalize object identity only when the evidence supports equivalence.
* **Create** — deliberately construct a new FV packet from established FV information or an explicit specification.
* **Resolve** — resolve packet disputes, ambiguities, and competing interpretations, including the required human-resolution and AI-reconciliation lifecycle.
* **Validate** — check a packet for structural problems, contradictions, missing information, and unresolved disputes.
* **Compile** — translate a resolved and validated packet into a lossless reconstruction specification and, where supported, perform the reconstruction.
* **Audit** — independently evaluate a reconstruction against the FV packet and, where available, the original source.

These operations are deliberately separated. Analysis does not silently become reconstruction; assembly does not silently become identity merge; validation does not repair a packet; resolution does not bypass validation; compilation does not add semantic information; and audit does not rewrite the packet to accommodate a generated result.

## Visual investigation

FV does not treat visual analysis as a single act of recognition.

The process can begin with an observed component and maintain multiple candidates rather than immediately assigning an object name:

**component → candidate set → targeted search → verification or rejection**

Identity investigations similarly begin as correspondence hypotheses. Components used for correspondence are assessed by evidence quality, and correspondence may be strengthened, weakened, rejected, or remain unresolved.

For video, FV can use temporal structure, change, component emergence, behaviour, and evidence yield to determine where further investigation is warranted. Sampling is an analysis strategy, not permission to ignore meaningful changes.

FV preserves uncertainty when the source does not support a conclusion.

## Auditable reconstruction

The FV packet is the reconstruction source of truth.

A reconstruction must not silently add semantic objects, components, relationships, motivations, world knowledge, or other information that was not supplied by the packet.

The packet-to-prompt or packet-to-renderer transformation is itself an auditable boundary. A renderer may translate FV information into its own syntax, but it may not use that translation as an opportunity to fill gaps from its learned world model.

Generated output is evaluated independently. The generator's explanation is not evidence for whether the reconstruction matches the packet.

## Agent skill

`SKILL.md` provides the operational agent interface for FV work.

The FV textarea commands are:

```text
fv analyse
fv investigate
fv assemble
fv merge
fv create
fv resolve
fv validate
fv compile
fv audit
```

The normal reconstruction path is:

```text
analyse / investigate / assemble / merge / create
                    ↓
                 resolve
                    ↓
                validate
                    ↓
                 compile
                    ↓
                  audit
```

Not every job requires every operation. In particular, **assemble** is for putting partial or overlapping observations of a larger view together, while **merge** is for reconciling knowledge contained in separate FV packets. **Compile is a hard fidelity gate:** it does not resolve disputes or repair invalid packets.

The skill is designed so an AI agent can operate FV without requiring the user to repeatedly supply the underlying FV specification. The authoritative process specification remains the governing source for FV procedures and rules.

## Repository structure

**How to use the repository:** `HOW_TO_USE.md`

**Agent skill:** `SKILL.md`

**Authoritative process specification:** `SPECIFICATION/FV_Working_Process_Specification.docx`

**Additional AI-agent guidance:** `SPECIFICATION/FV_Working_Process_Specification_AI_Agent_Additional_Guidance.md`

**Example packets:** `PACKETS/examples/`

The Working Process Specification is the authoritative FV process document. `SKILL.md`, `HOW_TO_USE.md`, and the additional AI-agent guidance provide operational access and supporting guidance; they do not silently override the authoritative specification.

Making Vision is foundational to FV but is maintained separately. It is not duplicated in this repository.

## Core principles

* Observe before naming.
* Do not turn plausibility into evidence.
* Keep observation, interpretation, and packet commitment distinct.
* Treat components as evidence, not identities.
* Preserve candidate alternatives when the evidence supports them.
* Search for discriminating evidence, not only confirming evidence.
* Treat correspondence as a hypothesis before promoting it to identity.
* Preserve uncertainty through the analysis pipeline.
* Do not use later recognition to rewrite the evidence path that existed earlier.
* Treat the packet as the reconstruction source of truth.
* Do not add semantic content during reconstruction.
* Independently audit generated results.

## Relationship to Making Vision

Making Vision provides the foundational visual-perception work behind FV and is maintained separately.
https://www.memoryprism.com/readings/making-vision

FV is the operational framework for applying and testing those ideas in AI visual investigation and reconstruction.

## License

This repository is licensed under **CC BY-NC 4.0**.

It is not an open-source software project. Non-commercial copying, sharing, study, and adaptation are permitted with attribution under the license. Commercial use requires separate permission.

## Image packet editing and environmental participation (v0.25–v0.26 design additions)

The `fv edit` interface and environmental participation rules are documented design additions to the agent workflow. The repository also contains two experimental browser-based tools: `PACKETS/tools/FV_Edit_Visual_Workbench.html` and `PACKETS/tools/FV_Media_Object_Editor_MVP.html`. These are prototypes and have not been fully tested or validated; their presence does not make them authoritative packet writers. The initial `fv edit` workflow scope is image packets only.

```text
fv edit
fv edit <object-name/object-id> --list
fv edit <object-name/object-id> <property-id>
```

- With no arguments, list available objects. With `--list`, list the selected object's available properties. The property form identifies a direct edit; the syntax for supplying a new value remains open.
- Direct edits require a sufficiently unique target and an applicable property. Do not guess between ambiguous objects. Record successful edits in the edit log; do not mark failed or unresolved operations as successful.
- A separate environment packet describes environmental conditions and includes an array of objects undergoing behaviour changes because of those conditions. Environmental edits are logged. Setting a condition does not by itself authorize inventing changes to affected objects.
- The edit log records `edit_base: singleton` for a single-object target and `edit_base: collection` for a collection target. Collections are environment-only for now. Preserve prior entries and provenance when logs are accumulated across appended packets.
- Packets carry a dedicated FV version file identifying the version against which they are mapped. The exact filename and schema remain to be standardized. An unversioned packet is legacy and is treated as mapped against an older FV version. A missing environment packet is acceptable for a legacy packet and can be ignored. Run `fv edit` on an older packet to enter the update workflow without falsifying its legacy provenance.
- The experimental Media Object Editor MVP accepts a video and FV JSON packet, supports manually drawn polygon keyframes and basic property edits, and can export packet data and a WebM recording where the browser supports it. It does not provide automatic segmentation or persistent object tracking; its visual tint is not semantic object-aware reconstruction. Interpolation can fail across scene cuts or major shape changes, and packet exports and visual output require separate review. The Visual Workbench is also experimental. Treat both tools as prototypes requiring evaluation, not validated or canonical FV implementations.

The v0.26 environmental-participation rules additionally distinguish changes to environment conditions from affected-object responses:

- Classify passive state/appearance changes separately from active behaviour or location changes, for each edit event rather than as a permanent object label.
- Record condition and stress in `ENVIRONMENT.json`, supported object state/behaviour in `OI.json`, spatial changes in `MSRM.json`, and the edit plus provenance/validation information in `edit_log.json`.
- Treat environmental stress as a cue to inspect affected objects, not proof of a particular behaviour. Preserve uncertainty and do not invent a response from typical expectations alone.
- Validate structural consistency and semantic expectations separately from the independent visual audit; an edit log is not proof that the resulting image matches the intended state.
- Preserve legacy packet provenance when mapping older packets to a later FV version.

The environment packet schema, edit-value syntax, exact edit-log fields, version-file schema, and dependent-record update rules remain open design items.
