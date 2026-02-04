'''
Jade Chang
CS 151
Lab4 
'''
from graphics import *
win = GraphWin("lab4_Collage", 500, 500)
win.setBackground('white')

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



if __name__ == '__main__':
    myList = [circle(), rectangle(), polygon()]
    for letter in myList:
        letter.draw(win)
    win.getMouse() # pause for click in window
    win.close()
