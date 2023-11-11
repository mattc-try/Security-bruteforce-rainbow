# This code requires a python version higher or equal to 3.6 
# If your version is older than that (how old is your install???), please consider upgrading :)

import hashlib

from string import ascii_letters
from time import time
from typing import Union


# The alphabet on which we will work
S = ascii_letters

def md5(message: str) -> str:
	"""
	Takes a string and return its md5 hash

	:param message: the message to be hashed
	:return: the md5 of the message
	"""
	return hashlib.md5(message.encode()).hexdigest()


assert(md5('test') == '098f6bcd4621d373cade4e832627b4f6')


#######################################################
# DO NOT MODIFY THE CODE ABOVE THIS                   #
# ONLY MODIFY THE CONTENT OF THE FUNCTIONS BELOW THIS #
#######################################################

##########
# Part 1 #
##########

def hashes_per_second() -> float:
	"""
	Compute how many hashes per second you can do on your computer.
	"""

	## Average version: 
	# 	hashes = []
	# for _ in range(20):
	# 	hashes_per_second = 0
	# 	t = time()
	# 	hashes_per_second = 0
	# 	while time() - t < 1:
	# 		md5(S)  
	# 		hashes_per_second +=1
	# 	hashes.append(hashes_per_second)
	# hashes_avg = sum(hashes) /  len(hashes)
	# print(f'avg for 20 iterations is {hashes_avg} ')
	# return hashes_avg

	## One time version
	t = time()
	hashes_per_second = 0
	while time() - t < 1:
		md5(S) # Hash a string from ASCII letters
		hashes_per_second +=1
	
	print(f'complicated stuff has taken {time() - t} seconds to execute')

	print(f'this many {hashes_per_second} ')
	return hashes_per_second

# hashes_per_second()

##########
# Part 2 #
##########

def convert_to_base(n: int, b: int) -> int:
	""" 
	Given a positive number n, convert it to base b.
	Result must be given in the form of a list, with the 
	most significant bit at the beginning.

	For instance, 101 in base 7 is 203 because 101 = 2 * 7^2 + 0 * 7^1 + 3 * 7^0
	So convert_to_base(101, 7) must return [2, 0, 3]

	:param int n: the number to be converted
	:param int b: the base to which the number should be converted 
	:return: the list representation of n in base b, with the most significant bit first
	"""

	# base case
	if n == 0:
		return[0]
	
	n_inbase_b = []
	while n > 0:
		n_inbase_b.insert(0, n%b)
		n //= b
	return n_inbase_b

## 101 in base 7 is 203 because 101 = 2 * 7^2 + 0 * 7^1 + 3 * 7^0
## uncomment the next line to check if your code is working on that example
assert(convert_to_base(101, 7) == [2, 0, 3])
print(convert_to_base(10000000, 52))




def generate_from_indexes(n_repr: list) -> str:
	"""
	From an integer representation in base S, return a string such that
	the i-th element of n_repr is the index in S of the i-th letter of the returned string.

	:param list n_repr: a representation in base S of an integer
	:return: a string with letters in S
	"""
	return "".join(S[i] for i in n_repr)


## We have S = ascii_letters (see line 12), hence
## S[:7] = 'abcdefg' so generate_from_indexes([2, 0, 3]) must return 
## S[2] + S[0] + S[3] = 'c' + 'a' + 'd' = 'cad' 
# print(generate_from_indexes([2, 0, 3]))

def generator(h: str) -> str:
	"""
	From a hash, generate a 5-letters passwords with letters from S

	:param str h: a MD5 hash
	:return: a 5-letter password with characters from S
	"""
	to_hash = '0' + h
	generated_value = md5(to_hash)
	value_in_base_S = convert_to_base(int(generated_value, 16), len(S))
	return generate_from_indexes(value_in_base_S)[:5]


assert(generator('098f6bcd4621d373cade4e832627b4f6') == 'fVNYG')
# print(generator(md5("unilu")))



def hash_chain(length: int, start: str) -> list:
	"""
	Create a hash chain of given length, with a given starting password.
	The hash chain of length n is of the form 
	[p0, h0, p1, h1, p2, h2, ..., pn, hn] where :
		* p0 = start
		* all the hashes are obtained from the password using md5: h0 = md5(p0), h1 = md5(p1), etc
		* all the passwords (except p0) are obtained from the previous hash: p1 = generator(h0), p2 = generator(h1), etc.

	:param int length: 	the length of the hash chain
	:param str start: 	the initial password of the chain
	"""
	hash_chain = [start]
	for i in range(length):
		pswd = hash_chain[-1] # last value in the array is the password for each iteration as we append both an hash and pass for each new one
		hash_chain.append(md5(pswd))
		if i < length - 1: 
			hash_chain.append(generator(md5(pswd))) # for the last iteration we don't need a new password for the next one.
		
	return hash_chain

