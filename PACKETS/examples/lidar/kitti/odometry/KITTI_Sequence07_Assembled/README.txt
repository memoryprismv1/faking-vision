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
