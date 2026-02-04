from turtle import *
import random
class TurtleInterpreter:
    turt = Turtle()
    screen = Screen()
    def __init__(self, width=800, height=800, bgColor='white'):
        '''TurtleInterpreter constructor.
        Creates instance variables for a Turtle object and a Screen object with a particular window
        `width`, `height`, and background color `bgColor`.
        '''
        # Set the screen's height, width, and color based on the parameters
        TurtleInterpreter.screen.bgcolor(bgColor)
        TurtleInterpreter.screen.screensize(width,height)
        # Turn the screen's tracer off.
        TurtleInterpreter.screen.tracer(False)
    def setColor(self, c):
        TurtleInterpreter.turt.color(c)
    def setWidth(self, w):
        TurtleInterpreter.turt.pensize(w) 
    def goto(self, x, y, heading=None):
        TurtleInterpreter.turt.penup()
        TurtleInterpreter.turt.goto(x,y)
        if heading != None:
            TurtleInterpreter.turt.setheading(heading)
        TurtleInterpreter.turt.pendown()
    def getScreenWidth(self):
        return TurtleInterpreter.screen.window_width() 
    def getScreenHeight(self):
        return TurtleInterpreter.window_height()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        TurtleInterpreter.turt.hideturtle()
        TurtleInterpreter.screen.update()

        # Close the window when users presses the 'q' key
        TurtleInterpreter.screen.onkey(bye, 'q')

        # Listen for the q button press event
        TurtleInterpreter.screen.listen()

        # Have the turtle listen for a click
        TurtleInterpreter.screen.exitonclick()
    def drawString(self, lsysString, distance, angle):
        '''Interpret each character in an L-system string as a turtle command.

        Here is the starting L-system alphabet:
            F is forward by a certain distance
            + is left by an angle
            - is right by an angle

        Parameters:
        -----------
        lsysString: str. The L-system string with characters that will be interpreted as drawing
            commands.
        distance: distance to travel with F command.
        angle: turning angle (in deg) for each right/left command.
        '''
        branch=[]
        currColor=[]
        currLeaves=[]
        currBerries=[]
        for i in lsysString:
            if i =="F":
                TurtleInterpreter.turt.forward(distance)
            elif i == '+':
                TurtleInterpreter.turt.left(angle)
            elif i == '-':
                TurtleInterpreter.turt.right(angle)
            elif i == "[":
                branch.append([TurtleInterpreter.turt.xcor(),TurtleInterpreter.turt.ycor(),TurtleInterpreter.turt.heading()])
            elif i == "]":
                previous=branch.pop()
                TurtleInterpreter.turt.penup()
                TurtleInterpreter.turt.setposition(previous[0],previous[1])
                TurtleInterpreter.turt.pendown()
                TurtleInterpreter.turt.setheading(previous[2])
            elif i == '<':
                currColor.append(TurtleInterpreter.turt.color()[0])
            elif i == '>':
                previousColor=currColor.pop()
                TurtleInterpreter.turt.fillcolor(previousColor)
            elif i == 'g':
                TurtleInterpreter.turt.pencolor((0.15, 0.5, 0.2))
            elif i == 'y':
                TurtleInterpreter.turt.pencolor((0.8, 0.8, 0.3))
            elif i == 'r':
                TurtleInterpreter.turt.pencolor((0.7, 0.2, 0.3))
            elif i=='z':
                TurtleInterpreter.turt.pencolor((random.random()),random.random(),random.random())
            elif i == 'L':
                currBerries.append([TurtleInterpreter.turt.xcor(),TurtleInterpreter.turt.ycor(),TurtleInterpreter.turt.heading()])
                preB=currBerries.pop()
                TurtleInterpreter.turt.circle(10,180)
                TurtleInterpreter.turt.setposition(preB[0],preB[1])
                TurtleInterpreter.turt.setheading(preB[2])
            elif i == 'B':
                currLeaves.append([TurtleInterpreter.turt.xcor(),TurtleInterpreter.turt.ycor(),TurtleInterpreter.turt.heading()])
                pre=currLeaves.pop()
                TurtleInterpreter.turt.begin_fill()
                TurtleInterpreter.turt.circle(5)
                TurtleInterpreter.turt.end_fill()
                TurtleInterpreter.turt.setposition(pre[0],pre[1])
                TurtleInterpreter.turt.setheading(pre[2])
            elif i == '{':
                TurtleInterpreter.turt.begin_fill()
            elif i == '}':
                TurtleInterpreter.turt.end_fill()
         
        TurtleInterpreter.screen.update()
        # Walk through the lsysString character-by-character and
        # have the turtle object (instance variable) carry out the
        # appropriate commands

        # Call the update method on the screen object to make sure
        # everything drawn shows up at the very end of the method
        # (remember: you turned off animations in the constructor)



    



