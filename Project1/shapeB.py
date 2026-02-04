from turtle import *

def shapeB():
    for i in range(12):
        circle(120,-60)
        left(90)

color('dark orange')
begin_fill()
penup()
goto(180,150)
pendown()
shapeB()
end_fill

exitonclick()