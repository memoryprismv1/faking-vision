#!/usr/bin/env python3
"""Query MAST for the Hubble Ultra Deep Field ACS/WFC observations.

This creates an observation/product manifest only. It does not download FITS
exposures or claim to reproduce calibration or image registration.
Requires astroquery and astropy.
"""
from __future__ import annotations
import argparse, datetime as dt, json
from pathlib import Path
import astroquery, astropy
from astroquery.mast import Observations

OBS_FIELDS = [
    "obsid", "obs_id", "obs_collection", "proposal_id", "target_name",
    "instrument_name", "filters", "t_min", "t_max", "s_ra", "s_dec",
    "calib_level", "dataURL"
]
PRODUCT_FIELDS = [
    "obsID", "productFilename", "productSubGroupDescription", "productType",
    "calib_level", "size", "dataURI"
]

def clean(value):
    if value is None:
        return None
    if hasattr(value, "item"):
        try:
            value = value.item()
        except Exception:
            pass
    if str(value) in {"--", "masked", "nan"}:
        return None
    return value if isinstance(value, (str, int, float, bool)) else str(value)

def records(table, fields):
    available = [f for f in fields if f in table.colnames]
    result = []
    for row in table:
        result.append({field: clean(row[field]) for field in available})
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    criteria = {
        "obs_collection": "HST",
        "proposal_id": [9978, 10086],
        "instrument_name": "ACS/WFC",
    }
    observations = Observations.query_criteria(**criteria)
    if len(observations) == 0:
        raise SystemExit("MAST returned zero ACS/WFC observations for proposals 9978/10086")

    obs_records = records(observations, OBS_FIELDS)
    products = Observations.get_product_list(observations)
    product_records = records(products, PRODUCT_FIELDS) if len(products) else []

    obs_path = out / "hubble_udf_observations.json"
    product_path = out / "hubble_udf_products.json"
    obs_path.write_text(json.dumps(obs_records, indent=2) + "\n", encoding="utf-8")
    product_path.write_text(json.dumps(product_records, indent=2) + "\n", encoding="utf-8")

    by_program = {}
    for row in obs_records:
        key = str(row.get("proposal_id"))
        by_program[key] = by_program.get(key, 0) + 1
    by_filter = {}
    for row in obs_records:
        key = str(row.get("filters"))
        by_filter[key] = by_filter.get(key, 0) + 1
    by_subgroup = {}
    for row in product_records:
        key = str(row.get("productSubGroupDescription"))
        by_subgroup[key] = by_subgroup.get(key, 0) + 1

    summary = {
        "dataset": "Hubble Ultra Deep Field, ACS/WFC",
        "query_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "query_criteria": criteria,
        "astroquery_version": astroquery.__version__,
        "astropy_version": astropy.__version__,
        "observation_count": len(obs_records),
        "product_count": len(product_records),
        "observations_by_proposal": by_program,
        "observations_by_filter": by_filter,
        "products_by_subgroup": by_subgroup,
        "files": {
            "observations": obs_path.name,
            "products": product_path.name,
        },
        "download_status": "METADATA_ONLY - no FITS exposure products downloaded",
        "reproducibility_status": (
            "Archive observation and product identifiers are enumerated. "
            "Raw exposure acquisition, calibration reference files/CRDS context, "
            "and registration/reprojection logs are not produced by this query."
        ),
    }
    (out / "hubble_udf_mast_manifest.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
