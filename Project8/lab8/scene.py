import turtle_interpreter2 as ti
import lsystem as ls

turt=ti.TurtleInterpreter(1000,1000,'sky blue')
# draw trees (write its x,y,angle,distance,the file.txt, the number of iterations,colors) in a list 

listOfTrees=[[0,-300,42,10,'systemC.txt',2,'purple'],[200,-300,42,10,'systemCL.txt',3,'purple'],[-200,-300,42,10,'systemCL.txt',1,'purple'],
[-200,150,42,10,'Mysystem.txt',5,'white'],[120,125,42,10,'Mysystem.txt',5,'white'],[200,135,40,5,'Mysystem.txt',3,'white'],
[-125,200,42,5,'Mysystem.txt',5,'white'],[145,300,42,10,'Mysystem.txt',5,'white']]

if __name__ == '__main__':
    turt.setColor('brown')
    turt.setWidth(10)

    turt.goto(-350,-310)
    for i in range(2):
        turt.drawString("F+",1000,90)
        turt.drawString("F+",50,90)

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
        turt.setColor(item[6])
        turt.setWidth(2)
        turt.drawString(lsysString, distance, angle)
    
    turt.hold()