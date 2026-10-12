Faking Vision ASSEMBLE Packet v0.24 - KITTI Sequence 07 Downtown
packet_id: PKT-KITTI-ASSEMBLE-007
operation: fv assemble
sequence: 07 (1101 scans) - downtown Karlsruhe, urban canyon

Source: KITTI Odometry 07 - velodyne/*.bin 1101 files, poses/07.txt, calib.txt
Total coverage: ~1500m x 900m, ~3.2M points after merge
This is the downtown sequence with dense building clusters, narrow streets, high overlap (40-60%)

FV Assemble procedure same as PKT-KITTI-ASSEMBLE-001 but for 07:
- Registration: poses from 07.txt + ICP where overlap >30%
- Provenance: scan_07_0000 to scan_07_1100 preserved
- Dynamic objects excluded via SemanticKITTI

Generated: 2026-10-12T05:53:45.240336
