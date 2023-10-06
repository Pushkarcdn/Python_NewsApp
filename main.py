import requests
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

voices = speaker.GetVoices()
for index, voice in enumerate(voices):
    # print(f"Voice {index}: {voice.GetDescription()}")
    pass

# voice_index = 2
# speaker.Voice = voices.Item(voice_index)
speaker.rate = 1.7

print(
    "\n\n\n\t What news are you intrested in ? \n\n\t\t 1. Tech \n\t\t 2. Cricket \n\t\t 3. Food \n\n\t\t Any other topic ? Just write it down. "
)

choice = input("\n\t\t Enter your choice: ")

if choice == "1":
    keyword = "tech"
elif choice == "2":
    keyword = "cricket"
elif choice == "3":
    keyword = "food"
else:
    keyword = choice

api_key = "1de9c2ef82864b5ba401d1c4b0fbb504"
lang = "en"

main_url = (
    "https://newsapi.org/v2/everything?q="
    + keyword
    + "&language="
    + lang
    + "&from=2023-10-06&sortBy=popularity&apiKey="
    + api_key
)

response = requests.get(main_url).json()
# print(news)

articles = response["articles"]
# print(article)

news = []
for article in articles:
    news.append(article["title"])
    # print(news_article)

print("\n\n News are: \n\n")

for i in range(10):
    print("\n", i + 1, news[i])
    speaker.Speak(news[i])
