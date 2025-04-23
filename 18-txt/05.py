import tkinter as tk

canvas = tk.Canvas()
canvas.pack()


fbody = open("18-txt/body.txt", "r")
for body in fbody:
    # print(body)
    x, y = (body.split(" "))
    x = int(x)
    y = int(y)
    canvas.create_oval(x-5, y-5, x+5, y+5)
tk.mainloop()