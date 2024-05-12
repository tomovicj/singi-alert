import requests
from bs4 import BeautifulSoup


def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Get all news on the web site
    news_list = soup.findAll("div", class_="news-item")

    # Last news in the array is always the archived news (used to open news archive)
    news_list.pop()

    news_data_list = []
    for news in news_list:
        # Extract all needed data
        title = news.find("a", class_="news-item-title").text
        description = news.find("div", class_="news-item-excerpt").text
        url = news.find("a", class_="news-item-title").get("href")
        img = news.img.get("src")
        datetime = news.find("meta", itemprop="datePublished")["content"]

        news_data_list.append({
            "title": title.strip(),
            "description": description.strip() + "...",
            "img": img,
            "url": url,
            "datetime": datetime
        })

    return news_data_list
