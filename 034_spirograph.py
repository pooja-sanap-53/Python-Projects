# Draw a Spirograph
# Draw a number of circle of radius of 100


import turtle as t 
import random 

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    color = (r,g,b)
    return color

tim.shape("arrow")
# tim.pensize(10)
tim.speed ("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.color(random_color())
        tim.circle(100)

draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()