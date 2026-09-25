# Faking Vision

**Working Process Specification / Additional Guidance — v0.22**

## Image Analysis Manual for the AI Team

### Purpose

**Faking Vision is an operational manual for an AI image-analysis
tool.**

Its purpose is to make image analysis more reliable by separating: -
what is visibly present, - what can be derived from visual
relationships, - what is inferred from stored knowledge, - what remains
unresolved, - and what additional observation would resolve the
uncertainty.

The goal is not to produce the most fluent description. It is to produce
the **best-supported visual analysis available from the evidence**.

## 1. The Core Problem

Humans receive images through extensive perceptual preprocessing. A
useful abstraction is:

**pixels → boundaries → objects → relationships → motion/state →
significance → language**

An AI image-analysis system has to perform much of this construction
itself.

The dangerous failure is not only misrecognition. A system can identify
a plausible object, infer plausible properties, construct a plausible
scene, and produce a fluent explanation while one or more underlying
inferences are unsupported.

The result can be **internally coherent but externally wrong**.

That is the central Faking Vision problem.

## 2. Evidence Levels

### Level 1 --- Direct visual evidence

What is visibly present in the image.

### Level 2 --- Relational evidence

What is derived from visible relationships: relative size, position,
overlap, grouping, orientation, and so on.

### Level 3 --- Calibrated inference

Claims derived using a reliable reference, known geometry, or other
justified calibration.

### Level 4 --- Knowledge-supported inference

Claims requiring stored knowledge about the object, species,
environment, or typical behaviour.

### Level 5 --- Unresolved / speculative

The available image does not justify a unique answer. Say so.

A fluent answer is not evidence.

## 3. Construct Objects Before Interpreting the Scene

Do not jump directly from the whole image to a narrative.

First construct the local visual scene: - candidate objects, -
boundaries, - major surfaces, - spatial relationships, - overlaps and
occlusion, - relative scale, - repeated objects, - unusual objects, -
foreground/background structure.

The image should first become a **maplet**: a locally useful
representation of the scene.

## 4. Object Properties vs. Object Methods

An image can provide evidence about both what an object **is** and what
it **does**.

Properties include shape, colour, texture, visible components, relative
size, and orientation.

Methods/actions include holding, resting, leaning, climbing, bracing,
moving, and interacting.

A single image is a snapshot. Do not pretend to have observed a complete
temporal sequence. A method may be inferred from configuration, but keep
the inference distinct from direct observation.

## 5. Object Promotion

Vision cannot process every possible object and relationship with equal
depth.

**Object promotion** means giving some candidate object or relationship
additional processing priority.

Promotion can be influenced by visual salience, movement, context, task
relevance, known affordances, current situation, previous interaction,
expected behaviour, unusualness, and relationships with other promoted
objects.

Do not assume the most visually obvious object is necessarily the most
important object.

## 6. Multiple Promotion Passes

When an image contains an ambiguous object or event, do not force the
first interpretation to become the final interpretation.

Run alternative analyses by changing what is promoted.

**Pass A --- Broad scene:** major objects and spatial structure.

**Pass B --- Ambiguous-object promotion:** focus on the uncertain object
and establish its visible properties.

**Pass C --- Context promotion:** focus on surrounding objects and
environment.

**Pass D --- Relationship promotion:** focus on scale, position,
contact, interaction, and alternative bindings.

When warranted, output **3--4 candidate interpretations**. These must be
evidence-based alternatives, not four random guesses.

## 7. Size Anchoring

An image does not automatically provide absolute physical size.

A familiar object can act as a **size anchor**: person, animal, door,
car, coin, common bottle, furniture, etc.

One reliable reference can establish a local scale regime for a whole
visual maplet:

**known reference → local scale → unknown objects → group comparison →
outlier detection**

For example, calibrated size can allow a fruit-sorting system to
identify unusually large or small fruit.

Distinguish:

> "A is twice the apparent size of B"

from:

> "A is 80 cm tall."

The second requires calibration.

Before using an object as an anchor, ask whether its physical size is
actually known, whether it is a normal-sized instance, whether
perspective affects the comparison, whether the objects occupy
comparable depth/planes, and whether the reference itself has been
correctly identified.

A bad anchor can produce a coherent **wrong scale**.

## 8. Faking Vision: The Adversarial Principle

The same machinery that allows useful visual construction can be
manipulated.

**Making Vision:** reliable reference → useful inference.
https://www.memoryprism.com/readings/making-vision-v2

**Faking Vision:** misleading reference → coherent wrong inference.

Potential manipulation targets include size reference, depth reference,
context, object identity, object promotion, movement,
background/foreground classification, and familiar-object assumptions.

A Faking Vision test should ask:

> **What assumption does this image cause the analyser to make?**

not merely:

> **Can the analyser recognize this image?**

## 9. Camouflage and Sleight of Hand

These are related but distinct object-promotion manipulations.

**Camouflage:** the target attempts to remain background --- "I am part
of the scenery."

**Sleight of hand:** the performer promotes the wrong object ---
"process B while A undergoes the consequential event."

Looking at the general scene is not equivalent to allocating equal
processing to every object.

## 10. When the View Is Insufficient

A major failure mode is treating an inadequate view as a complete
observation.

A system should be able to say:

> **Object detected; identity unresolved.**

A wide view may show "small blue object in a candleholder"; a closer
view may establish "small blue cat-shaped figurine." The second view
provides additional evidence rather than merely a prettier picture.

**Do not hallucinate the missing pixels.**

## 11. Active Vision

For an embodied system:

**SEE → CONSTRUCT → ASSESS → IDENTIFY UNCERTAINTY → ACQUIRE BETTER VIEW
→ UPDATE**

If the uncertainty matters, the system should be able to request or
generate a better observation by moving the camera/body, changing
viewpoint, zooming, obtaining another image, using another sensor, or
inspecting another side.

A robot should be able to spend movement in order to obtain information.

## 12. Blind Image Analysis

