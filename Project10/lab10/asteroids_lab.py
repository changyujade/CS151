import mosaic as m
import turtle_interpreter as t 
import turtle
class Game:
    def __init__(self,distance=20):
        m.mosaic(-450,-300,1,10,8)
        turt = t.TurtleInterpreter()
        self.screen = turt.getScreen()
        self.player = self.makePlayer()
        self.distance = distance
        self.setupEvents()


    def setupEvents(self):
        self.screen.onkeypress(self.moveUp,"Up")
        self.screen.onkeypress(self.moveDown,"Down")
        self.screen.onkeypress(self.moveRight,"Right")
        self.screen.onkeypress(self.moveLeft,"Left")

    def moveUp(self):
        #moves pacnab up by self.disrance
        self.player.setheading(90)
        self.player.forward(self.distance)
    
    
    def moveDown(self):
        #moves pacnab up by self.disrance
        self.player.setheading(270)
        self.player.forward(self.distance)

    def moveRight(self):
        #moves pacnab up by self.disrance
        self.player.setheading(0)
        self.player.forward(self.distance)

    def moveLeft(self):
        #moves pacnab up by self.disrance
        self.player.setheading(180)
        self.player.forward(self.distance)

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

    def makePlayer(self):
        player = turtle.Turtle()
        self.screen.register_shape('rocketship.gif')
        player.shape('rocketship.gif')
        player.penup()
        player.setheading(90)
        return player

def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()


