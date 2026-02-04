import graphics as gr
import display as d 
import sys

def test(filename,OtherImg):
    myImage = gr.Image(gr.Point(0, 0), filename)
    ImageTwo= gr.Image(gr.Point(0,0), OtherImg)
    greenScreen(myImage,ImageTwo) #how to get coordinates in range
    win=d.displayImage(myImage,"foliage")
    win.getMouse()
    win.close()

def swapGreenBlue(myImage):
    '''Swaps the green and blue values of every pixel of a Zelle image `img`'''
    for x in range(myImage.getWidth()):
        for y in range(myImage.getHeight()):
            (r, g, b) = myImage.getPixel(x,y)
            myImage.setPixel(x, y, gr.color_rgb(r, b, g))

def accentuateRed(myImage):
    for x in range(myImage.getWidth()):
        for y in range(myImage.getHeight()):
            (r, g, b) = myImage.getPixel(x,y)
            if r<100:
                myImage.setPixel(x, y, gr.color_rgb(r+100, g, b))

def lowContrast(myImage):
    for x in range(myImage.getWidth()):
        for y in range(myImage.getHeight()):
            (r, g, b) = myImage.getPixel(x,y)
            myImage.setPixel(x, y, gr.color_rgb(r//3, g//3, b//3))

def noRed(myImage):
    for x in range(myImage.getWidth()):
        for y in range(myImage.getHeight()):
            (r, g, b) = myImage.getPixel(x,y)
            myImage.setPixel(x, y, gr.color_rgb(r=0, g=g, b=b))

def blackWhite(myImage):
    for x in range(myImage.getWidth()):
        for y in range(myImage.getHeight()):
            (r, g, b) = myImage.getPixel(x,y)
            myImage.setPixel(x, y, gr.color_rgb(round(r*0.3), round(g*0.59), round(b*0.11)))

def greenScreen(greenImg, otherImg):
    '''If a pixel in `greenImg` is very green, replace it with the corresponding pixel in `otherImg`.

    A reasonable test for 'very green' is if the green pixel is 1.5 times the blue channel and also bigger than the red pixel.
    Play around with the 1.5 number to see if you can get better results.
    '''
    for x in range(greenImg.getWidth()):
        for y in range(greenImg.getHeight()):
            (r, g, b) = greenImg.getPixel(x,y)
            if g>1.5*b and g>1.5*r:
                (r, g, b) = otherImg.getPixel(x,y)
                greenImg.setPixel(x, y, gr.color_rgb(r,g,b))


if __name__ == '__main__':
    if len(sys.argv)<2:
        print('Usage: python3 show.py <filename of image>')
        exit()
    else:
        test(sys.argv[1],sys.argv[2])

