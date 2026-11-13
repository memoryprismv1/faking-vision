# Faking Vision

## What if AI could see?

What if AI could see, see as in actually see? I know it sounds absurd, but can you actually spoof vision in AI?

Not see in a strict computer vision sense, but see an image or video and analyse it in the way human minds do. Where are the boundaries? What is the object? What are the components of the objects? What is standing out? What makes no sense in the media? What is the placement of the objects? What is the background? And so on.

When we walk into a room, what do we actually see? What is nearby, what is placed where? You might not be doing this consciously, but it happens. You move your vision field, take in more information, create a maplet and add it to the entire map that was produced.

Sounds like pop sci, but it is not. Have you ever thought about how you can get to the bathroom half asleep without walking into ten things?

I spent a month figuring out how human vision works and then how to spoof it in an AI. My aim wasn't a grand plan. It was mostly to get AI to do a better job of media analysis for me. But once you do it, the possibilities become endless.

AI has great computing capacity. Harnessing and leveraging it in the visual sphere has extreme potential that is currently underexplored.

Sometimes when we read, we imagine the whole scene in our heads: the table there, the couch there, the characters here and there, what someone is wearing, what they are doing, etc. Faking Vision does the same thing with an image or video. It converts it into a map composed of different files (natively called an **FV packet**).

An FV packet is auditable, reconstructable, etc.

## What can Faking Vision do?

Faking Vision (FV) can do a lot of things. Things which I have tried:

- Analyse images and videos.
- Editorialise a video for key events only. For example, CCTV footage cleaned down to when things actually happen.
- Take mass overlapping media inputs and stitch together a cohesive structure. This includes sources such as LiDAR, telescopes and other systems which generate a lot of overlapping content.
- Raise disputes when an AI has trouble recognising an object. This requires human intervention.
- Create local object databases from CCTV footage provided in chunks.
- Provide a collaborative space for AI generative work.

I haven't tried dashcam footage yet because I don't have any available files.

FV can do a lot of things, things I would rather leave to a user to find.

## How it works

Faking Vision does not treat visual analysis as a single act of object recognition.

It works through visible components, boundaries, spatial relationships, object properties, temporal evidence and correspondence. Instead of immediately deciding what something is, it can maintain candidates and investigate them further.

A component can lead to multiple possible candidates. Further examination can strengthen or reject those candidates. If the available evidence is insufficient, uncertainty can be retained rather than forcing a recognition.

For video, this also means looking at changes over time, object behaviour, events and relationships between frames.

The output is an FV packet: a structured representation of the visual information, its objects, components, relationships and supporting evidence.

The packet is the source of truth for reconstruction. A reconstruction should not silently introduce objects, components or relationships that were never established in the packet.

## Making Vision and Faking Vision

Faking Vision grew out of my exploration of how human vision works and how some of its processes could be reproduced in AI.

**Making Vision** is the foundational work behind this exploration.

