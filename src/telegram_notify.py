import requests
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

# --- Завантажуємо .env ---
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # вихід із /src
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("ADMIN_CHAT_ID")

# --- Логи ---
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "telegram_notify.log")
FULL_LOG_FILE = os.path.join(LOG_DIR, "full_log.log")

def log(message):
    timestamp = datetime.now(ZoneInfo("Europe/Kyiv")).strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} [telegram_notify] {message}"
    print(line)
    #with open(LOG_FILE, "a", encoding="utf-8") as f:
    #    f.write(line + "\n")
    with open(FULL_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# --- Відправка фото з підписом ---
def send_photo(image_path, caption=None):
    if not TOKEN or not CHAT_ID:
        log("❌ BOT_TOKEN або ADMIN_CHAT_ID не встановлені!")
        return

    if not os.path.exists(image_path):
        log(f"⚠️ Фото не знайдено: {image_path}")
        return

    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
        with open(image_path, "rb") as img:
            requests.post(
                url,
                data={"chat_id": CHAT_ID, "caption": caption or "", "parse_mode": "HTML"},
                files={"photo": img}
            )
        caption = caption.replace("\n", " ")
        log(f"✅ Відправлено фото: {image_path} з підписом: {caption or ''}")

    except Exception as e:
        log(f"❌ Помилка при відправленні фото: {e}")

def send_error(text):
    if not TOKEN or not CHAT_ID:
        log("❌ BOT_TOKEN або ADMIN_CHAT_ID не встановлені!")
        return

    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": f"<b>TOE_PARSER</b>\n{text}",
            "parse_mode": "HTML"
        }
        requests.post(url, data=data)
        log(f"⚠️ Відправлено помилку: {text}")

    except Exception as e:
        log(f"❌ Помилка при відправленні error: {e}")

#def send_message(text):
#    if not TOKEN or not CHAT_ID:
#        log("❌ BOT_TOKEN або ADMIN_CHAT_ID не встановлені!")
#        return
#
#    try:
#        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#        data = {
#            "chat_id": CHAT_ID,
#            "text": f"<b>TOE_PARSER</b>\n{text}",
#            "parse_mode": "HTML"
#        }
#        requests.post(url, data=data)
#        log(f"Відправлено повідомлення: {text}")
#
#    except Exception as e:
#        log(f"❌ Помилка при відправленні error: {e}")
def send_message(text, silent=False):
    if not TOKEN or not CHAT_ID:
        log("❌ BOT_TOKEN або ADMIN_CHAT_ID не встановлені!")
        return

    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": f"<b>TOE_PARSER</b>\n{text}",
            "parse_mode": "HTML",
            "disable_notification": silent  # Додано параметр для беззвучного режиму
        }
        requests.post(url, data=data)
        log(f"Відправлено {'безувучне ' if silent else ''}повідомлення: {text}")

    except Exception as e:
        log(f"❌ Помилка при відправленні повідомлення: {e}")
