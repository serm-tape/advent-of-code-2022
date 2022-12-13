f = open("07_input.txt")
lines = f.read().split('\n')[1:-1]

class FileObject:
	def __init__(self, name, file_type, size):
		self.name = name
		self.file_type = file_type
		self.children = {}
		self.size = size
		self.parent = None

	def add_child(self, child):
		child.parent = self
		self.children[child.name] = child

	def get_size(self):
		if self.file_type == 'FILE':
			return self.size
		else:
			if self.size is not None:
				return self.size
			else:
				total_size = 0
				for f in self.children.values():
					total_size += f.get_size()
				return total_size

	def up(self):
		return self.parent

	def cd(self, to):
		return self.children[to]

	def ls(self):
		for f in self.children.values():
			print(f)

	def small_dir_sum(self, limit):
		total = 0
		for f in self.children.values():
			if f.file_type == 'DIR' and f.small_dir_sum(limit) <= limit:
				total += f.small_dir_sum(limit)

		return total

	def __str__(self):
		return f'type: {self.file_type}, name: {self.name}, size: {self.get_size()}'

	def __repr__(self):
		return f'type: {self.file_type}, name: {self.name}, size: {self.get_size()}'

file_system = FileObject('/', 'DIR', None)
current = file_system

for line in lines:
	if line == '$ cd ..':
		current = current.up()
	elif '$ cd ' in line: #cd
		directory = line.split(' ')[2]
		current = current.cd(directory)
	elif 'dir' in line:
		name = line.split(' ')[1]
		current.add_child(FileObject(name, 'DIR', None))
	elif line.split(' ')[0].isnumeric():
		file = line.split(' ')
		size = int(file[0])
		name = file[1]
		current.add_child(FileObject(name, 'FILE', size))


total_size = file_system.get_size()

def all_size(fo, size_dict, pwd):
	pwd.append(fo.name)
	size_dict['/'.join(pwd)] = fo.get_size()

	for fi in fo.children.values():
		if fi.file_type == 'DIR':
			all_size(fi, size_dict, pwd)

	return size_dict

all_dir = all_size(file_system, {}, [])
space_to = 40000000
to_remove = total_size - space_to
removed_size = 70000000
removed_dir = ''
print(f'{to_remove} to be removed')
for key,value in all_dir.items():
	if value >= to_remove and value < removed_size:
		print(f'candidate value: {value}')
		removed_size = value
		removed_dir = key
print(f'removed dir = {removed_dir} size = {removed_size}')
f.close()