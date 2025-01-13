#import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("red")

def draw_square(turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

#Challenge 1 - Draw a square
draw_square(tim)

#Challenge 2 - Use dashed lines
for _ in range(15):
    tim.back(10)
    tim.penup()
    tim.back(10)
    tim.pendown()

print(tim.pos())

d




screen = Screen()
screen.bgcolor("black")
screen.exitonclick()

