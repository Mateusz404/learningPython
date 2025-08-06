# Excercise 3

# Write a Python program that prompts for input and displays a cat "saying" what was provided by
# the user. Place the input provided by the user inside a speech bubble. Make the speech bubble
# expand or contract to fit around the input provided by the user.

print("Please type something for the cat to say:")
userInput = input()

cat = r"""
 /\_/\ 
( o.o )
 > ^ < 
"""

wrapper = '-' * (len(userInput) + 4)

print('{}{}'.format(' ' * len(cat), wrapper))
print('{}{}'.format(' ' * len(cat), '< ' + userInput + ' >'))
print('{}{}'.format(' ' * len(cat), wrapper))
print(cat)
