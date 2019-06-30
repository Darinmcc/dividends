import requests
from dotenv import load_dotenv
from pprint import pprint


import json
import csv
import os


load_dotenv() #> loads contents of the .env file into the script's environment

#GET /stock/{symbol}/dividends/next





# INFO INPUTS
#
print("Welcome to Daily Dividends!")
print("------------------------")
symbol = input("Enter stock symbol:")

api_key = os.environ.get("IEX_API_KEY")

symbol_ref_url = f"https://cloud.iexapis.com/stable/ref-data/symbols?token={api_key}"
ref_response = requests.get(symbol_ref_url) #< response variable - sends get requests, specify the URL for the request - see documentation
print(type(ref_response)) #<class 'requests.models.Response'>
print(ref_response.status_code) #200
print(type(ref_response.text))
#print(ref_response.text) #same as print(response.json())
ref_parsed_response = json.loads(ref_response.text)
print(type(ref_parsed_response))


dividend_url = f"https://cloud.iexapis.com/stable/stock/{symbol}/dividends/ytd?token={api_key}"
dividend_response = requests.get(dividend_url) #< response variable - sends get requests, specify the URL for the request - see documentation
print(type(dividend_response)) #<class 'requests.models.Response'>
print(dividend_response.status_code) #200
print(type(dividend_response.text))
#print(dividend_response.text) #same as print(response.json())
dividend_parsed_response = json.loads(dividend_response.text) # variable, parse str to dict
print(dividend_parsed_response)




#if symbol is not in ref_parsed_response:
    #print("Not a valid stock symbol. Please re-run")
    #exit()
#else:
    #print(price_parsed_response)


#USE TO CYCLE THROUGH LIST FOR SYMBOLS
#print(price_parsed_response[0]["symbol"])

#breakpoint()

#--csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
 #don't change csv file path or __file__ variable
 #file starts in app directory

#--csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

#--with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    #--writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    #--writer.writeheader() # uses fieldnames set above
    #--for date in dates:
        #--daily_prices = tsd[date]
        #--writer.writerow({
            #-"timestamp": date, 
            #-"open": daily_prices["1. open"], 
            #-"high": daily_prices["2. high"], 
            #-"low": daily_prices["3. low"], 
            #-"close": daily_prices["4. close"], 
            #-"volume": daily_prices["5. volume"]})


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





#price_url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={api_key}"
#price_response = requests.get(price_url) #< response variable - sends get requests, specify the URL for the request - see documentation
#print(type(price_response)) #<class 'requests.models.Response'>
#print(price_response.status_code) #200
#print(type(price_response.text))
#print(price_response.text) #same as print(response.json())
#price_parsed_response = json.loads(price_response.text) # variable, parse str to dict
#print(price_parsed_response)