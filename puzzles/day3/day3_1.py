def getNbCollisions():
	f=open("input.txt")
	m=f.read().splitlines()
	
	x=0
	width = len(m[0])	
	nbCollisions = 0

	for y in range(len(m)):
		if(m[y][x] == '#'):
			nbCollisions+=1
		x = (x+3)%width
	
	return nbCollisions

nbCollisions = getNbCollisions()
print("nbCollisions : {}".format(nbCollisions))
