def encodeVigenere(text, key, keyPlace=0): #Both inputs should be in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	i=0
	while i<len(textList):
		letter = textList[i]
		shift = keyList[keyPlace%len(keyList)]
		textList[i] = letter+shift-1
		if(textList[i]>26):
			textList[i]-=26
		i+=1
		keyPlace+=1
	return numListToString(textList),keyPlace

def decodeVigenere(text, key, keyPlace=0): #Again, both inputs in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	i=0
	while i<len(textList):
		letter = textList[i]
		shift = keyList[keyPlace%len(keyList)]
		textList[i] = letter-shift+1
		if(textList[i]<=0):
			textList[i]+=26
		i+=1
		keyPlace+=1
	return numListToString(textList), keyPlace

def encodeVigenereFromFile(fileName, key):
	file = open(fileName, 'r')
	writeFile = open("Encoded_"+fileName, 'w+')
	contents = file.read().splitlines()
	keyPlace = 0
	allString = ''
	for string in contents:
		encodedString, keyPlace = encodeVigenere(string, key, keyPlace)
		writeFile.write(encodedString+'\n')
		allString+=encodedString
	file.close()
	writeFile.close()
	return allString

def decodeVigenereFromFile(fileName, key):
	file = open(fileName, 'r')
	writeFile = open("Decoded_"+fileName, 'w+')
	contents = file.read().splitlines()
	keyPlace=0
	for string in contents:
		decodedString, keyPlace = decodeVigenere(string, key, keyPlace)
		writeFile.write(decodedString + '\n')
	file.close()
	writeFile.close()

def testEncodeDecode(text, key):
	encodedString = encodeVigenere(text, key)[0]
	print("Encoded Vigenere Cipher: " + encodedString)
	decodedString = decodeVigenere(encodedString, key)[0]
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
