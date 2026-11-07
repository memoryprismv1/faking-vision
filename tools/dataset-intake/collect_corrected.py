#!/usr/bin/env python3
"""Corrected direct downloads for catalogued overlap and a documented single-visit ACS set."""
from __future__ import annotations
import hashlib, json, math, subprocess, sys, traceback, zipfile
from pathlib import Path
import requests

BASE=Path(sys.argv[1] if len(sys.argv)>1 else "intake")
RAW, INS = BASE/"downloads", BASE/"inspection"
RAW.mkdir(parents=True,exist_ok=True); INS.mkdir(parents=True,exist_ok=True)
S=requests.Session(); S.headers["User-Agent"]="FV-dataset-intake/1.2"
RECS=[]

def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def audit_exif(root):
    from PIL import Image
    files=sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".jpg",".jpeg",".tif",".tiff",".png"})
    rows=[]
    for p in files:
        try:
            im=Image.open(p); ex=im.getexif(); g={}
            try:
                v=ex.get_ifd(34853)
                if v:
                    def dms(x): return float(x[0])+float(x[1])/60+float(x[2])/3600
                    lat,lon=dms(v[2]),dms(v[4])
                    if v.get(1)=="S": lat=-lat
                    if v.get(3)=="W": lon=-lon
                    g={"lat":lat,"lon":lon}
            except Exception as e: g={"parse_error":str(e)}
            rows.append({"file":str(p.relative_to(BASE)),"width":im.width,"height":im.height,
                         "datetime":ex.get(36867) or ex.get(306),"gps":g})
        except Exception: pass
    tagged=[x for x in rows if "lat" in x.get("gps",{})]
    out={"file_count":len(files),"readable_count":len(rows),"geotagged_count":len(tagged),"images":rows}
    if tagged:
        out["gps_bounds"]={"min_lat":min(x["gps"]["lat"] for x in tagged),
                           "max_lat":max(x["gps"]["lat"] for x in tagged),
                           "min_lon":min(x["gps"]["lon"] for x in tagged),
                           "max_lon":max(x["gps"]["lon"] for x in tagged)}
        ordered=sorted(tagged,key=lambda x:x.get("datetime") or "")
        ds=[]
        for a,b in zip(ordered,ordered[1:]):
            la,loa=math.radians(a["gps"]["lat"]),math.radians(a["gps"]["lon"])
            lb,lob=math.radians(b["gps"]["lat"]),math.radians(b["gps"]["lon"])
            q=math.sin((lb-la)/2)**2+math.cos(la)*math.cos(lb)*math.sin((lob-loa)/2)**2
            ds.append(6371000*2*math.asin(math.sqrt(q)))
        if ds:
            ds.sort()
            out["successive_capture_position_distance_m"]={"min":min(ds),"median":ds[len(ds)//2],"max":max(ds),
                "note":"Capture-position spacing only; not a ground-footprint overlap measurement."}
    return out

def phalaborwa():
    label="OpenDroneMap Phalaborwa small overlap/sidelap survey"
    source="https://github.com/OpenDroneMap/ODMdata"
    folder="https://drive.google.com/drive/folders/1e1eA8LNpP4scYyDYdWd6UQ1qJ006iOXG"
    dest=RAW/"drone_phalaborwa_sm_ol"; dest.mkdir(parents=True,exist_ok=True)
    try:
        # gdown installed in workflow; --remaining-ok is not supported by all gdown versions.
        p=subprocess.run([sys.executable,"-m","gdown","--folder","--continue","-O",str(dest),folder],
                         capture_output=True,text=True,timeout=1800)
        imgs=sorted(x for x in dest.rglob("*") if x.is_file() and x.suffix.lower() in {".jpg",".jpeg",".tif",".tiff",".png"})
        total=sum(x.stat().st_size for x in dest.rglob("*") if x.is_file())
        if p.returncode!=0 or len(imgs)<10:
            raise RuntimeError("gdown return=%s images=%s stdout=%s stderr=%s"%(p.returncode,len(imgs),p.stdout[-1500:],p.stderr[-1500:]))
        audit=audit_exif(dest)
        (INS/"phalaborwa_sm_ol_exif_audit.json").write_text(json.dumps(audit,indent=2),encoding="utf-8")
        rec={"dataset":label,"status":"DOWNLOADED","source_page":source,"download_url":folder,
             "local_path":str(dest.relative_to(BASE)),"image_count":len(imgs),"total_bytes":total,
             "catalogue_claim":{"images":36,"size_mb":178,"exif_coordinates":True,"note":"For overlap/sidelap testing"},
             "exif_audit":{"geotagged_count":audit["geotagged_count"],"gps_bounds":audit.get("gps_bounds"),
                           "successive_capture_position_distance_m":audit.get("successive_capture_position_distance_m")},
             "notes":"OpenDroneMap catalogue explicitly identifies this collection for overlap/sidelap testing. Capture GPS spacing is not itself proof of image-footprint overlap; inspect the frames/pose geometry. Dataset reuse terms not verified in this intake."}
        RECS.append(rec); print("Phalaborwa DOWNLOADED images=%d bytes=%d GPS=%d"%(len(imgs),total,audit["geotagged_count"]),flush=True)
    except Exception as e:
        RECS.append({"dataset":label,"status":"FAILED","source_page":source,"download_url":folder,
                     "error":type(e).__name__+": "+str(e),"notes":"Catalog advertises 36 images/~178MB for overlap/sidelap testing; not counted as acquired."})
        print("Phalaborwa FAILED: "+str(e),flush=True)

def hst_m81_single_visit():
    label="HST ACS/WFC M81 GO-10605 single-visit F555W dither"
    source="https://hst-docs.stsci.edu/acsdhb/chapter-2-acs-data-structure/2-1-types-of-acs-files ; https://archive.stsci.edu/"
    try:
        from astroquery.mast import Observations
        from astropy.io import fits
        obs=Observations.query_criteria(obs_collection="HST",proposal_id="10605",instrument_name="ACS/WFC",
                                        filters="F555W",dataRights="PUBLIC")
        if len(obs)==0: raise RuntimeError("MAST returned no public ACS/WFC F555W observations for GO-10605")
        if "target_name" in obs.colnames:
            mask=["M81" in str(x).upper() for x in obs["target_name"]]
            if any(mask): obs=obs[mask]
        candidates=[]
        for i,row in enumerate(obs):
            products=Observations.get_product_list(obs[i])
            if "productSubGroupDescription" not in products.colnames or "productFilename" not in products.colnames:
                continue
            flc=products[[str(x).upper()=="FLC" for x in products["productSubGroupDescription"]]]
            groups={}
            for j,p in enumerate(flc):
                fname=str(p["productFilename"]).lower()
                if fname.endswith("_flc.fits") and len(fname)>=15:
                    root=fname.split("_")[0]
                    key=root[:6] # ACS rootname: instrument/program/visit; next chars distinguish visit exposures.
                    groups.setdefault(key,[]).append(j)
            for key,idx in groups.items():
                if len(idx)>=3:
                    candidates.append((len(idx),i,key,flc[idx]))
        if not candidates:
            raise RuntimeError("No MAST observation group yielded >=3 individual FLC files sharing a six-character ACS rootname visit prefix")
        candidates.sort(key=lambda x:x[0],reverse=True)
        _,obsidx,visit_prefix,flc=candidates[0]
        flc=flc[:6]
        dest=RAW/"hst_m81_go10605_single_visit"; dest.mkdir(parents=True,exist_ok=True)
        manifest=Observations.download_products(flc,download_dir=str(dest))
        files=sorted(p for p in dest.rglob("*") if p.is_file() and p.name.lower().endswith("_flc.fits"))
        if len(files)<3: raise RuntimeError("Only %d FLC files downloaded"%len(files))
        exposures=[]
        for p in files:
            with fits.open(p,memmap=True) as hdul:
                hdr=hdul[0].header
                sci=next((h for h in hdul if h.name=="SCI" and h.data is not None),None)
                exposures.append({"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),
                    "rootname":hdr.get("ROOTNAME"),"date_obs":hdr.get("DATE-OBS"),"time_obs":hdr.get("TIME-OBS"),
                    "exptime":hdr.get("EXPTIME"),"filter1":hdr.get("FILTER1"),"filter2":hdr.get("FILTER2"),
                    "proposal":hdr.get("PROPOSID"),"visitnum":hdr.get("VISITNUM"),"pa_v3":hdr.get("PA_V3"),
                    "science_shape":list(sci.data.shape) if sci is not None else None})
        prefixes=sorted({str(x["rootname"])[:6] for x in exposures if x["rootname"]})
        visitnums=sorted({str(x["visitnum"]) for x in exposures if x["visitnum"] is not None})
        status="DOWNLOADED" if len(prefixes)==1 and len(visitnums)<=1 else "DOWNLOADED_NEEDS_REVIEW"
        rec={"dataset":label,"status":status,"source_page":source,"local_path":str(dest.relative_to(BASE)),
             "proposal_id":"10605","target":"M81","instrument":"ACS/WFC","filter":"F555W",
             "observation_row":str(obs[obsidx]["obs_id"]) if "obs_id" in obs.colnames else obsidx,
             "visit_prefix":visit_prefix,"exposure_count":len(files),"root_prefixes":prefixes,"visitnums":visitnums,
             "exposures":exposures,"manifest_statuses":[str(x) for x in manifest["Status"]],
             "reference_description":"STScI ACS handbook documents GO-10605 visit 1 as a two-point ACS-WFC dither, with individual calibrated FLC examples j9cm01jvq, j9cm01jwq, j9cm01k2q, j9cm01k4q.",
             "notes":"Selected from MAST by a shared ACS six-character rootname prefix (proposal + visit), then independently checked FITS ROOTNAME/VISITNUM. Inspect WCS and detector footprints; this is a candidate single-visit set, not yet an FV assembly result."}
        RECS.append(rec); print("HST M81 %s prefix=%s exposures=%d visitnums=%s"%(status,visit_prefix,len(files),visitnums),flush=True)
    except Exception as e:
        RECS.append({"dataset":label,"status":"FAILED","source_page":source,"error":type(e).__name__+": "+str(e),
                     "traceback":traceback.format_exc(),"notes":"The documented STScI example is the intended query; no cross-visit substitution is made."})
        print("HST M81 FAILED: "+str(e),flush=True)

def main():
    # Auditable EXIF for Mygla, already downloaded by the baseline collector.
    mygla=BASE/"extracted"/"odm_mygla_dataset"
    if mygla.exists():
        audit=audit_exif(mygla)
        (INS/"odm_mygla_exif_audit.json").write_text(json.dumps(audit,indent=2),encoding="utf-8")
        print("Mygla EXIF files=%s geotagged=%s bounds=%s"%(audit["file_count"],audit["geotagged_count"],audit.get("gps_bounds")),flush=True)
    phalaborwa()
    hst_m81_single_visit()
    (INS/"corrected_receipts.json").write_text(json.dumps(RECS,indent=2),encoding="utf-8")
    with (BASE/"RECEIPTS.md").open("a",encoding="utf-8") as f:
        f.write("\n\n# Corrected follow-up acquisition\n")
        for r in RECS:
            f.write("\n## "+r.get("dataset","unnamed")+"\n")
            f.write("- Status: **"+r.get("status","UNKNOWN")+"**\n")
            f.write("- Source: "+r.get("source_page","")+"\n")
            f.write("- Notes: "+r.get("notes",r.get("error",""))+"\n")
    print("CORRECTED SUMMARY: "+json.dumps({r["dataset"]:r["status"] for r in RECS}),flush=True)

if __name__=="__main__": main()
