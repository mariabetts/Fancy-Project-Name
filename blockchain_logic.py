from dataclasses import dataclass
from typing import List
import datetime as datetime
import hashlib
import streamlit as st


@dataclass
class Records:
    sender:str
    receiver:str
    amount:float
    
@dataclass
class Block:
    records:Records
    creator_id:int  
    previous_hash: str = 0
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    nonce: str = 0
    
    def hash_block(self):
        sha_encrypt = hashlib.sha256()
        
        records = str(self.records).encode()
        sha_encrypt.update(records)
        
        creator_id = str(self.creator_id).encode()
        sha_encrypt.update(creator_id)
        
        previous_hash = str(self.previous_hash).encode()
        sha_encrypt.update(previous_hash)
        
        nonce = str(self.nonce).encode()
        sha_encrypt.update(nonce)

        return sha_encrypt.hexdigest()

@dataclass
class PyChain:
    chain: List[Block]
    difficulty: int = 4
    
    def proof_of_work(self,block):
        calculated_hash = block.hash_block()
        
        number_of_zeros = "0" * self.difficulty
        
        while not calculated_hash.startswith(number_of_zeros):
            
            block.nonce += 1
            
            calculated_hash = block.hash_block()
            
        print("Placeholder Hash", calculated_hash)
        return block
    
    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]
    
    def is_block_valid(self):
        block_hash = self.chain[0].hash_block()
        
        for block in self.chain[1:]:
            if block_hash != block.previous_hash:
                print("Invalid Blockchain")
                return True
            
            block_hash = block.hash_block
        
        print("Blockchain Is Valid")
        return True

@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing Chain")
    return PyChain([Block({'sender': 'Genesis', 'receiver': 'Genesis', 'amount': 'Genesis'}, 0)])
