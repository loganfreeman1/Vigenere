import EncodeDecode
import Caesar
import Kasiski
import DictionaryCheck
from itertools import permutations

def crackVigenere(message):
	messageNums = [] #Numerical characters, all lowercase
	messageModified = '' #String, all lowercase
	for c in message:
		n = ord(c)
		if 65<=n<=90:
			messageNums.append(n+32)
		elif 97<=n<=122:
			messageNums.append(n)
	for n in messageNums:
		messageModified+=str(chr(n))

	keyLength = Kasiski.kasiski(messageModified,3,15)[0] #Most likely key length based on Kasiski Analysis of ciphertext
	print('Guessed key length as: '+str(keyLength))

	frequencyAnalyses = []
	splitTexts = []
	permutationSet = []
	for i in range(keyLength):
		l=[]
		n=i
		while n<len(messageNums):
			l.append(messageNums[n])
			n+=keyLength
		splitTexts.append(l)
		frequencyAnalyses.append(Caesar.frequencyAnalysis(l))
		permutationSet.extend([0,1,2,3]) #Highest number defines how deep in frequency tree program will search.

	p = permutations(permutationSet, keyLength)
	perms = sorted(set(p))
	for perm in perms:
		key = ''
		for j in range(keyLength):
			print(perm[j])
			key+=str(chr((frequencyAnalyses[j])[perm[j]]+97))
		print(key)
		decodedString = str(EncodeDecode.decodeVigenere(messageModified, key))
		return
		if(DictionaryCheck.dictCheck(decodedString)>500000):
			return decodedString
		#print(l, end = ' ')

