import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import requests
from utilsformapping import get_transaction_list, get_account_balance, visualize_transaction_graph 

def app():
    st.title("Transaction Mapping")
    api_key = "ZACGG1654HI5ANR3P2XIX558YRQGCR4UI5"

    ether_address = st.text_input("Enter The Desired Ethereum Address")
    
    if ether_address:
        balance = get_account_balance(api_key, ether_address)
        st.success(f"Account balance: {balance}")
        transactions = get_transaction_list(api_key, ether_address)
        visualize_transaction_graph(transactions)
        st.pyplot()
    

st.write("transaction mapping")


            

            