import turtle
import random

screen = turtle.Screen()

pen = turtle.Turtle()

pen.speed(45)


for _ in range(2000):
    pen.color("red")
    pen.forward(8)
    pen.left(3.14)

screen.exitonclick()