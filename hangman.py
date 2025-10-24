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
user_guesses = 0
max_guesses = 8

print("Let us play Hangman. You need to guess the word I am thinking of.")
print("Hint: The word has", len(secret_word), "letters")
print(user_hint)

user_guess = input("Guess a letter or the word:")
count = secret_word.count(user_guess)
print("Did you guess a letter in the word?", count)





