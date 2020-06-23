from twofish import Twofish
import binascii

#binascii.unhexlify()
key=input("Enter the secret key of 16 bytes size:\n")
secret_key=binascii.unhexlify(key)
message_key=Twofish(secret_key)

message=input("Enter the message to encrypt:/nNote: Shoulb be 16 bytes or multiple of 16.\n")
mesg=str.encode(message)

encrypt_message=message_key.encrypt(mesg)

decrypt_message=message_key.decrypt(encrypt_message).decode()

print("Encrypted message for your the text: ")
print(encrypt_message)
print("Decrypted message for your the text: ")
print(decrypt_message)
