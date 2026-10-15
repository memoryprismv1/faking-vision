# CCTV Snapshot + TD Reconstruction Experiment

**Status: experimental reconstruction; not a validated or compiled FV packet.**

This example demonstrates a review video reconstructed from three packet-scoped CCTV records, their Temporal Declarations (TDs), and preserved snapshots. The source part files are not stored in this repository because of GitHub file-size restrictions; the reconstruction video is available here.

## Files

- `FV_CCTV_snapshot_TD_reconstruction.mp4` — human-review reconstruction derived from TD records and snapshots.
- `PROCESS_LOG.md` — experiment steps, findings, and limitations.
- `SOURCE_AND_PROVENANCE.md` — original source and repository media availability.
- `PKT-CCTV-001/`, `PKT-CCTV-002/`, `PKT-CCTV-003/` — packet records and preserved snapshot evidence.

## Interpretation

This is not a canonical FV compile. The FV CLI was not run, disputes remain unresolved, and exhaustive frame-by-frame reconstruction was not performed. Packet-local timestamps do not by themselves establish continuous chronology across the three parts. Candidate identity correspondences remain provisional unless distinctive visual evidence supports them.

Original source: https://commons.wikimedia.org/wiki/File:BLK-HDPTZ12_Security_Camera_Parkng_Lot_Surveillance_Video.webm
