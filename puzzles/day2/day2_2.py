def getNbCorrectPwd():
	f = open("input.txt")
	nbValid = 0
	for line in f.readlines():
		l = line.split(' ')
		position = [int(s) for s in l[0].split('-')]
		c = l[1][:-1]
		pos1, pos2 = position[0]-1, position[1]-1
		if((l[2][pos1] == c) ^ (l[2][pos2]==c)):
			nbValid += 1
	return nbValid	

print(getNbCorrectPwd())
