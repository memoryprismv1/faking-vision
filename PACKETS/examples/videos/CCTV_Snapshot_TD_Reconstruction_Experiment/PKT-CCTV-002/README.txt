FAKING VISION — FV PACKET

Packet ID: PKT-CCTV-002
Operation: fv analyse
Specification: FV Working Process Specification v0.24
Status: Initial analysis packet; independent of PKT-CCTV-001; not merged, validated, or compiled.

SOURCE INTAKE
- Packet source: part_02.mp4
- Parent source: BLK-HDPTZ12_Security_Camera_Parking_Lot_Surveillance_Video (1).webm
- Parent-source interval: approximately 105.569333–211.138667 seconds (Part 2)
- Packet-source duration: 105.599675 seconds
- Video: 1920 × 1080, H.264, reported frame rate 30/1
- Audio stream present: True. Audio was not intentionally included or used as evidence.
- SHA-256 of part_02.mp4: d729c47eea1aa2a3d44a878ebf3068deb51f3899df9c444def000ff54c0896a5
- This is a re-encoded duration split of the parent video, not a bit-for-bit segment of the original WebM.

FV METHOD AND EVIDENCE
- Sampled at nominal one-second intervals from t=0 through t=105; all 106 full-frame snapshots are retained in snapshot/verification/ and indexed in snapshot/manifest.json.
- Eight source-derived, unannotated crops are retained in snapshot/objs/.
- Manual visual inspection only: no built-in object detector, image classifier, automated tracker, OCR, or automated visual inference was used. Code was used only to extract/copy snapshots, crop specified regions, hash files and package the artifact.
- Times are relative to part_02.mp4, nominal to the nearest sampled second; they are not wall-clock CCTV times. Parent-relative time is approximately packet-local time + 105.569333 seconds.
- Unlike Part 1, Part 2 contains a substantial camera reframe around t=49–52 and a tighter zoom around t=99. These are represented as camera/view changes, not as objects leaving or a hard cut.
- The small signs/placards in the final zoom are retained as visual evidence. Their markings are not transcribed or interpreted.

PACKET CONTENTS
- OI.json: packet-scoped candidates and supported visible properties; static vehicle candidates are position-scoped to the initial wide view.
- MSRM.json: scene intervals and coarse spatial organization across the changing camera views.
- TD.json: baseline and sampled changes, with evidence references and unresolved correspondences.
- snapshot/manifest.json: source lineage, timestamps, snapshot/crop hashes and crop provenance.
- snapshot/verification/: 106 full-frame snapshots.
- snapshot/objs/: eight source-derived evidence crops.

BOUNDARIES
- This packet is not merged with Part 1. IDs are packet-local and must not be treated as cross-packet identities.
- The packet is an initial FV analysis output. Validation, investigation, merge and compilation remain separate operations.
- No make/model, person identity, sign meaning, or cross-view identity is asserted beyond the retained visual evidence.

DISPUTES: NONE at packet level. Local uncertainties and provisional correspondence are preserved in OI/TD; no identity merge or reconstruction compilation is authorized by this statement.
