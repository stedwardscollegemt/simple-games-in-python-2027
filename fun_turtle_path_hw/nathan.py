from turtle import *

# some functions need a turtle object
t = Turtle() # create turtle
t.shape("turtle") # make it look like a turtle
t.showturtle() # make it visible on screen
t.color("green")

# drawing a hexagon using the turtle called t

# Each side of the hexagon
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)
t.forward(100)
t.right(60)

quit = input("Press any key to quit...")