from get_news import get_news
from validate_news import validate_news
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
    all_news = get_news(os.environ.get("SINGIDUNUM_SITE_URL"))
    
    # Filter out old news
    new_news = validate_news(all_news, os.environ.get("LAST_FILE_PATH"))

    for news in new_news:
        # Send notifications about the new news if any
        notify(news, os.environ.get("DISCORD_WEBHOOK"))
