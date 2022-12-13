class Elf:
	def __init__(self, number, calories):
		self.number = number
		self.calories = calories

	def __str__(self):
		return 'elf: ' + str(self.number) + ' food: ' + str(self.calories)

	def __repr__(self):
		return 'elf: ' + str(self.number) + ' food: ' + str(self.calories)

f = open("C:\\Users\\Serm\\github.com\\advent-of-code-2022\\01_input.txt")
lines = f.read().split('\n')

top = [
	Elf(0, 0),
	Elf(0, 0),
	Elf(0, 0)
]

current_food = 0
current_elf = 0
for item in lines:
	#print('item: ' + item)
	if item == '':
		elf = Elf(current_elf, current_food)
		for t in range(3):
			if elf.calories > top[t].calories:
				replace = elf
				tmp_elf = None
				for i in range(t, 3):
					tmp_elf = top[i]
					top[i] = replace
					replace = tmp_elf
				break

		print(elf)
		current_food = 0
		current_elf += 1
	else:
		current_food += int(item)

print(top)
f.close()