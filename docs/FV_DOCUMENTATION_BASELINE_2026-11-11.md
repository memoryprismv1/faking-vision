# FV documentation and skill baseline audit

Date: 2026-11-11
Repository baseline: `main`
Working branch: `work/fv-docs-skill-cleanup-20261111`
Scope: documentation, skill, command reference, and related support files.
Status: initial audit; no examples changed.

## Source hierarchy confirmed

1. `SPECIFICATION/FV_Working_Process_Specification.md` — authoritative process specification.
2. `SPECIFICATION/FV_Provenance_And_Audit.md` and its schemas — supplementary provenance and audit rules.
3. `SKILL.md` — agent-facing operating instructions.
4. `commands.md` — command interface reference.
5. `HOW_TO_USE.md` — human-facing operating guide.
6. `README.md` — project overview and navigation.
7. `PACKETS/README.md` and `PACKETS/META_EXAMPLES_CATALOG.md` — packet conventions and example provenance.
8. `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md` — preserved historical extract only; not current authority.

## Baseline size

| File | Lines | Characters |
|---|---:|---:|
| README.md | 150 | 7,888 |
| SKILL.md | 1,590 | 129,507 |
| commands.md | 345 | 20,112 |
| HOW_TO_USE.md | 583 | 29,365 |
| Working Process Specification | 2,250 | 148,956 |
| Provenance and Audit | 184 | 11,767 |
| PACKETS/README.md | 25 | 2,253 |

## Command inventory comparison

| Interface | Commands found |
|---|---|
| `commands.md` | analyse, investigate, assemble, merge, create, rebuild, edit, resolve, validate, compile, audit |
| `SKILL.md` | Same core operations, plus explicit `fv edit viewpoint` subcommand |
| `HOW_TO_USE.md` | Same core operations as command reference |
| `README.md` | At baseline, listed rebuild and upgrade as separate entries; upgrade is an alias |

Finding at baseline: viewpoint editing was documented under `fv edit` in `commands.md`, but absent from its command map. The command map has now been corrected.

## Findings

The command-reference comparison also found a formatting defect in `HOW_TO_USE.md`: the `fv audit` row sat outside the command-map table after a prose subsection. It has been moved back into the table. The README reconstruction path now shows the optional rebuild/upgrade step already documented in the command reference and how-to guide.

### High priority

1. **Historical specification embedded in the skill was not clearly separated from current instructions.** The skill's operating-rule paragraph described it as containing the "complete v0.24 FV operating material", then labelled the appended extraction "complete authoritative source". Current viewpoint instructions explicitly supersede older v0.24 wording. This created an avoidable authority ambiguity for an unfamiliar agent. The extraction is now labelled historical/reference-only, and the current Working Process Specification is explicitly authoritative.
2. **The command reference map omitted the explicit viewpoint subcommand.** Detailed syntax existed later in the same file, but the top-level command map did not expose it. The map now includes `fv edit viewpoint`.
3. **The skill's `fv validate` instruction hard-coded validation against v0.24 packet rules.** This was inconsistent with the skill's migration assessment and current-specification authority. It now directs validation against the current authoritative Working Process Specification and the packet's declared version/compatibility rules.
4. **The skill conflated Making Vision promotion with evidence-based object commitment.** Its initial rule said candidates should be promoted only when supported by visual evidence and made promotion a gate before object counting/identity assignment. Making Vision V2 defines promotion as allocation of additional processing; it can be driven by state, needs, uncertainty, risk, learned relevance, expectations, and environmental statistics, and can precede recognition or persistence. The skill now separates allocation/promotion from evidence-based entity and identity commitment, states that perturbation does not guarantee promotion, points to the current V2 material, preserves the prerequisite as a hard gate for visual operations, states that MV's unified architecture is a synthesis rather than an established named biological mechanism, and keeps learning distinct from persistence/storage.
5. **The skill's self-contained-use claim depended on repository availability.** It said the user need not supply the specification, but the embedded full text is a historical v0.24 snapshot while the current specification is a separate repository file. The operating rule now says to read the current file when the repository is available and to disclose when it cannot be consulted; the historical snapshot is not a substitute.
6. **The documentation set repeated substantial process material.** The skill originally embedded a 1,042-line historical v0.24 specification snapshot alongside active instructions. The snapshot has now been moved verbatim into `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md`; `SKILL.md` retains a short historical-reference pointer. The active skill was 561 lines immediately after extraction and is now 597 lines after adding the audio-enabled video procedure, while the historical source remains preserved separately.

### Medium priority

