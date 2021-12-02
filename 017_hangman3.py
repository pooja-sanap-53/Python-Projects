# Hangman 3
'''

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

'''

import random
end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


display = []
a = len(chosen_word)
for i in range(len(chosen_word)):
    display.append("_")
print(display)


while  not end_of_game:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You won!")
