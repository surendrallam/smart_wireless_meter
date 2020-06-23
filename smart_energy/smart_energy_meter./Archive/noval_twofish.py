from twofish_lib import Twofish

def twofish():
	secret_key=input("Enter the secret key:\n")
	byte_key=bytes(secret_key, 'utf-8')
	print(byte_key)
	encrypted_key = Twofish(byte_key)

	input_message=input("Enter your message in a pack of 16 bytes:\n")
	byte_message=bytes(input_message, 'utf-8')
	print(byte_message)
	encrypted_message = encrypted_key.encrypt(byte_message)

	print("Twofish Encrypted messages: \n")
	print(encrypted_message)

	decrypted_message=encrypted_key.decrypt(encrypted_message).decode()
	print("Two fish decrypted message: \n")
	print(decrypted_message)


def twofish_encode():
	secret_key=input("Enter the secret key:\n")
	byte_key=bytes(secret_key, 'utf-8')
	print(byte_key)
	encrypted_key = Twofish(byte_key)

	input_message=input("Enter your message in a pack of 16 bytes:\n")
	byte_message=bytes(input_message, 'utf-8')
	print(byte_message)
	encrypted_message = encrypted_key.encrypt(byte_message)
	print(encrypted_message)
	
	inp_message=encrypted_message.decode('utf-8')
	print(inp_message)
	encrypt_message=base64.b64encode(encrypted_message.encode('utf-32',errors = 'strict'))
	print(encrypt_message)

def diff():
	secret_key=input("Enter the secret key:\n")
	byte_key=bytes(secret_key, 'utf-8')
	print(byte_key)
	encrypted_key = Twofish(byte_key)

	input_message=input("\nEnter your message in a pack of 16 bytes:\n")
	byte_message=bytes(input_message, 'utf-8')
	print(byte_message)
	encrypted_message = encrypted_key.encrypt(byte_message)

	encrypt_message=input_message.encode('utf-16', 'strict')
	print("\nNormal encrypted message: ")
	print(encrypt_message)

	print("\nTwofish Encrypted messages: ")
	print(encrypted_message)

	decrypt_message=encrypt_message.decode('utf-16', 'strict')
	print("\nNormal decrypted message: ")
	print(decrypt_message)

	decrypted_message=encrypted_key.decrypt(encrypted_message).decode()
	print("\nTwo fish decrypted message: ")

	print(decrypted_message)	

def noval_twofish():
	secret_key=input("Enter the secret key:\n")
	byte_key=bytes(secret_key, 'utf-8')
	print(byte_key)
	encrypted_key = Twofish(byte_key)

	input_message=input("\nEnter your message in a pack of 16 bytes:\n")
	byte_message=bytes(input_message, 'utf-8')
	print(byte_message)
	twofish_encrypt = encrypted_key.encrypt(byte_message)

	noval_inp=str(twofish_encrypt)
	
	print("\nTwofish Encrypted messages: ")
	print(twofish_encrypt)

	noval_encrypt=noval_inp.encode('utf-16', 'strict')
	print("\nNoval twofish encrypted message: ")
	print(noval_encrypt)

	noval_decrypt=noval_encrypt.decode('utf-16', 'strict')
	#print("\nNormal decrypted message: ")
	#print(noval_decrypt)

	#twofish_inp=bytes(noval_decrypt, 'utf-16')

	#print(twofish_inp)

	decrypted_message=encrypted_key.decrypt(twofish_encrypt).decode()
	print("\nTwo fish decrypted message: ")

	print(decrypted_message)
	

#diff()
#twofish_encode()
noval_twofish()
