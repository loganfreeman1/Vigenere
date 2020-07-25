import DictionaryCheck
import random
import string
import numpy

def getRandomString(length):
	letterSet = string.ascii_lowercase
	return ''.join(random.choice(letterSet) for i in range(length))

def randomPercentageCheck(depth, maxSize):
	i = 0
	averageWords = []
	while i<depth:
		num = numpy.random.randint(2,maxSize)
		string = getRandomString(num)
		words = DictionaryCheck.dictCheck(string)
		print("string is: "+string+"and words are: " + str(words))
		averageWords.append(words/num)
		i+=1
	return sum(averageWords)/len(averageWords)
