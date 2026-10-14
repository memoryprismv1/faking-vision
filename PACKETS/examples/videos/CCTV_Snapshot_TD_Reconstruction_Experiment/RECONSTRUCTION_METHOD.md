# Reconstruction method

## Inputs and time

The source is the Wikimedia Commons parking-lot surveillance video. The working copy was divided into three segments of approximately 105.6 seconds each. Each segment was treated as a packet-scoped source with its own local timebase.

Do not infer that packet 1's end, packet 2's beginning, and packet 3's beginning are a single continuous observed chronology merely because the segments originated from one source.

## Reconstruction basis

The review rendering was assembled from available snapshot material and TD records. Selected source-video intervals were also inspected manually at finer sampling when a temporal question could materially change the interpretation.

This was not an object detector/tracker pipeline, and no claim is made that every source frame was analysed.

## Adaptive follow-up examples

- **Part 1, about 20–26 s:** refine the pedestrian/silver-sedan proximity interval. The person moves toward the foreground/right and becomes increasingly occluded by a red SUV; the sedan moves left relative to fixed parking geometry. Contact and deliberate response are not established.
- **Part 2, about 96–99 s:** inspect a dark vehicle-like form moving left relative to fixed poles and the curb island. Its exact subtype and path boundaries remain uncertain.
- **Part 3, about 78–104 s:** inspect a light-coloured sedan-like vehicle moving left across the mid/foreground aisle. Direction is supported by changing position relative to fixed scene features; exact path and identity are uncertain.

## Evidence discipline

- Distinguish direct visual observation from relational inference and unresolved hypotheses.
- Treat packet records as independent knowledge stores until evidence supports correspondence.
- Do not merge vehicles based on colour or category alone.
- Preserve aggregate-to-component relationships rather than collapsing a sign assembly into one object or inventing independent identities.
- Occlusion is not deletion; movement is not duplication.
- Camera/composition change must not automatically be attributed to an object's motion.
- Keep candidate reasoning in the investigation layer; promote only supported conclusions into official temporal records.

## Output status

The MP4 is a human-review reconstruction, not a canonical FV compile. The CLI was not run; the dispute-resolution gate was not satisfied; exhaustive frame-by-frame reconstruction was not performed.