7. **README initially listed `fv rebuild` and `fv upgrade` as separate commands**, while the skill and command reference define upgrade as an alias. The README now labels `fv upgrade` as an alias.
8. **The Working Process Specification contains legacy version/change-log material and later sections whose numbering/order is not strictly sequential.** The PC subsections and the v0.9–v0.11 changelog order are now corrected, along with the misplaced audio headings. Other historical section numbering remains unchanged pending a separate review.
9. **The command interface is an AI-agent textarea interface, not a standalone FV CLI.** This distinction is already stated in `commands.md` and `HOW_TO_USE.md`; retain it prominently and avoid describing these commands as executable shell commands.
10. **`fv audit batch` is not an implemented skill command.** The offline Python batch aggregation utility, JSON schema, tests, and workflow exist; the agent-level command remains proposed pending reliable skill-runtime invocation.
11. **Question-directed media analysis belongs to `fv investigate`, not a separate `fv query` command.** TD temporal queryability remains a packet capability and acceptance test; users can ask what an object did and when directly against supplied media without opening TD files.
12. **The normal workflow diagrams implied that `resolve` was always required**, although the accompanying prose made it conditional on a blocking dispute or ambiguity. The README, command reference, how-to guide, and current specification now label it `resolve if required`.
13. **The viewpoint command descriptions blurred source viewpoint records and render VPOs.** They now distinguish inspection of both from editing render-preset pose/state while preserving source `initial_state`.
14. **The `fv analyse` command output contract omitted required `viewpoint.json` metadata.** The command reference now includes source-supported viewpoint initialisation and video viewpoint transitions in TD.
15. **The active skill and command guides underexposed the normative audio-enabled video procedure.** They omitted timestamped transcript creation before initial TIR/TD, cumulative transcription-fidelity versus cross-modal assessment, transcript-guided adaptive sampling, and the rule that selected source frames receive full FV image analysis. The skill, command reference, and how-to guide now expose these requirements.
16. **Several specification headings obscured the structure of normative material.** The audio transcript subsection appeared after its body; audio packet requirements were formatted as headings; PC subsections appeared in reverse order; and v0.11 changelog appeared before v0.9/v0.10. These were structurally repaired without changing the underlying requirements. The snapshot subsection is now 8.7 (following 8.6 audio), the final acceptance-test subsections are numbered 30.1–30.3, and the v0.9–v0.11 change logs are nested subsections rather than duplicate numbered chapters.

## Existing support implementation (not a CLI claim)

**Offline audit/provenance utilities**
- `TOOLS/fv_audit_batch.py`
- `TOOLS/test_fv_audit_batch.py`
- `TOOLS/test_fv_packet_provenance_schema.py`
- `TOOLS/requirements.txt`
- `SPECIFICATION/FV_Audit_Report_Schema.json`
- `SPECIFICATION/FV_Audit_Batch_Report_Schema.json`
- `.github/workflows/fv-audit-batch.yml`

**Browser editing prototypes and tests**
- `PACKETS/tools/FV_Edit_Visual_Workbench.html` and its README/smoke test.
- `PACKETS/tools/FV_Media_Object_Editor_MVP.html` and its README.
- `tests/browser/viewpoint-editor.spec.js`
- `tests/browser/environment-workbench.spec.js`
- `tests/browser/media-object-editor.spec.js`
- `playwright.config.js` and `package.json`
- `.github/workflows/fv-environment-workbench-browser.yml`

The browser editors are bounded prototypes. The Visual Workbench is schematic-only and its local checks are not the authoritative FV validator. The Media Object Editor uses manual masks and planar image approximation; it is not a full 3D renderer or semantic packet validator. The browser suite tests these bounded behaviors, not agent-level FV commands.

The audit/provenance workflow runs on pushes to `feature/fv-audit-batch`, relevant pull requests, and manual dispatch. The browser workflow runs on relevant pull requests and manual dispatch. The latest `main` commit inspected (6d47e1f) returned no associated pull-request-triggered workflow runs through the available commit-run lookup. That lookup does not enumerate every workflow trigger. This is not evidence that tests pass or fail; execution status remains unverified.

## Branch review notes

The repository has multiple active and historical branches. Comparisons against `main` show that several branches are divergent, not simple descendants. In particular, the batch-clean, viewpoint-scope, skill-status, dataset-intake, and assembly experiment branches contain unique commits. They must be reviewed as evidence, not merged automatically.

No branch has been merged as part of this work. The working branch was created from `main`.

## Version-label and rebuild-target clarity

The Working Process Specification's title still labels the base text v0.24, while later sections contain normative v0.26 and v0.27 additions. The highest explicit normative addition is v0.27. The header now states that the base text is v0.24 and later normative additions include v0.26 and v0.27, without inventing a consolidated release number. Because `fv rebuild` defaults to the current authoritative version, the consolidated target-version designation remains an explicit open decision rather than something to infer or silently rewrite. The provenance/audit document now clarifies that it originated as a v0.24 extension but remains a supplementary contract referenced by the current specification. The skill's rebuild syntax has also been normalized to the generic `[packet]` form used by the specification and command reference.

## Making Vision source alignment

The skill previously linked to the generic `/readings/making-vision` path, while the site now exposes separate V1 and V2 readings. The skill's processing/allocation distinctions align with V2, which explicitly separates candidate from object, promotion from attention, and promotion from recognition/persistence, and identifies internal state, needs, uncertainty, risk, and learned relevance as allocation variables. The skill and the repository's README/specification links now point to Making Vision V2. This is a source-alignment correction, not a claim that the Making Vision synthesis is an established biological mechanism.

## Viewpoint command gap

