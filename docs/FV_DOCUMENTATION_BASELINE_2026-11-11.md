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
| `README.md` | Includes rebuild and upgrade as separate list entries; upgrade is an alias |

Finding: viewpoint editing is documented under `fv edit` in `commands.md`, but is absent from its command map. This makes the command discoverability inconsistent even though the detailed syntax exists.

## Findings

### High priority

1. **Historical specification embedded in the skill is not clearly separated from current instructions.** The skill's operating-rule paragraph described it as containing the "complete v0.24 FV operating material", then labelled the appended extraction "complete authoritative source". Meanwhile, current viewpoint instructions explicitly supersede older v0.24 wording. This creates an avoidable authority ambiguity for an unfamiliar agent.
2. **Command reference map omits the explicit viewpoint subcommand.** Detailed syntax exists later in the same file, but the top-level command map does not expose it.
3. **The documentation set repeats substantial process material.** The 1,590-line skill contains a 129,507-character historical specification extraction, while the current authoritative specification is maintained separately. This is a maintainability and drift risk; the historical content should be clearly marked, not silently treated as current policy.

### Medium priority

4. **README lists `fv rebuild` and `fv upgrade` as separate commands**, while the skill and command reference define upgrade as an alias. The README should make the relationship explicit.
5. **The Working Process Specification contains legacy version/change-log material and later sections whose numbering/order is not strictly sequential.** Preserve historical content; improve navigation rather than renumbering or deleting without a separate review.
6. **The command interface is an AI-agent textarea interface, not a standalone FV CLI.** This distinction is already stated in `commands.md` and `HOW_TO_USE.md`; retain it prominently and avoid describing these commands as executable shell commands.
7. **`fv audit batch` is not an implemented skill command.** The offline Python batch aggregation utility, JSON schema, tests, and workflow exist; the agent-level command remains proposed pending reliable skill-runtime invocation.
8. **No `fv query` command is currently defined in the command map.** Temporal queryability is discussed in the specification and examples, but this does not establish a general-purpose query command.

## Existing support implementation (not a CLI claim)

- `TOOLS/fv_audit_batch.py`
- `TOOLS/test_fv_audit_batch.py`
- `TOOLS/requirements.txt`
- `SPECIFICATION/FV_Audit_Report_Schema.json`
- `SPECIFICATION/FV_Audit_Batch_Report_Schema.json`
- `.github/workflows/fv-audit-batch.yml`

The workflow file currently runs on pushes to `feature/fv-audit-batch`, relevant pull requests, and manual dispatch. The latest `main` commit inspected (6d47e1f) returned no associated workflow runs through the available commit-run lookup. This is not evidence that the tests pass or fail; execution status remains unverified.

## Branch review notes

The repository has multiple active and historical branches. Comparisons against `main` show that several branches are divergent, not simple descendants. In particular, the batch-clean, viewpoint-scope, skill-status, dataset-intake, and assembly experiment branches contain unique commits. They must be reviewed as evidence, not merged automatically.

No branch has been merged as part of this work. The working branch was created from `main`.

## Changes made in this audit pass

- Added `fv edit viewpoint` to the command-reference map.
- Reworded the skill's operating-rule paragraph so the current Working Process Specification is explicitly authoritative.
- Relabelled the embedded v0.24 extraction as a historical snapshot/reference, not current operating authority.

## Open work

- Reconcile README command labels and alias wording.
- Inspect skill/specification duplication and identify safe consolidation boundaries without losing the unfamiliar-AI acceptance procedure.
- Compare the unique content of relevant divergent branches against current `main`; do not merge.
- Review command syntax, inputs, outputs, and constraints across skill/reference/how-to-use.
- Verify CI using existing run evidence or a controlled test run on this working branch.
- Review the status of every operation: specified, implemented in a tool, experimentally demonstrated, or still conceptual.
- Discuss `fv query` separately before defining or implementing it.
- Leave examples untouched until the final phase.
