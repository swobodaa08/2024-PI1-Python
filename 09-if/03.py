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

    if (sirka / 4) < x+10 < (sirka / 4*3) and (vyska / 4) < y+10 < (vyska / 4*3):
        canvas.create_oval(x, y, x+10, y+10, fill="black", width=0)

    else:
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