# ----- Practice string functions ----------------------
message = "Happy birthday, Aiden!"

# how to get the position of a character in a string
pos_A = message.index("A")
pos_a = message.index("a")

# how to change a string to lower case or upper case
lower = message.lower()
upper = message.upper()

# how to count all letter a's and t's
count_a = lower.count("a")
count_T = upper.count("T")

# ----- Practice print functions -----------------------

# simplest way to use print
print("A very simple message")
print(message)

# print function with concatenation (joining two or more strings)
print("Original message:", message)
print("Position of A is", pos_A)
print("Position of a is", pos_a)
print("Message after using lower():", lower)
print("Message after using upper():", upper)
print("Number of letter a's in my message: ", count_a)
print("Number of letter t's in my message: ", count_T)

# print function using formatting
name = "Aiden"
print(f"Happy birthday, {name}")

# looping through a list and using print formatting
list_birthday_treats = ["cake", "cupcakes", "motor oil"]
for treat in list_birthday_treats:
    print(f"For my birthday I would like: {treat}")

# print using end (do not automatically add a new line)
print("For my birthday I would like", end="")
for treat in list_birthday_treats:
    print(f"{treat}, ", end="")
print("")

# ----- Practice list functions -----------------------

list_bday_activities = ["bouncy castle", "zipline", "laser tag"]

# We already know about append() - this adds an item to the end of the list
print("Original list:", list_bday_activities)
list_bday_activities.append("LAN party")
print("Now list has:", list_bday_activities)

# We also know about len
print("Length of list:", len(list_bday_activities))

# Let us see what pop() does... 
# Gives the last element and removes it
popped_item = list_bday_activities.pop()
print("I have already done this activity:", popped_item)
print("Activities left:", list_bday_activities)

# How do we use remove?
# Remove tries to look for something you want deleted from the list
list_bday_activities.remove("bouncy castle")
print("Removed bouncy castle from my list: ", list_bday_activities)

# We think that clear() removes all elements of the list
list_bday_activities.clear()
print("What does the list look like now?", list_bday_activities)

# We can learn about count(), insert(), reverse(), and sort() as we develop simple games.

# Let us try to use sort and reverse in one go
fruit = ["cherry", "banana", "kiwi"]
print("Original list: ", fruit)
fruit.sort(reverse=True)
print("List after I have sorted and reversed: ", fruit)