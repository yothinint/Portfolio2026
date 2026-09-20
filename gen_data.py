#!/usr/bin/env python3
"""สร้าง data.js จาก extracted.json (ผลแกะสไลด์) + ข้อมูลที่กำหนดไว้ด้านล่าง"""
import hashlib, json, os, re
from PIL import Image, ImageStat

HERE = os.path.dirname(os.path.abspath(__file__))
EX = json.load(open(os.path.join(HERE, "extracted.json"), encoding="utf-8"))

DROP = {"img/s01-1.webp", "img/s01-2.webp", "img/s03-2.webp", "img/s03-4.webp"}

def imgs(slide):
    return [p for p in EX[str(slide)]["images"] if p not in DROP]

def blank(path):
    im = Image.open(os.path.join(HERE, path)).convert("RGB").resize((64, 64))
    return sum(ImageStat.Stat(im).stddev) / 3 < 28

def drive(slide, labels=None):
    """วิดีโอ Google Drive ที่ฝังอยู่ในสไลด์"""
    out = []
    for i, v in enumerate(EX[str(slide)]["videos"]):
        rec = {"type": v["type"], "id": v["id"]}
        if labels and i < len(labels) and labels[i]:
            rec["label"] = labels[i]
        p = v.get("poster")
        ar = None
        if p:
            w, h = Image.open(os.path.join(HERE, p)).size
            ar = round(w / h, 4) if min(w, h) >= 400 else 1.7778
            if not blank(p):
                rec["poster"] = p
        rec["ar"] = ar or v.get("ar") or 1.7778
        out.append(rec)
    return out

YT = json.load(open("/tmp/yt.json", encoding="utf-8"))

def clean(t):
    t = re.split(r"\s+#\S", t)[0].strip()      # ตัดหางแฮชแท็กออก
    return re.sub(r"\s{2,}", " ", t)

def yt(group, n=None):
    """วิดีโอ YouTube — ดึงชื่อคลิปจริงมาเป็น label"""
    rows = YT[group][:n] if n else YT[group]
    return [{"type": "youtube", "id": r["id"], "label": clean(r["title"]),
             "ar": 0.5625 if r["short"] else 1.7778} for r in rows]

# ------------------------------------------------------------------ ข้อมูลส่วนตัว
SITE = {
    "name": "โยธิน อินทรภิรมย์",
    "nameEn": "Yothin Intaraphirom",
    "nickname": "โย",
    "role": "Senior Video Editor & Motion Designer",
    "photo": "photo/profile.webp",
    "avatar": "photo/avatar.webp",
    "contacts": [
        {"type": "โทรศัพท์", "value": "080-379-1992", "url": "tel:+66803791992", "icon": "phone"},
        {"type": "อีเมล", "value": "yothin42@gmail.com", "url": "mailto:yothin42@gmail.com", "icon": "mail"},
        {"type": "LINE", "value": "iryothin", "url": "https://line.me/ti/p/~iryothin", "icon": "line"},
    ],
}

