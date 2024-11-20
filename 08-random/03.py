import random
import tkinter as tk

pocet = int(input("Zadaj počet jednotiek: "))

canvas = tk.Canvas(width=500, height=400)
canvas.pack()


def jednotka(x, y):
    x = random.randint(3, 500-33)
    y = random.randint(3, 400-73)
    random_farba = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown"])
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=random_farba)
    canvas.create_rectangle(x+10, y, x+20, y+10, fill=random_farba)
    canvas.create_rectangle(x+10, y+10, x+20, y+20, fill=random_farba)
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill=random_farba)
    canvas.create_rectangle(x+10, y+30, x+20, y+40, fill=random_farba)
    canvas.create_rectangle(x+10, y+40, x+20, y+50, fill=random_farba)
    canvas.create_rectangle(x+10, y+50, x+20, y+60, fill=random_farba)
    canvas.create_rectangle(x, y+60, x+10, y+70, fill=random_farba)
    canvas.create_rectangle(x+10, y+60, x+20, y+70, fill=random_farba)
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill=random_farba)

for _ in range(pocet):
    random_farba = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown"])
    jednotka(10, 10)


tk.mainloop()