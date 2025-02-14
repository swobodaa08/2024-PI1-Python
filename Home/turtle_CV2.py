import turtle
import tkinter as tk

t = turtle.Turtle()
root = tk.Tk()
root.geometry("500x500")
farba1 = "blue"
farba2 = "yellow"

def terc(pocet, farba1, farba2):
    biggest = (pocet * 15) + 15
    for _ in range(pocet):
        biggest = biggest - 15
        t.pencolor(farba1)
        t.dot(biggest)
        biggest = biggest - 15
        print(biggest)
        t.pencolor(farba2)
        t.dot(biggest)
        if biggest == 15:
            break

def prekresli():
    farba1 = entry1.__getattribute__()
    farba2 = entry2.__getattribute__()
    farba1 = str
    farba2 = str
    terc(20, farba1, farba2)

terc(20, farba1, farba2)

label = tk.Label()
entry1 = tk.Entry(root).pack()
entry2 = tk.Entry(root).pack()
button = tk.Button(root, text="Prekresli", command=prekresli).pack()


turtle.exitonclick()