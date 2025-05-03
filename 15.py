import hashlib
import binascii

# Define the Merkle Tree with corrected root
merkle_tree = {
    'root': 'c9475ba22e175fbc3556e5795d6dc1c579fc48bdb806cca3bf79a7f6e7c79290',
    'levels': [
        ['3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b',
         '78e7771b8b46e11ddb34ba48887e1330525215f96d94778980d1186e6f09f6b4',
         'f9782dd7999dc14b39c1329735e6e4ef72e77a3cf5fa32f2f57bf8d5493f0fc5',
         '6455dbcb9597e2174aedccfd387db577d487fc7fc6027c2d66eb7c239cf56922'],
        ['598fc043e5ed43b9c82bf89ece2688d2b2fdce099cd6830b6446b1a99360854c',
         '87089fb19e5aff0c7bca0528e40155ee737148b8b5eba53f529d9ad19e1c0d5b'],
        ['c9475ba22e175fbc3556e5795d6dc1c579fc48bdb806cca3bf79a7f6e7c79290']
    ]
}

def sha256_hex(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def generate_and_verify(element, merkle_tree):
    current_hash = hashlib.sha256(element.encode()).hexdigest()

    for level in merkle_tree['levels']:
        if len(level) == 1:
            break

        if current_hash not in level:
            return False  # Element not found in this level

        idx = level.index(current_hash)

        # Use standard if/else for sibling index
        if idx % 2 == 0:
            sibling_idx = idx + 1
        else:
            sibling_idx = idx - 1

        sibling = level[sibling_idx]

        # Use standard if/else for ordering left/right
        if idx % 2 == 0:
            left = current_hash
            right = sibling
        else:
            left = sibling
            right = current_hash

        combined = binascii.unhexlify(left) + binascii.unhexlify(right)
        current_hash = sha256_hex(combined)

    return current_hash == merkle_tree['root']

# Run the check
ok = generate_and_verify("apple", merkle_tree)
print("Verified?", ok)