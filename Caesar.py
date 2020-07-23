#Solves Caesar cipher
def crackCaesar(charList): #Takes charList, all lower-case characters
	shiftSuccess={}
	for i in range(26):
		message = []
		letterFrequencies = {}
		netDeviation = 0
		for c in charList: #Does shift
			num = c+i
			if num>122:
				num-=26
			message.append(num)
		for c in message:
			if c in letterFrequencies:
				letterFrequencies[c]+=1
			else:
				letterFrequencies[c]=1

		for l in letterFrequencies:
			letterFrequencies[l]=letterFrequencies[l]/len(message)

		for l in letterFrequencies:
			deviation = abs(letterFrequencies[l]-alphabetFrequency[l])
			netDeviation += deviation

		shiftSuccess[i] = netDeviation

	shiftSuccess = sorted(shiftSuccess, key=shiftSuccess.get, reverse=False)
	crackedMessage = []
	for c in charList:
		char = c-shiftSuccess[0]
		if char<97:
			char+=26
		crackedMessage.append(char)
	return crackedMessage


alphabetFrequency = {
	97:0.08167,
	98:0.01492,
	99:0.02782,
	100:0.04253,
	101:0.12702,
	102:0.02228,
	103:0.02015,
	104:0.06094,
	105:0.06966,
	106:0.00153,
	107:0.00772,
	108:0.04025,
	109:0.02406,
	110:0.06749,
	111:0.07507,
	112:0.01929,
	113:0.00095,
	114:0.05987,
	115:0.06327,
	116:0.09056,
	117:0.02758,
	118:0.00978,
	119:0.02360,
	120:0.00150,
	121:0.01974,
	122:0.00074
}
