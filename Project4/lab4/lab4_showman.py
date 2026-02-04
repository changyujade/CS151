'''
Jade Chang
CS 151
Lab4 Snowman
'''
from graphics import *
win = GraphWin("lab4_Collage", 500, 500)
win.setBackground('white')


def snowman_init(x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a snowman.
    Minimally, this is just three equal sized circles stack on top of each other
    with two smaller circles for the eyes

    Parameters:
    -----------
    x: int. x coordinate for the top circle center.
    y: int. y coordinate for the top circle center.
    scale: float. Scaled size of the snowman.

    Returns:
    -----------
    list with 5 Zelle Circle objects in it.
    '''
    radius=30
    eyeRadius=3
    
    a=Circle(Point(x,y), radius)
    b=Circle(Point(x,y+2*radius*scale), radius)
    c=Circle(Point(x,y+4*radius*scale), radius)
    e=Circle(Point(x-scale*radius/2,y), eyeRadius)
    f=Circle(Point(x+scale*radius/2,y), eyeRadius)
    myList=[a,b,c,e,f]
    
    print(myList)
    for letter in myList:
        letter.draw(win)
    win.getMouse() # pause for click in window
    win.close()

snowman_init(200,200,1)
    


