import requests
from dotenv import load_dotenv
from pprint import pprint


import json
import csv
import os


load_dotenv() #> loads contents of the .env file into the script's environment

#GET /stock/{symbol}/dividends/next

csv_file_path_port = os.path.join(os.path.dirname(__file__), "..", "portfolio", "my_portfolio.csv")

csv_headers_port = ["Symbol"]
with open(csv_file_path_port, "r") as csv_file: # "w" means "open the file for writing"
    reader = csv.DictReader(csv_file, fieldnames=csv_headers_port)
    for row in reader:
        print(row["Symbol"])



# INFO INPUTS
#
print("Welcome to Daily Dividends!")
print("------------------------")
symbol = input("Enter stock symbol:")

api_key = os.environ.get("IEX_API_KEY")

symbol_ref_url = f"https://cloud.iexapis.com/stable/ref-data/symbols?token={api_key}"
ref_response = requests.get(symbol_ref_url) #< response variable - sends get requests, specify the URL for the request - see documentation
    #print(type(ref_response)) #<class 'requests.models.Response'>
    #print(ref_response.status_code) #200
    #print(type(ref_response.text))
    #print(ref_response.text) #same as print(response.json())
ref_parsed_response = json.loads(ref_response.text)

ref_dictionary = []

for symbols in ref_parsed_response:
    if symbols["symbol"] not in ref_dictionary:
        ref_dictionary.append(symbols["symbol"])

if symbol.upper() not in ref_dictionary:
    print("Not a valid stock symbol. Please re-run")
    exit()
else:
    dividend_url = f"https://cloud.iexapis.com/stable/stock/{symbol}/dividends/next?token={api_key}"
    dividend_response = requests.get(dividend_url) #< response variable - sends get requests, specify the URL for the request - see documentation#
        #print(type(dividend_response)) #<class 'requests.models.Response'>
        #print(dividend_response.status_code) #200
        #print(type(dividend_response.text))
        #print(dividend_response.text) #same as print(response.json())
    dividend_parsed_response = json.loads(dividend_response.text) # variable, parse str to dict
        #print(dividend_parsed_response)
    print(dividend_parsed_response)

#exDate	string	refers to the dividend ex-date
#paymentDate	string	refers to the payment date
#recordDate	string	refers to the dividend record date
#declaredDate	string	refers to the dividend declaration date
#amount	number	refers to the payment amount
    #flag	string	Type of dividend event
#currency	string	Currency of the dividend
#description	string	Description of the dividend event
#frequency	string	Frequency of the dividend

print(dividend_parsed_response["exDate"])

csv_file_path_div = os.path.join(os.path.dirname(__file__), "..", "data", "dividends.csv")
 #don't change csv file path or __file__ variable
 #file starts in app directory

csv_headers_div = ["Symbol","Ex Date", "Payment Date", "Record Date", "Declared Date", "Dividend Amount", "Dividend Event Type","Currency","Description","Frequency"]

with open(csv_file_path_div, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers_div)
    writer.writeheader() # uses fieldnames set above
    writer.writerow({
        "Symbol": dividend_parsed_response["symbol"], 
        "Ex Date": dividend_parsed_response["exDate"], 
        "Payment Date": dividend_parsed_response["paymentDate"], 
        "Record Date": dividend_parsed_response["recordDate"], 
        "Declared Date": dividend_parsed_response["declaredDate"], 
        "Dividend Amount": dividend_parsed_response["amount"],
        "Dividend Event Type": dividend_parsed_response["flag"],
        "Currency": dividend_parsed_response["currency"],
        "Description": dividend_parsed_response["description"],
        "Frequency": dividend_parsed_response["frequency"]})

print("-------------------------")





#price_url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={api_key}"
#price_response = requests.get(price_url) #< response variable - sends get requests, specify the URL for the request - see documentation
#print(type(price_response)) #<class 'requests.models.Response'>
#print(price_response.status_code) #200
#print(type(price_response.text))
#print(price_response.text) #same as print(response.json())
#price_parsed_response = json.loads(price_response.text) # variable, parse str to dict
#print(price_parsed_response)