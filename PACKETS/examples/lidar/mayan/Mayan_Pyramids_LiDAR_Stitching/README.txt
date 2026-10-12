Faking Vision ASSEMBLE Packet v0.24 - Mayan Pyramids LiDAR Stitching
packet_id: PKT-MAYAN-LIDAR-STITCH-001
operation: fv assemble - stitching overlapping airborne LiDAR flight transects into entire lost city landscape

Source: PACUNAM LiDAR Initiative (Guatemala) - 2018
- Scanned 2,100 km2 of jungle in Maya Biosphere Reserve, Peten, firing billions of laser pulses
- Revealed 61,000+ structures including pyramids, elevated highways (sacbeob), irrigation systems, defensive fortifications, entire lost cities
- Sensor: Airborne LiDAR 560,000 points/sec, capable of penetrating dense canopy
- Publication: Science 2018, Garrison et al. - Spatiotemporal patterns of Maya urbanism
- Quote: "LiDAR is revolutionizing archaeology the way Hubble revolutionized astronomy" - Francisco Estrada-Belli

Other source: Mirador Basin Project - El Mirador, largest pyramids in world, believed heart of Maya civilization
- LiDAR 560k points/sec mapping pre-Columbian settlement in north Peten

FV Assemble problem:
- Single flight line = partial observation (~10km x 0.5km strip)
- Need to stitch 100+ overlapping strips into entire 2,100km2 landscape
- Must filter vegetation: first returns = canopy, last returns = ground (pyramids)
- Overlap 30-50% between strips for registration
- Provenance: each ground point retains flight ID

This is telescope data stitching analog: like stitching Hubble fields, but LiDAR penetrates jungle instead of space

Generated: 2026-10-12T06:24:39.614914
Spec: v0.24 + Additional Guidance - assembly vs merge, component->candidate->search->verify, TIR, ATD
