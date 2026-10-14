# Process log

## Goal

Investigate whether three separately prepared CCTV packets could be reconciled into a useful cross-packet view, while preserving object identity uncertainty, temporal evidence, and the distinction between investigation and official temporal records.

## Work sequence

1. **Source preparation.** The Commons CCTV video was split into three source segments for separate packet-level handling. The working segments were approximately 105.6 seconds each; the original source is approximately 316.7 seconds.
2. **Packet review.** Reviewed the three packet inventories, snapshot manifests, TDs, TIR material and dispute records as separate knowledge stores. Their timebases were not assumed to form one uninterrupted timeline.
3. **Reconstruction by instruction.** The user explicitly declined dispute resolution and directed reconstruction from snapshots and TDs. This instruction was followed as an experiment, despite the normal FV lifecycle gate; see `FV_DEVIATION.md`.
4. **Cross-packet correspondence.** Compared scene structures and candidate objects. Stronger correspondences were retained as candidate links; aggregate assemblies were not collapsed into their components. Vehicle identities were not merged merely on the basis of colour or broad category.
5. **Targeted temporal investigation.** Manually inspected selected intervals at finer temporal sampling when the unresolved question warranted it. Examples included the Part 2 dark vehicle near 96–99 seconds and the Part 1 pedestrian/silver-sedan proximity interval around 20–26 seconds.
6. **Evidence-qualified conclusions.** For the pedestrian/sedan interval, the inspected samples support different motion paths and increasing pedestrian occlusion by a red SUV. They do not establish contact or a directed reaction. No interaction was promoted as established.
7. **Reconstruction output.** Built a review MP4 from the available snapshot/TD-derived material and generated contact sheets for selected intervals. This output is a review artefact, not a canonical FV compile.
8. **Documentation.** Recorded provenance, process, deviations, evidence references, and limits so a reader can distinguish observed evidence from hypotheses and unsupported continuity.

## Cross-packet findings

- Part 2 aggregate sign assembly corresponds strongly to the Part 3 placards and pole as an assembly-to-components relationship.
- The landscaped curb island and the three-way utility structure have strong scene correspondences across packet boundaries.
- Broad parking-lot and road regions correspond at scene level.
- Vegetation is a broad setting correspondence, not a one-to-one object identity.
- Individual vehicles were not merged across packets without distinctive evidence.
- Several moving-object episodes were kept distinct where position, path, or time did not support a shared identity.

## Limitations

This was manual source-frame inspection and reconstruction work. The FV CLI was not run. There was no exhaustive frame-by-frame audit, no validated packet compile, and no resolution of the open disputes. The reconstruction must not be represented as satisfying those gates.
