# Draw a Etch a Sketch

from turtle import Turtle,Screen

tim = Turtle()
tim.write('''Hii, I am turtle.
Follow the below commands to draw.
W = forwards
S = backwards
A = Counter Clockwise
D = Clockwise
C - clear the screen and return to home ''', align="center")

tim.color("chocolate")
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(90)

def move_anticlockwise():
    tim.left(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
