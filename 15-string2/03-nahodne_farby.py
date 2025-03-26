import tkinter as tk
import random

canvas = tk.Canvas(width=800, height=600)
canvas.pack()
for i in range(10):
    x = random.randint(3, 700)
    y = random.randint(3, 500)
    r = f"{random.randint(0, 255):02x}"
    g = f"{random.randint(0, 255):02x}"
    b = f"{random.randint(0, 255):02x}"
    canvas.create_rectangle(x, y, x+40, y+40, fill=f"#{r}{g}{b}")
tk.mainloop()