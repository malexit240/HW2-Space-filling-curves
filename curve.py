import turtle as t
from L_System import *


class Curve:
    """Abstract class of curve"""

    def __init__(self):
        self.system = LSystem()

    def Draw(self, level: int):
        """Draw curve by level"""
        pass


class GosperCurve(Curve):

    def __init__(self):
        Curve.__init__(self)

        self.system.variables = {'A', 'B'}
        self.system.constants = {'+', '-'}
        self.system.axioma = 'A'
        self.system.rules = {
            'A': 'A-B--B+A++AA+B-',
            'B': '+A-BB--B-A++A+B'
        }

    def Draw(self, level: int):
        """Draw Gosper curve by level"""

        instruction = get_Linstruction(level, self.system)

        distance = 100.0/(2**level)

        for symbol in instruction:
            if(symbol == 'A' or symbol == 'B'):
                t.forward(distance)
            elif(symbol == '-'):
                t.right(60)
            elif(symbol == '+'):
                t.left(60)


class GilbertCurve(Curve):

    def __init__(self):
        Curve.__init__(self)

        self.system.variables = {'A', 'B'}
        self.system.constants = {'F', '+', '-'}
        self.system.axioma = 'A'
        self.system.rules = {
            'A': '-BF+AFA+FB-',
            'B': '+AF-BFB-FA+'
        }

    def Draw(self, level: int):
        """Draw Gilbert curve by level"""
        instruction = get_Linstruction(level, self.system)

        t.penup()
        t.goto(-250, -250)
        t.pendown()
        distance = 400.0/(2**level)

        for symbol in instruction:
            if(symbol == 'F'):
                t.forward(distance)
            elif(symbol == '+'):
                t.right(90)
            elif(symbol == '-'):
                t.left(90)


class Segment32Curve(Curve):

    def __init__(self):
        Curve.__init__(self)

        self.system.variables = {'A'}
        self.system.constants = {'+', '-'}
        self.system.axioma = 'A'
        self.system.rules = {
            'A': '-A+A-A-A+A+AA-A+A+AA+A-A-AA+AA-AA+A+A-AA-A-A+AA-A-A+A+A-A+'
        }

    def Draw(self, level: int):
        """Draw 32-segments curve by level"""

        instruction = get_Linstruction(level, self.system)

        t.penup()
        t.goto(-100, -100)
        t.pendown()
        distance = 20.0/(2**level)

        for symbol in instruction:
            if(symbol == 'A'):
                t.forward(distance)
            elif(symbol == '+'):
                t.right(90)
            elif(symbol == '-'):
                t.left(90)
