import sys
from curve import *

curves = {'gilbert': GilbertCurve(),
          'gosper': GosperCurve(),
          'segment': Segment32Curve()
          }

if(__name__ == '__main__'):
    # returns list of available curves
    if(len(sys.argv) == 2 and sys.argv[1] == 'list'):
        for key in curves:
            print(key)
    else:
        t.speed(100)
        t.shapesize(0.001)
        if(len(sys.argv) == 3):
            allowDraw = True
            try:
                currentCurve = curves[sys.argv[1]]
            except KeyError:
                print(
                    "Incorrect curve type. Check available type list use a 'run.py list'")
                allowDraw = False
            try:
                currentLevel = int(sys.argv[2])
                if(currentLevel > 7):
                    currentLevel = 7
                if(currentLevel < 0):
                    currentLevel = 0
            except ValueError:
                print("Level must be a number")
                allowDraw = False

            if(allowDraw):
                currentCurve.Draw(currentLevel)
                t.done()
