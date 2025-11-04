# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------
def title():
    print(" _                                             ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                   |___/                       ")

# ------ algorithm steps section ----------------------------------------

title()

secret_word = "secret" # this is a string variable
user_hint = ["_", "_", "_", "_", "_"] # this is a list variable
user_guesses = 0 # this is an integer variable
max_guesses = 8

print("Let us play Hangman. You need to guess the word I am thinking of.") # this is a simple output statement
print("Hint: The word has", len(secret_word), "letters") # an output statement with joining (,)
print(user_hint) # this is how we can display variable values

user_guess = input("Guess a letter or the word:") # this is an input statement
count = secret_word.count(user_guess) # an example using a string function

print("Did you guess a letter in the word?")
answer = count > 0 # an example of a Boolean expression with a conditional operator
print(answer)

# simple if/else statement (two branches)
if count > 0:
    print("You guessed a letter or the word.")
else:
    print("You did not guess anything!")

# if/elif/else statement (three branches)
if len(user_guess) == 1:
    print("You tried to guess a letter.")
elif len(user_guess) == len(secret_word):
    print("You tried to guess the word.")
else:
    print("We don't know what you are doing!")






