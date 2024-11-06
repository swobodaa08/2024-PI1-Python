import tkinter

canvas = tkinter.Canvas(width=320, height=320) # Zadám šírku a výšku strán
canvas.pack()

# Prvé písmeno S
    # Horna hrana
canvas.create_rectangle(20,20,30,30, fill="red")
canvas.create_rectangle(30,20,40,30, fill="blue")
canvas.create_rectangle(40,20,50,30, fill="magenta")
canvas.create_rectangle(50,20,60,30, fill="yellow")
    # lava strana
canvas.create_rectangle(10,30,20,40, fill="red")
canvas.create_rectangle(10,40,20,50, fill="yellow")
    # Stredna hrana
canvas.create_rectangle(20,50,30,60, fill="green")
canvas.create_rectangle(30,50,40,60, fill="orange")
canvas.create_rectangle(40,50,50,60, fill="cyan")
    # Prava hrana
canvas.create_rectangle(50,60,60,70, fill="red")
canvas.create_rectangle(50,70,60,80, fill="yellow")
    # Spodna hrana
canvas.create_rectangle(20,80,30,90, fill="cyan")
canvas.create_rectangle(30,80,40,90, fill="red")
canvas.create_rectangle(40,80,50,90, fill="cyan")
canvas.create_rectangle(10,80,20,90, fill="green")

# Druhé písmeno S
    # Horna hrana
canvas.create_rectangle(80,20,90,30, fill="red")
canvas.create_rectangle(90,20,100,30, fill="cyan")
canvas.create_rectangle(100,20,110,30, fill="red")
canvas.create_rectangle(110,20,120,30, fill="cyan")
    # lava strana
canvas.create_rectangle(70,30,80,40, fill="red")
canvas.create_rectangle(70,40,80,50, fill="cyan")
    # Stredna hrana
canvas.create_rectangle(80,50,90,60, fill="red")
canvas.create_rectangle(90,50,100,60, fill="cyan")
canvas.create_rectangle(100,50,110,60, fill="red")
    # Prava hrana
canvas.create_rectangle(110,60,120,70, fill="cyan")
canvas.create_rectangle(110,70,120,80, fill="red")
    # Spodna hrana
canvas.create_rectangle(80,80,90,90, fill="cyan")
canvas.create_rectangle(90,80,100,90, fill="red")
canvas.create_rectangle(100,80,110,90, fill="cyan")
canvas.create_rectangle(70,80,80,90, fill="red")

tkinter.mainloop()