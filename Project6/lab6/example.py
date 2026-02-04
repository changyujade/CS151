'''zelle-example.py
    Create a Zelle Image with random RGB values
    Hannah Wolfe
    CS151 Visual Media, Spring 2020
'''

import graphics
import random
import display

def main():
    myImage = graphics.Image(graphics.Point(0, 0), 'miller.ppm')
    rainbowImage = myImage.clone()#graphics.Image(graphics.Point(0, 0), 512,512)

    for row in range(rainbowImage.getWidth()):
        for col in range(rainbowImage.getHeight()):
            color = myImage.getPixel(row,col)
            print(myImage.getPixel(row,col))
            randR = (random.randint(0, 255) +color[0])//2
            randG = (random.randint(0, 255) +color[1])//2
            randB = (random.randint(0, 255) +color[2])//2
            rainbowImage.setPixel(row, col, graphics.color_rgb(randR,randB,randG))

    window = display.displayImage(rainbowImage, "Here is our rainbow image!")
    # display image until we get a mouse click
    window.getMouse()



if __name__ == '__main__':
    main()