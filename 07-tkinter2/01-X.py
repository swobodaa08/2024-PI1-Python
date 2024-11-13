import tkinter as tk

canvas = tk.Canvas(width=600, height=600) # Zadám šírku a výšku strán
canvas.pack()

def xko(x, y):  # definicia funkcie, xko nazov (to davame my), () Sú takzvané parametre funkcie


    canvas.create_rectangle(x, y, x+10, y+10, fill="blue")
    canvas.create_rectangle(x, y+10, x+10, y+20, fill="blue")
    canvas.create_rectangle(x+10, y+30, x+20, y+20, fill="blue")
    canvas.create_rectangle(x+40, y+30, x+30, y+20, fill="blue")
    canvas.create_rectangle(x+50, y+20, x+40, y+10, fill="blue")
    canvas.create_rectangle(x+50, y+10, x+40, y, fill="blue")
    canvas.create_rectangle(x+30, y+40, x+20, y+30, fill="blue")
    canvas.create_rectangle(x+10, y+50, x+20, y+40, fill="blue")
    canvas.create_rectangle(x+30, y+50, x+40, y+40, fill="blue")
    canvas.create_rectangle(x+40, y+60, x+50, y+50, fill="blue")
    canvas.create_rectangle(x+40, y+70, x+50, y+60, fill="blue")
    canvas.create_rectangle(x, y+60, x+10, y+50, fill="blue")
    canvas.create_rectangle(x, y+70, x+10, y+60, fill="blue")



def riadok_x(x, y, pocet):
    for i in range(pocet):
        xko(x, y)
        x += 60


def riadky_x(x, y, pocet_riadkov, pocet_stlpcov):
    for i in range(pocet_riadkov):
        riadok_x(x, y, pocet_stlpcov)
        y += 90

# xko(10, 10) volanie funkcie
# xko(70, 10)
# xko(130, 10)

# x = 10
# y = 10
# pocet = 5

# for i in range(3):
#     for i in range(pocet):
#         xko(x, y)
#         x += 60
#     x = 10
#     y += 80

xko(10, 10)
riadok_x(10, 100, 3)
riadky_x(10, 190, 3, 5)

tk.mainloop()