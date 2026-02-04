import shapes

def tile(x=-50, y=1, scale=1.0):
    for j in range(5):
        scale = scale - 0.1
        square = shapes.Square(100*scale,color='blue', fill=False)
        square.draw(x+j*5,y-j*5)
    #square.getTI().hold()
    return square

def mosaic(x, y, scale, Nx, Ny):
    for i in range(Nx):
        for j in range(Ny):
            square = tile(x+j*100*scale,y+i*100*scale,scale)
    square.getTI().hold()

mosaic(-200,-100,1,5,4)