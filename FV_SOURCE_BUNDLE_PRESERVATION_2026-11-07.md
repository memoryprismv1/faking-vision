# FV source bundle preservation — 2026-11-07

This file records the source-bundle artifacts created by the successful overlap/single-visit intake workflow. The artifacts have been downloaded into the working session as ZIP files; keep all eight parts together.

- Workflow run: https://github.com/memoryprismv1/faking-vision/actions/runs/42375613368
- Source bundle total reported by workflow: 844,602,030 bytes
- Full bundle SHA-256 reported by workflow: `33d31f64ff5bcddc14efc99627e5fcabc3e33616b84c522d4153785b1bf309a8`
- Receipt artifact: `fv-dataset-receipts`, ID `13575970606`, 610,773 bytes
- Git source branch snapshot: `work/fv-dataset-receipts-20261107` at `8a32cec0c666efa104eda08d6103e6872aac7cb4`
- Archive branch: `archive/fv-dataset-intake-preservation-2026-11-07`

## Source bundle parts

| Part | Actions artifact ID | ZIP name |
|---|---:|---|
| 00 | 13576040458 | fv-source-bundle-part-00.zip |
| 01 | 13575308775 | fv-source-bundle-part-01.zip |
| 02 | 13575687506 | fv-source-bundle-part-02.zip |
| 03 | 13574999474 | fv-source-bundle-part-03.zip |
| 04 | 13576055993 | fv-source-bundle-part-04.zip |
| 05 | 13575811866 | fv-source-bundle-part-05.zip |
| 06 | 13575139235 | fv-source-bundle-part-06.zip |
| 07 | 13576020987 | fv-source-bundle-part-07.zip |

## Handling

- Retain all eight parts; do not extract only selected chunks and discard the originals.
- Reconstruct/verify only according to the intake packaging manifest and checksums inside the receipt bundle.
- Actions artifacts were configured for 30-day retention and were shown with 2026-12-07 expiry. The downloaded ZIP copies are the recovery copies.
- This manifest records provenance; it is not itself a substitute for the binary ZIP parts.
