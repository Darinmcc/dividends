import requests
from dotenv import load_dotenv
from pprint import pprint


import json
import csv
import os


load_dotenv() #> loads contents of the .env file into the script's environment

#GET /stock/{symbol}/dividends/next

api_key = os.environ.get("IEX_API_KEY")

url = f"https://cloud.iexapis.com/stable/tops?token={api_key}&symbols=aapl"

response = requests.get(url)

#print(type(response)) #<class 'requests.models.Response'>
#print(response.status_code) #200
#print(type(response.text))
print(response.text) #same as print(response.json())


parsed_response = json.loads(response.text) # variable, parse str to dict


print(type(parsed_response))

print(parsed_response[0]["symbol"])


#print("-------------------------")
#print("SELECTED SYMBOL: XYZ")
#print("-------------------------")
#print("REQUESTING STOCK MARKET DATA...")
#print("REQUEST AT: 2018-02-20 02:00pm")
#print("-------------------------")
#print("LATEST DAY: 2018-02-20")
#print("LATEST CLOSE: $100,000.00")
#print("RECENT HIGH: $101,000.00")
#print("RECENT LOW: $99,000.00")
#print("-------------------------")
#print("RECOMMENDATION: BUY!")
#print("RECOMMENDATION REASON: TODO")
#print("-------------------------")
#print("HAPPY INVESTING!")
print("-------------------------")