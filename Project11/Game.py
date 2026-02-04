from abc import ABC, abstractmethod
import turtle

class Game(ABC):

    class Button:

        def __init__(self, turtleDrawer: turtle.Turtle, topLeftX: int, topLeftY: int, bottomRightX: int, bottomRightY: int, buttonText: str, borderColor = "Black", fillColor = None, fontColor = None, fontSize: int = 12):
            self.turt = turtleDrawer
            self.topLeftX = topLeftX
            self.topLeftY = topLeftY
            self.bottomRightX = bottomRightX
            self.bottomRightY = bottomRightY
            self.text = buttonText
            self.fill = fillColor
            self.font = ('Arial', fontSize, 'normal')
            self.fontColor = fontColor
            self.borderColor = borderColor
            self.draw()
        
        def draw(self):
            ''' This function draws the button using the turtleDrawer given in the constructor'''
            self.turt.goto(self.topLeftX, self.topLeftY)
            self.turt.setheading(0)
            oldColor = self.turt.color()
            oldWidth = self.turt.width()
            self.turt.color(self.borderColor)

            if self.fill: # Begins filling if fillColor was given in constructor
                self.turt.fillcolor(self.fill)
                self.turt.begin_fill()
            
            self.turt.pendown()
            self.turt.width(5)
            for i in range(2): # Draws the boundary of the button
                self.turt.forward(self.bottomRightX-self.topLeftX)
                self.turt.right(90)
                self.turt.forward(self.topLeftY - self.bottomRightY)
                self.turt.right(90)
            self.turt.penup()

            if self.fill:
                self.turt.end_fill()

            # Draws the text in the center of the box
            self.turt.goto(int((self.topLeftX + self.bottomRightX)/2), 
                           int((self.topLeftY + self.bottomRightY)/2) - self.font[1])
            self.turt.pencolor(self.fontColor)
            self.turt.write(self.text, align = "center", font = self.font)
            self.turt.pencolor(oldColor[0])
            self.turt.pencolor(oldColor[1])
            self.turt.width(oldWidth)

        def pointInside(self, pointX: int, pointY: int) -> bool:
            ''' This function returns True if the point given by (pointX, pointY) is within the 
                bounds of the button given in the constructor'''
            return (pointX >= self.topLeftX
                and pointX <= self.bottomRightX
                and pointY >= self.bottomRightY
                and pointY <= self.topLeftY)

    class Game(ABC):

        def __init__(self):
            self.drawer = turtle.Turtle()
            self.drawer.hideturtle()
            self.drawer.penup()

            self.titleScreen()
            self.player = self.createMainPlayer()
            print('game init')

        @abstractmethod
        def createMainPlayer(self):
            ''' Creates a main player and returns it'''

        @abstractmethod
        def titleScreen(self):
            ''' Creates the title screen'''

        @abstractmethod
        def createTitleScreenEvents(self):
            ''' Creates the events for the title screen'''

        @abstractmethod
        def createGameScreen(self):
            ''' Creates the game screen'''

        @abstractmethod
        def createGameScreenEvents(self):
            ''' Creates the events for the game screen'''

        @abstractmethod
        def play(self):
            ''' Handles actually playing the game'''

        @abstractmethod
        def createResultScreen(self, result):
            ''' Creates the end screen, which should contain a button to restart the game'''

        @abstractmethod
        def createResultScreenEvents(self):
            ''' Creates the events for the result screen'''

'''
if __name__ == "__main__":
    turtleDrawer = turtle.Turtle()
    screen = turtle.Screen()
    turtleDrawer.penup()
    turtleDrawer.hideturtle()
    screen.tracer(0)
    
    button = Game.Button(turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Print", borderColor="Red", 
                         fillColor="Green", fontColor="Blue", fontSize=13)
    quitButton = Game.Button(turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
                         fillColor="Green", fontColor="Blue", fontSize=13)

    def clickFunction(mouseX, mouseY):
        if button.pointInside(mouseX, mouseY):
            print("Button clicked!")
        elif quitButton.pointInside(mouseX, mouseY):
            print("Quit clicked")
            turtle.bye()
    screen.onclick(clickFunction)
    screen.listen()
    screen.mainloop()

'''