import requests
from bs4 import BeautifulSoup

TELEGRAM_TOKEN = "8887338793:AAGUji5p17xcJ6N88y7DYRlknGS7YBkQCW8"
CHAT_ID = 7844335135

def get_news():
    url = "https://news.google.com/rss/headlines/section/topic/WORLD.en_pk/Pakistan?ned=pk&hl=ur&gl=PK"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item', limit=5)
    
    report = "🔔 *تازہ ترین خبریں:* 🇵🇰\n\n"
    for item in items:
        title = item.title.text
        report += f"📢 {title}\n\n"
    return report

def check_messages():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    if response['result']:
        last_msg = response['result'][-1]['message']
        text = last_msg.get('text', '').lower()
        
        if "today news" in text:
            news = get_news()
            requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                          data={"chat_id": CHAT_ID, "text": news, "parse_mode": "Markdown"})

if __name__ == "__main__":
    check_messages()
    
