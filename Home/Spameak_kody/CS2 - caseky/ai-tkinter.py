import tkinter as tk
import random

# Predmety v bedni (príklady skínov)
items = [
    "P90 | Asiimov",
    "AK-47 | Redline",
    "AWP | Dragon Lore",
    "M4A4 | Howl",
    "Desert Eagle | Blaze",
    "USP-S | Orion",
    "Glock-18 | Water Elemental",
    "No item (Unlucky)"
]

# Funkcia na simulovanie otvárania bedne
def open_case():
    item = random.choice(items)
    if item == "No item (Unlucky)":
        result_label.config(text="Nezískal si žiadny vzácny predmet. Skús to znova.")
    else:
        result_label.config(text=f"Gratulujeme! Získal si: {item}")

# Vytvárame hlavné okno aplikácie
root = tk.Tk()
root.title("Simulátor Otvárania Bedne")
root.geometry("400x300")  # Veľkosť okna

# Tlačidlo na otvorenie bedne
open_button = tk.Button(root, text="Otvor Bedňu", font=("Arial", 14), command=open_case)
open_button.pack(pady=20)

# Label na zobrazenie výsledku
result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

# Spustenie hlavnej slučky aplikácie
root.mainloop()