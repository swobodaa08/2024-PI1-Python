import tkinter as tk, random

fdraw = open("19-txt2/tvary.txt", "r", encoding="UTF-8")

canvas = tk.Canvas(width=800, height=800)
canvas.pack()

riadok = fdraw.readline()
print(riadok)
tvar, x1, y1, x2, y2, farba = riadok.split()
print(tvar)
print(x1)
print(y1)
print(x2)
print(y2)
print(farba)

if tvar == "oval":
    canvas.create_oval(x1, y1, x2, y2, fill=farba)
elif tvar == "rectangle":
    canvas.create_rectangle(x1, y1, x2, y2, fill=farba)

def draw():
    pass
draw()

fdraw.close()
tk.mainloop()