# Auditable Prompt Generator — TODO

**Status:** Proposal / not implemented  
**Scope:** A standalone, repository-independent prompt-generation utility. This is not an FV runtime subsystem.

## Problem

The FV repository keeps accumulating packets, specifications, schemas, examples, fixtures, skills, and working instructions. Tests and agent tasks increasingly fail because the prompt that launches them does not carry all the context they depend on.

Typical failure modes include:

- A prompt refers to a skill or specification without supplying its path or contents.
- A task assumes that an agent already knows a convention established elsewhere.
- Required dependencies are omitted when a test is copied into a fresh session.
- A prompt relies on conversation history or repository access that the receiving agent does not have.
- Someone has to manually maintain and paste an ever-growing list of supporting files.

The goal is to reduce these failures without introducing an opaque component that silently decides what an agent should know.

## Goal

Create a **standalone prompt generator** that packages a task and its declared source material into a complete, portable, inspectable prompt.

The generated prompt must be usable in a fresh AI session, without relying on hidden conversation context, implicit repository access, or undocumented context injection.

This should be useful beyond FV: tests and tasks from AEL, Memory Prism, software projects, and other agent workflows should be able to use the same generator.

## Core design principle

**No hidden context. No silent selection. No magic.**

The generator may discover and assemble material, but its selection rules and every inclusion must be visible and reviewable. It must not silently decide that a potentially relevant document is irrelevant, rewrite the task's intent, or invent missing instructions.

The generated prompt itself is the primary audit artifact.

## Proposed inputs

- **Source location:** a repository or a specifically selected directory (for example, FV's `PACKETS/`).
- **Entry point:** the task, test, or prompt template to be run.
- **Explicit selections:** files, directories, or other source material the requester requires.
- **Task instructions:** the operation to perform, constraints, expected behavior, and output requirements.
- **Dependency rules:** references or declarations that identify additional required material.
- **Optional supporting material:** material that may be included but is not required.

The generator should support both:
1. **Template-driven use:** the requester specifies the content and structure to include.
2. **Reference-driven use:** the requester supplies files or references, and the generator expands their declared dependencies.

Whether these are two modes of one interface or separate entry points remains to be decided.

## Dependency and inclusion handling

Every included source must be classified and reported as one of:

- **Explicitly required** — directly selected or required by the task.
- **Dependency-expanded** — included because an explicit source refers to it or declares it as a dependency.
- **Optional supporting material** — included by an explicit selection or rule, but not required.
- **Unresolved reference** — referenced material that could not be located or included.

The generator must:

- Resolve declared references and dependencies using documented, inspectable rules.
- Preserve the reason each file was included and the chain of references that led to it.
- Report missing, ambiguous, inaccessible, or conflicting references.
- Avoid silently treating unresolved references as satisfied.
- Avoid silently excluding material that appears relevant.
- Make exclusions visible when selection rules or user choices exclude candidate material.
- Detect and handle dependency cycles.
- Distinguish source files from generated output and avoid recursively ingesting its own output.

## Required outputs

### 1. Expanded standalone prompt

A complete prompt containing the task instructions and the actual contents of all included source material—not merely file paths that may be inaccessible to the receiving agent.

The prompt must:

- State the task and expected output clearly.
- Include the relevant instructions, specifications, constraints, and supporting material.
- Preserve source identity and provenance.
- Preserve uncertainty, caveats, and distinctions present in source material.
- Clearly mark unresolved references and other known gaps.
- Be portable: it should work when copied into a separate AI session.

### 2. Inclusion and audit report

A human-readable report listing:

- Every source included.
- Its classification (explicit, dependency-expanded, or optional).
- Why it was included.
- The reference/dependency chain, where applicable.
- Sources considered but excluded, and the rule or decision responsible.
- Missing, ambiguous, inaccessible, or conflicting references.
- Any limits or warnings affecting completeness.

### 3. Source manifest

A machine-readable record of the inputs used to generate the prompt, including source paths/identifiers and version information such as commit or content hashes where available.

The manifest should make it possible to identify exactly which source state produced a given prompt.

## Auditability and reproducibility requirements

- **Inspectable selection:** inclusion and exclusion rules must be documented and reviewable.
- **No silent invention:** missing information stays missing and is reported.
- **No hidden context:** the output cannot depend on unreported conversation history or implicit access to files.
- **No lossy compression by default:** do not summarize away evidence, provenance, object identity, uncertainty, or constraints. Any requested transformation or summarization must be explicit and disclosed.
- **Reproducible generation:** identical inputs, source versions, and generator version should produce equivalent output, apart from explicitly declared variable metadata.
- **Traceability:** every assembled section should be traceable to its source.
- **Portable output:** the prompt must remain usable outside the repository and outside the session that generated it.

## Non-goals

The generator is not intended to:

- Become another FV editor or packet processor.
- Perform visual perception, scene interpretation, or reconstruction.
- Execute the generated prompt or run the task itself.
- Decide what a test ought to do or alter its intended behavior.
- Replace source specifications, skills, tests, or repository documentation.
- Act as an opaque intelligent hydrator whose internal context choices cannot be inspected.

Its responsibility ends when it has generated the prompt package and its audit information.

## TODO / implementation sequence

- [ ] Define the minimal input format for task templates, explicit source selections, and dependency declarations.
- [ ] Define supported reference forms and the exact dependency-expansion rules.
- [ ] Decide how template-driven and reference-driven use fit into the interface.
- [ ] Define inclusion classifications, exclusion reporting, and unresolved-reference behavior.
- [ ] Define cycle detection and duplicate-source handling.
- [ ] Define how source versions and content hashes are captured in the manifest.
- [ ] Specify deterministic assembly and stable ordering of included material.
- [ ] Define how binary, oversized, generated, or otherwise non-embeddable files are represented and reported.
- [ ] Produce a sample expanded prompt and audit report from a real FV test.
- [ ] Test the output in a fresh AI session with no access to the originating conversation or repository.
- [ ] Verify that deliberately missing dependencies are reported rather than silently ignored.
- [ ] Verify that the generated prompt can be audited against its source manifest and inclusion report.
- [ ] Consider reuse for AEL, Memory Prism, and non-FV software tasks after the FV example establishes the basic contract.

## First implementation target

Use one existing FV test that currently depends on context being supplied informally. Generate a fully expanded prompt package for that test and inspect it manually.

Do not begin by ingesting the entire repository. Start from an explicit task entry point, expand only declared dependencies, and make every expansion visible. The growing size of `PACKETS/` is the reason to make dependency handling explicit—not a reason to dump the whole directory into every prompt.

## Open design questions

- Should dependency declarations live in each source document, in a separate manifest, or support both?
- Should the generator stop on unresolved required references, or produce a clearly marked incomplete prompt as an option?
- What size limits and file types should be supported for embedded source content?
- Should the audit report be embedded in the prompt, emitted beside it, or both?
