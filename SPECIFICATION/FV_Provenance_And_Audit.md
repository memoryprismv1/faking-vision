# FV Provenance, Independent Audit and Audit Files

This document defines the additive provenance record and machine-readable audit output. It extends FV v0.24 without invalidating existing packets or changing OI, MSRM, TD, PC, or dispute semantics.

## 1. Packet provenance

Newly generated FV packets MUST include a root-level `packet_provenance.json`. This is a separate metadata file; it does not alter the structure or meaning of OI.json, MSRM.json, TD.json, PC.json, or dispute.json.

Validate it against `FV_Packet_Provenance_Schema.json`.

The record distinguishes:

- `packet_generator`: the agent/process that produced this FV packet.
- `media.media_generator`: the agent/process that generated the media being analysed, when known.
- The model is not the agent. Preserve both identities independently.

The packet generator record carries `agent_id`, `model_provider`, `model_name`, `model_version`, `run_id`, `generated_at`, and `identity_source`. Use a stable agent identifier, not a display name where a stable identifier exists. Use UTC ISO 8601 timestamps.

The media record carries a media identifier, SHA-256 when calculable, media type, media-generator record, and any embedded provenance observations (for example, C2PA Content Credentials). Embedded credentials are evidence about the media claim; they do not automatically identify the orchestrating agent or prove depicted content is true.

Unknown means unknown. Do not infer an agent, model version, run ID, or generation time from visual appearance, filename, or model familiarity. Null is permitted for unavailable values. Set `identity_source` to `unknown` when no supported identity source exists.

### 1.1 Backward compatibility

- Existing v0.24 packets without `packet_provenance.json` remain valid under the legacy compatibility path.
- Missing provenance in a legacy packet MUST be represented downstream as `legacy_missing` / unknown, not treated as a packet validation failure.
- Newly generated packets MUST include the provenance file, even when some values are unknown.
- Do not rewrite old packets merely to add guessed provenance.
- The provenance file is additive and does not require changes to existing packet JSON structures.

Example:

```json
{
  "schema_version": "1.0",
  "packet_id": "PKT-EXAMPLE-001",
  "fv_spec_version": "0.24",
  "packet_generator": {
    "agent_id": "agent:example/visual-analyst",
    "model_provider": "Example Provider",
    "model_name": "Example Model",
    "model_version": null,
    "run_id": "run-2026-11-01-001",
    "generated_at": "2026-11-01T06:00:00Z",
    "identity_source": "execution_record"
  },
  "media": {
    "media_id": "media:sha256:...",
    "media_type": "video",
    "sha256": null,
    "media_generator": {
      "agent_id": null,
      "model_provider": "Example Provider",
      "model_name": "Example Video Model",
      "model_version": null,
      "run_id": null,
      "generated_at": "2026-11-01T05:50:00Z",
      "identity_source": "agent_declaration"
    },
    "embedded_provenance": [
      {
        "format": "C2PA",
        "validation_status": "unverified",
        "issuer": null,
        "model_claim": null,
        "generated_at": null,
        "claim_reference": null
      }
    ]
  }
}
```

The example values are illustrative. Do not copy them into real packets.

## 2. Independent audit inputs and comparison

The audit comparison is packet-to-packet:

1. The original/expected FV packet describes what the reconstruction was required to preserve.
2. The generated image/video is independently analysed into a generated-media FV packet. This analysis must not use the expected packet as evidence for what is visible in the generated media.
3. The auditor compares the expected packet with the generated-media packet.
4. The generated media remains available as evidence for inspecting and locating deviations.

The generated-media packet's `packet_generator` identifies the analyst that created that packet. Its `media.media_generator` identifies the system that generated the media, if supported by metadata or an execution record. These are separate from the auditor identity recorded in the report.

Do not use the reconstruction generator's explanation as evidence. Do not rewrite either packet during audit.

## 3. Downloadable JSON audit report

