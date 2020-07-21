def encodeVigenere(text, key): #Both inputs should be in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	i=0
	while i<len(textList):
		letter = textList[i]
		shift = keyList[i%len(keyList)]
		textList[i] = letter+shift-1
		if(textList[i]>26):
			textList[i]-=26
		i+=1
	return numListToString(textList)

def decodeVigenere(text, key): #Again, both inputs in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	i=0
	while i<len(textList):
		letter = textList[i]
		shift = keyList[i%len(keyList)]
		textList[i] = letter-shift+1
		if(textList[i]<=0):
			textList[i]+=26
		i+=1
	return numListToString(textList)

def testEncodeDecode(text, key):
	encodedString = encodeVigenere(text, key)
	print("Encoded Vigenere Cipher: " + encodedString)
	decodedString = decodeVigenere(encodedString, key)
	print("Decoded Vigenere Cipher: " + decodedString)

def charToInt(character):
	num = ord(character)
	if 65 <= num <= 90:
		#capital letter
		return (num-64)
	elif 97 <= num <= 122:
		#lowercase letter
		return (num-96)
	else:
		return None

def stringToNumList(string):
	charList = list(string)
	numList = []
	for c in charList:
		if charToInt(c) is not None:
			numList.append(charToInt(c))
	return numList

def numListToString(nList):
	string = ""
	for n in nList:
		string+=str(chr(96+n))
	return string
