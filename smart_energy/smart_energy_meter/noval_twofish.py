# Importing the necessary libraries
from twofish import Twofish

BLOCKSIZE = 16
secretKey = b'1234567890123456'

def encrypt_data(data):
    Type = type(data)
    if Type == bytes:
        pass
    elif Type == int:
        data = str(data)
        data = data.encode('utf-8')
    else:
        data = data.encode('utf-8')

    bytesRead = len(data)
    if bytesRead % BLOCKSIZE == 0:
        padLen = 0
    else:
        padLen = 16 - bytesRead % BLOCKSIZE
    data += bytes([padLen]) * padLen
    block_data = [data[i:i + BLOCKSIZE] for i in range(0, bytesRead, BLOCKSIZE)]
    data_out = bytes()
    for block in block_data:
        data_out += (Twofish(secretKey).encrypt(block))
    return data_out
