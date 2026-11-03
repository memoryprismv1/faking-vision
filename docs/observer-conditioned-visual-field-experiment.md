# Viewpoint initialisation and transition check

**Purpose:** verify that FV records viewpoint metadata in the correct packet location. This is a metadata test, not a scene-recognition or cross-view reconstruction experiment.

## Required behaviour

| Source | Required record |
|---|---|
| Image | Initial viewpoint in root-level `viewpoint.json` |
| Video | Initial viewpoint in root-level `viewpoint.json`, plus supported viewpoint transitions in TD |

## Image check

1. Analyse one image.
2. Create its viewpoint record with a stable `VP-` ID and observer type.
3. Record `initial_state.status` as `known`, `partially_known`, or `unknown`.
4. Include qualitative/source-supported position, orientation, description, and basis where available. Do not invent physical coordinates or camera geometry.
5. Validate `viewpoint.json` against `SPECIFICATION/FV_Viewpoint_Schema.json`.

## Video check

1. Analyse one video.
2. Create a viewpoint record for each distinct observer/viewpoint identity supported by the source. Record the initial state in `viewpoint.json`.
3. In TD, reference the active viewpoint with `viewpoint_id` where known.
4. Record supported viewpoint transitions over time, including movement, orientation change, zoom/reframing, or a switch to a distinct viewpoint. Retain the same ID when the same observer/camera moves.
5. Preserve unknowns; do not infer camera count, coordinates, or geometry from a scene cut or apparent perspective alone.

## Acceptance criteria

- An image packet records viewpoint initialisation without requiring TD solely for that purpose.
- A video packet records both initialisation and supported transitions.
- Unknown initial position/orientation is explicit, not silently omitted or guessed.
- Viewpoint movement is not recorded as object movement in OI.
- No same-scene image set, cross-view object matching, shared-scene hypothesis, correspondence ledger, or visual-field comparison is required for this test.

## Boundary

This check tests only viewpoint initialisation and transition metadata. It does not define a general visual-field schema or change existing OI, MSRM, TD, object promotion, or per-object visibility procedures.
