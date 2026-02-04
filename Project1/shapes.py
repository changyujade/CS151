from turtle import *
speed(10)
def shapeA():
    color('dark cyan')
    begin_fill()
    for i in range (15):
        right(110)
        forward(200)
        circle(50,180)
        left(26)
        forward(223)
    end_fill()

def shapeB():
    pencolor('white')
    for i in range(24):
        circle(60,-60)
        left(75)
    

def shapeC(x,y,z):
    pencolor('white')
    for i in range(y):
        circle(x,z)
        left(75)

#shapeA
penup()
goto(25,50)
pendown()
shapeA()

#shapeB
penup()
goto(165,233)
pendown()
shapeB()

#composition

def composition():
    penup()
    goto(150,200)
    pendown()
    shapeC(50,24,-60)
    penup()
    goto(100,140)
    pendown()
    shapeC(30,8,60)
    penup()
    setpos(-65,-70)
    pendown()
    shapeC(300,8,60)
    penup()
    setpos(-15,-15)
    pendown()
    shapeC(150,8,60)
    penup()
    setpos(6,18)
    pendown()
    shapeC(75,8,60)

composition()

exitonclick()