def getNbCollisions(xslope, yslope):
	f=open("input.txt")
	m=f.read().splitlines()
	
	x=0
	width = len(m[0])	
	nbCollisions = 0

	for y in range(0,len(m),yslope):
		if(m[y][x] == '#'):
			nbCollisions+=1
		x = (x+xslope)%width
	
	print("slope x:{} y:{} has yielded {} collisions".format(xslope,yslope,nbCollisions))
	return nbCollisions

slope1 = getNbCollisions(1,1)
slope2 = getNbCollisions(3,1)
slope3 = getNbCollisions(5,1)
slope4 = getNbCollisions(7,1)
slope5 = getNbCollisions(1,2)
product = slope1*slope2*slope3*slope4*slope5
print("product : {}".format(product))
