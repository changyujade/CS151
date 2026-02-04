import turtle 
import random 
turtle.speed(10)
def goto(x,y): 
    print('goto(): before move, turtle at', turtle.position())
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    print('goto(): going to',turtle.goto(x,y))
    print('goto(): after move, turtle now at', turtle.position())

def rectangle(x,y,width,height,fill=False,edgeColor='black',fillColor='red',penWidth=1):
    goto(x,y)
    if fill == True:
        turtle.pensize(penWidth)
        turtle.color(edgeColor, fillColor)
        turtle.begin_fill()
    for x in range (2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()

#rectangle(0,0,50, 100,True, 'green', 'blue',10)

if __name__== '__main__':
    for x in range(200):
            x=random.randint(-500,500)
            y=random.randint(-500,500)
            width=random.randint(50,150)
            height=random.randint(50,150)
            penWidth=random.randint(1,10)
            tuple=[(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1))]
            if random.random() < 0.4:
                rectangle(x,y,width,height,True,'black',tuple)
            else:
                rectangle(x,y,width,height)


turtle.exitonclick()
