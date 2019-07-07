import requests
from dotenv import load_dotenv
from pprint import pprint


import json
import csv
import os

load_dotenv() #> loads contents of the .env file into the script's environment


# READ CSV FILE MY_PORTFOLIO AND GENERATE LIST
watchlist = []

csv_file_path_port = os.path.join(os.path.dirname(__file__), "..", "portfolio", "my_portfolio.csv")

with open(csv_file_path_port, "r") as csv_file: # "w" means "open the file for writing"
    reader = csv.DictReader(csv_file) 
    for row in reader:
        if row not in watchlist:
            watchlist.append(row["Symbol"])

sorted_watchlist = sorted(watchlist)



# INFO INPUTS
print("Welcome to Daily Dividends!")
print("------------------------")
print(f"Please see your current Portfolio: \n {sorted_watchlist}")
runport = input(F"Would you like to run upcoming dividends on your current portfolio? 'Y/N' \n")




api_key = os.environ.get("IEX_API_KEY")

# PULLING SECURITY REFERENCE DATA
symbol_ref_url = f"https://cloud.iexapis.com/stable/ref-data/symbols?token={api_key}"
ref_response = requests.get(symbol_ref_url) #< response variable - sends get requests, specify the URL for the request - see documentation
    #print(type(ref_response)) #<class 'requests.models.Response'>
    #print(ref_response.status_code) #200
    #print(type(ref_response.text))
    #print(ref_response.text) #same as print(response.json())
ref_parsed_response = json.loads(ref_response.text)


#BUILDING LIST OF REFERENCE SYMBOLS
ref_dictionary = []

for ref_symbols in ref_parsed_response:
    if ref_symbols["symbol"] not in ref_dictionary:
        ref_dictionary.append(ref_symbols["symbol"])

if runport.upper() == "Y":

#TO DO BUILD OUT A KICK OUT SHOWING THE BAD SYMBOL
    blank = []
    dividend_parsed_list = []
    upcomingdiv = []

    for ticker in watchlist:
        if ticker not in ref_dictionary:
            print(f"Symbol: {ticker} not a valid stock symbol. Please re-run")
            exit()
    
        else:
            dividend_url = f"https://cloud.iexapis.com/stable/stock/{ticker}/dividends/next?token={api_key}"
            dividend_response = requests.get(dividend_url) #< response variable - sends get requests, specify the URL for the request - see documentation#
            dividend_parsed_response = json.loads(dividend_response.text)
            if dividend_parsed_response == blank: #same as print(response.json())
                continue
            else:
                # variable, parse str to dict
                dividend_parsed_list.append(dividend_parsed_response)
                upcomingdiv.append(dividend_parsed_response["symbol"])
            
#print(dividend_parsed_list)

    divparse = 0

# BUILDING A SKIP FOR VALID SYMBOLS W/O DIVS

        # WRITE DIVIDENDS TO CSV FILE
    csv_file_path_div = os.path.join(os.path.dirname(__file__), "..", "data", "dividends.csv")
        #don't change csv file path or __file__ variable
        #file starts in app directory

    csv_headers_div = ["Symbol","Ex Date", "Payment Date", "Record Date", "Declared Date", "Dividend Amount", "Dividend Event Type","Currency","Description","Frequency"]

    with open(csv_file_path_div, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers_div)
        writer.writeheader() # uses fieldnames set above
        for row in upcomingdiv:
            writer.writerow({
                "Symbol": dividend_parsed_list[divparse]["symbol"], 
                "Ex Date": dividend_parsed_list[divparse]["exDate"], 
                "Payment Date": dividend_parsed_list[divparse]["paymentDate"], 
                "Record Date": dividend_parsed_list[divparse]["recordDate"], 
                "Declared Date": dividend_parsed_list[divparse]["declaredDate"], 
                "Dividend Amount": dividend_parsed_list[divparse]["amount"],
                "Dividend Event Type": dividend_parsed_list[divparse]["flag"],
                "Currency": dividend_parsed_list[divparse]["currency"],
                "Description": dividend_parsed_list[divparse]["description"],
                "Frequency": dividend_parsed_list[divparse]["frequency"]})
            divparse += 1

    print("-------------------------")
    print("Please check dividends.csv file for upcoming dividends!")
    print("-------------------------")
else:
    sblank = []
    runsymbol = input(F"Would you like to run upcoming dividends for an adhoc symbol? 'Y/N' \n")
    if runsymbol.upper() == "Y":
        symbol = input("Enter stock symbol:").upper()
        if symbol not in ref_dictionary:
            print(f"Symbol: {symbol} not a valid stock symbol. Please re-run")
            exit()
    
        else:
            dividend_url = f"https://cloud.iexapis.com/stable/stock/{symbol}/dividends/next?token={api_key}"
            dividend_response = requests.get(dividend_url) #< response variable - sends get requests, specify the URL for the request - see documentation#
            dividend_parsed_response = json.loads(dividend_response.text)
            if dividend_parsed_response == sblank: #same as print(response.json())
                print("-------------------------")
                print(f"There are no upcoming dividends for symbol: {symbol}")
                print("-------------------------")
                exit()
            else:
                # variable, parse str to dict
                print("-------------------------")
                print("See dividend details below.")
                print("-------------------------")
                print(dividend_parsed_response)
                print("-------------------------")
    else:
        print("-------------------------")
        print("Sorry we couldn't assist with your Daily Dividend needs.")
        print("Maybe next time...:)")
        print("-------------------------")






