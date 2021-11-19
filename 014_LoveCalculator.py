# Love Calculator 
'''
Instructions
You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.

'''
print('Welcome to the Love Calculator!')
name1 = input("Enter your name:")
name2 = input("Enter your partner's name:")

name = name1 + name2

# letters in love
lcount = name.lower().count("l")
ocount = name.lower().count("o")
vcount = name.lower().count("v")
ecount = name.lower().count("e")

# letters in true
tcount = name.lower().count("t")
rcount = name.lower().count("r")
ucount = name.lower().count("u")
e2count = name.lower().count("e")


love_sum = lcount+ ocount + vcount + ecount
true_sum = tcount + rcount + ucount + e2count

love_score =  str(true_sum) + str(love_sum)
love_score = int(love_score)

# message 

if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<= love_score <= 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"You score is {love_score}")