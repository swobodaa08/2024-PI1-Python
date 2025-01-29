import turtle

t = turtle.Turtle()

t.hideturtle()

pocet = 3
dlzka = 30

def schody(pocet, dlzka):
    for _ in range(pocet):
        t.forward(dlzka)
        t.right(90)
        t.forward(dlzka)
        t.left(90)

for _ in range(3):
    schody(pocet, dlzka)
    t.lt(90)
    t.penup()
    t.fd(pocet * dlzka)
    t.rt(90)
    t.pendown()

turtle.mainloop()