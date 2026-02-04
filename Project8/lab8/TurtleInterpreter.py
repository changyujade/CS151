from turtle import *

class TurtleInterpreter:
    def __init__(self, width=800, height=800, bgColor='white'):
        '''TurtleInterpreter constructor.
        Creates instance variables for a Turtle object and a Screen object with a particular window
        `width`, `height`, and background color `bgColor`.
        '''
        # Create a Turtle object, set it as an instance variable
        self.turt = Turtle()
        # Create a Screen object, set it as an instance variable.
        self.screen = Screen() #I don't remember how to do a screen object 
        # Set the screen's height, width, and color based on the parameters
        self.screen.bgcolor(bgColor)
        self.screen.screensize(width,height)
        # Turn the screen's tracer off.
        self.screen.tracer(False)
    def setColor(self, c):
        self.turt.pencolor(c)
    def setWidth(self, w):
        self.turt.pensize(w) 
    def goto(self, x, y, heading=None):
        self.turt.penup()
        self.turt.goto(x,y)
        self.turt.heading(heading)
        self.turt.pendown()
    def getScreenWidth(self):
        return self.screen.window_width() #these are not defined
    def getScreenHeight(self):
        return self.screen.window_height()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        self.turt.hideturtle()
        self.screen.update()

        # Close the window when users presses the 'q' key
        self.screen.onkey(self.screen.bye(), 'q')

        # Listen for the q button press event
        self.screen.listen()

        # Have the turtle listen for a click
        self.screen.exitonclick()
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
        for i in lsysString:
            if i =="F":
                self.turt.forward(50)
            elif i == '+':
                self.turt.left(120)
            else:
                self.turt.right(60)
        self.screen.update()
        # Walk through the lsysString character-by-character and
        # have the turtle object (instance variable) carry out the
        # appropriate commands

        # Call the update method on the screen object to make sure
        # everything drawn shows up at the very end of the method
        # (remember: you turned off animations in the constructor)


    



