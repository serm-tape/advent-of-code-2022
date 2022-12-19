import re 

f = open("15_input.txt")
lines = f.read().split('\n')[0:-1]
f.close()



class Sensor:
	def __init__(self, x, y, coverage):
		self.x = x
		self.y = y
		self.coverage = coverage

	def __repr__(self):
		return f'Sensors at ({self.x},{self.y}) coverage is {self.coverage} units'

	def covered_x(self, sy):
		signal = self.coverage - abs(sy - self.y)
		if (signal < 0):
			return (0,0)
		left_spread = max(self.x - signal, 0)
		right_spread = min(self.x + signal, 4000000)
		return (left_spread, right_spread)


beacons = []
sensors = []
for line in lines:
	m = re.findall("Sensor at x=(\-*\d+), y=(\-*\d+): closest beacon is at x=(\-*\d+), y=(\-*\d+)", line)
	sensors.append(Sensor(int(m[0][0]), int(m[0][1]), abs(int(m[0][2])-int(m[0][0])) + abs(int(m[0][1])-int(m[0][3]))))
	beacons.append((int(m[0][2]), int(m[0][3])))

covered = set()
for latitude in range(2600000,2700000):
	if latitude % 100000 == 0:
		print(latitude)
	distress = []
	for s in sensors:
		distress.append(s.covered_x(latitude))
	distress.sort()
	#print(distress)

	prev_candidate = None
	for d in distress:
		if prev_candidate is not None:
			if prev_candidate[1] < d[0]:
				print(f'vacancy range between {prev_candidate[1]} and {d[0]}, latitude = {latitude}')
				break
			if prev_candidate[1] < d[1]:
				prev_candidate = d
		else:
			prev_candidate = d




print(f'covered: {len(covered)}')
