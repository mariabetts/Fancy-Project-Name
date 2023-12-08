import streamlit as st
import streamlit as st
import pandas as pd
from firebase_admin import firestore
from blockchain_logic import Block,Records,setup
def app():
    
    if 'db' not in st.session_state:
        st.session_state.db = ''

    db=firestore.client()
    st.session_state.db=db    

    if st.session_state.username=='':
        st.write('Please Login To View')
    else:
         
        st.title("Create and view how blockchains work")
        st.write("Here, you can learn how blockchain hashes are made and verified")
        
        input_sender = st.text_input("Input Sender")
        input_receiver = st.text_input("Input Receiver")
        input_amount = st.text_input("Insert Amount")
        
        pychain = setup()  
        if st.button("Add Block"):
            prev_block = pychain.chain[-1]
            prev_block_hash = prev_block.hash_block()
            new_block = Block(
            records = Records(sender=input_sender, receiver=input_receiver, amount=input_amount),
            creator_id = 42,
            previous_hash = prev_block_hash
        )
        
            pychain.add_block(new_block)
    
            st.write("here is the ledger information")
    
            pychain_df = pd.DataFrame(pychain.chain)
            st.write(pychain_df)

        if st.button("Validate Chain"):
            st.write(pychain.is_block_valid)