'''
Jade Chang 
lab 2 
CS 151 F21
Create compound shapes
'''

import turtle 
turtle.speed(10)
def triangle(scale):
    '''
    This function draws a traingle 
    parameter: scale, variable that control sthe size of the triangle
    '''
    for x in range (3):
        turtle.forward(scale*100)
        turtle.left(120)

def goto(x,y): 
    print('goto(): before move, turtle at', turtle.position())
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    print('goto(): going to',turtle.goto(x,y))
    print('goto(): after move, turtle now at', turtle.position())

'''
triangle(3)
goto(30,0)
triangle(3)
goto(15,-25)
triangle(3)
'''


def triangle2(x, y, scale):
    '''Draws a triangle at any (`x`, `y`) position and scale (`scale`)
    By default, the side lengths are 100 (when `scale` = 1)
    '''
    goto(x,y)
    triangle(scale)

'''
triangle2(0,0,1)
triangle2(-50,-25,2)
triangle2(-100,-50,3)
'''

def triangleStack(x, y,scale):
    '''Draws three triangles on top of each other.
    Smaller triangles are placed on top of larger ones
    '''
    # Largest triangle
    triangle2(scale*(x+0), scale*(y+0),scale*(2))
    # Medium triangle in middle
    triangle2(scale*(x+50), scale*(y+173.2), scale*(1))
    # Small triangle on top of stack
    triangle2(scale*(x+75), scale*(y+259.81), scale*(0.5))


triangleStack(-200,0,1)
triangleStack(0,0,1/2)
triangleStack(300,0,1/3)

turtle.exitonclick()
