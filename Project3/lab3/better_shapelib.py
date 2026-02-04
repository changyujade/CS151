'''
Jade Chang
CS 151
Building a better Shape lib
'''

import turtle 
import random 
import math
turtle.tracer(False)
import shapelib_copy as sl

#importing functions from previous projects so scenes can be drawn. 
#These are foundamental building blocks and shapes
def goto(x,y): 
    print('goto(): before move, turtle at', turtle.position())
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    print('goto(): going to',turtle.goto(x,y))
    print('goto(): after move, turtle now at', turtle.position())

def rectangle(x,y,width,height,fill=False,edgeColor='black',fillColor='red',penWidth=1):
    #default color of the triangle is in the paramter above
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

def isosceles2(base,height,scale,color):
    turtle.color(color)
    turtle.begin_fill()
    #using trigonometry, the angle of is calculated 
    # and can draw isosceles of any width and height
    turtle.forward(scale*base)
    turtle.left(180-(math.degrees((math.atan(height/(base/2))))))
    turtle.forward(scale*(math.sqrt((base/2)**2+height**2)))
    turtle.left(180-(180-(2*(math.degrees(math.atan(height/(base/2)))))))
    turtle.forward(scale*(math.sqrt((base/2)**2+height**2)))
    turtle.end_fill()

def cir(radius,extent,color='blue'):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius,extent)
    turtle.end_fill()

#mondrian scene is created by randomising the width,height, and colors of the triangles
def mondrian(x,y,s,numRectangles=50):
    for i in range(numRectangles):
            z=s*(random.randint(-500,500))
            w=s*(random.randint(-500,500))
            width=s*(random.randint(50,150))
            height=s*(random.randint(50,150))
            penWidth=s*(random.randint(1,10))
            #randomise the numbers in the tuple to create rectangles of random float between 0.0 to 1.0
            tuple=[(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1))]
            if random.random() < 0.4:
                rectangle(z+x,w+y,width,height,True,'black',tuple,penWidth)
            else:
                rectangle(z+x,w+y,width,height)

#this scene will later on be used in the magritte
def compoundShape(x,y,radius,extent,color,color_2,base=10,height=10):
    goto(x,y)
    cir(radius,extent,color)
    turtle.penup()
    goto(x,y)
    turtle.pendown()
    isosceles2(base,height,1.5,color_2)

#the magritte is modified from the mondrian scene, 
#offsets of x,y,s is used for so it could be created on a desired x,y axis as well as the scale 
def magritte(x,y,s,numRectangles=200):
    for i in range(numRectangles):
            z=s*(random.randint(-500,500))
            w=s*(random.randint(-500,500))
            radius=s*(random.randint(10,50))
            extent=s*(random.randint(50,360))
            base=s*(random.randint(15,50))
            height=s*(random.randint(15,75))

            #randomise the numbers in the tuple to create rectangles of random float between 0.0 to 1.0
            tuple=[(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1))]
            tuple_2=[(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1)),(round(random.uniform(0.0,1.0),1))]

            if random.random() < 0.4:
                compoundShape(z+x,w+y,radius,extent,tuple,tuple_2,base,height)
            else:
                compoundShape(w+x,w+y,radius,360,tuple,tuple_2)

#this is the second scene that I will be using in my surreal artwork
def colby1(x=0,y=0,s=1):
    #Compound shape built from simple shapes defined in my shapelib. 
    # I used cir(), square(), and isosceles2()
    sl.goto(x+(s*-75),y+(s*50))
    turtle.color('brown')
    turtle.pensize(5)
    turtle.begin_fill()
    sl.rectangle(s*100,s*100)
    turtle.end_fill()
    turtle.pencolor('black')
    sl.goto(x+s*-75,y+s*50)
    sl.isosceles2(s*100,s*25,s*1)
    sl.goto(x+s*-63,y+s*125)
    sl.rectangle(s*75,s*75)
    sl.goto(x+s*-63,y+s*125)
    sl.rectangle(s*75,s*5)
    sl.goto(x+s*(-70),y+s*130)
    sl.rectangle(s*90,s*5)
    sl.goto(x+s*-52,y+s*180)
    sl.rectangle(s*50,s*50)
    sl.goto(x+s*-40,y+s*205)
    sl.rectangle(s*25,s*25) 
    sl.goto(x+s*-16,y+s*205)
    turtle.setheading(90)
    sl.cir(s*11,180)
    sl.goto(x+s*-35,y+s*210)
    sl.isosceles2(s*15,s*50,s*1)

    #magritte(200,200,0.2)

#extention - 3rd scene that I'll use in my surreal artwork
def tree(x,y,scale,color):
    #Compount Shape 2
    #tree trunk
    sl.goto(x,y)
    turtle.color('saddle brown')
    turtle.begin_fill()
    turtle.setheading(0)
    sl.rectangle(scale*10,scale*20)
    turtle.end_fill()

    #draws the tree
    turtle.setheading(0)
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(scale*30)
    turtle.setheading(0)
    sl.cir(scale*50,175)
    turtle.setheading(0)
    sl.cir(scale*30,175)
    turtle.setheading(90)
    sl.cir(scale*30,180)
    turtle.setheading(170)
    sl.cir(scale*30,175)
    turtle.setheading(180)
    sl.cir(scale*50,175)
    turtle.setheading(0)
    turtle.forward(43)
    turtle.end_fill()

def trees(x,y,s):
    #random function that decides the colors of the trees   
    myList = ["green","olive","dark green","olive drab","forest green","yellow green"]
    # x,y,s offsets added in order to specify the location and the location and scale 
    #left
    tree(x+(-90),y+(-65),s*1/2,random.choice(myList))
    tree(x+(-150),y+(-80),s*(3/4),random.choice(myList))

    #right
    tree(x+100,y+(-100),s*3/5,random.choice(myList))
    tree(x+170,y+(-180),s*4/5,random.choice(myList))
    tree(x+225,y+(-250),s*3/4,random.choice(myList))

    #center
    tree(x+(-35),y+(-75),s*1/5,random.choice(myList))
    tree(x+25,y+(-50),s*1/4,random.choice(myList))

'''
if __name__== '__main__':
    #mondrian(-200,0,0.3,200)
    #mondrian(-10,-150,0.1,200)
    #mondrian(50,150,0.4,200)
    colby1(125,-200,1)
    #colby1(-200,200,0.5)
    colby1(-200,-200,1.2)
'''
    
#turtle.update()
#turtle.exitonclick()
