from getNews import getNews
from validateNews import validateNews
from notify import notify
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


if __name__ == "__main__":
    # Check if the discord webhook is provided
    if os.environ.get("DISCORD_WEBHOOK") == "":
        print("Please provide a discord webhook url to the .env file")
        exit()

    # Get all available news from the given Singidunum site
    news = getNews(os.environ.get("SINGIDUNUM_SITE_URL"))
    # Filter out old news
    validatedNews = validateNews(news, os.environ.get("LAST_FILE_PATH"))
    if (validatedNews):
        # Send notifications about the new news if any
        notify(validatedNews, os.environ.get("DISCORD_WEBHOOK"))
