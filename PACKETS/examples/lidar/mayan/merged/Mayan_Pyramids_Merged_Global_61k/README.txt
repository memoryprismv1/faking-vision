# Maya-region LiDAR global-identity merge example

Packet ID: `PKT-MAYAN-MERGE-61K-001`
Operation intended: `fv merge`
Specification label in supplied packet: v0.24

## Intended demonstration

This example is intended to illustrate the distinction between:

- `fv assemble`: register local flight-line/maplet observations into a shared spatial representation; and
- `fv merge`: investigate whether packet-scoped declarations refer to the same underlying entity, then normalize identity only where evidence supports equivalence.

## Source and input status

The legacy README names the PACUNAM LiDAR Initiative and claims 100+ flight-transect packets as merge inputs. Those input packets, raw point clouds, flight identifiers, and reproducible correspondence evidence are not included here. The source reference and survey context do not establish that this example processed those inputs.

## Packet consistency and verification limits

- OI contains a 12-identity sample. MSRM originally listed only three of those IDs; it has been updated to list all 12 sample identities. This is a structural cross-reference correction, not a verification of their existence in the source survey.
- OI declares 61,000 total global structures, but the three typed totals shown (1,200 pyramids, 1,800 causeways, 3,000 plazas) account for only 6,000. The remaining 55,000 are not categorized in this packet. Do not assume a complete inventory.
- The correspondence-quality strings and TIR claim of 100+ source TIRs / 61,000 correspondence investigations are legacy claims. They are now explicitly qualified as unverified because the source flight transects, contributing packets, and correspondence evidence are absent.
- The legacy README also claims specific correspondence thresholds and a large storage-reduction ratio. These are not independently established. The merged-map visualizations do not prove source coverage or correspondence correctness.

Treat this as a conceptual merge example only. `dispute.json` now records two open blockers and sets the merge gate to BLOCKED: the 55,000 untyped remainder and the absent contributing packet/correspondence evidence. Do not cite the 61,000 count, the 100+ input count, the correspondence-quality claims, or the storage-reduction figure as reproduced results.
