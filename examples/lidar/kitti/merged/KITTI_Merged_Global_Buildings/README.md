# KITTI global-building merge example

Packet ID: `PKT-KITTI-MERGE-001`
Operation intended: `fv merge`
Specification label in supplied packet: v0.24

## Intended demonstration

This packet is intended to demonstrate reconciliation of packet-scoped building declarations from two KITTI assembly examples (Sequence 00 and Sequence 07), preserving source packet IDs and recording correspondence evidence before assigning global identities.

## Evidence and consistency audit

- The merged OI explicitly contains 12 entries in `global_buildings_normalized`.
- The same OI declares `total_global_identities: 54`.
- `COMPILED_SPEC.json` also declares 54 identities and describes 12 shared buildings plus 42 singletons, but its scene inventory lists only the 12 shared IDs. The 42 singleton identities are not explicitly represented in the merged OI or scene inventory.
- The packet references two source assembly packets, but the presence of those folders does not establish the claimed cross-sequence correspondence. The source scans, calibration/pose evidence, and reproducible merge log are not included.
- The 12 global records cite component-level provenance such as `building_0` through `building_11` under each source packet's `OBJ-002` building-cluster entity. Neither source OI actually declares those building components (the Sequence 00 cluster has an empty `components` array; Sequence 07 has no component list). The cited component-level source records therefore do not resolve to explicit source OI components.
- The snapshot manifest contains only the packet ID; it does not identify visual evidence files.

These are material internal completeness and evidence gaps. The 54-identity total and the 12 high-confidence correspondences are assertions in the supplied packet, not independently verified results.

## Status

Keep this packet as an **incomplete merge-structure example**. `dispute.json` now records two open blockers and sets the merge gate to BLOCKED. The compiled-spec draft has been constrained to the 12 identities actually listed; the legacy 54 total and 42 singleton identities are retained only as unverified claims, not renderable inventory. Do not present this as a completed or validated global-building merge until the inventory is made internally complete, source evidence is linked, and correspondence decisions can be independently reviewed. Duplicate suffixed files that were byte-identical to canonical files have been removed; the canonical unsuffixed records are retained.


## Provenance update (2026-11-13)

The “54 buildings” and merged-global geometry remain legacy claims. The source sequence mapping can be resolved (sequence 00 → 2011_10_03_drive_0027; sequence 07 → 2011_09_30_drive_0027), but this packet does not retain the exact contributing scan IDs, raw scans, calibration, poses, per-sequence coordinate transforms, registration parameters, convergence/residual logs or output hashes.

The KITTI odometry benchmark and raw-data portal are the authoritative acquisition routes:
- https://www.cvlibs.net/datasets/kitti/eval_odometry.php
- https://www.cvlibs.net/datasets/kitti/raw_data.php

The raw-data portal requires account access; odometry package downloads are email-gated. No claim of a reproducible 54-building merge should be made until the exact source frames and all registration/transform records are recovered. Current disposition: BLOCKED / historical visualization only.
