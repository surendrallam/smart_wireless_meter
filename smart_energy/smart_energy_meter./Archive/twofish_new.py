from twofish import Twofish
import binascii

#binascii.unhexlify()
key=input("Enter the secret key of 16 bytes size:\n")
#secret_key=binascii.unhexlify(key)
message_key=Twofish(key)

message=input("\nEnter the message to encrypt:\nNote: Shoulb be 16 bytes or multiple of 16.\n")
mesg=str.encode(message)

encrypt_message=message_key.encrypt(mesg)

decrypt_message=message_key.decrypt(encrypt_message).decode()

print("\nEncrypted message for your the text: ")
print(encrypt_message)
print("\nDecrypted message for your the text: ")
print(decrypt_message)
