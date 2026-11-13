#!/usr/bin/env python3
"""Enumerate HST ACS/WFC UDF observations and unique RAW products from MAST.
Metadata only: no FITS bytes, calibration or registration are downloaded/run.
"""
from __future__ import annotations
import argparse, datetime as dt, json
from pathlib import Path
from astroquery.mast import Observations
import astroquery, astropy

PROPOSALS = [9978, 10086]
EXPECTED_RAW = 800
CRITERIA = {"obs_collection": "HST", "proposal_id": PROPOSALS, "instrument_name": "ACS/WFC"}

def clean(value):
    try:
        if value is None or bool(getattr(value, "mask", False)): return None
        if hasattr(value, "item"): value = value.item()
        if isinstance(value, bytes): return value.decode("utf-8", "replace")
        return value
    except Exception: return str(value)

def rows(table):
    return [{str(k): clean(row[k]) for k in table.colnames} for row in table]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output-dir", type=Path, required=True)
    out = ap.parse_args().output_dir
    out.mkdir(parents=True, exist_ok=True)
    observations = Observations.query_criteria(**CRITERIA)
    product_table = Observations.get_product_list(observations)
    obs_rows, product_rows = rows(observations), rows(product_table)
    unique = {}
    for row in product_rows:
        uri = row.get("dataURI")
        if uri: unique.setdefault(uri, row)
    products = list(unique.values())
    raw = sorted([p for p in products if p.get("productSubGroupDescription") == "RAW"],
                 key=lambda p: (str(p.get("productFilename")), str(p.get("dataURI"))))
    for name, data in [
        ("hubble_udf_observations.json", obs_rows),
        ("hubble_udf_products.json", products),
        ("hubble_udf_raw_exposures.json", raw),
    ]:
        (out / name).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    counts = {}
    for p in products:
        key = str(p.get("productSubGroupDescription"))
        counts[key] = counts.get(key, 0) + 1
    manifest = {
        "dataset": "Hubble Ultra Deep Field, ACS/WFC",
        "query_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "query_criteria": CRITERIA, "astroquery_version": astroquery.__version__,
        "astropy_version": astropy.__version__, "observation_count": len(obs_rows),
        "product_rows_before_deduplication": len(product_rows),
        "product_count_unique_dataURI": len(products),
        "product_duplicate_rows_collapsed": len(product_rows) - len(products),
        "raw_exposure_count_unique_dataURI": len(raw),
        "products_by_subgroup_unique_dataURI": counts,
        "files": {"observations": "hubble_udf_observations.json",
                  "products": "hubble_udf_products.json",
                  "raw_exposure_ids": "hubble_udf_raw_exposures.json"},
        "download_status": "METADATA_ONLY - no FITS exposure products downloaded",
        "reproducibility_status": "Observation and product URIs enumerated; FITS bytes, CRDS calibration context, and registration logs are not included."
    }
    (out / "hubble_udf_mast_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))
    if len(raw) != EXPECTED_RAW:
        raise SystemExit(f"Expected {EXPECTED_RAW} unique RAW products; found {len(raw)}")

if __name__ == "__main__": main()
