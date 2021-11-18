# Leap Year Challenge

'''
Instructuions : 

Write a program that works out whether if a given year is a leap year.
'''

yr = int(input("Enter the year :"))

if (yr%4 == 0):
    
    if(yr%100 == 0):
        if (yr%400==0):
            print(f"{yr} is a leap year.") 
        else:
            print(f"{yr} is not a leap year.") 

    else:
        print(f"{yr} is a leap year.") 

else:
    print(f"{yr} is not a leap year.")