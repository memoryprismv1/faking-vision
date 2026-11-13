#!/usr/bin/env python3
"""Acquire and fingerprint the Fullerton Transportation Center Commons source.

Requires Python 3.10+, ffmpeg, and ffprobe. The 10-second pass is a locator
sample, not exhaustive analysis or proof that legacy observations are correct.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, shutil, subprocess, urllib.request
from pathlib import Path

SOURCE_URL = "https://upload.wikimedia.org/wikipedia/commons/3/3f/Full,_unedited_Kelly_Thomas_confrontation_video_(35_min.).webm"
SOURCE_PAGE = "https://commons.wikimedia.org/wiki/File:Full,_unedited_Kelly_Thomas_confrontation_video_(35_min.).webm"
YOUTUBE_SOURCE = "https://www.youtube.com/watch?v=dDpJ5FtG6Ac"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def run_json(args: list[str]) -> dict:
    return json.loads(subprocess.run(args, check=True, capture_output=True, text=True).stdout)

def extract_frame(source: Path, seconds: float, destination: Path) -> None:
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-ss",
                    f"{seconds:.3f}", "-i", str(source), "-frames:v", "1",
                    "-q:v", "2", str(destination)], check=True)

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    out = parser.parse_args().output_dir.resolve()
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise SystemExit("ffmpeg and ffprobe are required")
    source_dir, evidence_dir = out / "source", out / "source_aligned_evidence"
    source_dir.mkdir(parents=True, exist_ok=True)
    evidence_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / "fullerton_kelly_thomas_commons_original.webm"
    request = urllib.request.Request(SOURCE_URL, headers={
        "User-Agent": "FakingVision-source-acquisition/1.0 (reproducibility record)"
    })
    temp = source.with_suffix(".webm.part")
    with urllib.request.urlopen(request, timeout=120) as response:
        final_url, headers = response.geturl(), dict(response.headers.items())
        with temp.open("wb") as target:
            shutil.copyfileobj(response, target)
    temp.replace(source)

    probe = run_json([
        "ffprobe", "-v", "error", "-show_entries",
        "format=duration,size,format_name:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels",
        "-of", "json", str(source)
    ])
    duration = float(probe.get("format", {}).get("duration", 0))
    video = next((s for s in probe.get("streams", []) if s.get("codec_type") == "video"), {})
    audio = next((s for s in probe.get("streams", []) if s.get("codec_type") == "audio"), {})
    checks = {
        "duration_matches_2050_seconds_within_1s": abs(duration - 2050.0) <= 1.0,
        "dimensions_are_640x360": video.get("width") == 640 and video.get("height") == 360,
        "video_codec_is_vp9": video.get("codec_name") == "vp9",
        "audio_codec_is_opus_if_present": not audio or audio.get("codec_name") == "opus",
        "size_is_55_to_70_decimal_mb": 55_000_000 <= source.stat().st_size <= 70_000_000,
    }

    global_dir = evidence_dir / "global_10s"
    global_dir.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i",
                    str(source), "-vf", "fps=1/10", "-q:v", "3",
                    str(global_dir / "frame_%04d.jpg")], check=True)
    global_frames = sorted(global_dir.glob("frame_*.jpg"))
    global_records = [{
        "file": str(p.relative_to(out)), "nominal_source_time_s": i * 10,
        "sha256": sha256(p), "bytes": p.stat().st_size
    } for i, p in enumerate(global_frames)]

    boundary_times = [682.0, 683.0, 684.0, 1365.0, 1366.0, 1367.0, 2049.0]
    boundary_records = []
    for seconds in boundary_times:
        frame = evidence_dir / f"boundary_{seconds:07.3f}s.jpg"
        extract_frame(source, seconds, frame)
        boundary_records.append({
            "nominal_source_time_s": seconds, "file": str(frame.relative_to(out)),
            "sha256": sha256(frame), "bytes": frame.stat().st_size
        })

    record = {
        "record_type": "source_acquisition_record",
        "dataset": "Fullerton Transportation Center surveillance video",
        "source_file_title": "Full, unedited Kelly Thomas confrontation video (35 min.).webm",
        "source_page": SOURCE_PAGE,
        "source_page_revision": "999941538",
        "source_page_last_edited": "2025-02-18T19:40:00Z",
        "commons_upload_date": "2021-07-07",
        "commons_uploader": "Levivich",
        "commons_summary_author_field": "None (prepositioned surveillance camera at Fullerton Transportation Center)",
        "commons_embedded_metadata_author_field": "Orange County Register",
        "original_youtube_source": YOUTUBE_SOURCE,
        "commons_license_statement": "Commons displays California Public Records Act and ineligible-work public-domain rationales. This records Commons' assertions, not an independent legal opinion.",
        "retrieval": {
            "acquired_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "requested_url": SOURCE_URL, "final_url": final_url,
            "response_headers": headers,
            "local_file": str(source.relative_to(out)),
            "bytes": source.stat().st_size, "sha256": sha256(source)
        },
        "probe": probe,
        "expected_commons_metadata": {
            "duration_seconds": 2050, "dimensions": [640, 360],
            "video_codec": "VP9", "audio_codec": "Opus", "displayed_size": "61.4 MB"
        },
        "checks": checks,
        "all_expected_checks_pass": all(checks.values()),
        "limitations": [
            "This is a YouTube-derived Commons upload, not the camera's native recorder file.",
            "Commons' displayed licensing rationale is not independently adjudicated here.",
            "The 10-second global pass is a locator sample, not exhaustive visual analysis.",
            "Audio is not analyzed or transcribed by this workflow.",
            "Boundary-adjacent samples do not prove absent legacy split files were cut at the exact frames."
        ]
    }
    (out / "source_acquisition.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    (evidence_dir / "frame_manifest.json").write_text(json.dumps({
        "source_sha256": record["retrieval"]["sha256"],
        "sampling": "one frame every 10 seconds plus boundary-adjacent samples",
        "global_sample_count": len(global_records),
        "global_frames": global_records, "boundary_frames": boundary_records,
        "warning": "Locator evidence only; not exhaustive visual analysis."
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "source_sha256": record["retrieval"]["sha256"], "source_bytes": record["retrieval"]["bytes"],
        "duration_seconds": duration, "checks": checks,
        "global_sample_count": len(global_records), "output_dir": str(out)
    }, indent=2))
    if not all(checks.values()):
        raise SystemExit("Source metadata check failed; inspect source_acquisition.json")

if __name__ == "__main__":
    main()
