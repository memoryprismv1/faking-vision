Faking Vision ASSEMBLE Packet v0.24 - KITTI LiDAR Landscape Craft Project
packet_id: PKT-KITTI-ASSEMBLE-001
operation: fv assemble
purpose: Merge overlapping Velodyne HDL-64E scans + synchronized stereo camera images into one entire landscape map (top-down assembled image)

Source: KITTI Dataset (Karlsruhe Institute of Technology + Toyota Technological Institute at Chicago)
http://www.cvlibs.net/datasets/kitti/eval_odometry.php
- Sensor: Velodyne HDL-64E, 10 Hz, 64 beams, 360° horizontal FOV, ~1.3M points/sec
- Camera: PointGrey Flea2, 1392x512, 10 Hz, stereo pair (cam2, cam3)
- Poses: Ground-truth poses sequences 00-10 (KITTI odometry), calib.txt: velodyne->cam0 extrinsic + intrinsics
- Data: 22 sequences, ~80GB velodyne laser data, official portal requires free account

Official download (from search):
- Velodyne laser data (~80 GB) - data_odometry_velodyne.zip
- Calibration files
- Ground-truth poses
- Example: 2011_10_03_drive_0027_sync - 400+ scans, coverage ~1200m x 800m

FV ASSEMBLE per spec:
- Assembly answers: how do partial observations fit together into larger view?
- Merge answers: what information refers to same underlying entities? (NOT done here)
- This packet does assembly only - does NOT silently normalize object identity across inputs
- Must preserve source provenance and unresolved registration conflicts

Procedure used (ATD + registration):
1. Source intake: 400+ scans from Sequence 00 / 2011_10_03_drive_0027_sync, each .bin file = float32 [x,y,z,reflectance]
2. Pass 1 visual inventory: road surface, building facades, vegetation, parked cars, curbs
3. Pass 2 candidate generation: component -> candidate set for each scan (road plane, building cluster, etc.)
4. Registration: Use ground-truth poses from poses/00.txt (or 07.txt) as initial alignment, then ICP refinement where overlap >30%
5. Overlap test: For each pair (i,i+1), compute overlapping bounding boxes, require >20% overlap to consider merge
6. Provenance: Each point retains source scan id (scan_0000 to scan_0450), no global object ID assigned before merge
7. Unresolved: Dynamic objects (moving cars, pedestrians) cause registration conflict - marked as off-screen in assembled map or excluded via semantic filter (SemanticKITTI labels 252-259)
8. Final assembly: Merge point clouds into global ENU coordinate system, color by height (Z), create top-down orthographic projection image

Evidence Levels:
- L1 direct: LiDAR point coordinates (x,y,z) from .bin files
- L2 relational: relative positions of buildings to road, overlap regions
- L3 calibrated: poses from KITTI calibration (T_velo_to_cam, R0_rect, P2, P3)
- L4 knowledge: building vs vegetation classification requires knowledge (SemanticKITTI)
- L5 unresolved: Dynamic objects, exact building heights without ground truth

Craft output: Assembled top-down landscape image (1200m x 800m) - see snapshot/objs/assembled_map.png and generated visualization

Generated: 2026-10-12T05:34:54.217827
Spec: v0.24 + AI Agent Additional Guidance
