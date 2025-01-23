# SpameakCalc

import tkinter as tk

okno = tk.Tk()
canvas = tk.Canvas(okno, width=500, height=500)
okno.geometry("500x500")
okno.title("SpameakCalc")

first_number = ""
second_number = ""
operacia = 0
operacia_plus = 0
operacia_minus = 0
operacia_krat = 0
operacia_deleno = 0
vysledok = 0

# Definicia Cisel
def number1():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "1"
    else:
        second_number = second_number + "1"
    print(first_number)
    print(second_number)

def number2():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "2"
    else:
        second_number = second_number + "2"
    print(first_number)
    print(second_number)


def number3():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "3"
    else:
        second_number = second_number + "3"
    print(first_number)
    print(second_number)


def number4():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "4"
    else:
        second_number = second_number + "4"
    print(first_number)
    print(second_number)


def number5():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "5"
    else:
        second_number = second_number + "5"
    print(first_number)
    print(second_number)


def number6():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "6"
    else:
        second_number = second_number + "6"
    print(first_number)
    print(second_number)


def number7():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "7"
    else:
        second_number = second_number + "7"
    print(first_number)
    print(second_number)


def number8():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "8"
    else:
        second_number = second_number + "8"
    print(first_number)
    print(second_number)


def number9():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "9"
    else:
        second_number = second_number + "9"
    print(first_number)
    print(second_number)


def number0():
    global first_number, second_number, operacia
    if operacia == 0:
        first_number = first_number + "0"
    else:
        second_number = second_number + "0"
    print(first_number)
    print(second_number)

# Definicie Operacii 

def operation_plus():
    global first_number, second_number, operacia, operacia_plus
    if operacia == 0:
        operacia = operacia + 1
        operacia_plus = operacia_plus + 1
    print("+")

def operation_minus():
    global first_number, second_number, operacia, operacia_minus
    if operacia == 0:
        operacia = operacia + 1
        operacia_minus = operacia_minus + 1
    print("-")

def operation_multiple():
    global first_number, second_number, operacia, operacia_krat
    if operacia == 0:
        operacia = operacia + 1
        operacia_krat = operacia_krat + 1
    print("*")

def operation_divide():
    global first_number, second_number, operacia, operacia_deleno
    if operacia == 0:
        operacia = operacia + 1
        operacia_deleno = operacia_deleno + 1
    print("/")

# Definicia ostatne

def equal():
    global first_number, second_number, operacia, operacia_plus, operacia_minus, operacia_krat, operacia_deleno, vysledok
    cislo_1 = int(first_number)
    cislo_2 = int(second_number)
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
    first_number = ""
    second_number = ""
    print(f"= {vysledok}")

def backspace():
    global first_number, second_number, operacia
    operacia = 0
    print("")
    first_number = ""



b1 = tk.Button(okno, text="1", command=number1, font=("Heltvica", "30"))
b1.place(relx=0.20, rely=0.3)
b2 = tk.Button(okno, text="2", command=number2, font=("Heltvica", "30"))
b2.place(relx=0.50, rely=0.3)
b3 = tk.Button(okno, text="3", command=number3, font=("Heltvica", "30"))
b3.place(relx=0.80, rely=0.3)
b4 = tk.Button(okno, text="4", command=number4, font=("Heltvica", "30"))
b4.place(relx=0.2, rely=0.45)
b5 = tk.Button(okno, text="5", command=number5, font=("Heltvica", "30"))
b5.place(relx=0.5, rely=0.45)
b6 = tk.Button(okno, text="6", command=number6, font=("Heltvica", "30"))
b6.place(relx=0.8, rely=0.45)
b7 = tk.Button(okno, text="7", command=number7, font=("Heltvica", "30"))
b7.place(relx=0.2, rely=0.6)
b8 = tk.Button(okno, text="8", command=number8, font=("Heltvica", "30"))
b8.place(relx=0.5, rely=0.6)
b9 = tk.Button(okno, text="9", command=number9, font=("Heltvica", "30"))
b9.place(relx=0.8, rely=0.6)
b0 = tk.Button(okno, text="0", command=number0, font=("Heltvica", "30"))
b0.place(relx=0.5, rely=0.75)
b20 = tk.Button(okno, text="+", command=operation_plus, font=("Heltvica", "30"))
b20.place(relx=0.15, rely=0.9)
b30 = tk.Button(okno, text="-", command=operation_minus, font=("Heltvica", "30"))
b30.place(relx=0.30, rely=0.9)
b40 = tk.Button(okno, text="*", command=operation_multiple, font=("Heltvica", "30"))
b40.place(relx=0.45, rely=0.9)
b50 = tk.Button(okno, text="/", command=operation_divide, font=("Heltvica", "30"))
b50.place(relx=0.60, rely=0.9)
b60 = tk.Button(okno, text="=", command=equal, font=("Heltvica", "30"))
b60.place(relx=0.75, rely=0.9)
b70 = tk.Button(okno, text="DEL", command=backspace, font=("Heltvica", "30"))
b70.place(relx=0.90, rely=0.9)


okno.mainloop()