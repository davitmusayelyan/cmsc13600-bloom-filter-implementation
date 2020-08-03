'''bloom filter data structure implementation'''

import array
import binascii
import random
import string

class Bloom(object):
    '''Creates a bloom filter of size m with k
    independent hash functions.'''
	def __init__(self, m,k, seed=0):
		self.array = array.array('B', [0] * m)
		self.hashes = self.generate_hashes(m,k,seed)

    '''generate k independent hash functions each with range 0,...,m'''
	def generate_hashes(self, m, k, seed):
		MAXINT = 2**32-1
		NEXTPRIME = 4294967311
		hashes = []
		random.seed(seed)
		for i in range(0, k):
			A = random.randint(0, MAXINT)
			B = random.randint(0, MAXINT)
			f = lambda st, A=A, B=B: ((A * (binascii.crc32(bytes(str(st), 'utf-8')) & 0xffffffff) + B) % NEXTPRIME) % m
			hashes.append(f)
		return hashes

    '''Add a string to the bloom filter, returns void'''
	def put(self, item):
		for k in range(0, len(self.hashes)):
			i = self.hashes[k](item)
			self.array[i] = 1

    '''Test if the bloom filter either possibly contains the string (true (possibly)), or definitely doesn't (false (definitely)).'''
	def contains(self, item):
		for k in range(0, len(self.hashes)):
			i = self.hashes[k](item)
			if (self.array[i] == 0):
				return False
			else: return True
		#TODO
