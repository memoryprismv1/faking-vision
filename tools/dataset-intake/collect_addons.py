#!/usr/bin/env python3
"""Targeted follow-up: explicit-overlap drone set, BigStitcher OSF mirror, and HST visit-safe intake."""
from __future__ import annotations
import hashlib, json, math, subprocess, sys, traceback, zipfile
from datetime import datetime, timezone
from pathlib import Path
import requests

BASE = Path(sys.argv[1] if len(sys.argv) > 1 else "intake")
RAW, INS = BASE / "downloads", BASE / "inspection"
RAW.mkdir(parents=True, exist_ok=True)
INS.mkdir(parents=True, exist_ok=True)
S = requests.Session()
S.headers.update({"User-Agent": "FV-dataset-intake/1.1"})
RECS = []

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def exif_audit(root: Path) -> dict:
    from PIL import Image
    files = sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".tif", ".tiff", ".png"})
    rows = []
    for p in files:
        try:
            im = Image.open(p)
            ex = im.getexif()
            row = {"file": str(p.relative_to(BASE)), "width": im.width, "height": im.height,
                   "datetime_original": ex.get(36867) or ex.get(306),
                   "camera_make": ex.get(271), "camera_model": ex.get(272)}
            gps = {}
            try:
                g = ex.get_ifd(34853)
                if g:
                    def dms(v): return float(v[0]) + float(v[1]) / 60 + float(v[2]) / 3600
                    lat, lon = dms(g[2]), dms(g[4])
                    if g.get(1) == "S": lat = -lat
                    if g.get(3) == "W": lon = -lon
                    gps = {"latitude": lat, "longitude": lon}
                    if g.get(6) is not None:
                        gps["altitude_m"] = float(g[6]) * (-1 if g.get(5) == 1 else 1)
            except Exception as e:
                gps = {"parse_error": str(e)}
            row["gps"] = gps
            rows.append(row)
        except Exception:
            continue
    tagged = [x for x in rows if "latitude" in x.get("gps", {})]
    result = {"file_count": len(files), "readable_image_count": len(rows), "geotagged_count": len(tagged),
              "images": rows}
    if tagged:
        result["gps_bounds"] = {
            "min_lat": min(x["gps"]["latitude"] for x in tagged),
            "max_lat": max(x["gps"]["latitude"] for x in tagged),
            "min_lon": min(x["gps"]["longitude"] for x in tagged),
            "max_lon": max(x["gps"]["longitude"] for x in tagged)
        }
        ordered = sorted(tagged, key=lambda x: x.get("datetime_original") or "")
        distances = []
        for a, b in zip(ordered, ordered[1:]):
            lat1, lon1 = math.radians(a["gps"]["latitude"]), math.radians(a["gps"]["longitude"])
            lat2, lon2 = math.radians(b["gps"]["latitude"]), math.radians(b["gps"]["longitude"])
            dlat, dlon = lat2 - lat1, lon2 - lon1
            q = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
            distances.append(6371000 * 2 * math.asin(math.sqrt(q)))
        if distances:
            sd = sorted(distances)
            result["successive_capture_position_distance_m"] = {
                "min": min(sd), "median": sd[len(sd) // 2], "max": max(sd), "count": len(sd),
                "interpretation": "Capture-position spacing only; not a footprint-overlap measurement."
            }
    return result

def phalaborwa():
    label = "OpenDroneMap Phalaborwa small overlap/sidelap survey"
    source = "https://github.com/OpenDroneMap/ODMdata"
    folder = "https://drive.google.com/drive/folders/1e1eA8LNpP4scYyDYdWd6UQ1qJ006iOXG"
    dest = RAW / "drone_phalaborwa_sm_ol"
    dest.mkdir(parents=True, exist_ok=True)
    try:
        cmd = [sys.executable, "-m", "gdown", "--folder", "--remaining-ok", "--continue", "-O", str(dest), folder]
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=1800)
        imgs = sorted(x for x in dest.rglob("*") if x.is_file() and x.suffix.lower() in {".jpg", ".jpeg", ".tif", ".tiff", ".png"})
        total = sum(x.stat().st_size for x in dest.rglob("*") if x.is_file())
        if p.returncode != 0 or len(imgs) < 10:
            raise RuntimeError("gdown return=%s; images=%s; stdout=%s; stderr=%s" %
                               (p.returncode, len(imgs), p.stdout[-1500:], p.stderr[-1500:]))
        audit = exif_audit(dest)
        (INS / "phalaborwa_sm_ol_exif_audit.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
        rec = {
            "dataset": label, "status": "DOWNLOADED", "source_page": source, "download_url": folder,
            "local_path": str(dest.relative_to(BASE)), "image_count": len(imgs), "total_bytes": total,
            "catalogue_claim": {"images": 36, "size_mb": 178, "exif_coordinates": True,
                                "note": "For overlap/sidelap testing"},
            "measured_exif": {"geotagged_count": audit["geotagged_count"],
                              "gps_bounds": audit.get("gps_bounds"),
                              "successive_capture_position_distance_m": audit.get("successive_capture_position_distance_m")},
            "exif_audit": "inspection/phalaborwa_sm_ol_exif_audit.json",
            "notes": "Downloaded source files and measured counts are recorded. Catalog explicitly identifies this set for overlap/sidelap testing. GPS spacing is not itself proof of image footprint overlap; inspect camera footprint/pose and images. Dataset-specific reuse terms were not located in this intake; confirm before redistribution."
        }
        RECS.append(rec)
        print("Phalaborwa: DOWNLOADED images=%d bytes=%d geotagged=%s" %
              (len(imgs), total, audit["geotagged_count"]), flush=True)
    except Exception as e:
        dest_exists = any(dest.rglob("*"))
        rec = {"dataset": label, "status": "FAILED", "source_page": source, "download_url": folder,
               "error": type(e).__name__ + ": " + str(e),
               "partial_files_retained": dest_exists,
               "notes": "Catalog advertises 36 images/~178MB for overlap/sidelap testing; not counted as acquired unless the download completes."}
        RECS.append(rec)
        print("Phalaborwa FAILED: " + rec["error"], flush=True)

def bigstitcher_osf():
    label = "BigStitcher published example data via OSF mirror"
    source = "https://osf.io/bufza/"
    try:
        root = "https://api.osf.io/v2/nodes/bufza/files/osfstorage/"
        queue = [root]
        seen_folders, seen_pages, matches = set(), set(), []
        while queue and len(seen_pages) < 300:
            url = queue.pop(0)
            if url in seen_pages: continue
            seen_pages.add(url)
            rr = S.get(url, params={"page[size]": 100}, timeout=90)
            rr.raise_for_status()
            doc = rr.json()
            for item in doc.get("data", []):
                a = item.get("attributes", {})
                kind, name = a.get("kind"), a.get("name", "")
                if kind == "file" and name.lower().endswith((".zip", ".tif", ".tiff")):
                    matches.append({"id": item.get("id"), "name": name, "size": a.get("size"),
                                    "download": item.get("links", {}).get("download"),
                                    "path": a.get("materialized_path")})
                elif kind == "folder" and item.get("id") not in seen_folders:
                    seen_folders.add(item.get("id"))
                    href = item.get("relationships", {}).get("files", {}).get("links", {}).get("related", {}).get("href")
                    if href: queue.append(href)
            nxt = doc.get("links", {}).get("next")
            if nxt: queue.append(nxt)
        dest = RAW / "bigstitcher_osf"
        dest.mkdir(parents=True, exist_ok=True)
        successes = []
        candidates = [x for x in matches if x.get("download") and x.get("name", "").lower().endswith(".zip")]
        candidates.sort(key=lambda x: (x.get("size") or 10**15, x["name"]))
        for entry in candidates[:4]:
            size = entry.get("size")
            if size and size > 200_000_000: continue
            target = dest / entry["name"]
            with S.get(entry["download"], stream=True, timeout=(30, 600)) as resp:
                resp.raise_for_status()
                with target.open("wb") as f:
                    for block in resp.iter_content(1024 * 1024):
                        if block: f.write(block)
            if target.stat().st_size > 1024:
                with zipfile.ZipFile(target) as z:
                    bad = z.testzip()
                    if bad: raise RuntimeError("CRC check failed for %s member %s" % (target.name, bad))
                successes.append({"name": entry["name"], "bytes": target.stat().st_size,
                                  "sha256": sha(target), "local_path": str(target.relative_to(BASE)),
                                  "osf_path": entry.get("path")})
        rec = {"dataset": label, "status": "DOWNLOADED" if successes else "METADATA_ONLY" if matches else "FAILED",
               "source_page": source, "file_matches": matches, "downloads": successes,
               "notes": "Alternate OSF source checked because the BigStitcher institutional host failed DNS in the runner. Only ZIPs downloaded and CRC-checked here count as acquired. Verify dataset/readme and license before selecting as an FV example."}
        RECS.append(rec)
        print("BigStitcher OSF: matches=%d downloads=%d" % (len(matches), len(successes)), flush=True)
    except Exception as e:
        rec = {"dataset": label, "status": "FAILED", "source_page": source,
               "error": type(e).__name__ + ": " + str(e)}
        RECS.append(rec)
        print("BigStitcher OSF FAILED: " + rec["error"], flush=True)

def hst_single_visit():
    label = "HST ACS/WFC F606W visit-specific exposures"
    source = "https://archive.stsci.edu/ ; https://docs.astropy.org/projects/astroquery/en/latest/mast/mast_obsquery.html"
    try:
        from astroquery.mast import Observations
        from astropy.io import fits
        obs = Observations.query_criteria(obs_collection="HST", proposal_id="10737",
                                          instrument_name="ACS/WFC", filters="F606W", dataRights="PUBLIC")
        if len(obs) == 0: raise RuntimeError("No public proposal 10737 ACS/WFC F606W observations")
        if "target_name" in obs.colnames:
            mask = [("NGC 104" in str(x).upper()) or ("47 TUC" in str(x).upper()) for x in obs["target_name"]]
            if any(mask): obs = obs[mask]
        if "obs_id" not in obs.colnames:
            raise RuntimeError("MAST observation table lacks obs_id; cannot determine HST visit ID")
        groups = {}
        for i, row in enumerate(obs):
            oid = str(row["obs_id"]).strip()
            tokens = oid.split("_")
            # MAST HST obs IDs typically encode proposal and visit as hst_<proposal>_<visit>.
            if len(tokens) < 3 or tokens[0].lower() != "hst":
                continue
            visit_key = "_".join(tokens[:3])
            groups.setdefault(visit_key, []).append(i)
        candidates = sorted(groups.items(), key=lambda kv: len(kv[1]), reverse=True)
        chosen = next(((k, idx) for k, idx in candidates if len(idx) >= 3), None)
        if not chosen:
            summary = [{"visit_key": k, "count": len(idx)} for k, idx in candidates[:10]]
            raise RuntimeError("No HST visit key containing >=3 exposures: " + json.dumps(summary))
        visit_key, idx = chosen
        selected = obs[idx]
        products = Observations.get_product_list(selected)
        if "productSubGroupDescription" not in products.colnames:
            raise RuntimeError("MAST product list lacks productSubGroupDescription")
        flc = products[[str(x).upper() == "FLC" for x in products["productSubGroupDescription"]]][:6]
        if len(flc) < 3: raise RuntimeError("Visit has fewer than three FLC calibrated products")
        dest = RAW / "hst_single_visit"; dest.mkdir(parents=True, exist_ok=True)
        manifest = Observations.download_products(flc, download_dir=str(dest))
        files = sorted(p for p in dest.rglob("*") if p.is_file() and p.name.lower().endswith("_flc.fits"))
        if len(files) < 3: raise RuntimeError("Only %d FLC files found after download" % len(files))
        exposures = []
        for p in files:
            with fits.open(p, memmap=True) as hdul:
                hdr = hdul[0].header
                sci = next((x for x in hdul if x.name == "SCI" and x.data is not None), None)
                exposures.append({"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p),
                                  "date_obs": hdr.get("DATE-OBS"), "time_obs": hdr.get("TIME-OBS"),
                                  "exptime": hdr.get("EXPTIME"), "filter1": hdr.get("FILTER1"),
                                  "filter2": hdr.get("FILTER2"), "proposal": hdr.get("PROPOSID"),
                                  "visitnum": hdr.get("VISITNUM"), "rootname": hdr.get("ROOTNAME"),
                                  "pa_v3": hdr.get("PA_V3"),
                                  "science_shape": list(sci.data.shape) if sci is not None else None})
        visitnums = sorted({str(x["visitnum"]) for x in exposures if x["visitnum"] is not None})
        status = "DOWNLOADED" if len(visitnums) <= 1 else "DOWNLOADED_NEEDS_REVIEW"
        rec = {"dataset": label, "status": status, "source_page": source,
               "local_path": str(dest.relative_to(BASE)), "visit_key": visit_key,
               "observation_rows": len(idx), "exposure_count": len(files), "visitnums": visitnums,
               "exposures": exposures, "manifest_statuses": [str(x) for x in manifest["Status"]],
               "notes": "Visit grouping uses MAST HST obs_id proposal+visit tokens (hst_<proposal>_<visit>). FITS VISITNUM is checked independently. FITS WCS/footprints still require inspection before declaring this a same-pass overlap example."}
        RECS.append(rec)
        print("HST %s visit_key=%s exposures=%d visitnums=%s" % (status, visit_key, len(files), visitnums), flush=True)
    except Exception as e:
        rec = {"dataset": label, "status": "FAILED", "source_page": source,
               "error": type(e).__name__ + ": " + str(e),
               "traceback": traceback.format_exc(),
               "notes": "No cross-visit substitution was made."}
        RECS.append(rec)
        print("HST FAILED: " + rec["error"], flush=True)

def main():
    # The main collection extracted Mygla into extracted/odm_mygla_dataset, not downloads/.
    mygla = BASE / "extracted" / "odm_mygla_dataset"
    if mygla.exists():
        audit = exif_audit(mygla)
        (INS / "odm_mygla_exif_audit.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
        print("Mygla EXIF: files=%s geotagged=%s bounds=%s" %
              (audit["file_count"], audit["geotagged_count"], audit.get("gps_bounds")), flush=True)
    phalaborwa()
    bigstitcher_osf()
    hst_single_visit()
    (INS / "addon_receipts.json").write_text(json.dumps(RECS, indent=2), encoding="utf-8")
    with (BASE / "RECEIPTS.md").open("a", encoding="utf-8") as f:
        f.write("\n\n# Additional acquisition and inspection\n")
        for r in RECS:
            f.write("\n## " + r.get("dataset", "unnamed") + "\n")
            f.write("- Status: **" + r.get("status", "UNKNOWN") + "**\n")
            f.write("- Source: " + r.get("source_page", "") + "\n")
            f.write("- Notes: " + r.get("notes", r.get("error", "")) + "\n")
    print("ADDON SUMMARY: " + json.dumps({x["dataset"]: x["status"] for x in RECS}), flush=True)

if __name__ == "__main__":
    main()
