# Setup
file = open('adv07.txt', 'r')
lines = [l.strip() for l in file.readlines()]


class File:
	name = None
	parent = None
	children: dict = None
	is_directory = False
	size = 0

	def __init__(self, name, is_directory, parent = None, size = 0):
		self.name = name
		self.is_directory = is_directory
		self.parent = parent
		self.size = size
		self.children = {}


# Create tree of files
head = File('/', True)
current = head

for l in lines:
	if l.startswith('$'):
		if l.startswith('$ cd '):
			dir = l.replace('$ cd ', '')
			if dir == '/':
				current = head
			elif dir == '..':
				current = current.parent if current.parent != None else current
			else:
				current = current.children[dir]
	elif (l.startswith('dir ')):
		name = l.replace('dir ', '')
		current.children[name] = File(name, True, current)
	else:
		size, name = l.split(' ')
		size = int(size)
		current.children[name] = File(name, False, current, size)
		c_temp = current
		while True:
			c_temp.size += size
			c_temp = c_temp.parent
			if c_temp == None:
				break


# Part 1

sum = 0

def sum_dirs_smaller_than(dir, max_size):
	global sum
	if dir.size < max_size:
		sum += dir.size
	
	for key in dir.children.keys():
		if dir.children[key].is_directory:
			sum_dirs_smaller_than(dir.children[key], max_size)

sum_dirs_smaller_than(head, 100000)
print(f'Part 1: {sum}')


def get_dir_size_for_update(dir, req_size):
	global smallest_size
	if dir.size < smallest_size and dir.size >= req_size:
		smallest_size = dir.size
	
	for key in dir.children.keys():
		if dir.children[key].is_directory:
			get_dir_size_for_update(dir.children[key], req_size)


smallest_size = head.size
required_size = 30000000 - (70000000 - head.size)
get_dir_size_for_update(head, required_size)
print(f'Part 2 {smallest_size}')
