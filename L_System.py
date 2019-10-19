class LSystem:
    """L-System"""

    variables = {}
    constants = {}
    axioma = ''
    rules = {}


def get_Linstruction(level: int, system: LSystem):
    """Returns L-instruction by recursion level"""

    oldInstruction = system.axioma
    newInstruction = oldInstruction

    for l in range(level):  # recursion level
        newInstruction = ''

        for symbol in oldInstruction:
            for key in system.variables:  # key of rule
                if(symbol == key):
                    newInstruction += system.rules[key]
                    break
            else:
                newInstruction += symbol
        oldInstruction = newInstruction

    return newInstruction
