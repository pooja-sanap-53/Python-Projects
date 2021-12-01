# Draw a square of distance 100 using turtle

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan")

for i in range(4):
    timmy.forward(100)
    timmy.right(90)
    
my_screen = Screen()
my_screen.exitonclick()