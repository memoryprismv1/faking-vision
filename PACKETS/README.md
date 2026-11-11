# FV Packets

An FV packet is a portable structured representation used as the reconstruction source of truth.

Examples are organized by reconstruction target or source family:

- `examples/images/` — image reconstruction packets
- `examples/videos/` — video reconstruction packets
- `examples/cctv/` — CCTV packet families
- `examples/lidar/` — LiDAR assembly and merge examples
- `examples/telescope/` — telescope-exposure assembly examples
- `examples/environmental_edit_pairs/` — original/edited packet metadata for environmental changes and object behaviour, including a deliberately failing negative example

## Before using an example

See the [examples index and evidence-status audit](examples/README.md) for a directory-by-directory guide to what each example demonstrates and what evidence is actually present.

Examples have different evidence and verification levels. A folder's presence does not prove that source media were acquired, the described processing was executed, or the result was independently verified. Read the example README, provenance notes, manifests, disputes, and validation records before treating it as a reconstruction-ready packet.

The environmental edit-pair contribution originated with Meta and was integrated and corrected by ChatGPT under [issue #2](https://github.com/memoryprismv1/faking-vision/issues/2). Its current branch version is metadata-only: source image URLs and licence/permission evidence were not provided, so image binaries are withheld pending provenance review. See the folder's README, asset manifest, and verification report before using the examples.

## Packet provenance

Newly generated packets include a root-level `packet_provenance.json` identifying the packet-generating agent and, where known, the media-generating system. Its media record may also contain three independent optional add-ons: an `attribution` object for the original source/creator, an `organizations` array, and a `contributions` array recording people's roles in relation to the current media. Any or all of these add-ons may be omitted; their absence does not affect packet validity. The attribution object's internal properties are intentionally not yet standardized. The format is defined by `../SPECIFICATION/FV_Packet_Provenance_Schema.json`. Existing packets without this file remain valid; do not retrofit missing provenance or contribution data by guessing.

## Audit reports

Independent audits produce a downloadable `FV_AUDIT_REPORT.json` when file creation is available. Its schema is `../SPECIFICATION/FV_Audit_Report_Schema.json`. The repository also contains an offline batch utility that validates and aggregates existing audit reports; it does not re-audit media and is not a native `fv audit batch` skill command.
