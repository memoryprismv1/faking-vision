# FV versioning status

Status date: 2026-11-13

This document resolves how the repository's historical version labels are to be read. It is a navigation and status note, not a replacement for the authoritative [Working Process Specification](../SPECIFICATION/FV_Working_Process_Specification.md).

## Current authority

The current Working Process Specification is authoritative as a whole. Its base text is labelled v0.24 and it contains later normative additions labelled v0.26 and v0.27. The document does **not** assign a consolidated release number.

Until a consolidated release is explicitly assigned, describe the current rebuild target as:

> Current authoritative FV Working Process Specification (v0.24 base with later normative additions v0.26 and v0.27; consolidated release label unassigned).

Do not call the entire current specification simply "v0.27", and do not invent a new consolidated number. The default `fv rebuild` / `fv upgrade` target is the current authoritative specification itself, not the highest-numbered subsection in it.

## Version history and status

| Label | What it represents | Current status |
|---|---|---|
| **v0.24** | Base Working Process Specification and historical packet/spec baseline. | Preserved as the base of the current specification and as a separate historical snapshot. It is not the complete current normative content. |
| **v0.25** | Image-packet editing design addition: object listing, property listing, and direct property-edit target interaction. Early proposals also discussed environment records, edit-base distinctions, and a version-marker file. | Historical design phase, not a standalone normative specification release. Core interaction forms remain in the current command model. The early environment/version-marker proposals were not adopted as general packet requirements. |
| **v0.26** | Normative addition for environmental participation, passive/active object response classification, and related edit-log consistency. | Included in the current Working Process Specification as a labelled normative addition. It builds on the v0.25 design but does not make the earlier proposals a complete v0.25 packet schema. |
| **v0.27** | Normative addition defining packet migration through `fv rebuild` / `fv upgrade`, including preservation of historical provenance and target-version validation. | Included in the current Working Process Specification as a labelled normative addition. The operation is specified; this does not imply that a general migration executable exists. |

## Packet version fields and legacy compatibility

- A packet's `fv_spec_version`, when present, describes the specification version declared for that packet. Preserve it as historical source metadata; do not rewrite it merely because the current specification has later additions.
- If a packet is unversioned, treat its authoring version as unknown. Do not infer a version from its folder, filename, model, or the newest specification subsection.
- Newly generated packets must include the current required provenance record.
- Legacy packets created before the provenance requirement may omit `packet_provenance.json` and remain valid under the legacy compatibility path. Represent missing provenance as unknown / `legacy_missing`; do not fabricate it.
- No general packet-level `fv_version.json` filename or schema is established by the current specification. Do not add one unless a future normative specification defines it.

## Prototype editor labels are not release claims

The Visual Workbench's `0.25 legacy` and `0.26 proposed` selector values, its `v0.26-proposed` badge, and the Media Object Editor's local v0.26 import fallback belong to constrained prototype interchange behaviour. They are not complete FV version implementations, do not migrate packets, and do not establish a consolidated FV release. The Workbench's `fv_version.json` object is part of its local `fv-packet-bundle-v1` wrapper only, not a canonical packet requirement.

## What remains open

A consolidated release label may be assigned when a numbered release is actually needed. That decision should be made deliberately and applied consistently to the specification header, migration target wording, packet-version guidance, examples, schemas, and prototype documentation. Until then, the unassigned status above is intentional—not a missing instruction that an agent may fill in.
