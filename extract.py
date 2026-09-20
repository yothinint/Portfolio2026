#!/usr/bin/env python3
"""
แกะ .pptx ที่ export จาก Google Slides → ภาพ WebP + ลิงก์วิดีโอ (จับคู่กับภาพปกให้ด้วย)

ใช้:  python3 extract.py ~/Downloads/xxx.pptx
ได้:  img/s07-1.webp ...      ภาพเนื้อหา เรียงตามตำแหน่งบนสไลด์
      img/poster/s07-v1.webp  ภาพปกของวิดีโอ
      extracted.json          ข้อมูลทั้งหมดต่อสไลด์
"""
import hashlib, io, json, os, re, shutil, sys, zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from PIL import Image

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
}
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
POST = os.path.join(IMG, "poster")
TMP = os.path.join(HERE, ".pptx_tmp")

YT = re.compile(r"(?:youtube\.com/(?:watch\?v=|embed/|v/)|youtu\.be/)([\w-]{11})")
GD = re.compile(r"drive\.google\.com/(?:file/d/|open\?id=|uc\?id=)([\w-]{20,})")

MAX_W, QUALITY = 1600, 80
DECOR_MIN_SLIDES = 4      # ภาพเดียวกันโผล่ตั้งแต่กี่สไลด์ = พื้นหลัง/ของตกแต่ง
MIN_SIDE = 300            # เล็กกว่านี้ = ไอคอน/โลโก้
MAX_RATIO = 3.0           # ผอม/แบนเกินนี้ = แถบโลโก้


def vid_of(url):
    m = YT.search(url)
    if m:
        return {"type": "youtube", "id": m.group(1)}
    m = GD.search(url)
    if m:
        return {"type": "drive", "id": m.group(1)}
    return None


def save_webp(src_path, out_path):
    im = Image.open(src_path)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(bg, im).convert("RGB")
    else:
        im = im.convert("RGB")
    if im.width > MAX_W:
        im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
    im.save(out_path, "WEBP", quality=QUALITY, method=5)
    return im.size