Separate:

### Image evidence

What can be seen directly?

### Internal comparison

What can be compared using objects already present?

### External knowledge

What is supplied by the model's object database?

### Calibration

What is established from known references?

### Uncertainty

What remains unresolved?

For difficult images, explicitly produce multiple candidates rather than
collapsing immediately to one.

## 13. What the Tool Must Not Do

-   Do not manufacture absolute measurements without calibration.
-   Do not turn database knowledge into visual evidence.
-   Do not infer a complete temporal event from one frame.
-   Do not promote the first plausible interpretation into certainty.
-   Do not treat familiar-looking as known.
-   Do not hide calibration assumptions.
-   Do not confuse absence of evidence with evidence of absence.

## 14. Preferred Output Structure

For difficult or consequential images:

1.  **Scene**
2.  **Objects**
3.  **Relationships**
4.  **Calibration**
5.  **Direct evidence**
6.  **Inferences**
7.  **Uncertainties**
8.  **Alternative readings**
9.  **Next observation**

## 15. Core Rule

> **Never confuse a useful visual inference with a directly observed
> fact.**

Vision is a construction process. That construction is necessary for
useful analysis and is also where errors enter.

Faking Vision does not try to eliminate inference. It makes inference
**visible, calibrated, testable, and revisable**.

## 16. Long-Term Robot Version

For a static image analyser:

**observe → construct → qualify**

For an embodied robot:

**observe → construct → qualify → decide whether information is
sufficient → move/look → observe again**

Robot eyes are therefore not simply object-recognition cameras. They are
an information-acquisition system.

The robot should know:

> **what it has seen, what it has inferred, what it does not know, and
> what it could look at next to reduce uncertainty.**

### Working principle

**Better vision is not more confident description.**

**Better vision is better separation between evidence, inference,
calibration, uncertainty, and the next useful observation.**


---

## 17. Adaptive Temporal Decomposition for Video

Video analysis must not be reduced to a fixed frame-sampling rate.

### Core rule

**Frame = source evidence.  
Temporal interval = representation unit.**

The AI should determine how much temporal resolution is needed from the visual evidence.

A useful formulation is:

> **Recursively divide time wherever the current visual representation cannot adequately account for what occurs between its observations.**

This is an evidence-resolution problem, not a frame-count problem.

### 17.1 Do not use fixed-rate sampling as the FV model

Do not define the analysis as:

- every N frames
- every X seconds
- one frame per second
- a fixed number of keyframes per scene

Such sampling can be used as an engineering shortcut, pre-pass, or comparison condition, but it is not the FV temporal architecture.

Likewise, an algorithm that simply subdivides every interval until it reaches a predetermined minimum duration is not genuinely adaptive.

### 17.2 Recursive procedure

For each coherent temporal region:

1. Establish an initial interval.
2. Inspect its temporal endpoints and sufficient interior evidence.
3. Construct the relevant FV state: entities, boundaries, properties, relationships, state, persistence, and uncertainty.
4. Ask whether one representation can adequately describe the interval.
5. If yes, retain the interval as a temporal leaf.
6. If no, divide the interval into ordered subintervals.
7. Repeat until the retained intervals are adequately represented or the available evidence reaches its limit.

The purpose is not to keep every frame. The purpose is to preserve every materially relevant observation and the uncertainty about what happened between observations.

### 17.2.1 Perturbation-driven adaptive sampling

Adaptive temporal decomposition should allocate observation effort according to the observed rate and concentration of visual perturbation. Begin with a **lazy/coarse scan**. When a temporal-difference (TD) cluster appears inside a chunk or interval, increase sampling density locally and recursively inspect the affected subinterval. If perturbation persists or becomes denser, increase temporal resolution again. When perturbation subsides, reduce the sampling density and return toward the lazy scan.

The initial division of a video into length-dependent chunks is an engineering search structure, not a fixed temporal resolution. A **merge-sort-like temporal sampling strategy** is an allowed implementation pattern: divide the source into chunks, inspect boundaries and representative interior points, detect perturbation, and recursively subdivide only the affected chunks/subintervals.

The intended behaviour is: **quiet → lazy; emerging perturbation → more attention; sustained/high perturbation → high-power scan; perturbation subsides → relax.** The exact sampling rates are implementation parameters to be empirically calibrated. They are not FV constants.

The purpose of adaptive sampling is efficient acquisition of sufficient temporal evidence. It does not require object identity, interaction inference, or maintenance of a persistent event history. Those may be downstream uses and are not prerequisites for temporal packet generation.


### 17.2.2 Change Propensity and change propagation

**Change Propensity (CP)** is an attention-prior mechanism for deciding what to inspect first under limited observation effort. It is not an importance score, observed change, motivation, or source fact.

**Static Change Propensity (SCP)** is the baseline propensity associated with an object before the current event develops. It remains stable during an analysis unless the experiment explicitly defines recalibration. Low-SCP objects are not discarded; lazy scanning remains responsible for the rest of the scene.

**Current Change Propensity (CCP)** is the present change-priority state after incorporating current observations, interactions, and propagation. CCP can rise or fall while SCP remains unchanged.

When a perturbation propagates through objects, TIR should record **`change_generator_obj_ids`**: the persistent object IDs for which source evidence supports generator/transmitter status. Also record affected object IDs where supported. An affected object may become a subsequent generator. Preserve only the propagation chain actually supported by observations; do not invent a complete causal graph.

Example:

`generator A → affected B → subsequent generator B → affected C`

### 17.2.3 Evidence Yield (EY)

**Evidence Yield (EY)** is a temporal evidence record, not a scalar score.

Conceptual minimum structure:

```text
EY = {
    current: <current evidence/state>,
    frameid: <source frame>,
    previous: [<earlier evidence records>]
}
```

`current` records what meaningful evidence the object or region is producing now. `previous` preserves relevant prior evidence so the current observation can be interpreted temporally. EY may describe movement, boundary change, displacement, interaction, emergence, disappearance, or other source-grounded evidence.

