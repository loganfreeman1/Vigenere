import csv
import EncodeDecode
#First, Kasiski for key-length identification
#Then, Caesar decryption for possible key lengths
#Dictionary checks on Caesar decryptions ---METRIC
#Cleanliness of frequency distribution on kasiski key-length ---METRIC
factorFrequency = { #Frequency of factors of differences, done from an analysis of 200,000 random letters
	2:0,
	3:0.083566881,
	4:0.0625754,
	5:0.05037445,
	6:0.041757921,
	7:0.035491564,
	8:0.03125522,
	9:0.027926001,
	10:0.024712782,
	11:0.02259229,
	12:0.020998441,
	13:0.019601793,
	14:0.017722582,
	15:0.016325934,
	16:0.01562993,
	17:0.014604484,
	18:0.013989681,
	19:0.013112716,
	20:0.012354071
}

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
			spaceList.append(instances[i+1]-instances[i])
	#Now, spaceList contains every space between instances of repeated substrings. Now, have to make frequency list of key lengths
	totalFactors=0
	for num in spaceList:
		for i in range(minSize, maxSize+1):
			if num%i==0:
				if i in frequencies:
					frequencies[i]+=1
					totalFactors+=1
				else:
					frequencies[i]=1
					totalFactors+=1

	#Now, do an irregularity analysis, to find the likely key length(s)
	differences = {}
	for i in range(minSize, maxSize+1):
		if i in frequencies:
			expected = (factorFrequency[i]*totalFactors)
			actual = (frequencies[i])
			differences[i]=actual-expected

	possibleKeyLengths = []
	sortedDict = sorted(differences, key=differences.get, reverse=True)[:3]
	return sortedDict

def csvDict(mydict):
	with open('dict.csv', 'w') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in mydict.items():
			writer.writerow([key, value])
	#Analyse kasiski for deviation from normal (random) to score probable key-length using R^2
	#Frequency-analyse most deviant kasiski shifts for normality R^2
	#TODO FUTURE: CHECK FOR INTELLIGIBLE ENGLISH to score
