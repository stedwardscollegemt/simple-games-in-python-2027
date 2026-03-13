# ------ import modules section -----------------------------------------
from time import sleep # we try to import the functions we need only

# ------ define functions section ---------------------------------------
def title():
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    print("        |R|I|D|D|L|E|R|            ")
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")

def reveal_message(message):
    # Here is code for a typing effect to display the riddle using functions
    #       - print(char, end="", flush=True)
    #       - time.sleep(delay)
    for char in message:
        print(char, end="", flush=True)
        sleep(0.1)
    print("") # print a new line

# ------ algorithm steps section ----------------------------------------
title()

riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
clue = "You would probably hear it in a large cave."
answer = "echo"

reveal_message(riddle)

# Give the user two chances to guess, for the second chance display the clue
chances = 2
win = False

while True:
    if chances == 0:
        break
    
    guess = input("Enter your guess: ").lower() # ensures the user input is in lower case
    chances = chances - 1

    if guess == answer:
        win = True
        break
    
    if chances == 1:
        reveal_message(clue)

# Display whether the user won or not, in which case the answer will be revealed
if win:
    message = "Correct. You have guessed."
    reveal_message(message)
else:
    message = "The answer is" + answer
    reveal_message(message)