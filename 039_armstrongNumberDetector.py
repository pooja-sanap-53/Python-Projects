# ArmStrong Number Detector using Python

# First Approach - for beginners
print("ArmStrong Number is a number that is equal to sum of the cubes of its own digits.")
num = int(input("Enter the number you want to check: "))

str = str(num)
n = len(str)

final = 0
for i in range(n):
    numi = int(str[i])
    power = numi**n
    final += power


if final == num:
    print(f"The number {num} is a ArmStrong number of order {n}.")
else:
    print(f"The number {num} is not a ArmStrong number.")


# Second approach
n = int(input("Enter the number you want to check: "))
sum = 0
stri = str(n)
order = len(stri)
copy_num = n

while (n > 0):
    digit = n % 10
    sum += digit ** order
    n = n//10

if sum == copy_num:
    print(f"The number {copy_num} is a ArmStrong number of order {order}.")
else:
    print(f"The number {copy_num} is not a ArmStrong number.")
