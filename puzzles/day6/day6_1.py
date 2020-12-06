def getFlag():
	f=open("input.txt")
	groups = [set(list(s)) for s in f.read().replace('\n\n',';').replace('\n','').split(';')]
	totalSum = sum([len(l) for l in groups])
	return totalSum

print("The flag is : {}".format(getFlag()))