[Making Vision V2 – Reading](https://www.memoryprism.com/readings/making-vision-v2)

Making Vision is the architectural synthesis, not a substitute for empirical research. The [FV research foundations](docs/FV_RESEARCH_FOUNDATIONS.md) map independent perceptual and AI studies to the operational procedures and distinguish findings from design translations and open hypotheses.

**Faking Vision** takes those ideas into an operational framework for visual investigation, media analysis, reconstruction and auditing. It operationalises selected perceptual principles; it does not claim to reproduce the biological visual system.

[Faking Vision – GitHub Repository](https://github.com/memoryprismv1/faking-vision)

## FV operations

FV has a set of distinct operations. They are deliberately separated because analysing, editing, reconstructing and auditing media are different activities.

| Operation         | Purpose                                                                               |
| ----------------- | ------------------------------------------------------------------------------------- |
| Analyse           | Examine an image or video and create an FV packet                                     |
| Investigate       | Examine a particular object, event, relationship or question                          |
| Assemble          | Combine partial or overlapping visual/spatial observations                            |
| Merge             | Reconcile information from separate FV packets                                        |
| Create            | Construct a new packet from established information or a specification                |
| Rebuild / Upgrade | Migrate an existing packet to a newer FV specification                                |
| Edit              | Make intentional changes to packet content                                            |
| Resolve           | Handle disputes, ambiguities and competing interpretations                            |
| Validate          | Check packet structure, contradictions and unresolved issues                          |
| Compile           | Produce a reconstruction specification from a resolved packet                         |
| Audit             | Compare a reconstruction against the packet and, where available, the original source |

These operations are not interchangeable. For example, assembling overlapping observations is different from merging two packets. Validation does not repair a packet, and compilation does not resolve disputes.

## The reconstruction principle

The FV packet is the reconstruction source of truth.

A generator may translate packet information into its own format, but it should not add semantic information from its own learned assumptions.

The resulting media can then be independently audited against the packet. The generator's own explanation is not evidence that its output is correct.

## Agent skill and commands

FV includes an operational agent skill. When the repository is available to the agent, it can read the current authoritative specification directly rather than requiring the user to repeatedly supply it. If the repository is unavailable, the agent must ask for the current specification; the skill's historical v0.24 reference is not a substitute.

The command set is:

```text
fv analyse
fv investigate
fv assemble
fv merge
fv create
fv rebuild (alias: fv upgrade)
fv edit
  fv edit viewpoint (subcommand)
fv resolve
fv validate
fv compile
fv audit
```

For full command details, including syntax, inputs, outputs, options, and operating restrictions, see the [FV command reference](commands.md).

The normal reconstruction workflow is:

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

Not every task requires every operation.

## Repository and documentation

- [GitHub repository](https://github.com/memoryprismv1/faking-vision)
- [Command reference](commands.md)
- [Operation implementation status](docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md)
- [Documentation audit and cleanup baseline](docs/FV_DOCUMENTATION_BASELINE_2026-11-11.md)
- [FV versioning status](docs/FV_VERSIONING_STATUS.md)
- [Artifact contract and schema coverage audit](docs/FV_ARTIFACT_CONTRACT_AUDIT_2026-11-11.md)
- [Research foundations and operational evidence map](docs/FV_RESEARCH_FOUNDATIONS.md)
- [Working process specification](SPECIFICATION/FV_Working_Process_Specification.md)
- [Historical v0.24 specification snapshot](SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md) (reference only)
- [Agent skill](SKILL.md)
- [How to use FV](HOW_TO_USE.md)
- Example packets: [`examples/`](examples/) — see the [examples index](examples/README.md).

The Working Process Specification is the authoritative process document. The agent skill and supporting documentation provide operational access and guidance.

## Example corpus privacy and provenance status

The example media corpus has undergone a visual privacy inventory and a basic embedded-metadata review. The current findings and asset-level observations are recorded in the [example corpus visual privacy audit](tests/acceptance/results/2026-11-12-example-corpus-privacy-audit.md).

- The reviewed inventory contains 305 images and 4 videos. No screenshot of a user's desktop, browser, application window, terminal, or other personal system was identified in the supplied corpus.
- The earlier handwritten-name concern in the Wikimedia desk/display photograph was withdrawn after direct reinspection; the text refers to the historical/public name Mileva Marić Einstein in an exhibit-like setting.
- CCTV observations must be read in their source context. The Commons description identifies the pole-mounted plate as a camera-demonstration test target. Incidental vehicles and public-facing bystanders are not automatically privacy violations; assess clearly legible identifiers and identifiable people in the actual reuse context rather than applying blanket masking.
- The Commons page currently labels the Supercircuits CCTV source public domain under an automated-recording rationale. That rationale is not independently established here; the camera's PTZ/product-demonstration context leaves a source-rights question open.
- The three generated story MP4s contain AAC audio tracks. **Those audio tracks were not listened to or transcribed and are not audio-cleared.** Audio-only names or other personal information therefore remain unchecked. This is a documented limitation, not a claim that personal information is present.
- Source/licence records are uneven across the legacy examples. The five still-image packet READMEs cite Wikimedia Commons pages and CC0/public-domain terms, while several LiDAR, telescope, and CCTV examples lack the original raw inputs or reproducible acquisition/provenance records. See the audit and each packet README before redistribution or claims of reproduced results.

The corpus should not be described as fully privacy-, rights-, or provenance-cleared. The audit distinguishes visual findings, metadata checks, source licensing, and unavailable evidence; one does not substitute for another.

## License

This repository is licensed under **CC BY-NC 4.0**.

Non-commercial copying, sharing, study and adaptation are permitted with attribution under the license. Commercial use requires separate permission.

## Publication

[Faking Vision – Zenodo](https://zenodo.org/records/22672967)  
DOI: [10.5281/zenodo.22672967](https://doi.org/10.5281/zenodo.22672967)