The `fv analyse` output contract in `commands.md` also omitted the required root-level `viewpoint.json` metadata already required by the skill, how-to guide, and current specification. The command reference now includes it, including TD viewpoint transitions for video.

The command descriptions also blurred source viewpoint records and editable render VPOs. The list/show operations can inspect both, but edits change the active/render pose and must preserve source `initial_state` as provenance. The skill and both command maps now state that boundary.

The authoritative specification permits explicit instantiation of `VPO_DEFAULT`, and the browser-editor documentation describes a dedicated **New render preset / Instantiate VPO_DEFAULT** action. However, the current `fv edit viewpoint` textarea subcommand list has no corresponding instantiate/create syntax. The skill and command reference now state this boundary explicitly: do not invent a command; use an explicitly available editor action or ask for clarification. The missing command form remains a design decision, not an implementation claim.

## Additional branch review

### `docs/zenodo-record-and-v026-summary`

This branch is one commit ahead and 85 behind current `main`. Its README contains a more expansive capability summary, but it also points to an obsolete `.docx` specification path and presents an older command list that omits rebuild/upgrade and viewpoint editing. Its content was reviewed but not imported wholesale; current `main` remains the base for this cleanup.

### Dataset and assembly implementation branches

- `work/fv-dataset-receipts-20261107`: 9 commits ahead, 2 behind; adds a dataset-intake workflow and collection/packaging scripts.
- `experiment/hst-single-visit-ngc3370`: 75 commits ahead, 6 behind; adds multiple source-intake and assembly workflows for HST and other datasets.
- `archive/fv-assemble-preservation-2026-11-07`: 12 commits ahead, 6 behind; adds selected assembly workflows and a preservation checkpoint.
- `chore/workbench-docs-and-audit` and `spec/prompt-only-compile-mode` are behind current `main` with no unique file changes in the comparison.

These are implementation/experiment branches, not documentation replacements. Their workflows and data receipts should be reviewed in the relevant later implementation/example phase. None was merged or cherry-picked.

## Divergent branch comparison — findings

### `fix/viewpoint-init-transition-scope`

This branch is divergent from current `main` (5 commits ahead, 25 behind at inspection). Its viewpoint schema is an earlier 90-line source-viewpoint-only form; current `main` has a 276-line schema that also defines reusable viewpoint objects (VPO), render roles, defaults, and coordinate-frame details. The branch also lacks the current maplet-grounded assembly expansion in the Working Process Specification and lacks newer provenance instructions in the skill. Do not cherry-pick or merge this branch as a whole.

### `feature/fv-audit-batch-clean` and `feature/fv-audit-batch`

Both are divergent from current `main`. The batch utility and batch-report schema match current `main` line-for-line in the inspected versions. The branch test file is shorter (90 lines versus 146 on `main`); current `main` adds batch-output-schema validation and invalid-report diagnostic tests. Current `main` also contains newer packet media provenance add-ons (attribution, organizations, contributions) that are not present in the branch version of the provenance document. These branches are not a better replacement for current `main`.

### General branch handling

The inspected divergences show why branch names and apparent feature intent are insufficient evidence for merging. Compare file content and current authority before considering individual changes. No branch content was merged or cherry-picked.

## Changes made in this audit pass

