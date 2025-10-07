from turtle import *

# some functions need a turtle object
t = Turtle() # create turtle
t.shape("turtle") # make it look like a turtle
t.showturtle() # make it visible on screen
t.color("green")

# drawing a square path for my turtle called t

# up
t.left(90)
t.forward(50)

# right
t.right(90)
t.forward(50)

# down
t.left(270)
t.forward(50)

# left
t.left(-90)
t.forward(50)

quit = input("Press any key to quit...")