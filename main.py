def check_binance():
    url = 'https://www.binance.com/bapi/composite/v1/public/cms/article/list?catalogId=48&pageSize=5&pageNo=1'
    response = requests.get(url)

    try:
        data = response.json()
        articles = data.get('data', {}).get('articles', [])
        for article in articles:
            title = article['title']
            link = f"https://www.binance.com/en/support/announcement/{article['code']}"
            if 'Launchpad' in title or 'Launchpool' in title:
                if title not in seen_titles:
                    seen_titles.add(title)
                    bot.send_message(chat_id=CHAT_ID, text=f"🚀 Yeni Binance Launchpad: {title}\n{link}")
    except Exception as e:
        print("Binance API hatası:", e)
