import turtle as t 
import time


turt = t.Turtle()
screen = t.Screen()

width=800
height=800
bgColor='black'
# Set the screen's height, width, and color based on the parameters
screen.bgcolor(bgColor)
screen.screensize(width,height)
# Turn the screen's tracer off.
screen.tracer(False)
turt.hideturtle()

def text():
    t.pencolor("white")
    style = ('Courier', 30, 'italic')
    t.write("GAME START", True, align="center",font=style)
    t.penup()
    t.goto(0,-100)
    t.pendown()
    t.color('yellow')
    style2 = ('Arial', 10, 'normal')
    t.write("The goal of this game is to arrive at point z with the highest score. Good Luck!", True, align="center",font=style2)
    t.penup()
    t.goto(0,-120)
    t.pendown()
    style3 = ('Arial', 10, 'italic')
    t.color('magenta')
    t.write("Game Starting in 5 seconds...", True, align="center",font=style3)

    time.sleep(5)
    t.clearscreen()


if __name__ == '__main__':
    text()   