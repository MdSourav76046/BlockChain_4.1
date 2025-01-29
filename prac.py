import hashlib


class Block:
    def __init__(self, data, previosu_hash):
        self.data = data
        self.previous_hash = previosu_hash
        self.nonse = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        hash_string = str(self.data) + self.previous_hash + str(self.nonse)
        return hashlib.sha256(hash_string.encode()).hexdigest()
    
    
    def mine_block(self, difficulty):
        while self.hash[0:difficulty] != '0' * difficulty:
            self.nonse += 1
            self.hash = self.calculate_hash()
            

class BlockChain:
    def __init__(self):
        self.difficulty = 2
        self.v = []
        self.v.append(self.create_genesis_block())
    
    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def get_previous_block(self):
        return self.v[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.v[-1].hash
        new_block.mine_block(self.difficulty)
        self.v.append(new_block)



blockchain = BlockChain()
for block in blockchain.v:
    print("Block Data ", block.data)
    print("Block Hash ", block.hash)   
    
blockchain.add_block(Block("Block 1", ""))
blockchain.add_block(Block("Block 2", ""))
blockchain.add_block(Block("Block 3", ""))
for block in blockchain.v:
    print("Block Data ", block.data)
    print("Block Hash ", block.hash)  
    
  
        
    