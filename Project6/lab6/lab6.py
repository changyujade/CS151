import graphics as gr
import sys

def main(filename):
    myImage= gr.Image(gr.Point(0,0),filename)
    winH=myImage.getHeight()
    winW=myImage.getWidth()
    win=gr.GraphWin("Maine", winW,winH, False)
    myImage.move(winW/2,winH/2)
    myImage.draw(win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    if (len(sys.argv)>1):
        main(sys.argv[1])
    else:
        main("maine.ppm")
