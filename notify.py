from datetime import datetime
import json
import requests
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def notify(news_list):
    def notify_ntfy(news, ntfy_webhook):
        try:
            requests.post(ntfy_webhook,
            data=news["description"].encode('utf-8'),
            headers={
                "Title": news["title"].encode('utf-8'),
                "Attach": news["img"],
                "Click": news["url"]
            })
        except:
            print("Failed to send a ntfy message.\n")
        else:
            print("Ntfy message sent successfully!\n")


    def notify_discord(news, discord_webhook):
        # Create a datatime object
        date = datetime.strptime(news["datetime"], "%Y-%m-%d %H:%M:%S")
        # Notification data
        data = {
            "content": None,
            "embeds": [
                {
                    "title": news["title"],
                    "description": news["description"],
                    "url": news["url"],
                    "color": 16711680,
                    "author": {
                        "name": "Singi Alert",
                        "url": "https://github.com/tomovicj/singi-alert"
                    },
                    "timestamp": date.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
                    "thumbnail": {
                        "url": news["img"]
                    }
                }
            ],
            "username": "Singidunum (Unofficial)",
            "avatar_url": "https://upload.wikimedia.org/wikipedia/sr/b/b9/%D0%A1%D0%B8%D0%BD%D0%B3%D0%B8%D0%B4%D1%83%D0%BD%D1%83%D0%BC_%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D0%B7%D0%B8%D1%82%D0%B5%D1%82.png",
            "attachments": []
        }

        # Turn data to a json
        jsonData = json.dumps(data)

        # Set the headers to specify the content type
        headers = {
            "Content-Type": "application/json"
        }

        try:
            # Send a POST request to the webhook URL
            response = requests.post(discord_webhook, data=jsonData, headers=headers)
            
            # Check the response status code
            if (response.status_code != 204):
                raise Exception(response)
        except:
            print("Failed to send a discord message. Status code:", response.status_code, "\n")
            print("Response:", response.text, "\n")
        else:
            print("Discord message sent successfully!\n")


    ntfy_url = os.environ.get("NTFY_URL")
    discord_webhook = os.environ.get("DISCORD_WEBHOOK")
    for news in news_list:
        if ntfy_url:
            notify_ntfy(news, ntfy_url)

        if discord_webhook:
            notify_discord(news, discord_webhook)
