# Currency Convertor

with open('currencyData.txt') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")  #to split the data by tabs

    currencyDict[parsed[0]] = parsed[1]

# to take input from user
amt = float(input("Enter the amount : "))

print("Enter the name of currency you want to convert this amount to? \nAvailable options are as follows:\n")

# List comphrension to print the available options to give user a idea about them
[print(item) for item in currencyDict.keys()]

# to take currency input from user 
currency = input("Please Enter the option you want : ")
print(f"{amt} INR is equal to {amt * float(currencyDict[currency])} {currency}.")