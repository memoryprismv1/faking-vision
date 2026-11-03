# CCTV global timeline and cross-packet identity ledger

Status: evidence-based continuity ledger; **not a merged FV packet**. Packet-local IDs and source records remain unchanged. This document records supported correspondences and explicit non-correspondences from the three existing packet analyses. It does not certify exhaustive object inventory or resolve active visual disputes.

## 1. Source chronology

All three packet manifests identify the same parent CCTV video:
`BLK-HDPTZ12_Security_Camera_Parking_Lot_Surveillance_Video (1).webm`.

| Packet | Parent-source interval (s) | Local duration (s) | Offset used for global time |
|---|---:|---:|---:|
| PKT-CCTV-001 | 0–105.600 (README duration; source manifest is snapshot-index based) | 105.600 nominal | 0 |
| PKT-CCTV-002 | 105.569333–211.138667 | 105.599675 | 105.569333 |
| PKT-CCTV-003 | 211.138667–316.708 | 105.554 | 211.138667 |

The part-01/part-02 parent intervals overlap by approximately 0.030667 s. Part-02/part-03 intervals meet at 211.138667 s. The offsets are parent-source interval metadata, not a claim that the extracted packet files are frame-accurately synchronized at every boundary. Packet snapshots are nominal whole-second samples and cannot settle sub-frame continuity.

Global time conversion for packets 002 and 003 is:
- packet 002 global time = local time + 105.569333 s
- packet 003 global time = local time + 211.138667 s

## 2. Global visual timeline

| Global time (s) | Packet/local time | Observed visual regime or event | Continuity interpretation |
|---:|---|---|---|
| 0–18 | 001 / 0–18 | Fixed elevated wide parking-lot view; dense parked-vehicle tableau, marked bays, landscaped island, access road, trees and utility infrastructure | Stable wide-view baseline. Inventory is explicitly provisional, not exhaustive. |
| 18–30 | 001 / 18–30 | Silver sedan traverses aisle right-to-left; a person walks diagonally toward foreground/right and becomes partly occluded by a red SUV | Both events supported at interval level. Proximity is observed; interaction/contact is not established. |
| 30–40 | 001 / 30–40 | Return to mostly stable tableau; sedan/person no longer visible in sampled view | Disappearance from view supported; routes after occlusion/exit unknown. |
| 40–54 | 001 / 40–54 | Small blue vehicle travels along background access road right/centre-to-left, partly obscured by trees | Broad direction/interval supported; exact path obscured. |
| 54–94 | 001 / 54–94 | Mostly stable parking-lot tableau | No new tracked event asserted by this packet's temporal record. |
| 94–105.6 | 001 / 94–105.6 | White pickup on background access road and dark sedan in foreground aisle, both moving toward left | Distinct image regions and distinct packet-local IDs; movement supported, exact entry times not frame-accurate. |
| 105.569–154.569 | 002 / 0–49 | Wide parking-lot view continues; opening dark sedan candidate moves in foreground (0–10 local); person candidate appears around 15–42 local | The opening sedan is not linked to part-01 OBJ-050; no cross-packet identity claim. Person continuity is provisional within packet 002 only. |
| 154.569–156.569 | 002 / 49–51 | Abrupt substantial framing change; earlier wide scene is displaced/out of frame | Explicit camera/view-state event. Do not encode displaced parked vehicles as having departed. Mechanism is not established here. |
| 157.569–203.569 | 002 / 52–98 | Tight view with vertical structures, hedge/road; partly occluded light vehicle around local 69–70; dark vehicle enters from right around local 96–97 | Both vehicle identities unresolved. OBJ-004 is explicitly not linked to packet-002 OBJ-001. Signed pole/placards appear from about local 59. |
| 203.569–211.169 | 002 / 98–105.6 | Camera tightens/reframes onto a pole with multiple placards; blur prevents reliable transcription | Signed pole continuity within packet 002 S03/S04 is supported. This is the outgoing boundary view. |
| 211.139–214.139 | 003 / 0–3 | Opening tight view of two placards on a vertical pole | Strong visual correspondence to packet-002 outgoing pole/placard view; one composite packet-002 record maps to three packet-003 records (pole + two placards), not a one-to-one object match. |
| 214.139–219.139 | 003 / 3–8 | View widens; pole/placards shrink; road, hedge, island and parking bays emerge | Major visual-regime change. Exact mechanism (zoom, pan/tilt, cut or compound movement) remains open. |
| 219.139–237.139 | 003 / 8–26 | Wide parking-lot scene resolves with rows of vehicles | Inventory is coarse/grouped; per-vehicle identity is intentionally incomplete. |
| 237.139–297.139 | 003 / 26–86 | Wide lot remains; parked rows and background structures; sparse samples show local changes | No complete trajectories or exhaustive identity set asserted. |
| 297.139–311.139 | 003 / 86–100 | Light-coloured elongated vehicle-like form changes position across middle-left region | Active temporal investigation. Exact identity, path and continuity remain unresolved. |
| 311.139–315.139 | 003 / 100–104 | Wide lot persists; placements differ from opening wide view | Sparse samples do not establish all movement or identities. |
| 315.139–316.693 | 003 / 104–105.554 | Final sampled wide view | No cut is confirmed in final sample. |

