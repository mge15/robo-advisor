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

latest_day = parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close = float(parsed_response["Time Series (Daily)"][latest_day]["4. close"])

timestamp = datetime.now()
human_friendly_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", human_friendly_timestamp)
print("-------------------------")
print("LATEST DAY: ", latest_day)
print("LATEST CLOSE: ", to_usd(latest_close))
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
