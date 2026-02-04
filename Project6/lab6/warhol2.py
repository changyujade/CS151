import graphics as gr
import display as d 
import sys
import filters as f 


def placeImageInCanvas(canvas, myImage , topleft_x,topleft_y):

    '''Place the image `img` into the larger canvas `canvas`. The image `img` should be positioned
    so that its top-left corner appears at (row , col) = (topleft_row, topleft_col) in the large canvas.
    NOTE: (0, 0) is the top-left corner.

    Parameters:
    -----------
    canvas: Image. Larger canvas to place the image on.
    img: Image. Image to be placed on the canvas.
    topleft_x: int. x pixel position (column) in `canvas` where the top-left corner of `img` should go
    topleft_y: int. y pixel position (row) in `canvas` where the top-left corner of `img` should go
    '''
    #pass    

    for x in range(myImage.getWidth()):
        for y in range(myImage.getHeight()):
            (r, g, b) = myImage.getPixel(x,y)
            canvas.setPixel(x+topleft_x,y+topleft_y, gr.color_rgb(r, g, b))

if __name__ == '__main__':
    myImage=gr.Image(gr.Point(0, 0), 'foliage.ppm')
    canvas = gr.Image(gr.Point(0,0),(myImage.getWidth())*3, (myImage.getHeight())*3)
    imageList = [[0, 0, 'original', myImage],[myImage.getWidth(), 0, 'swapGreenBlue', myImage],[0, myImage.getHeight(), 'accentuateRed', myImage],[myImage.getWidth(), myImage.getHeight(), 'blackWhite', myImage],[myImage.getWidth()*2, 0, 'blackWhite', myImage],[0, myImage.getHeight()*2, 'blackWhite', myImage]]
    for i in imageList:
        print(type(i[3]))
        cImage=i[3].clone()
        if i[2]=='swapGreenBlue':
            f.swapGreenBlue(cImage)
        elif i[2]=='accentuateRed':
            f.accentuateRed(cImage)
        elif i[2]=="blackWhite":
            f.blackWhite(cImage)
        placeImageInCanvas(canvas,cImage,i[0],i[1])
    print('displayImage')
    win=d.displayImage(canvas,"warhol")
    print('done')
    win.getMouse()
    win.close()