def isCorrectHgt(v):
	unit = v[-2:]

	if unit == "cm":
		return 150 <= int(v[:-2]) <= 193
	if unit == "in":
		return 59 <= int(v[:-2]) <= 76
	return False

def isCorrectHcl(v):
	if len(v) != 7 or v[0] != '#':
		return False

	for c in v[1:]:
		if not('0'<=c<='9' or 'a'<=c<='f'):
			return False
	return True 

def isCorrectPid(v):
	if len(v) == 9 and v.isnumeric():
		return True
	else:
		return False

def getNbValidPassports():
	f = open("input.txt")
	lines = f.read().replace(' ','\n').replace("\n\n",';').split(';')
	passports = [line.splitlines() for line in lines]
	
	eyeColors = ['amb','blu','brn','gry','grn','hzl','oth']
	nbValid = 0
	for i in range(len(passports)):
		dic = dict((k,v) for k,v in (data.split(':') for data in passports[i]) if k!="cid")
		if len(dic) == 7:
			if 1920 <= int(dic.get('byr')) <= 2002 and \
				2010 <= int(dic.get('iyr')) <= 2020 and \
				2010 <= int(dic.get('eyr')) <= 2030 and \
				2010 <= int(dic.get('eyr')) <= 2030 and \
				isCorrectHgt(dic.get('hgt')) and \
				isCorrectHcl(dic.get('hcl')) and \
				dic.get('ecl') in eyeColors and \
				isCorrectPid(dic.get('pid')) :
				nbValid+=1
	return nbValid

print("Number of valid passports: "+str(getNbValidPassports()))
