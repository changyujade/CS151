import mosaic as m
import turtle_interpreter as t 
import turtle
import random
import time
import intro
import Game as g

class Asteroids(g.Game.Game):
    def __init__(self):
        super().__init__()
        print('asteroids')

    def createMainPlayer(self):
        player = turtle.Turtle()
        self.screen.register_shape('rocketship.gif')
        player.shape('rocketship.gif')
        player.penup()
        player.setheading(90)
        print("main player created")
        return player
    
    def titleScreen(self):
        #move the intro scene here?
        self.turtleDrawer = turtle.Turtle()
        self.screen = turtle.Screen()
        self.turtleDrawer.penup()
        self.turtleDrawer.hideturtle()
        self.screen.tracer(0)
        print('title screen')

    def createTitleScreenEvents(self):
        print('createTitleScreenEvents')
        
        button = g.Game.Button(self.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Print", borderColor="Red", 
                                fillColor="Green", fontColor="Blue", fontSize=13)

        quitButton = g.Game.Button(self.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
                            fillColor="Green", fontColor="Blue", fontSize=13)

        def clickFunction(mouseX, mouseY):
            if button.pointInside(mouseX, mouseY):
                print("Button clicked!")
            elif quitButton.pointInside(mouseX, mouseY):
                print("Quit clicked")
                turtle.bye()
        self.screen.onclick(clickFunction)
        
    def createGameScreen(self):
        self.turtleDrawer = turtle.Turtle()
        self.screen = turtle.Screen()
        
        self.turtleDrawer.penup()
        m.mosaic(-450,-300,1,10,8)
        self.turtleDrawer.hideturtle()
        self.screen.tracer(0)
        print('crateGameScreen')

    def createGameScreenEvents(self):
        pass
        self.screen.onkeypress(self.moveUp,"Up")
        self.screen.onkeypress(self.moveDown,"Down")
        self.screen.onkeypress(self.moveRight,"Right")
        self.screen.onkeypress(self.moveLeft,"Left")

        self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.ontimer(self.checkCollisions, 250)

    def play(self):
        
        '''Turns the tracer animations on (but speeds up animations) and starts the main game loop.
        '''
        # Call the tracer method on your `Screen` instance variable,
        # passing in True as the parameter to turn animations on.
        self.screen.tracer(True)

        # Call the listen method on your `Screen` instance variable
        # so that keyboard presses are not registered as events

        self.screen.listen()

        # Call the mainloop method on your `Screen` instance variable.

        self.screen.mainloop()
    
    def createResultScreen(self, result):
        pass

    def createResultScreenEvents(self):
        pass

if __name__ == "__main__":
    asteroids = Asteroids()
     
    asteroids.createTitleScreenEvents()
    asteroids.play()

    '''
    turtle.clear()
    #clear screen and draw the next screen
    #or quit the screen and open a new screen
    asteroids.createGameScreen()
    asteroids.createGameScreenEvents()
    asteroids.play()
    '''
    

     