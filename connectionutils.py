import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
from datetime import datetime
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

## get transactions and connect to api w/ key
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

def get_address_info(address):
    base_url = 'https://api.etherscan.io/api'
    api_key = "ZACGG1654HI5ANR3P2XIX558YRQGCR4UI5"
    
    transactions_url = f'{base_url}?module=account&action=txlist&address={address}&apikey={api_key}'
    transactions_response = requests.get(transactions_url)
    transactions_data = transactions_response.json()
    transactions = transactions_data.get('result', [])

    if not transactions:
        return {
            'Latest Transaction Date': 'No transactions',
            'Minimum Transaction Value (ETH)': 'No transactions',
            'Maximum Transaction Value (ETH)': 'No transactions',
            'Most Common Address Received From': 'No transactions',
            'Most Common Address Sent To': 'No transactions'
        }
    
    # get date of the latest transaction
    latest_transaction_timestamp = int(transactions[0]['timeStamp'])
    latest_transaction_date = datetime.utcfromtimestamp(latest_transaction_timestamp).strftime('%m/%d/%Y %H:%M:%S')
    
    # get minimum and maximum transaction values (converted to Ether using the metrics in graphfunc)
    transaction_values = [int(tx['value']) for tx in transactions]
    min_transaction = min(transaction_values) / 1e18
    max_transaction = max(transaction_values) / 1e18
    
    # get the most common addresses received from and sent to address wanted
    to_addresses = [tx['to'] for tx in transactions]
    from_addresses = [tx['from'] for tx in transactions]
    
    common_to_address = max(set(to_addresses), key=to_addresses.count)
    common_from_address = max(set(from_addresses), key=from_addresses.count)
    
    return {
        'Latest Transaction Date': latest_transaction_date,
        'Minimum Transaction Value (ETH)': f'{min_transaction:.4f}',
        'Maximum Transaction Value (ETH)': f'{max_transaction:.4f}',
        'Most Common Address Received From': common_from_address,
        'Most Common Address Sent To': common_to_address
    }



    

    



    

    
    


    
