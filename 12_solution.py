f = open("12_input.txt")
lines = f.read().split('\n')[0:-1]
f.close()

width = len(lines[0])
height = len(lines)
height_map = []
start = (0,0)
end = (0,0)
min_length = 500
test_count = 0
unsuccess_path = set()

for i in range(height):
	height_map.append([])
	for j in range(width):
		if lines[i][j] == 'S':
			start = (j,i)
			height_map[i].append(0)
		elif lines[i][j] == 'E':
			end = (j,i)
			height_map[i].append(27)
		else:
			height_map[i].append(ord(lines[i][j]) - 96)

past_location = [start[1]*width+start[0]]
end = (48,10)
direction = []

def test_walk(x, y, step):

	ten_left = True
	if len(direction) >= 10:
		for d in direction[-10]:
			if d != '<':
				ten_left = False

		if ten_left:
			return False

	rr = lr = ur = dr = False
	if x+1 < width and height_map[y][x+1] - height_map[y][x] == step and width*y+x+1 not in past_location: #walk right
		past_location.append(width*y+x+1)
		direction.append('>')
		rr = walk(x+1, y)
		past_location.pop()
		direction.pop()

	if y+1 < height and height_map[y+1][x] - height_map[y][x] == step and width*(y+1)+x not in past_location: #walk down
		past_location.append(width*(y+1)+x)
		direction.append('v')
		dr = walk(x, y+1)
		past_location.pop()
		direction.pop()

	if x-1 >= 0 and height_map[y][x-1] - height_map[y][x] == step and width*y+x-1 not in past_location and (x >= 108 and step >= 0 and height_map[y][x] > 3 or x >= 134 and height_map[y][x] == 3): #walk left
		past_location.append(width*y+x-1)
		direction.append('<')
		lr = walk(x-1, y)
		past_location.pop()
		direction.pop()

	if y-1 >= 0 and height_map[y-1][x] - height_map[y][x] == step and width*(y-1)+x not in past_location: #walk up
		past_location.append(width*(y-1)+x)
		direction.append('^')
		ur = walk(x, y-1)
		past_location.pop()
		direction.pop()

	return rr or dr or lr or ur

def walk(x, y):
	global test_count
	test_count += 1
	print(f'test walking this path {len(direction)} - {"".join(direction)} - altitude: {chr(height_map[y][x]+96)} - location: {x},{y}')
	#print(f'walk({x}, {y}, {min_length})')
	global min_length
	#too far
	if len(past_location) > min_length:
		print(f'exceed step limit {len(past_location)}')
		return False

	#found solution
	if x==48 and y==10: #height_map[y][x] == 27:
		print(f'found solution: {len(past_location)-1}')
		min_length = len(past_location)-1
		return True

	#can cross -- can visit this location from past location too
	for loc in past_location[0:-2]:
		past_x = loc%width
		past_y = int(loc/width)
		if past_x == x and abs(past_y - y) == 1 and height_map[y][x] - height_map[past_y][x] <= 1:
			#print(f'can cross to ({x},{y}) from {past_x},{past_y}')
			return False
		if past_y == y and abs(past_x - x) == 1 and height_map[y][x] - height_map[y][past_x] <= 1:
			#print(f'can cross to ({x},{y}) from {past_x},{past_y}')
			return False

	#print(f'x: {x}, y:{y}')
	#Climb
	p1 = test_walk(x,y,1)
	p0 = test_walk(x,y,0)
	pn = False
	if (height_map[y][x] == 15):
		pn = test_walk(x,y,-2)

	unsuccess_path.add(width*y+x)



print(f'width: {width}, height: {height}')
print(f'start: {start}, end: {end}')
for l in past_location:
	print(f'({l%width}, {int(l/width)})', end=' ')

walk(start[0], start[1])

print(f'shortest = {min_length}, tested: {test_count}')