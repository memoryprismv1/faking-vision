#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, math, shutil, sys, traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import requests

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "intake")
RAW, INSPECT = OUT / "downloads", OUT / "inspection"
RAW.mkdir(parents=True, exist_ok=True)
INSPECT.mkdir(parents=True, exist_ok=True)
S = requests.Session()
S.headers.update({"User-Agent": "FV-dataset-intake/1.0"})
R: list[dict[str, Any]] = []

def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def get(label,url,rel,description,source,expected="",notes=""):
    dest=RAW/rel; dest.parent.mkdir(parents=True,exist_ok=True)
    rec={"dataset":label,"status":"FAILED","url":url,"source_page":source,"description":description,
         "expected_size":expected,"notes":notes,"local_path":str(dest.relative_to(OUT))}
    try:
        with S.get(url,stream=True,timeout=(30,300),allow_redirects=True) as resp:
            rec["http_status"]=resp.status_code; rec["content_type"]=resp.headers.get("Content-Type")
            resp.raise_for_status(); n=0
            with dest.open("wb") as f:
                for chunk in resp.iter_content(1024*1024):
                    if chunk: f.write(chunk); n+=len(chunk)
            rec["final_url"]=resp.url
        if n<1024: raise RuntimeError("download unexpectedly small: %s bytes"%n)
        rec.update(status="DOWNLOADED",bytes=n,sha256=sha(dest),downloaded_utc=datetime.now(timezone.utc).isoformat())
        print("DOWNLOADED %s: %s bytes"%(label,n),flush=True)
        result=dest
    except Exception as e:
        rec["error"]=type(e).__name__+": "+str(e)
        print("FAILED %s: %s"%(label,rec["error"]),flush=True)
        dest.unlink(missing_ok=True); result=None
    R.append(rec); return result

def inventory_zip(path: Path, label: str):
    from zipfile import ZipFile
    inv=[]; dest=OUT/"extracted"/path.stem; dest.mkdir(parents=True,exist_ok=True)
    try:
        with ZipFile(path) as z:
            infos=z.infolist()
            for x in infos:
                inv.append({"name":x.filename,"bytes":x.file_size,"compressed_bytes":x.compress_size,"directory":x.is_dir()})
            total=sum(x.file_size for x in infos if not x.is_dir())
            if total<1_500_000_000:
                root=dest.resolve()
                for x in infos:
                    if x.is_dir(): continue
                    target=(dest/x.filename).resolve()
                    if root not in target.parents: continue
                    target.parent.mkdir(parents=True,exist_ok=True)
                    with z.open(x) as src,target.open("wb") as dst: shutil.copyfileobj(src,dst)
    except Exception as e: inv.append({"error":type(e).__name__+": "+str(e)})
    p=INSPECT/(path.stem+"_archive_inventory.json")
    p.write_text(json.dumps(inv,indent=2),encoding="utf-8")
    previews=make_previews(dest,path.stem)
    for rec in R:
        if rec["dataset"]==label:
            rec.update(archive_member_count=len(inv),archive_inventory=str(p.relative_to(OUT)),
                       preview_files=previews,image_member_count=sum(1 for x in inv if x.get("name","").lower().endswith((".tif",".tiff",".jpg",".jpeg",".png"))))
            break

