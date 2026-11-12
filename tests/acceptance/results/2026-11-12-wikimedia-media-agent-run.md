# Wikimedia media FV agent rerun — 2026-11-12

**Branch:** `work/fv-docs-skill-cleanup-20261111`  
**Agent/model:** ChatGPT GPT-6  
**FV basis:** current `SPECIFICATION/FV_Working_Process_Specification.md` (v0.24 base plus later normative additions) and current provenance/viewpoint schemas  
**Conceptual basis:** Making Vision V2 (primary); Making Vision V1 (historical/origin context)  
**Execution scope:** Agent-level FV operation with local media inspection and packet artifact creation; not a standalone FV CLI  
**Generator invoked:** No  
**Reconstruction generated:** No

## Inputs

| Input | Type | Dimensions / duration | SHA-256 |
|---|---|---|---|
| `1280px-Cat_jump.jpg` | Image | 1280 × 853 | `e200298a5fbfb4df4ad3662d42727efb0e434226161614918a00bb126f7a873d` |
| `Kitten_jumping_on_bamboo_mat.webm` | Video | 1920 × 1080; 30 fps; 4.333333 s; 130 frames | `203244ad83246a7ee74c46600b390e66547e55ffd5ff7d9375d95b71f9dfc799` |

Both source files were retained unchanged in the final local rerun archive. Neither source binary is committed to the repository. The supplied media metadata did not retain the original Commons file-page URLs; attribution records the source page as not recorded and the licence as unverified. No reuse-rights claim is made.

## Correction made during acceptance

The first redone packet bundle omitted an explicit no-dispute state from its packet READMEs. The specification permits a packet with no dispute to declare `DISPUTES: NONE` in its manifest/README instead of carrying an empty `dispute.json`; without either declaration, the packet-level rendering gate is not satisfied. The prompt artifact from that intermediate bundle is therefore **not accepted**.

The final bundle adds the explicit `DISPUTES: NONE` declaration to both packet READMEs, without changing either source media file. It also aligns the video tail/appendage finding and adjacent TD interval boundary at 1.0 s. Validation and prompt-only compilation were then repeated against the corrected packet. The original intermediate bundle remains distinct from the final accepted bundle.

## Image analysis — `fv analyse`

- Packet: `PKT-093b5e7066c20685`; OI + MSRM, with root-level `viewpoint.json` and `packet_provenance.json`.
- Direct structure was recorded before semantic commitment: one bounded cat figure, forelimbs extended toward an irregular embankment, tail extending rearward, vegetation and uneven ground.
- Committed semantic inventory: one domestic cat and one irregular stone/earth embankment.
- Vegetation and ground remain background appearance, not extra object identities.
- The narrow brown strip at lower-right remains unresolved between exposed soil, a shallow drainage channel, and a path.
- The still establishes one pose only. It does not establish takeoff, landing, trajectory, or preceding/following action.
- Source camera position, orientation and calibration remain unknown.
- A separately instantiated default render VPO is explicit and marked `is_default: true`; it is not source-camera evidence.

## Video investigation — `fv investigate`

- Packet: `PKT-d1b7f0221871c504`; OI + MSRM + TD, with TIR retained as the investigation workspace.
- Decoded all 130 frames for a low-resolution adjacent-frame difference pass. This was used only to allocate inspection, not as semantic evidence.
- Broad reconnaissance: 44 samples at 0.1-second intervals across the clip.
- Selective review: 87 samples at 0.05-second intervals, focusing on posture change, curling/appendage movement, the white form entering near the cat's head, and follow-through.
- The filename says “jumping”, but no takeoff, airborne displacement or landing sequence is visible. No jump is reported within this 4.333-second clip.
- 0.0–0.45 s: the cat shifts its body/forelimbs and lowers its head.
- 0.45–1.0 s: the cat continues curling; a pale furry appendage sweeps laterally around 0.7–1.0 s, likely the tail but not conclusively attributed.
- 1.0–1.7 s: forepaws draw inward and the head lowers close to the paws/body. Grooming or mouthing is plausible but unconfirmed.
- 1.7–1.95 s: the cat remains curled with small adjustments.
- 1.95–2.25 s: a white furry limb-like form enters from the top edge near the head. Its identity and relationship to the cat remain unresolved.
- 2.25–4.333 s: the cat remains curled with minor movement; the white form remains partly visible near the upper edge in portions of the interval.
- The unresolved form was promoted for further inspection but was not committed as a second OI entity. The action candidate was not promoted to a definite behaviour label.
- “Kitten” and “jumping” in the filename were not treated as visual evidence; the visual source establishes a cat, not its age.
- Audio was not analysed; the decoder emitted an Opus packet-header warning. No audio-derived claim is made.

