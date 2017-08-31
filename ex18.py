#writtng function in Python
def print_two_argv(*argv):
	one,two,three = argv
	print("inside argv")
	print(f"One: {one}\nTwo: {two}")

def print_two(one,two):
	print(f"One: {one}\nTwo: {two}")

def print_two(one,two,three):
	print(f"One: {one}\nTwo: {two}\nthree: {three}")

def print_one(one):
	print(f"One: {one}")

def print_none():
	print("none")

print_two_argv(1,2,3)
print("\n")
print_two(1,2,3)
print("\n")
print_two(1,2,3)
print("\n")
print_one(1)
print("\n")
print_none()
