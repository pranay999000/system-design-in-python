class File:
	def __init__(self, name):
		self.name = name

class Directory:
	def __init__(self, name):
		self.name = name
		self.files = list()
		self.directories = list()
	
	def ls(self):
		print('>>', self.name)
		for d in self.directories:
			print("\\", self.name, "\\", d.name)
		for f in self.files:
			print("\\", self.name, "..", f.name)

	def touch(self, filename):
		self.files.append(File(filename))
	
	def mkdir(self, dirname):
		self.directories.append(Directory(dirname))

stack = list()
directory = Directory("root")
stack.append(directory)
while True:
	command = input()
	op = command.split()[0]

	if op == "ls":
		directory.ls()

	elif op == "mkdir":
		directory.mkdir(command.split()[1])
		print('directory created inside', directory.name)

	elif op == "touch":
		directory.touch(command.split()[1])
	
	elif op == "cd":
		if not command.split()[1]:
			print("invalid command")
		elif command.split()[1] == "..":
			if len(stack) == 1:
				print("invalid command!")
			else:
				stack.pop()
				directory = stack[-1]
		else:
			f = False
			for d in directory.directories:
				if d.name == command.split()[1]:
					directory = d
					stack.append(d)
					f = True
			if not f:
				print("directory not found!")

	elif op == "rm":
		if not command.split()[1]:
			print("invalid command")
		else:
			f = False
			for i in range(len(directory.directories)):
				if directory.directories[i].name == command.split()[1]:
					directory.directories.pop(i)
				f = True

	elif op == "pwd":
		for s in stack:
			print(s.name, end="\\")
		print()
	
	elif op == "exit":
		print("thanks for using")
		break