- Made the actual failure target explicit in the active skill and how-to guide: coherent but wrong scene models, not just object misclassification, with corresponding evidence and uncertainty safeguards.
- Added the unassigned consolidated-release-label clarification to the authoritative rebuild rule itself, not just the agent skill and operator guides.
- Added `fv rebuild` and `fv edit` to the canonical operation model and included optional rebuild/upgrade in the specification's normal downstream path.
- Traced the v0.25 edit-interface forms to merged PR #1 and aligned them across the authoritative operation model, active skill, and command reference. Recorded which v0.25 proposal details are superseded or MVP-specific; the standalone v0.25 history section remains a deliberate review item.
- Updated the image-analysis pipeline to show selective candidate promotion as additional processing, followed by evidence-grounded packet commitment; added the same distinction to per-frame skill instructions.
- Verified that the active skill's reduction from 1,590 to 622 lines reflects relocation of its embedded v0.24 extraction into `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md`; the historical specification body was checked against the original embedded text and retained.
- Disambiguated Making Vision candidate/object promotion (processing allocation) from FV packet commitment (evidence-supported entry into OI/TD); updated the specification, skill, commands, and how-to language.
- Corrected an over-restrictive rebuild-target caution: absent `--to`, the normative rule selects the current authoritative Working Process Specification itself. The report must describe its v0.24 base and later normative additions without inventing a consolidated release label; the missing label alone does not block migration.
- Added the mandatory Making Vision V2 prerequisite and candidate/promotion-versus-packet-commitment distinction to the how-to guide, matching the active skill.
- Completed an operational procedure cross-check against the canonical specification; expanded resolve/reconciliation state transitions and audit evidence/metric rules in the skill and command reference.
- Aligned command interpretation and artifact-output contracts across `commands.md`, `SKILL.md`, and `HOW_TO_USE.md`; documented rebuild/edit/viewpoint artifacts, video ZIP delivery, and the non-native batch-audit boundary.
- Added `docs/FV_ARTIFACT_CONTRACT_AUDIT_2026-11-11.md` and linked it from the README; it compares operation artifacts, confirmed schemas, and uncovered schema/command gaps.
- Added `docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md` and linked it from the README.
- Clarified that dispute resolution is conditional in the normal workflow diagrams; it is required only when a dispute or ambiguity blocks downstream work.
- Added `fv edit viewpoint` to the command-reference map.
- Added required `viewpoint.json` metadata to the `fv analyse` command output contract.
- Added an operation implementation/test status matrix, including the two browser editors, their limits, CI workflows, and pending agent-level acceptance.
- Added audio-enabled video requirements and selected-frame analysis guidance to the active skill, command reference, and how-to guide.
- Repaired audio subsection hierarchy, PC subsection order, chronological v0.9–v0.11 change-log order and heading level, snapshot subsection numbering, and final acceptance-test numbering in the current specification.
- Moved the `fv audit` command row into the `HOW_TO_USE.md` command-map table.
- Documented the missing textarea syntax for explicit `VPO_DEFAULT` instantiation without inventing a command.
- Clarified that viewpoint commands list/inspect source records but edit render VPO state only, preserving source `initial_state`.
- Updated the Making Vision links to V2 and separated processing allocation/promotion from evidence-based packet commitment.
- Added the Making Vision research-status boundary so the synthesis is not presented as an established biological mechanism.
- Marked the opening v0.24 temporal-analysis note in `HOW_TO_USE.md` as historical.
- Clarified the provenance/audit document's historical v0.24 origin and its current supplementary role.
- Clarified the Working Process Specification header's v0.24 base and later v0.26/v0.27 normative additions without inventing a consolidated release number.
- Normalized the skill's rebuild syntax to `[packet]`, made the examples use the implicit current-version target rather than the ambiguous literal `current`, and added the v0.27 rebuild workflow to the how-to guide.
- Added the optional rebuild/upgrade step to the README reconstruction path.
- Exposed `fv edit viewpoint` as a subcommand in the README command list.
- Reworded the skill's operating-rule paragraph so the current Working Process Specification is explicitly authoritative and its availability requirement is honest; clarified the same dependency in README and how-to guide.
- Relabelled the embedded v0.24 extraction as a historical snapshot/reference, not current operating authority.
- Preserved the historical v0.24 extraction verbatim in a separate specification reference, linked it from the README, and reduced the active skill from 1,601 to 561 lines at extraction; subsequent operational additions bring it to 597 lines.
- Removed a hard-coded v0.24 validation target from the active skill command and tied validation to the current authoritative specification and declared packet compatibility.

## Open work at documentation-phase checkpoint

The following items remain open or are deliberately deferred. Items already completed by the follow-up reviews below are not repeated here.

- **CI execution evidence:** no workflow run or combined status is recorded for `work/fv-docs-skill-cleanup-20261111`. The branch has no pull request. The browser workflow is triggered by relevant pull requests or manual dispatch; the audit/provenance workflow is triggered by pushes to `feature/fv-audit-batch`, relevant pull requests, or manual dispatch. A branch-specific Actions run lookup returned zero runs and the commit's combined status returned no status entries. No manual dispatch was performed. Treat CI as **unverified**, not passed.
- **Agent acceptance:** the operation definitions and implementation boundaries are documented, but agent-level acceptance remains pending where identified in `docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md`. Test-file presence is not evidence of a passing run.
- **Artifact schemas:** decide separately whether validation/rebuild reports and audio transcripts need dedicated schemas. The artifact-contract audit records the current gaps; no speculative schemas have been added.
- **Viewpoint command surface:** decide whether additional schema-supported VPO fields should receive standard text-command syntax or remain editor-only.
- **Consolidated release label:** the current authoritative specification remains a v0.24 base with later normative additions, including v0.26 and v0.27. The default rebuild target is correctly defined as the current authoritative specification itself; the absence of a consolidated numeric label does not block that operation. Decide on a release label only when a numbered consolidated release is needed. Do not infer v0.27 as the consolidated target.
- **Divergent implementation branches:** review unique branch content in the later implementation/dataset phase. The documentation pass records the branch comparisons but does not merge or cherry-pick them.
- **`fv investigate` question-directed media use:** resolved by including single-image/video questions and timestamped object/event findings in the existing investigation operation. No separate `fv query` command will be defined.
- **Examples:** the final examples phase is now underway; the targeted provenance, packaging, and cross-reference review is recorded below and in `PACKETS/examples/README.md`.

The operation-status inventory is complete as a documentation artifact and is maintained in `docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md`. Command syntax and cross-document consistency review is also complete for the defined operations; question-directed media analysis is included in `fv investigate`, not listed as a separate operation.


## Follow-up: v0.25 history continuity review

The baseline's open question about v0.25 has been investigated against the repository's commit history. The October 20, 2026 commit `7940131c` records the v0.25 design addition in `SKILL.md`, `README.md`, `HOW_TO_USE.md`, and supplementary AI-agent guidance. It defines the initial image-only `fv edit` interaction (list objects, list properties, identify a property edit), while leaving value-assignment syntax and several environment/edit-log/version-marker details open. The current Working Process Specification incorporates the core image-edit command convention in its command description; it does not contain a standalone v0.25 normative section.

