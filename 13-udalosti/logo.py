import tkinter as tk

# Vytvorenie hlavného okna
root = tk.Tk()
root.attributes("-fullscreen", True)  # Celá obrazovka
root.title("LogoMaker - Svoboda")

# Získanie veľkosti obrazovky
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Plátno na kreslenie
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white")
canvas.pack(fill="both", expand=True)

# Posuvník na nastavenie veľkosti
size = tk.Scale(root, orient="horizontal", from_=5, to=40, length=140)
size.pack()

# Funkcia na kreslenie kruhu
def vykresli(event):
    radius = size.get()
    x1, y1 = event.x - radius, event.y - radius
    x2, y2 = event.x + radius, event.y + radius
    canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")

# Pripojenie kreslenia k plátnu
canvas.bind("<Button-1>", vykresli)  # Kliknutie myšou kreslí kruh

# Ukončenie aplikácie klávesom ESC
def zavriet(event):
    root.destroy()

root.bind("<Escape>", zavriet)

root.mainloop()
