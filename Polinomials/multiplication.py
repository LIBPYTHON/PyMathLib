def multiplication (polynomial1, polynomial2):
    # Check Param
    if (not isinstance(polynomial1, (list, int, float)) or not isinstance(polynomial2, list)) and (not isinstance(polynomial2, (list, int, float)) or not isinstance(polynomial1, list)):
        raise TypeError("Unexpected parameter.")
    if not polynomial1 or not polynomial2:
        return 0
    if isinstance(polynomial1, list):
        if not all(isinstance(e, (int, float)) for e in polynomial1):
            raise TypeError("Unexpected parameter.")
    if isinstance(polynomial2, list):
        if not all(isinstance(e, (int, float)) for e in polynomial2):
            raise TypeError("Unexpected parameter.")

    finalPol = []
    if isinstance(polynomial1, list) and isinstance(polynomial2, (int, float)) or isinstance(polynomial2, list) and isinstance(polynomial1, (int, float)):
        if isinstance(polynomial2, (float, int)):
            for e in polynomial1:
                finalPol.append(e * polynomial2)
        else:
            for e in polynomial2:
                finalPol.append(e * polynomial1)
    else:
        ie1 = -1
        for e1 in polynomial1:
            ie1 += 1
            ie2 = -1
            for e2 in polynomial2:
                try:
                    ie2 += 1
                    finalPol[ie1 + ie2] = (e1 * e2) + finalPol[ie1 + ie2]
                except:
                    finalPol.insert(ie1 + ie2, e1 * e2)
    return finalPol