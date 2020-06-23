from Crypto.Cipher import DES3
from Crypto import Random
import time
key = input("Enter 16 char secret key: \n")
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = input("Enter your message in multiples of 8 char: \n") #padded with spaces so than len(plaintext) is multiple of 8
start_time = time.time()
encrypted_text = cipher_encrypt.encrypt(plaintext)

cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
decrypt_message=cipher_decrypt.decrypt(encrypted_text)
#decrypt_message=cipher_decrypt.decrypt(encrypted_text) #you cant do it twice
print("encrypted_text: ",encrypted_text)
print("decrypt_message: ",plaintext)
time.sleep(0.0002)
print("Time taken: %s seconds" % (time.time() - start_time))

Time=str(time.time() - start_time)
Tim=['3DES', ",", Time,"\n"]
file = open("plot.txt","a")#append mode 
file.writelines(Tim) 
file.close() 