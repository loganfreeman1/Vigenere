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

	try:
		keyLength = Kasiski.kasiski(messageModified,3,15)[0] #Most likely key length based on Kasiski Analysis of ciphertext
	except IndexError:
		print('Kasiski Analysis failed. Message might be too short, or key might be too short or too long')
		return None

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
			key+=str(chr((frequencyAnalyses[j])[perm[j]]+97))
		decodedString = str(EncodeDecode.decodeVigenere(messageModified, key))
		validWords = DictionaryCheck.dictCheck(decodedString)
		print('Guessed key as: ' + key+ '. There are ' + str(validWords) +' valid words as a part of the decoded message')
		if(DictionaryCheck.dictCheck(decodedString)>0.28*len(decodedString)): #0.28, approximately
			print('Number of valid words is greater than 0.28*message length. This key is likely correct!')
			return decodedString

