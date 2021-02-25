# this is the "app/robo_advisor.py" file

import csv
import json
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71

load_dotenv()

while True:
    symbol = input("Please input one stock or cryptocurrency symbol: ")
    if symbol.isalpha() and len(symbol) < 5:
        break
    else:
        print("Expecting a properly-formed stock symbol like 'MSFT'. Please try again.")

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

if parsed_response.contains("error"):
    print("Sorry, couldn't find any trading data for that stock symbol")
    break #fix this
else:


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


csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = parsed_response["Time Series (Daily)"][date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        })


print("-------------------------")
print("SELECTED SYMBOL: ", symbol.upper())
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", human_friendly_timestamp)
print("-------------------------")
print("LATEST DAY: ", last_refreshed)
print("LATEST CLOSE: ", to_usd(latest_close))
print("RECENT HIGH: ", to_usd(recent_high))
print("RECENT LOW: ", to_usd(recent_low))
print("-------------------------")
print("RECOMMENDATION: BUY!") #need to still do this
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("WRITING DATA TO CSV: ", csv_file_path)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
