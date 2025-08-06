# Exercise 1:

# Create a dictionary that contains a list of people and one interesting fact about each of them.
# 1. Display each person and their interesting fact to the screen. 
# 2. Next, change a fact about one of the people. 
# 3. Also add an additional person and corresponding fact. 
# 4. Display the new list of people and facts. Run the program multiple times and notice if the order changes.

people = {
	"Alice": "Loves hiking in the mountains.",
	"Bob": "Is an avid chess player.",
	"Charlie": "Enjoys painting landscapes."
}

def displayPeopleFacts():
	"""Display each person and their interesting fact."""
	for person in people:
		print("A fact about " + person + " is: " + people[person])

displayPeopleFacts()

people["Alice"] = "Alice loves hiking in the mountains and has climbed several peaks."
people["David"] = "Is a passionate photographer who captures wildlife."

print("Updated facts:")
displayPeopleFacts()