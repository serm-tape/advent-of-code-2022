#f = open("11_input.txt")
#lines = f.read().split('\n')[0:-1]
#f.close()

class Item:
	def __init__(self, worry_level):
		self.worry_level = worry_level

	def __repr__(self):
		return str(self.worry_level)

class Test:
	def __init__(self, div_by, success, fail):
		self.div_by = div_by
		self.success = success
		self.fail = fail

	def run(self, worry_level):
		if worry_level % self.div_by == 0:
			return self.success
		else:
			return self.fail

class Monkey:
	def __init__(self, items, operation, test):
		self.inspected = 0
		self.items = []
		for item in items:
			self.items.append(Item(item))
		self.operation = operation
		self.test = test

	def throw_item(self, item, to):
		item.worry_level
		self.items.remove(item)
		to.items.append(item)

	def perform(self, monkies):
		for i in range(len(self.items)):
			self.inspected += 1
			worry = int(self.operation(self.items[0].worry_level)%9699690)
			self.items[0].worry_level = worry
			to = self.test.run(worry)
			#print(f'throw {self.items[0].worry_level} to {to}. Worry is {worry}')
			self.throw_item(self.items[0], monkies[to])

	def __repr__(self):
		return f'Insepected {self.inspected} times. Holding item: {self.items}'


monkies = [
	Monkey([99, 63, 76, 93, 54, 73], lambda old: old*11, Test(2, 7, 1)),
	Monkey([91, 60, 97, 54], lambda old: old+1, Test(17, 3, 2)),
	Monkey([65], lambda old: old+7, Test(7, 6, 5)),
	Monkey([84, 55], lambda old: old+3, Test(11, 2, 6)),
	Monkey([86, 63, 79, 54, 83], lambda old: old*old, Test(19, 7, 0)),
	Monkey([96, 67, 56, 95, 64, 69, 96], lambda old: old+4, Test(5, 4, 0)),
	Monkey([66, 94, 70, 93, 72, 67, 88, 51], lambda old: old*5, Test(13, 4, 5)),
	Monkey([59, 59, 74], lambda old: old+8, Test(3, 1, 3))
]
'''
monkies = [
	Monkey([79, 98], lambda old: old*19, Test(23, 2, 3)),
	Monkey([54, 65, 75, 74], lambda old: old+6, Test(19, 2, 0)),
	Monkey([79, 60, 97], lambda old: old*old, Test(13, 1, 3)),
	Monkey([74], lambda old: old+3, Test(17, 0, 1))
]
'''
print(monkies)
rounds = 10000
for i in range(rounds):
	for m in monkies:
		m.perform(monkies)
	
for m in monkies:
	print(m)
print('---')