The table preserves gaps: packet-local sampling is sparse, and the global timeline does not interpolate unobserved motion.

## 3. Cross-packet identity ledger

### 3.1 Supported correspondence

| Source record(s) | Candidate target record(s) | Relation | Evidence and limits | Status |
|---|---|---|---|---|
| PKT-CCTV-002-OBJ-035 | PKT-CCTV-003-OBJ-001, OBJ-002, OBJ-003 | One-to-many: composite pole/placards record to two placard candidates plus supporting pole | Packet 002 TD records the pole with attached placards in its final tight view; packet 003 opens on two placards attached to a vertical pole in the adjacent parent-source interval. Packet 003 separates the visual components that packet 002 represented as one structure candidate. Markings remain unreadable. | **Supported visual correspondence; composite-to-components.** Do not duplicate as three independent global physical objects without retaining the part-whole relation. |

### 3.2 Boundary associations retained from earlier dense-review work

The user's earlier CCTV boundary-review artifacts (dated 2026-10-14 and retained in the ChatGPT Library) contain additional evidence that is not represented in the three packet JSON files:

| Boundary / candidate | Earlier review evidence | Decision to carry forward |
|---|---|---|
| PKT-CCTV-001 → PKT-CCTV-002: dark foreground sedan-like vehicle | 5-fps native-resolution review across P1 local 100.0–105.4 s and P2 local 0–6.0 s; a later sequential decode pass retained every third decoded frame through P1 100–105.5667 s and P2 0–3.0 s. Broad positional progression image-left is supported, but no full 30-fps track, reliable visibility bounds or independently checked box sequence exists. | **Strong provisional candidate, not confirmed global identity.** Keep packet-local IDs separate. |
| PKT-CCTV-001 → PKT-CCTV-002: light-coloured pickup/utility-like vehicle | Earlier dense half-second crops and 5-fps boundary review describe a candidate moving image-left through the middle/background aisle. The downscaled overview and sparse samples do not establish unique identity or precise displacement. | **Provisional, weaker than the dark-sedan candidate.** No confirmed global identity. |
| PKT-CCTV-002 → PKT-CCTV-003: sign-bearing support / attached marking | Separate boundary evidence reports matching sign arrangement, support, hedge texture and foreground crop in P2 terminal close-up and P3 first decoded frame. | **High-confidence scene-anchor correspondence**, not a vehicle-identity bridge. Preserve pole/placard part-whole relationship in packet-level ledger. |
| PKT-CCTV-002 → PKT-CCTV-003: vehicles around rapid reframing | Earlier review explicitly leaves these unresolved; apparent disappearance/appearance around changed field of view is not motion evidence. | **No match made.** |

The sequential extraction review used OpenCV decoding and frame indices but did not independently verify presentation timestamps; nominal times derived from the reported 30-fps rate must not be promoted to authoritative PTS. The 5-fps review omits five of every six source frames. Neither pass confirms a vehicle match. The earlier P1/P2 review records zero confirmed cross-chunk vehicle matches.

Earlier evidence artifacts to preserve with this ledger:
- `CCTV_FV_P1_P2_DENSE_SAMPLING_REVIEW.md` (5-fps, 0.2-s nominal samples)
- `CCTV_FV_P1_P2_CONSECUTIVE_FRAME_PASS.md` (every third sequentially decoded frame; nominal timing)
- `CCTV_FV_P2_P3_BOUNDARY_EVIDENCE.md` (sign-bearing support scene anchor)
- `CCTV_FV_CROSS_CHUNK_CORRESPONDENCE_DECISIONS.md` and its JSON companion (provisional correspondence decisions)

