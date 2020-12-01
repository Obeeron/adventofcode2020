def getFlag(inputPath):
	try:
		inputFile = open(inputPath, 'r')
	except:
		print("Can't open file "+inputPath)
		exit()
	lines = inputFile.readlines()
	nbLines = len(lines)
	for i in range(nbLines):
		a = int(lines[i])
		for j in range(i+1,nbLines):
			b = int(lines[j])
			for k in range(j+1,nbLines):
				c = int(lines[k])
				if(a+b+c == 2020):
					print("a={}".format(a))
					print("b={}".format(b))
					print("c={}".format(c))
					return a*b*c
	return -1

flag = getFlag("input.txt")
if(flag == -1):
	print("Flag not found")
else:
	print("flag:{}".format(flag))
