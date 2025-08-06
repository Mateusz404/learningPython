# Exercise 2:

# Read the contents of animals.txt and produce a file named animals­sorted.txt that is sorted
# alphabetically.

animalsList = []

def populateAnimalsList(verbose):
	with open('animals.txt') as animals:
		try:
			for animal in animals:
				animalsList.append(animal.strip())
				if verbose: print("Adding '{}' to the internal animals list.".format(animal.strip()))
			print("----")
		except:
			print("Couldn't loop over animals.txt.")

def sortAnimalsList():
	try:
		animalsList.sort()
		print("animalsList sorted, content: ")
		for i in animalsList:
			print(i)
		print("----")
	except:
		print("Couldn't sort animalsList.")

populateAnimalsList(False)
sortAnimalsList()