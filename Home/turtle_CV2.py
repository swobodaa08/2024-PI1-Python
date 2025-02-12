import turtle
from tkinter import Entry

t = turtle.Turtle()

def terc(pocet):
    first = 15
    t.pencolor("yellow")
    t.dot(first)
    for _ in range(pocet):
        t.pencolor("yellow")
        first = first + 15
        t.dot(first)

entryy = Entry


terc(20)

turtle.exitonclick()