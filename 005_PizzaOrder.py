# Pizza Order 
'''
Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''

print('Welcome to Pizza Hut!!')
pizza = input('''\nWhich size of Pizza you want?
Press 'S' for small size
Press 'M' for medium size
Press 'L' for large size
''')

bill = 0

if(pizza == 'S'):
    bill = 15
    print("\nPrice for small size pizza is $15") 

elif(pizza == 'M'):
    bill = 20
    print("\nPrice for medium size pizza is $20") 

elif(pizza == 'L'):
    bill = 25
    print("\nPrice for large size pizza is $25") 

else:
    print("\nYou have entered wrong input.") 

pepper = input("Do you want to take Pepperoni? Y or N\n")

if(pizza == 'S' and pepper == "Y"):
    bill = bill + 2
    print("Price for Pepperoni of small size pizza is $2") 

elif(pizza == 'M' and pepper == "Y"):
    bill = bill + 3
    print("Price for Pepperoni of  medium size pizza is $3") 

elif(pizza == 'L'and pepper == "Y"):
    bill = bill + 3
    print("Price for Pepperoni of large size pizza is $3") 

else:
    print("You have not selected Pepperoni option.") 

cheese = input("Do you want cheese? Y or N\n")

if (cheese == 'Y'):
    bill = bill + 1
    print("Price for cheese is $1 for any type of pizza.")
else:
    print("You have not selected cheese option.") 

print(f"Your total bill is ${bill}.")