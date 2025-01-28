import turtle

t=turtle.Turtle()
t.hideturtle()
t.pencolor("black")
t.speed(0)
dl=20

def stvorec(dl):
    for i in range(4):
        t.fd(dl)
        t.lt(90)

def line(n):
    for i in range(n):
        stvorec(dl)
        t.penup()
        t.fd(dl)
        t.pendown()

def left_turn(x,y):
    t.penup()
    t.setpos(x,y)
    t.lt(90)
    t.pendown()

line(4)
left_turn(dl*5,dl)
line(2)
left_turn(dl*4,dl*4)
line(3)
t.rt(90)
line(2)
t.rt(90)
line(4)

turtle.exitonclick()