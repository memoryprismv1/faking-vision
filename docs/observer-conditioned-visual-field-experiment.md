# Controlled viewpoint and visual-access experiment

**Purpose:** test whether FV can record viewpoint-conditioned appearance of a fixed scene without confusing physical scene content with observer-relative exposure, detection, recognition, interpretation, or selection.

**Status:** protocol proposal; not yet run. No empirical results are claimed.

## Experiment A — fixed 2D page

### Setup
- One fixed page/surface with a clearly defined x,y coordinate frame.
- A small grid and a few simple marks/shapes at known page coordinates.
- Keep page, marks, and lighting constant across captures.
- Move the observer/camera viewpoint (or a clearly documented directional/view-cone proxy) to different positions and orientations.
- If a torch is used as the observer proxy, it represents the viewpoint/direction in this experiment, not an independent light source. Do not vary illumination at the same time.

### Captures
Capture separate still images from:
1. directly above the page;
2. an oblique viewpoint from one side;
3. a lower/grazing viewpoint;
4. an additional position chosen to create a meaningful change in foreshortening or overlap.

For each image, create a separate FV image packet and record its initial viewpoint in root-level `viewpoint.json`. Use source-supported qualitative position/orientation or the experiment's explicitly defined coordinate frame. Do not infer physical coordinates from pixels alone.

### Questions
- Does the same fixed mark appear with different apparent shape, proportion, spacing, or orientation?
- Which marks/surfaces are geometrically exposed, partially occluded, or outside the view?
- Which visible marks are detected?
- Which detected marks are correctly recognised?
- Which are misinterpreted, and what evidence supports that distinction?
- Are unknowns preserved rather than converted into absence?

No cross-view identity matching is required merely to validate viewpoint initialisation. Page coordinates are known experimental ground truth and may be used to compare observations, but FV must not force visual observations from different viewpoints to be identical.

## Experiment B — fixed 3D retail-shelf arrangement

### Setup
- One fixed shelf with a small, known set of products/boxes.
- Define a scene coordinate frame only if the physical measurements and origin are explicitly established.
- Keep product placement, shelf arrangement, and lighting fixed.
- Change observer position, height, and approach direction.

### Captures
Capture frontal, oblique, and lower/higher approach viewpoints. Record each still image's viewpoint initialisation independently. Optionally record a continuous video for TD transition testing.

### Questions
- Which product facings and surfaces are exposed from each viewpoint?
- Which are partially occluded or outside the view?
- Does the same product appear differently due to perspective or visible surface?
- Which items are detected and recognised?
- Which items receive attention or selection, if that behaviour is directly observed?

Do not infer attention, preference, or purchase selection from visibility alone. Do not assign intrinsic 'eye-level', 'hidden', 'locked cabinet', or 'glitch' labels to products; those are analogy categories that require task-specific definitions.

## Required distinctions in the record

| Layer | Record |
|---|---|
| Physical scene | Objects, surfaces, placements, and relationships supported by the source or controlled setup |
| Viewpoint | Observer identity, initial position/orientation, and video transitions |
| Geometric exposure | In view, partially exposed, occluded, or outside field, with cause/uncertainty |
| Detection | Candidate noticed or not detected |
| Recognition | Correctly identified, uncertain, or misidentified |
| Interpretation | Inferred orientation/structure/state and supporting evidence |
| Attention/selection | Only when directly observed; do not infer from visibility |

## Acceptance criteria
- Each still image has its own viewpoint initialisation.
- A fixed scene can be described from different viewpoints without forcing identical appearances.
- Scene coordinates, image coordinates, and observer coordinates are not conflated.
- Physical presence is not inferred from detection alone; non-detection is not treated as physical absence.
- Geometric exposure, detection, recognition, interpretation, and selection remain distinguishable.
- Unknowns and unsupported geometry remain explicit.
- For video, initial viewpoint is in `viewpoint.json` and supported viewpoint transitions are in TD.

## Scope boundary
This protocol tests observer-conditioned visual access. It does not validate a universal predator-selection model, retail purchase behaviour, camera calibration, or a general 3D reconstruction algorithm. The Retail Shelf essay supplies a useful conceptual analogy; its categories are hypotheses/illustrations, not established FV labels or quantitative metrics.