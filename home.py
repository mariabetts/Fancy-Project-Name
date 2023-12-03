import streamlit as st
from firebase_admin import firestore

def app():
    st.header('Ethereum Addressbook ')
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db
    
  
    if st.session_state.username=='':
        st.write("Login to view")
    else:
        eth_address = st.text_input("Enter an Ethereum Address to Save")
        if st.button('Save Address'):
            if eth_address !='':
                    
                info = db.collection('eth_addres').document(st.session_state.username).get()
            if info.exists:
                info = info.to_dict()
                if 'saved_ethress' in info.keys():
                
                    pos=db.collection('eth_addres').document(st.session_state.username)
                    pos.update({u'saved_ethress': firestore.ArrayUnion([u'{}'.format(eth_address)])})
                    
                else:
                    
                    data={"saved_ethress":[eth_address],'Username':st.session_state.username}
                    db.collection('eth_addres').document(st.session_state.username).set(data)    
            else:
                    
                data={"saved_ethress":[eth_address],'Username':st.session_state.username}
                db.collection('eth_addres').document(st.session_state.username).set(data)
                
            st.success('Address Is Now Saved')
    

            
    