import hashlib

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        hashStirng = str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hashStirng.encode()).hexdigest()
    
    def proof_of_work(self, difficulty):
        while(self.hash[:difficulty] != '0' * difficulty):
            self.nonce += 1
            self.hash  = self.calculate_hash()
            
        
    
class Blockchain:
    def __init__(self):
        self.difficulty = 2
        self.list = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def get_last_block(self):
        return self.list[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.proof_of_work(self.difficulty)
        self.list.append(new_block)


#Create the Blockchain
blockchain = Blockchain()   
blockchain.add_block(Block("Block 1", ""))
blockchain.add_block(Block("Block 2", ""))
blockchain.add_block(Block("Block 3", ""))

for block in blockchain.list:
    print("Data ", block.data)
    print("Hash ", block.hash)
     