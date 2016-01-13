import random
import hashlib
from Crypto.Cipher import AES

#benjamin.arnaud.72@gmail.com

def hash(pre_puzzle_key, n):
	m = hashlib.md5(pre_puzzle_key).digest()

	for i in range(1, n):
		m = hashlib.md5(m).digest()

	return m

def generate_paires(n):
	paires=[]
	for i in range(0, n):
		pre_puzzle_key = bytearray(str(random.getrandbits(128)), "ascii")
		print(type(pre_puzzle_key))
		secret_key = bytearray(str(random.getrandbits(128)), "ascii")
		paires.append([pre_puzzle_key, secret_key])

	return paires

def generate_puzzle(list):
	puzzle_key = []
	secret_key= []
	pre_puzzle_key = [(pre_puzzle_key) for (pre_puzzle_key, secret_key) in list]
	secret_key = [(secret_key) for (pre_puzzle_key, secret_key) in list]
	print("secret key generate puzzle ")
	print(secret_key)

	for i in range(0, len(pre_puzzle_key)):
		print (i,"->",pre_puzzle_key[i])
		puzzle_key.insert(i, hash(pre_puzzle_key[i], 1000))



	print("puzzle key :")
	print(puzzle_key)
	print("secret key : ")
	print(secret_key)

	message = []
	for i in range(0, len(list)):
		secret_key[i].append(i)
		message.append(secret_key[i])
		print("message : ")
		print(message)

	obj = AES.new(secret_key[i], AES.MODE_CBC)
	ciphertext = obj.encrypt(message)

def User_puzzle ():
	liste = [(pre_puzzle_key, secret_key) for (pre_puzzle_key, secret_key) in generate_paires(3)]
	generate_puzzle(liste)
	print (liste)

if __name__ == "__main__":
	User_puzzle()