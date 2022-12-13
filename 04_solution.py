f = open("C:\\Users\\Serm\\github.com\\advent-of-code-2022\\04_input.txt")
lines = f.read().split('\n')

class Assignment:
	def __init__(self, fromto):
		tmp = fromto.split('-')
		self.start = int(tmp[0])
		self.end = int(tmp[1])

overlap = 0
for line in lines:
	if line != '':
		ranges = line.split(',')
		a = []
		for r in ranges:
			a.append(Assignment(r))

		#if a[0].start <= a[1].start and a[0].end >= a[1].end or a[1].start <= a[0].start and a[1].end >= a[0].end:
		#	overlap += 1

		if a[0].start >= a[1].start and a[0].start <= a[1].end or a[0].end >= a[1].start and a[0].end <= a[1].end or a[0].start <= a[1].start and a[0].end >= a[1].end or a[1].start <= a[0].start and a[1].end >= a[0].end:
			overlap += 1

print(overlap)

f.close()