Every `fv audit` MUST produce a downloadable JSON file when file creation is available. The JSON is the primary audit artifact; a human-readable summary is supplementary. Use a stable filename such as `FV_AUDIT_REPORT.json`; do not append dates or versions to the filename.

Validate the report against `FV_Audit_Report_Schema.json`. The report records:

- audit ID, creation time, auditor agent/model/run identity;
- expected packet ID and generated-media packet ID;
- generated media ID, type, hash when available, and embedded provenance status;
- provenance status for both packets;
- audit specification version and packet-to-packet comparison method;
- individual deviations, class, status, confidence, evidence references, and packet references;
- category-specific numerator, denominator, uncertainty count, rate, and exact unit definition;
- limitations and unavailable evidence.

### 3.1 Rate calculation and comparability

For each metric, calculate:

`rate_percent = 100 * numerator / denominator`

If the denominator is zero, set `rate_percent` to null. Never report a fabricated zero rate for an unmeasurable category.

Each metric MUST state its unit definition and scope. The denominator is the number of assessable units for that specific category; the numerator is the number of those units with a confirmed deviation. Uncertain units are reported separately and are not silently counted as passes or failures.

Use stable unit definitions across audits before comparing percentages. Keep category-specific rates separate; do not collapse unlike categories into one overall hallucination percentage. Report evaluator uncertainty and assessment coverage alongside deviation rates.

For longitudinal agent profiles, retain the original audit reports and aggregate counts by summing numerators and denominators within matching metric definitions. Do not take an unweighted average of percentages. Stratify by agent role (packet generator, media generator, auditor), agent ID, model/version, FV specification version, and audit schema version. Do not merge different roles or incompatible metric definitions.

## 4. Audit deviation classes

Use the existing FV failure taxonomy: INV-O, INV-C, ID-S, ID-M, SP-D, TM-D, BH-D, ST-D, DET-U, and UNC. A deviation record must point to source media evidence (frame/time/region/crop where applicable) and to the relevant expected/generated packet records where possible.

Do not promote an uncertain observation into a confirmed deviation without supporting evidence. Evaluator uncertainty remains visible in both the deviation list and the uncertainty metric.


## 6. Batch aggregation reference implementation

A reference batch processor is provided at `TOOLS/fv_audit_batch.py`. It is an offline aggregation utility, not a claim that a standalone FV CLI has been installed. Invoke it with Python 3.10+ and the dependency in `TOOLS/requirements.txt`:

```sh
python TOOLS/fv_audit_batch.py path/to/FV_AUDIT_REPORT.json another/FV_AUDIT_REPORT.json
```

The utility writes `FV_AUDIT_BATCH_REPORT.json` and `FV_AUDIT_BATCH_SUMMARY.md` in the current directory. Use `--output`, `--summary`, or `--schema` to override those paths.

Each input is checked against the current `FV_Audit_Report_Schema.json`. Invalid files are listed with validation/read errors and excluded from aggregation. Identical copies of one audit ID are counted once. If the same audit ID appears with different content, all copies of that ID are excluded pending manual reconciliation; the utility does not guess which is authoritative.

Profiles are separated by role, declared agent identity/model version, audit specification version, report schema version, metric code, unit definition, and scope. Missing generator identities are retained as explicit unknown-role profiles rather than silently omitted. Numerators, denominators, and uncertain-unit counts are pooled; percentages are recomputed from pooled counts. Zero denominators yield a null rate.

The batch report schema is `FV_Audit_Batch_Report_Schema.json`. The reference tests are in `TOOLS/test_fv_audit_batch.py`; run them with:

```sh
python -m pip install -r TOOLS/requirements.txt
python -m unittest discover -s TOOLS -p 'test_*.py' -v
```

**Interface boundary:** this utility is a batch processor for existing report files. It does not perform visual analysis, regenerate reports, infer missing provenance, or change the meaning of `fv audit`. The skill-level command `fv audit batch` remains a proposed interface until the skill runtime can reliably invoke this utility with attached files.
