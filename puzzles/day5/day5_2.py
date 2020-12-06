def getMaxSeatID():
	f = open("input.txt")
	lines = f.read().splitlines()
	maxSeatId = 0
	
	idList = []
	for line in lines:
		minRow = 0
		maxRow = 127
		for c in line[:7]:
			m = (minRow+maxRow)//2
			if(c == 'F'):
				maxRow = m
			else:
				minRow = m+1
		minCol = 0
		maxCol = 7
		for c in line[7:]:
			m = (minCol+maxCol)//2
			if(c == 'L'):
				maxCol = m
			else:
				minCol = m+1
		if(minRow != 0 and minRow != 127):
			seatId = minRow * 8 + minCol
			idList.append(seatId)
	
	idList.sort()
	for i in range(len(idList)-1):
		if idList[i]+1 != idList[i+1]:
				f.close()
				return idList[i]+1
	f.close()
	return -1

print("missing seatID : {}".format(getMaxSeatID()))
