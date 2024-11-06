import tkinter

canvas = tkinter.Canvas(width=320, height=320) # Zadám šírku a výšku strán
canvas.pack()

canvas.create_rectangle(10,10,110,110, fill="red")
canvas.create_text(60,60, text="Ahoj")
canvas.create_rectangle(110,110,210,210, fill="#0088cc")
canvas.create_text(160,160, text="Ahoj")
canvas.create_rectangle(210,210,310,310, fill="magenta")
canvas.create_text(260,260, text="Ahoj")
canvas.create_rectangle(10,210,110,310, fill="yellow")
canvas.create_text(60,260, text="Ahoj")
canvas.create_rectangle(210,10,310,110, fill="cyan")
canvas.create_text(260,60, text="Ahoj")




tkinter.mainloop()