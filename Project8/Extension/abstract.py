import lsystem as ls
import turtle_interpreter2_copy as ti

turt=ti.TurtleInterpreter()

# draw 9 trees (write its x,y,angle,distance,the file.txt, the number of iterations,scale) in a list 
listOfTrees=[[-200,-200,22,10,'systemC.txt',1,1],[0,-200,22,10,'systemC.txt',2,2],[200,-200,22,10,'systemC.txt',3,3], #Extention 3: take in (x, y, scale) as parameters and demonstrate you can properly translate and scale the abstract image by including multiple copies, at different locations and scales, in one scene
[-150,-50,22,10,'abstract.txt',3,3],[-250,150,22,10,'abstract.txt',5,1],[50,200,22,10,'circle.txt',4,2]] 

for item in listOfTrees: # loop through the list 
    # assign values
    angle = item[2]
    distance = item[3]*item[6]
    # create a instance variable/object 
    lsys = ls.Lsystem(item[4])
    # number of iteration to generate string using build string method
    nIter = item[5]
    lsysString = lsys.buildString(nIter)
    turt.goto(item[0],item[1],90) #how to set heading
    turt.setColor('purple')
    turt.setWidth(2)
    turt.drawString(lsysString, distance, angle)

turt.hold()