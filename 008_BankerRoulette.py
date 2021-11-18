# Banker Roulette
'''
Instructions
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.


Example Input
Angela, Ben, Jenny, Michael, Chloe

Example Output
Michael is going to buy the meal today!
'''
import random

test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

names_string = input("Enter everybody's names, separated by a comma :")
names = names_string.split(",")

number_of_people = len(names)
random_name = random.randint(0, number_of_people-1)
person_to_pay = names[random_name]

print(f"{person_to_pay} is going to pay for meals today!")