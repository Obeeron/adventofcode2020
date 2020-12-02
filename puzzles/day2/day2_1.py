def getNbCorrectPwd():
	f = open("input.txt")
	nbValid = 0
	for line in f.readlines():
		l = line.split(' ')
		intervals = [int(s) for s in l[0].split('-')]
		c = l[1][:-1]
		nbOcc = l[2].count(c)
		if(nbOcc>=intervals[0] and nbOcc<=intervals[1]):
			nbValid += 1
	return nbValid	

print(getNbCorrectPwd())
