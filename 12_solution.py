
f = open("12_input.txt")
lines = f.read().split('\n')[0:-1]
f.close()

for test in range(40):
	width = len(lines[0])
	height = len(lines)
	height_map = []
	start = (0,test)
	end = (0,0)
	distances = []
	unvisitted = []

	for y in range(height):
		height_map.append([])
		distances.append([])
		for x in range(width):
			distances[y].append(500)
			if lines[y][x] == 'S':
				#start = (x,y)
				height_map[y].append(1)
				#distances[y][x] = 0
				#print(f'x:{x} y:{y} distances[i][j]: {distances[y][x]}')
			elif lines[y][x] == 'E':
				end = (x,y)
				height_map[y].append(27)
			else:
				height_map[y].append(ord(lines[y][x]) - 96)

	def find_dist(x, y):
		if (x,y) not in unvisitted:
			return 

		path = [(1,0), (0,1), (0,-1), (-1,0)]
		for p in path:
			nx = x + p[0]
			ny = y + p[1]
			#print(f'nx: {nx}, ny: {ny}')
			if nx >= 0 and nx < width and ny >= 0 and ny < height and height_map[ny][nx] - height_map[y][x] <= 1:
				nd = distances[y][x] + 1
				#print(f'nd: {nd}, distance[ny][nx]: {distances[ny][nx]}')
				if distances[ny][nx] is None or nd < distances[ny][nx]:
					distances[ny][nx] = nd
					unvisitted.append((nx, ny))
		unvisitted.remove((x,y))


	#print(f'widht: {width} height: {height} height_map: {len(height_map[0])} * {len(height_map)}')
	distances[start[1]][start[0]] = 0
	unvisitted.append((start[0], start[1]))
	while len(unvisitted) > 0:
		find_dist(unvisitted[0][0], unvisitted[0][1])


	print(f'distance from start to end = {distances[end[1]][end[0]]}')
