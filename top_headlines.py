import requests

api_key = "1de9c2ef82864b5ba401d1c4b0fbb504"

main_url = (
    "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey="
    + api_key
)

news = requests.get(main_url).json()
# print(news)

article = news["articles"]
# print(article)

news_article = []
for arti in article:
    news_article.append(arti["title"])
    # print(news_article)

for i in range(10):
    print("\n", i + 1, news_article[i])
