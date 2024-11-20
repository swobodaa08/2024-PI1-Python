import random
import tkinter as tk

pocet = int(input("Zadaj počet jednotiek: "))

canvas = tk.Canvas(width=500, height=400)
canvas.pack()


def jednotka(x, y):
    farba1 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba2 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba3 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba4 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba5 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba6 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba7 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba8 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba9 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])
    farba10 = random.choice(["red", "cyan", "magenta", "yellow", "green", "brown", "black", "pink"])

    x = random.randint(3, 500-33)
    y = random.randint(3, 400-73)
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=farba1, outline=farba1)
    canvas.create_rectangle(x+10, y, x+20, y+10, fill=farba2, outline=farba2)
    canvas.create_rectangle(x+10, y+10, x+20, y+20, fill=farba3, outline=farba3)
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill=farba4, outline=farba4)
    canvas.create_rectangle(x+10, y+30, x+20, y+40, fill=farba5, outline=farba5)
    canvas.create_rectangle(x+10, y+40, x+20, y+50, fill=farba6, outline=farba6)
    canvas.create_rectangle(x+10, y+50, x+20, y+60, fill=farba7, outline=farba7)
    canvas.create_rectangle(x, y+60, x+10, y+70, fill=farba8, outline=farba8)
    canvas.create_rectangle(x+10, y+60, x+20, y+70, fill=farba9, outline=farba9)
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill=farba10, outline=farba10)

for _ in range(pocet):
    jednotka(10, 10)


tk.mainloop()