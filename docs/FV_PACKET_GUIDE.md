# FV Packets

An FV packet is a portable structured representation used as the reconstruction source of truth.

## Example corpus

Examples are maintained in the repository-level [examples directory](../examples/), separately from packet tooling and packet-format documentation.

- [Image examples](../examples/images/)
- [Video examples](../examples/videos/)
- [LiDAR examples](../examples/lidar/)
- [Telescope examples](../examples/telescope/)

The [examples index](../examples/README.md) distinguishes what each example demonstrates from the evidence actually retained. A folder's presence does not prove that source media were acquired, processing was executed, or results were independently verified. Read each packet README, provenance note, manifest, dispute and validation record before using an example.

## Packet provenance

Newly generated packets include a root-level `packet_provenance.json` identifying the packet-generating agent and, where known, the media-generating system. Its media record may also contain three independent optional add-ons: an `attribution` object for the original source/creator, an `organizations` array, and a `contributions` array recording people's roles in relation to the current media. Any or all of these add-ons may be omitted; their absence does not affect packet validity. The attribution object's internal properties are intentionally not yet standardized. The format is defined by `../SPECIFICATION/FV_Packet_Provenance_Schema.json`. Existing packets without this file remain valid; do not retrofit missing provenance or contribution data by guessing.

## Audit reports

Independent audits produce a downloadable `FV_AUDIT_REPORT.json` when file creation is available. Its schema is `../SPECIFICATION/FV_Audit_Report_Schema.json`. The repository also contains an offline batch utility that validates and aggregates existing audit reports; it does not re-audit media and is not a native `fv audit batch` skill command.
