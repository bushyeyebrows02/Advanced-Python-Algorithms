import random 
print("Hi welcome to the game, This is a number guessing game.\nYou got 7 chances to guess the number. Let's start the game")
#Creating a variable that will hold the random number guessed by the computer.
number_to_guess = random.randrange(100)
# A predefined number of chances to guess for the user. 
chances = 7
guess_counter = 0

# creating a while loop that will execute a task while a certain condition is unmet. 
while guess_counter < chances:
    guess_counter +=1
    # my_guess is a variable that holds the user's guess for comparison with the computer`s random guessed number.`
    my_guess =int(input('please enter your guess: '))
    # The condition is (while the guess_counter is less than the maximum number of chances to guess) keeping letting the user guess.
     # Calculate the score based on remaining attempts
    score = chances - guess_counter
    if my_guess == number_to_guess:
        print(f'the number to guess is {number_to_guess} and the you found it it in {guess_counter} attempts')
        break
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f'The Number to guess was {number_to_guess}, better luck next time...')
    elif my_guess > number_to_guess:
        print('you guessed higher')
    elif my_guess < number_to_guess:
        print('you guessed lower')
        print(f"Your score is {score}")
    