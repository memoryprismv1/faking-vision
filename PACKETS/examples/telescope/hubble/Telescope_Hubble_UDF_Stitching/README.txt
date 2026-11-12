# Hubble Ultra Deep Field exposure-stitching example

Packet ID: `PKT-TELESCOPE-HUDF-STITCH-001`
Operation intended: `fv assemble`
Specification label in supplied packet: v0.24

## Source context

The legacy packet identifies the Hubble Space Telescope Ultra Deep Field (HUDF), 2003–2004. The repository does not include the original exposures, archive identifiers, a complete exposure list, calibration/distortion data, or a reproducible registration log.

## Intended demonstration

This example is intended to illustrate assembly of overlapping telescope exposures into a larger field while preserving exposure-level provenance. Assembly answers how local observations fit together; a later merge would investigate whether detections across exposures correspond to the same persistent astronomical object.

## Verification limits

The legacy README claims 800 exposures, approximately 20-minute exposures, four dither positions, 90% overlap, 11.3 days of exposure, and approximately 10,000 galaxies. These are not independently verified by the packet files. The supplied workflow poster is illustrative and is not the assembled HUDF image or evidence that the stated registration/cosmic-ray/distortion processing was executed.

A cross-reference check found that OI declares two entities (a galaxy and a 10,000-galaxy cluster), while the MSRM scene originally listed only the galaxy. The cluster ID has now been added to `entities_present`, matching the OI and the scene's `total_galaxies` field. This is a structural correction only; the source exposures and claimed galaxy count remain unavailable for independent verification.

Treat this as an assembly-contract illustration, not a reproduced HUDF reduction or validated astronomical catalogue. `dispute.json` now records two open blockers and sets the merge/acceptance gate to BLOCKED: the exposure assembly cannot be reproduced from retained inputs, and the astronomical inventory/count claims lack source catalogue evidence.
