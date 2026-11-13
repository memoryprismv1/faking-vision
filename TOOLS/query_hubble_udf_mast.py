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
        item = {field: clean(row[field]) for field in available}
        if item.get("productSubGroupDescription") == 0.0:
            item["productSubGroupDescription"] = None
        result.append(item)
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
    product_rows = records(products, PRODUCT_FIELDS) if len(products) else []
    # MAST may associate the same file with multiple observation records.
    # Preserve each product once and retain all associated MAST obsIDs.
    product_map = {}
    for row in product_rows:
        uri = row.get("dataURI")
        if not uri:
            continue
        if uri not in product_map:
            product_map[uri] = {**row, "associated_obsIDs": []}
        obs_id = row.get("obsID")
        if obs_id is not None and obs_id not in product_map[uri]["associated_obsIDs"]:
            product_map[uri]["associated_obsIDs"].append(obs_id)
    product_records = list(product_map.values())
    raw_exposures = [p for p in product_records if p.get("productSubGroupDescription") == "RAW"]

    # MAST observation IDs are association-level names; the RAW exposure
    # rootnames share their first six characters with the corresponding
    # observation ID. Validate that this join resolves uniquely.
    prefix_map = {}
    for observation in obs_records:
        obs_id = str(observation.get("obs_id") or "")
        prefix = obs_id[:6]
        if not prefix or prefix.lower().startswith("hst_"):
            continue
        entry = prefix_map.setdefault(prefix, {"filters": set(), "proposals": set(), "obs_ids": set()})
        if observation.get("filters") is not None:
            entry["filters"].add(str(observation["filters"]))
        if observation.get("proposal_id") is not None:
            entry["proposals"].add(str(observation["proposal_id"]))
        entry["obs_ids"].add(obs_id)
    filter_counts = {}
    proposal_filter_counts = {}
    filter_join_failures = []
    for exposure in raw_exposures:
        filename = str(exposure.get("productFilename") or "")
        prefix = filename[:6]
        entry = prefix_map.get(prefix)
        if entry and len(entry["filters"]) == 1 and len(entry["proposals"]) == 1:
            exposure["obs_id_prefix"] = prefix
            exposure["filter"] = next(iter(entry["filters"]))
            exposure["proposal_id"] = next(iter(entry["proposals"]))
            exposure["filter_mapping_status"] = "UNAMBIGUOUS_OBS_ID_PREFIX_JOIN"
            filter_counts[exposure["filter"]] = filter_counts.get(exposure["filter"], 0) + 1
            key = f'{exposure["proposal_id"]}:{exposure["filter"]}'
            proposal_filter_counts[key] = proposal_filter_counts.get(key, 0) + 1
        else:
            exposure["obs_id_prefix"] = prefix
            exposure["filter"] = None
            exposure["proposal_id"] = None
            exposure["filter_mapping_status"] = "UNRESOLVED_OR_AMBIGUOUS"
            filter_join_failures.append(filename)

    obs_path = out / "hubble_udf_observations.json"
    product_path = out / "hubble_udf_products.json"
    raw_path = out / "hubble_udf_raw_exposures.json"
    obs_path.write_text(json.dumps(obs_records, indent=2) + "\n", encoding="utf-8")
    product_path.write_text(json.dumps(product_records, indent=2) + "\n", encoding="utf-8")
    raw_path.write_text(json.dumps(raw_exposures, indent=2) + "\n", encoding="utf-8")

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
        key = str(row.get("productSubGroupDescription") or "UNSPECIFIED")
        by_subgroup[key] = by_subgroup.get(key, 0) + 1

    summary = {
        "dataset": "Hubble Ultra Deep Field, ACS/WFC",
        "query_time_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "query_criteria": criteria,
        "astroquery_version": astroquery.__version__,
        "astropy_version": astropy.__version__,
        "observation_count": len(obs_records),
        "product_count_unique_dataURI": len(product_records),
        "raw_exposure_count_unique_dataURI": len(raw_exposures),
        "raw_exposures_by_filter_prefix_join": filter_counts,
        "raw_exposures_by_proposal_and_filter_prefix_join": proposal_filter_counts,
        "raw_exposure_filter_join_failures": filter_join_failures,
        "raw_exposure_filter_join_complete": len(filter_join_failures) == 0,
        "product_rows_before_deduplication": len(product_rows),
        "product_duplicate_rows_collapsed": len(product_rows) - len(product_records),
        "observations_by_proposal": by_program,
        "observations_by_filter": by_filter,
        "products_by_subgroup_unique_dataURI": by_subgroup,
        "files": {
            "observations": obs_path.name,
            "products": product_path.name,
            "raw_exposure_ids": raw_path.name,
        },
        "download_status": "METADATA_ONLY - no FITS exposure products downloaded",
        "reproducibility_status": (
            "MAST observation records and deduplicated product URIs are enumerated. "
            "The unique RAW product list identifies the original exposure files. "
            "FITS exposure bytes, calibration reference files/CRDS context, "
            "and registration/reprojection logs are not downloaded or reproduced by this query."
        ),
    }
    (out / "hubble_udf_mast_manifest.json").write_text(
        json.dumps(summary, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
