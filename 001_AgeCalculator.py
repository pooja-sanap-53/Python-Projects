# Age Calculator
'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Example Input
56
Example Output
You have 12410 days, 1768 weeks, and 408 months left.
'''
age = int(input("What is your age?"))
a = 90 - age
days = a *365
weeks = a*52
months = a*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
