def getNbValidPassports():
	f = open("input.txt")
	lines = f.read().replace(' ','\n').replace("\n\n",';').split(';')
	passports = [line.splitlines() for line in lines]
	
	nbValid = 0
	for i in range(len(passports)):
		nbKeys = len([data[:3] for data in passports[i] if data[:3] != "cid"])
		if nbKeys >= 7:
			nbValid += 1
	return nbValid

print("Number of valid passports: "+str(getNbValidPassports()))
