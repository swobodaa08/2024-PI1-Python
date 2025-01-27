# SpameakCalc

import tkinter as tk

okno = tk.Tk()
canvas = tk.Canvas(okno, width=500, height=500)
canvas.pack()
okno_width = 500
okno_height = 600
okno.geometry(f"{okno_width}x{okno_height}")
okno.title("SpameakCalc")

x = ""
y = ""
first_number = ""
next_numbers = ""
operacia = 0
operacia_plus = 0
operacia_minus = 0
operacia_krat = 0
operacia_deleno = 0
vysledok = 0
canvas.create_rectangle(10,30,490,120, fill="cyan")
# Definicia Cisel
def number1():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "1"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "1"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)

def number2():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "2"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "2"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number3():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "3"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "3"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number4():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "4"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "4"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number5():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "5"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "5"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number6():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "6"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "6"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number7():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "7"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "7"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number8():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "8"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "8"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number9():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "9"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "9"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)


def number0():
    global first_number, next_numbers, operacia, x, y
    if operacia == 0:
        x = x + "0"
        first_number = int(x)
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number}", font=("Heltvica", "21", "bold"))
    else:
        y = y + "0"
        next_numbers = int(y)
        if operacia_krat == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} x {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_deleno == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} / {next_numbers}", font=("Heltvica", "21", "bold"))
        elif operacia_minus == 1:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} - {next_numbers}", font=("Heltvica", "21", "bold"))
        else:
            canvas.delete
            canvas.create_rectangle(10,30,490,120, fill="cyan")
            canvas.create_text(250, 80, text=f"{first_number} + {next_numbers}", font=("Heltvica", "21", "bold"))
    print(first_number)
    print(next_numbers)

# Definicie Operacii 

def operation_plus():
    global first_number, next_numbers, operacia, operacia_plus
    if operacia == 0:
        operacia = operacia + 1
        operacia_plus = operacia_plus + 1
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number} +", font=("Heltvica", "21", "bold"))
    print("+")

def operation_minus():
    global first_number, next_numbers, operacia, operacia_minus
    if operacia == 0:
        operacia = operacia + 1
        operacia_minus = operacia_minus + 1
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number} -", font=("Heltvica", "21", "bold"))
    print("-")

def operation_multiple():
    global first_number, next_numbers, operacia, operacia_krat
    if operacia == 0:
        operacia = operacia + 1
        operacia_krat = operacia_krat + 1
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number} x", font=("Heltvica", "21", "bold"))
    print("*")

def operation_divide():
    global first_number, next_numbers, operacia, operacia_deleno
    if operacia == 0:
        operacia = operacia + 1
        operacia_deleno = operacia_deleno + 1
        canvas.delete
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{first_number} /", font=("Heltvica", "21", "bold"))
    print("/")

# Definicia ostatne

def equal():
    global first_number, next_numbers, operacia, operacia_plus, operacia_minus, operacia_krat, operacia_deleno, vysledok, x, y
    cislo_1 = first_number
    cislo_2 = next_numbers
    if operacia_plus == 1:
        vysledok = cislo_1 + cislo_2
    elif operacia_minus == 1:
        vysledok = cislo_1 - cislo_2
    elif operacia_krat == 1:
        vysledok = cislo_1 * cislo_2
    elif operacia_deleno == 1:
        vysledok = cislo_1 / cislo_2
    else:
        vysledok = "Math Error"
    operacia = 0
    operacia_deleno = 0
    operacia_krat = 0
    operacia_plus = 0
    operacia_minus = 0
    x = ""
    y = ""
    first_number = ""
    next_numbers = ""
    print(f"= {vysledok}")
    if vysledok > 9999999999999999999999999:
        canvas.delete("all")    
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text="Too big number", font=("Heltvica", "25", "bold"))
    else:
        canvas.delete("all")    
        canvas.create_rectangle(10,30,490,120, fill="cyan")
        canvas.create_text(250, 80, text=f"{vysledok}", font=("Heltvica", "25", "bold"))

def backspace():
    global first_number, next_numbers, operacia, x, y
    operacia = 0
    print("")
    first_number = ""
    next_numbers = ""
    x = ""
    y = ""
    canvas.delete("all")
    canvas.create_rectangle(10,30,490,120, fill="cyan")



b1 = tk.Button(okno, text="1", command=number1, font=("Heltvica", "30"))
b1.place(relx=0.15, rely=0.25)
b2 = tk.Button(okno, text="2", command=number2, font=("Heltvica", "30"))
b2.place(relx=0.45, rely=0.25)
b3 = tk.Button(okno, text="3", command=number3, font=("Heltvica", "30"))
b3.place(relx=0.75, rely=0.25)
b4 = tk.Button(okno, text="4", command=number4, font=("Heltvica", "30"))
b4.place(relx=0.15, rely=0.4)
b5 = tk.Button(okno, text="5", command=number5, font=("Heltvica", "30"))
b5.place(relx=0.45, rely=0.4)
b6 = tk.Button(okno, text="6", command=number6, font=("Heltvica", "30"))
b6.place(relx=0.75, rely=0.4)
b7 = tk.Button(okno, text="7", command=number7, font=("Heltvica", "30"))
b7.place(relx=0.15, rely=0.55)
b8 = tk.Button(okno, text="8", command=number8, font=("Heltvica", "30"))
b8.place(relx=0.45, rely=0.55)
b9 = tk.Button(okno, text="9", command=number9, font=("Heltvica", "30"))
b9.place(relx=0.75, rely=0.55)
b0 = tk.Button(okno, text="0", command=number0, font=("Heltvica", "30"))
b0.place(relx=0.45, rely=0.7)
b20 = tk.Button(okno, text="+", command=operation_plus, font=("Heltvica", "30"))
b20.place(relx=0.08, rely=0.85)
b30 = tk.Button(okno, text="-", command=operation_minus, font=("Heltvica", "30"))
b30.place(relx=0.33, rely=0.85)
b40 = tk.Button(okno, text="*", command=operation_multiple, font=("Heltvica", "30"))
b40.place(relx=0.58, rely=0.85)
b50 = tk.Button(okno, text="/", command=operation_divide, font=("Heltvica", "30"))
b50.place(relx=0.83, rely=0.85)
b60 = tk.Button(okno, text="=", command=equal, font=("Heltvica", "30"))
b60.place(relx=0.75, rely=0.7)
b70 = tk.Button(okno, text="DEL", command=backspace, font=("Heltvica", "30"))
b70.place(relx=0.09, rely=0.7)


okno.mainloop()
