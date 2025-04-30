import tkinter as tk, random

ftvary = open("19-txt2/tvary.txt", "w", encoding="UTF-8")

moznosti = "oval", "rectangle", "line"

def choice():
    tvar = random.choice(moznosti)

    x1 = random.randint(3, 797)
    y1 = random.randint(3, 797)
    x2 = random.randint(3, 797)
    y2 = random.randint(3, 797)

    farba = f"#{random.randrange(256**3):06x}"

    print(tvar, x1, y1, x2, y2, farba, file=ftvary)

for _ in range(2):
    choice()

ftvary.close()