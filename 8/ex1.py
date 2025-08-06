# Exercise 1:

# Create a program that opens file.txt. Read each line of the file and prepend it with a line
# number.

selectImplementation = int(input("Which implementation do we test? (1/2): "))

def showImplementation():
	if selectImplementation == 1:
		implementation1()
	elif selectImplementation == 2:
		implementation2()

# Manual (first try)
def implementation1():
	try:
		with open('file.txt') as file:
			lineNumber = 0
			for line in file:
				lineNumber += 1
				print(str(lineNumber) + ": " + line.rstrip()) 
	except:
		print("Couldn't perform implementation1")

# Probably a better way, I came back here after some research
def implementation2():
	try:
		with open('file.txt') as file:
			for i, line in enumerate(file, start=1):
				print(f"{i}: {line.rstrip()}")
	except:
		print("Couldn't perform implementation1")

showImplementation()