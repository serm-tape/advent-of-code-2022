f = open("10_input.txt")
lines = f.read().split('\n')[0:-1]

def render(cycle, x):
	#print(f'during wave {cycle} finished, strength = {strength}')
	if cycle%40 >= strength and cycle%40 < strength + 3:
		print('#', end='')
	else:
		print('.', end='')

waves = list(range(0, 300, 40))
print(waves)
strength = 1
total_strength = 0
cycle = 0
clock_wait = 2
for line in lines:
	if 'addx' in line:
		v = int(line.split(' ')[1])
		for wait in range(clock_wait):
			cycle += 1
			render(cycle, strength)
			if cycle in waves:
				#print(f'during wave {cycle} finished, strength = {strength}')
				#total_strength += strength * cycle
				print('')
		strength += v
	else:
		cycle += 1
		render(cycle, strength)
		if cycle in waves:
			#print(f'during wave {cycle} finished, strength = {strength}')
			#total_strength += strength * cycle
			print('')

	#print(f'after wave {cycle} finished, strength = {strength}')

print(f'total strength = {total_strength}')

'''
waves = list(range(1,21))
cycle_to_take = 2
playbook = []
for w in waves:
	playbook.append((w, 0))


for cycle in range(len(lines)):
	print(lines[cycle])
	if 'addx' in lines[cycle]:
		v = int(lines[cycle].split(' ')[1])
		inserted = False
		effected_cycle = cycle + 1 + cycle_to_take
		for i in range(len(playbook)):
			if playbook[i][0] == effected_cycle:
				playbook[i] = (playbook[i][0], playbook[i][1] + v)
				inserted = True
				break
			if playbook[i][0] > effected_cycle:
				playbook.insert(i, (effected_cycle, v))
				inserted = True
				break
		if not inserted:
			playbook.append((effected_cycle, v))

print(playbook)

strength = 1 
total_strength = 0
for event in playbook:
	strength += event[1]
	if event[0] in waves:
		print(f'strength @ {event[0]} is {strength}')
		total_strength += event[0] * strength
'''


f.close()

