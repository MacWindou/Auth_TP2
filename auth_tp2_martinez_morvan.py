import random
import hashlib

def hash(pre_puzzle_key, n):
	i=0
	m = hashlib.md5()

	while i < 1000:

		m.update(bytearray(pre_puzzle_key))
		m.digest()
		i=i+1
	#if n > 1:
	#	print(m.digest(),n)
	#	hash(m.digest(), n-1)
	#else:
	#	return m.digest()

def generate_paires(n):
	paires=[]
	for i in range(0, n):
		pre_puzzle_key = random.getrandbits(128)
		secret_key = random.getrandbits(128)
		paires.append([pre_puzzle_key, secret_key])

	return paires

def generate_puzzle(list):
	puzzle_key = []
	pre_puzzle_key = [(pre_puzzle_key) for (pre_puzzle_key, secret_key) in list]
	secret_key = [(secret_key) for (pre_puzzle_key, secret_key) in list]

	for i in range(0, len(pre_puzzle_key)):
		print (i,"->",pre_puzzle_key[i])
		puzzle_key[i] = hash(pre_puzzle_key[i], 1000)


	print(pre_puzzle_key)
	print(secret_key)

def User_puzzle ():
	liste = [(pre_puzzle_key, secret_key) for (pre_puzzle_key, secret_key) in generate_paires(3)]
	generate_puzzle(liste)
	print (liste)

if __name__ == "__main__":
	User_puzzle()