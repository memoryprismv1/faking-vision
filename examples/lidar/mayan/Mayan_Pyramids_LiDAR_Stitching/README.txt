# Maya-region airborne LiDAR stitching example

Packet ID: `PKT-MAYAN-LIDAR-STITCH-001`
Operation intended: `fv assemble`
Specification label in supplied packet: v0.24 plus additional guidance

## Source context

The legacy packet names the PACUNAM LiDAR Initiative in Guatemala and cites Garrison et al., *Science* (2018), “Spatiotemporal patterns of Maya urbanism”. These are source-context references; the exact flight transects used to create this packet are not identified by acquisition IDs or supplied with the repository.

## Intended demonstration

The example is intended to illustrate assembly of overlapping airborne LiDAR flight transects into a larger spatial representation. Each local observation should retain its flight-line provenance. Assembly should not silently normalize object identity across observations; that is a separate `fv merge` decision.

## What is present and what is missing

The repository contains structured packet records, a snapshot manifest, and a separate merged-packet example. The visualizations directory currently contains only its README; the previously listed workflow image is absent from the repository tree. It does not contain the raw LiDAR point clouds, flight-line list, calibration/registration inputs, or a reproducible processing log for this assembly.

## Verification limits

The legacy README repeats figures such as 2,100 km², 61,000 structures, 100+ overlapping strips, and 30–50% overlap. These figures describe the cited research context or the supplied README; they do not demonstrate that this packet acquired or processed those inputs. The workflow image is illustrative, not a rendered survey result.

An additional packet-level correction: the legacy OI had placed a west-facing staircase in the observed component list while describing it as an “expected component”. That entry has now been removed from the observed components and retained only in the expected-component candidature record, with an explicit uncertainty note. It is not an observed staircase. The OI's candidate/search narrative and the specific dimensions/orientations also remain unverified.

`dispute.json` now records two open blockers and sets the assembly gate to BLOCKED_FOR_REPRODUCTION. The former `VALID` report has been corrected to `BLOCKED_UNVERIFIED`; the source-dependent pyramid/causeway classifications and the flight-line assembly are not independently verified. Treat this as an assembly-contract illustration, not a verified reproduction of the PACUNAM survey or a completed 2,100 km² assembly.


## Public-source provenance review (2026-11-13)

The 2016 PACUNAM LiDAR survey is described in the published study as covering approximately 2,144 km² and supporting an estimate of 61,480 ancient structures. These are study-level claims, not a measurement of the local packet's point count or a reconstruction result.

A public derivative-data release was located:
- Dryad DOI: https://doi.org/10.5061/dryad.k51j708
- Dataset page: https://datadryad.org/dataset/doi:10.5061/dryad.k51j708
- 14 files, approximately 25.04 MB, published 2019-09-28.
- The release consists of derivative GIS/vector/raster products, including survey-block polygons, ground-replication coverage and mapped structure layers.

The Dryad release does not provide the original airborne LAS/LAZ point clouds or exact flight-line/transect identifiers. The survey-block polygon layer is not a flight-line index. The MARI-GISLAB ArcGIS services are also derivative feature layers, not a substitute for the raw point-cloud strips.

Required to reproduce this packet:
- exact flight-line/strip IDs and acquisition dates/times;
- original LAS/LAZ tiles and tile index;
- trajectory and GPS/IMU data;
- sensor configuration and boresight/lever-arm calibration;
- coordinate reference system and vertical datum;
- classification and strip-adjustment reports;
- ground-control/check-point records;
- software versions, processing parameters and strip-registration logs;
- the exact source tiles and transforms used for the merged output.

The public Dryad release and this repository do not contain those inputs. No matching public raw point-cloud release was identified in the checked OpenTopography catalogue. The remaining access route is a data request to PACUNAM/MARI-GISLAB/NCALM; no request has been sent. Reproduction remains BLOCKED.
