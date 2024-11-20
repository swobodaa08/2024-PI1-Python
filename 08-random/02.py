import random
import tkinter as tk

dlzka = int(input("Zadaj dlzku stvorca: "))
stvorce = int(input("Kolko stvorcov chces vygenerovat: "))

canvas = tk.Canvas(width=500, height=400)
canvas.pack()

for i in range(stvorce):
    x = random.randint(3, 497 - dlzka)
    y = random.randint(3, 397 - dlzka)
    canvas.create_rectangle(x, y, x+dlzka, y+dlzka, fill=random.choice(["red", "green", "blue", "magenta", "cyan", "yellow"]))

tk.mainloop()