from datetime import datetime


def validate_news(newsList, file):
    try:
        with open(file, "r") as f:
            # Load datetime of last known news from the file
            last = datetime.strptime(f.read(), "%Y-%m-%d %H:%M:%S")
    except:
        # If an error occurred or no datetime/last file is found, set the new last to the current datetime
        last = datetime.now()

    validatedNews = []
    # Go true all news from behind of an array (oldest to newest)
    for news in newsList[::-1]:
        # Turn datetime string in the datetime object
        date = datetime.strptime(news["datetime"], "%Y-%m-%d %H:%M:%S")
        if date > last:
            validatedNews.append(news)
            last = date

    # Save new last datetime to the last file
    with open(file, "w") as f:
        f.write(last.strftime("%Y-%m-%d %H:%M:%S"))

    return validatedNews
