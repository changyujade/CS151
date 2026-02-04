import mosaic as m
import turtle_interpreter as t 
import turtle
import random
import time
import intro
#import Game

class Game():

    def __init__(self,distance=2,min_x=-200,min_y=0,max_x=200,max_y=200,score=100):
        
        m.mosaic(-450,-300,1,10,8)
        turt = t.TurtleInterpreter()
        self.lastCollision = time.time()
        self.screen = turt.getScreen()
        self.player = self.makePlayer()
        #can create a second player (reusable for other projects)
        self.goal= self.makeGoal()
        self.distance = distance
        self.min_x=min_x
        self.min_y=min_y
        self.max_x=max_x
        self.max_y=max_y
        self.score=score
        print("Welcome to the Game. Your starting score is",score) #Extention: adding a score system
        self.makeEnemies()
        self.makeObstacles()
        self.setupEvents()


    def setupEvents(self):
        self.screen.onkeypress(self.moveUp,"Up")
        self.screen.onkeypress(self.moveDown,"Down")
        self.screen.onkeypress(self.moveRight,"Right")
        self.screen.onkeypress(self.moveLeft,"Left")

        self.screen.ontimer(self.moveEnemiesRandomly, 50)
        self.screen.ontimer(self.checkCollisions, 250)

    def moveUp(self):
        #moves player up by self.disrance
        self.player.setheading(90)
        self.player.forward(self.distance)
    
    def moveDown(self):
        #moves player up by self.disrance
        self.player.setheading(270)
        self.player.forward(self.distance)

    def moveRight(self):
        #moves player up by self.disrance
        self.player.setheading(0)
        self.player.forward(self.distance)

    def moveLeft(self):
        #moves player up by self.disrance
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
    
    def placeObstacle(self, obstacle,i):
        "Place the obstacles at x, y in the canvas"
        #for i in range(4):
        obstacle.speed(0)
        obstacle.goto(-50+i*100, -100+i*100)
        obstacle.speed(6)

    def makeObstacles(self):

        "Extention: creating obstacles"
        self.obstacleList=[]
        for i in range(4):
            obstacle = turtle.Turtle() 
            obstacle.shape('triangle') 
            self.obstacleList.append(obstacle)
        #for i in self.obstacleList:
            obstacle.penup()
            self.placeObstacle(obstacle,i) 
        return self.obstacleList

    def makeGoal(self):
        goal=turtle.Turtle()
        goal.shape('square')
        goal.penup()
        goal.speed(0)
        goal.goto(-200, 200)
        goal.speed(6)
        return goal


    def moveEnemiesRandomly(self):
        for i in self.enemyList:
            x = random.randint(i.xcor()-10, i.xcor()+10)
            y = random.randint(i.ycor()-10, i.ycor()+10)
            i.goto(x,y) 
            #print(type(self.min_x))
            
            if (i.xcor()<self.min_x or i.xcor()>self.max_x) and (i.ycor()<self.min_y or i.ycor()>self.max_y):
                i.goto(0,0) #keeps the enemies within the given border range
            
            
        self.screen.ontimer(self.moveEnemiesRandomly, 1000)
        return self.enemyList

    def checkCollisions(self):
        '''Checks for whether we have a collision between the player and one of the obstacles or enemies.
        '''

        player_x = self.player.xcor()
        player_y = self.player.ycor()
        for i in self.enemyList:
            enemies_x = i.xcor() 
            enemies_y = i.ycor()
        
        # 10 defines how close player needs to get to pellet to register a collision
        # 10 plays role as collision radius: higher values = collisions from farther way.
        # smaller values mean player has to get very close to enemy for it to go away.
            if abs(player_x - enemies_x) < 10 and abs(player_y - enemies_y) < 10:
                #self.enemies.hideturtle()
                print("Boom!")
                self.score = self.score - 10
                print("your current score is",self.score)
                self.placeEnemyRandomly(i)

        for i in self.obstacleList:
            obstacle_x = i.xcor()
            obstacle_y = i.ycor()

            if abs(player_x - obstacle_x) < 10 and abs(player_y - obstacle_y) < 10 and time.time()-self.lastCollision >1:
                self.lastCollision=time.time()
                print("Ouch!")
                self.score = self.score - 5
                print("your current score is",self.score)
        
        goal_x=self.goal.xcor()
        goal_y=self.goal.ycor()

        if abs(player_x - goal_x) < 10 and abs(player_y - goal_y) < 10 and time.time()-self.lastCollision >1:
                self.lastCollision=time.time()
                print("yay")
                print("You arrived at the goal with the score of",self.score)
                
        if self.score <=0:
            print("You died, Game Over")
            exit()

        self.screen.ontimer(self.checkCollisions, 250)

def main():
    turtle.onkeypress(intro.text(),"Up")
    game = Game()
    game.play()

if __name__ == '__main__':
    intro.text() #Extention: create an intro scene before the game starts
    main()


