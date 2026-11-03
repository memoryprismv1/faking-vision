# CCTV packet boundary continuity findings

**Status: preliminary boundary comparison completed from preserved snapshots and source manifests. Full packet merge and global identity normalization remain unperformed.**

This note records a narrow comparison of the three existing CCTV packets. It does not resolve their packet-level disputes, establish exhaustive inventory, or authorize rewriting packet-local IDs.

## Source chronology

All three packet manifests identify the same parent source file, `BLK-HDPTZ12_Security_Camera_Parkng_Lot_Surveillance_Video (1).webm`.

| Packet | Parent-source interval | Local duration | Boundary evidence used |
|---|---:|---:|---|
| PKT-CCTV-001 | Part 1 begins at source start; packet README records 105.600 s | 105.600 s | `V_105s.jpg` |
| PKT-CCTV-002 | 105.569333–211.138667 s | 105.599675 s | `frame_001.jpg` at 0 s; `frame_106.jpg` at 105 s |
| PKT-CCTV-003 | 211.138667–316.708 s | 105.554 s | `frame_000.jpg` at 0 s |

The Part 2 and Part 3 manifest intervals meet exactly at 211.138667 s. Part 1 and Part 2 overlap by approximately 0.030667 s according to their declared duration/start metadata. The preserved whole-second samples are not exact split-boundary frames: the comparisons below are offset by approximately 0.57 s.

## Boundary 1: Part 1 to Part 2

Compared:
- `PKT-CCTV-001/snapshot/verification/V_105s.jpg` (Part 1 local 105 s)
- `PKT-CCTV-002/snapshot/verification/frame_001.jpg` (Part 2 local 0 s)

Both show the same wide elevated parking-lot view: the same marked bays, landscaped island, tree line, utility structures, parked-vehicle arrangement, and camera framing. A dark vehicle in the foreground aisle is at a slightly different position between the samples, consistent with temporal progression rather than a scene reset.

**Finding:** same physical scene and same camera perspective across this packet boundary are strongly supported. This is scene/view continuity, not a complete object-by-object identity map. Do not map every parked vehicle across the boundary from colour and approximate position alone.

## Boundary 2: Part 2 to Part 3

Compared:
- `PKT-CCTV-002/snapshot/verification/frame_106.jpg` (Part 2 local 105 s)
- `PKT-CCTV-003/snapshot/verification/frame_000.jpg` (Part 3 local 0 s)

The two preserved images show the same tight view of the same vertical support and the same two placards. Their composition is effectively unchanged across the segment boundary. Part 3 subsequently widens/reframes the view, which its TD records as camera/view change rather than object entry.

Relevant packet-local descriptions:
- Part 2 `PKT-CCTV-002-OBJ-035`: pole with multiple attached placards; one lower placard has blurred alphanumeric-looking marks.
- Part 2 `PKT-CCTV-002-OBJ-036`: a second dark vertical pole/trunk-like structure in the close view; exact structure type unresolved.
- Part 3 `PKT-CCTV-003-OBJ-001` and `OBJ-002`: the two placards, separated into individual candidates.
- Part 3 `PKT-CCTV-003-OBJ-003`: the support pole.

**Finding:** continuity of the placard-bearing support across the boundary is strongly supported. The best correspondence is a composite-to-components relationship: Part 2 OBJ-035 corresponds to the Part 3 pole and its two separately represented placards. This is not a one-to-one identity match. Part 2 OBJ-036 remains unresolved and must not be merged into the support pole without further evidence.

## Viewpoint implications

The three packets describe one parent CCTV recording from one PTZ camera. The wide-to-tight and tight-to-wide changes are camera movement/reframing/zoom, not evidence of a different physical observer. For a future merged packet, the current viewpoint model therefore points toward one stable camera viewpoint identity with TD events for the supported movement/reframing/zoom intervals. Do not create a new viewpoint identity merely because the camera changes orientation or zoom.

The source files are split/re-encoded segments and the preserved samples are JPEG extractions, not lossless boundary frames. The original three source segments are not all present in this repository. These findings are therefore a preliminary continuity gate based on parent-source metadata and adjacent preserved samples, not a frame-accurate merge validation.

## Merge disposition

- **Supported:** one parent source; contiguous Part 2/Part 3 source intervals; same wide view at the Part 1/Part 2 boundary; same placard close-up at the Part 2/Part 3 boundary; camera movement/reframing rather than a new observer is the parsimonious supported interpretation.
- **Candidate correspondence:** Part 2 OBJ-035 ↔ Part 3 OBJ-001 + OBJ-002 + OBJ-003 as a composite-to-components relation.
- **Unresolved:** exact object-by-object continuity for parked vehicles; Part 2 OBJ-036 identity; all cross-packet matches based only on generic colour/category/location; full source-frame continuity at the exact boundaries.
- **Do not do:** rename or overwrite source packet IDs, silently pool packet-local IDs, infer vehicle identity from appearance category alone, or close packet disputes through this note.

The next merge test should preserve all three source packets, create a separate merged output, retain a source-to-merged identity ledger with one-to-many relation support, and run validation without altering the originals.
