def encodeVigenere(text, key): #Both inputs should be in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	i=0
	j=0
	while i<len(textList):
		if(textList[i]<0):
			#Letter
			letter = -1*textList[i]
			shift = -1*keyList[j%len(keyList)]
			textList[i] = -1*((letter+shift-1)%26)
			j+=1
		i+=1
	return textList

def decodeVigenere(text, key): #Again, both inputs in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	i=0
	j=0
	while i<len(textList):
		if(textList[i]<0):
			#Letter
			letter = -1*textList[i]
			shift = -1*keyList[j%len(keyList)]
			textList[i] = (letter-shift+1)
			if(textList[i]<0):
				textList[i]+=26
			textList[i]*=-1
			j+=1
		i+=1
	return textList

def testEncodeDecode(text, key):
	encodedList = encodeVigenere(text, key)
	encodedString = numListToString(encodedList)
	print(encodedList)
	print("Encoded Vigenere Cipher: " + encodedString)
	decodedList = decodeVigenere(encodedString, key)
	decodedString = numListToString(decodedList)
	print(decodedList)
	print("Decoded Vigenere Cipher: " + decodedString)

def charToInt(character):
	num = ord(character)
	if 65 <= num <= 90:
		#capital letter
		return -1*(num-64)
	elif 97 <= num <= 122:
		#lowercase letter
		return -1*(num-96)
	else:
		return num

def stringToNumList(string):
	charList = list(string)
	numList = []
	for c in charList:
		numList.append(charToInt(c))
	return numList

def numListToString(nList):
	string = ""
	for n in nList:
		if n<0:
			string+=str(chr(96+n*-1))
		else:
			string+=str(chr(n))
	return string
