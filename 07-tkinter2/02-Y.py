import tkinter

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

def yko(x, y, farba):
    canvas.create_rectangle(x, y, x+10, y+10, fill=f"{farba}")
    canvas.create_rectangle(x, y+10, x+10, y+20, fill=f"{farba}")
    canvas.create_rectangle(x+40, y, x+50, y+10, fill=f"{farba}")
    canvas.create_rectangle(x+40, y+10, x+50, y+20, fill=f"{farba}")
    canvas.create_rectangle(x+10, y+20, x+20, y+30, fill=f"{farba}")
    canvas.create_rectangle(x+30, y+20, x+40, y+30, fill=f"{farba}")
    canvas.create_rectangle(x+20, y+30, x+30, y+40, fill=f"{farba}")
    canvas.create_rectangle(x+20, y+40, x+30, y+50, fill=f"{farba}")
    canvas.create_rectangle(x+20, y+50, x+30, y+60, fill=f"{farba}")
    canvas.create_rectangle(x+20, y+60, x+30, y+70, fill=f"{farba}")

def riadok_y(x, y, pocet, farba):
    for i in range(pocet):
        yko(x, y)
        x += 60

def riadky_y(x, y, pocet_riadkov, pocet_stlpcov, farba):
    for i in range(pocet_riadkov):
        riadok_y(x, y, pocet_stlpcov)
        y += 90

riadok_y(10, 10, 3, "red")
riadky_y(10, 100, 3, 5, "magenta")

tkinter.mainloop()