EY does not itself identify the cause of the evidence.

### 17.2.4 Incongruity

Operational **incongruity** occurs when the current observation produces materially more or different evidence than the current expectation accounts for. A useful case is low expected change followed by meaningful EY.

Incongruity is an expectation/observation mismatch that can trigger additional investigation. It is not an object identity, cause, or semantic explanation.

### 17.2.5 Explicit task objectives

An experiment may supply an external task objective, such as tracking a specified thing across multiple videos. The objective may alter sampling priority and the objects/relationships selected for closer investigation.

The task objective remains separate from source evidence. It may specify **what to investigate**, but it must not supply missing identities, events, motivations, or temporal facts. Evidence acquired under the task objective is still subject to normal FV observation, uncertainty, and promotion rules.

CP/CCP, EY, and change-generator relationships must remain distinct: CP controls attention priority; EY records evidence produced; change-generator fields record supported propagation relationships; the task objective specifies the external investigative target.

### 17.3 What makes an interval unresolved?

Test at least:

- **Visual difference:** materially different visible structure.
- **Object/boundary difference:** appearance, disappearance, splitting, merging, or changed boundaries.
- **Persistence:** whether the same visual entity can still be represented continuously.
- **Spatial relationships:** contact, separation, relative position, ordering, containment, occlusion, co-motion, etc.
- **State:** pose, orientation, direction, behaviour, expression, component state, or other recorded state.
- **Uncertainty:** inability to establish whether a material change occurred or which identity/relationship is involved.

Global pixel difference is only one possible evidence source. It must not be the sole event criterion.

A small local event can require temporal subdivision even when almost the entire frame is unchanged.

### 17.4 Identity continuity

Temporal subdivision does not create new entities.

When associating observations across intervals, consider:

- position and geometry;
- motion and co-motion;
- shape, area, and appearance;
- boundary continuity;
- pairwise spatial relationships;
- occlusion and reappearance.

If continuity cannot be established, preserve the uncertainty rather than forcing either a merge or a split.

Movement is not duplication. Occlusion is not deletion. Off-screen absence is not deletion.

### 17.5 Relationship changes are temporal evidence

Do not look only for object-level state changes.

A relationship may change while both objects remain visually similar:

- near → farther
- separate → contact
- beside → separated
- visible → occluded
- following/co-moving → independent motion
- outside → inside

MSRM describes the spatial relationship. TD records how it changes through time.

### 17.6 Temporal maplets

A retained temporal leaf may be represented as a bounded temporal maplet containing:

- temporal bounds;
- relevant OI state;
- relevant MSRM state;
- transition/evidence references;
- uncertainty.

This does not replace OI, MSRM, or TD. It is a way of organizing the temporal leaves produced by adaptive decomposition.

### 17.6.1 Temporal timestamps are index metadata

A source timestamp, frame number, or derived source-time coordinate is temporal index metadata attached to an observation or TD record. It is not itself a visual object and must not be promoted or repeatedly represented as scene content merely because its displayed value changes from frame to frame.

If the source contains a visually displayed CCTV timestamp, that timestamp is visual evidence. Read it from the relevant source frame or snapshot only when the question requires it. The machine temporal coordinate and the visually displayed timestamp are distinct fields.

### 17.7 Evidence retention

Retain source evidence preferentially around:

- state transitions;
- identity ambiguity;
- occlusion and reappearance;
- important relationship changes;
- observations that promote or refine an object/component.

Do not retain every frame simply because a fixed-rate sampler selected it.

### 17.8 Operational test

When analysing a video, the AI should be able to answer:

> **Why does this interval need to be split?**

A valid answer should point to observable unresolved structure or perturbation, such as a local visual change, appearance/disappearance, boundary change, state transition, relationship change, uncertainty, or insufficient temporal evidence.

If the only answer is:

> "because the interval reached the sampling rate"

then the temporal analysis has not implemented FV's adaptive principle.

### 17.9 Generality

This rule applies to all FV visual sequences, not only CCTV.

Examples include:

- CCTV/security footage;
- driving and LiDAR-camera sequences;
- drone and archaeological video;
- phone video;
- historical film;
- animations/GIFs;
- scientific imaging sequences;
- any ordered visual sequence where temporal information matters.

The source determines where temporal resolution is required.

---


## 17.10 Moving-camera perturbation

A moving camera is itself a source of temporal perturbation. High temporal-difference density may arise from the camera sweeping past otherwise static world structure. Do not automatically interpret this as object motion, duplication, or independently moving entities. Transient structures that briefly enter, traverse, and leave the field of view remain observations and may be information-bearing without persistent identity.

## 17.11 Perturbation-density compression

A dense temporal-difference stream may be represented by fewer evidence-bearing snapshots when adaptive temporal decomposition retains the temporal structure needed to locate materially relevant perturbations. Snapshot count alone is not the measure of success. Reconstruction experiments should compare source TD behavior, FV-retained evidence, and reconstructed-output TD behavior.

## 17.12 Reconstruction experiments may be deliberately ugly

A reconstruction renderer does not need to be aesthetically convincing to be useful. The first question is whether FV packet + retained snapshots can drive regeneration of the temporal/visual structure represented by FV. Simple interpolation, stitching, compositing, or other crude operators are valid first tests. Generated intermediate imagery is reconstruction output, not source evidence, unless supported by the packet. Every generated reconstruction should be independently FV-audited.

## 17.13 Experimental material selection

FV experiments do not require prestigious, large, or specialized datasets. Prefer small, directly accessible material that permits rapid observation, modification, reconstruction, and failure analysis. Dataset prestige and scale are not FV requirements.

## 18. Updated temporal working principle

For still images:

**observe → construct → qualify**

For video:

**observe → construct → test temporal consistency → subdivide unresolved intervals → qualify → reconstruct**

For embodied systems:

**observe → construct → identify uncertainty → acquire better observation → update**

