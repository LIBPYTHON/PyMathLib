from PyPil.Polinomials.ruffini import ruffini
from PyPil.Polinomials.generalAlgorithm import generalAlgorithm


def division (polynomial1, polynomial2):
    # Check parameters
    if not isinstance(polynomial1, list) or not isinstance(polynomial2, list):
        raise TypeError("Unexpected parameter.")
    if not polynomial1 or not polynomial2 or polynomial2 == 0 or polynomial2 == [0]:
        raise TypeError("Unexpected parameter.")
    if not all(isinstance(e, (int, float)) for e in polynomial1) or not all(isinstance(e, (int, float)) for e in polynomial2):
        raise TypeError("Unexpected parameter.")

    if len(polynomial2) == 2 and polynomial2[1] == 1:
        return ruffini(polynomial1, polynomial2[0] * -1)
    else:
        return generalAlgorithm(polynomial1, polynomial2)