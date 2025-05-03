# Write a program in Python to implement a blockchain and UTXo (unspent transaction output). 

# Importing required libraries
import hashlib

# Defining the UTXO class
class UTXO:
    def __init__(self, txid, index, value):
        self.txid = txid
        self.index = index
        self.value = value

    def __str__(self):
        return f"UTXO ({self.txid}:{self.index}) with value {self.value}"
    def __repr__(self):
        return self.__str__()

# Defining the transaction class
class Transaction:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def __str__(self):
        return f"Transaction with {len(self.inputs)} inputs and {len(self.outputs)} outputs"
    


    def hash(self):
        # Generating a hash for the transaction
        tx_input = ''
        for i in range(0, len(self.inputs), 1):
            inp = self.inputs[i]
            tx_input += str(inp.txid) + str(inp.index)

        tx_output = ''
        for i in range(0, len(self.outputs), 1):
            out = self.outputs[i]
            tx_output += str(out.value)
            
        tx_data = tx_input + tx_output
        return hashlib.sha256(tx_data.encode('utf-8')).hexdigest()

# Defining the sample UTXOs and transactions
utxo1 = [UTXO('txid1', 0, 10), UTXO("txid1", 1, 5)]
utxo2 = UTXO('txid2', 1, 20)

input1 = utxo1
output1 = [UTXO('txid3', 0, 15)]
tx1 = Transaction(input1, output1)

input2 = [utxo2]
output2 = [UTXO('txid4', 0, 15), UTXO('txid4', 1, 5)]
tx2 = Transaction(input2, output2)

# Printing the UTXOs and transactions
print(utxo1)
print(utxo2)
print(tx1)
print(tx2)

# Generating hashes for the transactions
print(tx1.hash())
print(tx2.hash())