The subsequent v0.26 addition is explicitly normative and builds on the v0.25 image-edit design. The how-to guide now labels the v0.25 material as a design addition, records which early proposals remained unstandardized, and separates the v0.26 environmental-response rules as the current normative contract. No missing v0.25 specification section has been invented. The historical continuity question is therefore resolved as a documentation-status clarification, not as a request to reconstruct a separate release specification.


## Follow-up: research grounding restored to the documentation path

A review of the active skill and canonical specification found that the Making Vision V2 architectural synthesis was prominent, but the empirical/theoretical research that motivates several FV procedures was not collected in an accessible research-to-design reference. Added `docs/FV_RESEARCH_FOUNDATIONS.md` to map peer-reviewed work on change blindness and visual monitoring, expertise-shaped visual sampling, border ownership and figure-ground organisation, component/shape cues, shadows, biological motion, and calibrated size anchoring to FV operating requirements. Sensory-regime adaptation is explicitly retained as a working hypothesis rather than a settled finding.

The active skill and how-to guide now identify the research map separately from Making Vision: the former summarises evidence and limits; the latter is the user's architectural synthesis. The README links the research reference. The Working Process Specification remains authoritative for FV packet and operation contracts. The new research map does not override it or claim that FV reproduces human neural mechanisms.


## Follow-up: command and operator-guide consistency pass

- Aligned the skill with the command reference's viewpoint-schema coverage boundary: orthographic poses require the schema's scale, coordinate-frame, and framing data; the current text console does not implement all schema fields.
- Clarified that published images/videos are analysed with `fv analyse`; `fv create` is for packets constructed from already established information or an explicit packet specification. Literature metadata and published interpretations remain distinct from direct visual evidence.
- Aligned the how-to analysis pipeline with the skill's candidate verification, entity/component/appearance decision, and supported identity-resolution gates before packet commitment.
- Corrected the how-to heading to match its five listed correctness dimensions.
- Added the textual `fv` prefix/activation rule to the skill to match the command reference.

The 12 defined operations remain aligned across `SKILL.md`, `commands.md`, and `HOW_TO_USE.md`. Question-directed analysis of supplied media is documented under `fv investigate`; no separate `fv query` command is defined.

## Follow-up: final cross-document verification

The final operator/agent documentation pass checked the README, active skill, command reference, how-to guide, current Working Process Specification, artifact-contract audit, operation-status matrix, and research-foundations reference on the working branch.

- Corrected the active skill's downstream command sequence to include optional `fv rebuild` / `fv upgrade` before conditional dispute resolution and validation. This brings its sequence into line with the README, command reference, how-to guide, and authoritative specification. Rebuild remains a separately requested migration, not an automatic step.
- Rechecked 18 internal Markdown link references across the eight primary documentation files; all 10 unique internal target paths resolve on the working branch.
- Recounted the automated test definitions in the inspected files: 22 Playwright tests (4 viewpoint editor, 11 environment workbench, 7 media object editor) and 14 Python unit tests (9 audit-batch, 5 provenance-schema). This verifies the inventory counts only; no tests were run and no pass is claimed.
- Rechecked the operation-status matrix against its test inventory and workflow descriptions. It continues to distinguish specified agent operations, bounded browser prototypes, offline audit aggregation, and pending agent-level acceptance.
- Rechecked the normal reconstruction path and terminology across the five principal operational documents. The optional rebuild stage and the distinction between candidate promotion and evidence-supported packet commitment are represented consistently.
- No example packet, test implementation, schema, or runtime code was changed in this follow-up.

CI remains unverified: the branch has no pull request, the branch-specific Actions lookup returned no workflow runs, and no manual dispatch was performed. Test definitions and local documentation checks must not be described as executed CI.


## Follow-up: question-directed media investigation

The discussion of a possible `fv query` command is resolved. The intended behaviour is ordinary investigation of a specified object or question in supplied media: for example, whether a white dog appears in an image, whether a delivery person appeared during a CCTV coverage period, or what a kitten did in a video and when. This belongs to `fv investigate`, including single-source image/video investigations as well as investigations across multiple observations.

The investigator returns the finding directly, with relevant timestamps/intervals and evidence references where applicable. It uses TIR for retained investigative reasoning and TD for authoritative temporal evidence; users do not need to open TD files to obtain ordinary findings. Coverage gaps and uncertainty must be stated, and absence must not be asserted without adequate coverage. Temporal queryability remains a packet capability and acceptance test, not a separate user-facing command. The command map, skill, how-to guide, implementation-status inventory, and current specification have been aligned to this decision. No example files were changed.


## Follow-up: final examples audit and cleanup

The examples phase was kept until the end, after the documentation, skill, command-reference, and `fv investigate` scope work. The review has now:

