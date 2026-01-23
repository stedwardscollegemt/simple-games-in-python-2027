# ------ import modules section -----------------------------------------

# ------ define functions section ---------------------------------------
def title():
    print("+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    print("|R|E|A|L| |F|I|Z|Z| |B|U|Z|Z|")
    print("+-+-+-+-+ +-+-+-+-+ +-+-+-+-+")
    
# ------ algorithm steps section ----------------------------------------
title()

print("Let us play FizzBuzz together. Can we get to 50?")

for num in range(1, 51):
    if num % 2 == 1:
        # computer is going to play
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz") # append adds to the end of the list
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)
    else:
        # ask the user to say what is next in the sequence
        next = input("Say what comes next... ")

        # check if the human made a mistake
        # != means not equal to
        if num % 5 == 0 and num % 3 == 0 and next != "FizzBuzz":
            print("Oops! You meant FizzBuzz. Game over.")
            break
        elif num % 5 == 0 and next != "Buzz":
            print("Oops! You meant Buzz. Game over.")
            break
        elif num % 3 == 0 and next != "Fizz":
            print("Oops! You meant Fizz. Game over.")
            break
        elif int(next) != num:
            print("What?!", num, "is next. Try again.")
            break
        # check if the human finished the sequence
        elif num == 50 and next == "Buzz":
            print("Good job! You won this time round.")