PROFILE = {
    "education": {
        "degree": "วท.บ. สาธารณสุขศาสตร์",
        "major": "สาขาสุขศึกษาและส่งเสริมสุขภาพ",
        "university": "มหาวิทยาลัยมหิดล",
        "logo": "photo/mahidol.webp",
    },
    "jobs": [
        "เตรียม Script และ Story Board สำหรับการถ่ายทำ",
        "จัดสถานที่สำหรับถ่ายทำ ดูแลเรื่องแสง เสียง และอุปกรณ์อื่น ๆ ที่จำเป็นในการถ่ายทำงานนั้น ๆ",
        "ถ่ายทำวิดีโอทั้งงานตั้งกล้องและงานเดินถ่าย เช่น งาน Event หรือคอนเทนต์ที่ต้องมีการแนะนำสินค้า",
        "ถ่ายภาพนิ่งทั้งงาน Event ภาพนิ่งสำหรับทำ Thumbnail และภาพเพื่อใช้ทำโปรโมทต่าง ๆ",
        "งาน Motion Graphic สำหรับใช้ในวิดีโอต่าง ๆ หรือสำหรับใช้เพื่อยิง Ad ใน Social Media",
        "งานวิดีโอและ Motion Graphic เพื่อใช้กับองค์กรใหญ่ ๆ เช่น SCBX, Kbank, True Business, NITMX",
    ],
    "career": [
        {"org": "MEZ Motowork Co., Ltd."},
        {"org": "Techsauce Media Co., Ltd."},
        {"org": "Sino-Thai Communications Group Co., Ltd."},
        {"org": "LEARN Corporation Public Company Limited"},
        {"org": "Thairath Money", "role": "Senior Video Editor", "current": True},
    ],
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

# ---------------------------------------------------------------------- ผลงาน
SCBX = drive(17, ["SCBX : Next Tech — Press Conference", "SCBX : AI Journey"])

GROUPS = [
    {"org": "Video", "role": "", "period": "", "works": [
        {"title": "MEZ Motowork", "desc": "",
         "videos": drive(5, ["METZELER Z8 — Road Sport with StreetUppercut"]), "images": []},

        {"title": "Techsauce Global Summit 2022",
         "desc": "งานรวม Startup สาย Technology และเชิญ Speaker ที่เป็นระดับผู้บริหารจากทั่วโลกมาพูดในงาน วันที่ 26–27 สิงหาคม 2565 ที่ไอคอนสยาม",
         "videos": drive(7, ["วิดีโอ Highlight งาน"]), "images": imgs(7)},

        {"title": "MIT Media Lab Forum",
         "desc": "งานที่รวมนวัตกรรมจากสถาบันเทคโนโลยีแมสซาชูเซตส์ ประเทศสหรัฐอเมริกา ซึ่งเป็นงานที่นำมาจัดที่ South East Asia เป็นครั้งแรก และนำมาจัดที่กรุงเทพมหานคร ประเทศไทย",
         "videos": drive(10, ["วิดีโองาน Press Conference"]), "images": imgs(10)},

        {"title": "TS Short", "desc": "คลิปสั้นแนวตั้งสำหรับช่องทางโซเชียลของ Techsauce",
         "videos": drive(12, ["Saucy Thoughts — Gen Z จะเป็นเจ้าของกิจการที่เจ๋งกว่ารุ่นพ่อรุ่นแม่",
                              "Sustainable — Climate Crisis causes cancer risk"]), "images": imgs(12)},

        {"title": "Thairath Money", "desc": "", "videos": yt("Thairath Money"), "images": []},

        {"title": "Money Monster",
         "desc": "ช่อง YouTube ของคุณทราย โศธิดา โชติวิจิตร เนื้อหาเกี่ยวกับการเงินและการลงทุน มีผู้ติดตามรวมกันทุกช่องทางมากกว่า 1,000,000 คน",
         "videos": yt("Money Monster"), "images": []},

        {"title": "Skooldio", "desc": "", "videos": yt("Skooldio"), "images": []},

        {"title": "Happy Me Clinic", "desc": "", "videos": yt("Happy Me Clinic"), "images": []},

        {"title": "TTB Fintalk", "desc": "",
         "sections": [
            {"label": "Long form", "videos": yt("TTB Long")},
            {"label": "Short form", "videos": yt("TTB Short")},
         ], "videos": [], "images": []},

        {"title": "Money Studio", "desc": "", "videos": yt("Money Studio"), "images": []},

        {"title": "SCBX Project", "desc": "",
         "bullets": ["SCBX : Next Tech — ทำวิดีโอเปิดงานเปิดตัวโซนพื้นที่ SCBX ที่สยามพารากอน ชั้น 4"],
         "videos": SCBX[0:1], "images": []},

        {"title": "NITMX",
         "desc": "ผู้คิดค้นระบบ PromptPay ของประเทศไทย ที่ล่าสุดจัดงาน NITMX : Hack to the Max ที่เปิดโอกาสให้คนสมัครเข้ามาแข่ง Hackathon เพื่อหาผู้ชนะไปดูงานที่ Singapore FinTech Festival 2024 ที่ประเทศสิงคโปร์",
         "videos": drive(21, ["NITMX : Hack to the Max"]), "images": imgs(21)},
    ]},

    {"org": "Motion Graphic Video", "role": "", "period": "", "works": [
        {"title": "NFT : Platfinder Club",
         "desc": "วิดีโอ Motion สำหรับการเปิดตัว NFT ของ Techsauce ในงาน Techsauce Global Summit 2022",
         "videos": drive(8, ["วิดีโอ Motion เปิดตัว NFT"]), "images": imgs(8)},

        {"title": "Thailand Accelerator",
         "desc": "งานที่จะช่วยเหลือบริษัท Startup รุ่นใหม่ ๆ ให้มีการเติบโตมากขึ้นในวงการธุรกิจไทย",
         "videos": drive(9, ["วิดีโองาน Press Conference"]), "images": imgs(9)},

        {"title": "SCBX Project", "desc": "",
         "bullets": ["SCBX : AI Journey — ทำ Motion Graphic สำหรับงาน AI Journey ภายในองค์กร SCBX ที่จะช่วยให้พนักงานเข้าใจลำดับและขั้นตอนการพัฒนาบุคลากรทางด้าน AI ในองค์กร"],
         "videos": SCBX[1:2], "images": []},

        {"title": "True Business", "desc": "ทำ Motion Graphic สำหรับยิง Ad Promotion ของ True Business",
         "videos": drive(18, ["True CPaaS", "One Call", "SMS Marketing", "M2M"]), "images": imgs(18)},
    ]},
]

def js(name, obj):
    return f"const {name} = " + json.dumps(obj, ensure_ascii=False, indent=2) + ";\n\n"

head = """/* ============================================================================
   ข้อมูลทั้งหมดของเว็บ — สร้างอัตโนมัติด้วย gen_data.py
   แก้ด้วยมือได้ แต่ถ้ารัน gen_data.py ใหม่ ไฟล์นี้จะถูกเขียนทับ

   วิดีโอ : { type:"youtube"|"drive", id:"...", label:"...", ar:1.7778, poster:"..." }
            ar 1.7778 = 16:9 · 0.5625 = 9:16 · 1 = 1:1
            YouTube ไม่ต้องใส่ poster (ดึงจาก i.ytimg.com ให้เอง)
============================================================================ */

"""
with open(os.path.join(HERE, "data.js"), "w", encoding="utf-8") as f:
    f.write(head + js("SITE", SITE) + js("PROFILE", PROFILE) + js("GROUPS", GROUPS))

# แปะ hash ของ data.js ไว้ท้าย src ใน index.html — กันเบราว์เซอร์ใช้ไฟล์เก่าจากแคช
# (GitHub Pages ส่ง cache-control: max-age=600 มาให้ทุกไฟล์)
_dp = os.path.join(HERE, "data.js")
_h = hashlib.md5(open(_dp, "rb").read()).hexdigest()[:8]
_ip = os.path.join(HERE, "index.html")
_html = open(_ip, encoding="utf-8").read()
_new = re.sub(r'<script src="data\.js(?:\?v=[^"]*)?"></script>',
              f'<script src="data.js?v={_h}"></script>', _html)
if _new != _html:
    open(_ip, "w", encoding="utf-8").write(_new)
print(f"เวอร์ชัน data.js = {_h}")

def count(w):
    return len(w.get("videos", [])) + sum(len(s["videos"]) for s in w.get("sections", []))
nv = sum(count(w) for g in GROUPS for w in g["works"])
print(f"data.js: ผลงาน {sum(len(g['works']) for g in GROUPS)} หัวข้อ · วิดีโอ {nv} ตัว")
for g in GROUPS:
    print(f"  [{g['org']}]")
    for w in g["works"]:
        print(f"      {w['title']:<30} วิดีโอ {count(w)} · ภาพ {len(w.get('images',[]))}")
