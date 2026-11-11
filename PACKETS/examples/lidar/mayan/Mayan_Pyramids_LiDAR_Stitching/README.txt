# Maya-region airborne LiDAR stitching example

Packet ID: `PKT-MAYAN-LIDAR-STITCH-001`
Operation intended: `fv assemble`
Specification label in supplied packet: v0.24 plus additional guidance

## Source context

The legacy packet names the PACUNAM LiDAR Initiative in Guatemala and cites Garrison et al., *Science* (2018), “Spatiotemporal patterns of Maya urbanism”. These are source-context references; the exact flight transects used to create this packet are not identified by acquisition IDs or supplied with the repository.

## Intended demonstration

The example is intended to illustrate assembly of overlapping airborne LiDAR flight transects into a larger spatial representation. Each local observation should retain its flight-line provenance. Assembly should not silently normalize object identity across observations; that is a separate `fv merge` decision.

## What is present and what is missing

The repository contains structured packet records, a snapshot manifest, a workflow visualization, and a separate merged-packet example. It does not contain the raw LiDAR point clouds, flight-line list, calibration/registration inputs, or a reproducible processing log for this assembly.

## Verification limits

The legacy README repeats figures such as 2,100 km², 61,000 structures, 100+ overlapping strips, and 30–50% overlap. These figures describe the cited research context or the supplied README; they do not demonstrate that this packet acquired or processed those inputs. The workflow image is illustrative, not a rendered survey result.

An additional packet-level caution: OI records a west-facing staircase as a pyramid component while describing it as an “expected component”. Without the raw transect data or retained source evidence, this cannot be treated as an observed component. The OI's candidate/search narrative and the specific dimensions/orientations also remain unverified.

Treat this as an assembly-contract illustration, not a verified reproduction of the PACUNAM survey or a completed 2,100 km² assembly.
