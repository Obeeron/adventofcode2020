import re

def isShinyGoldHolder(colorDict, colorContainers, M, i):
	if 'shiny gold' in colorContainers[i]:
		return True
	
	for color in colorContainers[i]:
		colorIdx = colorDict.get(color)
		if M[colorIdx]: 
			return True
		if M[colorIdx] == None and isShinyGoldHolder(colorDict,colorContainers,M,colorIdx):
			M[colorIdx] = True
			return True
		else:
			M[colorIdx] = False 
		
	return False

def getFlag():
	f = open("input.txt")
	lines = re.sub(' contain| no other| bags?[.,]?','',f.read()).splitlines()
	L = [re.split(' [0-9]+ ',l) for l in lines]
	
	nbColors = len(L)
	colorDict = dict()
	colorDict = dict((color,idx) for idx,color in enumerate([l[0] for l in L]))
	colorContainers = [l[1:] for l in L]
	M = [None]*nbColors

	flag = 0
	for i in range(nbColors):
		if isShinyGoldHolder(colorDict,colorContainers,M,i):
			flag += 1
			
	f.close()
	return flag

print(f"flag : {getFlag()}")
