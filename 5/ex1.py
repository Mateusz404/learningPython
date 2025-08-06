# Exercise 1:

# Create a Python program that captures and displays a person's to­do list. Continually prompt
# the user for another item until they enter a blank item. After all the items are entered, display the
# to­do list back to the user.

todoList = []

def askForTodo():
	"""Prompt the user to enter a to-do item."""
	task = input("Enter a task for your to­do list. (or press <Enter> to finish): ")
	if task == "":
		displayTodoList()
		return ""
	else:
		todoList.append(task)
		print("Task added: {}".format(task))
		askForTodo()
		return task

def displayTodoList():
	"""Display the to-do list."""
	if todoList:
		print("Your to­do list:")
		for task in todoList:
			print("- {}".format(task))
	else:
		print("Your to­do list is empty. Create a new task...")
		askForTodo()

askForTodo()
