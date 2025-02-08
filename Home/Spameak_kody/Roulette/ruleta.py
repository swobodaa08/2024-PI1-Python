import tkinter as tk
import time

canvas = tk.Canvas()
canvas.pack()


canvas.create_rectangle(50, 50, 200, 200)
time.sleep(2)
canvas.create_rectangle(80, 80, 300, 300)


tk.mainloop()