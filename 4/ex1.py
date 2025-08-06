# Exercise 1:

# Create a fill in the blank word game. Prompt the user to enter a noun, verb, and an adjective.
# Use those responses to fill in the blanks and display the story.

# Write a short story. Remove a noun, verb, and an adjective.

# Create a function to get the input from the user.
# Create a function that fills in the blanks in the story you created.
# Ensure each function contains a docstring.
# After the noun, verb, and adjective have been collected from the user, display the story using
# their input.

def getNoun():
	"""Prompt the user to enter a noun."""
	return input("Enter a noun: ")

def getVerb():
	"""Prompt the user to enter a verb."""
	return input("Enter a verb: ")

def getAdjective():
	"""Prompt the user to enter an adjective."""
	return input("Enter an adjective: ")

def getUserInputs():
	"""Get inputs from the user for noun, verb, and adjective."""
	adjective = getAdjective()
	noun = getNoun()
	verb = getVerb()
	return noun, verb, adjective

def fillInTheBlanks(noun, verb, adjective):
	"""Fill in the blanks of the story with the user's input."""
	story = "Once upon a time, there was a {adjective} {noun} that loved to {verb}. "
	return story

def displayStory(story, noun, verb, adjective):
	"""Display the completed story with the user's inputs."""
	print(story.format(adjective=adjective, noun=noun, verb=verb))


noun, verb, adjective = getUserInputs()
story = fillInTheBlanks(noun, verb, adjective)
displayStory(story, noun, verb, adjective)