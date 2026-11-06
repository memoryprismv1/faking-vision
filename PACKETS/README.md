# FV Packets

An FV packet is a portable structured representation used as the reconstruction source of truth.

Examples are organized by reconstruction target:

- `examples/images/` — image reconstruction packets
- `examples/videos/` — video reconstruction packets
- `examples/environmental_edit_pairs/` — original/edited packet metadata for environmental changes and object behaviour, including a deliberately failing negative example

The environmental edit-pair contribution originated with Meta and was integrated and corrected by ChatGPT under [issue #2](https://github.com/memoryprismv1/faking-vision/issues/2). Its current branch version is metadata-only: source image URLs and licence/permission evidence were not provided, so image binaries are withheld pending provenance review. See the folder's README, asset manifest, and verification report before using the examples.

Some example packets may be supplied without original source media. Always check each example's provenance and validation status before treating it as suitable for reconstruction or publication.

For creating a packet from an image or video, use the Working Process Specification in `../SPECIFICATION/`.


## Packet provenance

Newly generated packets include a root-level `packet_provenance.json` identifying the packet-generating agent and, where known, the media-generating system. Its media record may also contain three independent optional add-ons: an `attribution` object for the original source/creator, an `organizations` array, and a `contributions` array recording people's roles in relation to the current media. Any or all of these add-ons may be omitted; their absence does not affect packet validity. The attribution object's internal properties are intentionally not yet standardized. The format is defined by `../SPECIFICATION/FV_Packet_Provenance_Schema.json`. Existing packets without this file remain valid; do not retrofit missing provenance or contribution data by guessing.

## Audit reports

Independent audits produce a downloadable `FV_AUDIT_REPORT.json` when file creation is available. Its schema is `../SPECIFICATION/FV_Audit_Report_Schema.json`. Batch aggregation of audit files is documented as a future TODO, not an implemented command.
