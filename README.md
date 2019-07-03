# dividends

Issues requests to the [IEX Cloud API](https://iexcloud.io/) in order to access global symbol reference list as well as make requests for upcoming dividends. 
## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip
  + Github

## Installation

Fork this repository https://github.com/Darinmcc/dividends under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

After cloning the repo, navigate there from the command-line:

Possible locations
+ C:/Users/{username}/Documents/GitHub/dividends
+ Desktop/dividends


cd ~/Desktop/dividends


#Environment Setup
Create and activate a new Anaconda virtual environment:

conda create -n dividends-env python=3.7 # (first time only)

conda activate dividends-env

From within the virtual environment, install the required packages specified in the "requirements.txt":

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

#IEX Cloud API

Your program will need an API Key to issue requests to the IEX Cloud API (https://iexcloud.io/). 

Please click the get started button to create an account

 https://iexcloud.io/cloud-login#/register/ 
 
 complete registration to receive the necessary keys - can select free account


#Security Requirements

The program's source code should absolutely not include the secret API Key value. To not include the API key:

Create a file called ".env" and place the environment variable in the ".env" file

Set an environment variable IEX_API_KEY:

IEX_API_KEY="abc123"

The local ".gitignore" file prevents the ".env" file and its contents from being tracked


## Usage

from the command-line:

python app/dividends.py