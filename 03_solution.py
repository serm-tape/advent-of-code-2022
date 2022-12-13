f = open("C:\\Users\\Serm\\github.com\\advent-of-code-2022\\03_input.txt")
lines = f.read().split('\n')

def findOneDup(part1, part2, part3):
	for x in part1:
		for y in part2:
			for z in part3:
				if x==y and y==z:
					return x

def getPriority(item):
	if ord(item) < 97:
		return ord(item) - ord('A') + 27
	else:
		return ord(item) - ord('a') + 1

total = 0
parts = [None, None, None]
for i in range(len(lines)):
	if lines[i] != '':
		if i%3 == 2:
			parts[2] = lines[i]
			dup = findOneDup(parts[0], parts[1], parts[2])
			pri = getPriority(dup)
			total += pri
		else:
			parts[i%3] = lines[i]


print(total)
f.close()
