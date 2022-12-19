import os
from time import sleep

f = open("14_input.txt")
lines = f.read().split('\n')[0:-1]
f.close()

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y

sand = (500, 0)
left = 500
right = 500
top = 0
bottom = 0
wall = set()
for line in lines:
	rocks = line.split(' -> ')
	prev_coord = None
	for rock in rocks:
		pair = rock.split(',')
		coord = (int(pair[0]), int(pair[1]))
		if prev_coord is not None:
			if prev_coord[0] == coord[0]: #vertical
				if prev_coord[1] > coord[1]: #upward
					current_y = prev_coord[1]
					while current_y != coord[1]-1:
						wall.add((coord[0], current_y))
						current_y -= 1
				else:
					current_y = prev_coord[1]
					while current_y != coord[1]+1:
						wall.add((coord[0], current_y))
						current_y += 1 
			elif prev_coord[1] == coord[1]: #Horizontal
				if prev_coord[0] > coord[0]: #to left
					current_x = prev_coord[0]
					while current_x != coord[0]-1:
						wall.add((current_x, coord[1]))
						current_x -= 1
				else:
					current_x = prev_coord[0]
					while current_x != coord[0]+1:
						wall.add((current_x, coord[1]))
						current_x += 1
		prev_coord = coord
		
		if coord[0] < left:
			left = coord[0]
		if coord[0] > right:
			right = coord[0]
		if coord[1] > bottom:
			bottom = coord[1]

sand_count = 1
print(f'left{left} right{right} botom{bottom}')
filled = False
while not filled:
	travelled = Vector(0,0)
	while True:
		if (500, 0) in wall:
			filled = True
			break
		if sand[1]+travelled.y > bottom :
			#print(f'sand: {sand_count}, hit nothing after {sand[1]+travelled.y} and fall to the void')
			wall.add((sand[0]+travelled.x, sand[1]+travelled.y))
			break
		if (sand[0] + travelled.x, sand[1] + travelled.y + 1) in wall:
			#print(f'sand: {sand_count}, hit the wall at {sand[0]+travelled.x, sand[1]+travelled.y+1}', end='')
			#hit the wall slide left
			if (sand[0] + travelled.x - 1, sand[1] + travelled.y + 1) not in wall:
				travelled.x -= 1
				#print(f' and slide to the left as it has space')
				continue
			elif (sand[0] + travelled.x + 1, sand[1] + travelled.y + 1) not in wall:
				travelled.x += 1
				#print(f' and slide to the right as it has space')
				continue
			else:
				wall.add((sand[0]+travelled.x, sand[1]+travelled.y))
				#print(f' and stop at ({sand[0]+travelled.x}, {sand[1]+travelled.y})')
				if sand[0] + travelled.x < left:
					left = sand[0] + travelled.x
				if sand[0] + travelled.x > right:
					right = sand[0] + travelled.x
				break
		
		travelled.y += 1
	sand_count += 1

'''
	print('')
	os.system('cls')
	for j in range(0, bottom+3):
		for i in range(left-1, right+3):
			if (i,j) not in wall:
				print('.', end='')
			elif (i,j) == (sand[0]+travelled.x, sand[1]+travelled.y):
				print('o', end='')
			else:
				print(f'#', end='')
		print('')
		
	sleep(0.25)
	print('')
'''

print(f'after {sand_count-2} sand, it is in stable state')