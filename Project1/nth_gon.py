from turtle import *

sides= int(input("how many sides are there in your shape?"))

for x in range(sides):
    forward(100-4*sides)
    right(360/sides)

exitonclick()