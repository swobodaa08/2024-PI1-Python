import tkinter as tk
import random

while True:
    try:
        stvorce = int(input("Zadaj počet štvorcov: "))
        if 1 <= stvorce <= 500:
            break
        else:
            print("Počet kôl nemôže byť menej jak 1 a ani viac jak 500")
    except ValueError:
        print("Zadaj číslo")

while True:
    try:
        sirka = int(input("Zadaj šírka okna: "))
        if 100 <= sirka <= 1920:
            break
        else:
            print("Šírka nemôže byť menej jak 100 a ani viac jak 1920")
    except ValueError:
        print("Zadaj číslo")

while True:
    try:
        vyska = int(input("Zadaj výšku okna: "))
        if 100 <= vyska <= 1080:
            break
        else:
            print("Výška nemôže byť menej jak 100 a ani viac jak 1080")
    except ValueError:
        print("Zadaj číslo")



canvas = tk.Canvas(height=vyska, width=sirka)
canvas.pack()


for _ in range(stvorce):
    a = random.randint(1, 30)
    x = random.randint(3, sirka-3-a)
    y = random.randint(3, vyska-3-a)
    if a <= 10:
        farba = "red"
    elif a <= 20:
        farba = "green"
    else:
        farba = "blue"
    canvas.create_rectangle(x, y, x + a, y + a, fill=farba, width=0)


tk.mainloop()