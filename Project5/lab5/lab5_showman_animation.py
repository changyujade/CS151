'''
Jade Chang
CS 151
Lab4 Snowman
'''
from graphics import *

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
    '''

    '''
    return myList
    win.getMouse() # pause for click in window
    win.close()

def snowman_animate(shapes, frame, screen):
    '''Move the snowman at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the snowman
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the snowman is on.
        NOTE: The `screen` is not needed for lab.
    '''
    for i in shapes:
        if frame%2==0:
            i.move(10,5)
        else: 
            i.move(-10,5)

def main():
    win=GraphWin("My Rectangle",500,500)

    myList=snowman_init(100,100,1)
    for letter in myList:
        letter.draw(win)

    for frame in range(1000):  
        snowman_animate(myList,frame,win)
        #win.update()
        time.sleep(0.1)
        if win.checkMouse():
            break

    win.getMouse()
    win.close()

main()
    


