from PyPil.Polinomials.PolyRoot import PolyRoot


def EQ3p (Polynomial):
    # Check parameters
    if not isinstance(Polynomial, list):
        if not all(isinstance(e, (int, float)) for e in Polynomial):
            raise TypeError("Unexpected parameter.")
        raise TypeError("Unexpected parameter.")
    if len(Polynomial) < 3:
        raise TypeError("Unexpected parameter.")
    if Polynomial[-1] == 0:
        raise TypeError("Unexpected parameter")

    numLen = 0
    for e in Polynomial:
        if e != 0:
            numLen += 1

    if numLen == 2:
        complexNum = pow((Polynomial[0] * -1) / Polynomial[-1], 1/(len(Polynomial) - 2))
        return complexNum.real
    if numLen >= 3:
        return PolyRoot(Polynomial)
