# ------ import modules section -----------------------------------------
import time

# ------ define functions section ---------------------------------------
def title():
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    print("        |R|I|D|D|L|E|R|            ")
    print("+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    
# ------ algorithm steps section ----------------------------------------
title()

riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
clue = "You would probably hear it in a large cave."
answer = "echo"

# Here is code for a typing effect to display the riddle using functions
#       - print(char, end="", flush=True)
#       - time.sleep(delay)
for char in riddle:
    print(char, end="", flush=True)
    time.sleep(0.3)

# TODO: Give the user two chances to guess, for the second chance display the clue

# TODO: Display whether the user won or not, in which case the answer will be revealed
