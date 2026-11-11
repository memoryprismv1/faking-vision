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

## Verification limits

The legacy README claims 61,000 persistent global identities, specific correspondence-quality thresholds, and a large storage-reduction ratio. These are unverified packet/README assertions. The presence of an OI file and a merged-map visualization does not independently establish the claimed identity count, correspondence quality, source coverage, or storage equivalence.

Treat this as a conceptual merge example only. Do not cite the 61,000 count, the 100+ input count, or the storage-reduction figure as a reproduced result.
