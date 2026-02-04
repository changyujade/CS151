'''
Jade Chang 
CS 151 Compound Shapes
'''
from graphics import *

win = GraphWin("Compound Shape", 500, 500)
win.setBackground('white')

#the xx_init functions draws the compound shapes that will be used in scene.py
def circle_shape_init(x,y,s): 
    radius=30 #big circle  
    small_radius=8 #small circle inside the big shape 
    c=Circle(Point(x,y), radius*s)
    myList=[c]
    '''
    the for loops put the circles in a list 
    '''
    for i in range(1,50,15): 
        z=Circle(Point(x,y-24*s+i*s), small_radius*s)
        z.setFill('red')
        z.setWidth(0)
        myList.append(z)
    for i in range(1,45,15):
        z=Circle(Point(x+15*s,y-15*s+i*s), small_radius*s)
        z.setFill('red')
        z.setWidth(0)
        myList.append(z)
        z=Circle(Point(x-15*s,y-15*s+i*s), small_radius*s)
        z.setFill('red')
        z.setWidth(0)
        myList.append(z)
    
    c.setOutline('black')
    c.setFill('green')
    
    c.setWidth(0)
    
    # this loop draws the shapes inside the loop onto the canvas
    print(myList)
    for letter in myList: #Extention 1 - this system puts the objects' location, scale etc. in a list, and will draw it using a for loop 
        letter.draw(win)

def rectangle_init(x,y,s): 
    r=Rectangle(Point(x,y), Point(x+100*s,y+100*s))
    myList=[r]
    for i in range(1,60,10):
        z=Rectangle(Point(x+10*s+i*s,y+10*s+i*s), Point(x+40*s+i*s,y+40*s+i*s))
        z.setFill('blue')
        myList.append(z)
    
    r.setOutline('black')
    r.setWidth(1)

    print(myList)
    for letter in myList:
        letter.draw(win)

def triangle_init(x,y,s): 
    small_radius=8
    t=Polygon(Point(x,y), Point(x+90*s,y),Point(x+50*s,y-50*s))
    t.setFill('blue')
    myList=[t]
    for i in range(1,60,17):
        z=Circle(Point(x+20*s+i*s,y-8*s), small_radius*s)
        z.setFill('orange')
        myList.append(z)
    for l in range (1,45,16):
        o=Circle(Point(x+30*s+l*s,y-23*s),small_radius*s)
        o.setFill('magenta')
        myList.append(o)
    for i in range (1,50,17):
        o=Circle(Point(x+15*s+l*s,y-36*s),small_radius*s)
        o.setFill('pink')
        myList.append(o)
    
    t.setOutline('black')
    t.setWidth(1)

    print(myList)
    for letter in myList:
        letter.draw(win)

def road():
    '''This is an additional shape''' 
    r=Polygon(Point(500,0),Point(500,25), Point(0,480),Point(-10,460))
    myList=[r]
    '''
    this for loop make multiple rectangles that represent the divide on the roads
    '''
    for i in range(0,50):
        d=Polygon(Point(480-11*i,31+10*i),Point(484-11*i,33+10*i),Point(478-11*i,39+10*i),Point(475-11*i,36+10*i))
        d.setFill('Yellow')
        myList.append(d)
    z=Polygon(Point(480-10*i,31-15*i),Point(484-10*i,33-15*i),Point(478-10*i,39-15*i),Point(475-10*i,36-15*i))
    myList.append(z)

    r.setOutline('black')
    r.setFill('black')
    r.setWidth(1)

    for letter in myList:
        letter.draw(win)
    
def circle_shape_init2(x,y,s): 
    '''This is an additional shape'''
    radius=30 #big circle  
    c=Circle(Point(x,y), radius*s)
    myList=[c]
    c.setOutline('black')
    c.setFill('green')
    c.setWidth(0)
    
    z=Polygon(Point(x-10*s,y-25*s),Point(x+0*s,y+0*s),Point(x+10*s,y-25*s))
    z.setFill('red')
    myList.append(z)
    z=Polygon(Point(x-10*s,y+20*s),Point(x+0*s,y+0*s),Point(x+10*s,y+20*s))
    z.setFill('red')
    myList.append(z)
    z=Polygon(Point(x-20*s,y-15*s),Point(x+0*s,y+0*s),Point(x-20*s,y+10*s))
    z.setFill('red')
    myList.append(z)
    z=Polygon(Point(x+20*s,y-15*s),Point(x+0*s,y+0*s),Point(x+20*s,y+10*s))
    z.setFill('red')
    myList.append(z)
    

    # this loop draws the shapes inside the loop onto the canvas
    print(myList)
    for letter in myList: #Extention 1 - this system puts the objects' location, scale etc. in a list, and will draw it using a for loop 
        letter.draw(win)

'''
these test functions test out whether these functions will work
'''
def circle_test():
    circle_shape_init(50,50,1)
    circle_shape_init(100,200,2)
    circle_shape_init(300,400,3)

def rectangle_test():
    rectangle_init(50,50,1)
    rectangle_init(100,200,2)
    rectangle_init(300,400,3)

def triangle_test():
    triangle_init(50,50,1)
    triangle_init(100,200,2)
    triangle_init(300,400,3)



