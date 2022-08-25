import requests
import os
from datetime import datetime as dt
from newsapi import NewsApiClient
from twilio.rest import Client

if __name__ == "__main__":
    STOCK_NAME = "TSLA"
    COMPANY_NAME = "Tesla Inc"
    API = "D01A64Z909JO51QA"

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    params_res = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_NAME,
        'datatype': 'json',
        'apikey': API
    }
    paramas_two_res = {
        'q': 'tesla',
        'from': '2022-08-23',
        'sortBy': 'publishedAt',
        'apiKey': 'c90c540f2d3e4b9694752582630a3b30'
    }

    date = dt.now()

        ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    response = requests.get(url=STOCK_ENDPOINT, params=params_res)
    #TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
    close = float(response.json()["Time Series (Daily)"]["2022-08-23"]["4. close"])

    #TODO 2. - Get the day before yesterday's closing stock price
    close_one = float(response.json()["Time Series (Daily)"]["2022-08-22"]['4. close'])

    #TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    dif: float
    min: float
    high: float
    if close > close_one:
        dif = close-close_one
        high = close
        min = close_one
    elif close < close_one:
        dif = close_one-close
        high = close_one
        min = close
    else:
        dif = close-close_one
        high = close
        min = close_one

    #TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    perc = (high % min)-1


    #TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    news = requests.get(url=NEWS_ENDPOINT, params=paramas_two_res)
    if perc > 5:
        print("Get News")
        ## STEP 2: https://newsapi.org/
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    #TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

    #TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    articles = news.json()["articles"]
    send_news = []
    send_news.append(articles[0])
    send_news.append(articles[1])
    send_news.append(articles[2])

        ## STEP 3: Use twilio.com/docs/sms/quickstart/python
        #to send a separate message with each article's title and description to your phone number.

    #TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    #TODO 9. - Send each article as a separate message via Twilio.
    account_sid = os.environ.get("ASID")
    auth_token = os.environ.get("ATOKEN")
    client = Client(account_sid, auth_token)

    for now in send_news:        
        message = client.messages.create(
            body=f'TSLA: {perc}\nHeadline:{now["title"]}\nBrief:{now["description"]}',
            from_='+19403605740',
            to='+4915753695452'
        )

    #Optional TODO: Format the message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """

