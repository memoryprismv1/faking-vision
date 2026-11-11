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
6. **The documentation set repeated substantial process material.** The skill originally embedded a 1,055-line historical v0.24 specification snapshot alongside active instructions. The snapshot has now been moved verbatim into `SPECIFICATION/FV_Working_Process_Specification_v0.24_Historical.md`; `SKILL.md` retains a short historical-reference pointer. The active skill is now 561 lines, while the historical source remains preserved separately.

### Medium priority

7. **README initially listed `fv rebuild` and `fv upgrade` as separate commands**, while the skill and command reference define upgrade as an alias. The README now labels `fv upgrade` as an alias.
8. **The Working Process Specification contains legacy version/change-log material and later sections whose numbering/order is not strictly sequential.** Preserve historical content; improve navigation rather than renumbering or deleting without a separate review.
9. **The command interface is an AI-agent textarea interface, not a standalone FV CLI.** This distinction is already stated in `commands.md` and `HOW_TO_USE.md`; retain it prominently and avoid describing these commands as executable shell commands.
10. **`fv audit batch` is not an implemented skill command.** The offline Python batch aggregation utility, JSON schema, tests, and workflow exist; the agent-level command remains proposed pending reliable skill-runtime invocation.
11. **No `fv query` command is currently defined.** The specification defines temporal queryability through TD and includes temporal-query acceptance tests, but it does not define a general-purpose `fv query` operation or syntax.
12. **The normal workflow diagrams implied that `resolve` was always required**, although the accompanying prose made it conditional on a blocking dispute or ambiguity. The README, command reference, how-to guide, and current specification now label it `resolve if required`.
13. **The viewpoint command descriptions blurred source viewpoint records and render VPOs.** They now distinguish inspection of both from editing render-preset pose/state while preserving source `initial_state`.
14. **The `fv analyse` command output contract omitted required `viewpoint.json` metadata.** The command reference now includes source-supported viewpoint initialisation and video viewpoint transitions in TD.

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

- Added `docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md` and linked it from the README.
- Clarified that dispute resolution is conditional in the normal workflow diagrams; it is required only when a dispute or ambiguity blocks downstream work.
- Added `fv edit viewpoint` to the command-reference map.
- Added required `viewpoint.json` metadata to the `fv analyse` command output contract.
- Added an operation implementation/test status matrix, including the two browser editors, their limits, CI workflows, and pending agent-level acceptance.
- Moved the `fv audit` command row into the `HOW_TO_USE.md` command-map table.
- Documented the missing textarea syntax for explicit `VPO_DEFAULT` instantiation without inventing a command.
- Clarified that viewpoint commands list/inspect source records but edit render VPO state only, preserving source `initial_state`.
- Updated the Making Vision links to V2 and separated processing allocation/promotion from evidence-based packet commitment.
- Added the Making Vision research-status boundary so the synthesis is not presented as an established biological mechanism.
- Marked the opening v0.24 temporal-analysis note in `HOW_TO_USE.md` as historical.
- Clarified the provenance/audit document's historical v0.24 origin and its current supplementary role.
- Clarified the Working Process Specification header's v0.24 base and later v0.26/v0.27 normative additions without inventing a consolidated release number.
- Normalized the skill's rebuild syntax to `[packet]` and added the v0.27 rebuild workflow to the how-to guide.
- Added the optional rebuild/upgrade step to the README reconstruction path.
- Exposed `fv edit viewpoint` as a subcommand in the README command list.
- Reworded the skill's operating-rule paragraph so the current Working Process Specification is explicitly authoritative and its availability requirement is honest.
- Relabelled the embedded v0.24 extraction as a historical snapshot/reference, not current operating authority.
- Preserved the historical v0.24 extraction verbatim in a separate specification reference, linked it from the README, and reduced the active skill from 1,601 to 561 lines.
- Removed a hard-coded v0.24 validation target from the active skill command and tied validation to the current authoritative specification and declared packet compatibility.

## Open work

- Decide the consolidated target-version label used by default `fv rebuild` after reviewing the base v0.24 text and later normative additions.
- Inspect skill/specification duplication and identify safe consolidation boundaries without losing the unfamiliar-AI acceptance procedure.
- Continue reviewing the unique content of relevant divergent branches against current `main`; do not merge.
- Continue reviewing command syntax, inputs, outputs, and constraints across skill/reference/how-to-use.
- Verify CI using existing run evidence or a controlled test run on this working branch.
- Review the status of every operation: specified, implemented in a tool, experimentally demonstrated, or still conceptual. An initial evidence-based status matrix is now in `docs/FV_OPERATION_IMPLEMENTATION_STATUS_2026-11-11.md`.
- Discuss `fv query` separately before defining or implementing it.
- Leave examples untouched until the final phase.
