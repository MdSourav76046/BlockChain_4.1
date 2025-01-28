import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        self.chain.append(new_block)

    def traverse_chain(self):
        for block in self.chain:
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("")

# Create a new blockchain
my_blockchain = Blockchain()

# Add four blocks to the blockchain
my_blockchain.add_block(Block("Transaction 1", ""))
my_blockchain.add_block(Block("Transaction 2", ""))
my_blockchain.add_block(Block("Transaction 3", ""))
my_blockchain.add_block(Block("Transaction 4", ""))

# Traverse the blockchain and print the contents of each block
my_blockchain.traverse_chain()