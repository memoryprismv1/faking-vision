# Fullerton source acquisition and alignment report

Review date: 2026-11-13

## Source identity and acquisition

- Commons file: https://commons.wikimedia.org/wiki/File:Full,_unedited_Kelly_Thomas_confrontation_video_(35_min.).webm
- Page revision: 999941538; last edited 2025-02-18.
- Commons upload: 2021-07-07 by Levivich.
- Original YouTube source: https://www.youtube.com/watch?v=dDpJ5FtG6Ac
- SHA-256: e30f2ea56d69747113ed7ae2e5f45cd35968390343a20e4716b22437e6dde3d9.
- Measured size: 64,379,026 bytes (64.379 decimal MB; approximately 61.4 MiB).
- Measured duration: 2,049.826 seconds (34:09.826).
- ffprobe: 640 × 360, 30000/1001 fps, VP9 video, Opus audio at 48 kHz mono.
- The Commons summary author field says None (prepositioned surveillance camera at Fullerton Transportation Center); embedded metadata says Orange County Register. Both are preserved as conflicting metadata fields.
- Commons displays California Public Records Act and ineligible-work public-domain rationales. This records Commons' assertions; it is not an independent legal opinion.

**Source limitation:** this is the YouTube-derived Commons distribution copy, not the camera-native recorder file. The title says “Full, unedited,” but the distributed file contains opening/closing title cards and a change between distinct visual views. No camera IDs are supplied.

The source file and sample images were retained in GitHub Actions artifact fullerton-source-acquisition for 30 days (workflow run https://github.com/memoryprismv1/faking-vision/actions/runs/43405957378). The source media and sample images are not committed to the repository. The acquisition script TOOLS/acquire_fullerton_source.py reproduces the download and evidence pass. The committed acquisition record and frame manifest contain the source hash and sample hashes.

## Source-aligned review

The acquisition generated:
- 205 global locator frames at 10-second intervals;
- 7 frames around the legacy part boundaries;
- 30 frames at 10 fps from 991.0s through 993.9s to localize the view transition.

Observed source structure in the sampled evidence:

| Source time | Observation |
|---|---|
| 0s, 10s, 20s | Opening title/warning cards |
| 30s | First surveillance view (View A) is present |
| 683s | Sampled boundary; View A continues, no visible cut |
| 992.7s | View A still present |
| 992.8s | Distinct second view (View B) present |
| 1,366s | Sampled boundary; View B continues, no visible cut |
| 2,040s | Closing title/logo card |
| 2,049.826s | Measured end of file |

The source does not provide camera identifiers, so View A and View B are neutral visual labels, not claims about specific camera hardware.

## Consequences for the legacy packets

| Packet | Legacy interval | Source alignment finding |
|---|---:|---|
| Part1 | 0–683s | Opening cards followed by View A |
| Part2 | 683–1,366s | Contains View A and the View A → View B transition between 992.7s and 992.8s |
| Part3 | 1,366–2,050s label | View B; label end is 0.174s beyond measured file duration |

The labels 683 + 683 + 684 = 2,050s are arithmetically contiguous. The actual file is 2,049.826s. The samples at 683s and 1,366s are visually continuous; they are not the observed view transition. The original packet split files and exact split procedure are absent, so the historical segment boundaries and any gaps/overlaps cannot be proven from labels alone.

### TIR correction

The Part1 TIR claim that Person A is present at 00:00 + 10s is **rejected**. The source frame at 10 seconds is an opening title card; no person is visible. The source file SHA-256 and exact frame SHA-256 are recorded in Part1_00-00_to-11-23/TIR.json.

Other local person/action observations have not been exhaustively re-investigated. The two-view structure means the legacy cross-part identity matches cannot be assumed. All four global identity correspondences remain hypotheses; no global identity is committed.

## Current disposition

- Commons distribution-copy acquisition: verified.
- Source SHA-256 and ffprobe metadata: verified.
- Global locator, boundary and transition sample hashes: retained in source_frame_manifest.json.
- Part1 10-second TIR claim: rejected against direct source frame.
- Legacy part split files and packet-producer acquisition history: not recovered.
- Camera-native source: not obtained.
- Cross-part identity correspondence: blocked.
- Unified merge: remains blocked pending candidate-by-candidate source review and recovery of the historical split evidence.

## Dataset separation

This is not the separate CCTV Snapshot TD Reconstruction Experiment, which uses the Supercircuits BLK-HDPTZ12 parking-lot demonstration video. Do not mix its frames, duration, source metadata, or processing evidence with this Fullerton source.
