# FV Assemble — spatial maplet assembly preservation checkpoint
**Checkpoint date:** 2026-11-07

## Purpose and interpretation

FV Assemble is the computational analogue of human spatial perception through successive, overlapping visual fields. A person samples a larger environment through multiple fields of view, generates local maplets, and combines them into a coherent representation of the larger space.

The experiments here test whether overlapping media inputs can be processed in a single assembly pass to generate maplets and merge them into one coherent image. The work is not defined by any one stitching library or by a single media type.

A typical experiment should preserve:
- original source media and source hashes;
- per-source metadata and capture/time grouping;
- maplets or local-view outputs;
- relative registration/placement transforms and diagnostics;
- the final merged image;
- validation results and limitations.

Do not silently turn an image-space panorama into a claim of georeferencing, orthorectification, or 3D reconstruction. Those are separate capabilities and must be explicitly tested.

## Preservation status

No existing `PACKETS/examples` content was deleted, replaced, or cleaned up during the work recorded here.

At checkpoint:
- `main` head: `cb8c95ce032197d13d519f8eeaa4e59ff013a17f`
- active assembly branch `work/hubble-ngc104-fv` head: `b7175bb56a84edb1157d8005fca905784996988f`
- `PACKETS/examples` tree SHA on both `main` and the assembly branch: `fb74a2fcd53fad41197c46c28461bb30d0464169` (identical)
- dataset-intake branch `work/fv-dataset-receipts-20261107` head: `8a32cec0c666efa104eda08d6103e6872aac7cb4`

Two additional archive refs were created without rewriting either source commit:
- `archive/fv-assemble-preservation-2026-11-07` — based on the assembly branch head above.
- `archive/fv-dataset-intake-preservation-2026-11-07` — based on the dataset-intake branch head above.

These archive refs preserve the Git-tracked code and files at those exact points. They do not, by themselves, extend GitHub Actions artifact retention.

## Completed assembly runs

### NIST MIST 5×5 microscopy
- Run: https://github.com/memoryprismv1/faking-vision/actions/runs/42393259545
- Result: success.
- 25 original 16-bit TIFF tiles assembled as a 5×5 field.
- Output and diagnostic bundle: artifact `13582059642`, `fv-nist-mist-5x5-assembled-maplets`, 91,102,245 bytes.

### Brighton Beach drone
- Run 1: https://github.com/memoryprismv1/faking-vision/actions/runs/42394476469 — failed during DJI EXIF GPS metadata intake because `GPSAltitudeRef` arrived as byte data and was passed to `int()`.
- Run 2: https://github.com/memoryprismv1/faking-vision/actions/runs/42394706988 — successful after handling the byte-encoded altitude reference.
- Six original DJI FC300S views registered with OpenCV Stitcher SCANS into one image-space panorama.
- Reported output: 7316 × 5172 pixels.
- Five adjacent-pair registration diagnostics; minimum inlier count 156.
- The output is an image-space panorama, not an orthophoto, georeferenced map, or 3D reconstruction.
- Artifact: `13582997293`, `fv-brighton-single-pass-assembly`, 90,208,312 bytes.
- Artifact ZIP SHA-256: `9485d539c9b437206da2369d5fa331e2dfc561cf95ed8dbe7e50863a3c4dc721`.

### Hubble NGC 104 source-packet/assembly pilot
- Run: https://github.com/memoryprismv1/faking-vision/actions/runs/42379091711
- Result: success.
- Artifact: `13577075965`, `hubble-ngc104-fv-packets-and-assembled-mosaic`, 159,972,326 bytes.

## Dataset acquisition and intake receipts

### Public dataset intake
- Run: https://github.com/memoryprismv1/faking-vision/actions/runs/42379176332
- Result: successful intake workflow.
- Mygla drone survey: downloaded; 29 images. Acquired, not yet assembled.
- NIST MIST: downloaded; 25 images.
- Brighton Beach: downloaded; 20 images in the source dataset.
- BigStitcher 2D and 3D: download attempts failed because the source host could not be resolved (DNS/name-resolution failure). This is not evidence that the datasets themselves are invalid.
- Artifact: `13576069560`, `fv-assemble-public-dataset-intake`, 255,901,480 bytes.

### Overlap-specific and single-visit source intake
- Run: https://github.com/memoryprismv1/faking-vision/actions/runs/42375613368
- Result: successful intake, receipt verification, and eight source-bundle uploads.
- Full source bundle reported by the workflow: 844,602,030 bytes; SHA-256 `33d31f64ff5bcddc14efc99627e5fcabc3e33616b84c522d4153785b1bf309a8`.
- Receipt ZIP: artifact `13575970606`, `fv-dataset-receipts`, 610,773 bytes.
- Eight source parts were uploaded as separate Actions artifacts (IDs: `13576040458`, `13575308775`, `13575687506`, `13574999474`, `13576055993`, `13575811866`, `13575139235`, `13576020987`).

### Retention warning
The Actions artifacts listed above were created with 30-day retention and were shown as expiring on **2026-12-07**. Downloaded copies have been retrieved into the associated ChatGPT working session for handoff. Actions artifact retention is temporary; do not treat those links as permanent storage.

## Candidate priority rule

Choose candidates by what can actually be acquired and processed independently:
1. a working download route;
2. source files available locally to the workflow;
3. manageable media size and known structure;
4. enough metadata to establish which views overlap or belong to one capture/observation;
5. a feasible registration/assembly route.

Do not promote a dataset because it is scientifically interesting if the source cannot be downloaded and processed. Do not let the incidental success of acquiring a lower-priority candidate rewrite the agreed experiment order.

The prior working order remains:
1. HST single-visit exposures (use the proven MAST download route; group exposures by visit);
2. BigStitcher 2D (resolve a reliable download endpoint; tiny controlled test);
3. NIST MIST (larger controlled grid; already assembled as a reference experiment);
4. Phalaborwa drone survey (inspect real acquisition geometry and licensing before assembly);
5. USGS LiDAR (different media geometry; separate preparation path).

Mygla is an acquired reserve candidate, not an automatic priority change. Brighton is an additional successful drone assembly experiment.

## Non-destructive working rule

- Keep experiments on their work branches until deliberately reviewed.
- Do not merge into `main` without explicit instruction.
- Do not delete, replace, or reorganize existing `PACKETS/examples` contents as part of candidate intake or assembly.
- Preserve originals separately from generated maplets and composites.
- Keep source inventories, receipts, validation reports, and hashes with every experiment.
- Before future cleanup, make and verify an independent backup first.
