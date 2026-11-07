#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys, zipfile
from pathlib import Path

src=Path(sys.argv[1] if len(sys.argv)>1 else "intake")
delivery=src/"delivery"
delivery.mkdir(parents=True,exist_ok=True)
raw=src/"downloads"
bundle=delivery/"fv-original-source-material.zip"
manifest=[]
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()
with zipfile.ZipFile(bundle,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=1) as z:
    for p in sorted(raw.rglob("*")):
        if not p.is_file(): continue
        rel=p.relative_to(src).as_posix()
        z.write(p,rel)
        manifest.append({"path":rel,"bytes":p.stat().st_size,"sha256":digest(p)})
    z.writestr("SOURCE_FILE_MANIFEST.json",json.dumps(manifest,indent=2))
chunk=70*1024*1024
h=digest(bundle)
parts=[]
with bundle.open("rb") as f:
    i=0
    while True:
        data=f.read(chunk)
        if not data: break
        p=delivery/("source-part-%02d"%i)
        p.write_bytes(data)
        parts.append({"path":p.name,"bytes":p.stat().st_size,"sha256":digest(p)})
        i+=1
join_py="""from pathlib import Path
import zipfile
parts=sorted(Path(".").glob("source-part-*"))
out=Path("fv-original-source-material.zip")
with out.open("wb") as w:
    for p in parts:
        with p.open("rb") as r:
            while True:
                b=r.read(1024*1024)
                if not b: break
                w.write(b)
with zipfile.ZipFile(out) as z:
    bad=z.testzip()
    if bad: raise SystemExit("ZIP CRC failure: "+bad)
print("Reassembled and CRC-verified:",out)
"""
(delivery/"join_and_verify.py").write_text(join_py,encoding="utf-8")
(delivery/"transfer_manifest.json").write_text(json.dumps({
 "bundle":"fv-original-source-material.zip","bundle_bytes":bundle.stat().st_size,
 "bundle_sha256":h,"chunk_bytes":chunk,"parts":parts,"source_files":manifest
},indent=2),encoding="utf-8")
receipt=delivery/"fv-dataset-receipts.zip"
with zipfile.ZipFile(receipt,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(src.rglob("*")):
        if not p.is_file(): continue
        rel=p.relative_to(src).as_posix()
        if rel == "RECEIPTS.md" or rel.startswith("inspection/"):
            # Keep inspection originals and contact sheets; skip no receipt data.
            z.write(p,rel)
print("SOURCE BUNDLE",bundle.stat().st_size,"bytes","sha256",h)
print("CHUNKS",len(parts))
print("RECEIPT ZIP",receipt.stat().st_size,"bytes")
