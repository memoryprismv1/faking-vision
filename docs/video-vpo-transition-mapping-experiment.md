# Video VPO transition-mapping experiment

**Recorded:** 5 November 2026  
**Status:** Active experiment plan  
**Scope:** Establish how FV maps a moving camera/observer through time before testing whether a video generator can follow that movement.

## Objective

The current VPO work represents a static camera pose. This experiment establishes the temporal transition map needed to describe a camera that moves during a video.

The first task is observation and mapping, not renderer implementation. Generate deliberately simple, short video clips with controlled camera movement, inspect what the generator actually produced, and record the supported movement in TD.

The initial experiment should favour obvious, isolated movements over cinematic complexity. Poor or imperfect generations are useful if the camera behaviour can still be observed.

## Existing FV architecture

- Root viewpoint.json records the observer/camera identity and its initial state.
- TD owns temporal observations and supported viewpoint transitions.
- The same continuous camera retains its viewpoint_id while moving.
- A distinct camera/viewpoint gets a distinct identity only when supported by evidence.
- Viewpoint movement is not object movement and must not be recorded as an OI entity.
- Unknown position, orientation, calibration, and geometry remain unknown; do not invent world coordinates.

This experiment does not create a new packet layer or separate camera-motion file. Transition observations belong in TD.

## Camera movement vocabulary to test

Classify the observed motion before attempting numerical pose estimation.

| Motion class | Observable distinction |
|---|---|
| Pan | Camera rotates horizontally; optical centre is approximately stationary |
| Tilt | Camera rotates vertically; optical centre is approximately stationary |
| Roll | Camera rotates around the viewing axis |
| Dolly in/out | Camera translates forward/backward along its viewing direction; perspective/parallax may change |
| Truck left/right | Camera translates laterally |
| Pedestal up/down | Camera translates vertically |
| Orbit | Camera translates around a target while changing orientation to maintain/adjust its view |
| Zoom in/out | Field of view changes without the perspective/parallax pattern expected from camera translation |
| Reframe | Image framing/crop changes; physical camera movement is not established |
| Combined movement | More than one supported movement class occurs together |
| Cut/viewpoint switch | The observed viewpoint changes discontinuously; do not represent this as continuous camera travel without evidence |
| Unclassified | Camera movement is apparent but the available evidence does not support a reliable class |

Do not force every movement into one of these categories. Preserve an unclassified or ambiguous result when necessary.

## Transition-mapping procedure

### Pass 1 — Establish the baseline

1. Inspect the complete clip once.
2. Identify the continuous camera/observer identity or identities.
3. Record the initial viewpoint in viewpoint.json.
4. Identify any cuts, edits, or abrupt viewpoint changes separately from continuous movement.
5. Establish the clip timeline and the intervals in which camera motion appears to occur.

### Pass 2 — Map each movement interval

For each candidate transition:

1. Mark the earliest time/frame at which movement is supported.
2. Mark the latest time/frame at which movement is supported.
3. Inspect evidence near the beginning, middle, and end of the interval.
4. Classify the movement using the vocabulary above.
5. Record direction where observable (for example pan-left, tilt-up, dolly-in, truck-right).
6. Describe the observed start and end framing/orientation qualitatively.
7. Note whether movement appears continuous, eased, abrupt, interrupted, or uncertain.
8. Record the evidence frames/observations and confidence.
9. Identify competing explanations, such as moving objects, scene edits, digital crop, or uncertain perspective.

Refine sampling around movement onset, offset, reversals, and changes in movement class. Do not sample uniformly merely for the sake of uniformity.

### Pass 3 — Separate camera motion from scene motion

Use multiple scene references where available:

- Broad background displacement consistent across static scene features can support camera motion.
- Relative displacement/parallax between near and far features can help distinguish translation from rotation.
- A moving subject against a stable background is not evidence of camera movement by itself.
- A changing crop or scale alone does not establish physical camera translation.
- If the background itself is animated or the scene is generated inconsistently, retain ambiguity.

Do not claim a physical camera path from screen-space motion alone unless the evidence and calibration support it.

### Pass 4 — Build the temporal transition map

The transition map should answer:

- Which viewpoint/camera is active?
- When does its state begin changing and when does it settle?
- What movement class is observed?
- In what direction?
- What is known about the start and end states?
- Is the path continuous, interrupted, or ambiguous?
- Which observations support the claim?
- What remains unknown?

Use viewpoint_id on the relevant TD observations/intervals. Keep the initial state in viewpoint.json; represent subsequent supported changes in TD.

## Candidate information for a TD transition event

This is an experiment checklist, not a proposed final schema. Reuse the existing TD event structure and existing packet conventions.

- Active viewpoint_id.
- Transition start and end time/frame.
- Movement class and direction.
- Qualitative start/end pose or framing descriptions.
- Numeric pose values only when the source, calibration, and coordinate frame support them.
- Evidence observation/frame references.
- Confidence or uncertainty and alternative explanations.
- Continuity classification (continuous, interrupted, discontinuous switch, uncertain).

Do not add a separate transition JSON file. Do not create new schema fields until the first clips reveal what information is actually needed.

## First generation set

Use short clips with one simple scene and one intended camera action per clip. Keep subject action minimal so camera movement can be isolated.

1. Static camera — control/baseline.
2. Pan left, then stop.
3. Pan right, then stop.
4. Tilt up or down, then stop.
5. Dolly in, then stop.
6. Truck laterally, then stop.
7. Zoom in/out as a contrast case against dolly.
8. Orbit around a stationary subject, if the generator can attempt it.

Start with the simplest three or four clips if generation time is limited. Do not combine movements until the individual classes have been mapped.

For each clip preserve the exact prompt and generated output as test evidence. The prompt expresses intended movement; the observed clip determines the FV transition map. Never copy the requested movement into TD as if it had been achieved.

## Initial acceptance criteria

- Initial camera identity and state are recorded in viewpoint.json.
- A continuous moving camera retains one viewpoint_id.
- Camera transitions are represented in TD and time-bounded.
- Camera movement is not misclassified as object movement.
- A cut or viewpoint switch is not silently represented as continuous travel.
- Pan/tilt/roll, translation, zoom and reframe are distinguished where evidence permits.
- Unknown physical coordinates and calibration remain unknown.
- Every transition claim has supporting observations or is explicitly marked uncertain.
- Prompted movement and observed movement are kept separate so generator failure is measurable.

## Out of scope for this first pass

- Full SLAM or 3D scene reconstruction.
- Estimating metric camera trajectories without calibration.
- A universal camera-motion schema.
- Building a physical renderer or guaranteeing novel-view generation.
- Complex multi-camera choreography.
- Changing OI/MSRM semantics or adding camera motion as an object.
- Assuming the generator obeyed its prompt.

## Next decision

After mapping the first generated clips, review which transition fields were actually necessary and whether the current TD representation can express them cleanly. Only then decide whether a schema or implementation change is warranted.
