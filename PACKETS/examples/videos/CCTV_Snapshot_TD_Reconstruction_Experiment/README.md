# CCTV Snapshot + TD Reconstruction Experiment

**Status: experimental reconstruction; not a validated or compiled FV packet.**

This example demonstrates a review video reconstructed from three packet-scoped CCTV records, their Temporal Declarations (TDs), and preserved snapshots. The source part files are not stored in this repository because of GitHub file-size restrictions; the reconstruction video is available here.

## Files

- `FV_CCTV_snapshot_TD_reconstruction.mp4` — human-review reconstruction derived from TD records and snapshots.
- `PROCESS_LOG.md` — experiment steps, findings, and limitations.
- `SOURCE_AND_PROVENANCE.md` — original source and repository media availability.
- `PKT-CCTV-001/`, `PKT-CCTV-002/`, `PKT-CCTV-003/` — packet records and preserved snapshot evidence.

## Interpretation

This is not a canonical FV compile. The FV CLI was not run, some investigations remain active, and exhaustive frame-by-frame reconstruction was not performed. Packet-local timestamps do not by themselves establish continuous chronology across the three parts. Candidate identity correspondences remain provisional unless distinctive visual evidence supports them.

Original source: https://commons.wikimedia.org/wiki/File:BLK-HDPTZ12_Security_Camera_Parkng_Lot_Surveillance_Video.webm


## Packet-level review notes

- The three source segments are not stored in this repository. Packet snapshots are retained, but they are sampled evidence, not the original video or proof of exhaustive frame coverage.
- Packet-local timestamps do not establish a continuous timeline across segments. Part 1's manifest records no parent-source interval; Part 2 declares [105.569333, 211.138667] seconds with a 105.599675-second encoded duration; Part 3 declares [211.138667, 316.708] seconds with a 105.554-second encoded duration. The start + duration values do not exactly match the declared interval endpoints (about +30.3 ms for Part 2 and -15.3 ms for Part 3). Use the source metadata carefully; do not concatenate by nominal duration or infer identity continuity across parts without distinctive evidence.
- A follow-up structural repair added PKT-CCTV-003's seven previously unreferenced OI candidates (OBJ-013 through OBJ-019) to the relevant MSRM scenes using their existing OI time ranges and spatial summaries. All 19 OI IDs now resolve in MSRM, with no extra/unknown IDs. This repairs cross-references only; inventory completeness and visual correctness remain unestablished.
- PKT-CCTV-001 has two issues deferred as non-blocking for that chunk, not globally resolved; its older validation report's blocked-gate statement is stale. PKT-CCTV-003 has three dispute records: one deferred/non-blocking and two active/open. PKT-CCTV-002 now has three explicit open investigations (pedestrian correspondence, camera-view transitions, and one-second sampling coverage); it still has no PC.json or persistent TIR.json, and its merge gate is blocked.
- This experiment remains a human-review reconstruction artefact, not a canonical FV compile, exhaustive reconstruction, or independently validated result.
