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
| `videos/Cat_jumping_backwards/` | Historical video analysis, dispute, and compile-prompt lifecycle | Metadata-only analysis; no source video or retained snapshots; no `TIR.json`. The former post-resolution VALID claim was corrected to PARTIAL after the claimed snapshot directories were found absent; human permission to compile this metadata-only experiment remains recorded |
| `videos/CCTV_Snapshot_TD_Reconstruction_Experiment/` | Three packet-scoped CCTV analyses, sampled frame evidence, and a human-review reconstruction | Source segments are not stored. The reconstruction is not a canonical FV compile. PKT-CCTV-003's seven previously missing MSRM references have been restored from OI time ranges and spatial summaries; all 19 OI IDs now resolve in MSRM, while two investigations remain active; Part 1's two issues are deferred from current chunk-level attention but remain OPEN in the canonical dispute gate, so rendering/compilation remains blocked; Part 2 has a retained `dispute.json` with three active/open investigations but no `PC.json` or persistent `TIR.json`; its merge gate remains blocked. All three legacy packets also lack current root-level `viewpoint.json` and `packet_provenance.json`; those unknowns are not backfilled. The segment manifests' parent intervals and encoded durations do not exactly agree |
| `videos/Old_macdonald/` | Structured five-scene video reconstruction target | Generated output MP4 is present; persistent farm landmarks and the farmer's scene_04 placement were made explicit in MSRM; output not independently audited. AUDIO_COMPANION.txt is direction only, not a transcript |

## CCTV — legacy multi-part storage example

`cctv/CCTV_Storage_Crisis/` contains three illustrative part records and a proposed merged record. All three part packets now have two open disputes and BLOCKED analysis gates; their OIs are labelled unverified legacy candidates, their TDs are non-authoritative, and TIR observations/hypotheses are explicitly unverified. Unsupported personal names were removed from TIR. The merged packet has three open disputes and a BLOCKED merge gate: four global IDs remain uncommitted candidates, the unified timeline/coverage claim is unverified, and the compiled-spec draft is not an approved render target. The 10/5 Mbps figures are illustrative bitrate arithmetic; the claimed 10,000x reduction is not an evidence-equivalent comparison. See the family README before use.

## LiDAR and telescope — assembly/merge illustrations

- `lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/`: two open disputes now block reproduction: exact acquisition/registration inputs are missing and a moving-car registration conflict is unresolved. Its legacy snapshot manifest referenced a nonexistent assembled-map PNG and craft-project HTML; those references are withdrawn and the manifest now explicitly records that no snapshot objects are retained. The 400-scan/map claims are illustrative only.
- `lidar/kitti/odometry/KITTI_Sequence07_Assembled/`: one open dispute blocks reproduction because raw scans, poses, calibration and registration logs are absent; the 1,101-scan/3.2M-point/1,500 m × 900 m claims are unverified.
- `lidar/kitti/merged/KITTI_Merged_Global_Buildings/`: incomplete merge example with two open disputes and a BLOCKED merge gate. OI lists 12 global records but declares 54 identities; the other 42 are not explicitly represented. Its 12 component-level provenance references also point to building components not declared in the two source OIs. The compiled-spec draft is constrained to the 12 represented records and does not instantiate the 42 unrepresented legacy identities. See its README and dispute.json.
- `lidar/mayan/Mayan_Pyramids_LiDAR_Stitching/`: two open disputes block reproduction of the flight-line assembly and source-dependent archaeological classifications. The previous `VALID` report is corrected to `BLOCKED_UNVERIFIED`; the expected staircase remains only an unverified candidate.
- `lidar/mayan/merged/Mayan_Pyramids_Merged_Global_61k/`: raw flight transects and reproducible correspondence evidence are absent. The MSRM lists all 12 OI sample identities, but typed totals account for only 6,000 of the claimed 61,000 structures; 55,000 remain uncategorized. Two open disputes block the merge.
- `telescope/hubble/Telescope_Hubble_UDF_Stitching/`: packet records and a workflow visualization are present, but original exposures and reproducible processing are absent. OI declares a galaxy and a 10,000-galaxy cluster; the missing cluster reference has now been added to MSRM, but source exposures and the claimed count remain unverified. Two open disputes now record the missing reproducible exposure provenance and unverified astronomical inventory; the acceptance gate is blocked.

Do not present the numbers or processing claims in these examples as reproduced results.

## Environmental edit pairs — metadata-only contribution

`environmental_edit_pairs/` contains packet metadata for three environmental-change scenarios and their before/after states, including a deliberately failing negative example. The seven image binaries are withheld because source-page URLs and licence/permission evidence are absent. The active Bermuda edit's lighthouse is restored, and the baseline cat position is now internally aligned to the paired edit log (on the chair). The rainy Wall Cat edit has an open dispute and blocked-pending-source-review gate because vegetation appears in the edit inventory but not the baseline; the submitted PASS is unverified. See the folder README and verification report.

## Shared viewpoint sample

`viewpoint.json` is a minimal source-viewpoint record with unknown initial position/orientation. It includes the required `initial_state.status` field and is intended as a schema-shaped sample, not evidence of a calibrated camera pose.

## Duplicate packaging cleanup

Byte-identical suffixed copies were removed from the Cat-jumping and KITTI merged-building examples. The byte-identical `TIR_MERGED_UNIFIED.json` alias was removed from the CCTV Storage Crisis merged packet; canonical `TIR.json` remains. Shared version/provenance boilerplate repeated across distinct environmental packets and the same operational-disposition note reused in different CCTV packet folders were retained.

## Verification boundary

The checks recorded here are targeted structural, provenance, and cross-reference reviews. No full authoritative FV semantic validation, exhaustive frame-by-frame audit, independent reproduction of the LiDAR/telescope processing, or complete validation of every example packet is claimed.


Dispute-gate convention: the example `dispute.json` files use canonical aggregate `status` values (`none`, `open`, `resolved`) and per-record `resolution_status`. Chunk-local attention deferral is recorded separately as `operational_disposition`; a deferred issue remains unresolved (`resolution_status: OPEN`) and does not clear an open rendering/compilation gate. This preserves the Making Vision allocation distinction without introducing a new aggregate dispute status.
