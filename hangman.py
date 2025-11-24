# ------ import modules section -----------------------------------------
import random

# ------ define functions section ---------------------------------------
def title():
    print(" _                                             ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                   |___/                       ")

def update_user_hint(letter, secret_word, user_hint):
    pos = 0
    while pos < len(secret_word) - 1:
        if secret_word[pos] == letter:
            user_hint[pos] = letter
        pos = pos + 1
    return user_hint

# ------ algorithm steps section ----------------------------------------

title()

list_secret_words = ['sneaky', 'fairy', 'furniture', 'python', 'literature', 'hangman']
secret_word = random.choice(list_secret_words)
user_hint = ['_'] * len(secret_word) # use multiplication to make a list of any length with the same element
user_guesses = 0 # this is an integer variable
lives = 8

print("Let us play Hangman. You need to guess the word I am thinking of.") # this is a simple output statement
print("Hint: the word has", len(secret_word), "letters.")
print(user_hint) # this is how we can display variable values
print("You have", lives, "lives.")

while True:
    # win the game
    win = '_' not in user_hint
    if win:
        print("Well done. You guessed!")
        break

    # lose all lives
    lose = lives == 0
    if lose:
        print("Sorry, you have no lives left. The word was: ", secret_word)
        break
    
    # usual game update
    print(user_hint)
    user_guess = input("Guess a letter:")
    user_guesses = user_guesses + 1
    if secret_word.count(user_guess) > 0:
        print("Good guess")
        update_user_hint(user_guess, secret_word, user_hint)
    else:
        lives = lives - 1