## Let's build a hash chain starting with the password 'abcde'
## md5('abcde') == 'ab56b4d92b40713acc5af89985d4b786')
## generator('ab56b4d92b40713acc5af89985d4b786' == 'eYqUy')
## md5('eYqUy') == '1ad1f633175ed31d03aeeba82d2c784b')
## generator('1ad1f633175ed31d03aeeba82d2c784b' == 'dCEmM')
## etc
assert(hash_chain(5, 'abcde') == ['abcde', 'ab56b4d92b40713acc5af89985d4b786', 'eYqUy', '1ad1f633175ed31d03aeeba82d2c784b', 'dCEmM', 'bb50a1bb72b82cd189da6b260da6582f', 'dbHcC', 'b3b77f636f3676271b00fd668e708e91', 'dXpmV', '4956bc5e889556e5c6b662fc3b89501f'])
# print(hash_chain(3, "unilu"))


## Question 2.3
# print(hash_chain(5, 'DrWIW'))
# print(hash_chain(5, 'cVVWr'))


##########
# Part 3 #
##########


def generator_i(position: int, h: str) -> str:
	"""
	From a hash, generate a 5-letters password with letters from S
	The password will depend from the position value

	:param h: 			a MD5 hash
	:param position: 	a position (in the hash chain)
	"""
	to_hash = str(position) + h
	generated_value = md5(to_hash)
	value_in_base_S = convert_to_base(int(generated_value, 16), len(S))
	# print(generate_from_indexes(value_in_base_S)[:5])
	with open("generated_passwords.txt", 'a') as file:
		file.write(generate_from_indexes(value_in_base_S)[:5] + '\n')
	return generate_from_indexes(value_in_base_S)[:5]


assert(generator_i(3, '5d41402abc4b2a76b9719d911017c592') == 'PPmrg')
assert(generator_i(4, '5d41402abc4b2a76b9719d911017c592') == 'dEHZm')



def rainbow_chain(length: int, start: str) -> list:
	"""
	Create a rainbow chain of given length, with a given starting password.
	The hash chain of length n is of the form 
	[p0, h0, p1, h1, p2, h2, ..., pn, hn] where :
		* p0 = start
		* all the hashes are obtained from the password using md5: h0 = md5(p0), h1 = md5(p1), etc
		* all the passwords (except p0) are obtained from the previous hash: p1 = generator_i(0, h0), p2 = generator_i(1, h1), etc.

	:param int length: 	the length of the hash chain
	:param str start: 	the initial password of the chain
	:return: 			a rainbow string starting with start, of length length
	"""
	rainbow_chain = [start]
	for i in range(length):
		pswd = rainbow_chain[-1]
		
		rainbow_chain.append(md5(pswd))

		if i < length - 1:
			next_pswd = generator_i(i, md5(pswd))
			rainbow_chain.append(next_pswd)
		
	return rainbow_chain

## Let's build a rainbow chain starting with the password 'abcde'
## md5('abcde') == 'ab56b4d92b40713acc5af89985d4b786')
## generator_i(0, 'ab56b4d92b40713acc5af89985d4b786' == 'eYqUy')
## md5('eYqUy') == '1ad1f633175ed31d03aeeba82d2c784b')
## generator_i(1, '1ad1f633175ed31d03aeeba82d2c784b' == 'bTaKw')
## etc
assert(rainbow_chain(5, 'abcde') == ['abcde', 'ab56b4d92b40713acc5af89985d4b786', 'eYqUy', '1ad1f633175ed31d03aeeba82d2c784b', 'bTaKw', 'e0734129cb0d16d2cd3352f1b96c0bef', 'ciPLW', '5b46c61c5c632d2ccb45c417e7f2482a', 'cAdtl', 'effba8d1a2978d2908309be41e75ca77'])
print("\n\n Experiment \n")
rainbow_chain(10000000, "unilu")


## Question 3.2
# print(rainbow_chain(5, 'DrWIW'))
# print(rainbow_chain(5, 'cVVWr'))

## Question 3.4.a)

def retrieve(first_password, hash_of_pass):
	chain = rainbow_chain(10, first_password) # reconstitute the chain

	if chain[-1] == hash_of_pass: # base case
		return chain[-2]  # first password

    # Go back to find the password
	for i in range(10 - 2, -1, -1):
		next_hash = md5(chain[i * 2 + 1])
		if next_hash == hash_of_pass:
			return chain[i * 2]  # Return the corresponding password
	return "Password not found"

