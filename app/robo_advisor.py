# this is the "app/robo_advisor.py" file

import requests
import json
from datetime import datetime

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

# assumes that first day is on top
dates = list(parsed_response["Time Series (Daily)"].keys())
latest_day = dates[0]

latest_close = float(parsed_response["Time Series (Daily)"][latest_day]["4. close"])

# get high price form each day
high_prices = []
low_prices = []

for date in dates:
    high_price = float(parsed_response["Time Series (Daily)"][date]["2. high"])
    high_prices.append(high_price)
    low_price = float(parsed_response["Time Series (Daily)"][date]["3. low"])
    low_prices.append(low_price)

# maximum of all of the high prices
recent_high = max(high_prices)

# minimum of all the low prices
recent_low = min(low_prices)

timestamp = datetime.now()
human_friendly_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", human_friendly_timestamp)
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: ", to_usd(latest_close))
print("RECENT HIGH: ", to_usd(recent_high))
print("RECENT LOW: ", to_usd(recent_low))
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
