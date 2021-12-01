# Draw a triangle, square, pentagon, hexagoan, heptagon, octagaon, nonagon and decagon
# There are two solutions run any one at a time

from turtle import Turtle,Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")
colors = ["magenta", "navy", "lime green",  "deep sky blue", "orange red", "dark magenta", "gold"]

# first solution for beginners 
def triangle():
    for i in range(3):
        tim.right(120)
        tim.forward(100)
    print(tim)

def square():
    for i in range(4):
        tim.right(90)
        tim.forward(100)
    print(tim)

def pentagon():
    for i in range(5):
        tim.right(72)
        tim.forward(100)
    print(tim)

def hexagon():
    for i in range(6):
        tim.right(60)
        tim.forward(100)
    print(tim)

def heptagon():
    for i in range(7):
        tim.right(51.43)
        tim.forward(100)
    print(tim)

def octagon():
    for i in range(8):
        tim.right(45)
        tim.forward(100)
    print(tim)

def nonagon():
    for i in range(9):
        tim.right(40)
        tim.forward(100)
    print(tim)

def decagon():
    for i in range(10):
        tim.right(36)
        tim.forward(100)
    print(tim)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

# second solution for indermediate

def draw_shapes(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)
    print(tim)

for i in range(3,11):
    tim.color(colors[randint(0,7)])
    draw_shapes(i)

screen = Screen()
screen.exitonclick()
