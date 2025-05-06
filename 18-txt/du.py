import tkinter as tk
import random


root = tk.Tk()
root.title("Náhodné tvary")
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()


tvary = ["o", "r", "l"] 


def farba():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def nakresli(tvar, x, y, f):
    if tvar == "o":
        canvas.create_oval(x, y, x+random.randint(30, 70), y+random.randint(30, 70), fill=f)
    elif tvar == "r":
        canvas.create_rectangle(x, y, x+random.randint(40, 80), y+random.randint(30, 60), fill=f)
    elif tvar == "l":
        canvas.create_line(
            x, y,
            x + random.randint(20, 60), y + random.randint(80, 180),
            fill=f)


with open("18-txt/tvary.txt", "w", encoding="utf-8") as subor:
    for _ in range(10):
        t = random.choice(tvary)
        x = random.randint(50, 750)
        y = random.randint(50, 750)
        f = farba()
        nakresli(t, x, y, f)
        print(t, x, y, f, file=subor)

root.mainloop()