- Added `PACKETS/examples/README.md` as a directory-level index distinguishing reconstruction briefs, source-media analysis, sampled evidence, metadata-only examples, and incomplete/illustrative packets.
- Updated `PACKETS/README.md` to link the index and to describe the offline audit-batch utility accurately.
- Compared Git blob hashes and removed 38 byte-identical suffixed packaging copies from the Cat-jumping and KITTI merged-building folders. Removed the byte-identical `TIR_MERGED_UNIFIED.json` alias from the CCTV Storage Crisis merged folder; canonical `TIR.json` remains. Shared version/provenance boilerplate repeated across distinct environmental packets and the reused operational-disposition note in separate CCTV packet folders were retained.
- Corrected the viewpoint sample to include the required `initial_state.status` with an explicit unknown source pose.
- Corrected example READMEs where source availability, processing, or validation had been overstated: CCTV Storage Crisis, KITTI assembly, Mayan LiDAR, Hubble UDF, Cat jumping backwards, and CCTV Part 1. Added a family README for CCTV Storage Crisis and an audit README for the incomplete KITTI global-building merge.
- Recorded that the Cat post-resolution validation report claims snapshot folders exist even though the repository contains only a manifest that says no snapshots were preserved; the reconciliation record also says post-resolution validation was still pending. The report is retained as inconsistent historical output, not accepted as proof of validation.
- Recorded and corrected an OI/MSRM gap in Hubble UDF (the galaxy-cluster entity is now listed in the MSRM scene), a then-open seven-entity OI/MSRM gap in CCTV Part 3 (subsequently corrected in the follow-up audit below), and the unverified Mayan “expected staircase”, since removed from the observed component inventory and retained only as an expected-component candidate. The KITTI global-building merge declares 54 identities but explicitly records only 12.
- Checked the five image examples' source-page author/licence statements against their Wikimedia Commons pages and cross-checked OI/MSRM references: all five checked inventories have matching entity references and no duplicate IDs.

These checks are targeted, not a full FV semantic validation. No exhaustive pixel-level re-analysis, full reproduction of LiDAR/telescope processing, or full validation of every example packet was performed. Missing source media and unverified claims remain clearly labelled rather than repaired by invention. No runtime or test code was changed, no tests/CI were run, and no merge was performed.


## Follow-up: deeper example structure and evidence audit

The first examples pass was followed by cross-file consistency checks on the environmental edit pairs, CCTV packet families, and reconstruction-target examples.

- Environmental edit pairs: checked OI IDs against MSRM object keys in all seven packet states. Restored the lighthouse to the active Bermuda edit, which had dropped an unchanged baseline entity. Aligned the cat's behaviour descriptions with the single locations recorded in MSRM. Flagged the Wall Cat vegetation as an unresolved cross-state inventory issue: it appears in the rainy edit but not the pleasant baseline, and the withheld source images prevent determining whether it was omitted from the baseline or newly introduced. Clarified that Windy Day is a mixed edit: the person's state changes while the dog remains unchanged under the legacy v0.25 treatment.
- Trip to the Moon: added the missing explicit MSRM relations for Astronomer 03 in S02 and the declared scene backgrounds in S03/S06. Confirmed that the capsule's lack of an on-screen relation in S04/S05 is intentional because OI explicitly marks it off-screen but persistent.
- Hubble UDF: added the declared galaxy-cluster entity to the MSRM scene; the OI/MSRM cross-reference now matches. This does not verify the absent source exposures or the 10,000-galaxy claim.
- Mayan assembly: removed the west-facing staircase from the observed OI component list because it was only an expected feature and no source evidence established it as present; retained it as an unverified expected-component candidate.
- Mayan global merge: added all 12 OI sample identities to MSRM, qualified the legacy high-correspondence claims as unverified, and documented that typed totals account for 6,000 of the claimed 61,000 structures; 55,000 remain uncategorized in the packet.
- KITTI global-building merge: the 12 global records cite component-level building IDs under source cluster objects, but neither source OI declares those components (Sequence 00 has an empty component list; Sequence 07 has no component list). This source-provenance gap is now explicit in the example README.
- Old MacDonald: made all OI-declared persistent farm landmarks explicit in MSRM across scenes 02–05 and restored the farmer's scene_04 placement. A targeted cross-check now finds exact OI/MSRM object-set matches in all five scenes (6, 7, 8, 9, and 9 objects respectively). The generated MP4 remains unaudited.
- CCTV Snapshot TD experiment: checked that all manifest-declared snapshot/crop/file paths resolve. Corrected Part 1's README and validation report to match its current two deferred/non-blocking dispute records; corrected Part 3's wording to distinguish one deferred record from two active investigations. Documented that Part 2 has no retained TIR/PC/dispute files even though the process log describes targeted manual review. Recorded the parent-source interval/duration discrepancies in Parts 2 and 3; exact boundary reconciliation remains open.
- CCTV Storage Crisis legacy family: normalized abbreviated packet-scoped references in merged OI/TIR to the full IDs in the three part inventories; changed the unsupported personal name “Officer Ramos” to a role-level candidate label; qualified cross-part confidence and continuity claims as unverified; corrected bitrate arithmetic (10 Mbps = 108 GB/day and 5 Mbps = 54 GB/day per camera, decimal units); and removed the implied claim that metadata-only packet size is an evidence-equivalent replacement for source video. A targeted cross-reference check now resolves all 12 merged OI/TIR part references to the three part inventories.
- Corrected the KITTI landscape visualization README, which listed two files no longer present in the folder.

