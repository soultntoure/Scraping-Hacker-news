from bs4 import BeautifulSoup
import requests


response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
titles = soup.select(selector=".storylink")
count = 1
for title in titles:
    print(f"{count}-{title.text}")
    count +=1


