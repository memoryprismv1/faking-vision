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


## Packet-level review notes

- The three source segments are not stored in this repository. Packet snapshots are retained, but they are sampled evidence, not the original video or proof of exhaustive frame coverage.
- Packet-local timestamps do not establish a continuous timeline across segments. Use the parent-source offsets in each packet's provenance notes; do not infer identity continuity across parts without distinctive evidence.
- A cross-reference check found that PKT-CCTV-003 declares 19 OI candidates, while its MSRM scenes reference only 12 of them. OBJ-013 through OBJ-019 are not currently spatially represented in MSRM. Treat this as an unresolved packet completeness gap.
- PKT-CCTV-001 retains an open dispute; PKT-CCTV-003 has three open issues recorded in its dated addendum and dispute file. PKT-CCTV-002's local uncertainties remain provisional even though its packet-level dispute status is none.
- This experiment remains a human-review reconstruction artefact, not a canonical FV compile, exhaustive reconstruction, or independently validated result.
