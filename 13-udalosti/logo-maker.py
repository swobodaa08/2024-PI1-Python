# Logo maker by spaMeak (2025)

import tkinter as tk


root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.attributes("-fullscreen", True)
root.title("LogoMaker - Svoboda")
root.geometry(f"{screen_width}x{screen_height}")
canvas = tk.Canvas(root)

def vykresli(event):
    radius = size.get()
    x1 = event.x - radius
    y1 = event.y - radius
    x2 = event.x + radius
    y2 = event.y + radius
    canvas.create_oval(x1, y1, x2, y2, fill="black")

def square():
    pass


kruh = tk.Button(text="O", font=("30"))
kruh.bind("<ButtonPress>", vykresli)
kruh.place(x=20, y=10)
kruh.pack()

stvorec = tk.Button(text="D", command=square)
stvorec.place(x=40, y=10)
stvorec.pack()

size = tk.Scale(root, orient="horizontal", from_=5, to=40, length=140)
size.place(x=90, y=100)
size.pack()




root.mainloop()