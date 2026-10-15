FAKING VISION — FV PACKET

Packet ID: PKT-CCTV-003
Operation: fv analyse
Specification: FV Working Process Specification v0.24
Status: Initial analysis packet; independent of PKT-CCTV-001 and PKT-CCTV-002; not merged, validated, or compiled.

SOURCE INTAKE
- Packet source: part_03.mp4
- Parent source: BLK-HDPTZ12_Security_Camera_Parking_Lot_Surveillance_Video (1).webm
- Parent-source interval: approximately 211.138667–316.708 seconds (Part 3)
- Packet-source duration: 105.554 seconds
- Video: 1920 × 1080, H.264, reported frame rate 30/1
- Audio stream present: True. Audio was not intentionally included or used as evidence.
- SHA-256 of part_03.mp4: e779b27ab18369e29c9484c99fbecd9ba4c5c2820eb4c3127da426e0c67f9c10
- This is a re-encoded duration split of the parent video, not a bit-for-bit segment of the original WebM.

FV METHOD AND EVIDENCE
- Sampled at nominal one-second intervals from t=0 through t=104; 105 full-frame snapshots are retained in snapshot/verification/. A t=105 sample was not decodable from the split file.
- Eight source-derived, unannotated crops are retained in snapshot/objs/.
- Manual FV visual observation only: no built-in object detector, image classifier, automated tracker, OCR, or automated visual inference was used. Code was used only to extract/copy snapshots, crop specified regions, hash files and package the artifact.
- Times are relative to part_03.mp4, nominal to the nearest sampled second; they are not original CCTV wall-clock times. Parent-relative time is approximately packet-local time + 211.138667 seconds.
- The opening contains a tight view of two placards attached to a pole; the camera view widens during the first several seconds, then a wide parking-lot view persists. This is represented as camera/view change, not as objects entering or leaving the scene.
- A light-coloured elongated vehicle-like form changes position in the later samples. Exact route and identity correspondence remain uncertain.

PACKET CONTENTS
- OI.json: 19 packet-scoped object/region candidates; repeated vehicles are partly grouped or explicitly unresolved rather than assigned unsupported individual identities.
- MSRM.json: scene intervals and coarse relative spatial organization across the changing camera view.
- TD.json: ordered temporal observations with snapshot evidence references and explicit sampling limits.
- snapshot/manifest.json: source lineage, timestamps, hashes and crop provenance.
- snapshot/verification/: 105 full-frame snapshots.
- snapshot/objs/: eight source-derived evidence crops.

BOUNDARIES
- This packet is not merged with Part 1 or Part 2. IDs are packet-local and must not be treated as cross-packet identities.
- This is initial FV analysis output. Validation, investigation, merge and compilation remain separate operations.
- No vehicle make/model, person identity, placard meaning, exact world coordinates, or unsupported persistent vehicle identity is asserted.

DISPUTES: NONE at packet level. Local uncertainties and provisional correspondence are preserved in OI/TD; no identity merge or reconstruction compilation is authorized by this statement.


HONEST STATUS ADDENDUM (2026-10-14)
- PC.json and TIR.json added to make packet-local identity declarations and investigation limits explicit.
- dispute.json contains three open issues; merge gate remains blocked.
- VALIDATION_REPORT.txt records structural checks only.
- The 105 one-second snapshots are not proof of exhaustive object coverage or complete event capture.
- No FV executable/CLI was run. Do not describe this packet as fully analysed, validated, merged, or compiled.

OPERATIONAL DISPOSITION (Making Vision v1/v2)
See FV_OPERATIONAL_DISPOSITION.txt and dispute.json. Stable/background inventory and low-priority identity questions may be DEFERRED rather than treated as blocking. This is chunk-local only: later chunks may promote the same object or question again. Deferred is not deleted, forgotten, or globally resolved. Active event/view-change investigations remain open.
