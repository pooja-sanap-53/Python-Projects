# Trailing Zeros in Factorial

def factorial(n):
    if n ==1 or num==0:
        return 1
    return n* factorial(n-1)

def trailingZeros(n):
    count = 0
    i = 5
    while(n//i !=0):
        count += int(n/i)
        i = i*5 
    return count
    
num = int(input("Enter the Number:"))
# print(f"The Factorial of {num} is {factorial(num)}.")
print(f"The number of Traailing Zeros in Factorial of {num} is {trailingZeros(num)}.")

