# FV examples index and evidence status

This index distinguishes what an example is meant to demonstrate from what the repository actually contains. A packet-shaped folder, README claim, validation report, or visualization is not by itself proof that source media were acquired, processing was executed, or the result was independently verified.

The current tree contains **22 example packet directories with `OI.json`**: five image packets, five LiDAR packets, one telescope packet, and eleven video packets. Fourteen have a `dispute.json`; the other eight explicitly declare `DISPUTES: NONE` in their packet READMEs. These counts describe the current tree, not the number of all folders or visual assets.

## Visual privacy and provenance audit

A visual privacy inventory of the supplied example corpus is recorded in [the 2026-11-12/13 audit log](../tests/acceptance/results/2026-11-12-example-corpus-privacy-audit.md). It covers 305 images and four videos (the video review is sampled, not exhaustive). No screenshot of a user's desktop, browser, application window, terminal, or other personal system was identified. The three generated story MP4s contain AAC audio tracks that were not listened to or transcribed and are **not audio-cleared**. Source-rights and provenance gaps remain for several legacy examples; the audit identifies them individually. Do not interpret completion of the visual inventory as full privacy, rights, or provenance clearance.

## Images — source image packets

Five image examples include their source image files, OI/MSRM records, and source-page references:

- `images/blue_chairs/`
- `images/desk_with_objects/`
- `images/kitchen_interior_design/`
- `images/restaurant_kitchen/`
- `images/small_room_interior/`

The source-page author and licence statements in these five READMEs were checked against the corresponding Wikimedia Commons pages on 2026-11-11. A structural cross-reference check found that every OI entity ID in these five packets is represented in the corresponding MSRM scene, with no duplicate IDs in the checked inventories. Original acquisition timestamps, pre-import source hashes and image edit histories are not retained. The asset hash manifest records the current repository bytes only; it does not retroactively establish original-source identity. This is not a pixel-level re-analysis or full FV semantic validation.

## Videos — reconstruction briefs and analysis experiments

| Example | What it demonstrates | Evidence/status boundary |
|---|---|---|
| `videos/A_Trip_to_the_Moon_FV_Packet/` | Closed-inventory, multi-background reconstruction brief based on a public-domain film | Original film and source frames are not included; three missing OI/MSRM relations were added from declared scene states; authored target, not source analysis |
| `videos/Alice_in_wonderland/` | Text-derived reconstruction brief from a public-domain literary excerpt | Historical informal v0.4 packet layout; not current-schema guidance and not source-media analysis |
| `videos/Cat_jumping_backwards/` | Historical video analysis, dispute, and compile-prompt lifecycle | Commons source URL is recorded, but source video and snapshots are not retained and no source hash/frame manifest exists; no `TIR.json`. The former post-resolution VALID claim was corrected to PARTIAL after the claimed snapshot directories were found absent; compile gate remains blocked pending post-reconciliation validation |
| `videos/CCTV_Snapshot_TD_Reconstruction_Experiment/` | Three packet-scoped CCTV analyses, sampled frame evidence, and a human-review reconstruction | Parent Commons/YouTube-derived Supercircuits demo acquired and SHA-256 fingerprinted; source video and extracted frames are deleted after hashing, with metadata/frame hashes retained under `provenance/`. Commons public-domain rationale is flagged for review because the source is a zoom/reframe product demonstration. Source storyboard shows view changes inside Parts 2 and 3, not at the equal-third boundaries; Part 3's wide view returns by parent-source 240s (packet-local about 28.86s), later than the previous broad TIR wording. No plate-like marking is transcribed. The reconstruction is not a canonical FV compile; existing packet disputes/gates and missing historical split files remain |
| `videos/Old_macdonald/` | Structured five-scene video reconstruction target | Generated output MP4 is present; persistent farm landmarks and the farmer's scene_04 placement were made explicit in MSRM; output not independently audited. AUDIO_COMPANION.txt is direction only, not a transcript |

## Fullerton Transportation Center CCTV — temporal partition and merge

`videos/fullerton_transit_center_cctv/` contains three illustrative temporal-part records and a proposed merged record. The Commons distribution copy was acquired and fingerprinted on 2026-11-13. The source acquisition and source-alignment records are retained under `videos/fullerton_transit_center_cctv/provenance/`; the video and sample images are not committed. The source is a YouTube-derived Commons upload, not the camera-native recorder file. Source review rejects the Part1 TIR claim at 10s (opening title card) and identifies a distinct view transition between 992.7s and 992.8s inside Part2. The historical part split files remain unavailable. All four global identity correspondences remain hypotheses and the merged analysis gate remains BLOCKED. The 10/5 Mbps figures are illustrative bitrate arithmetic, not measured deployment rates; the claimed 10,000x reduction is not an evidence-equivalent comparison.

The Commons file page displays public-domain rationales under California public-record and ineligible-work tags. This is a record of the source page's stated status, not an independent legal assessment. See the family README before use.

## LiDAR and telescope — assembly/merge illustrations

