# Cat excercie refactored to be used as a module (first version in the /1/ex3.py file)

def main():
	print("Please type something for the cat to say:")

input = ''
cat = r"""
 /\_/\ 
( o.o )
 > ^ < 
"""

def meow(input):
	wrapper = '-' * (len(input) + 4)
	
	try:
		print('{}{}'.format(' ' * len(cat), wrapper))
		print('{}{}'.format(' ' * len(cat), '< ' + input + ' >'))
		print('{}{}'.format(' ' * len(cat), wrapper))
		print(cat)
	except:
		print("Meow :'(((")
