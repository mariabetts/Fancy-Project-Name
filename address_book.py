import streamlit as st
from firebase_admin import firestore

def app():
    st.header('Ethereum Addressbook ')
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db = firestore.client()
    st.session_state.db = db
    
    if st.session_state.username == '':
        st.write("Login to view")
    else:
        selected_action = st.selectbox("Select an action:", ["Add Address", "View Saved Addresses","Delete Address"])
        
        if selected_action == "Add Address":
            eth_address = st.text_input("Enter an Ethereum Address to Save")
            if st.button('Save Address') and eth_address:
                save_eth_address(st.session_state.username, eth_address)
                st.success('Address Is Now Saved')

        elif selected_action == "View Saved Addresses":
            display_saved_eth_addresses(st.session_state.username)
            
        elif selected_action == "Delete Address":
            eth_address_to_delete = st.selectbox("Select an address to delete:", get_saved_eth_addresses(st.session_state.username))
            if st.button('Delete Address') and eth_address_to_delete:
                delete_eth_address(st.session_state.username, eth_address_to_delete)
                st.success(f'Address "{eth_address_to_delete}" deleted successfully')

## for saving addresses
def save_eth_address(username, eth_address):
    info = st.session_state.db.collection('eth_addres').document(username).get()
    if info.exists:
        info_dict = info.to_dict()
        if 'saved_ethress' in info_dict.keys():
            pos = st.session_state.db.collection('eth_addres').document(username)
            pos.update({u'saved_ethress': firestore.ArrayUnion([u'{}'.format(eth_address)])})
        else:
            data = {"saved_ethress": [eth_address], 'Username': username}
            st.session_state.db.collection('eth_addres').document(username).set(data)
    else:
        data = {"saved_ethress": [eth_address], 'Username': username}
        st.session_state.db.collection('eth_addres').document(username).set(data)

 ##for viewing addresses
def display_saved_eth_addresses(username):
    info = st.session_state.db.collection('eth_addres').document(username).get()
    if info.exists:
        info_dict = info.to_dict()
        saved_eth_addresses = info_dict.get('saved_ethress', [])
        if saved_eth_addresses:
            st.header('Current Saved Ethereum Addresses')
            for address in saved_eth_addresses:
                st.write(f"- {address}")
        else:
            st.info("You haven't saved any Ethereum addresses yet.")
            
## get saved addresses  
def get_saved_eth_addresses(username):
    info = st.session_state.db.collection('eth_addres').document(username).get()
    if info.exists:
        info_dict = info.to_dict()
        return info_dict.get('saved_ethress', [])
    return []

## delete adresses   
def delete_eth_address(username, eth_address_to_delete):
    saved_eth_addresses = get_saved_eth_addresses(username)
    saved_eth_addresses.remove(eth_address_to_delete)
    st.session_state.db.collection('eth_addres').document(username).update({'saved_ethress': saved_eth_addresses})


            

    

            
    