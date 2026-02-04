'''test_square.py
Tests the `Square` subclass of `Shape`
Oliver W. Layton
CS151: Computational Thinking: Visual Media
Fall 2020
'''
import shapes


def testSquare():
    squareLeft = shapes.Pentagon(color='blue', fill=False)
    squareRight = shapes.Square(color='red', fill=True)

    squareLeft.draw(-200, 0)
    squareRight.draw(200, 0)

    squareLeft.getTI().hold()


if __name__ == '__main__':
    testSquare()
