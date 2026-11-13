#!/usr/bin/env python3
"""Fingerprint extracted official KITTI Odometry inputs; does not perform registration."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json
from pathlib import Path

SEQUENCES = {"00": 4541, "07": 1101}
OFFICIAL_PAGE = "https://www.cvlibs.net/datasets/kitti/eval_odometry.php"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True, help="Extracted dataset root")
    ap.add_argument("--output", type=Path, required=True)
    a = ap.parse_args()
    root = a.root.resolve()
    results, failures = {}, []
    for seq, expected in SEQUENCES.items():
        base = root / "dataset" / "sequences" / seq
        scan_dir = base / "velodyne"
        scans = sorted(scan_dir.glob("*.bin")) if scan_dir.exists() else []
        calib, times = base / "calib.txt", base / "times.txt"
        pose = root / "dataset" / "poses" / f"{seq}.txt"
        pose_lines = [x for x in pose.read_text().splitlines() if x.strip()] if pose.exists() else []
        calib_text = calib.read_text(errors="replace") if calib.exists() else ""
        keys = [k for k in ("P0:", "P1:", "P2:", "P3:", "Tr:") if k in calib_text]
        malformed = [p.name for p in scans if p.stat().st_size == 0 or p.stat().st_size % 16 != 0]
        checks = {
            "expected_scan_count": len(scans) == expected,
            "pose_file_present": pose.exists(),
            "pose_line_count_matches_scans": len(pose_lines) == len(scans),
            "calibration_file_present": calib.exists(),
            "calibration_contains_projection_and_velodyne_transform": all(k in keys for k in ("P0:", "P1:", "P2:", "P3:", "Tr:")),
            "timestamps_match_scans_if_present": not times.exists() or len([x for x in times.read_text().splitlines() if x.strip()]) == len(scans),
            "scan_files_have_xyzi_float32_byte_shape": not malformed,
        }
        results[seq] = {
            "expected_scan_count": expected, "actual_scan_count": len(scans),
            "pose_file": str(pose.relative_to(root)) if pose.exists() else None,
            "pose_line_count": len(pose_lines), "pose_sha256": sha256(pose) if pose.exists() else None,
            "calibration_file": str(calib.relative_to(root)) if calib.exists() else None,
            "calibration_sha256": sha256(calib) if calib.exists() else None,
            "calibration_keys_found": keys,
            "timestamps_file": str(times.relative_to(root)) if times.exists() else None,
            "malformed_scan_files": malformed[:20], "checks": checks,
            "all_checks_pass": all(checks.values()),
        }
        if not all(checks.values()): failures.append(seq)
    record = {
        "record_type": "local_dataset_verification_manifest",
        "dataset": "KITTI Vision Benchmark Suite - Odometry Velodyne",
        "source": OFFICIAL_PAGE, "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "root": str(root), "sequences": results, "all_checks_pass": not failures,
        "limitations": [
            "Verifies extracted structure, counts, pose/calibration presence and hashes only.",
            "Does not prove a legacy packet output was generated from these files.",
            "Does not run registration, ICP, dynamic-object filtering or map comparison.",
            "Odometry benchmark archives are distinct from KITTI raw-drive archives; do not substitute raw-drive paths without an explicit mapping."
        ]
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(a.output), "sequences": {
        k: {"scan_count": v["actual_scan_count"], "all_checks_pass": v["all_checks_pass"]}
        for k, v in results.items()
    }, "all_checks_pass": record["all_checks_pass"]}, indent=2))
    if failures: raise SystemExit("KITTI verification failed: " + ", ".join(failures))

if __name__ == "__main__": main()
