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
		for j in range(i,nbLines):
			b = int(lines[j])
			if(a+b == 2020):
				print("a={}".format(a))
				print("b={}".format(b))
				return a*b
	return -1

flag = getFlag("input.txt")
if(flag == -1):
	print("Flag not found")
else:
	print("flag:{}".format(flag))
