# CCTV Snapshot parent-source alignment report

Review date: 2026-11-13

## Source identity and acquisition

- Commons file: https://commons.wikimedia.org/wiki/File:BLK-HDPTZ12_Security_Camera_Parkng_Lot_Surveillance_Video.webm
- Page revision: 1269449350; revision timestamp 2026-08-29T20:59:41Z.
- Original date: 2012-10-23.
- Author/source: Supercircuits; original YouTube ID U7HRKjlXK-Y.
- Commons SHA-1: d1115753bffc8967898779dfedfa5fe609bdb530.
- SHA-256: ff14641c693dbd1e78b1d22042876b5d3a4068c3301be8d07e504dd592debfaa.
- File size: 67,736,771 bytes.
- Duration: 316.708 seconds.
- Video: 1920 × 1080, 30 fps, VP9. Audio: Opus, 48 kHz stereo.

The Commons description says this clip demonstrates a 2.1-megapixel imager and 12× optical zoom, with digital zoom used to show a plate-like test marking on a telegraph pole at 360 feet. This is a camera product demonstration, not a real incident recording.

## Reproducible processing

The acquisition tool is TOOLS/acquire_cctv_snapshot_source.py; workflow is .github/workflows/cctv-snapshot-source-acquisition.yml. Successful run: https://github.com/memoryprismv1/faking-vision/actions/runs/43409586287.

The tool downloads the Commons source, records page/file metadata, computes SHA-256, probes the media with ffprobe, extracts frames for hashing, then deletes the source file and frame images. Only JSON metadata and hashes are committed:
- source_acquisition.json
- source_frame_manifest.json

Sampling:
- 80 global frames at 4-second intervals.
- 6 frames around the declared packet boundaries.
- 240 frames at 10 fps across 154–162s, 204–212s and 236–244s.
- Total: 326 frame hashes.
No source video or extracted frame image is retained in the repository or artifact.

## Source storyboard and view timeline

A separate prior storyboard artifact (not stored in this repository) contains source-grounded screenshots at 0, 24, 64, 104, 156, 160, 184, 208, 220, 236, 240, 252, 268, 300 and 316 seconds. The storyboard states that these are unmodified screenshots from the original recording and does not claim complete event coverage.

Observed sampled states:
- 0s, 24s, 64s, 104s: wide parking-lot view.
- 156s: wide view shortly before tighter framing.
- 160s: tighter/shifted view.
- 184s: tight parking-bay/curb view.
- 208s: close-up of a plate-like marking; characters are not confidently transcribed.
- 220s and 236s: tight parking-area view continues.
- 240s: wide parking-lot view has returned.
- 252s, 268s, 300s, 316s: wide view.

The source has several view/zoom regimes. The first major reframe occurs between the 156s and 160s storyboard samples. A closer plate-like-marking view is present by 208s. The tight parking-area view remains at 220s and 236s; the wide view is present by 240s. The 10-fps windows are hashed, but images are not retained, so this report does not claim exact transition frames or camera mechanics.

## Packet interval mapping

The parent duration is 316.708 seconds. The packet intervals are equal thirds:
- Part 1: 0–105.569333s (inferred; original Part1 manifest does not record a parent interval).
- Part 2: 105.569333–211.138667s (recorded).
- Part 3: 211.138667–316.708s (recorded).

The first major reframe and close-up occur inside Part2. Part3 begins with the tight placard view, transitions to a tight parking-area view, and returns to the wide view by source 240s (about 28.86s into Part3). These view changes do not coincide with the equal-third packet boundaries.

Part2's encoded duration is 105.599675s, about 30.341ms longer than its declared parent interval. Part3's encoded duration is 105.554s, about 15.333ms shorter than its declared interval. Part1's README reports 105.600s, but its parent interval is not recorded. The historical split procedure and exact frame-level boundary mapping are unavailable. The packet parts are re-encoded H.264 segments, not bit-identical WebM byte ranges.

## Licensing and privacy

Commons metadata labels the file Public domain, Copyrighted=False and AttributionRequired=False. The Commons rationale is described as fixed CCTV/no human input. This is flagged REVIEW REQUIRED: the source is explicitly described as a Supercircuits camera demonstration with optical/digital zoom and deliberate framing changes. The Commons assertion is recorded, not independently validated as a legal conclusion. Do not redistribute extracted frames until the licence basis is resolved.

A plate-like marking is visible in the source/storyboard; no characters are transcribed. The acquisition workflow retains no media or sample images, only metadata and cryptographic hashes.

## Current disposition

- Parent Commons distribution copy acquired and fingerprinted: VERIFIED.
- Duration, dimensions, frame rate, codecs, page revision and source attribution: RECORDED.
- Global, boundary and transition frame hashes: RETAINED.
- Source-level view sequence: PARTIALLY VERIFIED from storyboard samples; exact transition frames/mechanism not verified.
- Original camera-native file and historical packet split files: NOT AVAILABLE.
- Commons licensing rationale: REVIEW REQUIRED.
- Packet-local observations and exhaustive object/event coverage: NOT fully revalidated.
- Cross-packet identity correspondence: remains provisional; no global identity is committed.
