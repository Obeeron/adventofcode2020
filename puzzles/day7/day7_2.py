import re

def getNbBags(colorDict, colorContainers, i):
	nbBags = 1
	for d in colorContainers[i]:
		if d != '':
			count, color = d.split(' ',1)
			idx = colorDict.get(color)
			nbBags += int(count) * getNbBags(colorDict, colorContainers, idx)
		
	return nbBags

def getFlag():
	f = open("input.txt")
	fStr = re.sub('no other| bags?\.','',f.read())
	lines = re.sub(' bags contain | bags?, ',',',fStr).splitlines()
	L = [l.split(',') for l in lines]
	
	nbColors = len(L)
	colorDict = dict()
	colorDict = dict((color,idx) for idx,color in enumerate([l[0] for l in L]))
	colorContainers = [l[1:] for l in L]
	flag = getNbBags(colorDict,colorContainers, colorDict.get('shiny gold'))-1
			
	f.close()
	return flag

print(f"flag : {getFlag()}")
