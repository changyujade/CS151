'''
Jade Chang
CS 151
surreal art scene
'''
from turtle import exitonclick
import better_shapelib as bsl
import sys


#this part allows multiple colbys to be drawn
x=-500
#the command line arguments allow x to be changed 
# in the terminal when the code is run. Since the number decides the position at which
# it starts drawing, I recommend putting -500 when it is run.  
for i in range(8):
    x=x+100
    bsl.colby1(x,0,0.5)
    bsl.colby1(x,200,0.5)

x=-500
for i in range (20):
    x=x+80
    bsl.colby1(x,100,0.3)
    bsl.colby1(x,-100,0.3)

#the magritte acts as the 'buildings', created by shifting its x,y positions and scale
bsl.magritte(-300,-200,0.2)
bsl.magritte(-200,-200,0.2)
bsl.magritte(-100,-200,0.2)
bsl.magritte(0,-200,0.2)
bsl.magritte(100,-200,0.2)
bsl.magritte(200,-200,0.2)
# extention - adding another scene
bsl.trees(20,200,0.5)
exitonclick()
