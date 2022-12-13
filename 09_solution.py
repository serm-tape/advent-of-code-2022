f = open("09_input.txt")
lines = f.read().split('\n')[0:-1]

class Knot:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def in_range(self, knot, dist=1):
		return self.x - dist <= knot.x and self.x + dist >= knot.x and self.y - dist <= knot.y and self.y + dist >= knot.y

	def move(self, direction):
		if direction == 'U':
			self.y += 1
		elif direction == 'D':
			self.y -= 1
		elif direction == 'L':
			self.x -= 1
		elif direction == 'R':
			self.x += 1

	def follow(self, leader):
		#print(f'in range? {self.in_range(leader, 1)}')
		if not self.in_range(leader, 1):
			dist_x = self.x - leader.x
			if dist_x > 0:
				self.move('L')
			if dist_x < 0:
				self.move('R')

			dist_y = self.y - leader.y
			if dist_y > 0:
				self.move('D')
			if dist_y < 0:
				self.move('U')

	def pos_str(self):
		return f'{self.x},{self.y}'

class Cmd:
	def __init__(self, cmd_str):
		c = cmd_str.split(' ')
		self.direction = c[0]
		self.dist = int(c[1])

rope = []
for i in range(10):
	rope.append(Knot(0,0))

visited = set()

for line in lines:
	cmd = Cmd(line)
	for i in range(cmd.dist):
		rope[0].move(cmd.direction)
		for j in range(1, len(rope)):
			rope[j].follow(rope[j-1])

		visited.add(rope[9].pos_str())
		#print(f'move {cmd.direction}, head is at {head.pos_str()}, tail is at {tail.pos_str()}')

print(f'visitted: {len(visited)}')
f.close()
