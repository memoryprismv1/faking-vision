# Legacy dataset provenance and reproducibility status

This register separates a dataset's public research context from the exact source files and processing evidence needed to reproduce an FV example. A published paper, catalog, derived map, or rendered visualization is not a substitute for the actual inputs used by a packet.

## 1. Fullerton Transportation Center CCTV

**Status: source acquired and source-alignment evidence generated; historic packet correspondence remains under review.**

- Exact source: Wikimedia Commons distribution copy of *Full, unedited Kelly Thomas confrontation video (35 min.).webm*.
- Commons source page: https://commons.wikimedia.org/wiki/File:Full,_unedited_Kelly_Thomas_confrontation_video_(35_min.).webm
- The source acquisition workflow records the Commons metadata, retrieval URL, response headers, SHA-256, FFprobe stream metadata, and a source-frame manifest.
- The three legacy part intervals are arithmetically contiguous (683 + 683 + 684 seconds = 2,050 seconds). Boundary-adjacent frames allow direct comparison; interval arithmetic alone does not prove the original packet parts were cut on those exact frames.
- The Commons upload is a YouTube-derived distribution copy, not the camera's native recorder file. Commons' displayed public-domain rationale is recorded as a source assertion, not an independent legal opinion.
- Do not confuse this Fullerton recording with the separate Supercircuits BLK-HDPTZ12 parking-lot CCTV experiment.

The source acquisition and frame-alignment record is in examples/videos/fullerton_transit_center_cctv/provenance/. Cross-view person identity correspondence is not established merely by temporal alignment; keep it blocked unless source evidence supports it.

## 2. KITTI Odometry — Sequence 00 and Sequence 07

**Status: authoritative dataset inputs are precisely identified; the repository still lacks the exact scans, calibration/poses and registration run used to make the legacy visualizations.**

Official benchmark: https://www.cvlibs.net/datasets/kitti/eval_odometry.php

The official Odometry benchmark provides 22 sequences: 00–10 with ground-truth trajectories for training and 11–21 for evaluation. Its separate download groups include Velodyne data, calibration files, poses, and the development kit. The official page lists the Velodyne archive at 80 GB, calibration at 1 MB, and poses at 4 MB.

For the two packets in this repository, the correct benchmark-level input layout is:

