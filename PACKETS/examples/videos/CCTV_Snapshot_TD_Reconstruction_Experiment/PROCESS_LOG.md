# CCTV experiment process record

This experiment used three packet-scoped CCTV analyses and their preserved snapshots/Temporal Declarations (TDs) to produce a human-review reconstruction video. The reconstruction was assembled from TD records and snapshots; it is not a canonical FV compile or proof of exhaustive reconstruction.

## Work and limits

- The three source segments were used as separate packet inputs with local timebases. Do not infer continuity solely from packet-local timestamps.
- Manual review targeted intervals where additional temporal evidence could change an interpretation, including the Part 1 pedestrian/sedan proximity interval, the Part 2 dark vehicle-like form, and the Part 3 light-coloured vehicle-like form.
- Candidate correspondences across packets remain provisional unless distinctive visual evidence supports them. Similar colour/category alone does not establish identity.
- Occlusion is not disappearance; camera reframing is not automatically object motion.
- The FV CLI was not run. There was no exhaustive frame-by-frame audit, no validated packet compile, and no resolution of all open disputes. The reconstruction is an experimental review artefact made at the user's direction despite those open gates.

## Output

`FV_CCTV_snapshot_TD_reconstruction.mp4` is retained in this directory. The three source part files are not stored in the GitHub repository because of file-size restrictions; the original source is linked in `SOURCE_AND_PROVENANCE.md`.