These are historical review derivatives, not original packet files and not an independent audit. They supplement the repo's packet records without authorizing mutation or merge.

### 3.2 Within-packet continuity only

| Source record(s) | Relation | Status |
|---|---|---|
| PKT-CCTV-002-OBJ-035 across S03/S04 | Same signed pole within the tight-view interval | Supported by packet 002 TD; packet-local continuity only. |
| PKT-CCTV-003-OBJ-003 across opening/widening view | Same pole candidate across the initial camera widening | Packet 003 describes continuity as likely; retain its uncertainty. |
| PKT-CCTV-001-OBJ-046 and OBJ-047 | Sedan/person events in same aisle interval | Both events supported; no contact or interaction established. |

### 3.3 Explicitly unresolved / do not merge

| Record(s) | Why no identity assignment is made |
|---|---|
| PKT-CCTV-001-OBJ-050 vs PKT-CCTV-002-OBJ-001 | Both are dark sedan-like foreground candidates in different packet intervals/views; appearance/category alone does not establish same vehicle. |
| PKT-CCTV-001-OBJ-049 vs PKT-CCTV-002-OBJ-003 | White pickup on part-01 background road vs partly occluded light vehicle on part-02 far road; no trajectory bridge. |
| PKT-CCTV-002-OBJ-001 vs PKT-CCTV-002-OBJ-004 | Packet 002 explicitly asserts no correspondence; retain separate packet-local candidates. |
| PKT-CCTV-002-OBJ-036 vs signed pole (OBJ-035) | Other dark vertical structures may be pole or tree trunk; appearance alone is insufficient. |
| PKT-CCTV-003-OBJ-009 vs any earlier vehicle | Later light-coloured moving form has unresolved identity/path; no supported bridge to part-01/02 vehicles. |
| Any packet-001 parked vehicle vs packet-002/003 grouped parked-vehicle records | Framing changes and grouping prevent defensible instance correspondence. |
| Packet-003 vehicle groups OBJ-010/011/012/019 vs individual packet-001/002 parked vehicles | Group records are not individual identities and must not be expanded into invented members. |

## 4. Camera/viewpoint continuity

The packets describe one source CCTV camera with substantial changes in framing. A stable physical camera/viewpoint identity is the appropriate working hypothesis; camera movement/reframing/zoom events belong in temporal camera-state records, not as new physical cameras or as object departures. The current packet evidence does not establish the precise mechanical operation behind every transition. Preserve the observed view changes and unresolved mechanism.

## 5. Merge gate and blockers

A global chronology and a limited cross-packet correspondence ledger can be prepared from the current repository evidence. A **settled merged FV packet cannot yet be truthfully produced**:

1. Packet 003 has two active disputes: the moving light-coloured vehicle-like form (DSP-002) and the opening view change/mechanism (DSP-003). Its declared merge gate is BLOCKED.
2. Packet 001's baseline inventory is provisional and explicitly not exhaustive; its deferred disputes are chunk-scoped, not global resolution.
3. Packet 002 has coarse/grouped baseline records and unresolved temporal identities; it has no packet-local PC/dispute/validation files in the current directory listing.
4. The parent intervals and nominal sample clocks do not provide frame-accurate synchronization at the part-01/02 overlap or packet boundaries.
5. Original source segments for all three chunks are not all present in the repository as directly available media. The retained evidence is the manifests, packet records and sampled frames.

Therefore this ledger is a handoff and reconciliation aid, **not permission to compile/merge**. A future merge must preserve all original packet-local IDs and records, introduce a separate global correspondence layer, retain one-to-many/part-whole relations and unresolved identities, and never overwrite source packets.

## 6. Next evidence needed

- Denser source frames around packet-003 local 81–104 to investigate the moving light-coloured form and its path.
- Denser source frames around packet-003 local 0–8 to characterize the opening view change without presuming zoom/pan/tilt/cut.
- The original part-01/02 boundary media or exact source-frame mapping to test the small overlap and wide-view continuity at frame level.
- A packet-002 dispute/validation disposition if the packet is intended to be promoted beyond its current exploratory status.

No outside bot reports or synthetic audit records were used to construct this ledger.
