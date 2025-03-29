# # uzivatel zada celu vetu a program vetu rozdeli na slova, ktore vypise nahodnou farbou na nahodnom mieste
# # aj pismenka zo slov vypise nahodnymi farbami
# # nastudovat retazce

# import tkinter as tk
# import random

# veta = input("Zadaj vetu: ")
# slova = []
# slova = slova + veta.split(" ")

# canvas = tk.Canvas(width=800, height=600)
# canvas.pack()

# for slovo in slova:
#     x = random.randint(10, 700)
#     y = random.randint(10, 500)
#     for pismeno in slovo:
#         r = f"{random.randint(0, 255):02x}"
#         g = f"{random.randint(0, 255):02x}"
#         b = f"{random.randint(0, 255):02x}"
#         canvas.create_text(x, y, text=slovo, font=("Heltvica", 24, "bold"), fill=f"#{r}{g}{b}")

# canvas.mainloop()


import tkinter as tk
import random

def random_color():
    """Generuje náhodnú farbu v hexadecimálnom formáte."""
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# Získanie vstupnej vety
veta = input("Zadaj vetu: ")
slova = veta.split(" ")

# Nastavenie canvasu
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Spracovanie slov a písmen
for slovo in slova:
    x = random.randint(50, 750)  # Náhodná pozícia slova
    y = random.randint(50, 550)
    
    pos_x = x  # Počiatočná pozícia pre prvé písmeno

    for pismeno in slovo:
        color = random_color()  # Každé písmeno dostane inú farbu
        canvas.create_text(pos_x, y, text=pismeno, font=("Helvetica", 24, "bold"), fill=color)
        pos_x += 20  # Posunutie ďalšieho písmena doprava

root.mainloop()