'''
Jade Chang 
Project 2 
CS 151 F21
A Shape Collection
'''
import turtle as t
import shapelib as sl
import math 
import random 

t.speed(11)


def colby1():
    #Compound shape built from simple shapes defined in my shapelib. 
    # I used cir(), square(), and isosceles2()
    sl.goto(-75,50)
    t.color('brown')
    t.pensize(5)
    t.begin_fill()
    sl.rectangle(100,100)
    t.end_fill()
    t.pencolor('black')
    sl.goto(-75,50)
    sl.isosceles2(100,25,1)
    sl.goto(-63,125)
    sl.rectangle(75,75)
    sl.goto(-63,125)
    sl.rectangle(75,5)
    sl.goto(-70,130)
    sl.rectangle(90,5)
    sl.goto(-52,180)
    sl.rectangle(50,50)
    sl.goto(-40,205)
    sl.rectangle(25,25) 
    sl.goto(-16,205)
    t.setheading(90)
    sl.cir(11,180)
    sl.goto(-35,210)
    sl.isosceles2(15,50,1)

    sl.goto(-250,-250)
    t.left(49)
    t.forward(280)

    sl.goto(210,-250)
    t.setheading(0)
    t.left(133)
    t.forward(280)

def tree(x,y,scale,color):
    #Compount Shape 2
    #tree trunk
    sl.goto(x,y)
    t.color('saddle brown')
    t.begin_fill()
    t.setheading(0)
    sl.rectangle(scale*10,scale*20)
    t.end_fill()

    #draws the tree
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.forward(scale*30)
    t.setheading(0)
    sl.cir(scale*50,175)
    t.setheading(0)
    sl.cir(scale*30,175)
    t.setheading(90)
    sl.cir(scale*30,180)
    t.setheading(170)
    sl.cir(scale*30,175)
    t.setheading(180)
    sl.cir(scale*50,175)
    t.setheading(0)
    t.forward(43)
    t.end_fill()


def trees():
    #random function that decides the colors of the trees   
    myList = ["green","olive","dark green","olive drab","forest green","yellow green"]
    
    #left
    tree(-90,-65,1/2,random.choice(myList))
    tree(-150,-80,3/4,random.choice(myList))

    #right
    tree(100,-100,3/5,random.choice(myList))
    tree(170,-180,4/5,random.choice(myList))
    tree(225,-250,3/4,random.choice(myList))

    #center
    tree(-35,-75,1/5,random.choice(myList))
    tree(25,-50,1/4,random.choice(myList))

def clouds():
    #here I used random functions to randomize the colors of the clouds and their sizes (within a given range)
    random.uniform(1/3, 1) 
    cloud_color = ["dark turquoise","sky blue","deep sky blue","light blue","pale turquoise"]
    sl.goto(175,50)
    cloud(random.uniform(0, 2),random.choice(cloud_color))
    sl.goto(100,200)
    cloud(random.uniform(0, 2),random.choice(cloud_color))
    sl.goto(130,225)
    cloud(random.uniform(0, 2),random.choice(cloud_color))
    sl.goto(-200,200)
    cloud(random.uniform(0, 2),random.choice(cloud_color))
    sl.goto(-175,180)
    cloud(random.uniform(0, 2),random.choice(cloud_color))

colby1()
trees()
clouds()
sl.rectangle(-200,500)

t.exitonclick()

