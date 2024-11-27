import tkinter as tk
import random


while True:
    try:
        pocet_kruhov = int(input("Zadaj počet štvorcov: "))
        if 10 <= pocet_kruhov <= 10000:
            break
        else:
            print("Počet kruhov nemôže byť menej jak 10 a ani viac jak 10000")
    except ValueError:
        print("Zadaj číslo")

sirka = 500
vyska = 500

canvas = tk.Canvas(width=sirka, height=vyska)
canvas.pack()

for _ in range(pocet_kruhov):
    x = random.randint(13, 487)
    y = random.randint(13, 487)
    # if x < (sirka/2)+5 and y < (vyska/2)+5: # Zlozena podmienka, pouzijeme viac vlastnosti
    #     # medzi zlozene podmienky vkladame logicke operatory (and = a zároveň) alebo (or = alebo)
    #     farba = "blue"
    # elif x < (sirka/2)+5 and y > (vyska/2)-5:
    #     farba = "lime"
    # elif x > (sirka/2)-5 and y < (vyska/2)+5:
    #     farba = "red"
    # elif x > (sirka/2)-5 and y > (vyska/2)-5:
    #     farba = "yellow"

    if x < sirka / 2:
        if y < (vyska/2)+5:
            farba = "blue"
        else:
            farba = "lime"

    else:
        if y < (vyska/2)+5:
            farba = "red"
        else:
            farba = "yellow"

    canvas.create_oval(x, y, x+10, y+10, fill=farba, width=0)

tk.mainloop()