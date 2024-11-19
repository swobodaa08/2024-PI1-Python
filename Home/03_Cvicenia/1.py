import tkinter
import random

canvas = tkinter.Canvas(bg="navy", width=500, height=500)
canvas.pack()
n = random.randint(20, 100)

for i in range(n):
    x = random.randint(0,500)
    y = random.randint(0,500)
    canvas.create_text(x, y, text="*", fill="yellow")


tkinter.mainloop()