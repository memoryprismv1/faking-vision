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

The packet also has an internal inventory/spatial mismatch: OI declares two entities (a galaxy and a 10,000-galaxy cluster), but the MSRM scene's `entities_present` list contains only the first entity. The MSRM's `total_galaxies` value does not replace the missing entity reference. This must be reconciled against source evidence before the packet is used as a coherent example.

Treat this as an assembly-contract illustration, not a reproduced HUDF reduction or validated astronomical catalogue.