The temporal question is therefore not:

> "How often should the system sample?"

It is:

> **"What temporal resolution is required to represent what the source actually shows?"**




### 17.18 Multi-pass temporal analysis and TIR

**TIR — Temporal Investigation Record** is the persistent investigation record
used during temporal analysis. It replaces the implementation-oriented name
TEMP_TD.

TIR is distinct from **TD.json**:

- **TIR** is the investigation record. It may contain rich observations,
  measurements, hypotheses, competing interpretations, intermediate conclusions,
  sampling decisions, rejected hypotheses, and unresolved questions.
- **TD.json** is the official temporal record. It contains the evidence-grounded
  temporal information committed to the FV packet.

TIR is therefore not a temporary or inferior version of TD. It is the record of
the investigation from which the official TD record is derived. The AI may use
TIR freely as an analytical workspace and may revise, extend, or contradict
provisional entries as new evidence is acquired.

Information should be promoted from TIR into TD only when the evidence supports
the corresponding official temporal statement. Provisional reasoning should
remain distinguishable from committed packet facts.



Adaptive Temporal Decomposition may use multiple analysis passes before deciding
which observations to retain. The passes serve different purposes and must not
be confused with a fixed sampling rate.

#### 17.18.1 Initial global interval for long video

For a video longer than one minute, an implementation may use an initial global
temporal interval of **4 seconds** as an engineering starting point.

Let:

- `L` = video duration in seconds;
- `I` = 4 seconds;
- `a = ceil(L / I)` = number of global interval positions.

The 4-second value is an implementation parameter, not an FV constant. It is a
starting probe whose adequacy must be evaluated empirically.

#### 17.18.2 Random reconnaissance pass

Before or alongside the normal global pass, the AI may perform an independent
random reconnaissance pass.

Set:

`r = ceil(a / 2)`

Generate `r` unique random temporal positions across the video, subject to the
experiment's sampling-coordinate rule. In the current implementation, random
reconnaissance positions are selected from **odd-numbered temporal positions**
so that they are distinct from the even-position global sampling structure.

Random positions must be non-duplicate and bounded by the actual video
duration. If an adaptive candidate would otherwise reuse a random observation,
select another unsampled coordinate.

Each random observation is analysed and its temporal evidence is accumulated in
**TIR**. The random reconnaissance TD is an in-memory analysis resource
during the run; it does not need to be exported as a separate file.

Random reconnaissance is not itself the final temporal representation. Its
purpose is to provide an independent view of where temporal activity,
object/action changes, transitions, or uncertainty may occur.

#### 17.18.3 Normal global pass

Run the global temporal sequence using the current initial interval:

`0, 4, 8, 12, 16, ...`

At each interval, compare the observations and update TIR.

The global interval is therefore a default observation stride, not a claim that
nothing meaningful occurred between its endpoints.

#### 17.18.4 TIR is the active temporal analysis workspace

During video analysis, maintain a rich temporary temporal-data structure
(**TIR**) that may contain substantially more information than the final
TD packet schema.

TIR may contain, as applicable:

- temporal observations and their source coordinates;
- global visual change;
- local/regional visual change;
- object appearance/disappearance;
- object movement;
- object action or apparent action;
- object pose, orientation, direction, or state change;
- object identity continuity and ambiguity;
- object-to-object relationship changes;
- contact, separation, following, containment, occlusion, and co-motion;
- camera movement, pan, tilt, zoom, and reframing;
- affected spatial regions;
- persistence and transition evidence;
- local activity baselines;
- hypotheses and intermediate conclusions;
- evidence supporting or contradicting a conclusion;
- uncertainty;
- reasons an interval does or does not require further observation;
- relationships between observations from different passes.

TIR is an analytical scratchpad, not a restricted scalar TD score. The AI
should use it to form meaningful temporal conclusions and to decide where
additional evidence is useful.

The final TD record is a structured, evidence-grounded representation derived
from the analysis. TIR may therefore be richer, messier, and more
exploratory than exported TD.

#### 17.18.5 TD dimensions for adaptive decisions

Adaptive decisions should consider multiple forms of temporal evidence rather
than a single pixel-difference value. At minimum, consider:

1. visual change;
2. object/boundary change;
3. object movement;
4. object action;
5. persistence/identity continuity;
6. spatial relationship change;
7. state change;
8. camera/framing change;
9. spatial concentration of change;
10. uncertainty and insufficient temporal evidence.

Object change and object action are temporal evidence even when whole-frame
visual difference is modest. Conversely, large whole-frame change caused by
camera motion must not automatically be treated as object-level activity.

#### 17.18.6 Global versus local TD

TIR should distinguish **global** temporal change from **local/regional**
temporal change where the evidence permits.

- Global TD describes change distributed across much or all of the frame.
- Local TD describes change concentrated in one or more spatial regions.

A frame-wide perturbation may indicate camera movement, zoom, reframing, lighting
change, or a genuinely global scene change. A concentrated perturbation may
indicate object movement, action, appearance/disappearance, occlusion, or a
local state/relationship change.

This distinction is an analysis aid, not an automatic semantic classification.
The AI must use the observed structure and uncertainty before assigning meaning.

#### 17.18.7 Local baseline

Where useful, TIR should maintain a slowly updating **local activity
baseline** for a region or temporal stretch.

Adaptive significance should be judged relative to recent local behaviour when
possible, rather than only against a single fixed global threshold.

A continuously busy region should not trigger unlimited subdivision merely
because its absolute TD remains high. A sudden departure from that region's
recent behaviour should receive greater attention.

A local baseline is itself provisional evidence and must be updated as new
observations arrive.

#### 17.18.8 Adaptive insertion

When the current global interval contains unresolved or materially significant
temporal evidence, insert an additional observation.

The default insertion point is the **midpoint** of the interval. Midpoint
selection is intentional: the global temporal positions and the random
reconnaissance positions use different coordinate parity in the current
implementation, so midpoint insertion normally supplies an observation that
has not already been sampled.

