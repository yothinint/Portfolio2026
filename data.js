/* ============================================================================
   ข้อมูลทั้งหมดของเว็บ — สร้างอัตโนมัติด้วย gen_data.py
   แก้ด้วยมือได้ แต่ถ้ารัน gen_data.py ใหม่ ไฟล์นี้จะถูกเขียนทับ

   วิดีโอ : { type:"youtube"|"drive", id:"...", label:"...", ar:1.7778, poster:"..." }
            ar 1.7778 = 16:9 · 0.5625 = 9:16 · 1 = 1:1
            YouTube ไม่ต้องใส่ poster (ดึงจาก i.ytimg.com ให้เอง)
============================================================================ */

const SITE = {
  "name": "โยธิน อินทรภิรมย์",
  "nameEn": "Yothin Intaraphirom",
  "nickname": "โย",
  "role": "Senior Video Editor & Motion Designer",
  "photo": "photo/profile.webp",
  "avatar": "photo/avatar.webp",
  "contacts": [
    {
      "type": "โทรศัพท์",
      "value": "080-379-1992",
      "url": "tel:+66803791992",
      "icon": "phone"
    },
    {
      "type": "อีเมล",
      "value": "yothin42@gmail.com",
      "url": "mailto:yothin42@gmail.com",
      "icon": "mail"
    },
    {
      "type": "LINE",
      "value": "iryothin",
      "url": "https://line.me/ti/p/~iryothin",
      "icon": "line"
    }
  ]
};

