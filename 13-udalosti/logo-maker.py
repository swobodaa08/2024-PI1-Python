# Logo maker by spaMeak (2025)

import tkinter as tk

def circle(event):
    radius = size.get()
    color = farba.get()
    x1, y1 = event.x - radius, event.y - radius
    x2, y2 = event.x + radius, event.y + radius
    if color == "":
        color = "black"
    canvas.create_oval(x1, y1, x2, y2, fill=f"{color}", outline=f"{color}")

def circle_bind():
    canvas.bind("<ButtonPress>", circle)
    kruh.config(bg="green")
    stvorec.config(bg="white")
    pero.config(bg="white")

def square(event):
    radius = size.get()
    color = farba.get()
    x1, y1 = event.x - radius, event.y - radius
    x2, y2 = event.x + radius, event.y + radius
    if color == "":
        color = "black"
    canvas.create_rectangle(x1, y1, x2, y2, fill=f"{color}", outline=f"{color}")

def square_bind():
    canvas.bind("<ButtonPress>", square)
    kruh.config(bg="white")
    stvorec.config(bg="green")
    pero.config(bg="white")

def pen(event):
    radius = size.get()
    color = farba.get()
    x1, y1 = event.x - radius, event.y - radius
    x2, y2 = event.x + radius, event.y + radius
    if color == "":
        color = "black"
    canvas.create_oval(x1, y1, x2, y2, fill=f"{color}", outline=f"{color}")

def pen_bind():
    canvas.bind("<B1-Motion>", pen)
    kruh.config(bg="white")
    stvorec.config(bg="white")
    pero.config(bg="green")

def eraser_bind():
    canvas.delete("all")
    kruh.config(bg="white")
    stvorec.config(bg="white")
    pero.config(bg="white")

def zavriet(event):
    root.destroy()
    

# Hlavne Okno
root = tk.Tk()
root.attributes("-fullscreen", True)
root.title("LogoMaker - Svoboda")

# info
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Velkost okna
root.geometry(f"{screen_width}x{screen_height}")
root.bind("<Escape>", zavriet)

# Canvas platno
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="white")
canvas.pack(fill="both", expand=True)

# Tlačidlá
frame = tk.Frame(canvas)
frame.pack(side="top", pady=10)

kruh = tk.Button(frame, text="⚪", fg="black", font=("Arial", 12), command=circle_bind)
kruh.pack(side="left", padx=10)

stvorec = tk.Button(frame, text="⬜", fg="black", font=("Heltvica", 12), command=square_bind)
stvorec.pack(side="left", padx=10)

pero = tk.Button(frame, text="✎", fg="black", font=("Heltvica", 12), command=pen_bind)
pero.pack(side="left", padx=10)

guma = tk.Button(frame, text="🗞️", fg="black", font=("Arial", 12), command=eraser_bind)
guma.pack(side="left", padx=10)

farba = tk.Entry(frame)
farba.pack()

# Posuvník pre veľkosť
size = tk.Scale(frame, orient="horizontal", from_=5, to=90, length=240)
size.pack()

root.mainloop()