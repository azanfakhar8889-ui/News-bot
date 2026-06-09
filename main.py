import requests
from bs4 import BeautifulSoup

TELEGRAM_TOKEN = "8887338793:AAGUji5p17xcJ6N88y7DYRlknGS7YBkQCW8"
CHAT_ID = 7844335135

def send_news():
    # اردو گوگل نیوز کا لنک
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pWVXlnQVAB?hl=ur&gl=PK&ceid=PK%3Aur"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # خبروں کو ڈھونڈنا
    articles = soup.find_all('h3', limit=5)
    
    report = "🔔 *پاکستان کی تازہ ترین خبریں* 🇵🇰\n\n"
    for article in articles:
        title = article.text.strip()
        report += f"📢 {title}\n\n"
            
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", 
                  data={"chat_id": CHAT_ID, "text": report, "parse_mode": "Markdown"})

if __name__ == "__main__":
    send_news()
    
