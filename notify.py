from datetime import datetime
import json
import requests


def notify(news, webhook):
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

    # Send a POST request to the webhook URL
    response = requests.post(webhook, data=jsonData, headers=headers)

    # Check the response status
    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print("Failed to send message. Status code:", response.status_code)
        print("Response:", response.text)
