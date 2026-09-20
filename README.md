# Portfolio — โยธิน อินทรภิรมย์

เว็บสแตติก ไม่มี dependency ไม่มี build step · ดูบนมือถือได้ · dark mode อัตโนมัติ

```
index.html      โครงเว็บ + สไตล์ + สคริปต์   (ปกติไม่ต้องแตะ)
data.js         ข้อมูลทั้งหมด                  ← แก้ที่นี่
img/            ภาพจากสไลด์ + ภาพปกวิดีโอ (WebP) — ⚠️ extract.py ล้างโฟลเดอร์นี้ทุกครั้ง
photo/          รูปโปรไฟล์ (เก็บแยกไว้ไม่ให้โดนล้าง)
extract.py      แกะภาพ+ลิงก์วิดีโอจาก .pptx
gen_data.py     สร้าง data.js จากผลแกะ
extracted.json  ผลแกะดิบ
```

## โฟลเดอร์วิดีโอบน Drive

วิดีโอทั้ง 22 ตัวอยู่ใน Google Drive โฟลเดอร์เดียวชื่อ **Video** ตั้งเป็น "ทุกคนที่มีลิงก์ = ผู้อ่าน" แล้ว

https://drive.google.com/drive/folders/1CQ8gWdqFpZDubuYUZ79sf6vqsVZbla0X

คลิกขวาที่โฟลเดอร์ → **แชร์** → เปลี่ยนจาก "จำกัด" เป็น **"ทุกคนที่มีลิงก์"** → สิทธิ์ **ผู้อ่าน**

ไฟล์ข้างในจะได้สิทธิ์ตามโฟลเดอร์อัตโนมัติ ทำครั้งเดียวได้ครบทุกคลิป

> ✅ **แชร์เรียบร้อยแล้ว (20 ก.ย. 2569)** — ตรวจครบทั้ง 22 คลิป เปิดได้จากภายนอกทุกตัว

### เช็คว่าแชร์สำเร็จหรือยัง

```bash
curl -s -o /dev/null -w "%{http_code}\n" "https://drive.google.com/file/d/1gMf9UEeOc9txMhJ5f4HgD05kqpua6-US/view"
```

`200` = แชร์แล้ว · `401` = ยังไม่ได้แชร์

## โครงสร้างเว็บ

**Dropdown 1 — ประวัติส่วนตัว**
Education (พร้อมตรามหาวิทยาลัยมหิดล) · ประวัติการทำงาน · My Jobs · ประสบการณ์ในรั้วมหาวิทยาลัย 2 หัวข้อ พร้อมภาพ 22 ใบ

**Dropdown 2 — ผลงานบางส่วน** 15 หัวข้อ แบ่ง 3 กลุ่ม แต่ละหัวข้อเป็น dropdown ย่อย

| กลุ่ม | ผลงาน |
|---|---|
| ยาง Metzeler | MEZ Motowork |
| Techsauce | Techsauce Global Summit 2022 · NFT : Platfinder Club · Thailand Accelerator · MIT Media Lab Forum · TS Short |
| โปรเจกต์งาน Video ต่าง ๆ | Thairath Money · Money Monster · Skooldio · Happy Me Clinic · TTB Fintalk · Money Studio · SCBX Project · True Business · NITMX |

วิดีโอรวม 34 ตัว — Google Drive 14 ตัว (จากสไลด์) + YouTube 20 ตัว


## แก้ข้อมูล

แก้ `data.js` ตรง ๆ ได้เลย

```js
{
  type:  "drive",                  // หรือ "youtube"
  id:    "1gMf9UEeOc9txMhJ5f4...", // รหัสใน /file/d/___/view
  label: "วิดีโอ Highlight งาน",
  poster:"img/poster/s07-v1.webp", // ไม่ใส่ก็ได้ เว็บจะวาดพื้นหลังไล่สีให้
  ar:    1.7778                    // 1.7778 = 16:9, 0.5625 = 9:16
}
```

**อย่ารัน `gen_data.py` ซ้ำหลังแก้มือ** — มันจะเขียนทับ `data.js` ทั้งไฟล์

## ดึงข้อมูลจากสไลด์ใหม่ (ถ้าอัปเดตสไลด์)

```bash
cd ~/Desktop/video-portfolio && python3 extract.py ~/Downloads/*.pptx && python3 gen_data.py
```

`extract.py` จะแกะภาพเป็น WebP (ย่อกว้าง 1600px) ตัดพื้นหลังเทมเพลตกับโลโก้ออก และจับคู่วิดีโอกับภาพปกให้อัตโนมัติ

## ทดสอบในเครื่อง

อย่าดับเบิลคลิกเปิดไฟล์ตรง ๆ — `file://` ไม่มี origin ที่ Google ยอมรับ

```bash
cd ~/Desktop/video-portfolio && python3 -m http.server 8777
```

เปิด http://localhost:8777

## ขึ้น GitHub Pages

```bash
cd ~/Desktop/video-portfolio && git init && git add -A && git commit -m "portfolio" && git branch -M main
```

สร้าง repo เปล่าบน GitHub แล้ว push:

```bash
git remote add origin https://github.com/USERNAME/REPO.git && git push -u origin main
```

repo → **Settings → Pages** → Source = `Deploy from a branch`, Branch = `main` / `(root)` → Save

ได้ลิงก์ `https://USERNAME.github.io/REPO/` — อยากได้สั้นเป็น `https://USERNAME.github.io/` ให้ตั้งชื่อ repo ว่า `USERNAME.github.io` เป๊ะ ๆ

> ไฟล์ `extract.py`, `gen_data.py`, `extracted.json` ไม่ต้องขึ้นเว็บก็ได้ แต่ทิ้งไว้ก็ไม่เสียหาย (เว็บไม่ได้เรียกใช้)

## หมายเหตุ

- iframe โหลด **ตอนกดเล่นเท่านั้น** หน้าแรกจึงเบา · ปิดแล้วเสียงหยุดทันที
- ปิดตัวเล่น: Esc / คลิกพื้นหลัง / ปุ่ม ✕
- คลิปแนวตั้ง (TS Short, Thairath Money) เว็บจัดกริดให้เองอัตโนมัติ
- วิดีโอ 6 ตัวที่เฟรมแรกเป็นดำ/ขาวล้วน เว็บจะวาดพื้นหลังไล่สีแทน — อยากได้ปกสวยกว่านี้ แคปเฟรมเองแล้วใส่ `poster:`

## โทนสี

ดึงจากไฟล์ ref ที่ให้มา

| | |
|---|---|
| เหลือง | `#F2AB1D` |
| เทาเข้ม | `#3A3A3A` |
| พื้นหลัง | `#E1E1E1` |
| ฟอนต์ | Prompt (Google Fonts) |

dark mode สลับพื้นเป็น `#1A1A1A` โดยคงสีเหลืองไว้เหมือนเดิม

## หัวข้อย่อยใน 1 ผลงาน

ถ้าอยากแบ่งเป็นกลุ่มย่อยแบบ TTB Fintalk (Long form / Short form) ใช้ `sections`:

```js
{
  title: "TTB Fintalk",
  sections: [
    { label: "Long form",  videos: [ ... ] },
    { label: "Short form", videos: [ ... ] },
  ],
  videos: [], images: [],
}
```