If an alternative insertion point is considered, first check whether that
temporal coordinate has already been sampled. Never duplicate an existing
observation merely because a different pass discovered the same coordinate.

The midpoint is therefore an evidence-acquisition convenience, not a claim that
the true event boundary lies at the mathematical midpoint.

#### 17.18.9 Meaningful adaptive conclusions

TIR should be used to make temporal conclusions before requesting further
observations.

Examples include:

- an object appears to persist while changing location;
- a person/object begins or ends an action;
- a camera movement explains frame-wide change;
- a localized change is inconsistent with camera movement and warrants object-level inspection;
- an object becomes occluded and later reappears;
- a relationship changes while the participating objects remain present;
- a transition appears to occur within a particular interval but its timing is unresolved;
- an interval contains insufficient evidence to distinguish competing temporal explanations.

The answer to "why sample here?" should therefore be a conclusion about the
source evidence or unresolved temporal structure, not merely "because the
threshold was exceeded."

#### 17.18.10 Minimum-width investigation

An implementation may define a minimum temporal width for a **specific hot
interval** when precise transition localization is required. Activity magnitude
and interval width answer different questions:

- activity evidence determines whether an interval deserves deeper investigation;
- minimum width determines when the investigation has reached the desired
  temporal resolution.

A minimum width must not be applied uniformly to every interval. Quiet intervals
remain on the global lazy scan. A hot interval may continue to be subdivided
until its temporal width is sufficiently small for the question being analysed
or the available source evidence reaches its limit.

This is an implementation control for unresolved hot regions, not a replacement
for evidence-driven adaptive sampling.

#### 17.18.11 Random reconnaissance refresh

The initial random reconnaissance pass is primarily a triage mechanism. It does
not automatically need to be repeated after every adaptive subdivision.

However, if a region becomes sufficiently complex or uncertain that the original
reconnaissance evidence is no longer informative, a local reconnaissance pass
may be performed. Such a refresh is optional and should itself be recorded in
TIR so that the provenance of the additional observations is clear.

#### 17.18.12 Pass interaction

The passes are complementary:

```text
random reconnaissance
        ↓
independent temporal evidence
        ↓
TIR  ←──────────────┐
        ↑               │
4-second global pass    │
        ↓               │
actual TD ──────────────┤
                        │
adaptive investigation ─┘
        ↓
richer TIR
        ↓
temporal conclusions
        ↓
retained evidence / final TD
```

The system must not treat the random pass, the global pass, or the adaptive
pass as independently authoritative. Their observations are evidence that is
combined in TIR.


### 17.18.13 Audio-assisted adaptive sampling

When the source video contains intentionally included audio, the AI may generate a timestamped transcript before beginning the initial temporary temporal investigation.

Treat the transcript as a **provisional sampling variable**, not as committed evidence. It can identify candidate times, events, actions, or relationships that may deserve additional visual sampling.

During TIR construction, test transcript claims against the source audio and the independently acquired visual observations. Maintain cumulative outcomes so that a few incorrect transcript interpretations do not cause the entire audio channel to be discarded.

Record at least:

- **transcription fidelity** — whether the transcript accurately represents the source audio;
- **cross-modal support** — whether a narrated claim corresponds to the visual evidence;
- unresolved or ambiguous transcript content;
- commentary whose timing/context does not correspond to the currently observed scene.

If a transcript claim identifies a potential gap in the current temporal representation, use its location as an adaptive sampling target, subject to the current transcript assessment and timing/context information. The claim does not need to be visually supported yet. Acquire the additional source observation, update TIR, and promote only source-supported temporal statements into TD.

Do not assume that commentary is synchronized scene-by-scene. A statement may describe an earlier or later event, an off-screen event, or a broader interpretation of the sequence. Do not resolve such a mismatch as false, satire, fabrication, or intent without evidence.

### 17.18.13 Selected-frame FV image analysis

Every source frame that FV actually captures or retains as an evidence observation **must undergo the default FV image-analysis procedure**. Temporal sampling determines which source frames are acquired as evidence; it does not replace image analysis of those frames with mere frame retention.

For each selected frame, perform the applicable FV image-analysis passes: visual inventory, candidate generation, entity/component/appearance decision, identity assessment where temporal context permits, and packet/evidence promotion as warranted. The resulting frame-level analysis must be available to TIR and may update OI, MSRM, TD, uncertainty, disputes, or other packet records where justified.

A selected frame is therefore both **source evidence and an FV image-analysis observation**. A packet must not treat a captured frame as semantically unanalysed merely because the temporal sampler selected it. Frames that were never selected do not require the same full FV image-analysis treatment.

The temporal sampler answers:

> **Which observations are worth acquiring?**

FV image analysis answers:

> **What is present in each acquired observation?**

These are distinct operations. Neither substitutes for the other.

### 17.18.14 Behaviour-triggered component tracking

Do not track every declared component merely because it exists. **Component tracking is triggered by component behaviour when that behaviour creates enough perturbation or uncertainty to matter to the FV representation.**

A component may remain an inventory/property detail while behaviourally irrelevant. Promote it to a temporal tracking target only when its change, movement, interaction, deformation, state transition, or other behaviour materially affects the scene representation, an object state, a relationship, an action, reconstruction fidelity, or an unresolved temporal question.

Examples:

- A visible wheel does not automatically require wheel tracking.
- Wheel rotation that materially explains vehicle behaviour may require local tracking.
- A person's hand does not automatically become a tracked component.
- A hand reaching for, contacting, or manipulating another object may make the hand's behaviour information-bearing.
- A decorative button that changes without affecting represented structure need not be tracked.

**Component tracking is therefore perturbation-triggered, not inventory-triggered.** The tracking decision and its evidence should be recorded in TIR, and any promoted component state/change should enter TD only when supported by the retained observations.


### 17.14 PC as a canonical object database

