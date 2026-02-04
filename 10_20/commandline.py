'''lecture_17.py
    animation with dictionary
    Hannen Wolfe
    CS151 Visual Media, Fall 2021
'''
import time
import random
import graphics as gr
import sys

def init_circles(number,color):
	shapes = {}
	for i in range(int(number)):
		ball = gr.Circle(gr.Point(250,200), 15)
		ball.setFill(color)
		dx = 1.5+(i*.1)
		dy = .67+(i*.1)
		shapes[ball] = [dx,dy]
	return shapes

def animate(ball, winW, winH, direction):
	centerX = ball.getCenter().getX()
	centerY = ball.getCenter().getY()

	if centerX > winW or centerX < 0:
		direction[0] = -direction[0]

	if centerY > winH or centerY < 0:
		direction[1] = -direction[1]

	ball.move(direction[0], direction[1])
	return direction


def main(number,color):
	winW, winH =500, 500
	win = gr.GraphWin('animation', winW, winH, False)
	
	#init circles
	shapes = init_circles(number,color)

	#draw circles
	for ball in shapes:
		ball.draw(win)

	while True:
		time.sleep(0.01)
		#animate circles
		for key in shapes:
			shapes[key] = animate(key,winW,winH,shapes[key])

		win.update()
		if win.checkMouse():
			break
			
	win.close()


if __name__ == '__main__':
	number=10
	color='blue'
	print(sys.argv)
	if len(sys.argv)<2:
		print("This program takes 2 arguments, an int for number and a string for color")
		main(number,color)
	else:
		main(eval(sys.argv[1]),sys.argv[2])
