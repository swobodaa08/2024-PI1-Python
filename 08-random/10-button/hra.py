import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x500")
pokus = 0
cisloPC = random.randint(0, 9)


def update():
    global pokus, cisloPC
    cisloJA = int(entry.get())
    if cisloJA < cisloPC:
        label.config(text = "Dal si menšie číslo")
        pokus += 1
    elif cisloJA > cisloPC:
        label.config(text = "Dal si väčšie číslo")
        pokus += 1
    else:
        pokus += 1
        messagebox.showinfo("Správne", f"Uhádol si! Číslo bolo {cisloPC}")
        messagebox.showinfo("Správne", f"Počet pokusov : {pokus}")

label = tk.Label(root, text="Uhádni číslo od 0 do 9")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Zadať", command=update)
button.pack()

root.mainloop()