# BMI 2.0

'''
Instructions

Write a program thta interprets the BMI based on a users height and weight.
- Under 18.5 - underweight
- over 18.5 but below 25 - normal
- over 25 but below 30 - overweight
- over 30 but below 35 - obese
- over 35 - clinically obese

'''

print("Welcome to the BMI Calculator!")

ht = float(input("Enter height in meters:"))
wt = float(input("Enter weight in kgs:"))

b = float((wt/(ht**2)))
BMI = round(b, 2)

print(f"Your BMI is {BMI}")

if (BMI <  18.5):
    print("You are underweight.")
elif (18.5 < BMI < 25):
    print("You are normal weighted .")
elif (25 < BMI < 30):
    print("You are overweight .")
elif (30 < BMI < 35):
    print("You are obese.")
else:
    print("You are clinically obese.")
