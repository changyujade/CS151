import graphics as gr
import display as d 
import sys

def main(filename):
    myImage = gr.Image(gr.Point(0, 0), filename)
    win=d.displayImage(myImage,"foliage")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main(sys.argv[1])
    