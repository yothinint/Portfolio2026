/* ============================================================================
   ข้อมูลทั้งหมดของเว็บ — สร้างอัตโนมัติจากสไลด์ด้วย gen_data.py
   แก้ด้วยมือได้เลย (แต่ถ้ารัน gen_data.py ใหม่ ไฟล์นี้จะถูกเขียนทับ)

   วิดีโอ : { type:"drive"|"youtube", id:"...", label:"ชื่อคลิป", poster:"img/..." }
   ถ้าไม่มี poster เว็บจะวาดพื้นหลังไล่สีพร้อมปุ่มเล่นให้เอง
============================================================================ */

const SITE = {
  "name": "โยธิน อินทรภิรมย์",
  "nameEn": "Yothin Intaraphirom",
  "nickname": "โย",
  "role": "Video Editor & Motion Designer",
  "photo": "img/profile.webp",
  "avatar": "img/avatar.webp",
  "links": [
    {
      "label": "อีเมล",
      "url": "mailto:yothin42@gmail.com"
    }
  ]
};

const PROFILE = {
  "education": {
    "degree": "วท.บ. สาธารณสุขศาสตร์",
    "major": "สาขาสุขศึกษาและส่งเสริมสุขภาพ"
  },
  "learn": [
    "ความรู้ทางวิทยาศาสตร์สุขภาพ",
    "การบริหาร / การจัดฝึกอบรม",
    "จิตวิทยาและพฤติกรรมศาสตร์",
    "นิเทศศาสตร์"
  ],
  "do": [
    "วิเคราะห์และวางแผนการจัดโครงการและการฝึกอบรม โดยใช้หลักจิตวิทยามาประกอบ",
    "จัดทำสื่อต่าง ๆ เพื่อการสื่อสารที่ง่ายขึ้น"
  ],
  "jobs": [
    "เตรียม Script และ Story Board สำหรับการถ่ายทำ",
    "จัดสถานที่สำหรับถ่ายทำ ดูแลเรื่องแสง เสียง และอุปกรณ์อื่น ๆ ที่จำเป็นในการถ่ายทำงานนั้น ๆ",
    "ถ่ายทำวิดีโอทั้งงานตั้งกล้องและงานเดินถ่าย เช่น งาน Event หรือคอนเทนต์ที่ต้องมีการแนะนำสินค้า",
    "ถ่ายภาพนิ่งทั้งงาน Event ภาพนิ่งสำหรับทำ Thumbnail และภาพเพื่อใช้ทำโปรโมทต่าง ๆ",
    "งาน Motion Graphic สำหรับใช้ในวิดีโอต่าง ๆ หรือสำหรับใช้เพื่อยิง Ad ใน Social Media",
    "งานวิดีโอและ Motion Graphic เพื่อใช้กับองค์กรใหญ่ ๆ เช่น SCBX, Kbank, True Business, NITMX"
  ],
  "university": [
    {
      "title": "ชมรมอีสาน มหาวิทยาลัยมหิดล (ประธานชมรม)",
      "items": [
        "กิจกรรมแรกพบชมรมอีสาน มหาวิทยาลัยมหิดล",
        "ค่ายจิตอาสาชมรมอีสาน — โรงเรียนบ้านหนองโดน อ.ปักธงชัย จ.นครราชสีมา",
        "ค่ายจิตอาสาชมรมอีสาน — โรงเรียนบ้านโนนสะอาด อ.กุดรัง จ.มหาสารคาม"
      ],
      "images": [
        "img/s03-1.webp",
        "img/s03-3.webp",
        "img/s03-5.webp",
        "img/s03-6.webp",
        "img/s03-7.webp",
        "img/s03-8.webp",
        "img/s03-9.webp",
        "img/s03-10.webp",
        "img/s03-11.webp",
        "img/s03-12.webp",
        "img/s03-13.webp",
        "img/s03-14.webp"
      ]
    },
    {
      "title": "การจัดกิจกรรมและการฝึกอบรม",
      "items": [
        "จัดอบรมการพูดในที่สาธารณะ (Public Speaking)",
        "ผู้นำทีมจัดกิจกรรมส่งเสริมสุขภาพ ชุมชนวัดมะกอกกลางสวน กทม."
      ],
      "images": [
        "img/s04-1.webp",
        "img/s04-2.webp",
        "img/s04-3.webp",
        "img/s04-4.webp",
        "img/s04-5.webp",
        "img/s04-6.webp",
        "img/s04-7.webp",
        "img/s04-8.webp",
        "img/s04-9.webp",
        "img/s04-10.webp"
      ]
    }
  ]
};

