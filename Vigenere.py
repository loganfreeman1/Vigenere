def encodeVigenere(text, key): #Both inputs should be in string form
	textList = stringToNumList(text)
	keyList = stringToNumList(key)
	for i in range(0, len(textList)):
		textList[i] = (textList[i]+keyList[i%len(keyList)])%26 - 1
	return textList

def charToInt(character):
	num = ord(character)
	if 65 <= num <= 90:
		#capital letter
		return num-64
	elif 97 <= num <= 122:
		#lowercase letter
		return num-96
	else:
		print("not a valid character")
		return None

def stringToNumList(string):
	charList = list(string)
	numList = []
	for c in charList:
		numList.append(charToInt(c))
	return numList
