Faking Vision Packet v0.24
packet_id: PKT-CAT-JUMP-BACK-001
source_id: Cat_jumping_backwards.webm
source_url: https://upload.wikimedia.org/wikipedia/commons/transcoded/f/f1/Cat_jumping_backwards.webm/Cat_jumping_backwards.webm.480p.vp9.webm
commons_page: https://commons.wikimedia.org/wiki/File:Cat_jumping_backwards.webm
description: A domestic cat (Felis catus) jumping backwards. Slow-motion replay (1/4 speed) added to original material.
date: 23 October 2016, Author: Mary Qin, Source: https://vimeo.com/188592921
duration: 19s, dimensions: 1920x1080, transcode: VP9 480P 574kbps

## Source and evidence limitations

- Direct pixel-level frame inspection was unavailable during the original packet production because source download was blocked. The analysis relied on Wikimedia metadata and the file description.
- The repository contains no source video and no retained frame snapshots. `snapshot/manifest.json` explicitly records that no snapshots were preserved.
- The original/replay transition is ordered but not precisely timestamped. Do not invent the transition time.
- Background and spatial layout remain unresolved; do not add props or setting details from world knowledge.
- The packet's object identity and action interpretation remain limited by the absence of direct frame evidence.

## Packet contents and lifecycle

The retained canonical packet files are `OI.json`, `MSRM.json`, `TD.json`, `PC.json`, `dispute.json`, `dispute.reconciled.json`, `COMPILED_SPEC.json`, `COMPILED_PROMPT.txt`, `snapshot/manifest.json`, and the validation reports.

The initial validation report records three snapshot-directory checks as failures and blocks rendering while disputes are open. The human resolution later accepted metadata-only analysis with uncertainty preserved and released the dispute gate; it did not add source frames or upgrade the evidence.

**Validation warning:** `VALIDATION_REPORT_POST_RESOLVE.txt` claims that `snapshot/verification`, `snapshot/objs`, and `snapshot/disputes` exist and reports the packet as valid. That claim conflicts with the repository tree and the snapshot manifest, which records that no snapshots were preserved. The reconciliation record also says post-reconciliation validation was still “to be performed”. Treat the post-resolution report as inconsistent historical output, not proof of a completed validation.

No FV executable/CLI was run. Do not describe this packet as visually verified, exhaustively analysed, or independently audited. The compilation artefacts are retained as an experimental prompt/specification, not evidence that the source was faithfully reconstructed.
