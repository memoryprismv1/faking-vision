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


## MAST archive provenance update (2026-11-13)

A reproducible MAST metadata query is now provided by TOOLS/query_hubble_udf_mast.py and .github/workflows/hubble-udf-mast-manifest.yml. Query criteria: HST collection, ACS/WFC, proposal IDs 9978 and 10086.

The query returned:
- 609 MAST observation/association records: 573 for proposal 9978 and 36 for proposal 10086.
- 800 unique RAW product URIs, identifying the original exposure files.
- RAW exposure filter totals: F435W 112, F606W 112, F775W 288, F850LP 288.
- 15,740 unique product URIs after deduplication by dataURI (45,187 product rows before deduplication).
- The RAW exposure-to-filter/proposal mapping uses the first six characters of the RAW product filename rootname joined to the first six characters of the MAST observation obs_id. All 800 RAW products mapped to one filter and one proposal without ambiguity.

The retained metadata is in provenance/MAST_2026-11-13/:
- hubble_udf_mast_manifest.json — query criteria, counts, tool versions and limitations.
- hubble_udf_observations.json — 609 observation records.
- hubble_udf_raw_exposures.json — 800 unique RAW exposure identifiers, MAST dataURIs, filter and proposal mapping.
- hubble_udf_products.json — 15,740 unique archive product identifiers and associated observation IDs.

Important boundary: this is an archive-identifier and product-metadata acquisition, not a FITS data download. The product manifest enumerates RAW, FLT, FLC, DRZ, DRC, LOG, TRL and support products. The FITS bytes, per-exposure CRDS context/reference-file contents, and calibration/registration/reprojection logs have not yet been downloaded or inspected. DRZ/DRC product IDs identify archived pipeline outputs; they do not reproduce the original alignment process. End-to-end reconstruction remains blocked pending those inputs and processing records.