These remain targeted structural/documentation checks. The Wall Cat cross-state vegetation question, inventory completeness and visual correctness in CCTV Part 3 (its seven missing MSRM references have since been restored), KITTI global-building inventory gap, Mayan global-merge uncategorized count, source provenance gaps, and all claims requiring unavailable raw media remain unresolved. No authoritative FV semantic validator, exhaustive visual audit, or test/CI run was performed.


## Follow-up: final example cross-reference and asset-inventory pass

- CCTV Part 3: restored the seven OI candidates OBJ-013 through OBJ-019 to the appropriate MSRM scenes using only their recorded OI time ranges and spatial summaries. A fresh cross-reference check now finds all 19 OI IDs represented in MSRM, with no unknown IDs. Updated the packet README, family README, examples index and structural review report. Two active investigations remain; merge gate remains blocked.
- Mayan assembly: removed the west-facing staircase from the observed component list because the record itself labelled it an expected component and no retained source evidence established it as present. It remains an unverified expected-component candidate. Corrected the visualization README and packet README: the workflow image previously listed is absent; the visualizations folder contains only its README.
- Cat Jump: corrected the former post-resolution validation report. It had claimed snapshot directories existed, but the repository tree and manifest show that no snapshots were retained. The corrected report records PARTIAL status, notes that no TIR.json is present, and preserves the narrower fact that the human accepted metadata-only compilation for this experiment. The examples index now reflects that correction.
- Five still-image packets: checked OI/MSRM entity references; all five inventories match their spatial records (15, 14, 16, 14 and 10 IDs respectively). This remains a structural check, not pixel-level re-analysis.
- KITTI Sequence 00 landscape and Sequence 07 assembly packets: checked OI/MSRM references; both four-entity inventories match their single scene records. Their source scans, calibration/pose inputs and reproducible registration logs remain absent.

No source-dependent uncertainty was silently resolved. No authoritative FV semantic validator, exhaustive visual audit, or test/CI run was performed.


- KITTI global-building merge: added two explicit open disputes for the 54-vs-12 inventory mismatch and source-component provenance that does not resolve to records in the two source OIs. The legacy compiled-spec draft is constrained to the 12 represented identities; the other 42 are retained only as an unverified legacy count and cannot be rendered as invented entities. Merge gate is BLOCKED.
- Mayan global merge: added two explicit open disputes for the 55,000 uncategorized remainder and absent source-flight/contributing-packet correspondence evidence. Merge gate is BLOCKED.
- Hubble HUDF assembly: qualified the legacy 800-exposure/10,000-galaxy timeline and registration claims as unverified, and added two open disputes for missing reproducible exposure provenance and unsupported astronomical inventory/count claims. The acceptance gate is BLOCKED (not labelled a merge gate because this is an assembly example).
- CCTV Part 2: independently checked its manifest against the repository tree. All 106 declared full-frame snapshots and all eight declared crops exist; all crop source-frame references resolve. Its missing PC/TIR/dispute records remain explicit in the packet README and were not fabricated during this pass.
- Reconstruction briefs: A Trip to the Moon's MSRM relations resolve all on-screen OI scene members; the capsule's absence from S04/S05 spatial relations is intentional because OI marks it off-screen but persistent. Old MacDonald's OI/MSRM placements match across all five scenes, including persistent landmarks and the farmer in S04.

- Structured inventory flags added to the KITTI and Mayan merged OI files: KITTI records 12 represented identities against a legacy declared 54 (42 unrepresented); Mayan records 12 sampled identities, 6,000 typed aggregate structures and a 55,000 uncategorized remainder. These fields make the gap machine-readable without fabricating records.


- CCTV Storage Crisis example family: all three part packets now have explicit open provenance/correspondence disputes and BLOCKED analysis gates. Their OIs are labelled unverified legacy candidates; their TDs are non-authoritative; TIR observations/hypotheses are marked unverified; unsupported personal names were removed from TIR. The merged packet has three open disputes and a BLOCKED merge gate; four global IDs remain uncommitted candidates, merged TD is non-authoritative, and the compiled-spec draft is not approved as a render target. The historical 10,000x storage-reduction claim remains withdrawn as non-evidence-equivalent.
- Environmental edit pairs: resolved Bermuda baseline cat-position ambiguity using the paired edit log as the authored basis (on the chair), aligned baseline OI/MSRM, and made the active edit's base packet explicit. Wall Cat rainy edit now has an open cross-state vegetation-inventory dispute and a blocked-pending-source-review gate; the submitted PASS is explicitly unverified. Image source/licence gaps remain open for all seven assets.
- KITTI Odometry Sequence 00 assembled landscape: added two open disputes for exact source acquisition/registration reproducibility and the unresolved dynamic-car registration conflict; assembly gate BLOCKED_FOR_REPRODUCTION. OI/TD/MSRM now qualify legacy registration claims as unverified.
- KITTI Odometry Sequence 07: added an open source/registration reproducibility dispute and qualified the scan count, coverage, calibration and filtering claims. Assembly gate BLOCKED_FOR_REPRODUCTION.
- Mayan LiDAR stitching: added two open disputes for absent flight-line/processing evidence and unsupported archaeological classification; corrected the former VALID report to BLOCKED_UNVERIFIED and blocked the compiled-spec draft. Assembly gate BLOCKED_FOR_REPRODUCTION.
- CCTV Snapshot TD Reconstruction Part 2: added three explicit open investigations for pedestrian correspondence, camera-view transitions and one-second sampling coverage. The README/index now correctly states there is no PC.json or persistent TIR.json; dispute.json is present and the merge gate is blocked. No TIR was fabricated from the README/TD.
- Re-audited all 15 example dispute.json files after these changes: no remaining status=none entries. Deferred/non-blocking issues in CCTV Parts 1 and 3 and the human-resolved metadata-only Cat-jumping experiment remain explicitly distinguished from active disputes.

