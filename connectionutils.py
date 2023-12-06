import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
import requests


#connect to etherscan
def get_account_balance(api_key, address):
    base_url = "https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data["result"]

def get_transaction_list(api_key, address):
    base_url = "https://api.etherscan.io/api"
    api_key = "ZACGG1654HI5ANR3P2XIX558YRQGCR4UI5"
    params = {
        "module": "account",
        "action": "txlist",
        "address": address,
        "startblock": 0,
        "endblock": 99999999,
        "sort": "asc",
        "apikey": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data["result"]




    

    
    


    