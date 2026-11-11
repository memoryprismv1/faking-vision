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

[Making Vision – Reading](https://www.memoryprism.com/readings/making-vision)

**Faking Vision** takes those ideas into an operational framework for visual investigation, media analysis, reconstruction and auditing.

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

FV includes an operational agent skill so that an AI agent can perform FV operations without requiring the user to repeatedly supply the underlying specifications.

The command set is:

```text
fv analyse
fv investigate
fv assemble
fv merge
fv create
fv rebuild (alias: fv upgrade)
fv edit
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
                 resolve
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
- [Working process specification](SPECIFICATION/FV_Working_Process_Specification.md)
- [Agent skill](SKILL.md)
- [How to use FV](HOW_TO_USE.md)
- Example packets: `PACKETS/examples/`

The Working Process Specification is the authoritative process document. The agent skill and supporting documentation provide operational access and guidance.

## License

This repository is licensed under **CC BY-NC 4.0**.

Non-commercial copying, sharing, study and adaptation are permitted with attribution under the license. Commercial use requires separate permission.

## Publication

[Faking Vision – Zenodo](https://zenodo.org/records/22672967)  
DOI: [10.5281/zenodo.22672967](https://doi.org/10.5281/zenodo.22672967)
