# Observer-conditioned visual-field experiment

**Status: protocol ready; experiment not yet run.** No staircase image set is currently committed as the experiment's source evidence. Do not mark results complete until the same staircase has been photographed from all three viewpoints and each image has been independently analysed.

## Question

Can FV represent differences in visible structure caused by observer viewpoint while keeping the physical staircase as one unchanged scene?

The unit of comparison is the observer-conditioned visual field, not the set of already-recognised objects. Perform the initial analysis independently for each image before cross-view reconciliation.

## Capture set

Use one unchanged staircase and capture:
1. Top viewpoint.
2. Bottom viewpoint.
3. Intermediate landing viewpoint.

Keep the staircase and its environment unchanged between captures. Record incidental changes (people, moved objects, lighting, doors, temporary obstructions) rather than silently treating the captures as identical. Preserve original image files and record cryptographic hashes in the experiment manifest when available.

Do not infer camera calibration, exact physical camera position, orientation, focal length, field-of-view angle, or metric geometry from an ordinary photograph. Record these as unknown unless independently measured or supplied by reliable source metadata.

## Per-image record

Create one record per image, with a distinct stable viewpoint ID. This is a working worksheet, not an authoritative schema.

| Field | Record |
|---|---|
| image/source ID | Original filename and source reference |
| viewpoint ID | Stable VP-... identity from viewpoint.json |
| observer type | Camera / human / unknown |
| position and orientation | Measured, source-described, approximate, or unknown; state basis |
| image dimensions/crop | Pixel dimensions and any known crop; do not equate crop with visual field |
| view direction and extent | Qualitative description unless calibrated evidence exists |
| exposed structures | Surfaces, boundaries, edges, openings, landings, risers, treads, rails, walls, adjacent regions; describe before object promotion |
| occluded regions | Regions inside the field but blocked by nearer structure |
| outside-field regions | Regions not included in the observer's field; distinguish from image crop when possible |
| unresolved regions | In-field areas that cannot be reliably resolved because of scale, blur, lighting, compression, or occlusion ambiguity |
| observation evidence | Image coordinates/regions and short source-grounded descriptions |
| uncertainty | What cannot be concluded from this view |

## Analysis sequence

1. Freeze the three original images and source metadata. Assign distinct viewpoint IDs; do not create new IDs for a single observer's mere movement within a continuous video.
2. Analyse each image separately. Record boundaries, surfaces, exposed regions and candidate structures before semantic object promotion.
3. For each view, classify relevant regions as exposed, inside-field-but-occluded, outside-field, or inside-field-but-unresolvable. If the available evidence cannot distinguish categories, retain an unresolved classification.
4. Only after the independent records are complete, compare views. Identify shared visible structures, newly exposed structures, and structures hidden or outside the field in each view.
5. Propose cross-view correspondences with evidence and confidence. Do not merge regions or identities solely because they look similar or occupy plausible positions.
6. Maintain one shared physical-scene hypothesis only where correspondences are supported. A viewpoint change is not itself a scene change.
7. Record contradictions and unresolved correspondences explicitly. Do not fill unseen staircase geometry from architectural expectations.

## Comparison outputs

The experiment is complete only when it contains:
- three preserved source images and source metadata;
- one viewpoint record per distinct perspective;
- three independent visual-field/structure records;
- a cross-view comparison identifying overlap and newly exposed regions;
- explicit distinctions among occlusion, outside-field, and unresolvable regions;
- a correspondence ledger with evidence, confidence, and unresolved items;
- an audit stating which conclusions are supported and which remain unknown.

## Failure criteria

The experiment fails or remains inconclusive if FV:
- treats the three images as three different physical staircases without evidence;
- treats the pixel crop as the observer's complete visual field;
- calls an occluded region outside the field, or calls an unresolvable region absent;
- builds the field only from recognised objects;
- forces cross-view identity or geometry matches without correspondence evidence;
- invents unseen structure from generic knowledge of stairs.

## Boundary

This is an experiment protocol, not implementation of a general visual-field representation. It does not replace OI, MSRM, TD, viewpoint identity, or per-object line-of-sight analysis. The viewpoint identity and temporal viewpoint state remain governed by sections 10.1B and 17.3 of the Working Process Specification.
