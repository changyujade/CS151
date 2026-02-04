import turtle 
canvas = turtle.Screen()
canvas.setup(width = 1000, height = 1000)
canvas.bgcolor('sky blue')
canvas.title("Multiple turtles demo")

#creates 2 turtle objects
turt1= turtle.Turtle()
turt2 = turtle.Turtle()


turt1.goto(50,0)
turt2.penup()
turt2.goto(-300,200)
turt2.pendown()

turt1.left(60)
turt1.forward(100)

turt2.right(30)
turt2.forward(200)

turt1.color('green')
turt2.color('red')

turt1.pensize(10)
turt2.pensize(2)

for i in range(10):
    turt1.left(60)
    turt1.forward(100)
    turt2.left(30)
    turt2.forward(200)
canvas.exitonclick()