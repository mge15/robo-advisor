# this is the "app/robo_advisor.py" file

import csv
import json
import os
import requests
import plotly
import plotly.express as px
from datetime import datetime
from dotenv import load_dotenv
from pandas import DataFrame
import matplotlib.pyplot as plt

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71

load_dotenv()
symbol_list = []

while True:
    symbol = input("Please input a stock or cryptocurrency symbol, or 'DONE' if there are no more stocks you would like to view: ")
    if symbol.upper() == "DONE":
        break
    if symbol.isalpha() and len(symbol) < 5:
        symbol_list.append(symbol)
    else:
        print("Expecting a properly-formed stock symbol like 'MSFT'. Please try again.")

api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

for sym in symbol_list:
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={sym}&apikey={api_key}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    if "Error Message" in parsed_response.keys():
        print()
        print("-------------------------")
        print("Sorry, couldn't find any trading data for the", sym.upper(), "stock symbol")
        print("-------------------------")
        print()
    else:
        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

        # assumes that first day is on top
        dates = list(parsed_response["Time Series (Daily)"].keys())
        latest_day = dates[0]

        latest_close = float(parsed_response["Time Series (Daily)"][latest_day]["4. close"])

        # get high price from each day
        high_prices = []
        low_prices = []
        late_closes = []
        end = 0

        for date in dates:
            high_price = float(parsed_response["Time Series (Daily)"][date]["2. high"])
            high_prices.append(high_price)
            low_price = float(parsed_response["Time Series (Daily)"][date]["3. low"])
            low_prices.append(low_price)
            late_close = float(parsed_response["Time Series (Daily)"][date]["4. close"])
            late_closes.append({"date": date, "stock price": late_close})

        # creating data frame
        line_df = DataFrame(late_closes)

        # maximum of all of the high prices
        recent_high = max(high_prices)

        # minimum of all the low prices
        recent_low = min(low_prices)

        timestamp = datetime.now()
        human_friendly_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        if latest_close < (1.2 * recent_low):
            recommendation = "Buy"
            reason = "The current stock price is close to the recent low i.e. within 20%"
        else:
            recommendation = "Don't Buy"
            reason = "The current stock price is too high to consider buying"

        csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", f"prices_{sym}.csv")

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
        print("SELECTED STOCK: ", sym.upper())
        print("-------------------------")
        print("REQUESTING STOCK MARKET DATA...")
        print("REQUEST AT: ", human_friendly_timestamp)
        print("-------------------------")
        print("LATEST DATA FROM: ", last_refreshed)
        print("LATEST CLOSE: ", to_usd(latest_close))
        print("RECENT HIGH: ", to_usd(recent_high))
        print("RECENT LOW: ", to_usd(recent_low))
        print("-------------------------")
        print("RECOMMENDATION: ", recommendation)
        print("RECOMMENDATION REASON: ", reason)
        print("-------------------------")
        print("WRITING DATA TO CSV: ", csv_file_path)
        print("-------------------------")
        print("Displaying Line Chart of Close Prices over Time in browser for your consideration...")
        graph = px.line(line_df, x="date", y="stock price", title=f"Stock Price over Time: {sym.upper()}")
        graph.show()
        print()

print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
