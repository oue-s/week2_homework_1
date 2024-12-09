import requests
import time


response_id = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
time.sleep(1)

for i in range(30):
    id_article = response_id.json()[i]
    response_article = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{id_article}.json?print=pretty"
    )
    if response_article.json()["url"] == "":
        print("{'title': '" + response_article.json()["title"] + "', 'link': 'None'}")
    else:
        print(
            "{'title': '"
            + response_article.json()["title"]
            + "', 'link': "
            + response_article.json()["url"]
            + "'}"
        )

    time.sleep(1)
