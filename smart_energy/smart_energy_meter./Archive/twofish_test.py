from twofish import Twofish
import binascii

#binascii.unhexlify()
secret_key=binascii.unhexlify('1234567890123456')
message_key=Twofish(secret_key)
message=input("abcdefghijklmnop")
mesg=binascii.unhexlify('message')
encrypt_message=message_key.encrypt(mesg)
decrypt_message=message_key.decrypt(encrypt_message.decode())
print("Encrypted message for your the text: "+encrypt_message)
print(decrypt_message)
