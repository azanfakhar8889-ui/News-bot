import requests
import xml.etree.ElementTree as ET
from datetime import datetime

TELEGRAM_TOKEN = "8887338793:AAGUji5p17xcJ6N88y7DYRlknGS7YBkQCW8"
CHAT_ID = 7844335135

def send_news():
    url = "https://news.google.com/rss/search?q=Pakistan&hl=ur&gl=PK&ceid=PK:ur"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    
    report = "🔔 *پاکستان کی تازہ ترین خبریں* 🇵🇰\n\n"
    count = 1
    for item in root.findall('.//item'):
        title = item.find('title').text.strip()
        if " - " in title: title = title.split(" - ")[0]
        if len(title) > 20:
            report += f"📢 {title}\n\n"
            count += 1
        if count > 5: break
            
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                  data={"chat_id": CHAT_ID, "text": report, "parse_mode": "Markdown"})

if __name__ == "__main__":
    send_news()
  
