# Independent audit notes

## Scope and handling
The supplied ZIP was used as an audit input and was not uploaded. The packet's original text records are retained in this folder. These notes are an additional reviewer-authored file. The five image assets are intentionally excluded from this text-only upload and are to be added separately.

## User instruction and edit set
The edit instruction was “dealers choice”. The four selected treatments—spring blossom morning, summer midday clear, autumn golden evening, and winter frost dawn—are within that requested discretion. The packet records four entities (sky, left-bank trees, right-bank trees, river), unchanged spatial relationships, and passive responses. No boats, figures, or signature were to be added. No Monet signature is appropriate: these are recreations/edits, not works signed by Monet.

## What the supplied reports claim
Meta's packet reports VALID and AUDIT PASS for all four variants. Those are producer-supplied claims, not independent FV validation results.

## Independent structural observations
- OI and MSRM enumerate the same four entity IDs and preserve the stated coarse spatial relationships.
- Each OI_after record marks the four entities passive and retains the same positions.
- ENVIRONMENT_after records only change a short condition label; they do not specify detailed before/after environmental property values.
- OI_after records do not provide property-level appearance deltas for the entities.
- edit_log is summary-level; it does not enumerate changed properties, affected-object arrays, or detailed before/after evidence references.
- packet_provenance identifies Meta / Muse Spark 1.3 and a run timestamp, but its media SHA field is a placeholder (“see source_image.png”), not a digest.
- viewpoint is a single still with unknown camera position/orientation; it is not a calibrated viewpoint.
- dispute.json retains an open identity dispute. The supplied packet itself says title/date are not verified.

## Source image identity and rights context
The source image was independently identified as Claude Monet's *Morning on the Seine near Giverny* (1897), The Metropolitan Museum of Art, object 437125, accession 56.135.4. The Met/Wikimedia Commons image is marked CC0 1.0 / Open Access. The local source_image.png is a resized/cropped derivative; its hash is recorded below, but it has not been hash-matched to the full-size museum master. This external identification contextualises the source; it does not rewrite Meta's original dispute.json record. Do not describe the edited images as works by Monet or add a Monet signature.

References:
- Met collection record: https://www.metmuseum.org/art/collection/search/437125
- Wikimedia Commons file record: https://commons.wikimedia.org/wiki/File:Morning_on_the_Seine_near_Giverny_MET_DT1903.jpg

## SHA-256 of supplied image files
- source_image.png: 5318964f1ea4ca6cf4d6317e863345790912511bf5c67e9051c400d2ba4a3538
- edited_image_spring_blossom_morning.webp: 883a13dd897f45f81061d4153fa6dc7098f58ff64e071c327a627bbd62152d93
- edited_image_summer_midday_clear.webp: ced5fb01391934607794efecfac3c6a831f00f87bbe95723d5ab63e87b127bc4
- edited_image_autumn_golden_evening.webp: f45d672dc4acdfa5c0b0c27a8ab20cc233744ca0d79b2fac3e4d53ae3bdcef4e
- edited_image_winter_frost_dawn.webp: 7c3ec1f4c16a634af6fe41637cb2345305163e52d55d13c92622e5bac973d0b1

## Overall assessment
Suitable as an illustrative environmental-edit example with transparent provenance and validation caveats. Not established as compilation-ready or fully validated under the cited FV requirements. The supplied PASS labels remain attributed to the packet producer.