const GROUPS = [
  {
    "org": "MEZ Motowork Co., Ltd.",
    "role": "Video Editor",
    "period": "May 2021 – Feb 2022",
    "works": [
      {
        "title": "MEZ Motowork",
        "desc": "งานตัดต่อวิดีโอโปรโมทยางมอเตอร์ไซค์ METZELER",
        "videos": [
          {
            "type": "drive",
            "id": "1XyHTWdCNKqUkcw7UMFx04cXdnXDvjWET",
            "label": "METZELER Z8 — Road Sport with StreetUppercut",
            "ar": 1.7778,
            "poster": "img/poster/s05-v1.webp"
          }
        ],
        "images": [
          "img/s05-1.webp"
        ]
      }
    ]
  },
  {
    "org": "Techsauce Media Co., Ltd.",
    "role": "Video Editor",
    "period": "Feb 2022 – Jul 2023",
    "works": [
      {
        "title": "Techsauce Media",
        "desc": "",
        "videos": [
          {
            "type": "drive",
            "id": "16Dhz8zPyvDj4V_OwdyVTV3zOILrKir_G",
            "label": "Major App — Mobile First",
            "ar": 1.7778,
            "poster": "img/poster/s06-v1.webp"
          }
        ],
        "images": []
      },
      {
        "title": "Techsauce Global Summit 2022",
        "desc": "งานรวม Startup สาย Technology และเชิญ Speaker ที่เป็นระดับผู้บริหารจากทั่วโลกมาพูดในงาน วันที่ 26–27 สิงหาคม 2565 ที่ไอคอนสยาม",
        "videos": [
          {
            "type": "drive",
            "id": "1gMf9UEeOc9txMhJ5f4HgD05kqpua6-US",
            "label": "วิดีโอ Highlight งาน",
            "ar": 1.7778
          }
        ],
        "images": [
          "img/s07-1.webp",
          "img/s07-2.webp",
          "img/s07-3.webp",
          "img/s07-4.webp",
          "img/s07-5.webp",
          "img/s07-6.webp"
        ]
      },
      {
        "title": "NFT : Platfinder Club",
        "desc": "วิดีโอ Motion สำหรับการเปิดตัว NFT ของ Techsauce ในงาน Techsauce Global Summit 2022",
        "videos": [
          {
            "type": "drive",
            "id": "1R4hEIWEin6RlXOB_ZxFB2_QVkz_tN5Zw",
            "label": "วิดีโอ Motion เปิดตัว NFT",
            "ar": 1.7778
          }
        ],
        "images": []
      },
      {
        "title": "Thailand Accelerator",
        "desc": "งานที่จะช่วยเหลือบริษัท Startup รุ่นใหม่ ๆ ให้มีการเติบโตมากขึ้นในวงการธุรกิจไทย",
        "videos": [
          {
            "type": "drive",
            "id": "1IcLll2Ri7Jy6keFhOtQCEToaleJVkzPF",
            "label": "วิดีโองาน Press Conference",
            "ar": 1.7778,
            "poster": "img/poster/s09-v1.webp"
          }
        ],
        "images": [
          "img/s09-1.webp",
          "img/s09-2.webp",
          "img/s09-3.webp",
          "img/s09-4.webp",
          "img/s09-5.webp"
        ]
      },
      {
        "title": "MIT Media Lab Forum",
        "desc": "งานที่รวมนวัตกรรมจากสถาบันเทคโนโลยีแมสซาชูเซตส์ ประเทศสหรัฐอเมริกา ซึ่งเป็นงานที่นำมาจัดที่ South East Asia เป็นครั้งแรก และนำมาจัดที่กรุงเทพมหานคร ประเทศไทย",
        "videos": [
          {
            "type": "drive",
            "id": "12LgjpmZ-Dnvu_p7XPvkiBm9RaeO78rsY",
            "label": "วิดีโองาน Press Conference",
            "ar": 1.7778,
            "poster": "img/poster/s10-v1.webp"
          }
        ],
        "images": [
          "img/s10-1.webp",
          "img/s10-2.webp",
          "img/s10-3.webp",
          "img/s10-4.webp"
        ]
      },
      {
        "title": "TS Short",
        "desc": "คลิปสั้นแนวตั้งสำหรับช่องทางโซเชียลของ Techsauce",
        "videos": [
          {
            "type": "drive",
            "id": "1vS5cuD-y91DPeqaYGv9we8lbPs7ntWMs",
            "label": "Saucy Thoughts — Gen Z จะเป็นเจ้าของกิจการที่เจ๋งกว่ารุ่นพ่อรุ่นแม่",
            "ar": 0.5625,
            "poster": "img/poster/s12-v1.webp"
          },
          {
            "type": "drive",
            "id": "1WEyxWjTHQBIy4sYXPwfMfIBVM7lte_0p",
            "label": "Sustainable — Climate Crisis causes cancer risk",
            "ar": 0.5625,
            "poster": "img/poster/s12-v2.webp"
          }
        ],
        "images": []
      }
    ]
  },
  {
    "org": "ประสบการณ์ทำงานอื่น ๆ",
    "role": "",
    "period": "",
    "works": [
      {
        "title": "SCBX Project",
        "desc": "",
        "bullets": [
          "SCBX : Next Tech — ทำวิดีโอเปิดงานเปิดตัวโซนพื้นที่ SCBX ที่สยามพารากอน ชั้น 4",
          "SCBX : AI Journey — ทำ Motion Graphic สำหรับงาน AI Journey ภายในองค์กร SCBX ที่จะช่วยให้พนักงานเข้าใจลำดับและขั้นตอนการพัฒนาบุคลากรทางด้าน AI ในองค์กร"
        ],
        "videos": [
          {
            "type": "drive",
            "id": "1NsZyXufgWog5jKlnXMf8VroFQ89Le4fx",
            "label": "SCBX : Next Tech — Press Conference",
            "ar": 1.6667,
            "poster": "img/poster/s17-v1.webp"
          },
          {
            "type": "drive",
            "id": "1rGn3DU3XbQKjrRbJmcyh8wTakXh4kHHZ",
            "label": "SCBX : AI Journey",
            "ar": 1.7778
          }
        ],
        "images": []
      },
      {
        "title": "True Business",
        "desc": "ทำ Motion Graphic สำหรับยิง Ad Promotion ของ True Business",
        "videos": [
          {
            "type": "drive",
            "id": "1d4-EaXLi4v4Sv0_IPzvxA860sxvpSbZ9",
            "label": "True CPaaS",
            "ar": 1.0
          },
          {
            "type": "drive",
            "id": "15pb8BV259_pR7MBM4ejTq_N6gck9rnLc",
            "label": "One Call",
            "ar": 1.0,
            "poster": "img/poster/s18-v2.webp"
          },
          {
            "type": "drive",
            "id": "1_368qU5MGIrcbsGRkKtdZiaEn5d8jpaQ",
            "label": "SMS Marketing",
            "ar": 1.7778,
            "poster": "img/poster/s18-v3.webp"
          },
          {
            "type": "drive",
            "id": "1T4L5q8dqNJXY91Gs0CowCEK3kU-8SC7Q",
            "label": "M2M",
            "ar": 1.7778
          }
        ],
        "images": []
      },
      {
        "title": "Thairath Money",
        "desc": "คลิปสั้นแนวตั้งให้กับ Thairath Money",
        "videos": [
          {
            "type": "drive",
            "id": "12D3MlUHolKV7bux2KtksDTDvYqOb-qFr",
            "label": "EP.03 L'Oréal",
            "ar": 0.5625,
            "poster": "img/poster/s19-v1.webp"
          },
          {
            "type": "drive",
            "id": "1Zun6pZVif-9PD5iBOdSsj3lLig32seDY",
            "label": "EP.05 AP",
            "ar": 0.5625,
            "poster": "img/poster/s19-v2.webp"
          },
          {
            "type": "drive",
            "id": "1Mbt9A7IGL1QkZZmw6faO_XrIJAwUEmHK",
            "label": "EP.08 TQM",
            "ar": 0.5625,
            "poster": "img/poster/s19-v3.webp"
          },
          {
            "type": "drive",
            "id": "13lOtln8QpTo8iUO_BEnQhlXBNsmd124o",
            "label": "EP.11 SCB",
            "ar": 0.5625,
            "poster": "img/poster/s19-v4.webp"
          }
        ],
        "images": []
      },
      {
        "title": "Money Monster",
        "desc": "ช่อง YouTube ที่มีผู้ติดตามกว่า 100,000 คน ของคุณทราย โศธิดา โชติวิจิตร เป็นเนื้อหาเกี่ยวกับการเงินและการลงทุน โดยมีลูกค้าเป็นผู้ให้บริการด้านการลงทุนชื่อดัง เช่น Binance, K Asset, The Wisdom, Dime, XM, Webull",
        "videos": [
          {
            "type": "drive",
            "id": "1YXvPgJ8r3r8BkV8xDFLBvuvYFYaVvxSD",
            "label": "Binance",
            "ar": 1.7778,
            "poster": "img/poster/s20-v1.webp"
          },
          {
            "type": "drive",
            "id": "11HuX9YY4JJ_gIhlO-EAG0ik-IZGII30b",
            "label": "K Asset",
            "ar": 1.7778,
            "poster": "img/poster/s20-v2.webp"
          },
          {
            "type": "drive",
            "id": "1K-ng0u5Qg1vW-tgBNGmVcU1X8RdGUlVC",
            "label": "Dime — เทศกาลลดหย่อนภาษี",
            "ar": 1.7778,
            "poster": "img/poster/s20-v3.webp"
          }
        ],
        "images": []
      },
      {
        "title": "NITMX",
        "desc": "ผู้คิดค้นระบบ PromptPay ของประเทศไทย ที่ล่าสุดจัดงาน NITMX : Hack to the Max ที่เปิดโอกาสให้คนสมัครเข้ามาแข่ง Hackathon เพื่อหาผู้ชนะไปดูงานที่ Singapore FinTech Festival 2024 ที่ประเทศสิงคโปร์",
        "videos": [
          {
            "type": "drive",
            "id": "1r0QaJsvL5zmLZzgWDTToCdkBN0KvdE16",
            "label": "NITMX : Hack to the Max",
            "ar": 1.7778
          }
        ],
        "images": []
      }
    ]
  }
];

