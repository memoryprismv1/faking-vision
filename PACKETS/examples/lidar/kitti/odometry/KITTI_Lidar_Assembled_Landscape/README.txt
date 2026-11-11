# KITTI LiDAR assembled-landscape example

Packet ID: `PKT-KITTI-ASSEMBLE-001`
Operation intended: `fv assemble`
Specification label in supplied packet: v0.24

## Source reference

The legacy packet names the [KITTI Odometry benchmark](https://www.cvlibs.net/datasets/kitti/eval_odometry.php) and describes Velodyne HDL-64E scans, stereo-camera data, calibration, and pose files. It also refers to a raw-drive sequence name. These references are retained as source pointers only; the exact acquisition used for this packet has not been established.

## Intended demonstration

The packet is intended to show registration and integration of partial LiDAR observations into a larger spatial representation while preserving scan provenance. Assembly is distinct from normalizing persistent object identities, which belongs to a separate merge operation.

## What is actually present

The repository contains packet JSON records, a snapshot manifest, and illustrative visualization assets. It does **not** contain the raw KITTI point-cloud scans, the corresponding calibration and pose files, or a reproducible registration log sufficient to reproduce the described assembly.

## Verification limits

The legacy README describes 400+ scans, a particular drive, ICP refinement, overlap thresholds, an ENU map, and a 1200 m × 800 m output. Those are claims in the supplied README, not independently verified results of this repository example. The README also mixes KITTI Odometry sequence references with a raw-drive identifier; do not assume they identify the same acquisition.

The visualizations are illustrative and are not substitutes for the missing source scans or a reproducible assembled point cloud. Treat this as a procedural/packet-shape example, not a verified LiDAR assembly.
