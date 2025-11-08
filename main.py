import requests
import time
from telegram import Bot

BOT_TOKEN = '8251923975:AAGtM7-fQT3Vakdbqj4SC3CiEWdIFbECCzc'
CHAT_ID = '1445775903'
bot = Bot(token=BOT_TOKEN)
seen_titles = set()

def check_binance():
    url = 'https://www.binance.com/bapi/composite/v1/public/cms/article/list?catalogId=48&pageSize=5&pageNo=1'
    response = requests.get(url)
    articles = response.json()['data']['articles']

    for article in articles:
        title = article['title']
        link = f"https://www.binance.com/en/support/announcement/{article['code']}"
        if 'Launchpad' in title or 'Launchpool' in title:
            if title not in seen_titles:
                seen_titles.add(title)
                bot.send_message(chat_id=CHAT_ID, text=f"🚀 Yeni Binance Launchpad: {title}\n{link}")

while True:
    check_binance()
    time.sleep(300)
