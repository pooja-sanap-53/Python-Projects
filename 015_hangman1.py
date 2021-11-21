
'''
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
'''


import random 
word_list = ["aardvark", "baboon", "camel"]

# To do 1
index = random.randint(0,2)
chosen_word = word_list[index]

# To do 2 
guess = input("Guess a letter in the word:")
guess = guess.lower()

# To do 3
for i in chosen_word:
    if guess == i:
        print("Is present")
    else:
        print("Is not present.")