# print("Retrieved Password:", retrieve('unilu', '523ffd2979b4067a80de673dfc270b70'))


## Question 3.4.b
# How do you retrieve the password of '523ffd2979b4067a80de673dfc270b70' from the rainbow chain ('unilu', '523ffd2979b4067a80de673dfc270b70') of size 10? 
# Show your code here or in the report.	



def is_at_position(chain: tuple, chain_length: int, test_hash: str, position: int) -> bool:
	"""
	This function returns True if a hash is at a given position in a rainbow chain of a given length, and false otherwise

	For instance, on the chain rainbow_chain(5, 'abcde') that we receive as chain = ('abcde', 'effba8d1a2978d2908309be41e75ca77'),
	we have is_at_position(chain, 5, 'effba8d1a2978d2908309be41e75ca77', 4) == True but
	is_at_position(chain, 5, 'effba8d1a2978d2908309be41e75ca77', 3) == False
	
	:param tuple chain: 		a rainbow chain, stored in compact form: (first_password, last_hash)
	:param int chain_lenght: 	the length of the rainbow chain
	:param str test_hash: 		the hash we are testing
	:param int position:		the position we are testing

	:return: True if the hash is at the given position of the given hash chain, False otherwise 

	"""
	(first_password, last_hash) = chain

	current_pswd= first_password
	if position == chain_length-1 and last_hash == test_hash:
		return True
	elif position == chain_length-1:
		return False
	
	for i in range(chain_length):
		current_hash = md5(current_pswd)
        
		if i == position:
			if current_hash == test_hash:
				return True
			else:
				return False
			
		next_pswd = generator_i(i, current_hash)
		current_pswd = next_pswd

chain = ('abcde', 'effba8d1a2978d2908309be41e75ca77')  # chain of length 5
assert(is_at_position(chain, 5, 'effba8d1a2978d2908309be41e75ca77', 4) == True)
# print(is_at_position(chain, 5, 'effba8d1a2978d2908309be41e75ca77', 4))
assert(is_at_position(chain, 5, 'effba8d1a2978d2908309be41e75ca77', 3) == False)


def find_position_of_hash(chain: tuple, chain_length: int, test_hash: str) -> Union[None, int]:
	"""
	Given a rainbow chain, its length and a hash, return None if the hash is not in the chain,
	and its index if the hash is in the chain.

	:param tuple chain: 		the rainbow chain we are operating on
	:param int chain_length: 	the rainbow chain length
	:param str hash:			the hash we are looking for

	:return: either the index of the hash in the rainbow chain, or None

	"""
	(first_password, last_hash) = chain
	current_pswd = first_password
	if last_hash == test_hash:
		return chain_length - 1 # Here what you cant us to return is the index of the hash tuple or a chain with only hash, this as been concluded from the given assert() other wise here it woudld be 2*chain_length -1
	
	for i in range(chain_length):
		current_hash = md5(current_pswd)
        
		if current_hash == test_hash:
			return i # same here as above would be 2 times but seems like we want to know which hash it is in the list of hashes or with tupples.
		
		next_pswd = generator_i(i, current_hash)
		current_pswd = next_pswd

	return None

chain = ('abcde', 'effba8d1a2978d2908309be41e75ca77')  # chain of length 5
assert(find_position_of_hash(chain, 5, 'e0734129cb0d16d2cd3352f1b96c0bef') == 2)
assert(find_position_of_hash(chain, 5, '5d41402abc4b2a76b9719d911017c592') == None)


def find_password_of_hash(chain: tuple, chain_length: int, test_hash: str) -> Union[None, str]:
	"""
	From a chain of given length, if a given hash belong to that chain, return the related password.
	Otherwise, return None.

	:param tuple chain:			the rainbow chain we are operating on
	:param int chain_length: 	the length of the rainbow chain
	:param test_hash: 			the hash we are looking for

	:return: either the password that hashes to test_hash, or None
	"""
	(first_password, last_hash) = chain

	
	if last_hash == test_hash:
		c = rainbow_chain(5, first_password)
		print("u")
		return c[chain_length*2-2]


	for i in range(chain_length-1):  # i here is the position the last is treated above
		if md5(first_password) == test_hash: # current hash == tested hash
			return first_password

		first_password = generator_i(i, md5(first_password)) # next password
	return None

chain = ('abcde', 'effba8d1a2978d2908309be41e75ca77')  # chain of length 5
assert(find_password_of_hash(chain, 5, '1ad1f633175ed31d03aeeba82d2c784b') == 'eYqUy')
assert(find_password_of_hash(chain, 5, '5d41402abc4b2a76b9719d911017c592') == None)
