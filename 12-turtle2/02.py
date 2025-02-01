import turtle, random

while True:
    try:
        velkost = int(input("Zadaj velkosť domu(10-60): "))
        if 10 <= velkost <= 60:
            break
        else:
            print("Neplatná hodnota!")
    except ValueError:
        print("Zadaj číslo...")

while True:
    try:
        pocet_domov_v_ulici = int(input("Zadaj počet domov v jednej ulici(5-20): "))
        if 5 <= pocet_domov_v_ulici <= 20:
            break
        else:
            print("Neplatná hodnota!")
    except ValueError:
        print("Zadaj číslo...")

while True:
    try:
        pocet_ulic = int(input("Zadaj počet ulíc(5-15): "))
        if 5 <= pocet_ulic <= 15:
            break
        else:
            print("Neplatná hodnota!")
    except ValueError:
        print("Zadaj číslo...")

t = turtle.Turtle()
x = -400
y = 250
t.hideturtle()
t.speed(0)

turtle.delay(0)

def domcek(velkost):
    global x, y
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    t.fd(velkost)
    t.lt(90)
    t.fd(velkost)
    t.lt(90)
    t.fd(velkost)
    t.lt(90)
    t.fd(velkost)
    t.end_fill()
    t.fillcolor('black')
    t.begin_fill()
    t.bk(velkost)
    t.lt(150)
    t.fd(velkost)
    t.rt(120)
    t.fd(velkost)
    t.rt(120)
    t.fd(velkost)
    t.end_fill()
    t.lt(180)
    t.fd(velkost/2)
    t.rt(90)
    t.penup()
    t.fd(velkost/4)
    t.pendown()
    t.pensize(3)
    t.fd(velkost/2)
    t.rt(90)
    t.fd(velkost/4)
    t.rt(90)
    t.fd(velkost/2)
    t.rt(90)
    t.fd(velkost/2)
    t.rt(90)
    t.fd(velkost/4)
    t.rt(90)
    t.fd(velkost/2)
    t.penup()
    t.lt(90)
    t.fd(velkost/4)
    t.lt(90)
    t.pendown()
    t.fd(velkost/2)
    t.lt(90)
    t.fd(velkost/4)
    t.rt(90)

def ulica(pocet_domov_v_ulici):
    global x
    for _ in range(pocet_domov_v_ulici):
        domcek(velkost)
        x = x + (velkost + 10)

def dedina(pocet_ulic, pocet_domov_v_ulici):
    global x, y
    for _ in range(pocet_ulic):
        ulica(pocet_domov_v_ulici)
        x = -400
        y = y - (velkost * 2)

dedina(pocet_ulic, pocet_domov_v_ulici)

turtle.mainloop()