import requests
from bs4 import BeautifulSoup


def getNews(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Get all news on the web site
    newsList = soup.findAll("div", class_="news-item")

    # Last news in the array is always the archived news (used to open news archive)
    newsList.pop()

    newsDataList = []
    for news in newsList:
        # Extract all needed data
        title = news.find("a", class_="news-item-title").text
        description = news.find("div", class_="news-item-excerpt").text
        url = news.find("a", class_="news-item-title").get("href")
        img = news.img.get("src")
        datetime = news.find("meta", itemprop="datePublished")["content"]

        newsDataList.append({
            "title": title.strip(),
            "description": description.strip() + "...",
            "img": img,
            "url": url,
            "datetime": datetime
        })

    return newsDataList
