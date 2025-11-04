import turtle as bob

import random

pencolor = ["red", "blue", "green", "yellow", "purple", "orange"]

bob.pensize(0.5)
bob.bgcolor("purple")  
forward = 0.0000001
angle = 190

bob.speed(5000000000000000)

while True:
    forward += random.randint(-2,4)
    angle += random.randint(-5, 5)
    bob.forward(forward)
    bob.right(angle)