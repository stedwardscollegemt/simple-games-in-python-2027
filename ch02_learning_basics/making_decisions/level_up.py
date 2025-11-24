# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------

# ------ algorithm steps section ----------------------------------------
print("**********************************")
print("* Who wants to be a millionaire? *")
print("**********************************")

# declare a list of all levels in a list variable called the money_tree
money_tree = ["$100", "$200", "$300", "$500", "$1000"]

# declare a variable called level to store the current level starting at 0
level = 0

# question for $100
print("Here is your first question for " + money_tree[level] + "...")
print("In the UK, the abbreviation NHS stands for National what Service?")
print("[A] Humanity [B] Household [C] Honour [D] Health")
player_guess = input("Enter your guess: ")
correct_answer = "D"

# if player_guess is equal to (==) correct_answer then level up, else, game is over
if player_guess == correct_answer:
    level = level + 1
else:
    print("Wrong! Game over.")


# code for a level 1 question
if level == 1:
    print("Here is your second question for " + money_tree[level] + "...")
    print("What is the capital city of Morocco?")
    print("[A] Valletta [B] Rabat [C] Qatar [D] Paris")
    player_guess = input("Enter your guess: ")
    correct_answer = "B"

    if player_guess == correct_answer:
        level = level + 1
    else:
        print("Wrong! Game over.")

if level == 2:
    print("Here is your second question for " + money_tree[level] + "...")
    print("Who was the first president of the US?")
    print("[A] George Washingtom [B] Thomas Jefferson [C] Charlie Kirk [D] Robert Abela")
    player_guess = input("Enter your guess: ")
    correct_answer = "A"

    if player_guess == correct_answer:
        level = level + 1
    else:
        print("Wrong! Game over.")

if level == 3:
    print("Here is your fourth question for " + money_tree[level] + "...")
    print("Who won the 2002 World Cup?")
    print("[A] Brazil [B] Italy [C] Argentina [D] France")
    player_guess = input("Enter your guess: ")
    correct_answer = "A"

    if player_guess == correct_answer:
        level = level + 1
    else:
        print("Wrong! Game Over.")