## Full validation result

**Image packet — PASS**
- Structural validity: PASS.
- FV semantic validity: PASS within the source's limits; uncertainty preserved.
- Evidence consistency: PASS; the single still is not used to infer trajectory or source-camera geometry.
- Dispute/reconciliation: NONE, explicitly declared in the packet README.
- Rebuild assessment: **REBUILD NOT INDICATED**. Newly created against the current authoritative rules; `0.24` records the specification base label, while later normative additions are applied. No legacy migration is required and no consolidated version label is invented.
- Provenance schema: PASS against the full repository `FV_Packet_Provenance_Schema.json` (Draft 2020-12).
- Viewpoint schema: PASS against the full repository `FV_Viewpoint_Schema.json` (Draft 2020-12).
- Exactly one default render VPO is declared; source viewpoint initialisation remains separately unknown.
- Compilation readiness: READY for prompt-only compilation.
- Prompt-only compilation: PASS; `COMPILED_SPEC.txt` selects the default render VPO and preserves the locked inventory and uncertainty.
- Input packet unchanged by validation/compilation: PASS.

**Video packet — PASS**
- Structural validity: PASS.
- FV semantic validity: PASS within the source's limits; cat and mat are committed, while the white furry form and action label remain unresolved.
- Evidence consistency: PASS; TD covers the full 4.333333-second source with contiguous intervals and the tail/appendage finding is aligned to the 1.0 s boundary.
- Dispute/reconciliation: NONE, explicitly declared in the packet README.
- Rebuild assessment: **REBUILD NOT INDICATED**. Newly created against the current authoritative rules; no legacy migration is required.
- Provenance and viewpoint schemas: PASS against the full repository Draft 2020-12 schemas.
- Source viewpoint position/orientation/calibration remain unknown. No render VPO is asserted or needed for this investigation-only packet.
- Compilation was not requested; no video prompt or reconstruction was produced.
- Audio was not intentionally included or analysed; no transcript or audio-derived claim is made.

## Checks and limits

- **47/47** local structural, reference, temporal, dispute-gate and schema checks passed.
- Four full JSON Schema validations passed with `jsonschema` 4.26.0 / `Draft202012Validator`: provenance and viewpoint schemas for both packets under Draft 2020-12. Tested schema blob SHAs: provenance `d4667c745b61414bff16cd5a0d9a026a12d2f933`; viewpoint `fd8ed83065e63778c1affc2d9c81b9edddefb058`.
- No dedicated OI, MSRM, TD or TIR JSON Schemas are present in the current `SPECIFICATION/` directory; those records received structural/reference/temporal consistency checks, not a formal schema-conformance claim.
- No standalone `fv validate` executable was invoked. The validation was performed as an agent-level skill operation against the current specification; the repository defines FV commands as agent-level operations, not a standalone CLI.
- No renderer, media generator, or independent generated-media audit was invoked.
- No reconstruction was generated.

## Other acceptance gates

- **Case B — legacy viewpoint compatibility: PASS.** The older `blue_chairs` packet has no `viewpoint.json`; virtual `VP-DEFAULT` remains read-time-only source compatibility, not a render VPO. No viewpoint file or camera geometry was invented. Prompt compilation was not attempted because no render VPO was available.
- **Case C — negative reconciliation gate: PASS.** See `2026-11-12-case-c-agent-run.md`. Pending post-reconciliation validation blocked prompt production.
- **Overall defined agent acceptance: PASS for Cases A, B and C.** This is acceptance of the defined skill-runtime cases, not evidence of a standalone CLI or general-purpose FV runtime.

## Artifact retention

The final rerun archive is retained locally as `FV_Wikimedia_Test_2026-11-12-final.zip`. It contains both packet structures, unchanged source files, observation and investigation records, prompt-only compile artifact, full validation report, manifest and 47-check log. The repository contains this evidence summary and source hashes, not the binary media or full archive.