- KITTI Sequence 00 assembled-landscape snapshot manifest: removed two stale references to an absent assembled-map PNG and absent craft-project HTML. The manifest now explicitly records that no snapshot objects are retained in that packet folder; separate visualization assets remain illustrative only.
- CCTV Snapshot Reconstruction Part 2: added three open dispute records for pedestrian correspondence, view-change mechanism and one-second sampling coverage. README and family index no longer describe the packet as having no disputes; absence of PC/TIR is still disclosed.
- KITTI and Mayan merged LiDAR MSRM/TD records now carry the same blocked/unverified status as their OI, dispute and compiled-spec records, rather than leaving legacy global totals or merge-step actions looking like committed results.

- PACKETS/META_EXAMPLES_CATALOG.md synchronized with the latest packet audit: Mayan stitching VALID claim withdrawn; Hubble OI/MSRM cross-reference correction acknowledged; KITTI snapshot manifest correction recorded; CCTV Storage Crisis gates and Cat-jumping human-acceptance closure clarified.
- CCTV Storage Crisis Part 1–3 MSRM records now mark scene/spatial/camera claims as unverified, consistent with their OI/TIR/TD evidence limitations. The CCTV Snapshot experiment process log now acknowledges the Part 2 dispute file while preserving the absence of a persistent TIR/PC.
- Reviewed all 15 example dispute.json files: none has status=none. CCTV Part 1's and Part 3's chunk-local deferred items and Cat-jumping's human acceptance with limitations remain distinct from active unresolved disputes.
- Reviewed all 14 example snapshot manifests against the repository tree. The only unresolved path is the KITTI Sequence 00 legacy assembled-map reference, which is explicitly classified in the manifest as not present and withdrawn; no active manifest claim remains that it is a retained snapshot.

- KITTI Sequence 00, KITTI Sequence 07 and Mayan stitching PC records no longer present unverified calibration/sensor/flight parameters as committed constants. Those values are retained as explicitly unverified legacy input claims; PC.constants is empty until exact acquisition-specific inputs are retained.
- KITTI merged-building PC now clarifies that no source-derived snapshot assets are retained; its snapshot manifest is only a packet-ID marker.
- CCTV Storage Crisis merged PC no longer asserts a fixed unmoving camera as a verified invariant; it records that statement as an unverified legacy assumption.
- Cat-jumping dispute closure note now distinguishes human acceptance of limitations from factual resolution of the visual/background/timing questions.
- CCTV experiment process log corrected to reflect Part 2's newly added dispute.json while retaining the explicit absence of PC.json and persistent TIR.json.

- Mayan stitching MSRM now marks coordinate system, registration method, coverage, point-level provenance and spatial relationships as unverified legacy claims; KITTI Sequence 00/07 MSRM coordinate-system/origin claims are likewise qualified. KITTI Sequence 00's moving-car handling is explicitly a proposed rule, not a verified filter result.

- Rechecked the five source-image packet inventories against their MSRM references: blue_chairs (15/15), desk_with_objects (14/14), kitchen_interior_design (16/16), restaurant_kitchen (14/14), small_room_interior (10/10). No missing/extra IDs or duplicate OI canonical IDs were found in these five structural comparisons.

- Rechecked SKILL.md, commands.md, HOW_TO_USE.md, README.md and the authoritative specification for the resolved query-command decision. All define question-directed source-media analysis under fv investigate, including still-image presence questions, video event/timing questions, adaptive sampling, coverage limits, evidence-grounded answers and TIR preservation. No separate fv query command is listed. TD temporal queryability remains a packet capability/acceptance test, not a user-facing command.
- Re-read all 376 lines of commands.md against SKILL.md and the specification. Its operation map, inputs/outputs, command boundaries, migration rules, viewpoint syntax limits, validation/compile gates and audit contract are internally consistent; no further command-reference edit was needed in this pass.
- FV_OPERATION_IMPLEMENTATION_STATUS now points readers to the separately completed examples audit rather than implying that example cleanup remains pending.
