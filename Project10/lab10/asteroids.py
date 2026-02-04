import mosaic as m
import turtle_interpreter as t 
import turtle
import random

class Game:
    numTimes = 0

    def __init__(self,distance=2,min_x=-200,min_y=0,max_x=200,max_y=200):
        m.mosaic(-450,-300,1,10,8)
        turt = t.TurtleInterpreter()
        self.screen = turt.getScreen()
        self.player = self.makePlayer()
        self.distance = distance
        self.min_x=min_x
        self.min_y=min_y
        self.max_x=max_x
        self.max_y=max_y

        self.makeEnemies()
        self.setupEvents()


    def setupEvents(self):
        self.screen.onkeypress(self.moveUp,"Up")
        self.screen.onkeypress(self.moveDown,"Down")
        self.screen.onkeypress(self.moveRight,"Right")
        self.screen.onkeypress(self.moveLeft,"Left")

        self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.ontimer(self.checkCollisions, 250)

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
    
    def placeEnemyRandomly(self, enemy):
        "Place the enemies at x, y in the canvas randomly."
        enemy.speed(0)
        enemy.goto(random.randint(self.min_x, self.max_x), random.randint(self.min_y, self.max_y))
        enemy.speed(6)
    
    def makeEnemies(self, n=4):
        '''Make a Turtle object (that look like an enemy). Return the enemy list
        '''
        self.enemyList=[]
        colorList = ['cyan','red','green','yellow']
        for i in range (n):
            enemy = turtle.Turtle()
            enemy.shape('square')
            enemy.color(random.choice(colorList))
            self.enemyList.append(enemy)

        for i in self.enemyList:
            i.penup()
            self.placeEnemyRandomly(i)
        return self.enemyList

    def moveEnemiesRandomly(self):
        for i in self.enemyList:
            x = random.randint(i.xcor()-10, i.xcor()+10)
            y = random.randint(i.ycor()-10, i.ycor()+10)

            i.goto(x,y) 

        self.screen.ontimer(self.moveEnemiesRandomly, 1000)
        return self.enemyList

    def checkCollisions(self):
        '''Checks for whether we have a collision between the player (Pacman) and one of the pellets.
        '''
        #Game.numTimes = Game.numTimes + 1
        #print('hi from 250 msec in the future!', Game.numTimes)

        player_x = self.player.xcor()
        player_y = self.player.ycor()
        for i in self.enemyList:
            enemies_x = i.xcor() #the enemies part still needs to be replaced with correct code 
            enemies_y = i.ycor()

        # 10 defines how close player/pacman needs to get to pellet to register a collision
        # 10 plays role as collision radius: higher values = collisions from farther way.
        # smaller values mean player has to get very close to pellet for it to go away.
            if abs(player_x - enemies_x) < 10 and abs(player_y - enemies_y) < 10:
                #self.enemies.hideturtle()
                print("Boom!")
                self.placeEnemyRandomly(i)

        self.screen.ontimer(self.checkCollisions, 250)
        return self.enemyList
def main():
    game = Game()
    game.play()

if __name__ == '__main__':
    main()


