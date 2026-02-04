from graphics import *
import compound_shapes as cs

cs.road()
cs.circle_shape_init2(100,400,2)
cs.circle_shape_init2(300,400,2)
for i in range(0,200,20):
    cs.rectangle_init(10+i,200,2)

cs.win.getMouse() # pause for click in window
cs.win.close()