'''
Jade Chang
CS 151
Lab4 
'''
from graphics import *
import time 
import random

def circle():    
    c = Circle(Point(200,50), 50)
    c.setFill('red')
    c.setOutline('blue')
    c.setWidth(5)
    return c 

def rectangle():
    aRectangle = Rectangle(Point(200,250), Point(250,300))
    aRectangle.setFill('green')
    aRectangle.setOutline('blue')
    aRectangle.setWidth(10)
    return aRectangle

def polygon():
    aPolygon = Polygon(Point(10,20), Point(30,25), Point(40,60),Point(20,50))
    aPolygon.setFill('green')
    aPolygon.setOutline('blue')
    aPolygon.setWidth(5)
    return aPolygon
def trees_init(x,y,s):
    tree=Polygon(Point(x*s,y*s),Point(x-20*s,y+20*s),Point(x-10*s,y+20*s),Point(x-40*s,y+40*s),Point(x+30*s,y+40*s),Point(x+10*s,y+20*s),Point(x+20*s,y+20*s))
    return tree
def main():
    win=GraphWin("My Rectangle",500,500)
    myList = [circle(), rectangle(), polygon(),trees_init(50,50,1)]
    for letter in myList:
        letter.draw(win)

    while True:  
        for letter in myList:
            letter.move(random.randint(0,10)-5,random.randint(0,10)-5)
            c=color_rgb(random.randint(0,255),0,0)
            letter.setFill(c)
        #win.update()
        time.sleep(0.1)
        if win.checkMouse():
            break

    win.getMouse()
    win.close()


if __name__ == '__main__':
    '''
    myList = [circle(), rectangle(), polygon()]
    for letter in myList:
        letter.draw(win)
    win.getMouse() # pause for click in window
    win.close()
    '''
    main()
