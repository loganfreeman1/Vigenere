import enchant
def dictCheck(string):
	d = enchant.Dict("en_US")
	validWords = 0
	for i in range(len(string)):
		for j in range(i+2,min(i+16,len(string)+1)):
			subString = string[i:j]
			if(d.check(subString)):
				validWords+=1
	return validWords
