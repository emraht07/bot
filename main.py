import os
import requests
from telegram import Bot

BOT_TOKEN = os.environ.get("8251923975:AAGtM7-fQT3Vakdbqj4SC3CiEWdIFbECCzc")
CHAT_ID = os.environ.get("1445775903")

bot = Bot(token=BOT_TOKEN)
seen_titles = set()

def send_test_message():
    bot.send_message(chat_id=CHAT_ID, text="✅ Bot başarıyla çalışıyor ve Telegram'a mesaj gönderebiliyor.")

def check_binance():
    url = 'https://www.binance.com/bapi/composite/v1/public/cms/article/list?catalogId=48&pageSize=5&pageNo=1'
    try:
        response = requests.get(url)
        data = response.json()
        articles = data.get('data', {}).get('articles', [])
        for article in articles:
            title = article['title']
            link = f"https://www.binance.com/en/support/announcement/{article['code']}"
            if 'Launchpad' in title or 'Launchpool' in title:
                if title not in seen_titles:
                    seen_titles.add(title)
                    bot.send_message(chat_id=CHAT_ID, text=f"🚀 Yeni Binance Duyurusu:\n{title}\n{link}")
    except Exception as e:
        print("Binance API hatası:", e)

# Test mesajı gönder
send_test_message()

# Binance duyurularını kontrol et
check_binance()

