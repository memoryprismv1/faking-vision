# Source and provenance

## Parent source

- Commons file: https://commons.wikimedia.org/wiki/File:BLK-HDPTZ12_Security_Camera_Parkng_Lot_Surveillance_Video.webm
- Commons page revision: 1269449350 (2026-08-29T20:59:41Z).
- Original date in Commons metadata: 2012-10-23.
- Original author/source: Supercircuits; YouTube source ID U7HRKjlXK-Y.
- Commons upload/import: 2026-08-29.
- Commons SHA-1: d1115753bffc8967898779dfedfa5fe609bdb530.
- Acquired file SHA-256: ff14641c693dbd1e78b1d22042876b5d3a4068c3301be8d07e504dd592debfaa.
- File size: 67,736,771 bytes.
- Measured duration: 316.708 seconds.
- Video: 1920 × 1080, 30 fps, VP9. Audio: Opus, 48 kHz, stereo.

The Commons description says the clip demonstrates a 2.1-megapixel imager and 12× optical zoom, and describes a plate-like test marking on a telegraph pole at 360 feet with digital zoom layered on optical zoom. This is a camera product demonstration, not a real incident or an independently authenticated surveillance event.

## Acquisition and processing record

The reproducible acquisition tool is TOOLS/acquire_cctv_snapshot_source.py. Workflow: .github/workflows/cctv-snapshot-source-acquisition.yml.

- Successful workflow run: https://github.com/memoryprismv1/faking-vision/actions/runs/43409586287
- Source acquisition record: provenance/source_acquisition.json.
- Source frame hash manifest: provenance/source_frame_manifest.json.
- The source media was downloaded, SHA-256 hashed, probed with ffprobe, and deleted after processing.
- 80 global frames were sampled at 4-second intervals.
- 6 samples were extracted around the two declared packet boundaries.
- 240 transition samples were hashed at 10 fps across windows 154–162s, 204–212s and 236–244s.
- The workflow artifact contains JSON manifests only (30-day retention). No source video or sample image is retained in the repository or artifact.

## Source-to-packet alignment

The three nominal packet intervals are equal thirds of the 316.708-second parent:
- Part 1: 0–105.569333s (inferred; its original manifest does not record the parent interval).
- Part 2: 105.569333–211.138667s (recorded in the packet manifest).
- Part 3: 211.138667–316.708s (recorded in the packet manifest).

The prior source screenshot storyboard was inspected as a separate review artifact; it is not stored in this repository. Its sampled source times show:
- 0s, 24s, 64s and 104s: wide parking-lot view.
- 156s: wide view shortly before tighter framing.
- 160s: tighter/shifted view.
- 184s: tight parking-bay/curb view.
- 208s: close-up of a plate-like marking; characters are not confidently transcribed.
- 220s and 236s: tight parking-area view continues.
- 240s: wide parking-lot view has returned.
- 252s, 268s, 300s and 316s: wide view.

Consequences:
- Part 1 contains the wide view.
- Part 2 contains the wide-to-tight reframe around 156–160s and a close-up by 208s.
- Part 3 starts with a tight placard view, moves to a tight parking-area view, and returns to the wide view by 240s (about 28.86s into Part 3).
- The view changes are not aligned with the equal-third packet boundaries.
- The exact transition frames and camera mechanism are not claimed from the hash-only manifest. The storyboard establishes sampled view states, not every intervening frame.

## Licensing and privacy boundary

Commons metadata labels the file Public domain, Copyrighted=False and AttributionRequired=False. The page's rationale is described as fixed CCTV/no human input. This is flagged REVIEW REQUIRED: the same page describes a Supercircuits camera demonstration with optical/digital zoom, and the storyboard shows deliberate changes in framing. The Commons assertion is recorded, not independently validated as a legal conclusion.

A plate-like marking is visible in the source/storyboard. No characters are transcribed. No video or frame images are retained by the workflow; only metadata and cryptographic hashes are committed. Do not add extracted images or redistribute source frames until licensing and privacy review is complete.

## Repository availability and limitations

The three historical packet split files are not stored in this repository. Part 2 and Part 3 are re-encoded H.264 segments, not bit-identical WebM byte ranges. Part 1 has no recorded parent-source interval in its original manifest. Their local snapshots and hashes do not prove exhaustive coverage or fully reconcile split-boundary timing. The source copy is not the camera-native recorder file.

The reconstruction MP4 is a human-review artifact assembled from packet TD records and snapshots. It is not a canonical FV compile, an exhaustive reconstruction, or a validated event record.
