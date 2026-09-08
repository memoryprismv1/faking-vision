FV_OMNI_001 — Old MacDonald Had a Farm

Packet files:
- PC.json  project constants / canonical declarations
- OI.json  scene object instances, states and behaviours
- MSRM.json scene spatial organization and relationships
- TD.json  temporal ordering, transitions and changes
- AUDIO_COMPANION.txt non-FV audio direction

Reconstruction contract:
The packet is the source of truth. Renderer consumes structured scene instructions, not the original source or a prose prompt.
Core video packet: OI + MSRM + TD. PC is optional and used here for project-wide invariant declarations.

Experiment purpose:
First Omni test of FV structured representation -> AI video reconstruction. Preserve persistent identity, object inventory, spatial relationships and temporal carryover before introducing adversarial modifications.
