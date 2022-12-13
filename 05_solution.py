f = open("C:\\Users\\Serm\\github.com\\advent-of-code-2022\\05_input.txt")
lines = f.read().split('\n')

stack_pos = [1,5,9,13,17,21,25,29,33]
def move(count, stack1, stack2):
	pos = len(stack2)
	for i in range(count):
		current = stack1.pop()
		stack2.insert(pos, current)

def move1(count, stack1, stack2):
	for i in range(count):
		current = stack1.pop()
		stack2.append(current)


stacks = [[],[],[],[],[],[],[],[],[]]
for line in lines[7::-1]:
	print(line)
	for j in range(len(stack_pos)):
		if line[stack_pos[j]] != ' ':
			stacks[j].append(line[stack_pos[j]])

print(stacks)

for line in lines[10::]:
	if line != '':
		cmd = line.split(' ')
		move(int(cmd[1]), stacks[int(cmd[3])-1], stacks[int(cmd[5])-1])

for s in stacks:
	print(s[-1])

f.close()

