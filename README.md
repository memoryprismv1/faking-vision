# Faking Vision

Faking Vision (FV) is an operational framework for converting visual observations into a portable structured information packet and testing whether a reconstruction system can reproduce that supplied representation without silently substituting its own learned world model.

## Start here

**How to use the repository:** `HOW_TO_USE.md`

**Authoritative process specification:** `SPECIFICATION/FV_Working_Process_Specification.docx`

**Additional AI-agent guidance:** `SPECIFICATION/FV_Working_Process_Specification_AI_Agent_Additional_Guidance.md`

**Example packets:** `PACKETS/examples/`

The Working Process Specification is the authoritative FV process document in this repository. The AI-agent guidance is supplementary; it does not replace, redefine, or shorten the specification.

Making Vision is foundational to FV but is maintained separately. It is not duplicated in this repository.

## Core reconstruction rule

The FV packet is the reconstruction source of truth. Reconstruction must not silently add semantic objects or components that are not supplied by the packet.

## License

This repository is licensed under **CC BY-NC 4.0**. It is not an open-source software project. Non-commercial copying, sharing, study, and adaptation are permitted with attribution under the license. Commercial use requires separate permission.
