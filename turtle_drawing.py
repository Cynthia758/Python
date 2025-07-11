import turtle # Used for drawing shapes with a pen on screen.
import random # Let us pick up a random color

# Create screen and Turtle
screen = turtle.Screen() # Creates Drawing Window.
screen.bgcolor("black")
t = turtle.Turtle() # Drawing pen
t.speed(10) # 1 = slowest, 10 = fast, 0 = instant

colors = ["red", "orange", "yellow", "pink", "green", "purple"]


for i in range(36): # Loop runs for 36 times
    t.color(random.choice(colors)) # Randomly picks color
    t.forward(100) # Moves the pen forward 100 times
    t.right(20) #turns the turtle 60 degree right
    t.forward(100)
    t.right(20)
    t.forward(100) 
    t.right(20) 
    t.forward(100) 
    t.right(20)
    t.forward(100) 
    t.right(20)
    t.forward(100) 
    t.right(20)

    t.right(10) # Rotate for next pattern

turtle.done()