PC may also serve as the project’s **canonical object database** when a project declares reusable visual objects as genuine project-wide constants. This is a functional use of the existing PC structure, not a new packet layer or a replacement for PC.

The purpose of PC object declarations is to prevent repeated object instantiation across scenes or temporal observations when the evidence supports persistent identity. OI records which declared objects are present and their scene-specific state; TD records changes to those persistent identities through time.

An object declared in PC remains in the existing PC object/declaration structure. **Do not reorganize PC, introduce a separate object-database container, or move existing PC information merely to support this use.** Object-database capability is additive.

When a PC file is created for a packet before packet merge, each object ID must be packet-scoped and traceable in the form `<packet_id>-<object_id>` (for example, `PKT-CCTV-001-OBJ-003`). Do not assign a merged/global object identity before packet merge. The packet-scoped ID preserves provenance and allows later identity matching and object-database normalisation.

A `packet_id` is a first-class packet identifier. It must be stable within the merge set and must be carried wherever packet provenance is required.

### 17.14.1 Snapshot property for PC objects

A PC object may include a `snapshots` property containing references to preserved visual evidence for that canonical object. These references provide visual grounding for inspection, comparison, packet merge, and later object-database normalisation. A snapshot does not replace the canonical PC declaration and does not become canonical truth merely by being attached to the object.

The `snapshots` property is an additive property of an existing PC object declaration. Adding it must not change the existing PC structure, field organization, or semantics. If no visual evidence is available or needed, the property may be absent.

### 17.14.2 Experimental status

Using PC as an object database is an **architectural capability to be tested**, not a claim that the methodology has already been validated. The intended test material is continuous same-camera footage divided into temporally adjacent files. The experiment is specifically intended to test object reuse, packet merge, and object-database normalisation.

### 17.14.3 Packet merge identity rule

When multiple packets describe temporally adjacent material from the same source/world, do not assume that local object IDs are globally identical. Merge packet-scoped PC object declarations by comparing their source evidence, temporal continuity, object properties, relationships, and retained snapshots. Preserve each source packet ID throughout the merge. Only after the evidence supports identity equivalence should a normalised persistent object identity be established.



### 17.15 TD owns video observation records

For video, the **observation record is a record type, not a required separate file**. TD is the authoritative temporal diff log and owns the temporal baseline observations and the differences derived from them. Do not create `observation.json` or `observations.json` merely because the workflow creates observation records. A separate observation file may be introduced only by an explicit future FV specification.


## 18. Packet-Level Disputes and Resolution Gate

A **dispute** is a structured packet-level record that explicitly states that automated analysis cannot reliably resolve a visual question and **human intervention is required**. Disputes are represented as JSON; do not use a `.flat` dispute file.

Disputes are not merely notes about uncertainty and are not limited to reconstruction failures. They may concern an object, component, identity association, spatial relationship, temporal event, image region, source frame, generated/re-rendered result, or any other consequential unresolved visual question. The affected OI/MSRM/TD record may reference a `dispute_id`, but the dispute remains visible at packet level.

### 18.1 Required dispute record

The packet must contain `dispute.json`. It is the current dispute state and the rendering gate. Each dispute record should preserve, at minimum:

- `dispute_id`;
- `issue`;
- source identifier and affected layer/record/region;
- `snapshot_ids` and other evidence references;
- what the AI observed or attempted to resolve;
- the specific ambiguity, conflict, or failure;
- `resolution_status`;
- `resolved_by`;
- `resolution_remark`;
- `human_action_required`;
- resolution/reprocessing timestamps where applicable;
- AI reprocessing status and affected records where applicable.

The aggregate `dispute.json.status` must be one of:

- `none` — no dispute exists;
- `open` — one or more disputes remain unresolved or require human intervention;
- `resolved` — all recorded disputes have been human-resolved, reprocessed by AI, and the packet has passed validation.

For rendering, only `none` and `resolved` release the packet. **An `open`, missing, malformed, or inconsistent dispute state blocks rendering.** The renderer must not decide that an unresolved dispute is harmless.

### 18.2 Human resolution and packet reconciliation

A human resolves the disputed question and may add or correct object information and other relevant packet detail. The human does **not** directly declare the packet reconciled. The original automated observation and uncertainty must remain traceable.

The packet is returned to the AI with the human-supplied information. The AI then performs **packet reconciliation**:

1. read the current `dispute.json`;
2. inspect the cited source evidence and referenced snapshots;
3. inspect the human-supplied changes/additions in the packet;
4. determine which object information and project-constant information are established by the human resolution;
5. update **OI** and **PC** as justified by the resolution and source/evidence;
6. preserve provenance and the original dispute evidence;
7. determine whether every recorded dispute has been resolved.

The human's additions are later resolution information. They must not be represented as evidence that the AI originally knew the answer.

### 18.3 Dispute reconciliation states

There are two reconciliation outcomes.

**A — All disputes resolved.** If all disputes are resolved and the reconciled packet passes validation, rename/move the existing `dispute.json` to `dispute.reconciled.json`. Then create a **new, small `dispute.json`** containing only the current aggregate resolved state needed by the rendering gate. The archived `dispute.reconciled.json` retains the detailed dispute history and resolution material; the new `dispute.json` is deliberately cheap to open.

**B — One or more disputes remain unresolved.** Keep the existing `dispute.json` in place and change **only its aggregate status** to `open`. Do not rebuild or rewrite the full dispute record merely to update the current state. The unresolved dispute details remain in the existing file.

This separation keeps the current rendering decision cheap to inspect even when a long investigation has accumulated a large dispute history.

When all disputes have been reconciled, the new `dispute.json` may be only:

```json
{
  "status": "resolved"
}
```

The detailed records remain in `dispute.reconciled.json`.

### 18.4 Mandatory AI reconciliation and rendering gate

After human intervention, rendering remains blocked until AI reconciliation and packet validation are complete. The AI must not merely change a status field to `resolved`.

For a fully resolved packet:

