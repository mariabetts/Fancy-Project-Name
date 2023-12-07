import streamlit as st
from firebase_admin import firestore
from address_book import get_saved_eth_addresses
from connectionutils import get_address_info

def app():
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db = firestore.client()
    st.session_state.db = db

    if st.session_state.username == '':
        st.write('Please Login To View')
    else:
        st.title("Address Information/Insights")
        st.write("Get the latest on an ethereum address")
        api_key = "ZACGG1654HI5ANR3P2XIX558YRQGCR4UI5"
        ether_address = get_saved_eth_addresses(st.session_state.username)

    if ether_address:
        address = st.selectbox("Please Select a saved address", ether_address)

        if st.button('Get Address Information'):
            address_info = get_address_info(address)
            st.subheader('Address Information:')
            for key, value in address_info.items():
                st.write(f'{key}: {value}')
    else:
        st.warning("You haven't saved any addresses yet")
        st.stop()
            
            