# ⚡ OE_OUTAGE_DATA  графіки відключень світла в Україні

<div align="center">

### 🇺🇦 Слава Україні! Героям Слава! 🇺🇦

[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://stand-with-ukraine.pp.ua)

</div>

---

### Актуальні дані про відключення:  
- **Черкасиобленерго**
- **Чернігівобленерго**
- **Хмельницькобленерго**
- **Харківобленерго**
- **Львівобленерго**
- **Прикарпаттяобленерго**
- **Полтаваобленерго**
- **Рівнеобленерго**
- **Тернопільобоенерго**
- **Закарпаттяобленерго**
- **Запоріжжяобленерго**
- **Житомиробленерго**

Цей репозиторій містить **актуальні дані про відключення електроенергії**, представлені у форматі **JSON**, а також автоматично згенеровані **PNG-зображення** графіків:

- окремі графіки для кожної групи
- загальний добовий графік для всіх груп

---

## 💬 Telegram-обговорення

Ми створили окрему Telegram-групу для технічних обговорень: парсингу, генерації графіків, Home Assistant інтеграцій, Telegram-ботів, API та покращень системи.

👉 **Приєднуйтесь до спільноти:**  
[![Telegram](https://img.shields.io/badge/Telegram-Приєднатися-blue?style=for-the-badge&logo=telegram)](https://t.me/OE_OUTAGE_CHAT)

---

## 💖 Підтримка 
   
Якщо проєкт корисний для вас, не забудьте поставити ⭐️ та **підтримати донатом**

💳 **Monobank:** [Підтримати проєкт](https://send.monobank.ua/jar/fMWjosNzo) ⚡️

Цей проєкт я розробляю та підтримую у вільний час — безкоштовно для всіх українців.

🔧 Зараз все працює на безкоштовних сервісах, але це має обмеження по швидкості та стабільності.

💡 Ваша підтримка допоможе:
- Перенести проєкт на якісний платний хостинг
- Додати нові регіони та функції
- Підтримувати сервери без перебоїв

Будь-яка сума — це мотивація продовжувати розвивати корисні інструменти для людей! 🙏

Дякую! 🇺🇦⚡️

--- 

## 🤖 Telegram-інтеграції

Дані з **OE_OUTAGE_DATA** також використовуються в Telegram-ботах для оперативних сповіщень про графіки відключень електроенергії.

#### ⚡ DTEK Schedule Power Out Sender Bot  
🤖 Бот: [@DtekSchedulePowerOutSenderBot](https://t.me/DtekSchedulePowerOutSenderBot)  
👤 Розробник: [@2ruslan](https://github.com/2ruslan)

---

## 🏠 Інтеграції з Home Assistant

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Integration-41BDF5?style=for-the-badge&logo=home-assistant)](https://www.home-assistant.io/)

### ⚡ Доступні інтеграції

#### 🔌 ha-svitlo-yeah  
👤 Розробник: [ALERTua](https://github.com/ALERTua)  
🔗 https://github.com/ALERTua/ha-svitlo-yeah

#### 🔌 Svitlo Live  
👤 Розробник: [chaichuk](https://github.com/chaichuk)  
🔗 https://github.com/chaichuk/svitlo_live

---

## 🔄 Як працює система

Парсери автоматично зчитують дані з офіційних сайтів кожні **5 хвилин**.

- Якщо знайдено зміни — JSON оновлюється  
- Генерується нове PNG-зображення  
- Дані автоматично публікуються у GitHub  

---

## 🧩 Формат JSON
```jsonc
{
  "regionId": "Zhytomyr",
  "lastUpdated": "2025-12-08T06:54:55.423Z", //<-- Дата та час останнього парсингу (UTC, ISO8601)
  "fact": {
    "data": {
      "1765144800": { //<-- Ключ — Unix timestamp (Europe/Kyiv), дата графіку відключень
        "GPV1.1": {},
        "GPV6.2": {}
      }
    },
    "update": "08.12.2025 08:30", //<-- Час оновлення у локальній зоні (Europe/Kyiv)
    "today": 1765144800 //<-- Timestamp поточного дня (Europe/Kyiv)
  }
}
```
---

## 📁 Структура репозиторію
```
OE_OUTAGE_DATA/
├── data/
├── images/
├── README.md
└── ...
```
---

## 🤝 Community & Credits

Дякуємо розробникам Home Assistant інтеграцій, які використовують дані OE_OUTAGE_DATA:
- [chaichuk](https://github.com/chaichuk) — Svitlo Live
- [ALERTua](https://github.com/ALERTua)   — ha-svitlo-yeah

---

## 🙌 Дякуємо за використання OE_OUTAGE_DATA!