- Sequence 00: dataset/sequences/00/velodyne/*.bin, dataset/sequences/00/calib.txt, dataset/sequences/00/times.txt, and dataset/poses/00.txt.
- Sequence 07: dataset/sequences/07/velodyne/*.bin, dataset/sequences/07/calib.txt, dataset/sequences/07/times.txt, and dataset/poses/07.txt.

Expected official scan counts are 4,541 for sequence 00 and 1,101 for sequence 07. These are benchmark sequence counts, not proof that the legacy packet used every scan. In particular, the Sequence 00 packet's legacy 400 scans assembled statement is an unspecified subset until exact selected frame IDs are recorded.

The separate KITTI Raw Data release contains synchronized/unsynchronized camera streams, Velodyne point clouds, GPS/IMU records, and calibration. The odometry devkit mapping confirms sequence 00 → raw drive 2011_10_03_drive_0027 and sequence 07 → raw drive 2011_09_30_drive_0027. These mappings do not supply the raw-drive files. Preserve the raw-drive calibration/OXTS files and do not silently substitute odometry poses. The raw-data portal requires account access; odometry archives are email-gated.

TOOLS/verify_kitti_odometry_inputs.py validates a locally extracted Odometry dataset: scan counts, point-file byte shape, calibration, timestamps, pose-line counts and SHA-256 fingerprints. It does not perform registration or validate the legacy map.

Still required for reproduction:
1. Exact downloaded archive names, acquisition date, and archive SHA-256 values.
2. Exact frame subset used by each packet, with source file hashes.
3. Calibration and pose file hashes.
4. Registration parameters and logs (including ICP configuration, coordinate frames, motion compensation and filtering).
5. A source-backed point/coverage summary and independent comparison against the committed visualization.

The KITTI global-building merge packet also remains blocked: its declared 54 identities are not all enumerated, and its 12 correspondence claims cite source components not present in the source OIs.

## 3. PACUNAM / Maya-region airborne LiDAR

**Status: public research context identified; raw source data are not generally public, and the exact flight transects for the legacy packet are not identified.**

Research context:
- Canuto et al. (2018), *Ancient Lowland Maya Complexity as Revealed by Airborne Laser Scanning of Northern Guatemala*, Science 361(6409), DOI 10.1126/science.aau0137.
- The 2016 survey covered approximately 2,144 km² of northern Guatemala.
- A related public derivative dataset is available through Dryad: https://doi.org/10.5061/dryad.k51j708. It includes derived archaeological feature layers and summaries, not the complete original raw point-cloud acquisition needed to reproduce the FV packet's flight-line stitching.

Published data-availability statements for PACUNAM LiDAR indicate that raw data are held by relevant institutions and interested researchers should contact them. Archaeological-site protection is a stated reason raw lidar data are not publicly downloadable. The relevant custodian for PACUNAM Guatemala data is Fundación PACUNAM; access may also involve the Instituto de Antropología e Historia de Guatemala (IDAEH) and project-specific agreements.

Do not treat Dryad feature layers, a public map service, the published survey area, or packet illustrative images as the raw flight transects.

Required access request and eventual acquisition record:
1. Exact project/site and flight-line/transect IDs contributing to this packet.
2. Original LAS/LAZ or equivalent point-cloud tiles and file-level checksums.
3. Acquisition date, sensor/platform, point density, return information, coordinate reference system and vertical datum.
4. GNSS/IMU trajectory and boresight/calibration records where applicable.
5. Strip-adjustment, ground-classification, tiling and registration software/parameters/logs.
6. Custodian, permission/MOU, permitted use, redistribution restrictions and archaeological sensitivity constraints.

Until those are supplied, keep both Mayan assembly and 61k merge examples blocked for reproduction. Do not claim that 100+ flight strips or 61,000 structures were independently processed by this repository.

## 4. Hubble Ultra Deep Field — ACS/WFC

**Status: MAST observation and product metadata enumerated; 800 unique RAW exposure product identifiers identified; FITS bytes and calibration/registration reproduction remain outstanding.**

The MAST query used collection HST, proposals 9978 and 10086, instrument ACS/WFC.

The 13 November 2026 MAST query returned:
- 609 observation records.
- 45,187 product rows before deduplication.
- 15,740 unique product dataURI values.
- 800 unique products with subgroup RAW.
- The 800 RAW product filenames and MAST URIs are committed in examples/telescope/hubble/Telescope_Hubble_UDF_Stitching/provenance/MAST_2026-11-13/hubble_udf_raw_exposures.json. The 15,740 unique product URIs are in hubble_udf_products.json; observations and query counts are in hubble_udf_observations.json and hubble_udf_mast_manifest.json.
- RAW filter mapping: F435W 112, F606W 112, F775W 288, F850LP 288. All 800 RAW products were mapped to one filter and proposal by joining the first six characters of the RAW product rootname to the first six characters of the MAST observation obs_id.
- Successful reproducible query run: https://github.com/memoryprismv1/faking-vision/actions/runs/43407889542.

This is a metadata result, not an exposure download. No FITS exposure bytes were downloaded. The RAW product list identifies archive products but does not establish the exact 800 files used in any historical stitching operation.

NASA's UDF catalog describes the 400-orbit ACS/WFC program across proposals 9978 and 10086, with 112 exposures each in F435W and F606W and 288 each in F775W and F850LP, totaling 800 science exposures. The MAST query independently enumerates 800 unique RAW products for the selected collection/proposals/instrument.

Reproduction still requires:
1. Download the exact 800 RAW FITS products (or exact selected subset) and record file hashes.
2. Retrieve and record the relevant calibration reference files and CRDS context.
3. Identify the exact calibration pipeline version and parameters.
4. Record selected exposure list, dither/association membership, registration transforms, distortion corrections, cosmic-ray rejection and drizzle/reprojection parameters.
5. Compare the resulting mosaic and catalog against the legacy output.

TOOLS/query_hubble_udf_mast.py regenerates the observation/product/raw-exposure metadata manifest and the per-RAW filter/proposal mapping. It intentionally does not download FITS bytes or claim to reproduce the mosaic. The metadata manifests are committed; the source FITS bytes, CRDS context/reference files and registration/reprojection logs remain outstanding.

## 6. Cross-dataset evidence rule

For all legacy examples, distinguish:
- Source existence: an authoritative archive or custodian has the data.
- Acquisition: this project actually obtained the exact files and recorded hashes.
- Processing: the transforms, filters, registrations and logs are retained.
- Reproduction: a clean rerun from retained inputs yields the claimed output.
- Validation: an independent comparison supports the output and its claims.

A successful metadata query or passing structural test only establishes the level it actually tests. It does not promote the next level.


## 5. Other legacy examples: source and processing records

The structured inventory is maintained in docs/provenance/legacy_source_registry.json. It covers the five image packets and the remaining video examples in addition to Fullerton, CCTV Snapshot, KITTI, Mayan and Hubble.

| Example family | Source status | Processing/reproducibility status |
|---|---|---|
| Five image packets | Source image assets are present; source page/licence references are in each packet README | OI/TIR/MSRM records exist, but original acquisition timestamps, pre-import source hashes and image edit history are missing |
| A Trip to the Moon | Public-domain film reference is recorded; source film and frames are not included | Authored reconstruction-target brief only; not a source-film inventory |
| Alice in Wonderland | Project Gutenberg text reference is recorded; no source video is asserted | Text edition, excerpt offsets/checksum and generation steps are not locked |
| Cat jumping backwards | Commons source URL is recorded; source video is not retained | No source hash, frame manifest or processing log |
| Old Macdonald | Generated MP4 output is present | Source audio, audio rights, prompt, renderer/model version and generation parameters are missing |
| CCTV Snapshot / BLK-HDPTZ12 | Commons distribution copy acquired and hashed; media/frames are not retained | Source storyboard and frame hashes provide partial alignment; Commons licence rationale is flagged for review |
| Fullerton | Commons distribution copy acquired and hashed; camera-native source absent | Source alignment report retained; cross-part identity correspondence remains blocked |

### Repository asset hashes

TOOLS/build_example_asset_manifest.py produces docs/provenance/example_asset_hashes.json for the current binary assets under examples/. These are hashes of the bytes currently checked into this repository. They do not retroactively establish original source hashes, acquisition dates, licences or processing history.

### Evidence boundary

A source URL is not an acquisition record. A repository hash is not an original-source hash. A MAST product identifier is not a downloaded FITS file. A derived GIS layer is not a raw LiDAR point cloud. A rendered MP4 is not a reproducible generation pipeline. Each record therefore keeps source availability, processing evidence, licence/privacy review and reproduction status separate.