- `lidar/kitti/odometry/KITTI_Lidar_Assembled_Landscape/`: sequence 00 maps to raw drive 2011_10_03_drive_0027; the exact legacy 400-scan subset is still unidentified. Raw scans, calibration, poses and registration logs are not acquired. The 400-scan/map claims remain illustrative only.
- `lidar/kitti/odometry/KITTI_Sequence07_Assembled/`: sequence 07 maps to raw drive 2011_09_30_drive_0027 and its 1,101-frame count matches the official sequence length. The raw scan files, calibration, poses and registration logs are still absent; the 3.2M-point/1,500 m × 900 m claims remain unverified.
- `lidar/kitti/merged/KITTI_Merged_Global_Buildings/`: incomplete merge example with two open disputes and a BLOCKED merge gate. OI lists 12 global records but declares 54 identities; the other 42 are not explicitly represented. Its 12 component-level provenance references also point to building components not declared in the two source OIs. The compiled-spec draft is constrained to the 12 represented records and does not instantiate the 42 unrepresented legacy identities. See its README and dispute.json.
- `lidar/mayan/Mayan_Pyramids_LiDAR_Stitching/`: the Dryad DOI 10.5061/dryad.k51j708 provides derivative GIS layers, not raw LAS/LAZ point clouds or exact flight-line/transect IDs. Raw acquisition, trajectory/calibration and strip-registration records remain unavailable; reproduction is blocked.
- `lidar/mayan/merged/Mayan_Pyramids_Merged_Global_61k/`: the “61k” label refers to the published estimate of 61,480 mapped structures, not a verified 61,000-point output. Raw flight transects, source tiles and reproducible correspondence/registration evidence are absent; the merge remains blocked.
- `telescope/hubble/Telescope_Hubble_UDF_Stitching/`: a reproducible MAST metadata query now enumerates 609 observations, 800 unique RAW exposure products and 15,740 unique product URIs; the committed manifest is under `provenance/MAST_2026-11-13/`. The four RAW filter counts are F435W 112, F606W 112, F775W 288 and F850LP 288. FITS bytes, CRDS context/reference files and calibration/registration logs are still absent; the packet's astronomical inventory and mosaic remain unverified.

Do not present the numbers or processing claims in these examples as reproduced results. For source URLs, acquisition status, processing gaps and licence/privacy notes across all 17 legacy example families, see [the structured source registry](../docs/provenance/legacy_source_registry.json) and [Legacy Dataset Provenance](../docs/LEGACY_DATASET_PROVENANCE.md).

## Shared viewpoint sample

`viewpoint.json` is a minimal source-viewpoint record with unknown initial position/orientation. It includes the required `initial_state.status` field and is intended as a schema-shaped sample, not evidence of a calibrated camera pose.

## Duplicate packaging cleanup

Byte-identical suffixed copies were removed from the Cat-jumping and KITTI merged-building examples. The byte-identical `TIR_MERGED_UNIFIED.json` alias was removed from the Fullerton Transportation Center CCTV merged packet; canonical `TIR.json` remains. A current tree-wide content-hash check found one remaining identical pair: `FV_OPERATIONAL_DISPOSITION.txt` in CCTV Parts 1 and 3. Both copies are retained because each belongs to its own packet's self-contained operating record. No other byte-identical file groups were found in `examples/`. The similarly named KITTI Sequence 00 map files are not byte-identical and remain distinct supplied versions. The environmental edit-pair family is no longer part of the active examples tree.

## Verification boundary

The checks recorded here are targeted structural, provenance, dispute-gate, and cross-reference reviews. All 22 example packet directories containing `OI.json` have an explicit dispute declaration: 14 use `dispute.json`, and eight declare `DISPUTES: NONE` in their packet README. No full authoritative FV semantic validation, exhaustive frame-by-frame audit, independent reproduction of the LiDAR/telescope processing, or complete validation of every example packet is claimed.


Dispute-gate convention: the example `dispute.json` files use canonical aggregate `status` values (`none`, `open`, `resolved`) and per-record `resolution_status`. Chunk-local attention deferral is recorded separately as `operational_disposition`; a deferred issue remains unresolved (`resolution_status: OPEN`) and does not clear an open rendering/compilation gate. This preserves the Making Vision allocation distinction without introducing a new aggregate dispute status.


Legacy no-dispute declarations: the five image examples and the three authored video-target folders (`A_Trip_to_the_Moon_FV_Packet`, `Alice_in_wonderland`, and `Old_macdonald`) now explicitly declare `DISPUTES: NONE` in their packet READMEs. The five image packets and the video targets remain legacy/target artifacts without current root-level viewpoint/provenance records; they are not thereby made current-format or compilation-ready. In particular, `blue_chairs` is the Case B legacy-viewpoint fixture: its virtual `VP-DEFAULT` is read-time compatibility only, not a render VPO.


## Provenance register

See [Legacy Dataset Provenance](../docs/LEGACY_DATASET_PROVENANCE.md), [structured source registry](../docs/provenance/legacy_source_registry.json), and [binary asset hash manifest](../docs/provenance/example_asset_hashes.json). The register distinguishes original-source hashes from hashes of the repository's current derived assets.


The generated `docs/provenance/example_asset_hashes.json` covers every file currently under `examples/`, including packet metadata and source-frame manifests. It records repository bytes at a specific commit; it is not an original-source checksum. Regenerate it after example assets or provenance records change.
