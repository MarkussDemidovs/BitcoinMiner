import hashlib

NONCE_LIMIT = 100000000000
zeroes = 4

print(hashlib.sha256("Hello World".encode()).hexdigest())

def mine(blockNum, trans, previousHash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(blockNum) + trans + previousHash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found Hash With Nonce: {nonce}")
            return hash_try
    return -1

blockNum = 24
trans = "76123fcc2141"
previousHash = "2948de1509c908"

mine(blockNum, trans,previousHash)
