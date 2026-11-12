FV_OMNI_001 — Old MacDonald Had a Farm

## Packet purpose

A structured visual reconstruction target for a five-scene Omni video experiment. The packet is intended to preserve persistent identity, object inventory, spatial relationships, and temporal carryover across the declared scenes.

## Packet files

- PC.json — project-wide invariants and declared object inventory.
- OI.json — scene object instances, states, and behaviours.
- MSRM.json — scene spatial organization and relationships.
- TD.json — temporal ordering, transitions, and changes.
- AUDIO_COMPANION.txt — non-FV direction for a possible generated soundtrack.

## Reconstruction contract

The packet is the source of truth for the visual target. A renderer consumes structured scene instructions, not the original source or a prose prompt. The audio companion is a direction note only; it is not source audio, a transcript, or evidence about the visual scenes.

## Evidence and output status

The repository contains `omni_rendering.mp4`, a generated experiment output. It does not contain a source video or source-audio recording used to derive the packet. This is a packet-to-generation experiment, not an example of source-media analysis or audio-enabled FV investigation.

No independent packet-to-video audit report is included here. Do not treat the presence of the rendered MP4 as proof that the output satisfies every packet constraint.


## Packet consistency review

The OI declares the farm landmarks present across all five scenes, and TD explicitly says the environment persists. The original MSRM only placed those landmarks in scene_01, and omitted the farmer from scene_04. The spatial records have been amended to carry the same global farm landmarks through scenes_02–05 and to retain the farmer in the widened scene_04 view. Where the exact screen position is not specified, the record says so rather than inventing one. This is a structural correction; the generated MP4 has not been independently audited against the packet.


DISPUTES: NONE

LEGACY/TARGET METADATA BOUNDARY
This is a packet-to-generation experiment, not a source-media analysis packet. It has no root-level `viewpoint.json` or `packet_provenance.json`; no source-camera geometry or source-media provenance is asserted. The generated MP4 is not independently audited against the packet, and the presence of the output does not establish compilation or reconstruction correctness.