def main():
    if len(sys.argv) < 2:
        sys.exit("ใช้:  python3 extract.py <ไฟล์.pptx>")
    pptx = os.path.expanduser(sys.argv[1])
    if not os.path.exists(pptx):
        sys.exit("ไม่พบไฟล์: " + pptx)

    shutil.rmtree(TMP, ignore_errors=True)
    shutil.rmtree(IMG, ignore_errors=True)
    os.makedirs(POST, exist_ok=True)
    with zipfile.ZipFile(pptx) as z:
        z.extractall(TMP)

    sdir = os.path.join(TMP, "ppt", "slides")
    names = sorted((f for f in os.listdir(sdir) if f.endswith(".xml")),
                   key=lambda n: int(re.search(r"\d+", n).group()))

    # ---------- รอบแรก: อ่านโครงสร้าง ----------
    raw, hash_slides = {}, defaultdict(set)
    for name in names:
        n = int(re.search(r"\d+", name).group())
        rels = {}
        rp = os.path.join(sdir, "_rels", name + ".rels")
        if os.path.exists(rp):
            for rel in ET.parse(rp).getroot():
                rels[rel.get("Id")] = (rel.get("Target", ""), rel.get("TargetMode", ""))

        tree = ET.parse(os.path.join(sdir, name))
        vids, pics = [], []

        for pic in tree.iter(f"{{{NS['p']}}}pic"):
            blip = pic.find(".//a:blip", NS)
            embed = blip.get(f"{R}embed") if blip is not None else None
            src = None
            if embed and embed in rels:
                cand = os.path.normpath(os.path.join(sdir, rels[embed][0]))
                if os.path.exists(cand):
                    src = cand

            off = pic.find(".//a:off", NS)
            ext = pic.find(".//a:ext", NS)
            x = int(off.get("x", 0)) if off is not None else 0
            y = int(off.get("y", 0)) if off is not None else 0
            cx = int(ext.get("cx", 0)) if ext is not None else 0
            cy = int(ext.get("cy", 0)) if ext is not None else 0

            # Google Slides export วิดีโอเป็นรูป + hyperlink ไปคลิป (ไม่ใช่ a:videoFile)
            cnv = pic.find(".//p:cNvPr", NS)
            link_url = ""
            title = ""
            if cnv is not None:
                title = cnv.get("title") or cnv.get("descr") or ""
                hl = cnv.find("a:hlinkClick", NS)
                if hl is not None:
                    rid = hl.get(f"{R}id")
                    if rid in rels and rels[rid][1] == "External":
                        link_url = rels[rid][0]
            vf = pic.find(".//a:videoFile", NS)
            if vf is not None and not link_url:
                rid = vf.get(f"{R}link")
                if rid in rels:
                    link_url = rels[rid][0]

            v = vid_of(link_url) if link_url else None
            if v:
                vids.append({**v, "poster_src": src, "title": title, "x": x, "y": y, "cx": cx, "cy": cy})
                continue

            if src:
                pics.append({"src": src, "x": x, "y": y, "cx": cx})
                hash_slides[hashlib.md5(open(src, "rb").read()).hexdigest()].add(n)

        # กันลิงก์ที่หลุดจากโครงสร้าง (เผื่อไว้)
        body = open(os.path.join(sdir, name), encoding="utf-8").read()
        known = {(v["type"], v["id"]) for v in vids}
        for url in re.findall(r'https?://[^"\'<>\s]+', body):
            v = vid_of(url)
            if v and (v["type"], v["id"]) not in known:
                known.add((v["type"], v["id"]))
                vids.append({**v, "poster_src": None, "title": "", "x": 0, "y": 0, "cx": 0, "cy": 0})

        raw[n] = {"videos": vids, "pics": pics}

    decor = {h for h, s in hash_slides.items() if len(s) >= DECOR_MIN_SLIDES}

    # ---------- รอบสอง: แปลงภาพ ----------
    out, stats = {}, {"kept": 0, "decor": 0, "small": 0, "poster": 0}
    for n in sorted(raw):
        d = raw[n]
        videos = []
        for i, v in enumerate(d["videos"], 1):
            rec = {"type": v["type"], "id": v["id"]}
            lab = re.sub(r"\.(mp4|mov|m4v|avi|wmv)$", "", (v.get("title") or "").strip(), flags=re.I)
            if lab:
                rec["label"] = lab
            if v.get("cx") and v.get("cy"):
                rec["ar"] = round(v["cx"] / v["cy"], 4)
            if v["poster_src"]:
                p = os.path.join(POST, f"s{n:02d}-v{i}.webp")
                save_webp(v["poster_src"], p)
                rec["poster"] = "img/poster/" + os.path.basename(p)
                stats["poster"] += 1
            videos.append(rec)

        images, idx = [], 0
        for pic in sorted(d["pics"], key=lambda q: (q["y"], q["x"])):
            h = hashlib.md5(open(pic["src"], "rb").read()).hexdigest()
            if h in decor:
                stats["decor"] += 1
                continue
            im = Image.open(pic["src"])
            w, ht = im.size
            if min(w, ht) < MIN_SIDE or max(w, ht) / max(min(w, ht), 1) > MAX_RATIO:
                stats["small"] += 1
                continue
            idx += 1
            p = os.path.join(IMG, f"s{n:02d}-{idx}.webp")
            save_webp(pic["src"], p)
            images.append("img/" + os.path.basename(p))
            stats["kept"] += 1

        out[n] = {"videos": videos, "images": images}

    shutil.rmtree(TMP, ignore_errors=True)
    with open(os.path.join(HERE, "extracted.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"\n{len(out)} สไลด์ · เก็บภาพ {stats['kept']} · ภาพปกวิดีโอ {stats['poster']}"
          f" · ตัดพื้นหลัง {stats['decor']} · ตัดโลโก้ {stats['small']}")
    print("-" * 58)
    for n, d in out.items():
        if d["videos"] or d["images"]:
            print(f"สไลด์ {n:>2}: วิดีโอ {len(d['videos'])} · ภาพ {len(d['images'])}")
            for v in d["videos"]:
                print(f"           {v['type']:<7} {v['id']}  {'ปก✓' if v.get('poster') else 'ปก✗'}  {v.get('label','')}")
    print("-" * 58)


if __name__ == "__main__":
    main()
