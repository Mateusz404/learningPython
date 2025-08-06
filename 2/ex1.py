# Exercise 1:

# Let's assume you are planning to use your Python skills to build a social networking service.
# You decide to host your application on servers running in the cloud. You pick a hosting provider
# that charges $0.51 per hour. You will launch your service using one server and want to know
# how much it will cost to operate per day and per month.
# Write a Python program that displays the answers to the following questions:
# How much does it cost to operate one server per day?
# How much does it cost to operate one server per month?

from calendar import monthrange

year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month (1-12): "))

hourlyPrice = float(input("Enter the hourly cost of the server (e.g., 0.51 for $0.51): "))

dailyPrice = 24 * hourlyPrice
monthlyPrice = dailyPrice * monthrange(year, month)[1]

print('Cost to operate one server')
print('Daily: | ${}'.format(dailyPrice))
print('Monthly: | ${}'.format(monthlyPrice))