```text
AI analysis
    ↓
dispute.json = open
    ↓
RENDERING BLOCKED
    ↓
human reviews source/evidence and adds or corrects packet information
    ↓
packet returned to AI
    ↓
AI reads dispute.json + human changes + source/evidence
    ↓
OI / PC updated as justified
    ↓
packet validation
    ↓
dispute.json → dispute.reconciled.json
    ↓
new small dispute.json = resolved
    ↓
RENDERING PERMITTED
```

If reconciliation cannot reliably resolve every dispute or validation fails, retain `dispute.json` with aggregate status `open`; do not create a resolved state.

The reconciliation process must preserve the distinction between source evidence, the original AI uncertainty, human resolution, and subsequent AI packet changes.

### 18.5 Current dispute file versus reconciliation history

`dispute.json` is the **current actionable/rendering-gate state**. `dispute.reconciled.json` is the **archived detailed record of a completed reconciliation**.

The current state file should remain small when possible. A long investigation must not require opening a large historical dispute file merely to determine whether rendering is currently permitted.

## 18.6 Audio evidence and transcript

When audio is intentionally included in a video packet, preserve the **audio file and its transcript together as source-derived evidence**. The transcript is an interpretation/extraction of the audio; it is not a substitute for the audio evidence.

### Audio-assisted temporal analysis

Generate the timestamped transcript **before the initial temporary TIR/TD temporal investigation** and keep it as a provisional analysis variable.

The transcript may be used during adaptive temporal sampling as an additional cue. A transcript segment can point the investigation toward a time or interval that deserves visual inspection because the initial temporal observations may not yet contain the relevant event.

The transcript is **not authoritative**. The temporal investigation must independently test it against the source audio and the visual evidence.

TIR should maintain a cumulative assessment of the transcript/audio channel rather than a binary keep/discard decision. At minimum distinguish:

- supported transcript content;
- contradicted transcript content;
- unresolved or ambiguous transcript content;
- audio-supported commentary that does not correspond scene-by-scene with the current visual interval.

A small number of transcript errors or apparent mismatches does not automatically invalidate the transcript as a useful information channel. Continue testing the channel and use transcript claims as candidate sampling cues to locate potential gaps in the current TIR/TD.

A commentary segment may be accurate while referring to an earlier, later, off-screen, or otherwise different scene state. Therefore, a mismatch with the current visual interval is not by itself evidence that the commentary is false, satirical, fabricated, or intentionally misleading. Preserve the discrepancy and uncertainty unless source evidence resolves it.

When a transcript-supported claim reveals a gap in the current temporal representation, perform additional sampling at the relevant location. Add the resulting evidence to TIR and promote the corresponding statement into TD only when the retained source evidence supports it.

Use an optional packet-level `audio/` directory:

```text
audio/
    source.<original-extension>
    transcript.json
```

The exact source audio format may vary. The packet must preserve the relationship between the audio file and the source video, including source identity and relevant time alignment.

`transcript.json` should contain timestamped transcript segments and, where supported, speaker/voice attribution and transcription uncertainty. Do not invent words that are not supported by the audio. If speech is unclear, preserve the uncertainty rather than silently normalising it.

Audio and visual evidence are separate evidence streams. A transcript may inform OI, TD, disputes, or other packet fields, but those fields must remain traceable to the audio segment or visual evidence that supports them. When audio and visual evidence disagree, preserve the conflict and handle it through the existing uncertainty/dispute process rather than silently privileging one stream.

`AUDIO_COMPANION.txt` may continue to provide human-readable audio notes, but it does not replace the audio file or `transcript.json` when a transcript is intentionally included.

When audio is included, packet validation must verify that the audio file and transcript are present, source-aligned, and mutually traceable, and that TIR records the transcript assessment and material discrepancies.

## 19. Snapshots

Use **snapshots** as the general name for preserved visual evidence. This replaces source-specific terminology such as `saved_frames`.

The packet filesystem location is lowercase **`snapshot/`**. Its permitted structure is:

```text
snapshot/
    manifest.json
    verification/
    objs/
    disputes/
```

`manifest.json` is optional and, when used, lives directly inside `snapshot/`; it is not a packet-root manifest. The three listed directories are the only permitted subfolders under `snapshot/`. **Do not create nested folders inside `verification/`, `objs/`, or `disputes/`. Do not create any other snapshot subfolder without explicit operator permission.**

Object evidence may be stored under `snapshot/objs/`. An object snapshot may include both a preserved source crop and a separate highlighted analytical crop showing the object boundary or region used for analysis. The highlighted version is an analytical aid and must never replace or masquerade as the source evidence.

A snapshot is preserved **as-is** when it represents source evidence. Analytical derivatives such as highlights must remain distinguishable from source evidence.

If the AI cannot confidently read an object or a re-rendered image produces a strange/inconsistent result, preserve the relevant snapshot(s) and create a packet-level dispute when human intervention is required.

### 19.1 Packet and filesystem discipline

Assign a stable `packet_id` before packet contents are generated. Use it consistently in packet metadata and packet-scoped object IDs.

Folder depth is an operator-interface cost. Do not create folders for organizational convenience. Before creating any folder not explicitly permitted by this specification, ask the operator for permission. The `snapshot/` structure above is closed: no extra subfolders and no nested folders inside its permitted subfolders without explicit permission.


## 20. Operational rule

**Uncertainty may remain in OI/MSRM/TD. A dispute makes consequential unresolved uncertainty visible and actionable at packet level. Snapshots preserve the visual evidence needed to resolve it. An open dispute blocks rendering; human resolution requires AI reprocessing and packet validation before the dispute can become resolved.**


## 21. Change log — v0.11

