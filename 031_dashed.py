# Draw a dashed line using turtle
# There are two solutions run any one at a time

from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")

# first solution
for i in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)
print(tim)

# second solution 
for i in range(20):
    tim.pencolor("white")
    tim.forward(10)
    tim.pencolor("black")
    tim.forward(10)
print(tim)

screen = Screen()
screen.exitonclick()
