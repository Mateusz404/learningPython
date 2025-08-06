# Exercise:

# Next, create a new program called cat_talk.py that imports the cat_say module. Use a function
# from the cat_say() module to display various messages to the screen.

import cat
import time
import random

catThings = ["Feed me.", "Pet me.", "Purr. Purr."]

while True:
	cat.meow(random.choice(catThings))
	print("---")
	time.sleep(2)