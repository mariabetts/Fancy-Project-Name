import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from firebase_admin import firestore
from connectionutils import get_transaction_list, get_account_balance
from graphingfunc import scatter_plot, bubblemap, heatmap, boxplot
from address_book import get_saved_eth_addresses

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

    
        ether_address = get_saved_eth_addresses(st.session_state.username)
        if ether_address:
            select_address = st.selectbox("Please Select a saved address", ether_address)
        else:
            st.warning("You haven't saved any addresses yet")
            st.stop
        
        if select_address:
            graphing_choice = st.selectbox("Please Select Which Graph To Make",  ['Click Me','Scatter Plot', 'Bubble Map', 'Heatmap', 'Box Plot'])
            transactions = get_transaction_list(api_key, select_address)
            if graphing_choice == "Scatter Plot":
                scatter_plot(transactions)
                st.pyplot(transactions)
            elif graphing_choice == "Bubble Map":
                bubblemap(transactions)
                st.pyplot(transactions)
            elif graphing_choice == 'Heatmap':
                heatmap(transactions)
                st.pyplot(transactions)
            elif graphing_choice == 'Box Plot':
                boxplot(transactions)
                st.pyplot(transactions)
                
            

            
        

            
            
 
            

            

            
    


            

            
