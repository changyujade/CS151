'''test_checkerboard.py
Test out color fill symbols { and } in TurtleInterpreter
Bruce Maxwell and Oliver W. Layton
CS151: Computational Thinking: Visual Media
- Revised for Spring 2013
- Tested for Python 3 Fall 2017
- Tweaked for Fall 2020
'''
import turtle_interpreter2_copy as turtle_interpreter
import random


def main():
    """ draw a 4x4 checkerboard of alternating filled and unfilled squares """
    terp = turtle_interpreter.TurtleInterpreter(width=400, height=400)

    square = 'F-F-F-F-'
    fsquare = '{F-F-F-F-}'

    for i in range(4):
        for j in range(4):
            terp.goto(-100 + j*50, -100 + i*50)
            terp.setColor((random.random(), random.random(), random.random()))
            if (j + (i % 2)) % 2 == 0:
                terp.drawString(square, 40, 90)
            else:
                terp.drawString(fsquare, 40, 90)

    terp.hold()


if __name__ == "__main__":
    main()
