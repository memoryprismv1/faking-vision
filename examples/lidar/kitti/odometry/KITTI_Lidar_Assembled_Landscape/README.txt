# KITTI LiDAR assembled-landscape example

Packet ID: `PKT-KITTI-ASSEMBLE-001`
Operation intended: `fv assemble`
Specification label in supplied packet: v0.24

## Source reference

The legacy packet names the [KITTI Odometry benchmark](https://www.cvlibs.net/datasets/kitti/eval_odometry.php) and describes Velodyne HDL-64E scans, stereo-camera data, calibration, and pose files. It also refers to a raw-drive sequence name. These references are retained as source pointers only; the exact acquisition used for this packet has not been established.

## Intended demonstration

The packet is intended to show registration and integration of partial LiDAR observations into a larger spatial representation while preserving scan provenance. Assembly is distinct from normalizing persistent object identities, which belongs to a separate merge operation.

## What is actually present

The repository contains packet JSON records, a manifest that now explicitly records that no snapshot objects are retained in the packet folder, and illustrative visualization assets. A legacy manifest reference to `snapshot/objs/assembled_map.png` and a craft-project HTML artifact did not resolve to files and has been withdrawn. The repository does **not** contain the raw KITTI point-cloud scans, the corresponding calibration and pose files, or a reproducible registration log sufficient to reproduce the described assembly.

## Verification limits

The legacy README describes 400+ scans, a particular drive, ICP refinement, overlap thresholds, an ENU map, and a 1200 m × 800 m output. Those are claims in the supplied README, not independently verified results of this repository example. The README also mixes KITTI Odometry sequence references with a raw-drive identifier; do not assume they identify the same acquisition.

The visualizations are illustrative and are not substitutes for the missing source scans or a reproducible assembled point cloud. `dispute.json` now records two open blockers and sets the assembly gate to BLOCKED_FOR_REPRODUCTION: the exact source acquisition/registration inputs are absent, and the moving-car registration conflict is unresolved. Treat this as a procedural/packet-shape example, not a verified LiDAR assembly.


## Provenance update (2026-11-13)

The sequence-to-raw-drive mapping is now verified against the mapping table in the KITTI odometry devkit README:
- Odometry sequence 00 → raw drive 2011_10_03_drive_0027, frames 000000–004540 (4,541 frames).
- Odometry sequence 07 → raw drive 2011_09_30_drive_0027, frames 000000–001100 (1,101 frames).

This resolves the drive/sequence correspondence, not the exact subset used by this packet. The legacy “400+ scans” claim and the mockup's 000000–000450 range do not identify the exact selected frame list. The actual scan files are not present here.

Official acquisition references:
- KITTI odometry benchmark: https://www.cvlibs.net/datasets/kitti/eval_odometry.php
- KITTI raw data: https://www.cvlibs.net/datasets/kitti/raw_data.php

The odometry benchmark lists an 80 GB Velodyne package, 1 MB calibration package and 4 MB ground-truth pose package. The raw-data portal requires account access; the small odometry packages are email-gated. The benchmark Velodyne scans are processed/egomotion-compensated, not a substitute for the raw-drive scans requested here.

Required source package for a reproducible raw-drive reconstruction:
- raw drive 2011_10_03_drive_0027 (prefer the synchronized package matching sequence 00);
- Velodyne point clouds and timestamps;
- OXTS/GPS/IMU packets and per-drive calibration files;
- odometry calibration and ground-truth poses for the matching sequence;
- exact selected frame IDs for this 400-scan subset.

No raw scans, calibration files, poses, or registration logs have been acquired into this packet. Registration logs are processing outputs, not KITTI source files; they must record input frame IDs, transforms, algorithm/version, parameters, convergence, residuals and output hashes. Reproduction remains BLOCKED pending source package access and the missing 400-frame selection list.
