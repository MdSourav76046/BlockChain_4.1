# Code to generate all levles of merklee tree

import hashlib
import binascii

def sha256_hex(data: bytes) -> str:
    """Returns the SHA-256 hash of the given data as a hex string."""
    return hashlib.sha256(data).hexdigest()

def build_merkle_tree(leaves):
    """Builds a Merkle tree and returns its levels and root."""
    # Compute leaf hashes
    level = [sha256_hex(leaf.encode('utf-8')) for leaf in leaves]
    levels = [level]
    
    # Build up until root
    while len(level) > 1:
        if len(level) % 2 == 1:
            level.append(level[-1])  # duplicate last for odd count
        # Compute parent level
        parent = []
        for i in range(0, len(level), 2):
            left = binascii.unhexlify(level[i])
            right = binascii.unhexlify(level[i+1])
            parent.append(sha256_hex(left + right))
        levels.append(parent)
        level = parent
    
    root = levels[-1][0]
    return levels, root


# Example usage with the given leaves
leaves = ["apple", "Orange", "Banana", "Mango"]
levels, root = build_merkle_tree(leaves)

print("Merkle Tree Levels:")
for i, lvl in enumerate(levels):
    print(f"Level {i}: {lvl}")
print("\nMerkle Root:", root)


