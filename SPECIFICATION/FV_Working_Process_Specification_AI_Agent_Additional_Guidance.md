# Faking Vision

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
