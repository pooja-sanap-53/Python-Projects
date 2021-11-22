# Prime Number Checker
'''
INSTRUCTIONS
Prime numbers are numbers that can only be cleanly divided by itself and 1.
You need to write a function that checks whether if the number passed into it is a prime number or not.

Example Input 1
73
Example Output 1
It's a prime number.
'''


def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number % i == 0:
            is_prime= False
    
    if is_prime:
        print("Given number is Prime.")
    else:
        print("Given number is Not Prime.")


n = int(input("Check this number: "))
prime_checker(number=n)
