import enchant
def dictCheck(string):
	d = enchant.Dict("en_US")
	return d.check(string)
