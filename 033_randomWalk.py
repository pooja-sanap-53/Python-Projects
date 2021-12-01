# Draw a random walk 
# Each time turtle covers equal distance but it can be any random direction east west north or south 
# There are two solutions run any one at a time

from turtle import Turtle,Screen
from random import choice

tim = Turtle()
tim.shape("arrow")
tim.color("chocolate")
tim.pensize(10)
tim.speed = "fastest"
colors = ["magenta", "navy", "lime green",  "deep sky blue", "orange red", "dark magenta", "gold"]
direction = [0, 90, 180 , 270 ]

# first solution - for beginners
for i in range(100):    
    tim.color(choice(colors))
    tim.right(choice(direction))
    tim.forward(20)


# second solution - for intermediaters
for i in range(100):
    tim.setheading(choice(direction))
    tim.color(choice(colors))
    tim.forward(20)

screen = Screen()
screen.exitonclick()
