def title():
    print("⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁ the ₊ ⊹ . ݁ ⟡ ݁ . ⊹ ")
    print("|     M A G I C      D O O R   |")
    print("⊹ . ݁ ⟡ ݁ . ⊹ ₊ ݁ ݁ ⟡ ݁ ₊ ⊹ . ݁ ⟡ ݁ . ⊹ ")

# ------ algorithm steps section ----------------------------------------

title()

# todo: 1a.	Ask the user to enter their name and display a personalised welcome message
#           e.g. "Welcome, John"


# todo: 1b. Create variables for player health (starting at 10), 
#           current location (starting in the hall) and game over (False)

# todo: 1c. Create an empty list of inventory items

 
print("You are standing in a mysterious hall.")

# todo: 2a. Construct an infinite loop so the game keeps running


# todo: 2b. Write a condition statement that checks whether the game over is True 
#           and breaks out of the infinite loop.

# todo: 2c. Display the player's health

# this code needs to be inside the game loop
if location == "hall":
        # Display door options
        print("Choose a magic door:")
        print("A. Green Door")
        print("B. Yellow Door")
        print("C. Purple Door")

        # todo: 2d. Ask the user to enter their choice and update the location
elif location == "forest":
      # todo: 3a. i Display a description of the forest
      print("You are in a forest.")

      # todo: 3a. ii. Ask the player if they want to take the clue item
      #          iii. If yes, add "clue: music"  to the inventory list

      # Return to hall
      location = "hall"

elif location == "cave":
      print("You are in a cave.")

      # todo: 3b.  i.   Check whether the player has a clue item in their inventory
      # todo: 3b.  ii.  If the player has a clue item, display a description of the creature that blocks the way. 
      #                 The creature can be fought by guessing a riddle: "What has keys but cannot open locks?" using the clue item. 
      #                 If the riddle is guessed, then the player collects a key item (add it to the inventory list).
      # todo: 3b. iii.  If the player does not have a clue item or fails to guess the riddle, then health is reduced
      # todo: 3b.  iv.	Game is over if health reaches 0
      
      # Return to hall if still alive
      if health > 0:
            location = "hall"

elif location == "treasure chamber":
      print("You are in the treasure chamber.")
      if "key" in inventory:
            print("You unlock the treasure chest.")
            print("You win!")
            game_over = True
      else:
            print("The chest is locked.")
            print("You need to find the key first.")
            location = "hall"
