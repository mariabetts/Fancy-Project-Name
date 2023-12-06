import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

## plot for transactions over time
def scatter_plot(transactions):
    df = pd.DataFrame(transactions)
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
    df['age'] = (pd.to_datetime('now') - df['timeStamp']).dt.days

    # Round the transaction amounts to two decimal places
    df['value'] = df['value'].astype(float) / 1e18  # Convert from Wei to Ether
    df['value'] = df['value'].round(2)

    fig = px.scatter(df, x='timeStamp', y='value', title='Transaction Amounts Over Time', 
                         labels={'value': 'Transaction Amount (ETH)', 'timeStamp': 'Time'},
                         hover_data={'To': True, 'value': True, 'timeStamp': '|%Y-%m-%d %H:%M:%S'})
    fig.update_layout(xaxis_title='Time', yaxis_title='Transaction Amount (ETH)')
    fig.show()

## plot for heatmap based on transaction amounts to receving address
def heatmap(transactions):
    df = pd.DataFrame(transactions)

    df['value'] = df['value'].astype(float) / 1e18 # Convert from Wei to Ether
    
    fig = px.density_heatmap(df, x='to', y='value', title='Transaction Amounts to Receiving Addresses',
                         labels={'value': 'Transaction Amount (ETH)', 'to': 'Receiving Address'})
    fig.update_layout(xaxis_title='Receiving Address', yaxis_title='Transaction Amount (ETH)')
    fig.show()
    
## box plot 
def boxplot(transactions):
    df = pd.DataFrame(transactions)
    
    df['value'] = df['value'].astype(float) / 1e18 # Convert from Wei to Ether
    
    fig = px.box(df, x='to', y='value', title='Transaction Amounts from Main Address to Receiving Addresses',
             labels={'value': 'Transaction Amount (ETH)', 'to': 'Receiving Address'})
    fig.update_layout(xaxis_title='Receiving Address', yaxis_title='Transaction Amount (ETH)')
    fig.show()
    
    
## bubble map
def bubblemap(transactions):
    df = pd.DataFrame(transactions)
    
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
    df['value'] = pd.to_numeric(df['value'], errors='coerce') / 1e18  # Convert from Wei to Ether
    
    fig = px.scatter(df, x='timeStamp', y='value', title='Transaction Amounts Over Time', 
            labels={'value': 'Transaction Amount (ETH)', 'timeStamp': 'Time'},
            hover_data={'from': True, 'value': True, 'timeStamp': '|%Y-%m-%d %H:%M:%S'})

    fig.update_layout(xaxis_title='Time', yaxis_title='Transaction Amount (ETH)')
    fig.show()
    
    
