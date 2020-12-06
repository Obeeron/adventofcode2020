def getMaxSeatID():
	f = open("input.txt")
	lines = f.read().splitlines()
	maxSeatId = 0
	
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
		seatId = minRow * 8 + minCol
		maxSeatId = max(maxSeatId,seatId)
	f.close()
	return maxSeatId

print("max seat ID : {}".format(getMaxSeatID()))
