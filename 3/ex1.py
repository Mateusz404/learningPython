# Exercise 1:

# Create a program that asks the user how far they want to travel. If they want to travel less than
# three miles tell them to walk. If they want to travel more than three miles, but less than three
# hundred miles, tell them to drive. If they want to travel three hundred miles or more tell them to
# fly.

travelDistance = float(input("How far do you want to travel (in miles)? "))

if travelDistance < 3:
	print("You should walk.")
elif travelDistance < 300:
	print("You should drive.")
elif travelDistance >= 300:
	print("You should fly.")