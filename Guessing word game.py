# import the radndom module
import random
# getting the user`s name`
userName = input('What is your name: ')
print('Good luck {userName}')

# A list of possible words for the guessing game is defined. 
# These words are strings stored in a list called words.
# Also, the program selects a random word from the words list using random.
# choice(). The selected word is stored in the variable word.
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

# Prompting the user to start guessing the characters of the randomly chosen words
print('Guess the charecters')
# An empty string that will hold all the characters guessed by the user.
guesses =''
# The number of attempts the user has to guess the word. Initially set to 12.
turns = 12
# THE MAIN GAME LOOP
# This loop runs as long as the user has turns remaining to guess. inside the loop the user
# will be prompted to guess the characters
while turns > 0:
    # This variable is a counter for the characters that have been guessed not correctly
    failed = 0
    for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_')
                failed += 1
    if failed == 0:
        print('You won!')
        print('The word is', word)
        break

    print()
    guess = input('Guess a character: ')
    guesses += guess
    
    if guess not in word:
        turns -= 1
        print('Wrong! You have', turns, 'more attempts')
        
        if turns == 0:
            print('You lose! The word was', word)