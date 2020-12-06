def isCommonAnswer(q, groupResponses):
	for response in groupResponses:
		if not(q in response):
			return False
	return True

def getFlag():
	f=open("input.txt")
	groups = [s.splitlines() for s in f.read().replace('\n\n',';').split(';')]
		
	totalSum = 0
	for group in groups:
		group.sort(key=len)
		for baseQ in group[0]:
			if isCommonAnswer(baseQ, group[1:]):
				totalSum+=1

	return totalSum

print("The flag is : {}".format(getFlag()))
