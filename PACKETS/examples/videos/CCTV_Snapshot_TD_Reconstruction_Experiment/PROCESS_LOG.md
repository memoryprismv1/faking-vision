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


## Cross-segment metadata review

The packet manifests do not provide a fully normalized parent-source timebase:

- Part 1's manifest records packet/source IDs and sampled source times but no parent-source interval.
- Part 2 declares parent interval 105.569333–211.138667 seconds and encoded duration 105.599675 seconds; start + duration is 211.169008 seconds, about 30.341 ms beyond the declared interval end.
- Part 3 declares parent interval 211.138667–316.708 seconds and encoded duration 105.554 seconds; start + duration is 316.692667 seconds, about 15.333 ms before the declared interval end.

These values may reflect segment-boundary and re-encoding/frame-duration differences, but the repository does not include the original split procedure needed to reconcile them. Do not silently normalize or concatenate the chunks using nominal duration alone. Preserve the source metadata and treat the precise boundary mapping as unresolved pending source-level verification.

Part 2 still has no retained TIR.json or PC.json. A later evidence-status review added `PKT-CCTV-002/dispute.json` with three open issues: provisional pedestrian correspondence, camera-view transitions, and one-second sampling coverage. This records the open questions but does not reconstruct a persistent TIR; the separate investigation reasoning remains incomplete and should not be inferred from the README/TD alone.
