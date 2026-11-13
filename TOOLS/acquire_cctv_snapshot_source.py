#!/usr/bin/env python3
"""Acquire and fingerprint the Commons BLK-HDPTZ12 demo video.

The source file and extracted frame images are deleted after hashing. Only
metadata and frame hashes are emitted; no video or potentially identifying
vehicle/plate imagery is retained in the repository or workflow artifact.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, shutil, subprocess, tempfile
from urllib.parse import urlsplit, urlunsplit
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from pathlib import Path
import requests

FILE_TITLE = "BLK-HDPTZ12 Security Camera Parking Lot Surveillance Video.webm"
PAGE_URL = "https://commons.wikimedia.org/wiki/File:BLK-HDPTZ12_Security_Camera_Parking_Lot_Surveillance_Video.webm"
API_URL = "https://commons.wikimedia.org/w/api.php"
YOUTUBE_ID = "U7HRKjlXK-Y"
STORYBOARD_TIMES = [0, 24, 64, 104, 156, 160, 184, 208, 220, 236, 240, 252, 268, 300, 316]
BOUNDARY_TIMES = [104.57, 105.57, 106.57, 210.14, 211.14, 212.14]
TRANSITION_WINDOWS = [(158.0, 162.0), (238.0, 242.0)]
ALLOWED_HEADERS = {"content-type", "content-length", "last-modified", "etag"}


def http_session():
    retry = Retry(
        total=8, connect=5, read=5, status=8, backoff_factor=2,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET"]), respect_retry_after_header=True,
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": "FakingVisionProvenance/1.0 (https://github.com/memoryprismv1/faking-vision)"})
    return session


def run_json(args):
    return json.loads(subprocess.check_output(args, text=True))

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def metadata_value(ext, key):
    item = ext.get(key) or {}
    return item.get("value") if isinstance(item, dict) else item

def commons_metadata():
    params = {
        "action": "query",
        "titles": f"File:{FILE_TITLE}",
        "prop": "imageinfo|revisions",
        "iiprop": "url|size|sha1|timestamp|mime|extmetadata",
        "rvprop": "ids|timestamp",
        "format": "json",
        "formatversion": 2,
    }
    r = http_session().get(API_URL, params=params, timeout=60)
    r.raise_for_status()
    payload = r.json()
    page = payload["query"]["pages"][0]
    if "missing" in page:
        raise RuntimeError(f"Commons file page missing: {FILE_TITLE}")
    info = page["imageinfo"][0]
    ext = info.get("extmetadata", {})
    selected = ["Artist", "DateTimeOriginal", "Source", "Credit",
                "LicenseShortName", "UsageTerms", "Copyrighted",
                "AttributionRequired", "Restrictions", "ImageDescription"]
    return {
        "page": {
            "title": page.get("title"),
            "pageid": page.get("pageid"),
            "lastrevid": page.get("lastrevid"),
            "touched": page.get("touched"),
            "revision_timestamp": (page.get("revisions") or [{}])[0].get("timestamp"),
        },
        "imageinfo": {
            "url": info["url"],
            "size": info.get("size"),
            "sha1": info.get("sha1"),
            "timestamp": info.get("timestamp"),
            "mime": info.get("mime"),
            "width": info.get("width"),
            "height": info.get("height"),
            "metadata": {k: metadata_value(ext, k) for k in selected if ext.get(k)},
        },
        "response_headers": {k.lower(): v for k, v in r.headers.items()
                             if k.lower() in ALLOWED_HEADERS},
    }

def download(url: str, target: Path):
    parts = urlsplit(url)
    clean_url = urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))
    r = http_session().get(clean_url, stream=True, timeout=240)
    r.raise_for_status()
    safe_headers = {k.lower(): v for k, v in r.headers.items()
                    if k.lower() in ALLOWED_HEADERS}
    with target.open("wb") as f:
        for chunk in r.iter_content(1024 * 1024):
            if chunk:
                f.write(chunk)
    return safe_headers

def extract_one(source: Path, timestamp: float, out: Path, label: str):
    target = out / f"{label}.jpg"
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{timestamp:.3f}",
        "-i", str(source), "-frames:v", "1", "-q:v", "2", str(target)
    ], check=True)
    return {"source_time_s": timestamp, "sha256": sha256(target),
            "bytes": target.stat().st_size}

def extract_window(source: Path, start: float, end: float, out: Path, label: str):
    folder = out / label
    folder.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-ss", f"{start:.3f}",
        "-i", str(source), "-t", f"{end-start:.3f}", "-vf", "fps=10",
        "-q:v", "2", str(folder / "frame_%03d.jpg")
    ], check=True)
    records = []
    frames = sorted(folder.glob("frame_*.jpg"))
    for i, frame in enumerate(frames):
        records.append({
            "source_time_s": round(start + i / 10, 3),
            "sha256": sha256(frame),
            "bytes": frame.stat().st_size,
        })
        frame.unlink()
    folder.rmdir()
    return records

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    metadata = commons_metadata()
    info = metadata["imageinfo"]
    with tempfile.TemporaryDirectory(prefix="blkhdptz12-") as temp:
        source = Path(temp) / "source.webm"
        download_headers = download(info["url"], source)
        source_sha = sha256(source)
        probe = run_json([
            "ffprobe", "-v", "error", "-show_format", "-show_streams",
            "-of", "json", str(source)
        ])
        duration = float(probe["format"]["duration"])

        frames_dir = Path(temp) / "frames"
        frames_dir.mkdir()
        global_times = [float(t) for t in range(0, 317, 4)]
        global_frames = [
            extract_one(source, t, frames_dir, f"global_{int(t):03d}")
            for t in global_times if t <= duration
        ]
        boundary_frames = [
            extract_one(source, t, frames_dir, f"boundary_{i:02d}")
            for i, t in enumerate(BOUNDARY_TIMES)
        ]
        transition_frames = []
        for i, (start, end) in enumerate(TRANSITION_WINDOWS):
            transition_frames.extend(extract_window(source, start, end, frames_dir,
                                                    f"transition_{i+1}"))

        stream_info = []
        for stream in probe.get("streams", []):
            stream_info.append({
                "codec_type": stream.get("codec_type"),
                "codec_name": stream.get("codec_name"),
                "width": stream.get("width"),
                "height": stream.get("height"),
                "avg_frame_rate": stream.get("avg_frame_rate"),
                "r_frame_rate": stream.get("r_frame_rate"),
                "sample_rate": stream.get("sample_rate"),
                "channels": stream.get("channels"),
            })

        acquisition = {
            "record_type": "commons_source_acquisition",
            "acquired_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "source_page": PAGE_URL,
            "original_youtube_url": f"https://www.youtube.com/watch?v={YOUTUBE_ID}",
            "source_page_metadata": metadata["page"],
            "commons_imageinfo": {k: v for k, v in info.items() if k != "url"},
            "original_imageinfo_url": info["url"],
            "download_url": urlunsplit((*urlsplit(info["url"])[:3], "", "")),
            "download_response_headers": download_headers,
            "source_sha256": source_sha,
            "source_bytes": source.stat().st_size,
            "ffprobe": {
                "duration_seconds": duration,
                "format_name": probe.get("format", {}).get("format_name"),
                "format_bit_rate": probe.get("format", {}).get("bit_rate"),
                "streams": stream_info,
            },
            "workflow_artifact": {
                "run_id": os.environ.get("GITHUB_RUN_ID"),
                "run_url": (f'https://github.com/{os.environ.get("GITHUB_REPOSITORY")}/actions/runs/{os.environ.get("GITHUB_RUN_ID")}'
                            if os.environ.get("GITHUB_RUN_ID") else None),
                "artifact_name": "cctv-snapshot-source-manifest",
                "retention_days": 30,
                "source_media_retained": False,
                "sample_images_retained": False,
            },
            "privacy_and_licensing_review": {
                "media_policy": "Source video and extracted frames are deleted after hashing; no plate-like markings or vehicle imagery are retained in the repository/artifact.",
                "commons_license_claim": "Commons metadata asserts public domain under a fixed-CCTV/no-human-input rationale.",
                "license_review_flag": "REVIEW REQUIRED: the page describes a Supercircuits camera demonstration and the storyboard shows deliberate PTZ/zoom framing changes. Commons' automated-camera rationale is not independently validated here; do not treat it as a legal conclusion.",
                "visual_privacy_note": "A plate-like marking is visible in the source/storyboard; characters are not transcribed and no frame images are retained.",
            },
            "expected_vs_measured": {
                "commons_page_duration_rounded": "5 min 17 s",
                "storyboard_duration_seconds": 316.708,
                "measured_duration_seconds": duration,
                "storyboard_resolution": "1920x1080",
                "storyboard_frame_rate": "30 fps",
            },
        }
        manifest = {
            "record_type": "source_frame_hash_manifest",
            "source_sha256": source_sha,
            "sampling": {
                "global_interval_seconds": 4,
                "storyboard_reference_times_seconds": STORYBOARD_TIMES,
                "boundary_times_seconds": BOUNDARY_TIMES,
                "transition_windows_seconds": TRANSITION_WINDOWS,
                "transition_sampling_fps": 10,
                "retained_frame_images": False,
            },
            "global_frames": global_frames,
            "boundary_frames": boundary_frames,
            "transition_frames": transition_frames,
            "counts": {
                "global": len(global_frames),
                "boundary": len(boundary_frames),
                "transition": len(transition_frames),
                "total_hashes": len(global_frames) + len(boundary_frames) + len(transition_frames),
            },
        }

    (out / "source_acquisition.json").write_text(
        json.dumps(acquisition, indent=2) + "\n", encoding="utf-8"
    )
    (out / "source_frame_manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "source_sha256": acquisition["source_sha256"],
        "source_bytes": acquisition["source_bytes"],
        "duration_seconds": duration,
        "global_frames": len(global_frames),
        "boundary_frames": len(boundary_frames),
        "transition_frames": len(transition_frames),
        "source_media_retained": False,
        "sample_images_retained": False,
    }, indent=2))

if __name__ == "__main__":
    main()
