import Vigenere
#First, Kasiski for key-length identification
#Then, Caesar decryption for possible key lengths
#Dictionary checks on Caesar decryptions ---METRIC
#Cleanliness of frequency distribution on kasiski key-length ---METRIC
def kasiski(string,minSize=3, maxSize=6):
	#Takes string, returns structure containing frequency list for potential key lengths.
	#NOTE: minSize is the minimum Key size to be considered, maxSize is the maximum key size to be considered.
	#A 2-length key is rarely used, and the longer the key is the harder it is to break the cipher
	alreadyChecked = []
	spaceList = []
	frequencies = {}
	for i in range(0,len(string)+1):
		for j in range(minSize,maxSize+1):
			if(len(string[i:])-j>3): #All substrings of string between minSize and maxSize
				subString = string[i:j+i]
				if(string.count(subString)>1):
					try:
						alreadyChecked.index(subString)
					except:
						alreadyChecked.append(subString)
	#Now, alreadyChecked contains 1 instance of every substring that has more than 1 instance
	for subString in alreadyChecked:
		instances = []
		lastIndex = 0
		while True:
			foundIndex = string.find(subString, lastIndex)
			if foundIndex>-1:
				instances.append(foundIndex)
				lastIndex = foundIndex+len(subString)
			else:
				break
		for i in range(len(instances)-1):
			print(subString)
			spaceList.append(instances[i+1]-instances[i])
	#Now, spaceList contains every space between instances of repeated substrings. Now, have to make frequency list of key lengths
	for num in spaceList:
		for i in range(minSize, maxSize+1):
			if num%i==0:
				if i in frequencies:
					frequencies[i]+=1
				else:
					frequencies[i]=1
	print(frequencies)
