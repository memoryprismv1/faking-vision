# Fullerton Transportation Center CCTV temporal-merge example family

This folder contains three packet-part records and one merged packet record. It is retained as a historical illustration of temporal partitioning and cross-part identity reconciliation.

## Source identification

The source is strongly matched to Wikimedia Commons [Full, unedited Kelly Thomas confrontation video (35 min.).webm](https://commons.wikimedia.org/wiki/File:Full,_unedited_Kelly_Thomas_confrontation_video_(35_min.).webm). The Commons page describes surveillance-camera footage from Fullerton Transportation Center on 2011-07-05 and lists a duration of 34 min 10 s at 640 × 360, matching the final interval in this packet family. It identifies the original YouTube source as https://www.youtube.com/watch?v=dDpJ5FtG6Ac and lists Orange County Register in the media metadata.

The source file page displays public-domain rationales under California public-record and ineligible-work tags. This records the source page's stated status; it is not an independent legal opinion. The page's summary author field says `None (prepositioned surveillance camera at Fullerton Transportation Center)`, while its embedded metadata names Orange County Register. Both fields are preserved as published; they are not silently normalized into a single author claim. The Commons file is a YouTube-derived upload, not the camera's native recorder file.

The Commons page's file history identifies the upload as 2021-07-07 by Levivich, from the Orange County Register YouTube source. Its current page revision is `999941538` (last edited 2025-02-18). The exact source file is 61.4 MB, VP9/Opus, 640 × 360, 34 min 10 s.

## Evidence status and limits

The Commons distribution copy was acquired and fingerprinted on 2026-11-13. It is a YouTube-derived upload, not the camera-native recorder file. The acquisition record and source-frame manifest are retained under provenance/; the media and sample images are not committed to this repository. The workflow artifact is retained for 30 days, and the acquisition script can reproduce it.

The legacy interval labels are arithmetically contiguous: 00:00–11:23 (683 s), 11:23–22:46 (683 s), and 22:46–34:10 (684 s), totaling 2,050 s. This confirms only the arithmetic of the labels; it does not verify that the absent part files were cut at those exact source frames. `TOOLS/acquire_fullerton_source.py` now provides a reproducible Commons download, SHA-256/ffprobe record, a 10-second locator pass, and samples around the two declared boundaries. Its output is a local acquisition artifact, not a validation of the legacy OI/TIR claims.

All three part packets retain open provenance/correspondence disputes and BLOCKED analysis gates. Their OIs remain unverified legacy candidates, TDs are non-authoritative, and TIR observations/hypotheses are explicitly unverified. The merged packet retains three open disputes and a BLOCKED merge gate; its four global IDs remain uncommitted candidates, not verified identities. The earlier abbreviated packet-scoped references in merged OI/TIR were corrected to the full IDs in the part inventories.

The 10/5 Mbps figures are illustrative bitrate arithmetic, not measured deployment rates. The claimed 10,000x reduction is not an evidence-equivalent comparison because the packet omits the source media and evidence needed to audit it.

## Dataset separation

This family is **not** the separate [CCTV Snapshot TD Reconstruction Experiment](../CCTV_Snapshot_TD_Reconstruction_Experiment/README.md). That experiment uses the Supercircuits `BLK-HDPTZ12` parking-lot demonstration video (5 min 17 s, 1,920 × 1,080); it must not be used as a source, segment, or visual reference for this Fullerton recording.

## How to use this example

Use it only to discuss the *shape* of a multi-part CCTV investigation and the distinction between local packet identities and cross-part correspondence. Do not use it as an evidentiary account of the incident, a validated identity merge, or a storage benchmark.

Before treating it as an evidence-backed teaching example, supply the source media or source-aligned evidence snapshots, an acquisition record, reproducible part boundaries, and a reviewable correspondence record.


## Source acquisition and alignment review

See provenance/source_alignment_report.md, provenance/source_acquisition.json, and provenance/source_frame_manifest.json. The acquired file SHA-256 is e30f2ea56d69747113ed7ae2e5f45cd35968390343a20e4716b22437e6dde3d9 (64,379,026 bytes). The source is 2,049.826 s, 640 × 360, 29.97 fps, VP9/Opus. The Part1 TIR claim of a person at 10 s is rejected: that source frame is an opening title card. Cross-part identity correspondences remain blocked; no names or global identities are committed.


Source review finding: the source contains a distinct view transition between 992.7 s and 992.8 s, inside Part2. The 683 s and 1,366 s boundaries are visually continuous in sampled frames. The Part1 TIR claim at 10 s is rejected because the source frame is an opening title card. See provenance/source_alignment_report.md.
