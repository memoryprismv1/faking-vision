# Meta's FV examples contribution

Date received: 2026-10-12
Contributor/work origin: Meta (AI-assisted packet production)
Specification referenced by the supplied packet READMEs: FV v0.24.

This document records the example families Meta produced and the artifacts present in the supplied ZIPs. It distinguishes packet contents from claims in README/validation files. The presence of an artifact is not proof that the underlying source data was downloaded or that the described processing was executed.

## Proposed packet architecture

Keep the existing reconstruction-target folders for compatibility, and add narrowly scoped organization where the new examples need it. Do not create a folder merely because a new label appears.

- `examples/images/`: image-target packets.
- `examples/videos/`: video-target packets.
- `examples/lidar/`: LiDAR-specific assembly/merge packets, with KITTI sequence and merge examples grouped together.
- `examples/telescope/`: telescope-exposure assembly, including Hubble Ultra Deep Field.
- `examples/cctv/`: long-recording packets partitioned into temporal parts and a merged global packet.
- `by_operation/`: only where an operation needs a teaching example independent of the source modality (analyse, investigate, assemble, merge, resolve, validate, compile, audit).
- `lifecycle/`: linked states of the same packet only when the supplied artifacts demonstrate those states.
- `templates/`: a template only when it is actually supplied and validated.
- `datasets/`: source pointers and acquisition notes, not copies of large source datasets unless licensing and storage have been checked.

This proposal retains the old `images/` and `videos/` entry points. It does not imply that all proposed folders or examples already exist in the repository.

## Example inventory

### 1. Mayan Pyramids LiDAR stitching
Packet ID: `PKT-MAYAN-LIDAR-STITCH-001`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `TD.json`, `TIR.json`, `COMPILED_SPEC.json`, `PC.json`, `dispute.json`, `snapshot/manifest.json`, `README.txt`, and `VALIDATION_REPORT.txt`.
Purpose described by Meta: assemble overlapping airborne LiDAR flight transects into a larger landscape; preserve flight-line provenance and distinguish assembly from global entity merge.
Source named in README: PACUNAM LiDAR Initiative (Guatemala), 2018; Garrison et al., *Science* (2018), “Spatiotemporal patterns of Maya urbanism”; Mirador Basin Project is also mentioned.
Verification caveat: raw LiDAR transects, exact flight acquisitions, calibration/registration inputs and processing logs are absent. The west-facing staircase has been removed from the observed component inventory and retained only as an unverified expected-component candidate. Two open disputes now block reproduction: missing flight-line/processing evidence and unsupported archaeological classification. The former `VALID` report was corrected to `BLOCKED_UNVERIFIED`; the compiled-spec draft is blocked.

### 2. Mayan Pyramids merged global packet
Packet ID: `PKT-MAYAN-MERGE-61K-001`
Operation: `fv merge`
Supplied artifacts: `OI.json`, `MSRM.json`, `PC.json`, `TD.json`, `TIR.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: reconcile overlapping flight-transect packets into persistent global identities, with provenance back to flight IDs and correspondence quality labels.
Source named in README: PACUNAM LiDAR Initiative; the README claims 2,100 km² and 61,000 structures.
Verification caveat: no underlying point clouds, flight transects or contributing packets are included. The packet contains a 12-identity sample; MSRM lists those 12 IDs. Typed totals (1,200 pyramids, 1,800 causeways, 3,000 plazas) account for 6,000 of the claimed 61,000 structures; the remaining 55,000 are uncategorized. Two open disputes now block the merge: the uncategorized inventory remainder and absent source correspondence evidence. The global count, 100+ input count, correspondence quality and storage-reduction claims are not reproduced results.

### 3. KITTI LiDAR assembled landscape
Packet ID: `PKT-KITTI-ASSEMBLE-001`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `PC.json`, `TD.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: assemble overlapping Velodyne scans and synchronized stereo-camera observations into a larger landscape representation, preserving scan provenance and leaving object identity normalization to a separate merge operation.
Source named in README: KITTI odometry dataset, with the official URL http://www.cvlibs.net/datasets/kitti/eval_odometry.php; the README mentions Velodyne HDL-64E scans, stereo images, calibration, and pose files.
Verification caveat: raw scans, calibration/pose files and reproducible registration logs are absent. The exact acquisition is not established, and a moving-car registration conflict remains unresolved. Two open disputes block reproduction. A legacy snapshot manifest reference to a missing assembled-map PNG and craft-project HTML was withdrawn; the manifest now explicitly records that no snapshot objects are retained in the packet folder. Separate visualization assets are illustrative only.

