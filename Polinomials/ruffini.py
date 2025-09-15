def ruffini(polynomial, independentTerm):  # Brain is not braining
    # Check parameters
    if not isinstance(polynomial, list) or not isinstance(independentTerm, (int, float)):
        raise TypeError("Unexpected parameter.")
    if not all(isinstance(e, (int, float)) for e in polynomial):
        raise TypeError("Unexpected parameter.")
    if not polynomial:
        raise TypeError("Unexpected parameter.")

    finalPol = []
    lastDigit = 0
    for e in reversed(polynomial):
        finalPol.append(e + lastDigit)
        lastDigit = finalPol[-1] * independentTerm
    rest = finalPol[-1]
    finalPol.pop(-1)

    toReturn = []
    for i in range(0, len(finalPol)):
        pointer = (i - len(finalPol) + 1) * -1
        toReturn.append(finalPol[pointer])
    return toReturn, rest