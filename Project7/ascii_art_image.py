'''
Jade Chang
CS 151
ASCII Art Image
'''


import graphics as gr


string=''
myImage = gr.Image(gr.Point(0, 0), 'exotic.ppm')
for x in range(myImage.getWidth()):
    for y in range(myImage.getHeight()):
        (r, g, b) = myImage.getPixel(x,y)
        #the if statements calculated the gradient of the pixel and designated a charcter, then add it to the string
        if int(r+g+b)/3 <=25:
            string += '#'
        elif int(r+g+b)/3 <= 75:
            string += '@'
        
        elif int(r+g+b)/3 <= 128:
            string += '1'
        else:
            string += '0'
    string +='\n'
f=open("ascii_art2.txt",'w')
f.write(string)
f.close()