def make_previews(root: Path,label: str):
    try:
        import numpy as np
        from PIL import Image,ImageOps,ImageDraw
        import tifffile
    except Exception as e: return ["Preview dependencies unavailable: "+str(e)]
    candidates=sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in (".tif",".tiff",".jpg",".jpeg",".png"))[:12]
    tiles=[]
    for p in candidates:
        try:
            if p.suffix.lower() in (".tif",".tiff"):
                with tifffile.TiffFile(p) as tf: arr=np.squeeze(tf.pages[0].asarray())
                if arr.ndim>2: arr=arr[0]
                if arr.ndim!=2: continue
                finite=arr[np.isfinite(arr)]
                if not finite.size: continue
                lo,hi=np.percentile(finite,[1,99])
                if hi<=lo: hi=lo+1
                im=Image.fromarray((np.clip((arr.astype("float32")-lo)/(hi-lo),0,1)*255).astype("uint8")).convert("RGB")
            else: im=ImageOps.autocontrast(Image.open(p).convert("RGB"))
            im.thumbnail((420,300))
            tile=Image.new("RGB",(460,350),"white")
            tile.paste(im,((460-im.width)//2,5))
            ImageDraw.Draw(tile).text((8,320),p.name[:65],fill="black")
            tiles.append(tile)
        except Exception as e: print("preview skipped %s: %s"%(p,e))
    if not tiles: return []
    sheet=Image.new("RGB",(1380,((len(tiles)+2)//3)*350),"#d8d8d8")
    for i,t in enumerate(tiles): sheet.paste(t,((i%3)*460,(i//3)*350))
    dest=INSPECT/"previews"/label; dest.mkdir(parents=True,exist_ok=True)
    f=dest/"contact_sheet.jpg"; sheet.save(f,quality=90)
    return [str(f.relative_to(OUT))]

def hst_visit():
    label="HST ACS/WFC F606W single-visit exposures"
    source="https://archive.stsci.edu/ ; https://docs.astropy.org/projects/astroquery/en/latest/mast/mast_obsquery.html"
    try:
        from astroquery.mast import Observations
        from astropy.io import fits
        import numpy as np
        from PIL import Image,ImageDraw
        obs=Observations.query_criteria(obs_collection="HST",proposal_id="10737",instrument_name="ACS/WFC",filters="F606W",dataRights="PUBLIC")
        if len(obs)==0: raise RuntimeError("No public proposal 10737 ACS/WFC F606W observations returned")
        if "target_name" in obs.colnames:
            mask=[("NGC 104" in str(x).upper()) or ("47 TUC" in str(x).upper()) for x in obs["target_name"]]
            if any(mask): obs=obs[mask]
        groups={}
        for i,row in enumerate(obs):
            oid=str(row["obs_id"]).strip()
            groups.setdefault(oid[:6],[]).append(i)
        options=sorted(groups.items(),key=lambda x:len(x[1]),reverse=True)
        chosen_key,idx=next(((k,v) for k,v in options if len(v)>=3),(None,[]))
        if not idx: raise RuntimeError("No visit-root group with at least three observations; refusing cross-visit substitution")
        selected=obs[idx]
        times=[float(x) for x in selected["t_min"]] if "t_min" in selected.colnames else []
        span=max(times)-min(times) if len(times)>1 else 0.0
        if span>2.0: raise RuntimeError("Candidate visit group spans %.2f days; rejecting grouping"%span)
        prods=Observations.get_product_list(selected)
        if "productSubGroupDescription" not in prods.colnames: raise RuntimeError("MAST product list has no FLC subgroup field")
        flc=prods[[str(x).upper()=="FLC" for x in prods["productSubGroupDescription"]]][:4]
        if len(flc)<3: raise RuntimeError("Selected group has fewer than three FLC products")
        dest=RAW/"hst_single_visit"; dest.mkdir(parents=True,exist_ok=True)
        manifest=Observations.download_products(flc,download_dir=str(dest))
        files=sorted(p for p in dest.rglob("*") if p.is_file() and p.name.lower().endswith("_flc.fits"))
        if len(files)<3: raise RuntimeError("Only %d calibrated FLC FITS products were downloaded"%len(files))
        exposures=[]
        for p in files:
            with fits.open(p,memmap=True) as hdul:
                h=hdul[0].header
                sci=next((x for x in hdul if x.name=="SCI" and x.data is not None),None)
                exposures.append({"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),
                    "date_obs":h.get("DATE-OBS"),"time_obs":h.get("TIME-OBS"),"exptime":h.get("EXPTIME"),
                    "filter1":h.get("FILTER1"),"filter2":h.get("FILTER2"),"proposal":h.get("PROPOSID"),
                    "visit_root":p.name[:6],"pa_v3":h.get("PA_V3"),
                    "science_shape":list(sci.data.shape) if sci is not None else None})
        rec={"dataset":label,"status":"DOWNLOADED","source_page":source,"local_path":str(dest.relative_to(OUT)),
             "query":{"obs_collection":"HST","proposal_id":"10737","instrument_name":"ACS/WFC","filters":"F606W",
                      "target_filter":"NGC 104 / 47 Tuc where available",
                      "grouping":"first six characters of obs_id; require >=3 exposures; reject span >2 days"},
             "visit_group":chosen_key,"exposure_count":len(files),"time_span_days":span,"exposures":exposures,
             "manifest_statuses":[str(x) for x in manifest["Status"]],
             "notes":"Candidate single-visit set based on archive rootname grouping and time-span check. Inspect FITS WCS and detector footprints before accepting as an overlap/assembly case."}
        R.append(rec); (INSPECT/"hst_single_visit_receipt.json").write_text(json.dumps(rec,indent=2),encoding="utf-8")
        print("DOWNLOADED HST visit %s (%d exposures)"%(chosen_key,len(files)),flush=True)
    except Exception as e:
        R.append({"dataset":label,"status":"FAILED","source_page":source,"error":type(e).__name__+": "+str(e),
                  "traceback":traceback.format_exc(),"notes":"No cross-visit substitution made."})
        print("FAILED HST visit: "+str(e),flush=True)

def usgs_probe():
    label="USGS 3DEP public EPT access probe"
    source="https://registry.opendata.aws/usgs-lidar/"
    try:
        import boto3
        from botocore import UNSIGNED
        from botocore.config import Config
        s3=boto3.client("s3",region_name="us-west-2",config=Config(signature_version=UNSIGNED))
        bucket="usgs-lidar-public"
        resp=s3.list_objects_v2(Bucket=bucket,Delimiter="/",MaxKeys=250)
        prefixes=[x["Prefix"] for x in resp.get("CommonPrefixes",[])]
        chosen=None; ept=None
        for pref in prefixes:
            try:
                o=s3.get_object(Bucket=bucket,Key=pref+"ept.json")
                chosen=pref; ept=json.loads(o["Body"].read()); break
            except Exception: continue
        if not chosen: raise RuntimeError("No EPT project found in first 250 public prefixes")
        base=RAW/"usgs_3dep_ept"; base.mkdir(parents=True,exist_ok=True)
        (base/"ept.json").write_text(json.dumps(ept,indent=2),encoding="utf-8")
        key=chosen+"ept-hierarchy/0-0-0-0.json"
        hierarchy=json.loads(s3.get_object(Bucket=bucket,Key=key)["Body"].read())
        (base/"0-0-0-0.json").write_text(json.dumps(hierarchy,indent=2),encoding="utf-8")
        point=chosen+"ept-data/0-0-0-0.laz"
        head=s3.head_object(Bucket=bucket,Key=point); size=int(head["ContentLength"])
        tiles=[]
        if size<=80_000_000:
            dest=base/"0-0-0-0.laz"; s3.download_file(bucket,point,str(dest))
            tiles.append({"key":point,"bytes":size,"sha256":sha(dest),"local_path":str(dest.relative_to(OUT))})
        rec={"dataset":label,"status":"DOWNLOADED" if tiles else "METADATA_ONLY","source_page":source,
             "bucket":bucket,"region":"us-west-2","project_prefix":chosen,"ept":ept,
             "hierarchy":hierarchy,"root_point_tile_size":size,"tiles":tiles,
             "license":"US Government Public Domain",
             "notes":"Bounded availability probe only. An EPT spatial subdivision is not proof of overlapping acquisition strips or a same-pass maplet set. Do not treat as a validated FV assembly input without checking the underlying survey metadata and neighboring coverage."}
        R.append(rec); (INSPECT/"usgs_3dep_ept_receipt.json").write_text(json.dumps(rec,indent=2),encoding="utf-8")
        print("USGS probe %s root point tile %s bytes"%(chosen,size),flush=True)
    except Exception as e:
        R.append({"dataset":label,"status":"FAILED","source_page":source,"error":type(e).__name__+": "+str(e),
                  "notes":"Public access is documented; this bounded programmatic probe did not complete."})
        print("FAILED USGS probe: "+str(e),flush=True)

def main():
    todo=[
      ("BigStitcher 2D six-tile microscopy grid","https://preibischlab.mdc-berlin.de/BigStitcher/Grid_2d.zip","microscopy/bigstitcher_grid_2d.zip",
       "Six 2D tiles, three channels; official example specifies a regular 2x3 grid with 10 percent overlap.",
       "https://imagej.net/plugins/bigstitcher/","2.8 MB","Raw input archive; aligned output project is not substituted."),
      ("BigStitcher 3D six-tile confocal grid","https://preibischlab.mdc-berlin.de/BigStitcher/Grid_3d.zip","microscopy/bigstitcher_grid_3d.zip",
       "Six 3D confocal tiles, three channels; volumetric tiled sample.",
       "https://imagej.net/plugins/bigstitcher/","123 MB","Needs 3D tile metadata inspection before FV use."),
      ("NIST MIST 5x5 Cy5 microscopy grid","https://github.com/usnistgov/MIST/wiki/testdata/Small_Fluorescent_Test_Dataset.zip","microscopy/nist_mist_5x5_cy5.zip",
       "Published 5x5 grid of 25 image tiles with approximately 10 percent overlap between consecutive tiles.",
       "https://github.com/usnistgov/MIST","about 32 MB","Official NIST project gives row/column naming and example results; 10x10 alternatives not fetched."),
      ("OpenDroneMap Mygla drone survey","https://github.com/merkato/odm_mygla_dataset/archive/refs/heads/master.zip","drone/odm_mygla_dataset.zip",
       "Published 29-image aerial dataset, about 150 MB, with EXIF coordinates.",
       "https://github.com/OpenDroneMap/ODMdata ; https://github.com/merkato/odm_mygla_dataset","about 150 MB",
       "Repository README credits Tomasz Nycz under CC BY 3.0; DJI P3S acquisition stated as 2012-02-08 at Tokarzonka.")
    ]
    for label,url,rel,desc,src,size,note in todo:
        p=get(label,url,rel,desc,src,size,note)
        if p: inventory_zip(p,label)
    hst_visit()
    usgs_probe()
    files=[]
    for p in sorted(RAW.rglob("*")):
        if p.is_file(): files.append({"path":str(p.relative_to(OUT)),"bytes":p.stat().st_size,"sha256":sha(p)})
    (INSPECT/"file_manifest.json").write_text(json.dumps(files,indent=2),encoding="utf-8")
    (INSPECT/"receipts.json").write_text(json.dumps(R,indent=2),encoding="utf-8")
    fields=sorted({k for x in R for k,v in x.items() if not isinstance(v,(dict,list))})
    with (INSPECT/"receipts.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for x in R: w.writerow({k:x.get(k) for k in fields})
    downloaded=sum(x.get("status")=="DOWNLOADED" for x in R)
    metadata=sum(x.get("status")=="METADATA_ONLY" for x in R)
    failed=sum(x.get("status")=="FAILED" for x in R)
    md=["# FV overlapping-media dataset intake receipts","",
        "Generated UTC: "+datetime.now(timezone.utc).isoformat(),"",
        "Intake/availability check only. No FV packet examples or PACKETS contents were changed.","",
        "Downloaded: %d | Metadata only: %d | Failed: %d"%(downloaded,metadata,failed),"",
        "## Dataset receipts",""]
    for x in R:
        md += ["### "+x.get("dataset","unnamed"),"- Status: "+x.get("status","UNKNOWN"),
               "- Source: "+x.get("source_page",x.get("url","")),
               "- Local path: "+x.get("local_path","see detailed receipt"),
               "- Notes: "+x.get("notes",x.get("description",""))]
        if x.get("bytes"): md.append("- Bytes: "+str(x["bytes"]))
        if x.get("sha256"): md.append("- SHA-256: "+x["sha256"])
        if x.get("error"): md.append("- Error: "+x["error"])
        md.append("")
    md += ["## Interpretation controls","",
       "- A catalogue entry is not considered acquired unless its receipt says DOWNLOADED.",
       "- An archive is not a valid assembly case until its contents, acquisition context, overlap, and metadata have been inspected.",
       "- The USGS EPT probe is an availability probe; spatial tiling alone does not prove acquisition overlap.",
       "- The HST sample is grouped by observation root and time span to avoid silently combining separate visits. FITS WCS and detector footprints still require inspection.",
       "- Original downloaded archives are retained unchanged; extracted copies and contact sheets are inspection aids.",
       "",
       "See inspection/receipts.json, receipts.csv, and file_manifest.json for machine-readable evidence."]
    (OUT/"RECEIPTS.md").write_text("\n".join(md),encoding="utf-8")
    print("INTAKE SUMMARY: downloaded=%d metadata_only=%d failed=%d"%(downloaded,metadata,failed),flush=True)

if __name__=="__main__": main()
