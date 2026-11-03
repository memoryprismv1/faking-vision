#!/usr/bin/env python3
"""Validate and aggregate FV independent-audit JSON reports.

Requires Python 3.10+ and jsonschema (see requirements.txt). This is a
reference batch processor; it does not re-audit media or modify source reports.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

DEFAULT_SCHEMA = Path(__file__).resolve().parents[1] / "SPECIFICATION" / "FV_Audit_Report_Schema.json"
OUTPUT_NAME = "FV_AUDIT_BATCH_REPORT.json"
SUMMARY_NAME = "FV_AUDIT_BATCH_SUMMARY.md"


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def digest(value: Any) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_report(report: Any, validator: Draft202012Validator) -> list[str]:
    if not isinstance(report, dict):
        return ["top-level JSON value must be an object"]
    errors = sorted(validator.iter_errors(report), key=lambda e: list(map(str, e.absolute_path)))
    return [
        f"{'.'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in errors
    ]


def agent_record(value: Any) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        return None
    if not any(value.get(key) for key in ("agent_id", "model_provider", "model_name")):
        return None
    return {
        "agent_id": value.get("agent_id"),
        "model_provider": value.get("model_provider"),
        "model_name": value.get("model_name"),
        "model_version": value.get("model_version"),
    }


def provenance_agents(report: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    """Read role snapshots when supplied; absent provenance remains unknown."""
    found: list[tuple[str, dict[str, Any]]] = []
    auditor = agent_record(report.get("auditor"))
    if auditor:
        found.append(("auditor", auditor))

    provenance = report.get("provenance")
    if isinstance(provenance, dict):
        # Canonical shape documented by FV batch processing:
        # expected_packet.packet_generator;
        # generated_media_packet.packet_generator/media_generator.
        expected = provenance.get("expected_packet", {})
        generated = provenance.get("generated_media_packet", {})
        media = provenance.get("generated_media", {})
        candidates = [
            ("packet_generator_expected", expected.get("packet_generator") if isinstance(expected, dict) else None),
            ("packet_generator_generated", generated.get("packet_generator") if isinstance(generated, dict) else None),
            ("media_generator", generated.get("media_generator") if isinstance(generated, dict) else None),
            ("media_generator", media.get("media_generator") if isinstance(media, dict) else None),
        ]
        seen: set[tuple[str, str]] = set()
        for role, raw in candidates:
            record = agent_record(raw)
            if record:
                marker = (role, canonical(record))
                if marker not in seen:
                    found.append((role, record))
                    seen.add(marker)
    if not found:
        found.append(("unknown_role", {
            "agent_id": None, "model_provider": None,
            "model_name": None, "model_version": None,
        }))
    return found


def profile_key(role: str, agent: dict[str, Any], report: dict[str, Any], metric: dict[str, Any]) -> tuple:
    comparison = report["comparison"]
    return (
        role, canonical(agent), comparison.get("audit_spec_version"),
        report.get("schema_version"), metric["metric_code"],
        metric["unit_definition"], metric.get("scope"),
    )


def aggregate(paths: list[Path], schema_path: Path) -> dict[str, Any]:
    schema = load_json(schema_path)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    loaded: list[dict[str, Any]] = []
    invalid: list[dict[str, Any]] = []
    for path in paths:
        try:
            report = load_json(path)
            errors = validate_report(report, validator)
            if errors:
                invalid.append({"source": str(path), "errors": errors})
            else:
                loaded.append({"source": str(path), "report": report, "fingerprint": digest(report)})
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            invalid.append({"source": str(path), "errors": [str(exc)]})

    by_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in loaded:
        by_id[item["report"]["audit_id"]].append(item)

    accepted: list[dict[str, Any]] = []
    duplicate_identical: list[dict[str, Any]] = []
    duplicate_conflicts: list[dict[str, Any]] = []
    for audit_id, items in sorted(by_id.items()):
        fingerprints = {item["fingerprint"] for item in items}
        if len(fingerprints) == 1:
            accepted.append(sorted(items, key=lambda x: x["source"])[0])
            if len(items) > 1:
                duplicate_identical.append({
                    "audit_id": audit_id,
                    "kept_source": sorted(items, key=lambda x: x["source"])[0]["source"],
                    "duplicate_sources": sorted(item["source"] for item in items)[1:],
                    "action": "counted once",
                })
        else:
            duplicate_conflicts.append({
                "audit_id": audit_id,
                "sources": sorted(item["source"] for item in items),
                "action": "excluded all conflicting copies; manual reconciliation required",
            })

    profiles: dict[tuple, dict[str, Any]] = {}
    deviations: list[dict[str, Any]] = []
    source_audits: list[dict[str, Any]] = []
    for item in accepted:
        report = item["report"]
        source = item["source"]
        comparison = report["comparison"]
        source_audits.append({
            "audit_id": report["audit_id"],
            "source": source,
            "audit_spec_version": comparison.get("audit_spec_version"),
            "schema_version": report["schema_version"],
        })
        for deviation in report.get("deviations", []):
            deviations.append({
                "audit_id": report["audit_id"],
                "source_report": source,
                **deviation,
            })
        agents = provenance_agents(report)
        for metric in report.get("metrics", []):
            for role, agent in agents:
                key = profile_key(role, agent, report, metric)
                profile = profiles.setdefault(key, {
                    "role": role, "agent": agent,
                    "audit_spec_version": comparison.get("audit_spec_version"),
                    "audit_schema_version": report["schema_version"],
                    "metric_code": metric["metric_code"],
                    "unit_definition": metric["unit_definition"],
                    "scope": metric.get("scope"),
                    "numerator": 0, "denominator": 0, "uncertain_units": 0,
                    "contributing_audit_ids": [],
                    "contributing_reports": [],
                })
                profile["numerator"] += metric["numerator"]
                profile["denominator"] += metric["denominator"]
                profile["uncertain_units"] += metric["uncertain_units"]
                profile["contributing_audit_ids"].append(report["audit_id"])
                profile["contributing_reports"].append(source)

    results = []
    for key in sorted(profiles, key=lambda k: tuple(str(x) for x in k)):
        profile = profiles[key]
        denominator = profile["denominator"]
        profile["rate_percent"] = (100.0 * profile["numerator"] / denominator) if denominator else None
        profile["audit_count"] = len(set(profile["contributing_audit_ids"]))
        profile["contributing_audit_ids"] = sorted(set(profile["contributing_audit_ids"]))
        profile["contributing_reports"] = sorted(set(profile["contributing_reports"]))
        results.append(profile)

    return {
        "schema_version": "1.0",
        "report_type": "fv_audit_batch",
        "source_report_count": len(paths),
        "valid_unique_audit_count": len(accepted),
        "invalid_report_count": len(invalid),
        "duplicate_identical_group_count": len(duplicate_identical),
        "duplicate_conflict_group_count": len(duplicate_conflicts),
        "source_audits": source_audits,
        "profiles": results,
        "deviations": deviations,
        "invalid_reports": invalid,
        "duplicate_identical_audits": duplicate_identical,
        "duplicate_conflicts": duplicate_conflicts,
        "limitations": [
            "Batch aggregation does not re-audit media or alter source audit reports.",
            "Profiles are separated by role, agent/model identity, FV audit specification version, audit schema version, metric code, unit definition, and scope.",
            "Metrics with different unit definitions or scopes are never combined.",
            "Reports without packet-generator or media-generator snapshots cannot contribute to those agent-specific profiles; missing roles remain unknown.",
            "A zero denominator produces a null rate, not a fabricated zero.",
            "Conflicting copies of one audit ID are all excluded pending manual reconciliation.",
        ],
    }


def write_summary(report: dict[str, Any], destination: Path) -> None:
    lines = [
        "# FV Audit Batch Summary", "",
        f"- Input reports: {report['source_report_count']}",
        f"- Valid unique audits counted: {report['valid_unique_audit_count']}",
        f"- Invalid reports: {report['invalid_report_count']}",
        f"- Identical duplicate groups (counted once): {report['duplicate_identical_group_count']}",
        f"- Conflicting duplicate groups (excluded): {report['duplicate_conflict_group_count']}",
        "", "## Aggregated profiles", "",
        "| Role | Agent | Metric | Numerator | Denominator | Uncertain | Rate | Audits |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for profile in report["profiles"]:
        agent = profile["agent"]
        label = agent.get("agent_id") or agent.get("model_name") or "unknown"
        rate = "n/a" if profile["rate_percent"] is None else f"{profile['rate_percent']:.2f}%"
        lines.append(
            f"| {profile['role']} | {label} | {profile['metric_code']} | "
            f"{profile['numerator']} | {profile['denominator']} | "
            f"{profile['uncertain_units']} | {rate} | {profile['audit_count']} |"
        )
    lines += ["", "## Data-quality findings", ""]
    for entry in report["invalid_reports"]:
        lines.append(f"- Invalid: `{entry['source']}` — {'; '.join(entry['errors'])}")
    for entry in report["duplicate_identical_audits"]:
        lines.append(f"- Duplicate audit {entry['audit_id']}: counted once; duplicates: {', '.join(entry['duplicate_sources'])}")
    for entry in report["duplicate_conflicts"]:
        lines.append(f"- Conflicting audit ID {entry['audit_id']}: excluded all copies: {', '.join(entry['sources'])}")
    if not report["invalid_reports"] and not report["duplicate_identical_audits"] and not report["duplicate_conflicts"]:
        lines.append("- No invalid reports or duplicate audit IDs detected.")
    lines += ["", "## Limitations", ""] + [f"- {item}" for item in report["limitations"]]
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+", type=Path, help="FV_AUDIT_REPORT.json files")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="audit report JSON Schema")
    parser.add_argument("--output", type=Path, default=Path(OUTPUT_NAME), help="aggregate JSON output")
    parser.add_argument("--summary", type=Path, default=Path(SUMMARY_NAME), help="Markdown summary output")
    args = parser.parse_args()
    report = aggregate(args.reports, args.schema)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_summary(report, args.summary)
    print(f"Wrote {args.output} and {args.summary}")
    print(
        f"Counted {report['valid_unique_audit_count']} unique audits; "
        f"{report['invalid_report_count']} invalid; "
        f"{report['duplicate_conflict_group_count']} conflicting duplicate groups."
    )
    return 0 if not report["invalid_reports"] and not report["duplicate_conflicts"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
