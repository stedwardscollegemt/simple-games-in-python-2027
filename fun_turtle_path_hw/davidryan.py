# Fun Turtle Project: Colorful Zig-Zag Path with Loops
# Created by David Ryan
# Inspired by a design suggested via ChatGPT (OpenAI) for learning purposes

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("midnightblue")
screen.title("Colorful Zig-Zag Path with Loops")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)

colors = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta", "white"]

# Draw a zig-zag looping path
for i in range(60):
    pen.color(colors[i % len(colors)])
    pen.forward(10 + i * 2)
    pen.right(60 if i % 2 == 0 else 120)
    pen.circle(20, 180)

# Add your name to the screen
pen.penup()
pen.goto(-280, 200)  # Move to top-left corner (adjust as needed)
pen.color("white")
pen.write("Created by David Ryan", font=("Arial", 16, "bold"))
pen.hideturtle()

# Keep the window open
screen.mainloop()
