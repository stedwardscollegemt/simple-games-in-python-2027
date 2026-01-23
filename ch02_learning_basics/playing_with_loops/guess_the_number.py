# ------ import modules section -----------------------------------------
import random

# ------ define functions section ---------------------------------------

# ------ algorithm steps section ----------------------------------------
print("************************")
print("*** Guess The Number ***")
print("************************")

# get a random number using the random module
number = random.randint(1, 10)

# display a message "We have thought of a number, can you guess?"
print("We have thought of a number, can you guess?")

# accept a guess input from the user
guess = input("Enter a guess...")

# convert user guess into an integer so that we can make comparisons
guess_num = int(guess)

# create a boolean variable is_guessed that checks whether guess is equal to number
is_guessed = (guess_num == number)

chances = 2

# ask for the user to keep guessing while not is_guessed... else, the user won!
# Hint: why not include a break and give the user three chances to guess?

while not is_guessed: # you can also write while is_guessed == False
    print(chances)
    if chances == 0:
        print("No. The number is", number)
        break
    if number > guess_num:
        print("No. The number I am thinking of is higher.")
    elif number < guess_num:
        print("No. The number I am thinking of is smaller.")
    # as we did before - get a number and check whether they guessed
    guess = input("Try again...")
    guess_num = int(guess)
    is_guessed = (guess_num == number)
    chances = chances - 1 # remove one chance
else:
    print("Wow! You guessed it.")