const PROFILE = {
  "education": {
    "degree": "วท.บ. สาธารณสุขศาสตร์",
    "major": "สาขาสุขศึกษาและส่งเสริมสุขภาพ",
    "university": "มหาวิทยาลัยมหิดล",
    "logo": "photo/mahidol.webp"
  },
  "jobs": [
    "เตรียม Script และ Story Board สำหรับการถ่ายทำ",
    "จัดสถานที่สำหรับถ่ายทำ ดูแลเรื่องแสง เสียง และอุปกรณ์อื่น ๆ ที่จำเป็นในการถ่ายทำงานนั้น ๆ",
    "ถ่ายทำวิดีโอทั้งงานตั้งกล้องและงานเดินถ่าย เช่น งาน Event หรือคอนเทนต์ที่ต้องมีการแนะนำสินค้า",
    "ถ่ายภาพนิ่งทั้งงาน Event ภาพนิ่งสำหรับทำ Thumbnail และภาพเพื่อใช้ทำโปรโมทต่าง ๆ",
    "งาน Motion Graphic สำหรับใช้ในวิดีโอต่าง ๆ หรือสำหรับใช้เพื่อยิง Ad ใน Social Media",
    "งานวิดีโอและ Motion Graphic เพื่อใช้กับองค์กรใหญ่ ๆ เช่น SCBX, Kbank, True Business, NITMX"
  ],
  "career": [
    {
      "org": "MEZ Motowork Co., Ltd."
    },
    {
      "org": "Techsauce Media Co., Ltd."
    },
    {
      "org": "Sino-Thai Communications Group Co., Ltd."
    },
    {
      "org": "LEARN Corporation Public Company Limited"
    },
    {
      "org": "Thairath Money",
      "role": "Senior Video Editor",
      "current": true
    }
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
    "org": "Video",
    "role": "",
    "period": "",
    "works": [
      {
        "title": "MEZ Motowork",
        "desc": "",
        "videos": [
          {
            "type": "drive",
            "id": "1XyHTWdCNKqUkcw7UMFx04cXdnXDvjWET",
            "label": "METZELER Z8 — Road Sport with StreetUppercut",
            "poster": "img/poster/s05-v1.webp",
            "ar": 1.7778
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
        "title": "MIT Media Lab Forum",
        "desc": "งานที่รวมนวัตกรรมจากสถาบันเทคโนโลยีแมสซาชูเซตส์ ประเทศสหรัฐอเมริกา ซึ่งเป็นงานที่นำมาจัดที่ South East Asia เป็นครั้งแรก และนำมาจัดที่กรุงเทพมหานคร ประเทศไทย",
        "videos": [
          {
            "type": "drive",
            "id": "12LgjpmZ-Dnvu_p7XPvkiBm9RaeO78rsY",
            "label": "วิดีโองาน Press Conference",
            "poster": "img/poster/s10-v1.webp",
            "ar": 1.7778
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
            "poster": "img/poster/s12-v1.webp",
            "ar": 0.5625
          },
          {
            "type": "drive",
            "id": "1WEyxWjTHQBIy4sYXPwfMfIBVM7lte_0p",
            "label": "Sustainable — Climate Crisis causes cancer risk",
            "poster": "img/poster/s12-v2.webp",
            "ar": 0.5625
          }
        ],
        "images": []
      },
      {
        "title": "Thairath Money",
        "desc": "",
        "videos": [
          {
            "type": "youtube",
            "id": "d1DjfLoO_Kc",
            "label": "Google Maps ได้อะไร ? ทำไมให้คนใช้ฟรี ทั้งที่ต้นทุนมหาศาล | Digital Frontiers EP.34",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "6zDMH_Uu5fA",
            "label": "GoPro หายไปไหน? แบรนด์กล้องสุดล้ำ จากสูงสุดสู่สามัญในพริบตาเดียว | Digital Frontiers EP.35",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "ZHoG3f9e-ew",
            "label": "ถอดโมเดล SpaceX ธุรกิจที่คนเข้าใจผิดว่า “ขายจรวด” | Digital Frontiers EP.53",
            "ar": 1.7778
          }
        ],
        "images": []
      },
      {
        "title": "Money Monster",
        "desc": "ช่อง YouTube ของคุณทราย โศธิดา โชติวิจิตร เนื้อหาเกี่ยวกับการเงินและการลงทุน มีผู้ติดตามรวมกันทุกช่องทางมากกว่า 1,000,000 คน",
        "videos": [
          {
            "type": "youtube",
            "id": "_fTA-Rr1D5k",
            "label": "Anthropic จากอาวุธลับ Pentagon สู่ศัตรูรัฐบาลสหรัฐ! | Money Monster EP.312",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "GodRVk34iaI",
            "label": "จีนแฉ! Luxury Brand 80% ผลิตในจีน ไม่ใช่ยุโรป | Money Monster EP.170",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "qD7FZqrToiE",
            "label": "ประเทศไทย ไม่จน เงินเข้าเยอะ แต่ไม่ถึงมือเรา? | Money Monster EP.301",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "-yp1oFeyhJE",
            "label": "BlackRock โคตรรวย โคตรมีอำนาจ! | Money Monster EP.376",
            "ar": 1.7778
          }
        ],
        "images": []
      },
      {
        "title": "Skooldio",
        "desc": "",
        "videos": [
          {
            "type": "youtube",
            "id": "irQocObdz98",
            "label": "AI, อัลกอริทึม, และอนาคตของการสร้างสรรค์ กับพี่มะเดี่ยว | Living With AI EP.7",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "z0LorZu7veo",
            "label": "AI x Mental Health ยุค AI โหดร้าย ฮีลใจยังไงได้บ้าง Feat.คุณดุจดาว วัฒนปกรณ์ | Living With AI EP.5",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "blEJm-bolk8",
            "label": "AI x ดูดวง ใครกันที่ลิขิตชะตาอนาคต กับ ดร. พีพี MIT Media Lab และ คุณแรปเตอร์ | Living with AI EP.4",
            "ar": 1.7778
          },
          {
            "type": "youtube",
            "id": "Pqgoq2yAIeA",
            "label": "AI x Relationship ไขปริศนารักยุคปัญญาประดิษฐ์กับ รศ.ดร.ชลิดาภรณ์ | Living With AI EP.3",
            "ar": 1.7778
          }
        ],
        "images": []
      },
      {
        "title": "Happy Me Clinic",
        "desc": "",
        "videos": [
          {
            "type": "youtube",
            "id": "9pyKETF96es",
            "label": "รักตัวเองก่อนจะรักคนใคร 🥰🤗",
            "ar": 0.5625
          },
          {
            "type": "youtube",
            "id": "fZzX_77KDwY",
            "label": "รู้สึกเบื่อแฟนควรทำอย่างไร?",
            "ar": 0.5625
          }
        ],
        "images": []
      },
      {
        "title": "TTB Fintalk",
        "desc": "",
        "sections": [
          {
            "label": "Long form",
            "videos": [
              {
                "type": "youtube",
                "id": "eW3NcQFDzq4",
                "label": "Fintalk with GURUs : จัดพอร์ตเกษียณ เปลี่ยนชีวิตคุณ กับ คุณเฟิร์น ศิรัถยา อิศรภักดี Wealth Me Up",
                "ar": 1.7778
              },
              {
                "type": "youtube",
                "id": "lnM0Qv8Z-b8",
                "label": "Fintalk with GURUs : รักต้องคุย เงินต้องเคลียร์ กับ ดีเจพี่อ้อย Club Friday",
                "ar": 1.7778
              }
            ]
          },
          {
            "label": "Short form",
            "videos": [
              {
                "type": "youtube",
                "id": "Nz4iLUzN1Ig",
                "label": "Fintalk EP5 | Temporal Discounting คืออะไร?",
                "ar": 0.5625
              },
              {
                "type": "youtube",
                "id": "8C7e8DsXQ7M",
                "label": "4 นิสัยการเงิน เข้าใจให้รักรอด💙 | Fintalk",
                "ar": 0.5625
              }
            ]
          }
        ],
        "videos": [],
        "images": []
      },
      {
        "title": "Money Studio",
        "desc": "",
        "videos": [
          {
            "type": "youtube",
            "id": "7YEm4pmMpZ4",
            "label": "EP13 | หุ้นกู้ หุ้น หรือกองทุนรวม…เลือกยังไงให้เหมาะกับเรา?",
            "ar": 0.5625
          },
          {
            "type": "youtube",
            "id": "WgrndtRpCWs",
            "label": "EP21 | รายได้สูง ≠ รวย",
            "ar": 0.5625
          },
          {
            "type": "youtube",
            "id": "HXdBPLFr8-w",
            "label": "Hydro Flask | ใช้ของแพงให้คุ้ม ด้วย The $1 Rule",
            "ar": 0.5625
          }
        ],
        "images": []
      },
      {
        "title": "SCBX Project",
        "desc": "",
        "bullets": [
          "SCBX : Next Tech — ทำวิดีโอเปิดงานเปิดตัวโซนพื้นที่ SCBX ที่สยามพารากอน ชั้น 4"
        ],
        "videos": [
          {
            "type": "drive",
            "id": "1NsZyXufgWog5jKlnXMf8VroFQ89Le4fx",
            "label": "SCBX : Next Tech — Press Conference",
            "poster": "img/poster/s17-v1.webp",
            "ar": 1.6667
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
  },
  {
    "org": "Motion Graphic Video",
    "role": "",
    "period": "",
    "works": [
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
            "poster": "img/poster/s09-v1.webp",
            "ar": 1.7778
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
        "title": "SCBX Project",
        "desc": "",
        "bullets": [
          "SCBX : AI Journey — ทำ Motion Graphic สำหรับงาน AI Journey ภายในองค์กร SCBX ที่จะช่วยให้พนักงานเข้าใจลำดับและขั้นตอนการพัฒนาบุคลากรทางด้าน AI ในองค์กร"
        ],
        "videos": [
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
            "poster": "img/poster/s18-v2.webp",
            "ar": 1.0
          },
          {
            "type": "drive",
            "id": "1_368qU5MGIrcbsGRkKtdZiaEn5d8jpaQ",
            "label": "SMS Marketing",
            "poster": "img/poster/s18-v3.webp",
            "ar": 1.7778
          },
          {
            "type": "drive",
            "id": "1T4L5q8dqNJXY91Gs0CowCEK3kU-8SC7Q",
            "label": "M2M",
            "ar": 1.7778
          }
        ],
        "images": []
      }
    ]
  }
];

