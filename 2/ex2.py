# Exercise 2:

# Building on the previous example, let's also assume that you have saved $918 to fund your new
# adventure. You wonder how many days you can keep one server running before your money
# runs out. Of course, you hope your social network becomes popular and requires 20 servers to
# keep up with the demand. How much will it cost to operate at that point?

# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per month?
# How much does it cost to operate twenty servers per day?
# How much does it cost to operate twenty servers per month?
# How many days can I operate one server with $918?

from calendar import monthrange

year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month (1-12): "))
hourlyPrice = float(input("Enter the hourly cost of the server (e.g., 0.51 for $0.51): "))
cloudServersNeeded = int(input("Enter the number of servers needed (e.g., 20): "))
budget = float(input("Enter your budget (e.g., 918): "))

dailyPrice = 24 * hourlyPrice
monthlyPrice = dailyPrice * monthrange(year, month)[1]

spacer = '-' * 20

print(spacer)
print('Cost to operate one server')
print('Daily: | ${0:8}'.format(dailyPrice))
print('Monthly: | ${0:8}'.format(monthlyPrice))
print(spacer)
print('With a budget of ${}, you can operate one server for:'.format(budget))
print('{} days'.format(int(budget / dailyPrice)))
print(spacer)
print('Cost to operate {} server/s '.format(cloudServersNeeded))
print('Daily: | ${0:8}'.format(dailyPrice * cloudServersNeeded))
print('Monthly: | ${0:8}'.format(monthlyPrice * cloudServersNeeded))
print(spacer)