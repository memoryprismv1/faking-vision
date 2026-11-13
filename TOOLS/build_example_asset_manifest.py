#!/usr/bin/env python3
"""Create SHA-256 inventory of all files currently checked into examples/."""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import mimetypes
import os
from pathlib import Path

ROOT = Path("examples")
OUTPUT = Path("docs/provenance/example_asset_hashes.json")

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def kind(path: Path) -> str:
    suffix = path.suffix.lower()
    groups = {
        "image": {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp", ".tif", ".tiff"},
        "video": {".mp4", ".webm", ".mov", ".avi", ".mkv"},
        "audio": {".wav", ".mp3", ".flac", ".ogg", ".m4a"},
        "lidar_or_3d": {".bin", ".las", ".laz", ".ply", ".pcd", ".obj", ".stl", ".xyz", ".e57"},
        "astronomy": {".fits", ".fit", ".fts"},
        "archive": {".zip", ".tar", ".gz", ".7z"},
        "document": {".pdf"},
        "structured_data": {".json", ".csv", ".xml", ".yaml", ".yml"},
        "text_or_code": {".md", ".txt", ".py", ".sh", ".html", ".css", ".js"},
    }
    for label, extensions in groups.items():
        if suffix in extensions:
            return label
    return "other"

def main():
    if not ROOT.is_dir():
        raise SystemExit("examples/ directory not found")
    files = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        rel = path.as_posix()
        files.append({
            "path": rel,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "kind": kind(path),
            "media_type": mimetypes.guess_type(path.name)[0],
        })
    manifest = {
        "schema_version": "1.0",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "git_commit": os.environ.get("GITHUB_SHA"),
        "scope": "all files under examples/ at the named git commit",
        "file_count": len(files),
        "hash_algorithm": "SHA-256",
        "interpretation": "Hashes identify the repository bytes at generation time. They do not prove original-source identity, acquisition date, licence, or processing history.",
        "files": files,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"file_count": len(files), "output": str(OUTPUT)}, indent=2))

if __name__ == "__main__":
    main()
