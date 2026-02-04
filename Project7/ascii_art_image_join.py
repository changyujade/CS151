'''
Jade Chang
CS 151
ASCII Art Image
'''


import graphics as gr


v=[]
myImage = gr.Image(gr.Point(0, 0), 'exotic.ppm')
for x in range(myImage.getWidth()):
    for y in range(myImage.getHeight()):
        (r, g, b) = myImage.getPixel(x,y)
        if int(r+g+b)/3 <=75:
            v.append('0')
        elif int(r+g+b)/3 <=125:
            v.append('#')
        else:
            v.append('1')
    v.append('\n')
j="".join(v)
print(j)

f=open("ascii_art3.txt",'w')
f.write(j)
f.close()

