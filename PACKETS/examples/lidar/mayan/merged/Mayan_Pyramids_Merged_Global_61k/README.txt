Faking Vision MERGE Packet v0.24 - 61,000 Mayan Structures Persistent IDs
packet_id: PKT-MAYAN-MERGE-61K-001
operation: fv merge - reconcile 100+ flight transect packets into global persistent identities

Source: PACUNAM LiDAR Initiative 2,100km2, 61,000 structures
Inputs: 100+ assemble packets (each flight line 10km x 0.5km)
Each packet-scoped pyramid: PKT-MAYAN-LIDAR-STITCH-001-OBJ-001 etc.
Now merge into global canonical IDs PYR-GLOBAL-001..61000, CAUSEWAY-GLOBAL-001.. etc.

Procedure per v0.24 0. and 5.1.1:
- Assembly answered: how do partial LiDAR strips fit together into 2,100km2 landscape? (fv assemble)
- Merge answers: what established info refers to same underlying entities? (fv merge)
- Correspondence investigation: component = rectangular base + cardinal orientation + causeway connection + height + adjacent plaza
- Quality: high = same base 40x40m +/-2m, same orientation +/-5deg, causeway connects, IoU >0.7; weak = base similar but orientation differs; transient = only one flight line sees it (edge)
- Provenance: each global pyramid retains flight IDs where it was observed

Result: 61,000 global persistent identities normalized, not duplicated. Example: pyramid seen in flight_001, flight_002, flight_003 (overlap 40%) -> single global ID PYR-GLOBAL-001 with 3 packet_scoped_ids

This addresses storage: 2,100km2 at 12pts/m2 = 25.2B points -> petabytes raw. FV merged packet = few MB with 61k semantic entities + relationships - 100000x reduction while preserving auditable evidence

Generated: 2026-10-12T06:36:11.099417
