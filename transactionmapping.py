import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from firebase_admin import firestore
from utilsformapping import get_transaction_list, get_account_balance, visualize_transaction_graph

def app():
    
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db    

    if st.session_state.username=='':
        st.write('Please Login To View')
    else:
        st.title("Transaction Mapping")
        st.write("Welcome to the Transaction Mapping Tool")
        api_key = "ZACGG1654HI5ANR3P2XIX558YRQGCR4UI5"
        
        
        ether_address = st.text_input("Enter The Desired Ethereum Address or Import")
    
        if ether_address:
            st.set_option('deprecation.showPyplotGlobalUse', False)
            
            balance = get_account_balance(api_key, ether_address)
            st.success(f"Account balance: {balance}")
            transactions = get_transaction_list(api_key, ether_address)
            visualize_transaction_graph(transactions)
            st.pyplot()
            

            

            
    


            

            