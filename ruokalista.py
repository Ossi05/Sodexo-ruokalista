import feedparser
import datetime
from bs4 import BeautifulSoup

#rss feed linkki
url = "https://www.sodexo.fi/ruokalistat/rss/weekly_rss/115/fi"
feed = feedparser.parse(url)

today = datetime.datetime.today().weekday()
days = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai"]
print(feed.feed.description + ":")

for entry in feed.entries:
    summary = entry.summary_detail.value
    soup = BeautifulSoup(summary, 'html.parser')
    strong_tag = soup.find('strong')
    day_tag = soup.find('h2')
    #Tänään
    if strong_tag and day_tag and day_tag.text == days[today]:
        print(f"{days[today]}:")
        print(f"          {strong_tag.text}")
        print("Muut päivät:")
    #Muut päivät    
    else:
        if strong_tag:
            print(f"          {strong_tag.text}")
