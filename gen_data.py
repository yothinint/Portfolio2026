#!/usr/bin/env python3
"""สร้าง data.js จาก extracted.json + การจัดหมวดที่กำหนดไว้ด้านล่าง"""
import json, os
from PIL import Image, ImageStat

HERE = os.path.dirname(os.path.abspath(__file__))
EX = json.load(open(os.path.join(HERE, "extracted.json"), encoding="utf-8"))

DROP = {"img/s01-1.webp", "img/s01-2.webp", "img/s03-2.webp", "img/s03-4.webp"}   # รูปเดิม + ตราสัญลักษณ์ + ภาพเอกสาร

def imgs(slide):
    return [p for p in EX[str(slide)]["images"] if p not in DROP]

def blank(path):
    """ปกที่เป็นเฟรมดำ/ขาวล้วน — ไม่เอามาใช้ ให้เว็บวาดพื้นหลังแทน"""
    im = Image.open(os.path.join(HERE, path)).convert("RGB").resize((64, 64))
    st = ImageStat.Stat(im)
    return sum(st.stddev) / 3 < 28

def vids(slide, labels=None):
    out = []
    for i, v in enumerate(EX[str(slide)]["videos"]):
        rec = {"type": v["type"], "id": v["id"]}
        if labels and i < len(labels) and labels[i]:
            rec["label"] = labels[i]
        # สัดส่วน: เชื่อขนาดภาพปกจริงก่อน (คือเฟรมของคลิป) — ถ้าปกเป็น placeholder
        # เล็ก ๆ ของ Google ค่อยถอยไปใช้ 16:9 เพราะกล่องบนสไลด์วาดมั่วได้
        p = v.get("poster")
        ar = None
        if p:
            w, h = Image.open(os.path.join(HERE, p)).size
            ar = round(w / h, 4) if min(w, h) >= 400 else 1.7778
        rec["ar"] = ar or v.get("ar") or 1.7778
        if p and not blank(p):
            rec["poster"] = p
        out.append(rec)
    return out

SITE = {
    "name": "โยธิน อินทรภิรมย์",
    "nameEn": "Yothin Intaraphirom",
    "nickname": "โย",
    "role": "Video Editor & Motion Designer",
    "photo": "img/profile.webp",
    "avatar": "img/avatar.webp",
    "links": [{"label": "อีเมล", "url": "mailto:yothin42@gmail.com"}],
}

PROFILE = {
    "education": {"degree": "วท.บ. สาธารณสุขศาสตร์", "major": "สาขาสุขศึกษาและส่งเสริมสุขภาพ"},
    "learn": ["ความรู้ทางวิทยาศาสตร์สุขภาพ", "การบริหาร / การจัดฝึกอบรม",
              "จิตวิทยาและพฤติกรรมศาสตร์", "นิเทศศาสตร์"],
    "do": ["วิเคราะห์และวางแผนการจัดโครงการและการฝึกอบรม โดยใช้หลักจิตวิทยามาประกอบ",
           "จัดทำสื่อต่าง ๆ เพื่อการสื่อสารที่ง่ายขึ้น"],
    "jobs": ["เตรียม Script และ Story Board สำหรับการถ่ายทำ",
             "จัดสถานที่สำหรับถ่ายทำ ดูแลเรื่องแสง เสียง และอุปกรณ์อื่น ๆ ที่จำเป็นในการถ่ายทำงานนั้น ๆ",
             "ถ่ายทำวิดีโอทั้งงานตั้งกล้องและงานเดินถ่าย เช่น งาน Event หรือคอนเทนต์ที่ต้องมีการแนะนำสินค้า",
             "ถ่ายภาพนิ่งทั้งงาน Event ภาพนิ่งสำหรับทำ Thumbnail และภาพเพื่อใช้ทำโปรโมทต่าง ๆ",
             "งาน Motion Graphic สำหรับใช้ในวิดีโอต่าง ๆ หรือสำหรับใช้เพื่อยิง Ad ใน Social Media",
             "งานวิดีโอและ Motion Graphic เพื่อใช้กับองค์กรใหญ่ ๆ เช่น SCBX, Kbank, True Business, NITMX"],
    "university": [
        {"title": "ชมรมอีสาน มหาวิทยาลัยมหิดล (ประธานชมรม)",
         "items": ["กิจกรรมแรกพบชมรมอีสาน มหาวิทยาลัยมหิดล",
                   "ค่ายจิตอาสาชมรมอีสาน — โรงเรียนบ้านหนองโดน อ.ปักธงชัย จ.นครราชสีมา",
                   "ค่ายจิตอาสาชมรมอีสาน — โรงเรียนบ้านโนนสะอาด อ.กุดรัง จ.มหาสารคาม"],
         "images": imgs(3)},
        {"title": "การจัดกิจกรรมและการฝึกอบรม",
         "items": ["จัดอบรมการพูดในที่สาธารณะ (Public Speaking)",
                   "ผู้นำทีมจัดกิจกรรมส่งเสริมสุขภาพ ชุมชนวัดมะกอกกลางสวน กทม."],
         "images": imgs(4)},
    ],
}

