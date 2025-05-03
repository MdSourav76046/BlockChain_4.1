import hashlib
import binascii

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

def sha_256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def membership_proof(tree, data):
    current_hash = sha_256(data.encode())
    
    for level in merkle_tree['levels']:
        if len(level) == 1:
            break
        
        if current_hash in level:
            ind = level.index(current_hash)
            
            sibling_ind = ind
            if ind % 2 == 0:
                sibling_ind += 1
            else:
                sibling_ind -= 1
                
            sibling_hash = level[sibling_ind]
            
            left = current_hash
            right = sibling_hash
            
            if(ind % 2 == 1):
                left = sibling_hash
                right = current_hash
            
            left = binascii.unhexlify(left)
            right = binascii.unhexlify(right)
            current_hash = sha_256(left + right)
            
    
    return current_hash == merkle_tree['root']

ok = membership_proof(merkle_tree, 'orange')
print("valid ?", ok)