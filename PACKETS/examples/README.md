# FV examples index and evidence status

This index distinguishes what an example is meant to demonstrate from what the repository actually contains. A packet-shaped folder, README claim, validation report, or visualization is not by itself proof that source media were acquired, processing was executed, or the result was independently verified.

## Images — source image packets

Five image examples include their source image files, OI/MSRM records, and source-page references:

- `images/blue_chairs/`
- `images/desk_with_objects/`
- `images/kitchen_interior_design/`
- `images/restaurant_kitchen/`
- `images/small_room_interior/`

The source-page author and licence statements in these five READMEs were checked against the corresponding Wikimedia Commons pages on 2026-11-11. A structural cross-reference check found that every OI entity ID in these five packets is represented in the corresponding MSRM scene, with no duplicate IDs in the checked inventories. This is not a pixel-level re-analysis or full FV semantic validation.

## Videos — reconstruction briefs and analysis experiments

| Example | What it demonstrates | Evidence/status boundary |
|---|---|---|
| `videos/A_Trip_to_the_Moon_FV_Packet/` | Closed-inventory, multi-background reconstruction brief based on a public-domain film | Original film and source frames are not included; three missing OI/MSRM relations were added from declared scene states; authored target, not source analysis |
| `videos/Alice_in_wonderland/` | Text-derived reconstruction brief from a public-domain literary excerpt | Historical informal v0.4 packet layout; not current-schema guidance and not source-media analysis |
| `videos/Cat_jumping_backwards/` | Historical video analysis, dispute, and compile-prompt lifecycle | Metadata-only analysis; no source video or retained snapshots. Post-resolution validation report conflicts with the repository tree and reconciliation record; see its README |
| `videos/CCTV_Snapshot_TD_Reconstruction_Experiment/` | Three packet-scoped CCTV analyses, sampled frame evidence, and a human-review reconstruction | Source segments are not stored. The reconstruction is not a canonical FV compile. PKT-CCTV-003's seven previously missing MSRM references have been restored from OI time ranges and spatial summaries; all 19 OI IDs now resolve in MSRM, while two investigations remain active; Part 1's older validation blocked-gate line is stale relative to its deferred/non-blocking dispute records; Part 2 has no retained TIR/PC/dispute files, and the segment manifests' parent intervals and encoded durations do not exactly agree |
| `videos/Old_macdonald/` | Structured five-scene video reconstruction target | Generated output MP4 is present; persistent farm landmarks and the farmer's scene_04 placement were made explicit in MSRM; output not independently audited. AUDIO_COMPANION.txt is direction only, not a transcript |

## CCTV — legacy multi-part storage example

`cctv/CCTV_Storage_Crisis/` contains three part records and a merged record intended to demonstrate cross-part identity reconciliation. The source identity, source URL, duration, part boundaries, and event summaries are unverified; no source recording or source-derived snapshots are included. The merged OI/TIR now uses resolvable full packet-scoped IDs, but the four global correspondences remain unverified; an unsupported personal name was removed and the 10/5 Mbps storage arithmetic was corrected. The claimed 10,000x reduction is not an evidence-equivalent comparison. See the family README before use.

## LiDAR and telescope — assembly/merge illustrations

- `lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/` and `KITTI_Sequence07_Assembled/`: packet records and visualizations are present; raw scans, calibration/pose files, and reproducible registration logs are not.
- `lidar/kitti/merged/KITTI_Merged_Global_Buildings/`: incomplete merge example. OI lists 12 global records but declares 54 identities; the other 42 are not explicitly represented. Its 12 component-level provenance references also point to building components not declared in the two source OIs. See its README.
- `lidar/mayan/Mayan_Pyramids_LiDAR_Stitching/` and `lidar/mayan/merged/Mayan_Pyramids_Merged_Global_61k/`: source context and packet claims are present, but raw flight transects and reproducible processing/correspondence evidence are absent. The stitching OI's unobserved expected staircase has been removed from the observed component inventory and retained only as an unverified expected-component candidate. The merged example's MSRM now lists all 12 OI sample identities, but the typed totals account for only 6,000 of the claimed 61,000 structures; 55,000 remain uncategorized.
- `telescope/hubble/Telescope_Hubble_UDF_Stitching/`: packet records and a workflow visualization are present, but original exposures and reproducible processing are absent. OI declares a galaxy and a 10,000-galaxy cluster; the missing cluster reference has now been added to MSRM, but source exposures and the claimed count remain unverified.

Do not present the numbers or processing claims in these examples as reproduced results.

## Environmental edit pairs — metadata-only contribution

`environmental_edit_pairs/` contains packet metadata for three environmental-change scenarios and their before/after states, including a deliberately failing negative example. The seven image binaries are withheld because the contribution did not include source-page URLs or licence/permission evidence. The asset manifest records hashes and filenames; it does not grant redistribution rights. The active Bermuda edit's omitted lighthouse has been restored. The rainy Wall Cat edit adds a vegetation entity absent from the baseline OI; with source images withheld, whether this was omitted baseline content or a newly introduced object remains unresolved. See the folder README and verification report.

## Shared viewpoint sample

`viewpoint.json` is a minimal source-viewpoint record with unknown initial position/orientation. It includes the required `initial_state.status` field and is intended as a schema-shaped sample, not evidence of a calibrated camera pose.

## Duplicate packaging cleanup

Byte-identical suffixed copies were removed from the Cat-jumping and KITTI merged-building examples. The byte-identical `TIR_MERGED_UNIFIED.json` alias was removed from the CCTV Storage Crisis merged packet; canonical `TIR.json` remains. Shared version/provenance boilerplate repeated across distinct environmental packets and the same operational-disposition note reused in different CCTV packet folders were retained.

## Verification boundary

The checks recorded here are targeted structural, provenance, and cross-reference reviews. No full authoritative FV semantic validation, exhaustive frame-by-frame audit, independent reproduction of the LiDAR/telescope processing, or complete validation of every example packet is claimed.
