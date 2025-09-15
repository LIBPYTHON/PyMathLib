from PyPil.Polinomials.multiplication import multiplication
from PyPil.Polinomials.subtraction import subtraction


def generalAlgorithm(polynomial1, polynomial2):
    # Check parameters
    if not isinstance(polynomial1, list) or not isinstance(polynomial2, list):
        raise TypeError("Unexpected parameter.")
    if not all(isinstance(e, (int, float)) for e in polynomial1) or not all(
            isinstance(e, (int, float)) for e in polynomial2):
        raise TypeError("Unexpected parameter.")

    coefficient = []
    rest = []

    # Itinerar 1 vez
    for i in range(0, len(polynomial1) - len(polynomial2)):
        coefficient.append(0)
    coefficient.insert(len(polynomial1) - len(polynomial2), polynomial1[-1] / polynomial2[-1])
    rest = multiplication(polynomial2, coefficient)
    rest = subtraction(polynomial1, rest)

    coeIndex = len(polynomial1) - len(polynomial2) - 1
    while coeIndex >= 0:
        isnt0rest = 0
        for e in rest:
            if e != 0:
                isnt0rest = e
        coefficient[coeIndex] = isnt0rest / polynomial2[-1]

        tempRest = [coefficient[coeIndex]]
        for i in range (0, coeIndex):
            tempRest.insert(0, 0)
        tempRest = multiplication(tempRest, polynomial2)
        rest = subtraction(rest, tempRest)
        coeIndex += -1
    lenRest = len(rest) - 1
    for e in reversed(rest):
        if e == 0:
            rest.pop(lenRest)
            lenRest += -1
        else:
            break
    return coefficient, rest