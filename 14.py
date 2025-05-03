# Write a program in Python to Create a Merkle Tree in Blockchain 

import hashlib

def build_merkle_tree(leaves):
    num_leaves = len(leaves)

    # If there is only one leaf, return it as the Merkle root
    if num_leaves == 1:
        return hashlib.sha256(leaves[0].encode()).hexdigest()

    # If the number of leaves is odd, duplicate the last leaf
    if num_leaves % 2 == 1:
        leaves.append(leaves[-1])
        num_leaves += 1

    # Use a for loop to create pairs and compute hashes
    hashes = []

    for i in range(0, num_leaves, 2):
        pair = leaves[i] + leaves[i + 1]

        hash_value = hashlib.sha256(pair.encode()).hexdigest()
        hashes.append(hash_value)

    # Recursively build the Merkle tree from the hashes 
    print(hashes)
    return build_merkle_tree(hashes)

# Example usage
leaves = ["apple", "Orange", "Banana", "Mango"]
for val in leaves:
    print( hashlib.sha256(val.encode()).hexdigest())
merkle_root = build_merkle_tree(leaves)
print("Merkle root:", merkle_root)

