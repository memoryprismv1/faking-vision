# How to Use Faking Vision

This guide is a quick route into the repository. The **FV Working Process Specification is authoritative**. This guide does not replace it.

## 1. Analyse an image or video with FV

Give the AI the source image or video together with:

`SPECIFICATION/FV_Working_Process_Specification.docx`

For image analysis, the process produces an FV packet using **OI + MSRM**, with optional **PC**.

For video analysis, the process produces **OI + MSRM + TD**, with optional **PC**. TD is required for video reconstruction targets.

The analysis proceeds from source intake and visible structure through candidate generation, entity/component/appearance decisions, identity resolution, packet promotion, packet construction, validation, and export.

For video, establish temporal units, sample more densely around meaningful changes, track persistent identities, and distinguish movement, occlusion, off-screen absence, and new instances.

Use the AI-agent additional guidance when useful, but do not treat it as a substitute for the specification.

## 2. Create FV packets from existing literature

When a published image or video is the source material, treat the published material as the source and apply the FV analysis process to it.

Keep the literature/source identity and the evidence supporting packet assertions traceable. Do not add scene content merely because it is typical of the source category or because it is supplied by outside knowledge.

The resulting packet can then be used independently as a reconstruction representation.

## 3. Render an image from an FV packet

Give the renderer/generator:

- the valid FV packet;
- the FV Working Process Specification;
- any renderer-specific information required by that particular generator.

The process is:

`packet → verify packet → compile into a lossless renderer specification → apply renderer-specific syntax → validate compilation → generate → independently audit`

The renderer instruction may translate syntax for the chosen generator, but may not add world knowledge or semantic content.

The packet's closed object/component inventory remains authoritative.

## 4. Render a video from an FV packet

Use a valid video packet containing **OI + MSRM + TD** (and PC only where applicable).

The process is:

`packet → verify identities/occupancy/temporal structure → compile → apply renderer-specific syntax → validate compilation → generate → independently audit`

Preserve persistent identities and temporal relationships. Do not create duplicate identities merely because movement, scene transitions, occlusion, or rendering difficulty makes reconstruction harder.

Temporal information that is not encoded in TD must not be invented during reconstruction or temporal querying.

## 5. Hotfix: “I haven't been taught to create an image/video from a packet.”

The FV specification already defines the reconstruction task and the packet-to-renderer compilation step.

The distinction is:

- **FV specifies what must be reconstructed.**
- **The compiler translates that representation into the syntax needed by a particular renderer.**
- **The renderer's own capabilities and limitations are renderer facts, not FV packet facts.**

FV does not require a particular rendering technology. A renderer that needs its own operational instructions may need those instructions, but that does not authorize rewriting the FV packet to fit the renderer.

If an AI can analyse the source and create the packet but refuses to attempt reconstruction because it has not been “taught” the controls of a particular image/video generator, that is a renderer/tool-use limitation, not a missing semantic definition in the FV packet. 

A generator can be asked to create a prompt for video from packet if renderer is unable to work directly with packet. 

## Minimal paths

**Source → packet**

`image/video + FV specification → FV packet`

**Packet → image**

`FV image packet → renderer compilation → image reconstruction → audit`

**Packet → video**

`FV video packet → temporal/identity handling → renderer compilation → video reconstruction → audit`