GROUPS = [
    {"org": "MEZ Motowork Co., Ltd.", "role": "Video Editor", "period": "May 2021 – Feb 2022",
     "works": [
        {"title": "MEZ Motowork", "desc": "งานตัดต่อวิดีโอโปรโมทยางมอเตอร์ไซค์ METZELER",
         "videos": vids(5, ["METZELER Z8 — Road Sport with StreetUppercut"]), "images": imgs(5)},
     ]},
    {"org": "Techsauce Media Co., Ltd.", "role": "Video Editor", "period": "Feb 2022 – Jul 2023",
     "works": [
        {"title": "Techsauce Media", "desc": "",
         "videos": vids(6, ["Major App — Mobile First"]), "images": imgs(6)},
        {"title": "Techsauce Global Summit 2022",
         "desc": "งานรวม Startup สาย Technology และเชิญ Speaker ที่เป็นระดับผู้บริหารจากทั่วโลกมาพูดในงาน วันที่ 26–27 สิงหาคม 2565 ที่ไอคอนสยาม",
         "videos": vids(7, ["วิดีโอ Highlight งาน"]), "images": imgs(7)},
        {"title": "NFT : Platfinder Club",
         "desc": "วิดีโอ Motion สำหรับการเปิดตัว NFT ของ Techsauce ในงาน Techsauce Global Summit 2022",
         "videos": vids(8, ["วิดีโอ Motion เปิดตัว NFT"]), "images": imgs(8)},
        {"title": "Thailand Accelerator",
         "desc": "งานที่จะช่วยเหลือบริษัท Startup รุ่นใหม่ ๆ ให้มีการเติบโตมากขึ้นในวงการธุรกิจไทย",
         "videos": vids(9, ["วิดีโองาน Press Conference"]), "images": imgs(9)},
        {"title": "MIT Media Lab Forum",
         "desc": "งานที่รวมนวัตกรรมจากสถาบันเทคโนโลยีแมสซาชูเซตส์ ประเทศสหรัฐอเมริกา ซึ่งเป็นงานที่นำมาจัดที่ South East Asia เป็นครั้งแรก และนำมาจัดที่กรุงเทพมหานคร ประเทศไทย",
         "videos": vids(10, ["วิดีโองาน Press Conference"]), "images": imgs(10)},
        {"title": "TS Short", "desc": "คลิปสั้นแนวตั้งสำหรับช่องทางโซเชียลของ Techsauce",
         "videos": vids(12, ["Saucy Thoughts — Gen Z จะเป็นเจ้าของกิจการที่เจ๋งกว่ารุ่นพ่อรุ่นแม่",
                             "Sustainable — Climate Crisis causes cancer risk"]), "images": imgs(12)},
     ]},
    {"org": "ประสบการณ์ทำงานอื่น ๆ", "role": "", "period": "",
     "works": [
        {"title": "SCBX Project", "desc": "",
         "bullets": ["SCBX : Next Tech — ทำวิดีโอเปิดงานเปิดตัวโซนพื้นที่ SCBX ที่สยามพารากอน ชั้น 4",
                     "SCBX : AI Journey — ทำ Motion Graphic สำหรับงาน AI Journey ภายในองค์กร SCBX ที่จะช่วยให้พนักงานเข้าใจลำดับและขั้นตอนการพัฒนาบุคลากรทางด้าน AI ในองค์กร"],
         "videos": vids(17, ["SCBX : Next Tech — Press Conference", "SCBX : AI Journey"]), "images": imgs(17)},
        {"title": "True Business", "desc": "ทำ Motion Graphic สำหรับยิง Ad Promotion ของ True Business",
         "videos": vids(18, ["True CPaaS", "One Call", "SMS Marketing", "M2M"]), "images": imgs(18)},
        {"title": "Thairath Money", "desc": "คลิปสั้นแนวตั้งให้กับ Thairath Money",
         "videos": vids(19, ["EP.03 L'Oréal", "EP.05 AP", "EP.08 TQM", "EP.11 SCB"]), "images": imgs(19)},
        {"title": "Money Monster",
         "desc": "ช่อง YouTube ที่มีผู้ติดตามกว่า 100,000 คน ของคุณทราย โศธิดา โชติวิจิตร เป็นเนื้อหาเกี่ยวกับการเงินและการลงทุน โดยมีลูกค้าเป็นผู้ให้บริการด้านการลงทุนชื่อดัง เช่น Binance, K Asset, The Wisdom, Dime, XM, Webull",
         "videos": vids(20, ["Binance", "K Asset", "Dime — เทศกาลลดหย่อนภาษี"]), "images": imgs(20)},
        {"title": "NITMX",
         "desc": "ผู้คิดค้นระบบ PromptPay ของประเทศไทย ที่ล่าสุดจัดงาน NITMX : Hack to the Max ที่เปิดโอกาสให้คนสมัครเข้ามาแข่ง Hackathon เพื่อหาผู้ชนะไปดูงานที่ Singapore FinTech Festival 2024 ที่ประเทศสิงคโปร์",
         "videos": vids(21, ["NITMX : Hack to the Max"]), "images": imgs(21)},
     ]},
]

