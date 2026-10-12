Faking Vision ASSEMBLE Packet v0.24 - Telescope Data Stitching - Hubble Ultra Deep Field
packet_id: PKT-TELESCOPE-HUDF-STITCH-001
operation: fv assemble - stitching overlapping telescope exposures into entire deep field landscape

Source: Hubble Space Telescope Ultra Deep Field (HUDF) - 2003-2004, 11.3 days exposure, 10,000 galaxies
- Overlapping exposures: 800 exposures, each ~20min, dithered 4 positions, overlap 90%
- Total area: 3 square arcminutes (1/10th moon), but deepest visible universe
- Analog to LiDAR: multiple flight transects overlapping -> entire landscape, but photons instead of laser pulses
- Problem: Each exposure partial, must stitch with sub-pixel registration, cosmic ray rejection, distortion correction

FV Assemble:
- Registration: stars as tie points, overlap 90%, distortion from HST ACS/WFC
- Provenance: each photon retains exposure ID
- Assembly vs merge: assembly = how exposures fit together into entire deep field; merge = what galaxies are same across exposures (persistent galaxy IDs)

Generated: 2026-10-12T06:36:11.100763
