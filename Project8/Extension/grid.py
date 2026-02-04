import lsystem as ls
import turtle_interpreter2 as ti

turt=ti.TurtleInterpreter()
# draw 9 trees (write its x,y,angle,distance,the file.txt, the number of iterations) in a list 
listOfTrees=[[-200,150,22,10,'systemC.txt',1],[0,150,22,10,'systemC.txt',2],[200,150,22,10,'systemC.txt',3],
[-200,-100,46,10,'systemCL.txt',1],[0,-100,46,10,'systemCL.txt',2],[200,-100,46,10,'systemCL.txt',3],
[-200,-300,60,10,'systemPineMod1.txt',1],[0,-300,60,10,'systemPineMod1.txt',2],[200,-300,60,10,'systemPineMod1.txt',3]]

for item in listOfTrees: # loop through the list 
    # assign values
    angle = item[2]
    distance = item[3]
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

