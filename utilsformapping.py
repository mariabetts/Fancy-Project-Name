import networkx as nx
import matplotlib.pyplot as plt
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

## definitely need to tinker with this and other params of visualization 
def visualize_transaction_graph(transactions):
    G = nx.DiGraph()

    # Add edges (transactions) to the graph
    for tx in transactions:
        G.add_edge(tx["from"], tx["to"])

    # Visualize the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", arrowsize=10)
    plt.title("Ethereum Transaction Graph")
    plt.axis("on")


    