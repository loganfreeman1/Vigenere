import EncodeDecode
import Caesar
import Kasiski
def crackVigenere(message):
	messageNums = []
	messageModified = ''
	for c in message:
		n = ord(c)
		if 65<=n<=90:
			messageNums.append(n+32)
		elif 97<=n<=122:
			messageNums.append(n)
	for n in messageNums:
		messageModified+=str(chr(n))

	keyLength = Kasiski.kasiski(messageModified,3,15)[0]

	keyList = []
	key = ''
	for i in range(keyLength):
		mono = []
		k=i
		while k<len(messageNums):
			mono.append(messageNums[k])
			k+=keyLength
		keyList.append(Caesar.crackCaesar(mono))

	for q in keyList:
		key += str(chr(q+97))
	print(key)

	#return EncodeDecode.decodeVigenere(message, key)
