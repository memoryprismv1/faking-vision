# Minority Report: Anticipatory Behaviour (Experimental)

**Status:** Exploratory research note  
**Scope:** Experimental capability definition only. No implementation or target application is committed to.

## Purpose

Explore whether Faking Vision (FV), informed by Making Vision (MV), can anticipate plausible next events from visual evidence.

The experiment may accept:
- a single image, for predictions from a static scene;
- a short video segment, to use temporal evidence and estimate what may happen over the next few seconds;
- an FV scene reconstruction, where available.

The goal is not to predict one certain future. It is to produce a set of plausible next behaviours and conditional event chains, preserve uncertainty, and compare predictions with what subsequently occurs.

## Core idea

Reason about objects, their current states, behaviour, relationships, and environmental constraints. Predict not only what an individual object may do next, but how one object's action may affect another.

Example structure:

`Object A performs action a`
→ `Object B may respond with b, c, or d`
→ `each response creates further possible states or interactions`

This is a branching, conditional chain, not a single deterministic storyline. New observations should update the branches. The system must be able to represent outcomes that were not anticipated by its current model.

## Proposed input and output

### Inputs
- Source type: image, video segment, or FV reconstruction.
- The observed scene and its objects, states, relationships, and temporal evidence where available.
- A prediction horizon, initially a few seconds for video experiments where the footage supports it.

### Outputs
For each prediction:
- the object(s) involved;
- the current observed state and evidence;
- a possible next action, state change, or interaction;
- conditional follow-on events and their dependencies;
- an estimate of likelihood or confidence, clearly distinguished from measured/calibrated probability;
- an explicit unknown/unmodelled-outcome category;
- assumptions and evidence that would change the prediction.

Separate observed facts from inferred behaviour and predicted futures. Do not present a prediction as an observation or certainty.

## Unknown outcomes and anomaly

The design must not force all possible futures into known behaviour categories. Preserve explicit space for outcomes the current model cannot adequately describe.

A 5% unknown reserve is an initial engineering hypothesis inspired by a prior software-architecture practice: leave room for unanticipated events. It is **not** a claim that real-world unknown behaviour occurs exactly 5% of the time, nor is it a statistically validated probability. Test whether the reserve should be fixed, adaptive, or represented separately from calibrated likelihoods.

An anomaly occurs when observed behaviour crosses the current behavioural baseline into something the model does not adequately explain. Unknown outcomes and anomalies are related but distinct: an unmodelled event is not necessarily objectively abnormal, and an unusual event may still be predictable.

## Relationship to FV, MV, and AEL

- **FV** provides an auditable account of the visible scene, objects, relationships, and temporal evidence.
- **MV** contributes to understanding objects, states, expected behaviour, and relevant deviations.
- **Minority Report** is the experimental anticipatory layer: it generates plausible next events and conditional behavioural chains.
- **AEL (Anticipated Enforcement Logic)** is a concept to investigate in this context. Initially, record how anticipated consequences could influence attention, investigation, tracking, or preparation. Do not assume autonomous action or commit to a specific integration before experiments provide evidence.

These are working distinctions for exploration, not a finalized architecture. A single image may support scene-based possibilities but generally cannot establish trajectory or intent; video provides temporal evidence and should be evaluated separately.

## Experimental method

1. Select an image or video segment and record the evidence available at prediction time.
2. Produce and preserve the prediction set before examining the future frames.
3. For video, specify the forecast horizon and generate branching conditional possibilities.
4. Inspect the subsequent footage and record what occurred, what was missed, and which assumptions failed.
5. Track unsupported additions, missed objects/interactions, unexpected outcomes, and overconfident predictions.
6. Repeat across varied scenes before choosing algorithms, metrics, or applications.

Keep predictions auditable and avoid retrospective rewriting. Where numerical probabilities are used, distinguish illustrative estimates from calibrated values and assess calibration only when enough outcomes have been collected.

## Open questions

- What is the right prediction unit: action, state transition, interaction, or event?
- How should the unknown category be represented and estimated?
- How should object identity and behavioural history affect predictions?
- How far ahead can useful predictions be made from images versus video?
- How should competing branches and their conditional dependencies be recorded?
- Where and how should AEL influence attention or investigation?
- Which evaluation measures are meaningful once a sufficient experimental corpus exists?

## Non-goals for this stage

- No claim of reliable real-world forecasting.
- No fixed application or autonomous response behaviour.
- No commitment to a particular model, algorithm, or probability-calibration method.
- No assumption that anomalous behaviour implies malicious intent.

**Current outcome sought:** a disciplined experimental record of what FV/MV can anticipate, how it represents uncertainty and unknown outcomes, and how its predictions compare with what actually happens.
