from twofish import Twofish
import time
start_time = time.time()

T = Twofish(b'secret')
x = T.encrypt(b'YELLOWSUBMARINES')
print("Secret key: ")
print(T)
print("Encrypted messages: ")
print(x)
print(T.decrypt(x).decode())

print("--- %s seconds ---" % (time.time() - start_time)

