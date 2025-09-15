from PyPil.Polinomials.ruffini import ruffini
from PyPil.Equations.EQ2 import EQ2


def PolyRoot (Polynomial):
    # Check parameters
    if not isinstance(Polynomial, list):
        if not all(isinstance(e, (int, float)) for e in Polynomial):
            raise TypeError("Unexpected parameter.")
        raise TypeError("Unexpected parameter.")

    finalRoots = []
    if Polynomial[0] == 0:
        Polynomial.pop(0)
        finalRoots.append(0)

    temp = []
    for e in Polynomial:
        temp.append(e)
    Polynomial = temp


    dividers = []
    Polynomial[0] = int(Polynomial[0])
    for i in range(1, abs(Polynomial[0]) // 2 + 1):
        if Polynomial[0] % i == 0:
            dividers.append(i)
            dividers.append(i * -1)
    dividers.append(Polynomial[0])
    dividers.append(Polynomial[0] * -1)

    finalPol = Polynomial.copy()
    while True:
        if len(finalPol) == 3:
            try:
                x1 = EQ2(finalPol)[0]
                x2 = EQ2(finalPol)[1]
                finalRoots.append(x1)
                finalRoots.append(x2)
                break
            except:
                finalRoots.append(finalPol)
                break
        else:
            found = False
            for e in dividers:
                tempPol = ruffini(finalPol, e)[0]
                rest = ruffini(finalPol, e)[1]
                if rest == 0:
                    finalRoots.append(e)
                    finalPol = tempPol
                    found = True
                    break
            if not found:
                finalRoots.append(finalPol)
                break

    toReturn = []
    for e in finalRoots:
        toReturn.append(float(e))
    return list(set(toReturn))