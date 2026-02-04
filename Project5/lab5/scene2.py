'''
Jade Chang 
CS 151 Scene 2 Animation
'''
from graphics import *
import random

win = GraphWin("Compound Shape", 500, 500)
win.setBackground('white')

def trees_init():
    'This function draws the trees in rows and columns that start from outside of the frame'
    tree_list=[]
    for j in range(-1000,0,100):
        for k in range(0,500,100):
            tree=Polygon(Point(j,k),Point(j-20,k+20),Point(j-10,k+20),Point(j-40,k+40),Point(j+30,k+40),Point(j+10,k+20),Point(j+20,k+20))
            tree_trunk=Rectangle(Point(j-10,k+40),Point(j+10,k+60))
            c=color_rgb(165,42,42)
            tree_trunk.setFill(c)
            c1=color_rgb(0,128,0)
            tree.setFill(c1)
            tree_list.append(tree)
            tree_list.append(tree_trunk)        
        
    print(tree_list)
    return tree_list


def tree_animate(shapes, frame, screen):
    "This function moves the tree to the right on even frames"
    for i in shapes:
        if frame%2==0:
            i.move(10,0)


def person_init(x,y,s):
    "This function draws the person"
    radius=30
    c=Circle(Point(x,y), radius*s)
    pList=[c]
    aRectangle = Rectangle(Point(x-25*s,y+40*s), Point(x+25*s,y+100*s))
    pList.append(aRectangle)
    l=Rectangle(Point(x+25*s,y+70*s),Point(x+50*s,y+40*s))
    pList.append(l)
    m=Rectangle(Point(x-25*s,y+60*s),Point(x-40*s,y+100*s))
    pList.append(m)

    return pList


def person_animate(shapes, frame, screen):
    '''
    This moves the person up and down within a certain range
    '''
    for i in shapes:
        if frame%2==0:
            i.move(10,5)
            i.setFill('dark gray')
        else: 
            i.move(-10,-5)

def leg_init(x,y,s):
    "this function draws the two legs, left and right"
    o=Polygon(Point(x-10*s,y+100*s),Point(x-5,y+105),Point(x-20,y+140),Point(x-40,y+120),Point(x-30,y+110),Point(x-25*s,y+105*s),Point(x-20,y+120))
    leg=[o]
    k=Rectangle(Point(x+10*s,y+100*s),Point(x+30*s,y+140*s))
    leg.append(k)
    return leg

def leg_animate(shapes,frame,screen):
    "This function animates and changes the colours of the two legs."
    for i in shapes:
        if frame%2==0:
            i.setFill('grey')
            i.move(10,5)
        else: 
            i.setFill('white')
            i.move(-10,-5)
    "the shapes[] accesses each accesses left or right leg. When the left leg is white, right leg becomes grey and vice versa"
    if frame%2 == 0:
        shapes[0].setFill('grey')
        shapes[1].setFill('white')
    else:
        shapes[1].setFill('grey')
        shapes[0].setFill('white')

def text_init(x,y):
    'This line draws the text FIN'
    t=Text(Point(x,y), "FIN")
    t.setSize(36)
    t.setStyle("bold")
    t.setTextColor("gold")
    t_list=[t]
    return t_list

def text_animate(shapes,frame,screen):
    "this funciton moves the text FIN upwards and stop when the frame reaches 100"
    for i in shapes:
        if frame >=100:
            break
        elif frame%2==0:
            i.move(0,-5)
        

def main():
    pList=person_init(150,50,1)
    tree_list=trees_init()
    leg=leg_init(150,50,1)
    t=text_init(250,500)
    
    "This part of the code draws all the objects onto the screen win"
    for letter in tree_list:
        letter.draw(win)
    for letter in pList:
        letter.draw(win)
    for letter in leg:
        letter.draw(win)
    for letter in t:
        letter.draw(win)

    "This part of the code animates the objects by going through the list and interating the frame numbers"
    for frame in range(1000):  
        person_animate(pList,frame,win)
        leg_animate(leg,frame,win)
        tree_animate(tree_list,frame,win)
        text_animate(t,frame,win)
        time.sleep(0.1)
        if win.checkMouse():
            break

    win.getMouse()
    win.close()

main()