- Refined Adaptive Temporal Decomposition to explicitly support perturbation-driven adaptive sampling: lazy scanning by default, increased local sampling around TD clusters, recursive subdivision while perturbation persists, and relaxation when it subsides.
- Added a merge-sort-like chunking strategy as an implementation pattern for locating temporal perturbations efficiently without making fixed-rate sampling the FV model.
- Clarified that sampling density is a dynamic implementation parameter driven by observed perturbation rate/concentration and must be empirically calibrated.
- Clarified that CCTV packet generation does not require object identity, interaction inference, or persistent event history.
- Clarified that frame numbers and source timestamps are temporal index metadata, not visual objects; displayed CCTV timestamps remain source visual evidence and are inspected only when needed.

### Change log — v0.12

- Added moving-camera perturbation.
- Added perturbation-density compression.
- Added deliberately ugly reconstruction as a valid experimental method.
- Added independent FV audit of reconstructed outputs.
- Added small/directly accessible experimental material as the preferred exploratory criterion.

### Change log — v0.13

- Replaced the dispute flat-file concept with structured `dispute.json`.
- Defined `dispute.json` as the current packet-level rendering gate.
- Added `none`, `open`, and `resolved` aggregate dispute states, with rendering permitted only for `none` or fully validated `resolved`.
- Defined structured dispute fields including issue, snapshot references, resolution status, resolver, resolution remark, human-action requirement, and AI reprocessing state.
- Added `dispute.reconciled.json` as the preserved resolution record.
- Added mandatory AI reprocessing after human resolution and before rendering.
- Clarified that human resolution resolves the disputed question but does not directly repair the packet; AI incorporates the resolution and validates the resulting packet.
- Added a dispute lifecycle and rendering-gate rules.


## Change log — v0.14

- Added PC as an optional canonical object-database use without changing the existing PC structure.
- Added an additive `snapshots` property for PC object declarations to provide preserved visual grounding.
- Clarified that object-database use, packet merge, and object-database normalisation remain experimental goals requiring continuous same-camera temporal material for validation.

## Change log — v0.15

- Made TD the owner of video observation records; no separate `observation.json`/`observations.json` is required.
- Clarified PC as the existing canonical object-database structure and its role in preventing repeated object instantiation.
- Required packet-scoped PC object IDs in the form `<packet_id>-<object_id>` before packet merge.
- Made `packet_id` a first-class provenance identifier.
- Defined the lowercase `snapshot/` structure: optional `manifest.json` plus `verification/`, `objs/`, and `disputes/`, with no nested folders without explicit permission.
- Added support for highlighted analytical object snapshots while preserving the original source evidence separately.
- Added explicit filesystem discipline requiring operator permission before creating unlisted folders.


### Change log — v0.21

- Clarified that transcript claims may identify potential gaps and trigger adaptive sampling before the claims are visually supported.
- Separated transcription fidelity from cross-modal visual support in cumulative audio/transcript assessment.

### Change log — v0.20

- Defined transcript generation as an early provisional analysis step before the initial temporary TIR/TD temporal investigation.
- Defined the transcript as an adaptive-sampling cue rather than a source-of-truth record.
- Added cumulative transcript/channel assessment so isolated errors do not automatically invalidate otherwise useful audio information.
- Added distinction between transcript errors, unresolved content, and commentary that is temporally or contextually displaced from the current visual scene.
- Clarified that transcript-supported gaps may trigger targeted adaptive sampling and that only source-supported results are promoted into TD.

### Change log — v0.19

- Replaced the previous `dispute-resolved.json` resolution model with the **dispute reconciliation** workflow.
- Defined `dispute.json` as the small current actionable/rendering-gate state when reconciliation is complete.
- Defined `dispute.reconciled.json` as the preserved detailed dispute/reconciliation history after all disputes are resolved.
- Clarified that unresolved disputes keep `dispute.json` in place and only its aggregate status is changed to `open`.
- Defined human intervention as packet enrichment/correction followed by AI reconciliation, with OI and PC updated from the returned packet and supporting evidence.
- Added optional packet-level audio evidence with the source audio file and timestamped `transcript.json`.
- Clarified that transcript text is an interpretation of audio and does not replace the audio source evidence.

### Change log — v0.17

- Added a multi-pass temporal-analysis procedure combining an optional random
  reconnaissance pass, a long-video 4-second global starting interval, and
  evidence-driven adaptive insertion.
- Defined TIR as a rich in-memory temporal-analysis scratchpad that may
  contain observations, object/action changes, relationships, camera changes,
  regions, uncertainty, hypotheses, and intermediate conclusions before final
  TD export.
- Added object change and object action as explicit temporal evidence.
- Added global-versus-local TD distinction to help separate camera/framing
  perturbation from concentrated object-level change.
- Added a provisional local activity baseline for adaptive significance.
- Clarified midpoint insertion and sampling-coordinate uniqueness.
- Added optional minimum-width investigation for specifically hot intervals
  without turning minimum width into a global fixed-rate sampler.
- Clarified that random reconnaissance is independent evidence/triage rather
  than the final temporal representation, and may be locally refreshed when
  initial evidence becomes stale.


### Change log — v0.17

- Renamed the temporal investigation workspace from `TEMP_TD` to **TIR
  (Temporal Investigation Record)**.
- Defined TIR as a persistent investigation record distinct from the official
  `TD.json`.
- Clarified that TIR may retain rich, provisional, contradictory, exploratory,
  and rejected temporal reasoning while TD contains committed,
  evidence-grounded temporal information.
- Clarified that TIR is the source/workspace for deriving the official TD
  record, not a temporary copy of TD.


### Change log — v0.22

- Added Static Change Propensity (SCP) and Current Change Propensity (CCP) as distinct temporal-analysis attention controls.
- Added `change_generator_obj_ids` and evidence-grounded propagation chains.
- Defined Evidence Yield (EY) as a structured temporal evidence record with `current`, `frameid`, and `previous`.
- Added operational incongruity as expectation/observation mismatch that can trigger additional investigation.
- Added explicit external task objectives as a separate source of sampling priority, without allowing the objective to become evidence.
- Clarified the separation between CP/CCP, EY, change-generator relationships, and task objectives.
