
'''
This is a two-player game where each player chooses one object.  As we know, there are three objects, snake, water, and gun. So, the result will be 

Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.
In situations where both players choose the same object, the result will be a draw.

Now moving on to instructions:
You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
You do not have to use a print statement in case of the above function.
Then you have to give input from your side.
After getting ten consecutive inputs, the computer will show the result based on each iteration.
You have to use loops(while loop is preferred).

'''

import random 

l1 = ["S", "W", "G"]

print("""
    Welcome to Snake, Water, Gun GAME!!!

    Gun shoots the Snake, Snake drinks the Water and the Water makes Gun unfunctional.
    Computer will randomly choose its option. 
    Your choice in no way will affect the decision of the Computer.
    So this is gonna be a FAIR GAME 

    Choose from following : 
    S - Snake 
    W - Water
    G - Gun 
    
    Rules:
    1.Use CAPITAL letters only !
    2.There will be 10 matches. 
    3.The one who wins most of the matches will be the WINNER!\n
""")

computer_point = 0
human_point = 0
match_tie = 0
i = 0

while (i<10) :
        
    a = str(input("Enter your choice from above:\n"))
    b = random.choice(l1)
    if a == "S" :

        if b == "S":
            print("Match Tie.")
            match_tie = match_tie + 1
        elif b == "W" :
            print("1 point for you.")
            human_point = human_point + 1
        elif b == "G" :
            print("1 point for computer.")
            computer_point = computer_point + 1
        else:
            print("Invalid input!")

    elif a == "W" : 

        if b == "S" :
            print("1 point for computer.")
            computer_point = computer_point + 1
        elif b == "W" :
            print("Match Tie.")
            match_tie = match_tie + 1
        elif b == "G" :
            print("1 point for you.")
            human_point = human_point + 1
        else:
            print("Invalid input!")

    elif a == "G" :

        if b == "S" :
            print("1 point for you.")
            human_point = human_point + 1
        elif b == "W" :
            print("Match Tie.")
            match_tie = match_tie + 1
        elif b == "G" :
            print("1 point for computer.")
            computer_point = computer_point + 1
        else:
            print("Invalid input!")

    else : 
        print("Invalid input!")

    i = i + 1

    print("\nYour score : ", human_point)
    print("Computer score : ", computer_point)
    print("Matches Tie : ", match_tie)
    print("Number of matches left : ", 10 - i, "\n")

    if i == 10 :
        print("Game Over")

if human_point > computer_point:
    print("Congratulations, you won !! ")
elif human_point < computer_point :
    print("You lose. ")
else : 
    print("Match Draw")