### 4. KITTI Sequence 07 assembled packet
Packet ID: `PKT-KITTI-ASSEMBLE-007`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `TD.json`, `PC.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: downtown urban-canyon sequence assembly, with scan IDs preserved and dynamic objects excluded using SemanticKITTI labels.
Source named in README: KITTI Odometry Sequence 07, including `velodyne/*.bin`, `poses/07.txt`, and `calib.txt`.
Verification caveat: raw scans, poses, calibration and reproducible registration logs are absent. One open dispute blocks reproduction; the 1,101 scan count, 3.2M point count, 1,500 m × 900 m coverage and dynamic-object filtering claims remain unverified.

### 5. KITTI merged global buildings
Packet ID and exact global-ID claims are encoded in the packet files; the supplied ZIP contains `COMPILED_SPEC.json`, `MSRM.json`, `OI.json`, `PC.json`, `TD.json`, `dispute.json`, and `snapshot/manifest.json`, but no README. A review README has since been added at `examples/lidar/kitti/merged/KITTI_Merged_Global_Buildings/README.md`.
Purpose inferred from packet naming and contents: merge observations into persistent global building identities.
Verification caveat: duplicate suffixed JSON/manifests were byte-identical to canonical records and have been removed. OI contains 12 represented global records but retains a legacy declared total of 54; 42 singleton identities are not represented. The compiled-spec draft is constrained to the 12 represented identities and does not instantiate the missing 42. Two open disputes block the merge: inventory completeness and source-component provenance. No raw KITTI source data is retained.

### 6. Hubble Ultra Deep Field telescope stitching
Packet ID: `PKT-TELESCOPE-HUDF-STITCH-001`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `PC.json`, `TD.json`, `TIR.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: assemble overlapping telescope exposures into a larger deep-field view, with exposure-level provenance; distinguish exposure assembly from later persistent-galaxy merge.
Source named in README: Hubble Space Telescope Ultra Deep Field, 2003–2004.
Verification caveat: the Hubble exposures, archive identifiers, complete exposure list, calibration inputs and reproducible processing log are absent. The OI's two entities are now both represented in the MSRM scene; that was a structural cross-reference correction only. Two open disputes block acceptance: reproducible exposure provenance and unverified astronomical inventory/count claims. The 800-exposure and 10,000-galaxy figures remain legacy claims, not reproduced results.

### 7. CCTV storage-crisis temporal parts and global merge
Packet family: `CCTV_Storage_Crisis`.
Sub-packets: `Part1_00-00_to_11-23`, `Part2_11-23_to_22-46`, `Part3_22-46_to_34-10`, and `MERGED_Global`.
Supplied artifacts across the family include per-packet `OI.json`, `TD.json`, `TIR.json`, `MSRM.json`, `PC.json`, `dispute.json`, and `snapshot/manifest.json`; the merged packet additionally includes `COMPILED_SPEC.json` and the canonical merged `TIR.json`. Each part and the merged packet has a `README.txt`.
Purpose described by Meta: divide a long recording into three temporal segments, then reconcile object identities and a unified timeline across the segments.
Source named by README: a full, unedited Kelly Thomas confrontation video. The README calls it CCTV; the source type and original publication/source URL still need verification.
Verification caveat: the source video, source URL/acquisition record and source-aligned snapshots are absent. All three part packets now have two open provenance/correspondence disputes and BLOCKED analysis gates; their OIs are unverified legacy candidates, TDs are non-authoritative, and TIR observations/hypotheses are explicitly unverified. Unsupported personal names were removed from the part TIRs. The merged packet has three open disputes and a BLOCKED merge gate: four global IDs remain uncommitted candidates, the unified timeline/coverage claim is unverified, and the compiled-spec draft is not an approved render target. Bitrate arithmetic is corrected; the 10,000x reduction claim remains withdrawn as non-evidence-equivalent.

### 8. Cat jumping backwards video packet and dispute lifecycle
Packet ID: `PKT-CAT-JUMP-BACK-001`
Supplied artifacts include `OI.json`, `MSRM.json`, `TD.json`, `PC.json`, `dispute.json`, `dispute.reconciled.json`, `COMPILED_SPEC.json`, `COMPILED_PROMPT.txt`, `README.txt`, `VALIDATION_REPORT.txt`, `VALIDATION_REPORT_POST_RESOLVE.txt`, and `snapshot/manifest.json` (which records that no frame snapshots were preserved). The ZIP also contained suffixed copies such as `OI_1.json`, `README_1.txt`, and `MSRM_2.json`. Their Git blob hashes were identical to the canonical unsuffixed files, so the suffixed packaging duplicates have been removed. The distinct pre-resolution and post-resolution reports and the reconciliation record are retained.
Sources named by README: Wikimedia Commons file page and transcoded media URL, plus the original Vimeo URL.
Purpose described by Meta: video analysis with inventory lock, temporal decomposition, uncertainty, explicit disputes, reconciliation, validation, and compilation.
Important lifecycle distinction: the initial validation report records open disputes and missing snapshot subdirectories. The human resolution accepted metadata-only analysis with uncertainty preserved; it did not add source frames or resolve the factual uncertainties. The post-resolution report has been corrected: snapshot structure remains FAIL/NOT PRESENT, no TIR.json exists, and the overall status is PARTIAL. Human permission to compile this metadata-only experiment is not visual verification or full packet validation.
Evidence limitation stated by README: direct pixel-level frame inspection was unavailable in the production environment. The repository contains no source video or retained frame snapshots. L1 visual evidence is limited and temporal/correspondence claims remain provisional.

## Provenance and quality policy for this contribution

1. Keep supplied README and validation artifacts with their packet; do not rewrite source claims as verified facts.
2. Record source URLs and dataset identifiers where supplied. Flag missing source links and acquisition records.
3. Distinguish four states: source identified, source acquired, processing executed, result independently verified.
4. Preserve original dispute files, reconciliations, pre-resolution and post-resolution reports, and packet manifests.
5. Compare duplicate-looking files by content hash. This review removed byte-identical suffixed packaging copies from the Cat-jumping and KITTI merged-building examples, retaining canonical unsuffixed files. Shared boilerplate files repeated across different environmental packets were retained. The byte-identical `TIR_MERGED_UNIFIED.json` alias in the CCTV Storage Crisis merged packet was removed; canonical `TIR.json` remains. Never discard a distinct lifecycle state.
6. Do not claim raw sensor media is included where the ZIP contains only structured packet artifacts.
7. Retain provenance and uncertainty; do not silently promote unresolved claims or create global identities without documented correspondence evidence.

## Contents of this contribution

This catalog covers eight packet bundles represented in the supplied archives: Mayan LiDAR stitching, Mayan global merge, KITTI landscape assembly, KITTI Sequence 07 assembly, KITTI global buildings merge, Hubble Ultra Deep Field stitching, the three-part CCTV family plus merged global packet, and the cat-jumping video/lifecycle packet. Duplicate ZIP uploads were treated as repeat packaging, not new examples.

This document is an inventory and provenance guide. It is not a claim that the raw sensor sources are included or that every processing step has been independently reproduced. The current example review also adds explicit evidence/dispute gates across the CCTV Storage Crisis, KITTI, Mayan LiDAR and Hubble packets, plus the environmental-pair Wall Cat dispute. Read `PACKETS/examples/README.md` for the current directory-level evidence-status index.
