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
        if int(r)>=200 and int(g)>=200:
            v.append('🟨')
        elif int(g)>=175:
            v.append('🟩')
        elif int(b)>=145:
            v.append('🟦')
        else:
            v.append('⬜️')
    v.append('\n')
j="".join(v)
print(j)

f=open("emoji_art.txt",'w')
f.write(j)
f.close()

