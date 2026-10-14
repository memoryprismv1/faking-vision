# FV lifecycle deviation: unresolved disputes

## Required lifecycle

The Faking Vision working-process guidance separates investigation, dispute resolution, validation and compilation. An unresolved dispute is not silently repaired by reconstruction; normal compilation requires a resolved and validated packet.

## What happened in this experiment

The user explicitly refused dispute resolution and instructed the assistant to proceed with reconstruction from snapshots and Temporal Declarations (TDs). The assistant followed that instruction for this experiment.

This was a deliberate deviation from the normal process, not a claim that the dispute-resolution requirement had been met.

## Consequences

- Disputes remain unresolved.
- Reconstruction output is a review artefact only.
- Cross-packet identity correspondences remain provisional where evidence is insufficient.
- TIR hypotheses and candidate correspondences are not automatically official TD facts.
- No claim is made that `fv validate` or `fv compile` ran successfully.
- This example must not be used as evidence that FV permits normal compilation with unresolved disputes.

## Why preserve the deviation?

The experiment records what could be reconstructed from available snapshots and TDs when the ordinary resolution gate was intentionally bypassed. Keeping the deviation explicit makes the result inspectable without normalising the bypass into standard procedure.
