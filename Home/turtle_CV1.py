import turtle
import tkinter as tk
import random

farby = ("blue", "red", "gold", "orange", "pink")

def slnko(pocet, velkost):
    t.pencolor(random.choice(farby))
    t.dot(velkost)
    vypocet = 360 / pocet
    for _ in range(pocet):
        t.fd(velkost)
        t.lt(180)
        t.fd(velkost)
        t.lt(180)
        t.lt(vypocet)

def new_sun():
    t.clear()
    slnko(random.randint(3, 20), random.randint(20, 100))


t = turtle.Turtle()
t.pensize(10)
turtle.delay(0)
t.speed(0)
slnko(20, 80)
tk.Button(text="Nové slnko", command=new_sun).pack()

turtle.done()