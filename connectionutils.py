import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
from datetime import datetime,timezone
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
            'Latest Transaction Age (days)': 'No transactions',
            'Oldest Transaction Age (days)': 'No transactions',
            'Minimum Transaction Value (ETH)': 'No transactions',
            'Maximum Transaction Value (ETH)': 'No transactions',
            'Most Common Address Received From': 'No transactions',
            'Most Common Address Sent To': 'No transactions',
            'Latest Movement Type': 'No transactions',
            'Account Age': 'No transactions',
            
        }

    # Get minimum and maximum transaction values (converted to Ether using the metrics in graphfunc)
    transaction_values = [int(tx['value']) for tx in transactions]
    min_transaction = min(transaction_values) / 1e18
    max_transaction = max(transaction_values) / 1e18

    # Get the most common addresses received from and sent to the address
    to_addresses = [tx['to'] for tx in transactions]
    from_addresses = [tx['from'] for tx in transactions]

    common_to_address = max(set(to_addresses), key=to_addresses.count)
    common_from_address = max(set(from_addresses), key=from_addresses.count)

    # Get the timestamp of the oldest/newest transaction
    oldest_transaction_timestamp = min(int(tx['timeStamp']) for tx in transactions)
    youngest_transaction_timestamp = max(int(tx['timeStamp']) for tx in transactions)

    # Convert the timestamp to UTC
    oldest_transaction_utc = datetime.utcfromtimestamp(oldest_transaction_timestamp).replace(tzinfo=timezone.utc)
    youngest_transaction_timestamp_utc = datetime.utcfromtimestamp(youngest_transaction_timestamp).replace(tzinfo=timezone.utc)
    return {
        'Oldest Transaction Date:': f'{oldest_transaction_utc}',
        'Latest Transaction Date:': f'{youngest_transaction_timestamp_utc}',
        'Minimum Transaction Value (ETH)': f'{min_transaction:.4f}',
        'Maximum Transaction Value (ETH)': f'{max_transaction:.4f}',
        'Most Common Address Received From': common_from_address,
        'Most Common Address Sent To': common_to_address,
        
    }


    

    



    

    
    


    
