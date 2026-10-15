FAKING VISION — CCTV PART 1 PACKET

Packet ID: PKT-CCTV-001
Source segment: part_01.webm (included at packet root; preserved source segment)
Source ID: SRC-CCTV-001-PART-01
Duration: 105.600 s
Frame size/rate: 1920x1080 at 30 fps; VP9 source stream; VP9 source stream

Operation: manual FV-style analyse procedure; no FV executable/CLI was invoked. This packet has not been certified as exhaustive or compilation-ready.

Contents
- OI.json: object/instance inventory.
- MSRM.json: qualitative spatial relationships and baseline positions.
- TD.json: authoritative temporal baseline and evidence-supported differences.
- PC.json: packet-scoped object declarations for later FV merge; no global IDs assigned.
- TIR.json: temporal investigation record, sampling decisions, hypotheses, evidence paths and unresolved questions.
- snapshot/verification/: preserved source frames selected by the global, random reconnaissance and adaptive passes.
- snapshot/objs/: preserved source crops for the principal moving candidates.
- snapshot/manifest.json: snapshot provenance and source coordinates.

Method note
The temporal procedure used a 4-second global pass, a separate 14-position odd-second random reconnaissance pass, and local adaptive insertions around observed perturbations. A preliminary 1-second contact-sheet scout was used only to locate candidate activity regions and is disclosed in TIR. Every exported evidence frame has a source timestamp/frame index and is represented in TIR. No object detector, classifier, tracker or OCR was used.

Known limitations
The parking scene is dense; some vehicles overlap or are cropped at the frame boundaries. The 45-vehicle baseline inventory is manually enumerated and not independently proven exhaustive. Small distant objects and precise movement boundaries remain uncertain. The interaction between the pedestrian and silver sedan is unresolved; no contact is asserted. Audio was not analysed for this visual experiment. These limitations are not silently repaired.

Disputes: OPEN — inventory completeness and distant-object ambiguity require further review before any claim of exhaustive reconstruction coverage.

OPERATIONAL DISPOSITION (Making Vision v1/v2)
See FV_OPERATIONAL_DISPOSITION.txt and dispute.json. Stable/background inventory and low-priority identity questions may be DEFERRED rather than treated as blocking. This is chunk-local only: later chunks may promote the same object or question again. Deferred is not deleted, forgotten, or globally resolved. Active event/view-change investigations remain open.

Source integrity note
The included part_01.webm is the source segment used to verify the packet snapshot time/frame mapping. Packet analysis remains provisional: the retained sampling is not a full frame-by-frame inspection, and the open dispute gate remains in force.
