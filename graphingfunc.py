import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


## plot for transactions over time
def scatter_plot(transactions):
    df = pd.DataFrame(transactions)
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
    df['age'] = (pd.to_datetime('now') - df['timeStamp']).dt.days
    df['value'] = df['value'].astype(float) / 1e18  # Convert from Wei to Ether
    df['value'] = df['value'].round(2)

    fig = px.scatter(df, x='timeStamp', y='value', title='Transaction Amounts Over Time', 
                         labels={'value': 'Transaction Amount (ETH)', 'timeStamp': 'Time'},
                         hover_data={'to': True, 'value': True, 'timeStamp': '|%Y-%m-%d %H:%M:%S'})
    
    fig.update_layout(xaxis_title='Time', yaxis_title='Transaction Amount (ETH)')
    st.plotly_chart(fig)

## plot for heatmap based on transaction amounts to receving address
def heatmap(transactions):
    df = pd.DataFrame(transactions)
    df['value'] = df['value'].astype(float) / 1e18  # Convert from Wei to Ether
    df['to'] = df['to'].astype(str) 
    df['count_capped'] = df.groupby('to')['value'].transform(lambda x: min(x.sum(), 50))

    fig = px.density_heatmap(df, x='to', y='count_capped', title='Transaction Amounts to Receiving Addresses',
                         labels={'count_capped': 'Capped Transaction Amount (ETH)', 'to': 'Receiving Address'})

    fig.update_layout(xaxis_title='Receiving Address', yaxis_title='Transaction Amount (ETH)')
    fig.update_xaxes(type='category')
    fig.update_traces(hovertemplate='Receiving Address: %{x}<br>Transaction Amount (ETH): %{y}')

    st.plotly_chart(fig)
    
## box plot 
def boxplot(transactions):
    df = pd.DataFrame(transactions)

    df['value'] = df['value'].astype(float) / 1e18  # Convert from Wei to Ether
    df['to'] = df['to'].astype(str)  # Ensure 'to' column is treated as a string

    fig = px.box(df, x='to', y='value', title='Transaction Amounts from Main Address to Receiving Addresses',
                 labels={'value': 'Transaction Amount (ETH)', 'to': 'Receiving Address'})
    
    fig.update_layout(xaxis_title='Receiving Address', yaxis_title='Transaction Amount (ETH)')
    fig.update_xaxes(type='category')
    fig.update_traces(hovertemplate='Receiving Address: %{x}<br>Transaction Amount (ETH): %{y}')
    
    st.plotly_chart(fig)
    
## bubble map
def bubblemap(transactions):
    df = pd.DataFrame(transactions)
    df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')
    df['value'] = pd.to_numeric(df['value'], errors='coerce') / 1e18  # Convert from Wei to Ether

    fig = px.scatter(df, x='timeStamp', y='value', size='value', color='timeStamp',
                 title='Bubble Chart of Transaction Amounts Over Time',
                 labels={'value': 'Transaction Amount (ETH)', 'timeStamp': 'Time'},
                 hover_data={'from': True, 'value': True, 'timeStamp': '|%Y-%m-%d %H:%M:%S'})
    
    fig.update_layout(xaxis_title='Time', yaxis_title='Transaction Amount (ETH)')
    st.plotly_chart(fig)
    
    
