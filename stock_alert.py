import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# create your personal apha vinatge api key
STOCK_API_KEY = ""
NEWS_API_KEY = ""

# create your personal twilio vinatge api key
TWILIO_SID = ""
TWILIO_TOKEN = ""

# put your personal phone number here
MOBILE_NUMBER = ""
THRESHOLD = 2

# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED",
                    "symbol": STOCK_NAME,
                    "apikey": STOCK_API_KEY}

response = requests.get(STOCK_ENDPOINT, stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for value in data.values()]

# get the closing stock price for yesterday
previous_day_end_price = float(data_list[0]["4. close"])

# get the closing stock price for two_days ago
prev_prev_day_end_price = float(data_list[1]["4. close"])

# find the percentage difference in the stock price change
diff = previous_day_end_price - prev_prev_day_end_price
if diff < 0:
    symbol = "✅"
else:
    symbol = "🔻"

diff = abs(diff)
diff_percent = (diff / previous_day_end_price) * 100
print(diff_percent)

# if the stock_price difference meets a threshold, then get news articles.
if diff_percent > THRESHOLD:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language": "en",
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params).json()
    all_articles = news_response["articles"]

# get first three articles
articles = all_articles[:3]



formatted_articles = [
    f"{STOCK_NAME}: {symbol}{round(diff_percent)}%\nHeadline: {article['title']}. \nBrief: {article['description']}. " \
    f"\nRead Here: {article['url']}" for
    article in articles]

url_images = [article['urlToImage'] for article in articles]

for x in url_images:
    print(x)

#  generate a client for the messaging twilio api
client = Client(TWILIO_SID, TWILIO_TOKEN)

# send the message to the desired mobile number
for index, article in enumerate(formatted_articles):
    message = client.messages.create(
        body=article,
        from_='+18556487635',
        media_url=[url_images[index]],
        to=MOBILE_NUMBER
    )
