# Fullerton Transportation Center CCTV — merged packet

Packet ID: `PKT-CCTV-MERGE-001`
Inputs named by the legacy packet: Parts 1–3 of the full video now matched to Wikimedia Commons [Full, unedited Kelly Thomas confrontation video (35 min.).webm](https://commons.wikimedia.org/wiki/File:Full,_unedited_Kelly_Thomas_confrontation_video_(35_min.).webm).

## Intended demonstration

The packet is intended to illustrate merging packet-scoped identities across temporal parts and retaining a unified investigation timeline.

## Evidence status and limits

- The Commons source match is strong: its file page lists 34 min 10 s at 640 × 360 and describes Fullerton Transportation Center surveillance-camera footage dated 2011-07-05. It identifies the original YouTube source as https://www.youtube.com/watch?v=dDpJ5FtG6Ac. The source video is not included in this repository, and no acquisition record establishes that the packet producer obtained it or aligned the part boundaries to it.
- The three source-part packet records are present, but the underlying source media and source-aligned frame evidence are not included in this family.
- The claims of four global identities (three people and one structure), high correspondence quality, and a unified 00:00–34:10 timeline are packet/README assertions. They have not been independently reproduced or verified. The merged OI/TIR packet references have been normalized to the full packet-scoped IDs in the three part OIs; the earlier abbreviated IDs did not resolve to those records.
- The legacy “few KB” / 10,000x packet-size comparison does not account for source media or evidence required to audit the claims and must not be presented as an equivalent replacement for the original video. The bitrate arithmetic has been corrected: 10 Mbps is 108 GB/day per camera; 5 Mbps is 54 GB/day (decimal units). These are calculations, not measured deployment rates. The named “Officer Ramos” identity has been removed from the merged label because the personal name is not established by the retained packet evidence; correspondence claims remain unverified.

`dispute.json` now records three open blockers and sets the merge gate to BLOCKED. The four global IDs remain legacy candidates, not committed identities; the merged TD is explicitly non-authoritative and the compiled-spec draft is not approved as a render target. Treat this as a historical merge illustration with source-copy provenance established but unresolved identity, historical split, and evidence-equivalent storage claims; it is not a validated CCTV analysis or quantitative storage benchmark.


Source review update (2026-11-13): the Commons distribution copy is acquired and hashed. It contains a distinct view transition between 992.7s and 992.8s inside Part2; the declared 683s and 1,366s boundaries are visually continuous in sampled frames. The Part1 10s person-presence claim is rejected because that frame is an opening title card. All four global identity correspondences remain hypotheses and the merge gate remains BLOCKED. See the family provenance/source_alignment_report.md.
