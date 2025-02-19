# Logo maker by spaMeak (2025)

import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.title("LogoMaker - Svoboda")
root.geometry(f"{screen_width}x{screen_height}")
canvas = tk.Canvas(root, width=1920, height=1080)

def nakresli(event):
    radius = velkosť.get()
    x1 = event.x - radius
    y1 = event.y - radius
    x2 = event.x + radius
    y2 = event.y + radius

    canvas.create_oval(x1, y1, x2, y2)

def circle():
    canvas.bind("<ButtonPress>", nakresli)

def square():
    pass


kruh = tk.Button(text="O", command=circle).pack()
stvorec = tk.Button(text="D", command=square).pack()
velkosť = tk.Scale(root, orient="horizontal", from_=5, to=40, length=140).pack()




root.mainloop()