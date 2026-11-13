# KITTI Odometry Sequence 07 assembly example

Packet ID: `PKT-KITTI-ASSEMBLE-007`
Operation intended: `fv assemble`
Specification label in supplied packet: v0.24

## Source reference

The packet identifies KITTI Odometry Sequence 07 and names the expected `velodyne/*.bin`, `poses/07.txt`, and `calib.txt` inputs. The raw scans, poses, calibration files, and a reproducible registration log are not included in this repository.

## Intended demonstration

This packet is intended to illustrate assembly of a sequence of LiDAR observations while preserving scan-level provenance and keeping assembly distinct from object-identity merge.

## Verification limits

The legacy README claims 1,101 scans, approximately 1,500 m × 900 m coverage, 3.2 million points, and 40–60% overlap. Those figures and the claim that dynamic objects were excluded using SemanticKITTI are not independently verified by the files present here.

`dispute.json` now records an open source/reproducibility blocker and sets the assembly gate to BLOCKED_FOR_REPRODUCTION. Treat the packet and its point-cloud visualization as illustrative. Do not present the scan count, coverage, registration quality, filtering, or assembled result as reproduced or validated.


## Provenance update (2026-11-13)

The KITTI odometry devkit mapping confirms sequence 07 corresponds to raw drive 2011_09_30_drive_0027, frames 000000–001100 inclusive (1,101 frames). The legacy 1,101-scan count matches the official sequence length, but the scan files are not present here, so the packet's actual contents have not been independently verified.

Official references:
- KITTI odometry benchmark: https://www.cvlibs.net/datasets/kitti/eval_odometry.php
- KITTI raw data: https://www.cvlibs.net/datasets/kitti/raw_data.php

The odometry package provides a calibration archive and ground-truth pose archive, but its Velodyne scans are processed/egomotion-compensated. The raw-data portal requires account access. To reproduce this packet as a raw-scan example, obtain raw drive 2011_09_30_drive_0027 with Velodyne scans, timestamps, OXTS/GPS/IMU and calibration, plus the matching odometry calibration/poses. No raw files, calibration, poses, exact processing parameters or registration logs are retained here. Reproduction remains BLOCKED.
