f = open("08_input.txt")
lines = f.read().split('\n')[0:-1]

forest = []
for i in range(len(lines)):
	#print(lines[i])
	forest.append([])
	for j in range(len(lines[i])):
		forest[i].append(int(lines[i][j]))

count = 0
max_score = 0
max_i = 0
max_j = 0
for i in range(99):
	for j in range(99):
		#print(f'considering at location {i},{j}')
		dist_left = 0
		dist_right = 0
		dist_top = 0
		dist_bottom = 0
		seen_direction = 0
		
		#left
		is_visible = True
		for k in range(j-1, -1, -1):
			#print(f'left -- forest[{i},{k}]: {forest[i][k]} vs forest[{i},{j}]: {forest[i][j]}')
			if forest[i][k] >= forest[i][j]:
				dist_left = j-k
				is_visible = False
				break
		if is_visible or j == 0:
			seen_direction += 1
			dist_left = j
			#print(f'visible from left: ({i},{j})')
		#right
		is_visible = True
		for k in range(j+1, len(forest[i])):
			#print(f'right -- forest[{i},{k}]: {forest[i][k]} vs forest[{i},{j}]: {forest[i][j]}')
			if forest[i][k] >= forest[i][j]:
				dist_right = k-j
				is_visible = False
				break
		if is_visible or j == len(forest[i])-1:
			seen_direction += 1
			dist_right = len(forest[i])-1-j
			#print(f'visible from right:({i},{j})')
		#top
		is_visible = True
		for k in range(i-1, -1, -1):
			#print(f'top -- forest[{k},{j}]: {forest[k][j]} vs forest[{i},{j}]: {forest[i][j]}')
			if forest[k][j] >= forest[i][j]:
				dist_top = i-k
				is_visible = False
				break
		if is_visible or i == 0:
			seen_direction += 1
			dist_top = i
			#print(f'visible from top:({i},{j})')
		#bottom
		is_visible = True
		for k in range(i+1, len(forest)):
			#print(f'bottom -- forest[{k},{j}]: {forest[k][j]} vs forest[{i},{j}]: {forest[i][j]}')
			if forest[k][j] >= forest[i][j]:
				dist_bottom = k-i
				is_visible = False
				break
		if is_visible or i == len(forest)-1:
			seen_direction += 1
			dist_bottom = len(forest[i])-1-i
			#print(f'visible from bottom: ({i},{j})')

		score = dist_left * dist_right * dist_top * dist_bottom
		#print(f'{i},{j} ({forest[i][j]}) -> {dist_left} * {dist_right} * {dist_top} * {dist_bottom} = {score}')
		if score > max_score:
			max_i = i
			max_j = j
			max_score = score

		if seen_direction >= 3:
			print(f'seeeen: {i},{j} = {seen_direction}')
			print(f'{i},{j} ({forest[i][j]}) -> {dist_left} * {dist_right} * {dist_top} * {dist_bottom} = {score}')

print(f'max_score: {max_score} ({max_i},{max_j})')
f.close()