#  Fizz Buzz 

'''
You are going to write a program that automatically prints the solution to the FizzBuzz game.

Your program should print ecah number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz"
When the number is divisible by 5, then instead of printing the number it should print "Buzz"
And if the number is divisble by both 3 and 5 , it should print "FizzBuzz"

'''

for i in range (1, 101):
    if(i%3 == 0 and i%5==0):
        print("FizzBuzz")
    elif(i%5 == 0):
        print("Buzz")
    elif (i%3 == 0):
        print("Fizz")
    else:
        print(i)
    