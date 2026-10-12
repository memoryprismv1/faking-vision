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
Verification caveat: the packet describes the source and method, but the supplied archive does not contain the raw LiDAR transects or a rendered assembled landscape. Its validation report's “VALID” status is a packet claim, not independent verification of the survey or assembly.

### 2. Mayan Pyramids merged global packet
Packet ID: `PKT-MAYAN-MERGE-61K-001`
Operation: `fv merge`
Supplied artifacts: `OI.json`, `MSRM.json`, `PC.json`, `TD.json`, `TIR.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: reconcile overlapping flight-transect packets into persistent global identities, with provenance back to flight IDs and correspondence quality labels.
Source named in README: PACUNAM LiDAR Initiative; the README claims 2,100 km² and 61,000 structures.
Verification caveat: no underlying point clouds or input assembly packets are included. The claim that 61,000 persistent identities were normalized, and the claimed storage-reduction figures, are not established by the included files alone. Preserve as an example claim until inputs and computation can be inspected.

### 3. KITTI LiDAR assembled landscape
Packet ID: `PKT-KITTI-ASSEMBLE-001`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `PC.json`, `TD.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: assemble overlapping Velodyne scans and synchronized stereo-camera observations into a larger landscape representation, preserving scan provenance and leaving object identity normalization to a separate merge operation.
Source named in README: KITTI odometry dataset, with the official URL http://www.cvlibs.net/datasets/kitti/eval_odometry.php; the README mentions Velodyne HDL-64E scans, stereo images, calibration, and pose files.
Verification caveat: raw KITTI files, calibration files, poses, and the rendered assembled map are not present in the supplied archive. The README describes a procedure; it does not prove that all steps were run.

### 4. KITTI Sequence 07 assembled packet
Packet ID: `PKT-KITTI-ASSEMBLE-007`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `TD.json`, `PC.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: downtown urban-canyon sequence assembly, with scan IDs preserved and dynamic objects excluded using SemanticKITTI labels.
Source named in README: KITTI Odometry Sequence 07, including `velodyne/*.bin`, `poses/07.txt`, and `calib.txt`.
Verification caveat: the 1,101 raw scans and poses are not in the ZIP. Treat scan count, coverage, registration, and filtering as README assertions until reproducible inputs or processing logs are supplied.

### 5. KITTI merged global buildings
Packet ID and exact global-ID claims are encoded in the packet files; the supplied ZIP contains `COMPILED_SPEC.json`, `MSRM.json`, `OI.json`, `PC.json`, `TD.json`, `dispute.json`, and `snapshot/manifest.json`, but no README.
Purpose inferred from packet naming and contents: merge observations into persistent global building identities.
Verification caveat: the archive includes multiple suffixed copies of core JSON files and manifests. Before publication, compare their hashes and preserve any genuinely different versions; do not publish packaging duplicates as distinct semantic artifacts. No raw KITTI source data is included.

### 6. Hubble Ultra Deep Field telescope stitching
Packet ID: `PKT-TELESCOPE-HUDF-STITCH-001`
Operation: `fv assemble`
Supplied artifacts: `OI.json`, `MSRM.json`, `PC.json`, `TD.json`, `TIR.json`, `dispute.json`, `snapshot/manifest.json`, and `README.txt`.
Purpose described by Meta: assemble overlapping telescope exposures into a larger deep-field view, with exposure-level provenance; distinguish exposure assembly from later persistent-galaxy merge.
Source named in README: Hubble Space Telescope Ultra Deep Field, 2003–2004.
Verification caveat: the Hubble exposures, archive identifiers, exposure list, and assembled image are not included. README figures such as exposure count, overlap, and field dimensions require source-level confirmation before being treated as verified.

### 7. CCTV storage-crisis temporal parts and global merge
Packet family: `CCTV_Storage_Crisis`.
Sub-packets: `Part1_00-00_to_11-23`, `Part2_11-23_to_22-46`, `Part3_22-46_to_34-10`, and `MERGED_Global`.
Supplied artifacts across the family include per-packet `OI.json`, `TD.json`, `TIR.json`, `MSRM.json`, `PC.json`, `dispute.json`, and `snapshot/manifest.json`; the merged packet additionally includes `COMPILED_SPEC.json` and `TIR_MERGED_UNIFIED.json`. Each part and the merged packet has a `README.txt`.
Purpose described by Meta: divide a long recording into three temporal segments, then reconcile object identities and a unified timeline across the segments.
Source named by README: a full, unedited Kelly Thomas confrontation video. The README calls it CCTV; the source type and original publication/source URL still need verification.
Verification caveat: the actual video is not in the supplied ZIP. The claimed source size, duration, identities, and 10,000x storage reduction are descriptions in the README, not independently verified results. Preserve the part boundaries and merged timeline together.

### 8. Cat jumping backwards video packet and dispute lifecycle
Packet ID: `PKT-CAT-JUMP-BACK-001`
Supplied artifacts include `OI.json`, `MSRM.json`, `TD.json`, `PC.json`, `dispute.json`, `dispute.reconciled.json`, `COMPILED_SPEC.json`, `COMPILED_PROMPT.txt`, `README.txt`, `VALIDATION_REPORT.txt`, `VALIDATION_REPORT_POST_RESOLVE.txt`, and snapshot-related artifacts. The ZIP also contains suffixed duplicate-looking files such as `OI_1.json`, `README_1.txt`, and `MSRM_2.json`; inspect hashes and contents before deciding whether they are duplicates or distinct state versions.
Sources named by README: Wikimedia Commons file page and transcoded media URL, plus the original Vimeo URL.
Purpose described by Meta: video analysis with inventory lock, temporal decomposition, uncertainty, explicit disputes, reconciliation, validation, and compilation.
Important lifecycle distinction: the pre-resolution validation report says open disputes block rendering and reports missing snapshot subdirectories; the post-resolution report says disputes were reconciled and rendering is permitted. Keep both reports and the reconciliation record; do not silently replace the earlier state or treat the later report as independent proof of visual correctness.
Evidence limitation stated by README: direct pixel-level frame inspection was unavailable in the production environment. L1 visual evidence is explicitly limited and some temporal/correspondence claims remain provisional.

## Provenance and quality policy for this contribution

1. Keep supplied README and validation artifacts with their packet; do not rewrite source claims as verified facts.
2. Record source URLs and dataset identifiers where supplied. Flag missing source links and acquisition records.
3. Distinguish four states: source identified, source acquired, processing executed, result independently verified.
4. Preserve original dispute files, reconciliations, pre-resolution and post-resolution reports, and packet manifests.
5. Compare duplicate-looking files by content hash. Remove only packaging duplicates from the published tree; never discard a distinct lifecycle state.
6. Do not claim raw sensor media is included where the ZIP contains only structured packet artifacts.
7. Retain provenance and uncertainty; do not silently promote unresolved claims or create global identities without documented correspondence evidence.

## Contents of this contribution

This catalog covers eight packet bundles represented in the supplied archives: Mayan LiDAR stitching, Mayan global merge, KITTI landscape assembly, KITTI Sequence 07 assembly, KITTI global buildings merge, Hubble Ultra Deep Field stitching, the three-part CCTV family plus merged global packet, and the cat-jumping video/lifecycle packet. Duplicate ZIP uploads were treated as repeat packaging, not new examples.

This document is an inventory and provenance guide. It is not a claim that the raw sensor sources are included or that every processing step has been independently reproduced.