def js(name, obj):
    return f"const {name} = " + json.dumps(obj, ensure_ascii=False, indent=2) + ";\n\n"

head = """/* ============================================================================
   ข้อมูลทั้งหมดของเว็บ — สร้างอัตโนมัติจากสไลด์ด้วย gen_data.py
   แก้ด้วยมือได้เลย (แต่ถ้ารัน gen_data.py ใหม่ ไฟล์นี้จะถูกเขียนทับ)

   วิดีโอ : { type:"drive"|"youtube", id:"...", label:"ชื่อคลิป", poster:"img/..." }
   ถ้าไม่มี poster เว็บจะวาดพื้นหลังไล่สีพร้อมปุ่มเล่นให้เอง
============================================================================ */

"""
with open(os.path.join(HERE, "data.js"), "w", encoding="utf-8") as f:
    f.write(head + js("SITE", SITE) + js("PROFILE", PROFILE) + js("GROUPS", GROUPS))

nv = sum(len(w["videos"]) for g in GROUPS for w in g["works"])
ni = sum(len(w["images"]) for g in GROUPS for w in g["works"])
np_ = sum(len(u["images"]) for u in PROFILE["university"])
noposter = sum(1 for g in GROUPS for w in g["works"] for v in w["videos"] if "poster" not in v)
print(f"data.js: วิดีโอ {nv} (ไม่มีปก {noposter}) · ภาพผลงาน {ni} · ภาพประวัติ {np_}")
